"""Example service module for managing items."""

from typing import List, Optional

from pydantic import BaseModel


class Item(BaseModel):
    """Data model for an item."""

    id: Optional[int] = None
    name: str
    description: Optional[str] = None


class ExampleService:
    """Service for managing items."""

    def __init__(self) -> None:
        """Initialize the service with empty storage."""
        # In-memory storage for demonstration
        self.items: List[Item] = []
        self._counter = 1

    def get_all_items(self) -> List[Item]:
        """Get all items."""
        return self.items

    def get_item(self, item_id: int) -> Optional[Item]:
        """Get a specific item by ID."""
        return next((item for item in self.items if item.id == item_id), None)

    def create_item(self, item: Item) -> Item:
        """Create a new item."""
        item.id = self._counter
        self._counter += 1
        self.items.append(item)
        return item

    def update_item(self, item_id: int, updated_item: Item) -> Optional[Item]:
        """Update an existing item."""
        for i, item in enumerate(self.items):
            if item.id == item_id:
                updated_item.id = item_id
                self.items[i] = updated_item
                return updated_item
        return None

    def delete_item(self, item_id: int) -> bool:
        """Delete an item."""
        initial_length = len(self.items)
        self.items = [item for item in self.items if item.id != item_id]
        return len(self.items) < initial_length
