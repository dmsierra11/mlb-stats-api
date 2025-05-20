"""Example router module for handling item-related endpoints."""

from typing import List

from fastapi import APIRouter, HTTPException, status

from app.services.example_service import ExampleService, Item

router = APIRouter(tags=["example"])
service = ExampleService()


@router.get("/items", response_model=List[Item])
async def get_items() -> List[Item]:
    """Get all items."""
    return service.get_all_items()


@router.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int) -> Item:
    """Get a specific item by ID."""
    item = service.get_item(item_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item {item_id} not found",
        )
    return item


@router.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_item(item: Item) -> Item:
    """Create a new item."""
    return service.create_item(item)


@router.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item) -> Item:
    """Update an existing item."""
    updated_item = service.update_item(item_id, item)
    if not updated_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item {item_id} not found",
        )
    return updated_item


@router.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: int) -> None:
    """Delete an item."""
    if not service.delete_item(item_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item {item_id} not found",
        )
