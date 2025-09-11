from fastapi import APIRouter

router = APIRouter()  # <-- this is what FastAPI is looking for

@router.get("/")
def read_users():
    return {"message": "Users route working!"}