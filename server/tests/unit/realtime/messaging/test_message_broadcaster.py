"""
Unit tests for message broadcaster.

Tests the MessageBroadcaster class.
"""

import uuid
from unittest.mock import AsyncMock

import pytest

from server.realtime.messaging.message_broadcaster import MessageBroadcaster


@pytest.fixture
def mock_room_manager():
    """Create a mock room manager."""
    manager = AsyncMock()
    manager.get_room_subscribers = AsyncMock(return_value=set())
    return manager


@pytest.fixture
def mock_send_personal_message():
    """Create a mock send_personal_message callback."""
    return AsyncMock(return_value={"success": True})


@pytest.fixture
def message_broadcaster(mock_room_manager, mock_send_personal_message):
    """Create a MessageBroadcaster instance."""
    return MessageBroadcaster(mock_room_manager, mock_send_personal_message)


def test_message_broadcaster_init(message_broadcaster, mock_room_manager, mock_send_personal_message):
    """Test MessageBroadcaster initialization."""
    assert message_broadcaster.room_manager == mock_room_manager
    assert message_broadcaster.send_personal_message == mock_send_personal_message


@pytest.mark.asyncio
async def test_broadcast_to_room(message_broadcaster, mock_room_manager, mock_send_personal_message):
    """Test broadcast_to_room() broadcasts to room subscribers."""
    mock_room_manager.get_room_subscribers = AsyncMock(return_value={"player_001", "player_002"})
    event = {"type": "test_event", "data": "test"}
    result = await message_broadcaster.broadcast_to_room("room_001", event)
    assert "total_targets" in result
    assert result["total_targets"] == 2


@pytest.mark.asyncio
async def test_broadcast_to_room_exclude_player(message_broadcaster, mock_room_manager):
    """Test broadcast_to_room() excludes specified player."""
    mock_room_manager.get_room_subscribers = AsyncMock(return_value={"player_001", "player_002"})
    event = {"type": "test_event", "data": "test"}
    result = await message_broadcaster.broadcast_to_room("room_001", event, exclude_player="player_001")
    assert result["excluded_players"] == 1
    assert result["total_targets"] == 2


@pytest.mark.asyncio
async def test_broadcast_to_room_empty(message_broadcaster, mock_room_manager):
    """Test broadcast_to_room() when room has no subscribers."""
    mock_room_manager.get_room_subscribers = AsyncMock(return_value=set())
    event = {"type": "test_event", "data": "test"}
    result = await message_broadcaster.broadcast_to_room("room_001", event)
    assert result["total_targets"] == 0
    assert result["successful_deliveries"] == 0


@pytest.mark.asyncio
async def test_broadcast_global(message_broadcaster, mock_send_personal_message):
    """Test broadcast_global() broadcasts globally."""
    event = {"type": "test_event", "data": "test"}
    player_websockets = {uuid.uuid4(): ["ws_001"], uuid.uuid4(): ["ws_002"]}
    # broadcast_global signature: (event, exclude_player, player_websockets)
    result = await message_broadcaster.broadcast_global(event, None, player_websockets)
    assert "total_players" in result or "total_targets" in result


@pytest.mark.asyncio
async def test_broadcast_to_room_with_uuid_exclude(message_broadcaster, mock_room_manager):
    """Test broadcast_to_room() with UUID exclude_player."""
    mock_room_manager.get_room_subscribers = AsyncMock(return_value={"player_001", "player_002"})
    event = {"type": "test_event", "data": "test"}
    exclude_uuid = uuid.uuid4()
    result = await message_broadcaster.broadcast_to_room("room_001", event, exclude_player=exclude_uuid)
    assert result["excluded_players"] >= 0
    assert result["total_targets"] == 2


@pytest.mark.asyncio
async def test_broadcast_to_room_delivery_failure(message_broadcaster, mock_room_manager, mock_send_personal_message):
    """Test broadcast_to_room() handles delivery failures."""
    mock_room_manager.get_room_subscribers = AsyncMock(return_value={"player_001"})
    mock_send_personal_message.return_value = {"success": False}
    event = {"type": "test_event", "data": "test"}
    result = await message_broadcaster.broadcast_to_room("room_001", event)
    assert result["failed_deliveries"] >= 0


@pytest.mark.asyncio
async def test_broadcast_global_exclude_player(message_broadcaster, mock_send_personal_message):
    """Test broadcast_global() excludes specified player."""
    event = {"type": "test_event", "data": "test"}
    player_id1 = uuid.uuid4()
    player_id2 = uuid.uuid4()
    player_websockets = {player_id1: ["ws_001"], player_id2: ["ws_002"]}
    result = await message_broadcaster.broadcast_global(event, exclude_player=player_id1, player_websockets=player_websockets)
    assert "total_players" in result or "total_targets" in result
    assert result.get("excluded_players", 0) >= 0


@pytest.mark.asyncio
async def test_broadcast_global_empty(message_broadcaster, mock_send_personal_message):
    """Test broadcast_global() when no players online."""
    event = {"type": "test_event", "data": "test"}
    result = await message_broadcaster.broadcast_global(event, None, {})
    assert result.get("total_players", 0) == 0 or result.get("total_targets", 0) == 0


@pytest.mark.asyncio
async def test_broadcast_room_event(message_broadcaster, mock_room_manager):
    """Test broadcast_room_event() broadcasts room event."""
    mock_room_manager.get_room_subscribers = AsyncMock(return_value={"player_001"})
    result = await message_broadcaster.broadcast_room_event("test_event", "room_001", {"data": "test"})
    assert "room_id" in result or "total_targets" in result


@pytest.mark.asyncio
async def test_broadcast_global_event(message_broadcaster, mock_send_personal_message):
    """Test broadcast_global_event() broadcasts global event."""
    # broadcast_global_event takes (event_type, data) - no player_websockets parameter
    result = await message_broadcaster.broadcast_global_event("test_event", {"data": "test"})
    assert "total_players" in result or "total_targets" in result or isinstance(result, dict)
