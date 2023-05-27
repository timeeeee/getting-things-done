from sqlalchemy.orm import Session

import models
import schemas


def get_in_item(db: Session, in_item_id: int):
    return db.query(models.InItem).filter(models.InItem.id == in_item_id).first()


def get_in_item_list(db: Session, skip: int=0, limit: int=100):
    return db.query(models.InItem).offset(skip).limit(limit).all()


def create_in_item(db: Session, in_item: schemas.InItemCreate):
    db_item = models.InItem(description=in_item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


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