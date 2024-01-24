from fastapi.testclient import TestClient
from model_machine_learning.src.main import app

client = TestClient(app)


def test_get_results():
    response = client.get("image_detection/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_one_result():
    result_id = 1
    response = client.get(f"image_detection/{result_id}")
    assert response.status_code == 200
    assert "processed_image" in response.json()
