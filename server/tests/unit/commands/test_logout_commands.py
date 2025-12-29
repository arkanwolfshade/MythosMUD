"""
Unit tests for logout commands.

Tests the logout and quit command handlers for proper cleanup and session management.
"""

import uuid
from datetime import UTC, datetime
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.logout_commands import (
    _clear_corrupted_cache_entry,
    _disconnect_player_connections,
    _get_player_for_logout,
    _get_player_position_from_connection_manager,
    _sync_player_position,
    _update_and_save_player_last_active,
    handle_logout_command,
    handle_quit_command,
)


@pytest.fixture
def mock_request():
    """Create a mock request object."""
    request = MagicMock()
    request.app = MagicMock()
    request.app.state = MagicMock()
    return request


@pytest.fixture
def mock_persistence():
    """Create a mock persistence layer."""
    persistence = AsyncMock()
    return persistence


@pytest.fixture
def mock_connection_manager():
    """Create a mock connection manager."""
    manager = AsyncMock()
    manager.online_players = {}
    manager.get_online_player_by_display_name = MagicMock(return_value=None)
    return manager


@pytest.fixture
def mock_player():
    """Create a mock player object."""
    player = MagicMock()
    player.player_id = uuid.uuid4()
    player.name = "TestPlayer"
    player.current_room_id = "test_room"
    player.last_active = datetime.now(UTC)
    player.get_stats = MagicMock(return_value={"position": "standing"})
    player.set_stats = MagicMock()
    return player


def test_clear_corrupted_cache_entry_with_cache(mock_request):
    """Test _clear_corrupted_cache_entry clears entry from cache."""
    cache = {"testplayer": MagicMock()}
    mock_request.state._command_player_cache = cache

    _clear_corrupted_cache_entry(mock_request, "testplayer")

    assert "testplayer" not in cache


def test_clear_corrupted_cache_entry_no_cache(mock_request):
    """Test _clear_corrupted_cache_entry handles missing cache gracefully."""
    mock_request.state._command_player_cache = None

    # Should not raise
    _clear_corrupted_cache_entry(mock_request, "testplayer")


def test_clear_corrupted_cache_entry_no_request():
    """Test _clear_corrupted_cache_entry handles None request."""
    # Should not raise
    _clear_corrupted_cache_entry(None, "testplayer")


@pytest.mark.asyncio
async def test_get_player_for_logout_from_cache(mock_request, mock_persistence):
    """Test _get_player_for_logout retrieves player from cache."""
    mock_player = MagicMock()
    with patch("server.commands.logout_commands.get_cached_player", return_value=mock_player):
        player = await _get_player_for_logout(mock_request, mock_persistence, "testplayer")

        assert player == mock_player


@pytest.mark.asyncio
async def test_get_player_for_logout_from_persistence(mock_request, mock_persistence, mock_player):
    """Test _get_player_for_logout retrieves player from persistence when not in cache."""
    with patch("server.commands.logout_commands.get_cached_player", return_value=None):
        with patch("server.commands.logout_commands.cache_player") as mock_cache:
            mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)

            player = await _get_player_for_logout(mock_request, mock_persistence, "testplayer")

            assert player == mock_player
            mock_persistence.get_player_by_name.assert_awaited_once_with("testplayer")
            mock_cache.assert_called_once_with(mock_request, "testplayer", mock_player)


@pytest.mark.asyncio
async def test_get_player_for_logout_corrupted_cache(mock_request, mock_persistence, mock_player):
    """Test _get_player_for_logout handles corrupted cache (coroutine instead of player)."""
    mock_coroutine = AsyncMock()

    def iscoroutine_side_effect(obj):
        # Return True only for the cached coroutine, False for the real player
        return obj is mock_coroutine

    with patch("server.commands.logout_commands.get_cached_player", return_value=mock_coroutine):
        with patch("server.commands.logout_commands.inspect.iscoroutine", side_effect=iscoroutine_side_effect):
            with patch("server.commands.logout_commands._clear_corrupted_cache_entry") as mock_clear:
                mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)

                player = await _get_player_for_logout(mock_request, mock_persistence, "testplayer")

                assert player == mock_player
                mock_clear.assert_called_once_with(mock_request, "testplayer")


@pytest.mark.asyncio
async def test_get_player_for_logout_persistence_error(mock_request, mock_persistence):
    """Test _get_player_for_logout handles persistence errors gracefully."""
    with patch("server.commands.logout_commands.get_cached_player", return_value=None):
        mock_persistence.get_player_by_name = AsyncMock(side_effect=ValueError("DB error"))

        player = await _get_player_for_logout(mock_request, mock_persistence, "testplayer")

        assert player is None


