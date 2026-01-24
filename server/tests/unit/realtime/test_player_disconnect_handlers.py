"""
Unit tests for player disconnect handlers.

Tests the player disconnect handling functions.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions
from server.realtime.player_disconnect_handlers import (
    _cleanup_player_references,
    _collect_disconnect_keys,
    _remove_player_from_online_tracking,
    handle_player_disconnect_broadcast,
)


@pytest.fixture
def mock_player():
    """Create mock player."""
    player = MagicMock()
    player.player_id = uuid.uuid4()
    player.name = "TestPlayer"
    return player


@pytest.fixture
def mock_connection_manager():
    """Create mock connection manager."""
    manager = MagicMock()
    manager.async_persistence = MagicMock()
    manager.broadcast_to_room = AsyncMock()
    manager.player_websockets = {}
    manager.player_names = {}
    return manager


@pytest.mark.asyncio
async def test_handle_player_disconnect_broadcast_with_room(mock_connection_manager):
    """Test handle_player_disconnect_broadcast handles disconnect with room."""
    player_id = uuid.uuid4()
    mock_room = MagicMock()
    mock_room.has_player = MagicMock(return_value=True)
    mock_room.player_left = MagicMock()
    mock_connection_manager.async_persistence.get_room_by_id = MagicMock(return_value=mock_room)
    await handle_player_disconnect_broadcast(player_id, "TestPlayer", "room_001", mock_connection_manager)
    mock_room.player_left.assert_called_once()
    mock_connection_manager.broadcast_to_room.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_player_disconnect_broadcast_no_room(mock_connection_manager):
    """Test handle_player_disconnect_broadcast handles disconnect without room."""
    player_id = uuid.uuid4()
    await handle_player_disconnect_broadcast(player_id, "TestPlayer", None, mock_connection_manager)
    mock_connection_manager.broadcast_to_room.assert_not_awaited()


@pytest.mark.asyncio
async def test_handle_player_disconnect_broadcast_empty_player_name(mock_connection_manager):
    """Test handle_player_disconnect_broadcast handles empty player_name."""
    player_id = uuid.uuid4()
    mock_connection_manager.broadcast_to_room = AsyncMock()
    await handle_player_disconnect_broadcast(player_id, "", "room_001", mock_connection_manager)
    # Should use "Unknown Player" when name is empty
    mock_connection_manager.broadcast_to_room.assert_awaited_once()


def test_collect_disconnect_keys_with_player():
    """Test _collect_disconnect_keys collects keys from player."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.player_id = player_id
    uuid_keys, _str_keys = _collect_disconnect_keys(player_id, mock_player)
    assert player_id in uuid_keys


def test_collect_disconnect_keys_no_player():
    """Test _collect_disconnect_keys handles None player."""
    player_id = uuid.uuid4()
    uuid_keys, _str_keys = _collect_disconnect_keys(player_id, None)
    assert player_id in uuid_keys


def test_remove_player_from_online_tracking(mock_connection_manager):
    """Test _remove_player_from_online_tracking removes player."""
    player_id = uuid.uuid4()
    uuid_keys = {player_id}
    str_keys = {"TestPlayer"}
    mock_connection_manager.online_players = {player_id: MagicMock()}
    mock_connection_manager.player_names = {"TestPlayer": player_id}
    mock_connection_manager.room_manager = MagicMock()
    mock_connection_manager.room_manager.remove_player_from_all_rooms = MagicMock()
    _remove_player_from_online_tracking(uuid_keys, str_keys, mock_connection_manager)
    # Function should remove from online_players dictionary
    assert player_id not in mock_connection_manager.online_players


