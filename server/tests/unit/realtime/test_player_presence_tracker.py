"""
Unit tests for player presence tracker.

Tests the player_presence_tracker module functions.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.exceptions import DatabaseError
from server.realtime.player_presence_tracker import (
    _acquire_disconnect_lock,
    _build_player_info,
    _resolve_room_id,
    _should_skip_disconnect,
    broadcast_connection_message_impl,
    track_player_connected_impl,
    track_player_disconnected_impl,
)


def test_build_player_info_new_connection():
    """Test _build_player_info() creates new player info."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.level = 5
    mock_player.current_room_id = "room_123"
    mock_manager = MagicMock()
    mock_manager.player_websockets = {player_id: ["conn_1", "conn_2"]}

    with patch("server.realtime.player_presence_tracker.get_player_position", return_value="standing"):
        with patch("server.realtime.player_presence_tracker.extract_player_name", return_value="TestPlayer"):
            player_info = _build_player_info(player_id, mock_player, "websocket", mock_manager, True)

            assert player_info["player_id"] == player_id
            assert player_info["player_name"] == "TestPlayer"
            assert player_info["level"] == 5
            assert player_info["current_room_id"] == "room_123"
            assert player_info["position"] == "standing"
            assert "websocket" in player_info["connection_types"]
            assert player_info["total_connections"] == 2
            assert "connected_at" in player_info


def test_build_player_info_existing_connection():
    """Test _build_player_info() updates existing player info."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.level = 5
    mock_manager = MagicMock()
    mock_manager.player_websockets = {player_id: ["conn_1"]}
    existing_info = {
        "connected_at": 1234567890.0,
        "connection_types": {"websocket"},
        "position": "sitting",
    }
    mock_manager.online_players = {player_id: existing_info}

    with patch("server.realtime.player_presence_tracker.get_player_position", return_value="standing"):
        with patch("server.realtime.player_presence_tracker.extract_player_name", return_value="TestPlayer"):
            player_info = _build_player_info(player_id, mock_player, "websocket", mock_manager, False)

            assert player_info["connected_at"] == 1234567890.0
            assert "websocket" in player_info["connection_types"]
            assert player_info["position"] == "sitting"  # Preserved from existing


def test_build_player_info_no_level():
    """Test _build_player_info() handles player without level."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    del mock_player.level  # Remove level attribute
    mock_manager = MagicMock()
    mock_manager.player_websockets = {}

    with patch("server.realtime.player_presence_tracker.get_player_position", return_value="standing"):
        with patch("server.realtime.player_presence_tracker.extract_player_name", return_value="TestPlayer"):
            player_info = _build_player_info(player_id, mock_player, "websocket", mock_manager, True)

            assert player_info["level"] == 1  # Default value


def test_resolve_room_id_no_persistence():
    """Test _resolve_room_id() returns room_id when no persistence."""
    mock_player = MagicMock()
    mock_player.current_room_id = "room_123"
    mock_manager = MagicMock()
    mock_manager.async_persistence = None

    result = _resolve_room_id(mock_player, mock_manager)

    assert result == "room_123"


def test_resolve_room_id_no_room_id():
    """Test _resolve_room_id() returns None when no room_id."""
    mock_player = MagicMock()
    del mock_player.current_room_id
    mock_manager = MagicMock()
    mock_manager.async_persistence = MagicMock()

    result = _resolve_room_id(mock_player, mock_manager)

    assert result is None


def test_resolve_room_id_success():
    """Test _resolve_room_id() resolves canonical room ID."""
    mock_player = MagicMock()
    mock_player.current_room_id = "room_123"
    mock_manager = MagicMock()
    mock_room = MagicMock()
    mock_room.id = "canonical_room_123"
    mock_manager.async_persistence = MagicMock()
    mock_manager.async_persistence.get_room_by_id = MagicMock(return_value=mock_room)

    result = _resolve_room_id(mock_player, mock_manager)

    assert result == "canonical_room_123"


