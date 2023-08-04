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


def delete_in_item(db: Session, in_item_id: int):
    """
    For now, raise a ValueError if the item doesn't exist
    """
    db_item = db.query(models.InItem).filter(models.InItem.id == in_item_id)
    if db_item is None:
        raise ValueError(f"no in-item with id {in_item_id}")

    db_item.delete()
    db.commit()
