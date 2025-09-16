from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, database
from ..jwt import create_access_token
from passlib.context import CryptContext
import bcrypt

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.get("/")
def auth_test():
    return {"message": "Auth route working!"}

@router.post("/signup", response_model=schemas.UserOut)
def signup(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    db_user = db.query(models.User).filter(
    (models.User.email == user.email) | (models.User.username == user.username)).first()
    if db_user:
        raise HTTPException(
            status_code=400,
            detail="Username or email already registered"
        )
    
    # Hash the password properly
    hashed_password = bcrypt.hashpw(user.password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    new_user = models.User(
        username=user.username, 
        email=user.email, 
        hashed_password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(database.get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if not db_user or not pwd_context.verify(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    token = create_access_token({"user_id": db_user.id})
    return {"access_token": token, "token_type": "bearer"}