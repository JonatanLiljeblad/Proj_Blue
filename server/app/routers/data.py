from fastapi import APIRouter, Depends
from .. import schemas
from ..oauth2 import get_current_user

router = APIRouter(
    tags=["Data"]
)

@router.get("/protected")
def read_protected(current_user: schemas.UserOut = Depends(get_current_user)):
    return {"message": f"Hello {current_user.username}, your email is {current_user.email}"}

@router.get("/")
def data_test():
    return {"message": "Data route working!"}