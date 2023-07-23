import sys
import os
import pymysql
import pytest
from fastapi.testclient import TestClient

# Adds the project's root directory to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../" * 3))
sys.path.insert(0, project_root)

pymysql.install_as_MySQLdb()

from app.db.database import Base, engine, SessionLocal
from main import app

client = TestClient(app)


# Creates a fixture to set up the test database
@pytest.fixture(scope="module")
def test_db():
    Base.metadata.create_all(bind=engine)
    yield SessionLocal()
    Base.metadata.drop_all(bind=engine)


# TestClient fixture to make requests to the FastAPI app
@pytest.fixture(scope="module")
def client(test_db):
    return TestClient(app)
