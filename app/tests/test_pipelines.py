from fastapi.testclient import TestClient
from app.src.main import app

client = TestClient(app)


def test_add_pipeline():
    response = client.post(
        "pipelines/",
        json={
              "title": "test_pipeline2",
              "steps": [
                {
                  "title": "test_steps",
                  "step_parameters": "test"
                }
              ]
            })
    assert response.status_code == 200


def test_get_pipelines():
    response = client.get("pipelines/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_edit_pipeline():
    pipeline_id = 1
    response = client.patch(
        f"pipelines/{pipeline_id}",
        json={
            "title": "test_edit",
            "steps": [
                {
                    "title": "test_steps",
                    "step_parameters": "test"
                }
            ]
        })
    assert response.status_code == 200
    assert response.json()["title"] == "test_edit"


def test_get_one_pipeline():
    pipeline_id = 1
    response = client.get(f"pipelines/{pipeline_id}")
    assert response.status_code == 200
    assert "title" in response.json()


def test_delete_pipeline():
    pipeline_id = 1
    response = client.delete(f"pipelines/{pipeline_id}")
    assert response.status_code == 200
