import pytest
from fastapi.testclient import TestClient
from app.main import create_app

@pytest.fixture
def client(tmp_path):
    db_path = tmp_path / "test_ideas.db"
    with TestClient(create_app(db_path=db_path)) as test_client:
        yield test_client

def test_greeting_returns_json(client):
    response = client.get("/api/hello")
    assert response.status_code == 200
    assert isinstance(response.json()["message"], str)

def test_valid_post_returns_created_idea(client):
    response = client.post(
        "/api/ideas",
        json={
            "title": "Start a robotics club",
            "category": "clubs"
        }
    )

    assert response.status_code == 201

    data = response.json()

    assert data["id"] == 1
    assert data["title"] == "Start a robotics club"
    assert data["category"] == "clubs"
