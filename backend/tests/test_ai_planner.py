"""
Pytest configuration and global fixtures.

This module sets up the test environment, handles the lifecycle of the
test database, and configures dependency overrides to ensure tests run
against mock services rather than production infrastructure.
"""

import pytest
from sqlmodel import SQLModel, Session, create_engine
from fastapi.testclient import TestClient

from app.main import app

# Use a local sqlite file for tests
TEST_SQLITE_URL = "sqlite:///./test.db"
engine = create_engine(TEST_SQLITE_URL, echo=False)


@pytest.fixture(scope="session", autouse=True)
def create_test_db():
    """
    Manage the test database lifecycle at the session level.

    Creates all database tables defined in SQLModel metadata before any
    tests run and drops them after the entire test suite completes.
    """
    SQLModel.metadata.create_all(engine)
    yield
    SQLModel.metadata.drop_all(engine)


@pytest.fixture(scope="function", autouse=True)
def clean_db():
    """
    Reset the database schema between individual tests.

    Ensures that data created in one test does not leak into another by
    dropping and recreating tables before every test function.
    """
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)


@pytest.fixture()
def get_test_session():
    """
    Provide a database session specifically for use within test functions.

    Yields:
        Session: A SQLModel session connected to the test database.
    """
    with Session(engine) as session:
        yield session


def get_test_session_override():
    """
    Override function used to replace the production database dependency.

    Yields:
        Session: A SQLModel session connected to the test database.
    """
    with Session(engine) as session:
        yield session


@pytest.fixture(scope="session", autouse=True)
def override_dependencies():
    """
    Configure FastAPI dependency overrides for the duration of the test session.

    Replaces the live database session with the test session and swaps
    the real AI service for a deterministic MockAIPlanner.
    """
    # Late imports to avoid import-time side effects
    from app.core.database import get_session
    from app.api import planner as planner_module
    from tests.mocks.mock_ai_planner import MockAIPlanner

    # Override database session dependency to use test engine
    app.dependency_overrides[get_session] = get_test_session_override

    # Inject the mock AI service
    planner_module.ai_planner = MockAIPlanner()

    yield
