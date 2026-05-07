from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate

def get_all_users(db: Session):
    return db.query(User).all()

def get_users_by_name(db: Session, name: str):
    return db.query(User).filter(User.name.ilike(f"{name}%")).all()

def search_users(db: Session, query: str):
    return db.query(User).filter(
        (User.name.ilike(f"{query}%")) | (User.email.ilike(f"%{query}%"))
    ).all()

def create_user(db: Session, user_in: UserCreate):
    db_user = User(
        name=user_in.name,
        email=user_in.email,
        results=user_in.results
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
