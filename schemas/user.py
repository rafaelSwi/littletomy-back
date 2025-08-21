from typing import Optional, List
from pydantic import BaseModel, EmailStr, constr


class UserBase(BaseModel):
    username: constr(max_length=64)
    email_address: Optional[EmailStr] = None


class UserCreate(UserBase):
    username: constr(max_length=64)
    email_address: Optional[EmailStr] = None
    password: constr(max_length=32)


class UserUpdate(BaseModel):
    username: Optional[constr(max_length=64)] = None
    email_address: Optional[EmailStr] = None
    password_hash: Optional[constr(max_length=60)] = None


class UserPublic(BaseModel):
    username: constr(max_length=64)
    id: int


class UserResponse(UserBase):
    id: int
    permissions: List[str] = []

    class Config:
        from_attributes = True