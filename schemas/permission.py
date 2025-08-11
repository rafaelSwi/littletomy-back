from pydantic import BaseModel, constr
from typing import Optional


class PermissionBase(BaseModel):
    name: constr(max_length=64)


class PermissionCreate(PermissionBase):
    pass


class PermissionUpdate(BaseModel):
    name: Optional[constr(max_length=64)] = None


class PermissionResponse(PermissionBase):
    id: int

    class Config:
        from_attributes = True