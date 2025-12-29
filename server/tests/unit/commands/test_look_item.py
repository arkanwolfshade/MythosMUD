"""
Unit tests for item look functionality.

Tests the helper functions for looking at items in various locations.
"""

from unittest.mock import MagicMock

import pytest

from server.commands.look_item import (
    _check_equipped_item,
    _check_item_in_location,
    _find_item_in_equipped,
    _find_item_in_inventory,
    _find_item_in_room_drops,
    _get_item_description_from_prototype,
    _handle_item_look,
    _try_lookup_item_implicit,
)


@pytest.fixture
def mock_prototype_registry():
    """Create a mock prototype registry."""
    registry = MagicMock()
    prototype = MagicMock()
    prototype.name = "Test Item"
    prototype.long_description = "A test item description."
    registry.get.return_value = prototype
    return registry


@pytest.fixture
def sample_room_drop():
    """Create a sample room drop item."""
    return {
        "item_name": "sword",
        "prototype_id": "weapon_sword_001",
        "item_id": "weapon_sword_001",
        "quantity": 1,
    }


@pytest.fixture
def sample_inventory_item():
    """Create a sample inventory item."""
    return {
        "item_name": "potion",
        "prototype_id": "consumable_potion_001",
        "item_id": "consumable_potion_001",
        "quantity": 1,
    }


@pytest.fixture
def sample_equipped_item():
    """Create a sample equipped item."""
    return {
        "item_name": "armor",
        "prototype_id": "armor_plate_001",
        "item_id": "armor_plate_001",
        "quantity": 1,
    }


def test_find_item_in_room_drops_success(sample_room_drop):
    """Test finding item in room drops by name."""
    room_drops = [sample_room_drop]
    result = _find_item_in_room_drops(room_drops, "sword")
    assert result == sample_room_drop


def test_find_item_in_room_drops_by_prototype_id(sample_room_drop):
    """Test finding item in room drops by prototype_id."""
    room_drops = [sample_room_drop]
    result = _find_item_in_room_drops(room_drops, "weapon_sword_001")
    assert result == sample_room_drop


def test_find_item_in_room_drops_not_found():
    """Test finding item in room drops when not found."""
    room_drops = [{"item_name": "sword", "prototype_id": "weapon_sword_001"}]
    result = _find_item_in_room_drops(room_drops, "potion")
    assert result is None


def test_find_item_in_room_drops_multiple_matches():
    """Test finding item in room drops with multiple matches."""
    room_drops = [
        {"item_name": "sword", "prototype_id": "weapon_sword_001"},
        {"item_name": "longsword", "prototype_id": "weapon_longsword_001"},
    ]
    result = _find_item_in_room_drops(room_drops, "sword")
    assert result is None  # Ambiguous


def test_find_item_in_room_drops_with_instance_number(sample_room_drop):
    """Test finding item in room drops with instance number."""
    room_drops = [sample_room_drop]
    result = _find_item_in_room_drops(room_drops, "sword", instance_number=1)
    assert result == sample_room_drop


def test_find_item_in_room_drops_instance_number_out_of_range(sample_room_drop):
    """Test finding item in room drops with invalid instance number."""
    room_drops = [sample_room_drop]
    result = _find_item_in_room_drops(room_drops, "sword", instance_number=2)
    assert result is None


def test_find_item_in_inventory_success(sample_inventory_item):
    """Test finding item in inventory by name."""
    inventory = [sample_inventory_item]
    result = _find_item_in_inventory(inventory, "potion")
    assert result == sample_inventory_item


def test_find_item_in_inventory_not_found():
    """Test finding item in inventory when not found."""
    inventory = [{"item_name": "potion", "prototype_id": "consumable_potion_001"}]
    result = _find_item_in_inventory(inventory, "sword")
    assert result is None


def test_find_item_in_equipped_success(sample_equipped_item):
    """Test finding item in equipped items by name."""
    equipped = {"chest": sample_equipped_item}
    result = _find_item_in_equipped(equipped, "armor")
    assert result == ("chest", sample_equipped_item)


