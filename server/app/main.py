# app/main.py
from fastapi import FastAPI
from .routers import auth, users, data
from . import models, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Smart Insight Dashboard API", version="0.0.1")

# Root endpoint for health check
@app.get("/")
def root():
    return {"status": "healthy", "message": "Smart Insight Dashboard API is running"}

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(data.router, prefix="/data", tags=["Data"])