"""
Unit tests for inventory command helper functions.

Tests the helper functions in inventory_commands.py.
"""

from server.commands.inventory_item_matching import (
    match_equipped_item_by_name,
    match_inventory_item_by_name,
    match_room_drop_by_name,
    normalize_slot_name,
)


def test_match_room_drop_by_name_exact() -> None:
    """Test match_room_drop_by_name() finds exact match."""
    drop_list = [{"item_name": "sword"}, {"item_name": "shield"}]
    result = match_room_drop_by_name(drop_list, "sword")
    assert result == 0


def test_match_room_drop_by_name_not_found() -> None:
    """Test match_room_drop_by_name() returns None when not found."""
    drop_list = [{"item_name": "sword"}]
    result = match_room_drop_by_name(drop_list, "bow")
    assert result is None


def test_match_inventory_item_by_name_exact() -> None:
    """Test match_inventory_item_by_name() finds exact match."""
    inventory = [{"item_name": "potion"}, {"name": "scroll"}]
    result = match_inventory_item_by_name(inventory, "potion")
    assert result == 0


def test_match_inventory_item_by_name_not_found() -> None:
    """Test match_inventory_item_by_name() returns None when not found."""
    inventory = [{"item_name": "potion"}]
    result = match_inventory_item_by_name(inventory, "bow")
    assert result is None


def test_match_equipped_item_by_name() -> None:
    """Test match_equipped_item_by_name() finds equipped item."""
    equipped = {"weapon": {"item_name": "sword"}, "armor": {"item_name": "plate"}}
    result = match_equipped_item_by_name(equipped, "sword")
    assert result == "weapon"


def test_match_equipped_item_by_name_not_found() -> None:
    """Test match_equipped_item_by_name() returns None when not found."""
    equipped = {"weapon": {"item_name": "sword"}}
    result = match_equipped_item_by_name(equipped, "bow")
    assert result is None


def test_normalize_slot_name() -> None:
    """Test normalize_slot_name() normalizes slot names."""
    assert normalize_slot_name("weapon") == "weapon"
    assert normalize_slot_name("WEAPON") == "weapon"
    assert normalize_slot_name(None) is None
