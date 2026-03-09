import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel, create_engine, Session

from app.main import app
from app.core.database import get_session
from app.services.ai_services import AIPlanner


# -----------------------------
# Test Database
# -----------------------------

TEST_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
)

# Create tables before tests
@pytest.fixture(name="session")
def session_fixture():
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    SQLModel.metadata.drop_all(engine)


# Override dependency
@pytest.fixture(name="client")
def client_fixture(session: Session):

    def get_session_override():
        return session

    app.dependency_overrides[get_session] = get_session_override

    client = TestClient(app)

    yield client

    app.dependency_overrides.clear()


# -----------------------------
# Mock AIPlanner
# -----------------------------

@pytest.fixture(autouse=True)
def mock_ai(monkeypatch):

    def fake_generate_plan(self, project_name, description, tech_stack):
        return {
            "summary": "Test generated project plan",
            "phases": [
                {
                    "name": "Phase 1",
                    "tasks": ["task 1", "task 2"]
                }
            ]
        }

    monkeypatch.setattr(AIPlanner, "generate_plan", fake_generate_plan)