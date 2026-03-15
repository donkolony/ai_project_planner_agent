"""
Integration tests for the project plan creation endpoint.
"""

import json
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_plan():
    """
    Test the successful generation of a project plan.

    Validates that the POST /plan/ endpoint:
    1. Accepts a valid project payload.
    2. Returns a 200 OK status code.
    3. Returns the expected structured data provided by the MockAIPlanner.
    """
    payload = {
        "project_name": "Test Project",
        "description": "Test Description",
        "tech_stack": ["Python", "FastAPI"],
    }

    response = client.post("/plan/", json=payload)
    assert response.status_code == 200

    data = response.json()
    # The AIPlanner is mocked, so the returned summary is fixed
    assert data["summary"] == "Mock summary"
    assert data["phases"] == [
        {"name": "Mock phase 1", "tasks": ["Task A", "Task B"]},
        {"name": "Mock phase 2", "tasks": ["Task C"]},
    ]