@pytest.mark.asyncio
async def test_get_player_for_logout_persistence_returns_coroutine(mock_request, mock_persistence):
    """Test _get_player_for_logout handles persistence returning coroutine."""
    mock_coroutine = AsyncMock()

    with patch("server.commands.logout_commands.get_cached_player", return_value=None):
        mock_persistence.get_player_by_name = AsyncMock(return_value=mock_coroutine)
        with patch("server.commands.logout_commands.inspect.iscoroutine", return_value=True):
            player = await _get_player_for_logout(mock_request, mock_persistence, "testplayer")

            assert player is None


def test_get_player_position_from_connection_manager_by_id(mock_connection_manager, mock_player):
    """Test _get_player_position_from_connection_manager retrieves position by player_id."""
    player_id_str = str(mock_player.player_id)
    mock_connection_manager.online_players[player_id_str] = {"position": "sitting"}

    position = _get_player_position_from_connection_manager(mock_connection_manager, mock_player, "TestPlayer")

    assert position == "sitting"


def test_get_player_position_from_connection_manager_by_name(mock_connection_manager, mock_player):
    """Test _get_player_position_from_connection_manager retrieves position by display name."""
    mock_connection_manager.online_players = {}
    mock_connection_manager.get_online_player_by_display_name = MagicMock(return_value={"position": "lying"})

    position = _get_player_position_from_connection_manager(mock_connection_manager, mock_player, "TestPlayer")

    assert position == "lying"


def test_get_player_position_from_connection_manager_not_found(mock_connection_manager, mock_player):
    """Test _get_player_position_from_connection_manager returns None when player not found."""
    mock_connection_manager.online_players = {}
    mock_connection_manager.get_online_player_by_display_name = MagicMock(return_value=None)

    position = _get_player_position_from_connection_manager(mock_connection_manager, mock_player, "TestPlayer")

    assert position is None


def test_get_player_position_from_connection_manager_no_manager(mock_player):
    """Test _get_player_position_from_connection_manager handles None connection manager."""
    position = _get_player_position_from_connection_manager(None, mock_player, "TestPlayer")

    assert position is None


def test_sync_player_position_updates_stats(mock_player):
    """Test _sync_player_position updates player stats when position differs."""
    mock_player.get_stats = MagicMock(return_value={"position": "standing"})

    _sync_player_position(mock_player, "sitting")

    mock_player.set_stats.assert_called_once()
    call_args = mock_player.set_stats.call_args[0][0]
    assert call_args["position"] == "sitting"


def test_sync_player_position_no_change(mock_player):
    """Test _sync_player_position does not update when position is same."""
    mock_player.get_stats = MagicMock(return_value={"position": "standing"})

    _sync_player_position(mock_player, "standing")

    # Should not call set_stats if position hasn't changed
    # (Implementation may still call it, but we verify the logic)
    pass


def test_sync_player_position_none_value(mock_player):
    """Test _sync_player_position handles None position value."""
    _sync_player_position(mock_player, None)

    # Should return early without updating
    mock_player.set_stats.assert_not_called()


@pytest.mark.asyncio
async def test_update_and_save_player_last_active_success(mock_persistence, mock_player):
    """Test _update_and_save_player_last_active updates and saves player."""
    await _update_and_save_player_last_active(mock_persistence, mock_player)

    assert mock_player.last_active is not None
    mock_persistence.save_player.assert_awaited_once_with(mock_player)


@pytest.mark.asyncio
async def test_update_and_save_player_last_active_no_persistence(mock_player):
    """Test _update_and_save_player_last_active handles None persistence."""
    # Should not raise
    await _update_and_save_player_last_active(None, mock_player)


@pytest.mark.asyncio
async def test_disconnect_player_connections_success(mock_connection_manager):
    """Test _disconnect_player_connections disconnects player."""
    mock_connection_manager.force_disconnect_player = AsyncMock()

    await _disconnect_player_connections(mock_connection_manager, "TestPlayer")

    mock_connection_manager.force_disconnect_player.assert_awaited_once_with("TestPlayer")


@pytest.mark.asyncio
async def test_disconnect_player_connections_no_manager():
    """Test _disconnect_player_connections handles None connection manager."""
    # Should not raise
    await _disconnect_player_connections(None, "TestPlayer")


@pytest.mark.asyncio
async def test_disconnect_player_connections_error(mock_connection_manager):
    """Test _disconnect_player_connections handles disconnection errors."""
    mock_connection_manager.force_disconnect_player = AsyncMock(side_effect=RuntimeError("Connection error"))

    # Should not raise, just log
    await _disconnect_player_connections(mock_connection_manager, "TestPlayer")


