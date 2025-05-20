"""Tests for the example service."""

import pytest

from app.services.example_service import ExampleService, Item


@pytest.fixture
def service() -> ExampleService:
    """Provide a fresh service instance for each test."""
    return ExampleService()


def test_get_all_items_empty() -> None:
    """Test getting all items when none exist."""
    service = ExampleService()
    items = service.get_all_items()
    assert items == []


def test_create_item() -> None:
    """Test creating a new item."""
    service = ExampleService()
    item = Item(name="Test Item", description="Test Description")
    created_item = service.create_item(item)
    assert created_item.id == 1
    assert created_item.name == item.name
    assert created_item.description == item.description


def test_get_item() -> None:
    """Test getting a specific item."""
    service = ExampleService()
    item = Item(name="Test Item", description="Test Description")
    created_item = service.create_item(item)
    assert created_item.id is not None
    created_item_id = created_item.id  # type: int
    retrieved_item = service.get_item(created_item_id)
    assert retrieved_item is not None
    assert retrieved_item.id == created_item_id
    assert retrieved_item.name == created_item.name
    assert retrieved_item.description == created_item.description


def test_get_nonexistent_item() -> None:
    """Test getting a non-existent item."""
    service = ExampleService()
    item = service.get_item(999)
    assert item is None


def test_update_item() -> None:
    """Test updating an item."""
    service = ExampleService()
    item = Item(name="Test Item", description="Test Description")
    created_item = service.create_item(item)

    updated_item = Item(name="Updated Item", description="Updated Description")
    assert created_item.id is not None
    created_item_id = created_item.id  # type: int
    result = service.update_item(created_item_id, updated_item)

    assert result is not None
    assert result.id == created_item_id
    assert result.name == updated_item.name
    assert result.description == updated_item.description


def test_update_nonexistent_item() -> None:
    """Test updating a non-existent item."""
    service = ExampleService()
    updated_item = Item(name="Updated Item", description="Updated Description")
    result = service.update_item(999, updated_item)
    assert result is None


def test_delete_item() -> None:
    """Test deleting an item."""
    service = ExampleService()
    item = Item(name="Test Item", description="Test Description")
    created_item = service.create_item(item)

    assert created_item.id is not None
    created_item_id = created_item.id  # type: int

    # Verify item exists
    assert service.get_item(created_item_id) is not None

    # Delete item
    result = service.delete_item(created_item_id)
    assert result is True

    # Verify item is gone
    assert service.get_item(created_item_id) is None


def test_delete_nonexistent_item() -> None:
    """Test deleting a non-existent item."""
    service = ExampleService()
    result = service.delete_item(999)
    assert result is False


def test_multiple_items(service: ExampleService) -> None:
    """Test handling multiple items."""
    # Create multiple items
    items = [{"name": f"Item {i}", "description": f"Description {i}"} for i in range(3)]
    created_items = [service.create_item(Item(id=None, **item)) for item in items]

    # Verify all items were created with correct IDs
    for i, item in enumerate(created_items, 1):
        assert item.id == i
        assert item.name == f"Item {i-1}"
        assert item.description == f"Description {i-1}"

    # Verify get_all_items returns all items
    all_items = service.get_all_items()
    assert len(all_items) == 3
    assert all_items == created_items
