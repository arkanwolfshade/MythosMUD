"""
Tests for logout and quit command handlers.

This module tests the handle_logout_command and handle_quit_command functions
from server.commands.logout_commands, including all helper functions.
"""

from __future__ import annotations

from datetime import datetime
from types import SimpleNamespace
from unittest.mock import AsyncMock, MagicMock, patch
from uuid import uuid4

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


class TestClearCorruptedCacheEntry:
    """Test _clear_corrupted_cache_entry helper function."""

    def test_clear_corrupted_cache_entry_with_valid_cache(self) -> None:
        """Test clearing cache entry when cache exists."""
        request = SimpleNamespace()
        request.state = SimpleNamespace()
        request.state._command_player_cache = {"testplayer": "cached_data"}

        _clear_corrupted_cache_entry(request, "testplayer")

        assert "testplayer" not in request.state._command_player_cache

    def test_clear_corrupted_cache_entry_with_missing_key(self) -> None:
        """Test clearing cache entry when key doesn't exist."""
        request = SimpleNamespace()
        request.state = SimpleNamespace()
        request.state._command_player_cache = {}

        _clear_corrupted_cache_entry(request, "nonexistent")

        assert "nonexistent" not in request.state._command_player_cache

    def test_clear_corrupted_cache_entry_no_request(self) -> None:
        """Test clearing cache entry when request is None."""
        _clear_corrupted_cache_entry(None, "testplayer")  # Should not raise

    def test_clear_corrupted_cache_entry_no_state(self) -> None:
        """Test clearing cache entry when request has no state."""
        request = SimpleNamespace()
        _clear_corrupted_cache_entry(request, "testplayer")  # Should not raise

    def test_clear_corrupted_cache_entry_no_cache(self) -> None:
        """Test clearing cache entry when cache doesn't exist."""
        request = SimpleNamespace()
        request.state = SimpleNamespace()
        _clear_corrupted_cache_entry(request, "testplayer")  # Should not raise


class TestGetPlayerForLogout:
    """Test _get_player_for_logout helper function."""

    @pytest.mark.asyncio
    async def test_get_player_for_logout_from_cache(self) -> None:
        """Test getting player from cache."""
        mock_player = MagicMock()
        mock_player.name = "testplayer"

        request = SimpleNamespace()
        request.state = SimpleNamespace()
        request.state._command_player_cache = {"testplayer": mock_player}

        with patch("server.commands.logout_commands.get_cached_player", return_value=mock_player):
            result = await _get_player_for_logout(request, None, "testplayer")

            assert result == mock_player

    @pytest.mark.asyncio
    async def test_get_player_for_logout_from_persistence(self) -> None:
        """Test getting player from persistence when not in cache."""
        mock_player = MagicMock()
        mock_player.name = "testplayer"

        mock_persistence = AsyncMock()
        mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)

        request = SimpleNamespace()
        request.state = SimpleNamespace()
        request.state._command_player_cache = {}

        with patch("server.commands.logout_commands.get_cached_player", return_value=None):
            with patch("server.commands.logout_commands.cache_player") as mock_cache:
                result = await _get_player_for_logout(request, mock_persistence, "testplayer")

                assert result == mock_player
                mock_persistence.get_player_by_name.assert_called_once_with("testplayer")
                mock_cache.assert_called_once_with(request, "testplayer", mock_player)

    @pytest.mark.asyncio
    async def test_get_player_for_logout_corrupted_cache_coroutine(self) -> None:
        """Test handling corrupted cache entry that is a coroutine."""

        async def fake_coroutine():
            return None

        request = SimpleNamespace()
        request.state = SimpleNamespace()
        request.state._command_player_cache = {}

        mock_persistence = AsyncMock()
        mock_persistence.get_player_by_name = AsyncMock(return_value=None)

        with patch("server.commands.logout_commands.get_cached_player", return_value=fake_coroutine()):
            with patch("server.commands.logout_commands.logger") as mock_logger:
                with patch("server.commands.logout_commands._clear_corrupted_cache_entry") as mock_clear:
                    result = await _get_player_for_logout(request, mock_persistence, "testplayer")

                    assert result is None
                    mock_clear.assert_called_once()
                    mock_logger.warning.assert_called_once()

    @pytest.mark.asyncio
    async def test_get_player_for_logout_persistence_returns_coroutine(self) -> None:
        """Test handling when persistence returns a coroutine instead of player."""

        async def fake_coroutine():
            return None

        request = SimpleNamespace()
        request.state = SimpleNamespace()
        request.state._command_player_cache = {}

        mock_persistence = AsyncMock()
        mock_persistence.get_player_by_name = AsyncMock(return_value=fake_coroutine())

        with patch("server.commands.logout_commands.get_cached_player", return_value=None):
            with patch("server.commands.logout_commands.logger") as mock_logger:
                result = await _get_player_for_logout(request, mock_persistence, "testplayer")

                assert result is None
                mock_logger.error.assert_called_once()

    @pytest.mark.asyncio
    async def test_get_player_for_logout_persistence_error(self) -> None:
        """Test handling persistence errors."""
        request = SimpleNamespace()
        request.state = SimpleNamespace()
        request.state._command_player_cache = {}

        mock_persistence = AsyncMock()
        mock_persistence.get_player_by_name = AsyncMock(side_effect=Exception("Database error"))

        with patch("server.commands.logout_commands.get_cached_player", return_value=None):
            with patch("server.commands.logout_commands.logger") as mock_logger:
                result = await _get_player_for_logout(request, mock_persistence, "testplayer")

                assert result is None
                mock_logger.error.assert_called_once()

    @pytest.mark.asyncio
    async def test_get_player_for_logout_no_persistence(self) -> None:
        """Test getting player when persistence is None."""
        request = SimpleNamespace()
        request.state = SimpleNamespace()
        request.state._command_player_cache = {}

        with patch("server.commands.logout_commands.get_cached_player", return_value=None):
            result = await _get_player_for_logout(request, None, "testplayer")

            assert result is None