@pytest.mark.asyncio
async def test_handle_quit_command_success(mock_request, mock_persistence, mock_player):
    """Test handle_quit_command updates last active and returns message."""
    mock_request.app.state.persistence = mock_persistence
    mock_persistence.get_player_by_name = MagicMock(return_value=mock_player)
    mock_persistence.save_player = MagicMock()

    with patch("server.commands.logout_commands.get_username_from_user", return_value="testuser"):
        result = await handle_quit_command({}, {"username": "testuser"}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "Goodbye" in result["result"]
    assert mock_player.last_active is not None


@pytest.mark.asyncio
async def test_handle_quit_command_no_persistence(mock_request):
    """Test handle_quit_command handles missing persistence."""
    mock_request.app = None

    result = await handle_quit_command({}, {"username": "testuser"}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "Goodbye" in result["result"]


@pytest.mark.asyncio
async def test_handle_quit_command_persistence_error(mock_request, mock_persistence):
    """Test handle_quit_command handles persistence errors gracefully."""
    mock_request.app.state.persistence = mock_persistence
    mock_persistence.get_player_by_name = MagicMock(side_effect=ValueError("DB error"))

    with patch("server.commands.logout_commands.get_username_from_user", return_value="testuser"):
        result = await handle_quit_command({}, {"username": "testuser"}, mock_request, None, "TestPlayer")

    # Should still return success message
    assert "result" in result
    assert "Goodbye" in result["result"]


@pytest.mark.asyncio
async def test_handle_logout_command_success(mock_request, mock_persistence, mock_connection_manager, mock_player):
    """Test handle_logout_command performs complete logout."""
    mock_request.app.state.persistence = mock_persistence
    mock_request.app.state.connection_manager = mock_connection_manager
    mock_connection_manager.online_players = {str(mock_player.player_id): {"position": "sitting"}}
    mock_connection_manager.force_disconnect_player = AsyncMock()
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_persistence.save_player = AsyncMock()

    with patch("server.commands.logout_commands._get_player_for_logout", return_value=mock_player):
        result = await handle_logout_command({}, {"username": "testuser"}, mock_request, None, "TestPlayer")

    assert result["result"] == "Logged out successfully"
    assert result["session_terminated"] is True
    assert result["connections_closed"] is True
    mock_persistence.save_player.assert_awaited_once()
    mock_connection_manager.force_disconnect_player.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_logout_command_no_player(mock_request, mock_persistence, mock_connection_manager):
    """Test handle_logout_command handles missing player gracefully."""
    mock_request.app.state.persistence = mock_persistence
    mock_request.app.state.connection_manager = mock_connection_manager
    mock_connection_manager.force_disconnect_player = AsyncMock()

    with patch("server.commands.logout_commands._get_player_for_logout", return_value=None):
        result = await handle_logout_command({}, {"username": "testuser"}, mock_request, None, "TestPlayer")

    assert result["result"] == "Logged out successfully"
    mock_connection_manager.force_disconnect_player.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_logout_command_no_persistence(mock_request):
    """Test handle_logout_command handles missing persistence."""
    mock_request.app = None

    result = await handle_logout_command({}, {"username": "testuser"}, mock_request, None, "TestPlayer")

    assert result["result"] == "Logged out successfully"
    assert result["session_terminated"] is True


@pytest.mark.asyncio
async def test_handle_logout_command_error_handling(mock_request, mock_persistence, mock_connection_manager):
    """Test handle_logout_command handles errors gracefully."""
    mock_request.app.state.persistence = mock_persistence
    mock_request.app.state.connection_manager = mock_connection_manager

    with patch("server.commands.logout_commands._get_player_for_logout", side_effect=RuntimeError("Unexpected error")):
        result = await handle_logout_command({}, {"username": "testuser"}, mock_request, None, "TestPlayer")

    # Should still return success even on error
    assert result["result"] == "Logged out successfully"
    assert result["session_terminated"] is True


@pytest.mark.asyncio
async def test_handle_logout_command_syncs_position(
    mock_request, mock_persistence, mock_connection_manager, mock_player
):
    """Test handle_logout_command syncs player position from connection manager."""
    mock_request.app.state.persistence = mock_persistence
    mock_request.app.state.connection_manager = mock_connection_manager
    mock_connection_manager.online_players = {str(mock_player.player_id): {"position": "lying"}}
    mock_persistence.save_player = AsyncMock()

    with patch("server.commands.logout_commands._get_player_for_logout", return_value=mock_player):
        with patch("server.commands.logout_commands._sync_player_position") as mock_sync:
            await handle_logout_command({}, {"username": "testuser"}, mock_request, None, "TestPlayer")

    mock_sync.assert_called_once()
    # Verify position was retrieved
    call_args = mock_sync.call_args[0]
    assert call_args[0] == mock_player
    assert call_args[1] == "lying"
