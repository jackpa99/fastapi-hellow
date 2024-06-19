from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_create_item():
    response = client.post(
        "/items/",
        json={"name": "Item 1", "description": "A test item", "price": 10.5, "tax": 1.5}
    )
    assert response.status_code == 200
    assert response.json() == {"item_name": "Item 1", "item_price": 10.5}
