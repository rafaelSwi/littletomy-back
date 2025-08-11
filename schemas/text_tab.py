from pydantic import BaseModel, constr
from typing import Optional, List


class TextTabBase(BaseModel):
    content: Optional[str] = None
    title: constr(max_length=32)
    user_id: Optional[int] = None
    preferences_id: Optional[int] = None


class TextTabCreate(TextTabBase):
    pass


class TextTabUpdate(BaseModel):
    content: Optional[str] = None
    title: Optional[constr(max_length=32)] = None
    user_id: Optional[int] = None
    preferences_id: Optional[int] = None


class TextTabResponse(TextTabBase):
    id: int
    logs: List[int] = []  # ids

    class Config:
        from_attributes = True