from pydantic import BaseModel, constr
from datetime import datetime
from typing import Optional


class TextTabPreferencesBase(BaseModel):
    created: Optional[datetime] = None
    password_hash: Optional[constr(max_length=60)] = None
    public: Optional[bool] = True


class TextTabPreferencesCreate(TextTabPreferencesBase):
    pass


class TextTabPreferencesUpdate(TextTabPreferencesBase):
    pass


class TextTabPreferencesResponse(TextTabPreferencesBase):
    id: int

    class Config:
        from_attributes = True