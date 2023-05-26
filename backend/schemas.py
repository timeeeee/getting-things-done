from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class InItemBase(BaseModel):
    description: str


class InItemCreate(InItemBase):
    pass


class InItem(InItemBase):
    id: int
    created_at: datetime
    processed_at: Optional[datetime]

    class Config:
        orm_mode = True