def test_resolve_room_id_room_no_id():
    """Test _resolve_room_id() returns original when room has no id."""
    mock_player = MagicMock()
    mock_player.current_room_id = "room_123"
    mock_manager = MagicMock()
    mock_room = MagicMock()
    del mock_room.id  # Room has no id attribute
    mock_manager.async_persistence = MagicMock()
    mock_manager.async_persistence.get_room_by_id = MagicMock(return_value=mock_room)

    result = _resolve_room_id(mock_player, mock_manager)

    assert result == "room_123"


@pytest.mark.asyncio
async def test_track_player_connected_impl_new_connection():
    """Test track_player_connected_impl() tracks new connection."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.current_room_id = "room_123"
    mock_player.tutorial_instance_id = None  # Skip tutorial reconnect path
    mock_manager = MagicMock()
    mock_manager.online_players = {}
    mock_manager.player_websockets = {player_id: ["conn_1"]}
    mock_manager.mark_player_seen = MagicMock()
    mock_manager.async_persistence = MagicMock()
    mock_room = MagicMock()
    mock_room.id = "room_123"
    mock_manager.async_persistence.get_room_by_id = MagicMock(return_value=mock_room)

    with patch(
        "server.realtime.player_presence_tracker.handle_new_connection_setup", new_callable=AsyncMock
    ) as mock_setup:
        with patch("server.realtime.player_presence_tracker.get_player_position", return_value="standing"):
            with patch("server.realtime.player_presence_tracker.extract_player_name", return_value="TestPlayer"):
                with patch("server.realtime.player_presence_tracker.logger") as mock_logger:
                    await track_player_connected_impl(player_id, mock_player, "websocket", mock_manager)

                    assert player_id in mock_manager.online_players
                    mock_manager.mark_player_seen.assert_called_once_with(player_id)
                    mock_setup.assert_called_once()
                    mock_logger.info.assert_called_once()


@pytest.mark.asyncio
async def test_track_player_connected_impl_existing_connection():
    """Test track_player_connected_impl() tracks additional connection."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_manager = MagicMock()
    mock_manager.online_players = {player_id: {"connected_at": 1234567890.0}}
    mock_manager.player_websockets = {player_id: ["conn_1"]}
    mock_manager.mark_player_seen = MagicMock()

    with patch("server.realtime.player_presence_tracker.get_player_position", return_value="standing"):
        with patch("server.realtime.player_presence_tracker.extract_player_name", return_value="TestPlayer"):
            with patch("server.realtime.player_presence_tracker.logger") as mock_logger:
                await track_player_connected_impl(player_id, mock_player, "websocket", mock_manager)

                mock_manager.mark_player_seen.assert_called_once_with(player_id)
                mock_logger.info.assert_called_once()
                # Should log "Player additional connection tracked"


@pytest.mark.asyncio
async def test_track_player_connected_impl_no_room_id():
    """Test track_player_connected_impl() handles player with no room_id."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    del mock_player.current_room_id
    mock_player.tutorial_instance_id = None  # Skip tutorial reconnect path
    mock_manager = MagicMock()
    mock_manager.online_players = {}
    mock_manager.player_websockets = {player_id: ["conn_1"]}
    mock_manager.mark_player_seen = MagicMock()

    with patch(
        "server.realtime.player_presence_tracker.handle_new_connection_setup", new_callable=AsyncMock
    ) as mock_setup:
        with patch("server.realtime.player_presence_tracker.get_player_position", return_value="standing"):
            with patch("server.realtime.player_presence_tracker.extract_player_name", return_value="TestPlayer"):
                await track_player_connected_impl(player_id, mock_player, "websocket", mock_manager)

                # Should not call setup when no room_id
                mock_setup.assert_not_called()


@pytest.mark.asyncio
async def test_track_player_connected_impl_error():
    """Test track_player_connected_impl() handles errors."""

    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_manager = MagicMock()
    mock_manager.online_players = {}
    mock_manager.player_websockets = {}
    del mock_manager.mark_player_seen  # Cause AttributeError

    with patch("server.realtime.player_presence_tracker.get_player_position", return_value="standing"):
        with patch("server.realtime.player_presence_tracker.extract_player_name", return_value="TestPlayer"):
            with patch("server.realtime.player_presence_tracker.logger") as mock_logger:
                await track_player_connected_impl(player_id, mock_player, "websocket", mock_manager)

                mock_logger.error.assert_called_once()


@pytest.mark.asyncio
async def test_broadcast_connection_message_impl():
    """Test broadcast_connection_message_impl() handles broadcast."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.current_room_id = "room_123"
    mock_manager = MagicMock()
    mock_manager.async_persistence = MagicMock()
    mock_room = MagicMock()
    mock_room.id = "room_123"
    mock_manager.async_persistence.get_room_by_id = MagicMock(return_value=mock_room)

    with patch("server.realtime.player_presence_tracker.logger") as mock_logger:
        await broadcast_connection_message_impl(player_id, mock_player, mock_manager)

        mock_logger.debug.assert_called_once()


