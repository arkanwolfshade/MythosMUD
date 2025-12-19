"""
Tests for look item functionality.

This module tests item lookup functions including finding items in room drops,
inventory, equipped items, and formatting item descriptions.
"""

from typing import Any
from unittest.mock import MagicMock, patch

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


class TestFindItemInRoomDrops:
    """Test _find_item_in_room_drops function."""

    def test_find_item_in_room_drops_by_name(self) -> None:
        """Test finding item by name."""
        room_drops = [{"item_name": "sword", "item_id": "item-1"}]
        result = _find_item_in_room_drops(room_drops, "sword")
        assert result == room_drops[0]

    def test_find_item_in_room_drops_by_prototype_id(self) -> None:
        """Test finding item by prototype_id."""
        room_drops = [{"item_name": "sword", "prototype_id": "proto-123"}]
        result = _find_item_in_room_drops(room_drops, "proto-123")
        assert result == room_drops[0]

    def test_find_item_in_room_drops_by_item_id(self) -> None:
        """Test finding item by item_id."""
        room_drops = [{"item_name": "sword", "item_id": "item-456"}]
        result = _find_item_in_room_drops(room_drops, "item-456")
        assert result == room_drops[0]

    def test_find_item_in_room_drops_case_insensitive(self) -> None:
        """Test finding item case-insensitively."""
        room_drops = [{"item_name": "Sword", "item_id": "item-1"}]
        result = _find_item_in_room_drops(room_drops, "SWORD")
        assert result == room_drops[0]

    def test_find_item_in_room_drops_partial_match(self) -> None:
        """Test finding item with partial name match."""
        room_drops = [{"item_name": "iron sword", "item_id": "item-1"}]
        result = _find_item_in_room_drops(room_drops, "sword")
        assert result == room_drops[0]

    def test_find_item_in_room_drops_not_found(self) -> None:
        """Test when item is not found."""
        room_drops = [{"item_name": "sword", "item_id": "item-1"}]
        result = _find_item_in_room_drops(room_drops, "axe")
        assert result is None

    def test_find_item_in_room_drops_empty_list(self) -> None:
        """Test with empty room drops."""
        result = _find_item_in_room_drops([], "sword")
        assert result is None

    def test_find_item_in_room_drops_with_instance_number(self) -> None:
        """Test finding item with instance number."""
        room_drops = [
            {"item_name": "sword", "item_id": "item-1"},
            {"item_name": "sword", "item_id": "item-2"},
        ]
        result = _find_item_in_room_drops(room_drops, "sword", instance_number=2)
        assert result == room_drops[1]

    def test_find_item_in_room_drops_instance_number_out_of_range(self) -> None:
        """Test with instance number out of range."""
        room_drops = [{"item_name": "sword", "item_id": "item-1"}]
        result = _find_item_in_room_drops(room_drops, "sword", instance_number=5)
        assert result is None

    def test_find_item_in_room_drops_instance_number_zero(self) -> None:
        """Test with instance number zero."""
        room_drops = [{"item_name": "sword", "item_id": "item-1"}]
        result = _find_item_in_room_drops(room_drops, "sword", instance_number=0)
        assert result is None

    def test_find_item_in_room_drops_multiple_matches(self) -> None:
        """Test when multiple items match (returns None for ambiguity)."""
        room_drops = [
            {"item_name": "sword", "item_id": "item-1"},
            {"item_name": "sword", "item_id": "item-2"},
        ]
        result = _find_item_in_room_drops(room_drops, "sword")
        assert result is None  # Ambiguous

    def test_find_item_in_room_drops_none_values(self) -> None:
        """Test handling None values in item fields."""
        room_drops = [{"item_name": None, "prototype_id": "proto-123"}]
        result = _find_item_in_room_drops(room_drops, "proto-123")
        assert result == room_drops[0]


