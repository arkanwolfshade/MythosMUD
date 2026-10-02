"""
Unit tests for inventory_schema validation functions.

Tests the validation functions in inventory_schema.py module.
"""

from typing import Any

import pytest

from server.constants.containers import MAX_CONTAINER_CAPACITY_SLOTS
from server.schemas.shared.inventory_schema import (
    InventorySchemaValidationError,
    validate_inventory_items,
    validate_inventory_payload,
)


def test_validate_inventory_payload_valid():
    """Test validate_inventory_payload() accepts valid payload."""
    payload = {
        "inventory": [{"item_id": "item_001", "item_name": "Sword", "slot_type": "weapon", "quantity": 1}],
        "equipped": {},
    }

    # Should not raise
    validate_inventory_payload(payload)


def test_validate_inventory_payload_missing_required():
    """Test validate_inventory_payload() raises error for missing required fields."""
    payload: dict[str, Any] = {
        "inventory": [],
    }

    with pytest.raises(InventorySchemaValidationError):
        validate_inventory_payload(payload)


def test_validate_inventory_payload_invalid_inventory():
    """Test validate_inventory_payload() raises error for invalid inventory."""
    payload = {
        "inventory": "not_an_array",
        "equipped": {},
    }

    with pytest.raises(InventorySchemaValidationError):
        validate_inventory_payload(payload)


def test_validate_inventory_items_valid():
    """Test validate_inventory_items() accepts valid items."""
    items = [{"item_id": "item_001", "item_name": "Sword", "slot_type": "weapon", "quantity": 1}]

    # Should not raise
    validate_inventory_items(items)


def test_validate_inventory_items_missing_required():
    """Test validate_inventory_items() raises error for missing required fields."""
    items = [
        {"item_id": "item_001", "item_name": "Sword"}  # Missing slot_type and quantity
    ]

    with pytest.raises(InventorySchemaValidationError):
        validate_inventory_items(items)


def test_validate_inventory_items_invalid_quantity():
    """Test validate_inventory_items() raises error for invalid quantity."""
    items = [{"item_id": "item_001", "item_name": "Sword", "slot_type": "weapon", "quantity": 0}]

    with pytest.raises(InventorySchemaValidationError):
        validate_inventory_items(items)


@pytest.mark.parametrize(
    ("capacity", "valid"), [(MAX_CONTAINER_CAPACITY_SLOTS, True), (MAX_CONTAINER_CAPACITY_SLOTS + 1, False)]
)
def test_validate_inventory_items_inner_container_capacity_uses_global_cap(capacity: int, valid: bool) -> None:
    """inner_container capacity follows the global container ceiling, not the old 20-slot limit."""
    items: list[dict[str, object]] = [
        {
            "item_id": "bag_001",
            "item_name": "Bag",
            "slot_type": "backpack",
            "quantity": 1,
            "inner_container": {"capacity_slots": capacity, "items": []},
        }
    ]
    if valid:
        validate_inventory_items(items)
    else:
        with pytest.raises(InventorySchemaValidationError):
            validate_inventory_items(items)
