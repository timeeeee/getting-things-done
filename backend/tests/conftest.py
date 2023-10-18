import os

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from main import app, get_db
from database import Base
from tests.fixtures import add_test_data

engine = create_engine(os.environ[TEST_DB_URL])
TestingSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    try:
        db = TestingSession()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


"""
# I think I don't need this, with that "finally" in the test_client fixture
@pytest.fixture(scope="session")
def clean_up_old_test_db():
    Base.metadata.drop_all(bind=engine)
"""


@pytest.fixture(autouse=True)
def test_client():
    Base.metadata.create_all(bind=engine)
    db = TestingSession()
    add_test_data(db)
    db.close()

    try:
        yield
    finally:
        Base.metadata.drop_all(bind=engine)
