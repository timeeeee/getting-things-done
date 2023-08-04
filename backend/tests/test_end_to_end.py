from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from main import app, get_db
from database import Base
from settings import SQLALCHEMY_TEST_DATABASE_URL

engine = create_engine(SQLALCHEMY_TEST_DATABASE_URL)
SessionTest = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

"""
def override_get_db():
      try:
          db = TestingSessionLocal()
          yield db
      finally:
          db.close()
"""

def override_get_db():
    connection = engine.connect()

    # begin a non-ORM transaction
    transaction = connection.begin()

    # bind an individual Session to the connection
    db = Session(bind=connection)

    yield db

    db.close()
    transaction.rollback()
    connection.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


def test_pass():
    response = client.get("/in-items/")
    print(response)
