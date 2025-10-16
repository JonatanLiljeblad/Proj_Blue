from sqlalchemy.orm import Session
from . import models
from .utils import verify_password  # assuming you already have hashing/verify in utils.py

def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user:
        print(f"[AUTH] User not found: {email}")
        return None
    if not verify_password(password, user.hashed_password):
        print(f"[AUTH] Password mismatch for: {email}")
        return None
    return user