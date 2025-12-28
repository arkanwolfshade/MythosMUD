"""
Unit tests for look item helper functions.

Tests the helper functions in look_item.py.
"""

import pytest

from server.commands.look_item import _find_item_in_equipped, _find_item_in_inventory, _find_item_in_room_drops


def test_find_item_in_room_drops_found():
    """Test _find_item_in_room_drops() finds item by name."""
    room_drops = [{"item_name": "sword", "item_id": "item_001"}, {"item_name": "shield", "item_id": "item_002"}]
    result = _find_item_in_room_drops(room_drops, "sword")
    assert result is not None
    assert result["item_name"] == "sword"


def test_find_item_in_room_drops_not_found():
    """Test _find_item_in_room_drops() returns None when item not found."""
    room_drops = [{"item_name": "sword", "item_id": "item_001"}]
    result = _find_item_in_room_drops(room_drops, "bow")
    assert result is None


def test_find_item_in_room_drops_instance_number():
    """Test _find_item_in_room_drops() with instance number."""
    room_drops = [
        {"item_name": "sword", "item_id": "item_001"},
        {"item_name": "sword", "item_id": "item_002"},
    ]
    result = _find_item_in_room_drops(room_drops, "sword", instance_number=2)
    assert result is not None
    assert result["item_id"] == "item_002"


def test_find_item_in_inventory_found():
    """Test _find_item_in_inventory() finds item by name."""
    inventory = [{"item_name": "potion", "item_id": "item_001"}, {"name": "scroll", "item_id": "item_002"}]
    result = _find_item_in_inventory(inventory, "potion")
    assert result is not None
    assert result["item_name"] == "potion"


def test_find_item_in_inventory_not_found():
    """Test _find_item_in_inventory() returns None when item not found."""
    inventory = [{"item_name": "potion", "item_id": "item_001"}]
    result = _find_item_in_inventory(inventory, "bow")
    assert result is None


def test_find_item_in_equipped_found():
    """Test _find_item_in_equipped() finds item by name."""
    equipped = {"weapon": {"item_name": "sword", "item_id": "item_001"}, "armor": {"item_name": "plate", "item_id": "item_002"}}
    result = _find_item_in_equipped(equipped, "sword")
    assert result is not None
    assert result[0] == "weapon"
    assert result[1]["item_name"] == "sword"


def test_find_item_in_equipped_not_found():
    """Test _find_item_in_equipped() returns None when item not found."""
    equipped = {"weapon": {"item_name": "sword", "item_id": "item_001"}}
    result = _find_item_in_equipped(equipped, "bow")
    assert result is None
