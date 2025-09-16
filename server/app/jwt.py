from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = "your_super_secret_key_here"  # replace with a strong random key
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60  # token lasts 1 hour

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt