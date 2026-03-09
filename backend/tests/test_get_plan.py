# tests/test_get_plan.py
import json
import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel, Session, create_engine
from app.main import app
from app.models.db_models import PlanDB
from app.api.planner import get_ai_planner
from app.services.ai_services import AIPlanner

# Create an in-memory SQLite database for tests
TEST_DB_URL = "sqlite:///:memory:"
engine = create_engine(TEST_DB_URL, connect_args={"check_same_thread": False})


# Override get_session to use in-memory DB
def get_test_session():
    with Session(engine) as session:
        yield session


# Mock AIPlanner to return a predictable response
class MockAIPlanner:
    def generate_plan(self, project_name, description, tech_stack):
        return {
            "summary": "Mocked summary",
            "phases": [{"name": "Phase 1", "tasks": ["Task 1", "Task 2"]}],
        }


@pytest.fixture(autouse=True)
def prepare_db():
    SQLModel.metadata.create_all(engine)
    yield
    SQLModel.metadata.drop_all(engine)


# Apply dependency overrides
app.dependency_overrides[get_ai_planner] = lambda: MockAIPlanner()
app.dependency_overrides["get_session"] = get_test_session

client = TestClient(app)


def test_get_plan_by_id():
    # First, insert a plan into the test DB
    session = next(get_test_session())
    plan = PlanDB(
        project_name="Test Project",
        description="Test Description",
        tech_stack="Python,FastAPI",
        summary="Mocked summary",
        phases=json.dumps([{"name": "Phase 1", "tasks": ["Task 1", "Task 2"]}]),
    )
    session.add(plan)
    session.commit()
    session.refresh(plan)

    # Retrieve the plan
    response = client.get(f"/plan/{str(plan.id)}")  # <-- convert UUID to string
    assert response.status_code == 200
    data = response.json()
    assert data["summary"] == "Mocked summary"
    assert data["phases"] == [{"name": "Phase 1", "tasks": ["Task 1", "Task 2"]}]
