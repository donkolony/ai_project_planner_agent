from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/")
    assert response.status_code == 200

    data = response.json()
    assert data.get("status") == "AI Project Planner Backend Running"
