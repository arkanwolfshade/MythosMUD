"""
Unit tests for inventory command helper functions.

Tests the helper functions in inventory_commands.py.
"""

from server.commands.inventory_commands import (
    _match_equipped_item_by_name,
    _match_inventory_item_by_name,
    _match_room_drop_by_name,
    _normalize_slot_name,
)


def test_match_room_drop_by_name_exact():
    """Test _match_room_drop_by_name() finds exact match."""
    drop_list = [{"item_name": "sword"}, {"item_name": "shield"}]
    result = _match_room_drop_by_name(drop_list, "sword")
    assert result == 0


def test_match_room_drop_by_name_not_found():
    """Test _match_room_drop_by_name() returns None when not found."""
    drop_list = [{"item_name": "sword"}]
    result = _match_room_drop_by_name(drop_list, "bow")
    assert result is None


def test_match_inventory_item_by_name_exact():
    """Test _match_inventory_item_by_name() finds exact match."""
    inventory = [{"item_name": "potion"}, {"name": "scroll"}]
    result = _match_inventory_item_by_name(inventory, "potion")
    assert result == 0


def test_match_inventory_item_by_name_not_found():
    """Test _match_inventory_item_by_name() returns None when not found."""
    inventory = [{"item_name": "potion"}]
    result = _match_inventory_item_by_name(inventory, "bow")
    assert result is None


def test_match_equipped_item_by_name():
    """Test _match_equipped_item_by_name() finds equipped item."""
    equipped = {"weapon": {"item_name": "sword"}, "armor": {"item_name": "plate"}}
    result = _match_equipped_item_by_name(equipped, "sword")
    assert result == "weapon"


def test_match_equipped_item_by_name_not_found():
    """Test _match_equipped_item_by_name() returns None when not found."""
    equipped = {"weapon": {"item_name": "sword"}}
    result = _match_equipped_item_by_name(equipped, "bow")
    assert result is None


def test_normalize_slot_name():
    """Test _normalize_slot_name() normalizes slot names."""
    assert _normalize_slot_name("weapon") == "weapon"
    assert _normalize_slot_name("WEAPON") == "weapon"
    assert _normalize_slot_name(None) is None