def test_find_item_in_equipped_not_found():
    """Test finding item in equipped items when not found."""
    equipped = {"chest": {"item_name": "armor", "prototype_id": "armor_plate_001"}}
    result = _find_item_in_equipped(equipped, "sword")
    assert result is None


def test_get_item_description_from_prototype_success(mock_prototype_registry):
    """Test getting item description from prototype."""
    item = {"prototype_id": "weapon_sword_001", "item_name": "Sword"}
    result = _get_item_description_from_prototype(item, mock_prototype_registry)
    assert result == "Sword\nA test item description."


def test_get_item_description_from_prototype_no_registry():
    """Test getting item description when prototype registry is None."""
    item = {"prototype_id": "weapon_sword_001", "item_name": "Sword"}
    result = _get_item_description_from_prototype(item, None)
    assert result is None


def test_get_item_description_from_prototype_no_prototype_id():
    """Test getting item description when prototype_id is missing."""
    item = {"item_name": "Sword"}
    result = _get_item_description_from_prototype(item, MagicMock())
    assert result is None


def test_get_item_description_from_prototype_fallback(mock_prototype_registry):
    """Test getting item description with fallback name when prototype exists."""
    item = {"prototype_id": "weapon_sword_001"}
    result = _get_item_description_from_prototype(item, mock_prototype_registry, fallback_name="Fallback Item")
    # When prototype exists, it uses prototype.name, not fallback
    assert result is not None
    assert "Test Item" in result  # Uses prototype.name


def test_get_item_description_from_prototype_fallback_no_prototype():
    """Test getting item description with fallback name when prototype doesn't exist."""
    item = {"prototype_id": "weapon_sword_001"}
    registry = MagicMock()
    registry.get.return_value = None
    result = _get_item_description_from_prototype(item, registry, fallback_name="Fallback Item")
    assert result is not None
    assert "Fallback Item" in result


def test_check_item_in_location_success(mock_prototype_registry, sample_room_drop):
    """Test checking item in location successfully."""
    result = _check_item_in_location(sample_room_drop, mock_prototype_registry)
    assert result is not None
    assert "result" in result
    assert "sword" in result["result"].lower()


def test_check_item_in_location_with_location_name(mock_prototype_registry, sample_room_drop):
    """Test checking item in location with location name."""
    result = _check_item_in_location(sample_room_drop, mock_prototype_registry, location_name="chest")
    assert result is not None
    assert "chest" in result["result"].lower()


def test_check_item_in_location_not_found():
    """Test checking item in location when item not found."""
    result = _check_item_in_location(None, MagicMock())
    assert result is None


def test_check_item_in_location_no_prototype():
    """Test checking item in location when prototype not found."""
    item = {"item_name": "Unknown Item", "prototype_id": "unknown_001"}
    registry = MagicMock()
    registry.get.return_value = None
    result = _check_item_in_location(item, registry)
    assert result is not None
    assert "Unknown Item" in result["result"]


def test_check_equipped_item_success(mock_prototype_registry, sample_equipped_item):
    """Test checking equipped item successfully."""
    player = MagicMock()
    player.get_equipped_items.return_value = {"chest": sample_equipped_item}
    result = _check_equipped_item(player, "armor", None, mock_prototype_registry)
    assert result is not None
    assert "chest" in result["result"].lower()


def test_check_equipped_item_not_found(mock_prototype_registry):
    """Test checking equipped item when not found."""
    player = MagicMock()
    player.get_equipped_items.return_value = {}
    result = _check_equipped_item(player, "sword", None, mock_prototype_registry)
    assert result is None


