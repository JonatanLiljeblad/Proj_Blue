# app/main.py
from fastapi import FastAPI
from .database import engine, Base
from .routers import auth, users, data

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(Title="Smart Insight Dashboard API", version="0.0.1")

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(data.router, prefix="/data", tags=["data"])