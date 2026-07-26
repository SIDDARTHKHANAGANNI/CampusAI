import os
import sys

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)
sys.path.insert(0, PROJECT_ROOT)

from backend.app.main import app
from backend.app.database.database import Base, get_db

# Import models
from backend.app.models.user import User
from backend.app.models.student import Student
from backend.app.models.academic import AcademicRecord
from backend.app.models.skill import Skill
from backend.app.models.project import Project
from backend.app.models.career_goal import CareerGoal

TEST_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


@pytest.fixture()
def db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    database = TestingSessionLocal()

    try:
        yield database
    finally:
        database.close()


def override_get_db():
    database = TestingSessionLocal()

    try:
        yield database
    finally:
        database.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture()
def client(db):
    return TestClient(app)