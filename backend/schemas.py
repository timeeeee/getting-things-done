from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from models import BucketEnum

class InItemBase(BaseModel):
    description: str


class InItemCreate(InItemBase):
    pass


class InItemPut(InItemBase):
    pass


class InItem(InItemBase):
    id: int
    created_at: datetime
    processed_at: Optional[datetime]

    class Config:
        orm_mode = True


class ProjectBase(BaseModel):
    name: str
    notes: str
    bucket: BucketEnum
    next_step: str


class ProjectCreate(ProjectBase):
    pass


class ProjectPut(ProjectBase):
    pass


class Project(ProjectBase):
    id: int
    created_at: datetime
    updated_at: datetime
