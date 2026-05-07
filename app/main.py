from fastapi import FastAPI
from app.core.database import engine, Base
from app.routes import user

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router)

@app.get("/")
def home():
    return {
        "message": "FastAPI Production Server Running"
    }