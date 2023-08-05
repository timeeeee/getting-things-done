from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from models import BucketEnum

class InItemBase(BaseModel):
    description: str


class InItemCreate(InItemBase):
    pass


class InItemRead(InItemBase):
    id: int
    created_at: datetime
    processed_at: Optional[datetime]

    # I'm not sure why to do this. seems like otherwise pydantic tries
    # to convert the object to a dict?
    class Config:
        orm_mode = True


class InItemUpdate(InItemBase):
    processed_at: Optional[datetime]


# do I need a schema for deleting this?


class ProjectBase(BaseModel):
    name: str
    notes: Optional[str]
    bucket: BucketEnum
    next_step: Optional[str]


class ProjectRead(ProjectBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(ProjectBase):
    pass
