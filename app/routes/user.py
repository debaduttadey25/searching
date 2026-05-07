from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services import user_service

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=List[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    """Fetch all users from the database"""
    return user_service.get_all_users(db)

@router.get("/name/{name}", response_model=List[UserResponse])
def get_users_by_name(name: str, db: Session = Depends(get_db)):
    """Fetch users matching a specific name"""
    users = user_service.get_users_by_name(db, name=name)
    if not users:
        raise HTTPException(status_code=404, detail="No users found with this name")
    return users

@router.get("/search/", response_model=List[UserResponse])
def search_users(query: str, db: Session = Depends(get_db)):
    """Search users by name or email"""
    return user_service.search_users(db, query=query)

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """Create a new user"""
    return user_service.create_user(db, user_in=user)
