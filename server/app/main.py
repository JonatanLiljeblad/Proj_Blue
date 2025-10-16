# app/main.py
from fastapi import FastAPI
from .routers import auth, users, data
from . import models, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(Title="Smart Insight Dashboard API", version="0.0.1")

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(data.router, prefix="/data", tags=["Data"])