from typing import Union, List

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
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

@app.get("/", include_in_schema=False)
def docs_redirect():
    return RedirectResponse(url='/docs')


@app.get("/in-items/", response_model=List[schemas.InItem])
def list_in_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    in_item_list = crud.get_in_item_list(db, skip=skip, limit=limit)
    return in_item_list


@app.get("/in-items/{in_item_id}")
def read_in_item(in_item_id: int, db: Session = Depends(get_db)):
    print(f"fetching in-item with id {in_item_id}")
    in_item = crud.get_in_item(db, in_item_id)
    print(f"found {in_item}")
    if in_item is None:
        raise HTTPException(status_code=404, detail="In Item not found")

    return in_item


@app.post("/in-items/", response_model=schemas.InItem)
def create_in_item(in_item: schemas.InItemCreate, db: Session = Depends(get_db)):
    result = crud.create_in_item(db, in_item)
    return result


@app.get("/projects/")
def list_projects(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_project_list(db, skip=skip, limit=limit)


@app.get("/projects/{project_id}")
def read_project(project_id: int, db: Session = Depends(get_db)):
    project = crud.get_project(db, project_id)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")

    return project

@app.post("/projects/")
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    result = crud.create_project(db, project)
    return result



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
