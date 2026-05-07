from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    email: str
    results: int

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    

    class Config:
        from_attributes = True