class TestFindItemInInventory:
    """Test _find_item_in_inventory function."""

    def test_find_item_in_inventory_by_name(self) -> None:
        """Test finding item by name."""
        inventory = [{"item_name": "sword", "item_id": "item-1"}]
        result = _find_item_in_inventory(inventory, "sword")
        assert result == inventory[0]

    def test_find_item_in_inventory_by_name_alt_key(self) -> None:
        """Test finding item using 'name' key instead of 'item_name'."""
        inventory = [{"name": "sword", "item_id": "item-1"}]
        result = _find_item_in_inventory(inventory, "sword")
        assert result == inventory[0]

    def test_find_item_in_inventory_by_prototype_id(self) -> None:
        """Test finding item by prototype_id."""
        inventory = [{"item_name": "sword", "prototype_id": "proto-123"}]
        result = _find_item_in_inventory(inventory, "proto-123")
        assert result == inventory[0]

    def test_find_item_in_inventory_by_item_id_alt_key(self) -> None:
        """Test finding item using 'item_id' as fallback for prototype_id."""
        inventory = [{"item_name": "sword", "item_id": "proto-123"}]
        result = _find_item_in_inventory(inventory, "proto-123")
        assert result == inventory[0]

    def test_find_item_in_inventory_case_insensitive(self) -> None:
        """Test finding item case-insensitively."""
        inventory = [{"item_name": "Sword", "item_id": "item-1"}]
        result = _find_item_in_inventory(inventory, "SWORD")
        assert result == inventory[0]

    def test_find_item_in_inventory_not_found(self) -> None:
        """Test when item is not found."""
        inventory = [{"item_name": "sword", "item_id": "item-1"}]
        result = _find_item_in_inventory(inventory, "axe")
        assert result is None

    def test_find_item_in_inventory_with_instance_number(self) -> None:
        """Test finding item with instance number."""
        inventory = [
            {"item_name": "sword", "item_id": "item-1"},
            {"item_name": "sword", "item_id": "item-2"},
        ]
        result = _find_item_in_inventory(inventory, "sword", instance_number=1)
        assert result == inventory[0]

    def test_find_item_in_inventory_multiple_matches(self) -> None:
        """Test when multiple items match (returns None for ambiguity)."""
        inventory = [
            {"item_name": "sword", "item_id": "item-1"},
            {"item_name": "sword", "item_id": "item-2"},
        ]
        result = _find_item_in_inventory(inventory, "sword")
        assert result is None  # Ambiguous


class TestFindItemInEquipped:
    """Test _find_item_in_equipped function."""

    def test_find_item_in_equipped_by_name(self) -> None:
        """Test finding equipped item by name."""
        equipped = {"hand": {"item_name": "sword", "item_id": "item-1"}}
        result = _find_item_in_equipped(equipped, "sword")
        assert result == ("hand", equipped["hand"])

    def test_find_item_in_equipped_by_prototype_id(self) -> None:
        """Test finding equipped item by prototype_id."""
        equipped = {"hand": {"item_name": "sword", "prototype_id": "proto-123"}}
        result = _find_item_in_equipped(equipped, "proto-123")
        assert result == ("hand", equipped["hand"])

    def test_find_item_in_equipped_not_found(self) -> None:
        """Test when equipped item is not found."""
        equipped = {"hand": {"item_name": "sword", "item_id": "item-1"}}
        result = _find_item_in_equipped(equipped, "axe")
        assert result is None

    def test_find_item_in_equipped_with_instance_number(self) -> None:
        """Test finding equipped item with instance number."""
        equipped = {
            "hand": {"item_name": "sword", "item_id": "item-1"},
            "offhand": {"item_name": "sword", "item_id": "item-2"},
        }
        result = _find_item_in_equipped(equipped, "sword", instance_number=2)
        assert result == ("offhand", equipped["offhand"])

    def test_find_item_in_equipped_multiple_matches(self) -> None:
        """Test when multiple equipped items match (returns None for ambiguity)."""
        equipped = {
            "hand": {"item_name": "sword", "item_id": "item-1"},
            "offhand": {"item_name": "sword", "item_id": "item-2"},
        }
        result = _find_item_in_equipped(equipped, "sword")
        assert result is None  # Ambiguous