class TestGetPlayerPositionFromConnectionManager:
    """Test _get_player_position_from_connection_manager helper function."""

    def test_get_player_position_from_connection_manager_by_id(self) -> None:
        """Test getting position using player_id."""
        mock_player = MagicMock()
        mock_player.player_id = "player-123"

        mock_connection_manager = MagicMock()
        mock_connection_manager.online_players = {"player-123": {"position": "sitting"}}

        result = _get_player_position_from_connection_manager(mock_connection_manager, mock_player, "testplayer")

        assert result == "sitting"

    def test_get_player_position_from_connection_manager_by_name(self) -> None:
        """Test getting position using display name."""
        mock_player = MagicMock()
        mock_player.player_id = None

        mock_connection_manager = MagicMock()
        mock_connection_manager.online_players = {}
        mock_connection_manager.get_online_player_by_display_name = MagicMock(return_value={"position": "lying"})

        result = _get_player_position_from_connection_manager(mock_connection_manager, mock_player, "testplayer")

        assert result == "lying"

    def test_get_player_position_from_connection_manager_no_connection_manager(self) -> None:
        """Test getting position when connection manager is None."""
        mock_player = MagicMock()

        result = _get_player_position_from_connection_manager(None, mock_player, "testplayer")

        assert result is None

    def test_get_player_position_from_connection_manager_not_found(self) -> None:
        """Test getting position when player is not found."""
        mock_player = MagicMock()
        mock_player.player_id = "player-123"

        mock_connection_manager = MagicMock()
        mock_connection_manager.online_players = {}
        mock_connection_manager.get_online_player_by_display_name = MagicMock(return_value=None)

        result = _get_player_position_from_connection_manager(mock_connection_manager, mock_player, "testplayer")

        assert result is None


class TestSyncPlayerPosition:
    """Test _sync_player_position helper function."""

    def test_sync_player_position_updates_position(self) -> None:
        """Test syncing position when it differs."""
        mock_player = MagicMock()
        mock_player.get_stats.return_value = {"position": "standing"}
        mock_player.set_stats = MagicMock()

        _sync_player_position(mock_player, "sitting")

        mock_player.set_stats.assert_called_once_with({"position": "sitting"})

    def test_sync_player_position_no_change(self) -> None:
        """Test syncing position when it's already correct."""
        mock_player = MagicMock()
        mock_player.get_stats.return_value = {"position": "sitting"}
        mock_player.set_stats = MagicMock()

        _sync_player_position(mock_player, "sitting")

        mock_player.set_stats.assert_not_called()

    def test_sync_player_position_none(self) -> None:
        """Test syncing position when position_value is None."""
        mock_player = MagicMock()
        mock_player.set_stats = MagicMock()

        _sync_player_position(mock_player, None)

        mock_player.set_stats.assert_not_called()


class TestUpdateAndSavePlayerLastActive:
    """Test _update_and_save_player_last_active helper function."""

    @pytest.mark.asyncio
    async def test_update_and_save_player_last_active_success(self) -> None:
        """Test updating and saving player last active timestamp."""
        mock_player = MagicMock()
        mock_player.last_active = None

        mock_persistence = AsyncMock()
        mock_persistence.save_player = AsyncMock()

        with patch("server.commands.logout_commands.logger"):
            await _update_and_save_player_last_active(mock_persistence, mock_player)

            assert mock_player.last_active is not None
            assert isinstance(mock_player.last_active, datetime)
            mock_persistence.save_player.assert_called_once_with(mock_player)

    @pytest.mark.asyncio
    async def test_update_and_save_player_last_active_no_persistence(self) -> None:
        """Test updating when persistence is None."""
        mock_player = MagicMock()

        await _update_and_save_player_last_active(None, mock_player)

        # Should not raise