@pytest.mark.asyncio
async def test_broadcast_connection_message_impl_no_room():
    """Test broadcast_connection_message_impl() handles no room."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    del mock_player.current_room_id
    mock_manager = MagicMock()
    mock_manager.async_persistence = None

    with patch("server.realtime.player_presence_tracker.logger") as mock_logger:
        await broadcast_connection_message_impl(player_id, mock_player, mock_manager)

        # Should not log debug when no room_id
        mock_logger.debug.assert_not_called()


@pytest.mark.asyncio
async def test_broadcast_connection_message_impl_error():
    """Test broadcast_connection_message_impl() handles errors."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.current_room_id = "room_123"
    mock_manager = MagicMock()
    mock_manager.async_persistence = MagicMock()
    mock_manager.async_persistence.get_room_by_id = MagicMock(side_effect=DatabaseError("DB error"))

    with patch("server.realtime.player_presence_tracker.logger") as mock_logger:
        await broadcast_connection_message_impl(player_id, mock_player, mock_manager)

        mock_logger.error.assert_called_once()


def test_should_skip_disconnect_has_websocket():
    """Test _should_skip_disconnect() returns True when player has websocket."""
    player_id = uuid.uuid4()
    mock_manager = MagicMock()
    mock_manager.has_websocket_connection = MagicMock(return_value=True)

    with patch("server.realtime.player_presence_tracker.logger") as mock_logger:
        result = _should_skip_disconnect(player_id, mock_manager, "websocket")

        assert result is True
        mock_logger.info.assert_called_once()


def test_should_skip_disconnect_no_websocket():
    """Test _should_skip_disconnect() returns False when player has no websocket."""
    player_id = uuid.uuid4()
    mock_manager = MagicMock()
    mock_manager.has_websocket_connection = MagicMock(return_value=False)

    result = _should_skip_disconnect(player_id, mock_manager, "websocket")

    assert result is False


def test_should_skip_disconnect_no_connection_type():
    """Test _should_skip_disconnect() returns False when connection_type is None."""
    player_id = uuid.uuid4()
    mock_manager = MagicMock()
    mock_manager.has_websocket_connection = MagicMock(return_value=True)

    result = _should_skip_disconnect(player_id, mock_manager, None)

    assert result is False


@pytest.mark.asyncio
async def test_acquire_disconnect_lock_success():
    """Test _acquire_disconnect_lock() acquires lock successfully."""
    player_id = uuid.uuid4()
    mock_manager = MagicMock()
    mock_manager.disconnecting_players = set()
    mock_manager.disconnect_lock = AsyncMock()
    mock_manager.disconnect_lock.__aenter__ = AsyncMock(return_value=None)
    mock_manager.disconnect_lock.__aexit__ = AsyncMock(return_value=None)

    with patch("server.realtime.player_presence_tracker.logger") as mock_logger:
        result = await _acquire_disconnect_lock(player_id, mock_manager)

        assert result is True
        assert player_id in mock_manager.disconnecting_players
        mock_logger.debug.assert_called_once()


