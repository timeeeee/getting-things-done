from crud import in_items
import schemas
import models


def add_test_data(db):
    # add fixtures
    in_items.create_in_item(db, schemas.InItemCreate(description="this is an in item"))
    in_items.create_in_item(db, schemas.InItemCreate(description="this is another item"))

    
