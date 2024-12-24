from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Sample API"}

def test_create_item():
    item = {
        "name": "Test Item",
        "description": "Test Description",
        "price": 10.5,
        "tax": 1.5
    }
    response = client.post("/items/", json=item)
    assert response.status_code == 200
    assert response.json() == item

def test_get_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_item():
    # First create an item
    item = {
        "name": "Test Item 2",
        "price": 15.0
    }
    client.post("/items/", json=item)
    
    # Then get it by id
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Test Item 2"

def test_get_item_not_found():
    response = client.get("/items/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found" 