@pytest.mark.asyncio
async def test_acquire_disconnect_lock_already_disconnecting():
    """Test _acquire_disconnect_lock() clears stuck player and succeeds."""
    player_id = uuid.uuid4()
    mock_manager = MagicMock()
    mock_manager.disconnecting_players = {player_id}  # Stuck in disconnecting
    mock_manager.disconnect_lock = AsyncMock()
    mock_manager.disconnect_lock.__aenter__ = AsyncMock(return_value=None)
    mock_manager.disconnect_lock.__aexit__ = AsyncMock(return_value=None)

    with patch("server.realtime.player_presence_tracker.logger") as mock_logger:
        result = await _acquire_disconnect_lock(player_id, mock_manager)

        # The function clears stuck players first, then acquires lock successfully
        assert result is True
        mock_logger.warning.assert_called_once()  # Should log about stuck player
        mock_logger.debug.assert_called()  # Should log about marking as disconnecting


@pytest.mark.asyncio
async def test_acquire_disconnect_lock_stuck_player():
    """Test _acquire_disconnect_lock() clears stuck player."""
    player_id = uuid.uuid4()
    mock_manager = MagicMock()
    mock_manager.disconnecting_players = {player_id}  # Stuck in disconnecting
    mock_manager.disconnect_lock = AsyncMock()
    mock_manager.disconnect_lock.__aenter__ = AsyncMock(return_value=None)
    mock_manager.disconnect_lock.__aexit__ = AsyncMock(return_value=None)

    with patch("server.realtime.player_presence_tracker.logger") as mock_logger:
        result = await _acquire_disconnect_lock(player_id, mock_manager)

        # Should clear stuck player and then acquire lock
        assert result is True
        mock_logger.warning.assert_called_once()


@pytest.mark.asyncio
async def test_track_player_disconnected_impl_success():
    """Test track_player_disconnected_impl() tracks disconnection successfully."""
    player_id = uuid.uuid4()
    mock_manager = MagicMock()
    mock_manager.has_websocket_connection = MagicMock(return_value=False)
    mock_manager.disconnecting_players = set()
    mock_manager.disconnect_lock = AsyncMock()
    mock_manager.disconnect_lock.__aenter__ = AsyncMock(return_value=None)
    mock_manager.disconnect_lock.__aexit__ = AsyncMock(return_value=None)
    # Mark as intentional so handle_player_disconnect_broadcast is called
    mock_manager.intentional_disconnects = {player_id}
    mock_player = MagicMock()
    mock_player.current_room_id = "room_123"
    # Accessing protected members is necessary to mock the methods used by player_presence_tracker implementation
    mock_manager._get_player = AsyncMock(return_value=mock_player)  # pylint: disable=protected-access  # Reason: Accessing protected members is necessary to mock the methods used by player_presence_tracker implementation
    mock_manager._cleanup_ghost_players = MagicMock()  # pylint: disable=protected-access  # Reason: Accessing protected members is necessary to mock the methods used by player_presence_tracker implementation

    with patch("server.realtime.player_presence_tracker._should_skip_disconnect", return_value=False):
        with patch("server.realtime.player_presence_tracker._acquire_disconnect_lock", return_value=True):
            with patch("server.realtime.player_presence_tracker._collect_disconnect_keys", return_value=([], [])):
                with patch(
                    "server.realtime.player_presence_tracker.handle_player_disconnect_broadcast"
                ) as mock_broadcast:
                    with patch(
                        "server.realtime.player_presence_tracker._remove_player_from_online_tracking"
                    ) as mock_remove:
                        with patch(
                            "server.realtime.player_presence_tracker._cleanup_player_references"
                        ) as mock_cleanup:
                            with patch(
                                "server.realtime.player_presence_tracker.extract_player_name", return_value="TestPlayer"
                            ):
                                with patch("server.realtime.player_presence_tracker.logger") as mock_logger:
                                    await track_player_disconnected_impl(player_id, mock_manager, "websocket")

                                    mock_broadcast.assert_called_once()
                                    mock_remove.assert_called_once()
                                    mock_cleanup.assert_called_once()
                                    # Accessing protected member is necessary to verify the method was called
                                    mock_manager._cleanup_ghost_players.assert_called_once()  # pylint: disable=protected-access  # Reason: Accessing protected member is necessary to verify the method was called
                                    # Check for intentional disconnect log message
                                    assert any(
                                        "intentional" in str(call).lower() or "disconnected" in str(call).lower()
                                        for call in mock_logger.info.call_args_list
                                    )
                                    # Player should be removed from disconnecting_players in finally block
                                    assert player_id not in mock_manager.disconnecting_players