class TestGetItemDescriptionFromPrototype:
    """Test _get_item_description_from_prototype function."""

    def test_get_item_description_from_prototype_success(self) -> None:
        """Test getting description from prototype registry."""
        item_found = {"item_name": "sword", "prototype_id": "proto-123"}
        mock_prototype = MagicMock()
        mock_prototype.name = "Iron Sword"
        mock_prototype.long_description = "A sharp iron sword."
        mock_registry = MagicMock()
        mock_registry.get.return_value = mock_prototype

        result = _get_item_description_from_prototype(item_found, mock_registry)

        assert result == "sword\nA sharp iron sword."

    def test_get_item_description_from_prototype_no_registry(self) -> None:
        """Test when prototype registry is None."""
        item_found = {"item_name": "sword", "prototype_id": "proto-123"}
        result = _get_item_description_from_prototype(item_found, None)
        assert result is None

    def test_get_item_description_from_prototype_no_prototype_id(self) -> None:
        """Test when prototype_id is missing."""
        item_found = {"item_name": "sword"}
        mock_registry = MagicMock()
        result = _get_item_description_from_prototype(item_found, mock_registry)
        assert result is None

    def test_get_item_description_from_prototype_prototype_not_found(self) -> None:
        """Test when prototype is not found in registry."""
        item_found = {"item_name": "sword", "prototype_id": "proto-123"}
        mock_registry = MagicMock()
        mock_registry.get.return_value = None

        result = _get_item_description_from_prototype(item_found, mock_registry)

        assert result == "sword\nYou see nothing remarkable about it."

    def test_get_item_description_from_prototype_uses_fallback_name(self) -> None:
        """Test using fallback name when item_name is missing."""
        item_found = {"prototype_id": "proto-123"}
        mock_prototype = MagicMock()
        mock_prototype.name = "Iron Sword"
        mock_prototype.long_description = "A sharp iron sword."
        mock_registry = MagicMock()
        mock_registry.get.return_value = mock_prototype

        result = _get_item_description_from_prototype(item_found, mock_registry, fallback_name="Sword")

        assert result == "Iron Sword\nA sharp iron sword."

    def test_get_item_description_from_prototype_attribute_error(self) -> None:
        """Test handling AttributeError."""
        item_found = {"item_name": "sword", "prototype_id": "proto-123"}
        mock_registry = MagicMock()
        mock_registry.get.side_effect = AttributeError("Attribute error")

        result = _get_item_description_from_prototype(item_found, mock_registry)

        assert result == "sword\nYou see nothing remarkable about it."

    def test_get_item_description_from_prototype_uses_item_id_as_prototype_id(self) -> None:
        """Test using item_id as fallback for prototype_id."""
        item_found = {"item_name": "sword", "item_id": "proto-123"}
        mock_prototype = MagicMock()
        mock_prototype.name = "Iron Sword"
        mock_prototype.long_description = "A sharp iron sword."
        mock_registry = MagicMock()
        mock_registry.get.return_value = mock_prototype

        result = _get_item_description_from_prototype(item_found, mock_registry)

        assert result == "sword\nA sharp iron sword."


class TestCheckItemInLocation:
    """Test _check_item_in_location function."""

    def test_check_item_in_location_with_description(self) -> None:
        """Test checking item with description."""
        item_found = {"item_name": "sword", "prototype_id": "proto-123"}
        mock_prototype = MagicMock()
        mock_prototype.name = "Iron Sword"
        mock_prototype.long_description = "A sharp iron sword."
        mock_registry = MagicMock()
        mock_registry.get.return_value = mock_prototype

        result = _check_item_in_location(item_found, mock_registry)

        assert result == {"result": "sword\nA sharp iron sword."}

    def test_check_item_in_location_with_location_name(self) -> None:
        """Test checking item with location name."""
        item_found = {"item_name": "sword", "prototype_id": "proto-123"}
        mock_prototype = MagicMock()
        mock_prototype.name = "Iron Sword"
        mock_prototype.long_description = "A sharp iron sword."
        mock_registry = MagicMock()
        mock_registry.get.return_value = mock_prototype

        result = _check_item_in_location(item_found, mock_registry, location_name="hand")

        assert result == {"result": "sword (hand)\nA sharp iron sword."}

    def test_check_item_in_location_no_item(self) -> None:
        """Test when item is None."""
        result = _check_item_in_location(None, MagicMock())
        assert result is None

    def test_check_item_in_location_no_prototype_fallback(self) -> None:
        """Test fallback when prototype is not found."""
        item_found = {"item_name": "sword"}
        result = _check_item_in_location(item_found, None)

        assert result == {"result": "sword\nYou see nothing remarkable about it."}

    def test_check_item_in_location_no_prototype_with_location(self) -> None:
        """Test fallback with location name when prototype is not found."""
        item_found = {"item_name": "sword"}
        result = _check_item_in_location(item_found, None, location_name="hand")

        assert result == {"result": "sword (hand)\nYou see nothing remarkable about it."}

    def test_check_item_in_location_no_name_fallback(self) -> None:
        """Test fallback when item_name is missing but item_found is not empty."""
        # When item_found has no item_name/name keys, it uses "Unknown Item" as fallback
        # _get_item_description_from_prototype returns None (no prototype_registry)
        # Then _check_item_in_location should use fallback path
        # Note: Empty dict {} is falsy, so the function returns None early
        # We need a dict with some keys but no item_name/name
        item_found = {"some_other_key": "value"}
        result = _check_item_in_location(item_found, None)

        # The function should return a result with fallback name
        assert result == {"result": "Unknown Item\nYou see nothing remarkable about it."}

    def test_check_item_in_location_empty_dict(self) -> None:
        """Test when item_found is empty dict (returns None)."""
        # Empty dict is falsy, so function returns None early
        item_found: dict[str, Any] = {}
        result = _check_item_in_location(item_found, None)

        assert result is None


