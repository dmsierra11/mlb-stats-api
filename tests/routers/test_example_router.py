"""Tests for the example router."""

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_items_empty() -> None:
    """Test getting items when none exist."""
    response = client.get("/api/v1/items")
    assert response.status_code == 200
    assert response.json() == []


def test_create_item() -> None:
    """Test creating a new item."""
    item_data = {"name": "Test Item", "description": "Test Description"}
    response = client.post("/api/v1/items", json=item_data)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == item_data["name"]
    assert data["description"] == item_data["description"]
    assert "id" in data


def test_get_item() -> None:
    """Test getting a specific item."""
    # First create an item
    data = {"name": "Test Item", "description": "Test Description"}
    resp = client.post("/api/v1/items", json=data)
    item_id = resp.json()["id"]

    # Then get it
    resp = client.get(f"/api/v1/items/{item_id}")
    assert resp.status_code == 200
    result = resp.json()
    assert result["id"] == item_id
    assert result["name"] == data["name"]
    assert result["description"] == data["description"]


def test_get_nonexistent_item() -> None:
    """Test getting a non-existent item."""
    response = client.get("/api/v1/items/999")
    assert response.status_code == 404


def test_update_item() -> None:
    """Test updating an item."""
    # First create an item
    item_data = {"name": "Test Item", "description": "Test Description"}
    create_response = client.post("/api/v1/items", json=item_data)
    item_id = create_response.json()["id"]

    # Then update it
    update_data = {"name": "Updated Item", "description": "Updated Description"}
    response = client.put(f"/api/v1/items/{item_id}", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == item_id
    assert data["name"] == update_data["name"]
    assert data["description"] == update_data["description"]


def test_update_nonexistent_item() -> None:
    """Test updating a non-existent item."""
    update_data = {"name": "Updated Item", "description": "Updated Description"}
    response = client.put("/api/v1/items/999", json=update_data)
    assert response.status_code == 404


def test_delete_item() -> None:
    """Test deleting an item."""
    # First create an item
    item_data = {"name": "Test Item", "description": "Test Description"}
    create_response = client.post("/api/v1/items", json=item_data)
    item_id = create_response.json()["id"]

    # Then delete it
    response = client.delete(f"/api/v1/items/{item_id}")
    assert response.status_code == 204

    # Verify it's gone
    get_response = client.get(f"/api/v1/items/{item_id}")
    assert get_response.status_code == 404


def test_delete_nonexistent_item() -> None:
    """Test deleting a non-existent item."""
    response = client.delete("/api/v1/items/999")
    assert response.status_code == 404
