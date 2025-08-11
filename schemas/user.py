from typing import Optional, List
from pydantic import BaseModel, EmailStr, constr


class UserBase(BaseModel):
    username: constr(max_length=64)
    email_address: Optional[EmailStr] = None


class UserCreate(UserBase):
    password_hash: constr(max_length=60)


class UserUpdate(BaseModel):
    username: Optional[constr(max_length=64)] = None
    email_address: Optional[EmailStr] = None
    password_hash: Optional[constr(max_length=60)] = None


class UserResponse(UserBase):
    id: int
    permissions: List[str] = []

    class Config:
        from_attributes = True