import enum

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Text, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base

# these should be pretty much static!
class BucketEnum(enum.Enum):
    trash = 0
    maybe = 1
    active = 2
    complete = 3


class InItem(Base):
    __tablename__ = "in_item"

    id = Column(Integer, primary_key=True)
    description = Column(String(200), nullable=False)
    created_at = Column(DateTime, server_default=func.Now())
    processed_at = Column(DateTime)

    # when this is processed, the item could go in the trash/maybe, *or* it could become
    # associated with a project (which in turn has a bucket)
    


class Project(Base):
    __tablename__ = "project"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    notes = Column(Text)
    bucket = Column(Enum(BucketEnum), nullable=False)
    next_step = Column(String(200))
    created_at = Column(DateTime, server_default=func.Now())
    updated_at = Column(DateTime, onupdate=func.Now())


"""
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    # email = Column(String, unique=True, index=True)
    # hashed_password = Column(String)
    # is_active = Column(Boolean, default=True)
    username = Column(String(50), nullable=False)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
"""
