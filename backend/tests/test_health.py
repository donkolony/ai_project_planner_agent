"""
Basic health and connectivity tests for the API.
"""

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_endpoint():
    """
    Verify that the root endpoint is accessible and returning a healthy status.

    This test acts as a primary 'smoke test' to ensure that the FastAPI
    application is correctly initialized and the basic routing is functional.
    """
    response = client.get("/")
    assert response.status_code == 200

    data = response.json()
    assert data.get("status") == "running"
