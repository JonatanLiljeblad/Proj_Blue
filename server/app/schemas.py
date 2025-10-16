from pydantic import BaseModel

# For signup
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

# For login (JSON)
class UserLogin(BaseModel):
    email: str
    password: str

# For output (omit password)
class UserOut(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        from_attributes = True