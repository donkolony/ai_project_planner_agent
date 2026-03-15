import pytest
from sqlmodel import SQLModel, Session, create_engine
from fastapi.testclient import TestClient

from app.main import app

# Use a local sqlite file for tests
TEST_SQLITE_URL = "sqlite:///./test.db"
engine = create_engine(TEST_SQLITE_URL, echo=False)


# Create tables before tests and drop afterwards
@pytest.fixture(scope="session", autouse=True)
def create_test_db():
    SQLModel.metadata.create_all(engine)
    yield
    SQLModel.metadata.drop_all(engine)


@pytest.fixture(scope="function", autouse=True)
def clean_db():
    # Ensure a clean schema between tests
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)


# Fixture to provide a session for tests
@pytest.fixture()
def get_test_session():
    with Session(engine) as session:
        yield session


def get_test_session_override():
    with Session(engine) as session:
        yield session


@pytest.fixture(scope="session", autouse=True)
def override_dependencies():
    # Late imports to avoid import-time side effects
    from app.core.database import get_session
    from app.api import planner as planner_module
    from tests.mocks.mock_ai_planner import MockAIPlanner

    # Override database session dependency to use test engine
    app.dependency_overrides[get_session] = get_test_session_override

    planner_module.ai_planner = MockAIPlanner()

    # Provide a TestClient fixture via yield if any teardown is needed in future
    yield