@pytest.mark.asyncio
async def test_track_player_disconnected_impl_skip_disconnect():
    """Test track_player_disconnected_impl() skips when player has connections."""
    player_id = uuid.uuid4()
    mock_manager = MagicMock()
    mock_manager.has_websocket_connection = MagicMock(return_value=True)

    with patch("server.realtime.player_presence_tracker._should_skip_disconnect", return_value=True):
        await track_player_disconnected_impl(player_id, mock_manager, "websocket")

        # Should return early, no further processing


@pytest.mark.asyncio
async def test_track_player_disconnected_impl_no_lock():
    """Test track_player_disconnected_impl() returns early if lock not acquired."""
    player_id = uuid.uuid4()
    mock_manager = MagicMock()
    mock_manager.has_websocket_connection = MagicMock(return_value=False)
    mock_manager.disconnecting_players = {player_id}  # Already disconnecting
    mock_manager.disconnect_lock = AsyncMock()
    mock_manager.disconnect_lock.__aenter__ = AsyncMock(return_value=None)
    mock_manager.disconnect_lock.__aexit__ = AsyncMock(return_value=None)

    with patch("server.realtime.player_presence_tracker._acquire_disconnect_lock", return_value=False):
        await track_player_disconnected_impl(player_id, mock_manager, "websocket")

        # Should return early, no further processing


@pytest.mark.asyncio
async def test_track_player_disconnected_impl_no_player():
    """Test track_player_disconnected_impl() handles player not found."""
    player_id = uuid.uuid4()
    mock_manager = MagicMock()
    mock_manager.has_websocket_connection = MagicMock(return_value=False)
    mock_manager.disconnecting_players = set()
    mock_manager.disconnect_lock = AsyncMock()
    mock_manager.disconnect_lock.__aenter__ = AsyncMock(return_value=None)
    mock_manager.disconnect_lock.__aexit__ = AsyncMock(return_value=None)
    # Mark as intentional so handle_player_disconnect_broadcast is called
    mock_manager.intentional_disconnects = {player_id}
    # Accessing protected members is necessary to mock the methods used by player_presence_tracker implementation
    mock_manager._get_player = AsyncMock(return_value=None)  # pylint: disable=protected-access  # Reason: Accessing protected members is necessary to mock the methods used by player_presence_tracker implementation
    mock_manager._cleanup_ghost_players = MagicMock()  # pylint: disable=protected-access  # Reason: Accessing protected members is necessary to mock the methods used by player_presence_tracker implementation

    with patch("server.realtime.player_presence_tracker._should_skip_disconnect", return_value=False):
        with patch("server.realtime.player_presence_tracker._acquire_disconnect_lock", return_value=True):
            with patch("server.realtime.player_presence_tracker._collect_disconnect_keys", return_value=([], [])):
                with patch(
                    "server.realtime.player_presence_tracker.handle_player_disconnect_broadcast"
                ) as mock_broadcast:
                    with patch("server.realtime.player_presence_tracker._remove_player_from_online_tracking"):
                        with patch("server.realtime.player_presence_tracker._cleanup_player_references"):
                            with patch(
                                "server.realtime.player_presence_tracker.extract_player_name",
                                return_value="Unknown Player",
                            ):
                                await track_player_disconnected_impl(player_id, mock_manager, "websocket")

                                # Should still process disconnect even without player
                                mock_broadcast.assert_called_once()
                                assert player_id not in mock_manager.disconnecting_players


