import crud
import schemas
import models


def add_test_data(db):
    items = [
        schemas.InItemCreate(description="this is an in item"),
        schemas.InItemCreate(description="this is another item"),
    ]

    for item in items:
        crud.in_items.create_in_item(db, item)

    projects = [
        schemas.ProjectCreate(
            name="Getting Things Done website",
            notes="fastapi back-end, react front-end",
            bucket=models.BucketEnum.active,
            next_step="test"
        ),
        schemas.ProjectCreate(
            name="Apply for jobs",
            bucket=models.BucketEnum.active,
            next_step="sign up on tutoring website"
        ),
        schemas.ProjectCreate(
            name="The Contraption",
            bucket=models.BucketEnum.complete
        ),
    ]

    for project in projects:
        crud.projects.create_project(db, project)
