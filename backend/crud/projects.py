from sqlalchemy.orm import Session

import models
import schemas


def get_project(db: Session, project_id: int):
    return db.query(models.Project).filter(models.Project.id == project_id).first()


def get_project_list(db: Session, skip: int=0, limit: int=100):
    # todo: only return list of ids here?
    return db.query(models.Project).offset(skip).limit(limit).all()


def create_project(db: Session, project: schemas.ProjectCreate):
    db_project = models.Project(**project.dict())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project


def update_project(db: Session, project_id: int, project: schemas.ProjectUpdate):
    db_project = db.query(models.Project).filter(models.Project.id == project_id).first()
    if db_project is None:
        raise ValueError(f"no project with id {project_id}")

    for key, value in project.dict().items():
        setattr(db_project, key, value)

    db.commit()

    return db_project


def delete_project(db: Session, project_id: int):
    db_project = db.query(models.Project).filter(models.Project.id == project_id)
    if db_project is None:
        raise ValueError(f"no project with id {project_id}")

    db_project.delete()
    db.commit()