class TestDisconnectPlayerConnections:
    """Test _disconnect_player_connections helper function."""

    @pytest.mark.asyncio
    async def test_disconnect_player_connections_success(self) -> None:
        """Test disconnecting player connections successfully."""
        mock_connection_manager = MagicMock()
        mock_connection_manager.force_disconnect_player = AsyncMock()

        with patch("server.commands.logout_commands.logger"):
            await _disconnect_player_connections(mock_connection_manager, "testplayer")

            mock_connection_manager.force_disconnect_player.assert_called_once_with("testplayer")

    @pytest.mark.asyncio
    async def test_disconnect_player_connections_no_connection_manager(self) -> None:
        """Test disconnecting when connection manager is None."""
        with patch("server.commands.logout_commands.logger") as mock_logger:
            await _disconnect_player_connections(None, "testplayer")

            mock_logger.warning.assert_called_once()

    @pytest.mark.asyncio
    async def test_disconnect_player_connections_attribute_error(self) -> None:
        """Test handling AttributeError during disconnect."""
        mock_connection_manager = MagicMock()
        mock_connection_manager.force_disconnect_player = AsyncMock(side_effect=AttributeError("Missing method"))

        with patch("server.commands.logout_commands.logger") as mock_logger:
            await _disconnect_player_connections(mock_connection_manager, "testplayer")

            mock_logger.error.assert_called_once()

    @pytest.mark.asyncio
    async def test_disconnect_player_connections_runtime_error(self) -> None:
        """Test handling RuntimeError during disconnect."""
        mock_connection_manager = MagicMock()
        mock_connection_manager.force_disconnect_player = AsyncMock(side_effect=RuntimeError("Connection error"))

        with patch("server.commands.logout_commands.logger") as mock_logger:
            await _disconnect_player_connections(mock_connection_manager, "testplayer")

            mock_logger.error.assert_called_once()


class TestHandleQuitCommand:
    """Test handle_quit_command function."""

    @pytest.mark.asyncio
    async def test_handle_quit_command_success(self) -> None:
        """Test successful quit command."""
        mock_player = MagicMock()
        mock_player.name = "testplayer"
        mock_player.last_active = None

        mock_persistence = MagicMock()
        mock_persistence.get_player_by_name = MagicMock(return_value=mock_player)
        mock_persistence.save_player = MagicMock()

        mock_app = MagicMock()
        mock_app.state = SimpleNamespace()
        mock_app.state.persistence = mock_persistence

        mock_request = MagicMock()
        mock_request.app = mock_app

        current_user = {"username": "testplayer"}

        with patch("server.commands.logout_commands.get_username_from_user", return_value="testplayer"):
            with patch("server.commands.logout_commands.logger"):
                result = await handle_quit_command({}, current_user, mock_request, None, "testplayer")

                assert "Goodbye!" in result["result"]
                assert mock_player.last_active is not None

    @pytest.mark.asyncio
    async def test_handle_quit_command_no_app(self) -> None:
        """Test quit command when app is not available."""
        mock_request = MagicMock()
        mock_request.app = None

        current_user = {"username": "testplayer"}

        with patch("server.commands.logout_commands.logger"):
            result = await handle_quit_command({}, current_user, mock_request, None, "testplayer")

            assert "Goodbye!" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_quit_command_persistence_error(self) -> None:
        """Test quit command when persistence operations fail."""
        mock_persistence = MagicMock()
        mock_persistence.get_player_by_name = MagicMock(side_effect=OSError("Database error"))

        mock_app = MagicMock()
        mock_app.state = SimpleNamespace()
        mock_app.state.persistence = mock_persistence

        mock_request = MagicMock()
        mock_request.app = mock_app

        current_user = {"username": "testplayer"}

        with patch("server.commands.logout_commands.get_username_from_user", return_value="testplayer"):
            with patch("server.commands.logout_commands.logger") as mock_logger:
                result = await handle_quit_command({}, current_user, mock_request, None, "testplayer")

                assert "Goodbye!" in result["result"]
                mock_logger.error.assert_called_once()

    @pytest.mark.asyncio
    async def test_handle_quit_command_player_not_found(self) -> None:
        """Test quit command when player is not found."""
        mock_persistence = MagicMock()
        mock_persistence.get_player_by_name = MagicMock(return_value=None)

        mock_app = MagicMock()
        mock_app.state = SimpleNamespace()
        mock_app.state.persistence = mock_persistence

        mock_request = MagicMock()
        mock_request.app = mock_app

        current_user = {"username": "testplayer"}

        with patch("server.commands.logout_commands.get_username_from_user", return_value="testplayer"):
            with patch("server.commands.logout_commands.logger"):
                result = await handle_quit_command({}, current_user, mock_request, None, "testplayer")

                assert "Goodbye!" in result["result"]


