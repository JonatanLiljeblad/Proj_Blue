from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def data_test():
    return {"message": "Data route working!"}