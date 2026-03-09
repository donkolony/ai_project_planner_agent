import json
from uuid import uuid4
from fastapi.testclient import TestClient
from app.main import app
from app.models.db_models import PlanDB

client = TestClient(app)

def test_get_plan_by_id(get_test_session):
    session = get_test_session

    plan = PlanDB(
        id=uuid4(),
        project_name="Test Project",
        description="Test Description",
        tech_stack=json.dumps(["Python", "FastAPI"]),
        summary="Mocked summary",
        phases=json.dumps([{"name": "Phase 1", "tasks": ["Task 1", "Task 2"]}]),
    )
    session.add(plan)
    session.commit()
    session.refresh(plan)

    response = client.get(f"/plan/{plan.id}")
    assert response.status_code == 200

    data = response.json()
    assert data["summary"] == "Mocked summary"
    assert data["phases"] == [{"name": "Phase 1", "tasks": ["Task 1", "Task 2"]}]