@pytest.mark.asyncio
async def test_handle_item_look_in_room_drops(mock_prototype_registry, sample_room_drop):
    """Test handling item look when item is in room drops."""
    player = MagicMock()
    player.get_inventory.return_value = []
    player.get_equipped_items.return_value = {}
    command_data = {}
    result = await _handle_item_look(
        "sword", "sword", None, [sample_room_drop], player, mock_prototype_registry, command_data, "TestPlayer"
    )
    assert result is not None
    assert "result" in result
    assert "sword" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_item_look_in_inventory(mock_prototype_registry, sample_inventory_item):
    """Test handling item look when item is in inventory."""
    player = MagicMock()
    player.get_inventory.return_value = [sample_inventory_item]
    player.get_equipped_items.return_value = {}
    command_data = {}
    result = await _handle_item_look(
        "potion", "potion", None, [], player, mock_prototype_registry, command_data, "TestPlayer"
    )
    assert result is not None
    assert "result" in result
    assert "potion" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_item_look_in_equipped(mock_prototype_registry, sample_equipped_item):
    """Test handling item look when item is equipped."""
    player = MagicMock()
    player.get_inventory.return_value = []
    player.get_equipped_items.return_value = {"chest": sample_equipped_item}
    command_data = {}
    result = await _handle_item_look(
        "armor", "armor", None, [], player, mock_prototype_registry, command_data, "TestPlayer"
    )
    assert result is not None
    assert "result" in result
    assert "armor" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_item_look_not_found(mock_prototype_registry):
    """Test handling item look when item not found."""
    player = MagicMock()
    player.get_inventory.return_value = []
    player.get_equipped_items.return_value = {}
    command_data = {}
    result = await _handle_item_look(
        "sword", "sword", None, [], player, mock_prototype_registry, command_data, "TestPlayer"
    )
    assert result is not None
    assert "don't see" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_item_look_look_in_skips_equipped(mock_prototype_registry, sample_equipped_item):
    """Test handling item look with look_in flag skips equipped items."""
    player = MagicMock()
    player.get_inventory.return_value = []
    player.get_equipped_items.return_value = {"chest": sample_equipped_item}
    command_data = {"look_in": True}
    result = await _handle_item_look(
        "armor", "armor", None, [], player, mock_prototype_registry, command_data, "TestPlayer"
    )
    assert result is not None
    assert "don't see" in result["result"].lower()


@pytest.mark.asyncio
async def test_try_lookup_item_implicit_in_room_drops(mock_prototype_registry, sample_room_drop):
    """Test trying implicit lookup when item is in room drops."""
    player = MagicMock()
    player.get_inventory.return_value = []
    player.get_equipped_items.return_value = {}
    result = await _try_lookup_item_implicit("sword", None, [sample_room_drop], player, mock_prototype_registry)
    assert result is not None
    assert "sword" in result["result"].lower()


@pytest.mark.asyncio
async def test_try_lookup_item_implicit_not_found(mock_prototype_registry):
    """Test trying implicit lookup when item not found."""
    player = MagicMock()
    player.get_inventory.return_value = []
    player.get_equipped_items.return_value = {}
    result = await _try_lookup_item_implicit("sword", None, [], player, mock_prototype_registry)
    assert result is None


def test_find_item_in_room_drops_by_item_id(sample_room_drop):
    """Test finding item in room drops by item_id."""
    room_drops = [sample_room_drop]
    result = _find_item_in_room_drops(room_drops, "weapon_sword_001")
    assert result == sample_room_drop


def test_find_item_in_inventory_by_item_id(sample_inventory_item):
    """Test finding item in inventory by item_id."""
    inventory = [sample_inventory_item]
    result = _find_item_in_inventory(inventory, "consumable_potion_001")
    assert result == sample_inventory_item


def test_find_item_in_inventory_with_name_field():
    """Test finding item in inventory using 'name' field."""
    inventory = [{"name": "scroll", "item_id": "item_002"}]
    result = _find_item_in_inventory(inventory, "scroll")
    assert result is not None
    assert result["name"] == "scroll"


def test_find_item_in_equipped_by_prototype_id(sample_equipped_item):
    """Test finding item in equipped by prototype_id."""
    equipped = {"chest": sample_equipped_item}
    result = _find_item_in_equipped(equipped, "armor_plate_001")
    assert result == ("chest", sample_equipped_item)


