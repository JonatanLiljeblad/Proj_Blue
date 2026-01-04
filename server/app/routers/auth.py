from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import timedelta

from .. import models, schemas, database, oauth2, crud
from ..utils import hash_password

router = APIRouter(tags=["Auth"])


@router.get("/")
def auth_test():
    return {"message": "Auth route working!"}


# ----------------- SIGNUP -----------------
@router.post("/signup", response_model=schemas.UserOut)
def signup(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    # Check if user/email already exists
    db_user = db.query(models.User).filter(
        (models.User.email == user.email) | (models.User.username == user.username)
    ).first()
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username or email already registered"
        )

    # Hash password
    hashed_password = hash_password(user.password)

    new_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# ----------------- LOGIN -----------------
@router.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(database.get_db)):
    # Authenticate user
    user_db = crud.authenticate_user(db, user.email, user.password)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    # Create JWT
    access_token_expires = timedelta(minutes=oauth2.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = oauth2.create_access_token(
        data={"user_id": user_db.id},
        expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}