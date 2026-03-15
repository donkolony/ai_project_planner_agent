"""
Integration tests for the project plan listing endpoint.
"""

import json
from fastapi.testclient import TestClient
from uuid import uuid4
from app.main import app
from app.models.db_models import PlanDB

client = TestClient(app)


def test_list_plans(get_test_session):
    """
    Test the retrieval of all stored project plans.

    Validates that:
    1. The GET /plan/ endpoint returns a list of all plans in the database.
    2. Multiple plan records are correctly serialized into the response list.
    3. The integrity of individual plan data (summary and phases) is maintained
       during bulk retrieval.

    Args:
        get_test_session: The database session fixture used for seeding multiple plans.
    """
    session = get_test_session

    # Create multiple plans
    plans = [
        PlanDB(
            id=str(uuid4()),
            project_name=f"Project {i}",
            description="Desc",
            tech_stack=json.dumps(["Python"]),
            summary=f"Summary {i}",
            phases=json.dumps([{"name": f"Phase {i}", "tasks": ["Task 1"]}]),
        )
        for i in range(2)
    ]
    session.add_all(plans)
    session.commit()

    response = client.get("/plan/")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 2
    for i, plan in enumerate(data):
        assert plan["summary"] == f"Summary {i}"
        assert plan["phases"] == [{"name": f"Phase {i}", "tasks": ["Task 1"]}]