@pytest.mark.asyncio
async def test_handle_player_disconnect_broadcast_room_no_player(mock_connection_manager):
    """Test handle_player_disconnect_broadcast when room exists but player not in room."""
    player_id = uuid.uuid4()
    mock_room = MagicMock()
    mock_room.has_player = MagicMock(return_value=False)  # Player not in room
    mock_connection_manager.async_persistence.get_room_by_id = MagicMock(return_value=mock_room)
    await handle_player_disconnect_broadcast(player_id, "TestPlayer", "room_001", mock_connection_manager)
    mock_room.player_left.assert_not_called()
    mock_connection_manager.broadcast_to_room.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_player_disconnect_broadcast_no_persistence(mock_connection_manager):
    """Test handle_player_disconnect_broadcast when no async_persistence."""
    player_id = uuid.uuid4()
    mock_connection_manager.async_persistence = None
    await handle_player_disconnect_broadcast(player_id, "TestPlayer", "room_001", mock_connection_manager)
    # Should still broadcast
    mock_connection_manager.broadcast_to_room.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_player_disconnect_broadcast_no_room_found(mock_connection_manager):
    """Test handle_player_disconnect_broadcast when room not found."""
    player_id = uuid.uuid4()
    mock_connection_manager.async_persistence.get_room_by_id = MagicMock(return_value=None)
    await handle_player_disconnect_broadcast(player_id, "TestPlayer", "room_001", mock_connection_manager)
    # Should still broadcast
    mock_connection_manager.broadcast_to_room.assert_awaited_once()


def test_collect_disconnect_keys_with_user_id():
    """Test _collect_disconnect_keys collects user_id when available."""
    player_id = uuid.uuid4()
    user_id = uuid.uuid4()
    mock_player = MagicMock()
    # Ensure player_id attribute doesn't exist so it falls back to user_id
    del mock_player.player_id
    mock_player.user_id = user_id
    mock_player.name = "TestPlayer"
    uuid_keys, str_keys = _collect_disconnect_keys(player_id, mock_player)
    assert user_id in uuid_keys
    assert "TestPlayer" in str_keys


def test_collect_disconnect_keys_with_string_user_id():
    """Test _collect_disconnect_keys handles string user_id."""
    player_id = uuid.uuid4()
    user_id = "user_001"
    mock_player = MagicMock()
    # Ensure player_id attribute doesn't exist so it falls back to user_id
    del mock_player.player_id
    mock_player.user_id = user_id
    mock_player.name = "TestPlayer"
    _uuid_keys, str_keys = _collect_disconnect_keys(player_id, mock_player)
    assert user_id in str_keys


def test_collect_disconnect_keys_with_player_name():
    """Test _collect_disconnect_keys collects player name."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    _uuid_keys, str_keys = _collect_disconnect_keys(player_id, mock_player)
    assert "TestPlayer" in str_keys


def test_collect_disconnect_keys_no_name():
    """Test _collect_disconnect_keys handles player without name."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    # Mock extract_player_name to return None
    with patch("server.realtime.player_disconnect_handlers.extract_player_name", return_value=None):
        uuid_keys, _str_keys = _collect_disconnect_keys(player_id, mock_player)
        assert player_id in uuid_keys


def test_remove_player_from_online_tracking_not_in_online_players(mock_connection_manager):
    """Test _remove_player_from_online_tracking handles player not in online_players."""
    player_id = uuid.uuid4()
    uuid_keys = {player_id}
    str_keys = {"TestPlayer"}
    mock_connection_manager.online_players = {}  # Empty
    mock_connection_manager.room_manager = MagicMock()
    mock_connection_manager.room_manager.remove_player_from_all_rooms = MagicMock()
    _remove_player_from_online_tracking(uuid_keys, str_keys, mock_connection_manager)
    # Should still call remove_player_from_all_rooms
    assert mock_connection_manager.room_manager.remove_player_from_all_rooms.call_count >= 1


def test_cleanup_player_references(mock_connection_manager):
    """Test _cleanup_player_references cleans up all references."""
    player_id = uuid.uuid4()
    mock_connection_manager.online_players = {player_id: MagicMock()}
    mock_connection_manager.last_seen = {player_id: MagicMock()}
    mock_connection_manager.last_active_update_times = {player_id: MagicMock()}
    mock_connection_manager.rate_limiter = MagicMock()
    mock_connection_manager.rate_limiter.remove_player_data = MagicMock()
    mock_connection_manager.message_queue = MagicMock()
    mock_connection_manager.message_queue.remove_player_messages = MagicMock()
    _cleanup_player_references(player_id, mock_connection_manager)
    assert player_id not in mock_connection_manager.online_players
    assert player_id not in mock_connection_manager.last_seen
    assert player_id not in mock_connection_manager.last_active_update_times
    mock_connection_manager.rate_limiter.remove_player_data.assert_called_once()
    mock_connection_manager.message_queue.remove_player_messages.assert_called_once()


