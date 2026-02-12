"""
Unit tests for additional inventory_commands helper functions.

Tests helper functions in inventory_commands.py module that weren't covered in the first test file.
"""

from unittest.mock import AsyncMock, MagicMock

import pytest

from server.commands.inventory_command_helpers import (
    broadcast_room_event,
    clone_inventory,
    persist_player,
    resolve_player,
    resolve_state,
)


def test_resolve_state_with_app():
    """Test _resolve_state() extracts persistence and connection_manager from request."""
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_persistence = MagicMock()
    mock_connection_manager = MagicMock()
    mock_state.persistence = mock_persistence
    mock_state.connection_manager = mock_connection_manager
    mock_app.state = mock_state
    mock_request = MagicMock()
    mock_request.app = mock_app

    persistence, connection_manager = resolve_state(mock_request)

    assert persistence == mock_persistence
    assert connection_manager == mock_connection_manager


def test_resolve_state_no_app():
    """Test _resolve_state() returns None when request has no app."""
    mock_request = MagicMock()
    mock_request.app = None

    persistence, connection_manager = resolve_state(mock_request)

    assert persistence is None
    assert connection_manager is None


def test_resolve_state_no_state():
    """Test _resolve_state() returns None when app has no state."""
    mock_app = MagicMock()
    mock_app.state = None
    mock_request = MagicMock()
    mock_request.app = mock_app

    persistence, connection_manager = resolve_state(mock_request)

    assert persistence is None
    assert connection_manager is None


@pytest.mark.asyncio
async def test_resolve_player_success():
    """Test _resolve_player() returns player when found."""
    mock_persistence = MagicMock()
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    current_user = {"name": "TestPlayer"}

    player, error = await resolve_player(mock_persistence, current_user, "TestPlayer")

    assert player == mock_player
    assert error is None


@pytest.mark.asyncio
async def test_resolve_player_no_persistence():
    """Test resolve_player() returns error when persistence is None."""
    current_user = {"name": "TestPlayer"}

    player, error = await resolve_player(None, current_user, "TestPlayer")

    assert player is None
    assert error is not None
    assert "not available" in error["result"].lower()


@pytest.mark.asyncio
async def test_resolve_player_not_found():
    """Test _resolve_player() returns error when player not found."""
    mock_persistence = MagicMock()
    mock_persistence.get_player_by_name = AsyncMock(return_value=None)
    current_user = {"name": "TestPlayer"}

    player, error = await resolve_player(mock_persistence, current_user, "TestPlayer")

    assert player is None
    assert error is not None
    assert "not found" in error["result"].lower()


def test_clone_inventory():
    """Test _clone_inventory() returns deep copy of inventory."""
    player = MagicMock()
    original_inventory = [{"item_id": "sword_001", "quantity": 1}]
    player.get_inventory.return_value = original_inventory

    result = clone_inventory(player)

    assert result == original_inventory
    assert result is not original_inventory  # Should be a copy
    # Modify original to verify deep copy
    original_inventory[0]["quantity"] = 2
    assert result[0]["quantity"] == 1  # Copy should be unaffected


@pytest.mark.asyncio
async def test_broadcast_room_event_with_connection_manager():
    """Test _broadcast_room_event() calls broadcast_to_room."""
    mock_connection_manager = MagicMock()
    mock_connection_manager.broadcast_to_room = AsyncMock()
    event = {"type": "test_event", "data": "test"}

    await broadcast_room_event(mock_connection_manager, "room_001", event)

    mock_connection_manager.broadcast_to_room.assert_called_once_with("room_001", event, exclude_player=None)


@pytest.mark.asyncio
async def test_broadcast_room_event_with_exclude_player():
    """Test broadcast_room_event() passes exclude_player parameter."""
    mock_connection_manager = MagicMock()
    mock_connection_manager.broadcast_to_room = AsyncMock()
    event = {"type": "test_event", "data": "test"}

    await broadcast_room_event(mock_connection_manager, "room_001", event, exclude_player="player_001")

    mock_connection_manager.broadcast_to_room.assert_called_once_with("room_001", event, exclude_player="player_001")


@pytest.mark.asyncio
async def test_broadcast_room_event_no_connection_manager():
    """Test broadcast_room_event() handles None connection_manager."""
    event = {"type": "test_event", "data": "test"}

    # Should not raise
    await broadcast_room_event(None, "room_001", event)


@pytest.mark.asyncio
async def test_broadcast_room_event_no_broadcast_method():
    """Test _broadcast_room_event() handles connection_manager without broadcast_to_room."""
    mock_connection_manager = MagicMock()
    del mock_connection_manager.broadcast_to_room
    event = {"type": "test_event", "data": "test"}

    # Should not raise
    await broadcast_room_event(mock_connection_manager, "room_001", event)


@pytest.mark.asyncio
async def test_broadcast_room_event_exception():
    """Test _broadcast_room_event() handles exceptions gracefully."""
    mock_connection_manager = MagicMock()
    mock_connection_manager.broadcast_to_room = AsyncMock(side_effect=Exception("Test error"))
    event = {"type": "test_event", "data": "test"}

    # Should not raise, just log
    await broadcast_room_event(mock_connection_manager, "room_001", event)


@pytest.mark.asyncio
async def test_persist_player_success():
    """Test _persist_player() returns None on success."""
    mock_persistence = MagicMock()
    mock_persistence.save_player = MagicMock()
    player = MagicMock()
    player.name = "TestPlayer"

    result = await persist_player(mock_persistence, player)

    assert result is None
    mock_persistence.save_player.assert_called_once_with(player)


@pytest.mark.asyncio
async def test_persist_player_inventory_schema_error():
    """Test _persist_player() returns error on InventorySchemaValidationError."""
    from server.schemas.shared import InventorySchemaValidationError

    mock_persistence = MagicMock()
    mock_persistence.save_player = MagicMock(side_effect=InventorySchemaValidationError("Invalid schema"))
    player = MagicMock()
    player.name = "TestPlayer"

    result = await persist_player(mock_persistence, player)

    assert result is not None
    assert "schema validation" in result["result"].lower()


@pytest.mark.asyncio
async def test_persist_player_generic_exception():
    """Test _persist_player() returns error on generic exception."""
    mock_persistence = MagicMock()
    mock_persistence.save_player = MagicMock(side_effect=Exception("Test error"))
    player = MagicMock()
    player.name = "TestPlayer"

    result = await persist_player(mock_persistence, player)

    assert result is not None
    assert "error" in result["result"].lower()
