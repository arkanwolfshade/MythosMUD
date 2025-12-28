"""
Unit tests for inventory_schema validation functions.

Tests the validation functions in inventory_schema.py module.
"""

import pytest

from server.schemas.inventory_schema import (
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
    payload = {
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
