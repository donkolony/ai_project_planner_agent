"""
Integration tests for retrieving specific project plans from the database.
"""

import json
from uuid import uuid4
from fastapi.testclient import TestClient
from app.main import app
from app.models.db_models import PlanDB

client = TestClient(app)


def test_get_plan_by_id(get_test_session):
    """
    Test the retrieval of a project plan by its unique ID.

    Validates that:
    1. A plan seeded directly into the test database can be accessed via the API.
    2. The API correctly deserializes the JSON-encoded phases from the database.
    3. The summary and phases returned match the records in the database.

    Args:
        get_test_session: The database session fixture used for seeding data.
    """
    session = get_test_session

    plan = PlanDB(
        id=str(uuid4()),
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