def test_get_item_description_from_prototype_with_item_id():
    """Test getting item description using item_id when prototype_id missing."""
    item = {"item_id": "weapon_sword_001", "item_name": "Sword"}
    registry = MagicMock()
    prototype = MagicMock()
    prototype.name = "Test Item"
    prototype.long_description = "A test item description."
    registry.get.return_value = prototype
    result = _get_item_description_from_prototype(item, registry)
    assert result is not None
    assert "Sword" in result


def test_get_item_description_from_prototype_exception_handling():
    """Test getting item description handles exceptions."""
    item = {"prototype_id": "weapon_sword_001", "item_name": "Sword"}
    registry = MagicMock()
    # Make registry.get raise an exception
    registry.get.side_effect = KeyError("test")
    result = _get_item_description_from_prototype(item, registry)
    assert result is not None
    assert "Sword" in result
    assert "nothing remarkable" in result


def test_check_item_in_location_fallback_name():
    """Test checking item in location uses fallback when no prototype."""
    item = {"item_name": "Unknown Item"}
    registry = MagicMock()
    registry.get.return_value = None
    result = _check_item_in_location(item, registry)
    assert result is not None
    assert "Unknown Item" in result["result"]


def test_check_equipped_item_no_get_equipped_items_method(mock_prototype_registry):
    """Test checking equipped item when player has no get_equipped_items method."""
    player = MagicMock()
    # Remove get_equipped_items method
    del player.get_equipped_items
    result = _check_equipped_item(player, "armor", None, mock_prototype_registry)
    assert result is None


@pytest.mark.asyncio
async def test_handle_item_look_with_instance_number(mock_prototype_registry, sample_room_drop):
    """Test handling item look with instance number."""
    player = MagicMock()
    player.get_inventory.return_value = []
    player.get_equipped_items.return_value = {}
    command_data = {}
    # Add duplicate items
    room_drops = [sample_room_drop, {**sample_room_drop, "item_id": "weapon_sword_002"}]
    result = await _handle_item_look(
        "sword", "sword", 1, room_drops, player, mock_prototype_registry, command_data, "TestPlayer"
    )
    assert result is not None
    assert "result" in result


@pytest.mark.asyncio
async def test_try_lookup_item_implicit_in_equipped(mock_prototype_registry, sample_equipped_item):
    """Test trying implicit lookup when item is equipped."""
    player = MagicMock()
    player.get_inventory.return_value = []
    player.get_equipped_items.return_value = {"chest": sample_equipped_item}
    result = await _try_lookup_item_implicit("armor", None, [], player, mock_prototype_registry)
    assert result is not None
    assert "armor" in result["result"].lower() or "equipped" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_item_look_player_no_get_inventory(mock_prototype_registry, sample_room_drop):
    """Test _handle_item_look() when player has no get_inventory method."""
    player = MagicMock()
    del player.get_inventory
    command_data = {}
    result = await _handle_item_look(
        "sword", "sword", None, [sample_room_drop], player, mock_prototype_registry, command_data, "TestPlayer"
    )
    assert result is not None
    assert "result" in result


@pytest.mark.asyncio
async def test_try_lookup_item_implicit_player_no_get_inventory(mock_prototype_registry):
    """Test _try_lookup_item_implicit() when player has no get_inventory method."""
    player = MagicMock()
    del player.get_inventory
    result = await _try_lookup_item_implicit("sword", None, [], player, mock_prototype_registry)
    assert result is None


@pytest.mark.asyncio
async def test_try_lookup_item_implicit_player_no_get_equipped_items(mock_prototype_registry):
    """Test _try_lookup_item_implicit() when player has no get_equipped_items method."""
    player = MagicMock()
    player.get_inventory.return_value = []
    del player.get_equipped_items
    result = await _try_lookup_item_implicit("sword", None, [], player, mock_prototype_registry)
    assert result is None
