"""
Unit tests for websocket room updates build event function.

Tests the build_room_update_event function in websocket_room_updates.py.
"""

from unittest.mock import AsyncMock, MagicMock

import pytest

from server.realtime.websocket_room_updates import build_room_update_event


@pytest.fixture
def mock_room():
    """Create a mock room."""
    room = MagicMock()
    room.to_dict = MagicMock(return_value={"id": "room_001", "name": "Test Room"})
    room.get_players = MagicMock(return_value=[])
    room.get_objects = MagicMock(return_value=[])
    room.get_npcs = MagicMock(return_value=[])
    room.get_occupant_count = MagicMock(return_value=0)
    return room


@pytest.fixture
def mock_connection_manager():
    """Create a mock connection manager."""
    manager = MagicMock()
    manager.convert_room_players_uuids_to_names = AsyncMock(return_value={"id": "room_001", "name": "Test Room"})
    manager.room_manager = MagicMock()
    manager.room_manager.list_room_drops = MagicMock(return_value=[])
    return manager


@pytest.mark.asyncio
async def test_build_room_update_event(mock_room, mock_connection_manager):
    """Test build_room_update_event() creates room update event."""
    occupant_names = ["Player1", "NPC1"]
    result = await build_room_update_event(mock_room, "room_001", "player_001", occupant_names, mock_connection_manager)
    assert "event_type" in result
    assert result["event_type"] == "room_update"
    assert "data" in result
    assert "room" in result["data"]
    assert "occupants" in result["data"]
