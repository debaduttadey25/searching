from sqlalchemy import Column, Integer, String, Text
from app.core.database import Base

class User(Base):
    __tablename__ = "test"

 
    name = Column(String(255), primary_key=True, index=True)
    email = Column(String(255), index=True)
    results = Column(Integer)
