from datetime import datetime

from pydantic import BaseModel


class StuffBase(BaseModel):
    id: int
    description: str


class StuffCreate(StuffBase):
    pass


class Stuff(StuffBase):
    id: int
    created_at: datetime
    processed_at: datetime

    class Config:
        orm_mode = True