class TestCheckEquippedItem:
    """Test _check_equipped_item function."""

    def test_check_equipped_item_found(self) -> None:
        """Test checking equipped item when found."""
        mock_player = MagicMock()
        mock_player.get_equipped_items.return_value = {"hand": {"item_name": "sword", "prototype_id": "proto-123"}}
        mock_prototype = MagicMock()
        mock_prototype.name = "Iron Sword"
        mock_prototype.long_description = "A sharp iron sword."
        mock_registry = MagicMock()
        mock_registry.get.return_value = mock_prototype

        result = _check_equipped_item(mock_player, "sword", None, mock_registry)

        assert result == {"result": "sword (equipped in hand)\nA sharp iron sword."}

    def test_check_equipped_item_not_found(self) -> None:
        """Test when equipped item is not found."""
        mock_player = MagicMock()
        mock_player.get_equipped_items.return_value = {"hand": {"item_name": "sword", "item_id": "item-1"}}
        mock_registry = MagicMock()

        result = _check_equipped_item(mock_player, "axe", None, mock_registry)

        assert result is None

    def test_check_equipped_item_no_get_equipped_items_method(self) -> None:
        """Test when player doesn't have get_equipped_items method."""
        mock_player = MagicMock()
        delattr(mock_player, "get_equipped_items")
        mock_registry = MagicMock()

        result = _check_equipped_item(mock_player, "sword", None, mock_registry)

        assert result is None


class TestHandleItemLook:
    """Test _handle_item_look function."""

    @pytest.mark.asyncio
    async def test_handle_item_look_in_room_drops(self) -> None:
        """Test looking at item in room drops."""
        room_drops = [{"item_name": "sword", "prototype_id": "proto-123"}]
        mock_player = MagicMock()
        mock_prototype = MagicMock()
        mock_prototype.name = "Iron Sword"
        mock_prototype.long_description = "A sharp iron sword."
        mock_registry = MagicMock()
        mock_registry.get.return_value = mock_prototype

        with patch("server.commands.look_item.logger"):
            result = await _handle_item_look(
                "sword", "sword", None, room_drops, mock_player, mock_registry, {}, "testuser"
            )

            assert result == {"result": "sword\nA sharp iron sword."}

    @pytest.mark.asyncio
    async def test_handle_item_look_in_inventory(self) -> None:
        """Test looking at item in inventory."""
        room_drops: list[Any] = []
        mock_player = MagicMock()
        mock_player.get_inventory.return_value = [{"item_name": "sword", "prototype_id": "proto-123"}]
        mock_prototype = MagicMock()
        mock_prototype.name = "Iron Sword"
        mock_prototype.long_description = "A sharp iron sword."
        mock_registry = MagicMock()
        mock_registry.get.return_value = mock_prototype

        with patch("server.commands.look_item.logger"):
            result = await _handle_item_look(
                "sword", "sword", None, room_drops, mock_player, mock_registry, {}, "testuser"
            )

            assert result == {"result": "sword\nA sharp iron sword."}

    @pytest.mark.asyncio
    async def test_handle_item_look_in_equipped(self) -> None:
        """Test looking at equipped item."""
        room_drops: list[Any] = []
        mock_player = MagicMock()
        mock_player.get_inventory.return_value = []
        mock_player.get_equipped_items.return_value = {"hand": {"item_name": "sword", "prototype_id": "proto-123"}}
        mock_prototype = MagicMock()
        mock_prototype.name = "Iron Sword"
        mock_prototype.long_description = "A sharp iron sword."
        mock_registry = MagicMock()
        mock_registry.get.return_value = mock_prototype

        with patch("server.commands.look_item.logger"):
            result = await _handle_item_look(
                "sword", "sword", None, room_drops, mock_player, mock_registry, {}, "testuser"
            )

            assert result is not None
            assert "sword" in result["result"]
            assert result is not None
            assert "equipped in hand" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_item_look_not_found(self) -> None:
        """Test when item is not found."""
        room_drops: list[Any] = []
        mock_player = MagicMock()
        mock_player.get_inventory.return_value = []
        mock_player.get_equipped_items.return_value = {}
        mock_registry = MagicMock()

        with patch("server.commands.look_item.logger") as mock_logger:
            result = await _handle_item_look(
                "sword", "sword", None, room_drops, mock_player, mock_registry, {}, "testuser"
            )

            assert result is not None
            assert "don't see any 'sword'" in result["result"]
            mock_logger.debug.assert_called()

    @pytest.mark.asyncio
    async def test_handle_item_look_skips_equipped_when_look_in(self) -> None:
        """Test that equipped items are skipped when look_in is True."""
        room_drops: list[Any] = []
        mock_player = MagicMock()
        mock_player.get_inventory.return_value = []
        mock_player.get_equipped_items.return_value = {"hand": {"item_name": "sword", "prototype_id": "proto-123"}}
        mock_registry = MagicMock()

        with patch("server.commands.look_item.logger"):
            result = await _handle_item_look(
                "sword", "sword", None, room_drops, mock_player, mock_registry, {"look_in": True}, "testuser"
            )

            # Should not find equipped item when looking inside container
            assert result is not None
            assert "don't see any 'sword'" in result["result"]


