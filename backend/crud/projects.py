from sqlalchemy.orm import Session

import models
import schemas


def get_project(db: Session, project_id: int):
    return db.query(models.Project).filter(models.Project.id == project_id).first()


def get_project_list(db: Session, skip: int=0, limit: int=100):
    # todo: only return list of ids here?
    return db.query(models.Project)


def create_project(db: Session, project: schemas.ProjectCreate):
    db_project = models.Project(**project.dict())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project


def update_project(db: Session, project_id: int, project: schemas.ProjectPut):
    db_item = db.query(models.Project).filter(models.Project.id == project_id).first()
    if db_item is None:
        raise ValueError(f"no project with id {project_id}")

    for key, value in project.dict().items():
        setattr(db_item, key, value)

    db.commit()