@pytest.mark.asyncio
async def test_track_player_disconnected_impl_error():
    """Test track_player_disconnected_impl() handles errors."""
    player_id = uuid.uuid4()
    mock_manager = MagicMock()
    mock_manager.has_websocket_connection = MagicMock(return_value=False)
    mock_manager.disconnecting_players = set()
    mock_manager.disconnect_lock = AsyncMock()
    mock_manager.disconnect_lock.__aenter__ = AsyncMock(return_value=None)
    mock_manager.disconnect_lock.__aexit__ = AsyncMock(return_value=None)
    # Mark as intentional so _get_player is called and exception is raised
    mock_manager.intentional_disconnects = {player_id}
    # Accessing protected members is necessary to mock the methods used by player_presence_tracker implementation
    mock_manager._get_player = AsyncMock(side_effect=DatabaseError("DB error"))  # pylint: disable=protected-access  # Reason: Accessing protected members is necessary to mock the methods used by player_presence_tracker implementation
    mock_manager._cleanup_ghost_players = MagicMock()  # pylint: disable=protected-access  # Reason: Accessing protected members is necessary to mock the methods used by player_presence_tracker implementation

    with patch("server.realtime.player_presence_tracker.logger") as mock_logger:
        with patch("server.realtime.player_presence_tracker._should_skip_disconnect", return_value=False):
            with patch("server.realtime.player_presence_tracker._acquire_disconnect_lock", return_value=True):
                await track_player_disconnected_impl(player_id, mock_manager, "websocket")

                mock_logger.error.assert_called_once()
                # Player should still be removed from disconnecting_players in finally block
                assert player_id not in mock_manager.disconnecting_players


@pytest.mark.asyncio
async def test_track_player_disconnected_impl_finally_cleanup():
    """Test track_player_disconnected_impl() always removes from disconnecting_players in finally."""
    player_id = uuid.uuid4()
    mock_manager = MagicMock()
    mock_manager.has_websocket_connection = MagicMock(return_value=False)
    mock_manager.disconnecting_players = set()
    mock_manager.disconnect_lock = AsyncMock()
    mock_manager.disconnect_lock.__aenter__ = AsyncMock(return_value=None)
    mock_manager.disconnect_lock.__aexit__ = AsyncMock(return_value=None)
    # Mark as intentional so _get_player is called
    mock_manager.intentional_disconnects = {player_id}
    # Raise DatabaseError which is caught, but finally block should still execute
    # Accessing protected members is necessary to mock the methods used by player_presence_tracker implementation
    mock_manager._get_player = AsyncMock(side_effect=DatabaseError("Test error"))  # pylint: disable=protected-access  # Reason: Accessing protected members is necessary to mock the methods used by player_presence_tracker implementation
    mock_manager._cleanup_ghost_players = MagicMock()  # pylint: disable=protected-access  # Reason: Accessing protected members is necessary to mock the methods used by player_presence_tracker implementation

    # The function will add player to disconnecting_players in _acquire_disconnect_lock
    # Then raise exception (which is caught), then finally block removes it
    async def mock_acquire_lock(pid, mgr):
        mgr.disconnecting_players.add(pid)
        return True

    with patch("server.realtime.player_presence_tracker._should_skip_disconnect", return_value=False):
        with patch("server.realtime.player_presence_tracker._acquire_disconnect_lock", side_effect=mock_acquire_lock):
            with patch("server.realtime.player_presence_tracker._collect_disconnect_keys", return_value=([], [])):
                # Exception is caught internally, but finally block should still execute
                await track_player_disconnected_impl(player_id, mock_manager, "websocket")

                # Even with error, finally block should remove player
                assert player_id not in mock_manager.disconnecting_players
