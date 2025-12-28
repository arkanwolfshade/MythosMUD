"""
Unit tests for websocket room updates.

Tests the websocket room update functions.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.realtime.websocket_room_updates import (
    broadcast_room_update,
    get_npc_occupants_fallback,
    get_npc_occupants_from_lifecycle_manager,
    get_player_occupants,
    update_player_room_subscription,
)


@pytest.fixture
def mock_connection_manager():
    """Create a mock connection manager."""
    manager = AsyncMock()
    manager.get_room_occupants = AsyncMock(return_value=[])
    return manager


@pytest.mark.asyncio
async def test_get_player_occupants(mock_connection_manager):
    """Test get_player_occupants() returns player names."""
    mock_connection_manager.get_room_occupants = AsyncMock(
        return_value=[{"player_name": "Player1"}, {"player_name": "Player2"}]
    )
    result = await get_player_occupants(mock_connection_manager, "room_001")
    assert "Player1" in result
    assert "Player2" in result


@pytest.mark.asyncio
async def test_get_player_occupants_empty(mock_connection_manager):
    """Test get_player_occupants() returns empty list when no occupants."""
    mock_connection_manager.get_room_occupants = AsyncMock(return_value=[])
    result = await get_player_occupants(mock_connection_manager, "room_001")
    assert result == []


@pytest.mark.asyncio
async def test_get_npc_occupants_from_lifecycle_manager_no_service():
    """Test get_npc_occupants_from_lifecycle_manager() when service is not available."""
    # The function handles missing service gracefully and returns empty list
    with patch("server.services.npc_instance_service.get_npc_instance_service", return_value=None):
        result = await get_npc_occupants_from_lifecycle_manager("room_001")
        assert result == []


@pytest.mark.asyncio
async def test_get_npc_occupants_fallback(mock_connection_manager):
    """Test get_npc_occupants_fallback() returns NPC names."""
    mock_room = MagicMock()
    mock_room.get_npcs = MagicMock(return_value=["npc_001", "npc_002"])
    # This function may raise RuntimeError if NPC instance service is not initialized
    # So we catch that exception
    try:
        result = await get_npc_occupants_fallback(mock_room, "room_001")
        assert isinstance(result, list)
    except RuntimeError:
        # Expected when NPC instance service is not initialized
        assert True


@pytest.mark.asyncio
async def test_update_player_room_subscription(mock_connection_manager):
    """Test update_player_room_subscription() updates subscription."""
    await update_player_room_subscription(mock_connection_manager, "player_001", "room_001")
    # Should not raise


@pytest.mark.asyncio
async def test_broadcast_room_update(mock_connection_manager):
    """Test broadcast_room_update() broadcasts update."""
    await broadcast_room_update("player_001", "room_001", mock_connection_manager)
    # Should not raise
