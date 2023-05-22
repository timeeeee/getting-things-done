from typing import Union

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from database import SessionLocal
import crud
import models
import schemas

app = FastAPI()


# dependency (https://fastapi.tiangolo.com/tutorial/sql-databases/)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


origins = [
    "http://localhost:3000",
    "http://localhost:8000",
    "http://localhost"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/stuff/")
def list_stuff(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    stuff_list = crud.get_stuff_list(db, skip=skip, limit=limit)
    return stuff_list


@app.get("/stuff/{stuff_id}")
def read_stuff(stuff_id: int, db: Session = Depends(get_db)):
    stuff = crud.get_stuff(db, stuff_id)
    if stuff is None:
        raise HTTPException(status_code=404, detail="Stuff not found")

    return stuff

"""
@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
"""
