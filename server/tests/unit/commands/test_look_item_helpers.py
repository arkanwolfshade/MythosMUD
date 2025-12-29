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


def test_find_item_in_room_drops_empty():
    """Test _find_item_in_room_drops() with empty list."""
    result = _find_item_in_room_drops([], "sword")
    assert result is None


def test_find_item_in_room_drops_no_match():
    """Test _find_item_in_room_drops() with no matching items."""
    room_drops = [{"item_name": "Helmet", "prototype_id": "helmet_001"}]
    result = _find_item_in_room_drops(room_drops, "sword")
    assert result is None


def test_find_item_in_room_drops_multiple_matches():
    """Test _find_item_in_room_drops() with multiple matches (ambiguous)."""
    room_drops = [
        {"item_name": "Sword", "prototype_id": "sword_001"},
        {"item_name": "Long Sword", "prototype_id": "sword_002"},
    ]
    result = _find_item_in_room_drops(room_drops, "sword")
    assert result is None  # Ambiguous


def test_find_item_in_room_drops_with_instance_number():
    """Test _find_item_in_room_drops() with instance number."""
    room_drops = [
        {"item_name": "Sword", "prototype_id": "sword_001"},
        {"item_name": "Long Sword", "prototype_id": "sword_002"},
    ]
    result = _find_item_in_room_drops(room_drops, "sword", instance_number=1)
    assert result is not None
    assert result["item_name"] == "Sword"


def test_find_item_in_room_drops_instance_number_out_of_range():
    """Test _find_item_in_room_drops() with instance number out of range."""
    room_drops = [{"item_name": "Sword", "prototype_id": "sword_001"}]
    result = _find_item_in_room_drops(room_drops, "sword", instance_number=5)
    assert result is None


def test_find_item_in_room_drops_instance_number_zero():
    """Test _find_item_in_room_drops() with instance number zero."""
    room_drops = [{"item_name": "Sword", "prototype_id": "sword_001"}]
    result = _find_item_in_room_drops(room_drops, "sword", instance_number=0)
    assert result is None


def test_find_item_in_inventory_empty():
    """Test _find_item_in_inventory() with empty list."""
    result = _find_item_in_inventory([], "sword")
    assert result is None


def test_find_item_in_inventory_no_match():
    """Test _find_item_in_inventory() with no matching items."""
    inventory = [{"item_name": "Helmet", "prototype_id": "helmet_001"}]
    result = _find_item_in_inventory(inventory, "sword")
    assert result is None


def test_find_item_in_inventory_multiple_matches():
    """Test _find_item_in_inventory() with multiple matches (ambiguous)."""
    inventory = [
        {"item_name": "Sword", "prototype_id": "sword_001"},
        {"item_name": "Long Sword", "prototype_id": "sword_002"},
    ]
    result = _find_item_in_inventory(inventory, "sword")
    assert result is None  # Ambiguous


def test_find_item_in_inventory_with_instance_number():
    """Test _find_item_in_inventory() with instance number."""
    inventory = [
        {"item_name": "Sword", "prototype_id": "sword_001"},
        {"item_name": "Long Sword", "prototype_id": "sword_002"},
    ]
    result = _find_item_in_inventory(inventory, "sword", instance_number=2)
    assert result is not None
    assert result["item_name"] == "Long Sword"


def test_find_item_in_inventory_instance_number_out_of_range():
    """Test _find_item_in_inventory() with instance number out of range."""
    inventory = [{"item_name": "Sword", "prototype_id": "sword_001"}]
    result = _find_item_in_inventory(inventory, "sword", instance_number=5)
    assert result is None


def test_find_item_in_equipped_empty():
    """Test _find_item_in_equipped() with empty dict."""
    result = _find_item_in_equipped({}, "sword")
    assert result is None


def test_find_item_in_equipped_no_match():
    """Test _find_item_in_equipped() with no matching items."""
    equipped = {"head": {"item_name": "Helmet", "prototype_id": "helmet_001"}}
    result = _find_item_in_equipped(equipped, "sword")
    assert result is None


def test_find_item_in_equipped_multiple_matches():
    """Test _find_item_in_equipped() with multiple matches (ambiguous)."""
    equipped = {
        "left_hand": {"item_name": "Sword", "prototype_id": "sword_001"},
        "right_hand": {"item_name": "Long Sword", "prototype_id": "sword_002"},
    }
    result = _find_item_in_equipped(equipped, "sword")
    assert result is None  # Ambiguous


def test_find_item_in_equipped_with_instance_number():
    """Test _find_item_in_equipped() with instance number."""
    equipped = {
        "left_hand": {"item_name": "Sword", "prototype_id": "sword_001"},
        "right_hand": {"item_name": "Long Sword", "prototype_id": "sword_002"},
    }
    result = _find_item_in_equipped(equipped, "sword", instance_number=2)
    assert result is not None
    assert result[0] == "right_hand"
    assert result[1]["item_name"] == "Long Sword"


def test_find_item_in_equipped_instance_number_out_of_range():
    """Test _find_item_in_equipped() with instance number out of range."""
    equipped = {"head": {"item_name": "Helmet", "prototype_id": "helmet_001"}}
    result = _find_item_in_equipped(equipped, "helmet", instance_number=5)
    assert result is None
