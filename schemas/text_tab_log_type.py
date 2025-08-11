from pydantic import BaseModel, constr
from typing import Optional


class TextTabLogTypeBase(BaseModel):
    value: constr(max_length=16)


class TextTabLogTypeCreate(TextTabLogTypeBase):
    pass


class TextTabLogTypeUpdate(BaseModel):
    value: Optional[constr(max_length=16)] = None


class TextTabLogTypeResponse(TextTabLogTypeBase):
    id: int

    class Config:
        from_attributes = True