class TestHandleLogoutCommand:
    """Test handle_logout_command function."""

    @pytest.mark.asyncio
    async def test_handle_logout_command_success(self) -> None:
        """Test successful logout command."""
        player_id = str(uuid4())
        mock_player = MagicMock()
        mock_player.player_id = player_id
        mock_player.name = "testplayer"
        mock_player.get_stats.return_value = {"position": "standing"}

        mock_persistence = AsyncMock()
        mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
        mock_persistence.save_player = AsyncMock()

        mock_connection_manager = MagicMock()
        mock_connection_manager.online_players = {player_id: {"position": "sitting"}}
        mock_connection_manager.get_online_player_by_display_name = MagicMock(return_value=None)
        mock_connection_manager.force_disconnect_player = AsyncMock()

        mock_app = MagicMock()
        mock_app.state = SimpleNamespace()
        mock_app.state.persistence = mock_persistence
        mock_app.state.connection_manager = mock_connection_manager

        mock_request = MagicMock()
        mock_request.app = mock_app
        mock_request.state = SimpleNamespace()
        mock_request.state._command_player_cache = {}

        current_user = {"username": "testplayer"}

        with patch("server.commands.logout_commands.get_username_from_user", return_value="testplayer"):
            with patch("server.commands.logout_commands.get_cached_player", return_value=None):
                with patch("server.commands.logout_commands.cache_player"):
                    with patch("server.commands.logout_commands.logger"):
                        result = await handle_logout_command({}, current_user, mock_request, None, "testplayer")

                        assert "Logged out successfully" in result["result"]
                        assert result["session_terminated"] is True
                        assert result["connections_closed"] is True
                        mock_persistence.save_player.assert_called_once()
                        mock_connection_manager.force_disconnect_player.assert_called_once_with("testplayer")

    @pytest.mark.asyncio
    async def test_handle_logout_command_no_app(self) -> None:
        """Test logout command when app is not available."""
        mock_request = MagicMock()
        mock_request.app = None

        current_user = {"username": "testplayer"}

        with patch("server.commands.logout_commands.get_username_from_user", return_value="testplayer"):
            with patch("server.commands.logout_commands.logger"):
                result = await handle_logout_command({}, current_user, mock_request, None, "testplayer")

                assert "Logged out successfully" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_logout_command_player_not_found(self) -> None:
        """Test logout command when player is not found."""
        mock_persistence = AsyncMock()
        mock_persistence.get_player_by_name = AsyncMock(return_value=None)

        mock_connection_manager = MagicMock()
        mock_connection_manager.force_disconnect_player = AsyncMock()

        mock_app = MagicMock()
        mock_app.state = SimpleNamespace()
        mock_app.state.persistence = mock_persistence
        mock_app.state.connection_manager = mock_connection_manager

        mock_request = MagicMock()
        mock_request.app = mock_app
        mock_request.state = SimpleNamespace()
        mock_request.state._command_player_cache = {}

        current_user = {"username": "testplayer"}

        with patch("server.commands.logout_commands.get_username_from_user", return_value="testplayer"):
            with patch("server.commands.logout_commands.get_cached_player", return_value=None):
                with patch("server.commands.logout_commands.logger"):
                    result = await handle_logout_command({}, current_user, mock_request, None, "testplayer")

                    assert "Logged out successfully" in result["result"]
                    mock_connection_manager.force_disconnect_player.assert_called_once()

    @pytest.mark.asyncio
    async def test_handle_logout_command_exception_handling(self) -> None:
        """Test logout command exception handling."""
        mock_persistence = AsyncMock()
        mock_persistence.get_player_by_name = AsyncMock(side_effect=Exception("Unexpected error"))

        mock_connection_manager = MagicMock()
        mock_connection_manager.force_disconnect_player = AsyncMock()

        mock_app = MagicMock()
        mock_app.state = SimpleNamespace()
        mock_app.state.persistence = mock_persistence
        mock_app.state.connection_manager = mock_connection_manager

        mock_request = MagicMock()
        mock_request.app = mock_app
        mock_request.state = SimpleNamespace()
        mock_request.state._command_player_cache = {}

        current_user = {"username": "testplayer"}

        with patch("server.commands.logout_commands.get_username_from_user", return_value="testplayer"):
            with patch("server.commands.logout_commands.get_cached_player", return_value=None):
                with patch("server.commands.logout_commands.logger") as mock_logger:
                    result = await handle_logout_command({}, current_user, mock_request, None, "testplayer")

                    assert "Logged out successfully" in result["result"]
                    mock_logger.error.assert_called_once()
