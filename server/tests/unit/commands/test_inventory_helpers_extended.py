"""
Extended unit tests for inventory command helper functions.

Tests additional helper functions used by inventory commands.
"""

from unittest.mock import AsyncMock, MagicMock

import pytest

from server.commands.inventory_command_helpers import (
    broadcast_room_event,
    clone_inventory,
    persist_player,
    resolve_player,
)

# Note: _render_inventory doesn't exist - may need to be removed from tests or implemented
from server.exceptions import ValidationError as MythosValidationError
from server.schemas.shared import InventorySchemaValidationError


def test_clone_inventory():
    """Test clone_inventory creates deep copy."""
    player = MagicMock()
    player.get_inventory.return_value = [{"item_name": "sword", "quantity": 1}]

    result = clone_inventory(player)

    assert result == [{"item_name": "sword", "quantity": 1}]
    # Verify it's a deep copy (modifying result shouldn't affect original)
    result[0]["quantity"] = 2
    assert player.get_inventory()[0]["quantity"] == 1


@pytest.mark.asyncio
async def test_broadcast_room_event_no_connection_manager():
    """Test _broadcast_room_event when connection_manager is None."""
    await broadcast_room_event(None, "test_room", {"event": "test"})


@pytest.mark.asyncio
async def test_broadcast_room_event_no_broadcast_method():
    """Test broadcast_room_event when connection_manager has no broadcast_to_room."""
    connection_manager = MagicMock()
    del connection_manager.broadcast_to_room

    await broadcast_room_event(connection_manager, "test_room", {"event": "test"})


@pytest.mark.asyncio
async def test_broadcast_room_event_success():
    """Test broadcast_room_event successful broadcast."""
    connection_manager = MagicMock()
    connection_manager.broadcast_to_room = MagicMock(return_value=None)

    await broadcast_room_event(connection_manager, "test_room", {"event": "test"})

    connection_manager.broadcast_to_room.assert_called_once()


@pytest.mark.asyncio
async def test_broadcast_room_event_async():
    """Test broadcast_room_event with async broadcast."""
    connection_manager = MagicMock()
    connection_manager.broadcast_to_room = AsyncMock(return_value=None)

    await broadcast_room_event(connection_manager, "test_room", {"event": "test"})

    connection_manager.broadcast_to_room.assert_awaited_once()


@pytest.mark.asyncio
async def test_broadcast_room_event_with_exclude():
    """Test broadcast_room_event with exclude_player."""
    connection_manager = MagicMock()
    connection_manager.broadcast_to_room = MagicMock(return_value=None)

    await broadcast_room_event(connection_manager, "test_room", {"event": "test"}, exclude_player="Player1")

    connection_manager.broadcast_to_room.assert_called_once_with(
        "test_room", {"event": "test"}, exclude_player="Player1"
    )


@pytest.mark.asyncio
async def test_broadcast_room_event_error():
    """Test broadcast_room_event handles errors gracefully."""
    connection_manager = MagicMock()
    connection_manager.broadcast_to_room = MagicMock(side_effect=Exception("Broadcast error"))

    # Should not raise
    await broadcast_room_event(connection_manager, "test_room", {"event": "test"})


@pytest.mark.asyncio
async def test_persist_player_success():
    """Test _persist_player successful save."""
    persistence = MagicMock()
    persistence.save_player = MagicMock()
    player = MagicMock()
    player.name = "TestPlayer"

    result = await persist_player(persistence, player)

    assert result is None
    persistence.save_player.assert_called_once_with(player)


@pytest.mark.asyncio
async def test_persist_player_validation_error():
    """Test _persist_player handles InventorySchemaValidationError."""
    persistence = MagicMock()
    persistence.save_player = MagicMock(side_effect=InventorySchemaValidationError("Invalid schema"))
    player = MagicMock()
    player.name = "TestPlayer"

    result = await persist_player(persistence, player)

    assert result is not None
    assert "schema validation" in result["result"].lower()


@pytest.mark.asyncio
async def test_persist_player_general_error():
    """Test _persist_player handles general errors."""
    persistence = MagicMock()
    persistence.save_player = MagicMock(side_effect=Exception("Database error"))
    player = MagicMock()
    player.name = "TestPlayer"

    result = await persist_player(persistence, player)

    assert result is not None
    assert "error occurred" in result["result"].lower()