class TestTryLookupItemImplicit:
    """Test _try_lookup_item_implicit function."""

    @pytest.mark.asyncio
    async def test_try_lookup_item_implicit_in_room_drops(self) -> None:
        """Test implicit lookup in room drops."""
        room_drops = [{"item_name": "sword", "prototype_id": "proto-123"}]
        mock_player = MagicMock()
        mock_prototype = MagicMock()
        mock_prototype.name = "Iron Sword"
        mock_prototype.long_description = "A sharp iron sword."
        mock_registry = MagicMock()
        mock_registry.get.return_value = mock_prototype

        result = await _try_lookup_item_implicit("sword", None, room_drops, mock_player, mock_registry)

        assert result == {"result": "sword\nA sharp iron sword."}

    @pytest.mark.asyncio
    async def test_try_lookup_item_implicit_in_inventory(self) -> None:
        """Test implicit lookup in inventory."""
        room_drops: list[Any] = []
        mock_player = MagicMock()
        mock_player.get_inventory.return_value = [{"item_name": "sword", "prototype_id": "proto-123"}]
        mock_prototype = MagicMock()
        mock_prototype.name = "Iron Sword"
        mock_prototype.long_description = "A sharp iron sword."
        mock_registry = MagicMock()
        mock_registry.get.return_value = mock_prototype

        result = await _try_lookup_item_implicit("sword", None, room_drops, mock_player, mock_registry)

        assert result == {"result": "sword\nA sharp iron sword."}

    @pytest.mark.asyncio
    async def test_try_lookup_item_implicit_in_equipped(self) -> None:
        """Test implicit lookup in equipped items."""
        room_drops: list[Any] = []
        mock_player = MagicMock()
        mock_player.get_inventory.return_value = []
        mock_player.get_equipped_items.return_value = {"hand": {"item_name": "sword", "prototype_id": "proto-123"}}
        mock_prototype = MagicMock()
        mock_prototype.name = "Iron Sword"
        mock_prototype.long_description = "A sharp iron sword."
        mock_registry = MagicMock()
        mock_registry.get.return_value = mock_prototype

        result = await _try_lookup_item_implicit("sword", None, room_drops, mock_player, mock_registry)

        assert result is not None
        assert "sword" in result["result"]
        assert result is not None
        assert "equipped in hand" in result["result"]

    @pytest.mark.asyncio
    async def test_try_lookup_item_implicit_not_found(self) -> None:
        """Test implicit lookup when item is not found."""
        room_drops: list[Any] = []
        mock_player = MagicMock()
        mock_player.get_inventory.return_value = []
        mock_player.get_equipped_items.return_value = {}
        mock_registry = MagicMock()

        result = await _try_lookup_item_implicit("sword", None, room_drops, mock_player, mock_registry)

        assert result is None
