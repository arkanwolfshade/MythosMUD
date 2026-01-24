"""
Unit tests for InventoryItem model.
"""

import pytest
from pydantic import ValidationError

from server.models.game import InventoryItem


def test_inventory_item_creation():
    """Test InventoryItem can be created with required fields."""
    item = InventoryItem(item_id="test_item_123", quantity=5)

    assert item.item_id == "test_item_123"
    assert item.quantity == 5


def test_inventory_item_default_quantity():
    """Test InventoryItem defaults quantity to 1."""
    item = InventoryItem(item_id="test_item_123")

    assert item.quantity == 1


def test_inventory_item_quantity_validation_min():
    """Test InventoryItem validates quantity is >= 1."""
    with pytest.raises(ValidationError):
        InventoryItem(item_id="test_item_123", quantity=0)