# Note: _render_inventory function doesn't exist - tests skipped
# def test_render_inventory_empty():
#     """Test _render_inventory with empty inventory."""
#     result = _render_inventory([], {})
#     assert "No items" in result or "0 /" in result
#     assert "Nothing equipped" in result
#
#
# def test_render_inventory_with_items():
#     """Test _render_inventory with items."""
#     inventory = [
#         {"item_name": "sword", "quantity": 1, "slot_type": "inventory"},
#         {"item_name": "potion", "quantity": 3, "slot_type": "inventory"},
#     ]
#     result = _render_inventory(inventory, {})
#     assert "sword" in result
#     assert "potion" in result
#     assert "x1" in result
#     assert "x3" in result
#
#
# def test_render_inventory_with_equipped():
#     """Test _render_inventory with equipped items."""
#     inventory = []
#     equipped = {"main_hand": {"item_name": "sword", "quantity": 1}}
#     result = _render_inventory(inventory, equipped)
#     assert "main_hand" in result
#     assert "sword" in result


# Note: _render_inventory function doesn't exist - test skipped
# def test_render_inventory_with_containers():
#     """Test _render_inventory with container contents."""
#     inventory = []
#     equipped = {"backpack": {"item_name": "Backpack", "quantity": 1, "metadata": {"container": {}}}}
#     container_contents = {"backpack": [{"item_name": "scroll", "quantity": 1}]}
#     container_capacities = {"backpack": 20}
#     result = _render_inventory(inventory, equipped, container_contents=container_contents, container_capacities=container_capacities)
#     assert "Backpack" in result
#     assert "scroll" in result


@pytest.mark.asyncio
async def test_resolve_player_no_persistence():
    """Test _resolve_player when persistence is None."""
    result = await resolve_player(None, {"username": "TestPlayer"}, "TestPlayer")

    assert result[0] is None
    assert result[1] is not None
    assert "not available" in result[1]["result"].lower()


@pytest.mark.asyncio
async def test_resolve_player_username_error():
    """Test _resolve_player when username resolution fails."""
    persistence = MagicMock()

    # Test the error path - function catches the exception internally
    from unittest.mock import patch

    with patch(
        "server.commands.inventory_command_helpers.get_username_from_user",
        side_effect=MythosValidationError("Invalid user"),
    ):
        result = await resolve_player(persistence, {}, "TestPlayer")
        assert result[0] is None
        assert result[1] is not None
        assert "Invalid user" in result[1]["result"]


@pytest.mark.asyncio
async def test_resolve_player_not_found():
    """Test _resolve_player when player is not found."""
    persistence = AsyncMock()
    persistence.get_player_by_name = AsyncMock(return_value=None)

    from unittest.mock import patch

    with patch("server.commands.inventory_command_helpers.get_username_from_user", return_value="TestPlayer"):
        result = await resolve_player(persistence, {"username": "TestPlayer"}, "TestPlayer")
        assert result[0] is None
        assert result[1] is not None
        assert "not found" in result[1]["result"].lower()


@pytest.mark.asyncio
async def test_resolve_player_success():
    """Test _resolve_player successful resolution."""
    persistence = AsyncMock()
    mock_player = MagicMock()
    persistence.get_player_by_name = AsyncMock(return_value=mock_player)

    from unittest.mock import patch

    with patch("server.commands.inventory_command_helpers.get_username_from_user", return_value="TestPlayer"):
        result = await resolve_player(persistence, {"username": "TestPlayer"}, "TestPlayer")
        assert result[0] == mock_player
        assert result[1] is None


@pytest.mark.asyncio
async def test_resolve_player_persistence_error():
    """Test _resolve_player when persistence raises error."""
    persistence = AsyncMock()
    persistence.get_player_by_name = AsyncMock(side_effect=Exception("Database error"))

    from unittest.mock import patch

    with patch("server.commands.inventory_command_helpers.get_username_from_user", return_value="TestPlayer"):
        result = await resolve_player(persistence, {"username": "TestPlayer"}, "TestPlayer")
        assert result[0] is None
        assert result[1] is not None
        assert "error" in result[1]["result"].lower()
