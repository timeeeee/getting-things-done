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


def update_in_item(db: Session, in_item_id: int, in_item: schemas.InItemUpdate):
    """
    For now this will raise a ValueError if the id doesn't refer to an existing in-item
    """
    db_item = db.query(models.InItem).filter(models.InItem.id == in_item_id).first()
    if db_item is None:
        raise ValueError(f"no in-item with id {in_item_id}")

    for key, value in in_item.dict().items():
        setattr(db_item, key, value)

    db.commit()

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


def update_project(db: Session, project_id: int, project: schemas.ProjectPut):
    db_item = db.query(models.Project).filter(models.Project.id == project_id).first()
    if db_item is None:
        raise ValueError(f"no project with id {project_id}")

    for key, value in project.dict().items():
        setattr(db_item, key, value)

    db.commit()