def test_cleanup_player_references_partial_cleanup(mock_connection_manager):
    """Test _cleanup_player_references handles missing references gracefully."""
    player_id = uuid.uuid4()
    # Some references don't exist
    mock_connection_manager.online_players = {}
    mock_connection_manager.last_seen = {}
    mock_connection_manager.last_active_update_times = {}
    mock_connection_manager.rate_limiter = MagicMock()
    mock_connection_manager.rate_limiter.remove_player_data = MagicMock()
    mock_connection_manager.message_queue = MagicMock()
    mock_connection_manager.message_queue.remove_player_messages = MagicMock()
    # Should not raise
    _cleanup_player_references(player_id, mock_connection_manager)
    mock_connection_manager.rate_limiter.remove_player_data.assert_called_once()


@pytest.mark.asyncio
async def test_handle_player_disconnect_broadcast_room_player_left_called(mock_connection_manager):
    """Test handle_player_disconnect_broadcast calls room.player_left() when player in room."""
    player_id = uuid.uuid4()
    mock_room = MagicMock()
    mock_room.has_player = MagicMock(return_value=True)
    mock_room.player_left = MagicMock()
    mock_connection_manager.async_persistence.get_room_by_id = MagicMock(return_value=mock_room)
    await handle_player_disconnect_broadcast(player_id, "TestPlayer", "room_001", mock_connection_manager)
    # Should call player_left before broadcasting
    mock_room.player_left.assert_called_once_with(str(player_id))


@pytest.mark.asyncio
async def test_handle_player_disconnect_broadcast_no_player_name(mock_connection_manager):
    """Test handle_player_disconnect_broadcast handles None player_name."""
    player_id = uuid.uuid4()
    mock_connection_manager.broadcast_to_room = AsyncMock()
    await handle_player_disconnect_broadcast(player_id, None, "room_001", mock_connection_manager)
    # Should use "Unknown Player" as safe name
    mock_connection_manager.broadcast_to_room.assert_awaited_once()
    call_args = mock_connection_manager.broadcast_to_room.call_args
    assert call_args is not None


def test_collect_disconnect_keys_with_string_canonical_id():
    """Test _collect_disconnect_keys handles string canonical_id."""
    player_id = uuid.uuid4()
    canonical_id_str = "user_001"
    mock_player = MagicMock()
    del mock_player.player_id
    mock_player.user_id = canonical_id_str  # String user_id
    mock_player.name = "TestPlayer"
    uuid_keys, str_keys = _collect_disconnect_keys(player_id, mock_player)
    assert canonical_id_str in str_keys
    assert player_id in uuid_keys


def test_collect_disconnect_keys_with_uuid_canonical_id():
    """Test _collect_disconnect_keys handles UUID canonical_id."""
    player_id = uuid.uuid4()
    canonical_id_uuid = uuid.uuid4()
    mock_player = MagicMock()
    del mock_player.player_id
    mock_player.user_id = canonical_id_uuid  # UUID user_id
    mock_player.name = "TestPlayer"
    uuid_keys, _str_keys = _collect_disconnect_keys(player_id, mock_player)
    assert canonical_id_uuid in uuid_keys
    assert player_id in uuid_keys


def test_collect_disconnect_keys_no_canonical_id():
    """Test _collect_disconnect_keys handles player without canonical_id."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    # No player_id or user_id
    del mock_player.player_id
    if hasattr(mock_player, "user_id"):
        del mock_player.user_id
    mock_player.name = "TestPlayer"
    uuid_keys, str_keys = _collect_disconnect_keys(player_id, mock_player)
    assert player_id in uuid_keys
    # Should still collect name if available
    assert "TestPlayer" in str_keys
