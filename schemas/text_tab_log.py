from pydantic import BaseModel, constr
from datetime import datetime
from typing import Optional


class TextTabLogBase(BaseModel):
    user_id: Optional[int] = None
    date: Optional[datetime] = None
    type_id: Optional[int] = None
    ip_address: Optional[constr(max_length=45)] = None


class TextTabLogCreate(TextTabLogBase):
    pass


class TextTabLogUpdate(TextTabLogBase):
    pass


class TextTabLogResponse(TextTabLogBase):
    id: int

    class Config:
        from_attributes = True