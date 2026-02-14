"""
Unit tests for the logout command handler.
"""

import uuid
from typing import Any
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.commands.utility_commands import handle_logout_command

# Valid UUID for mock player (handle_logout_command uses UUID(player_id))
_TEST_PLAYER_UUID_STR = "12345678-1234-1234-1234-123456789012"
_TEST_PLAYER_UUID = uuid.UUID(_TEST_PLAYER_UUID_STR)


class TestLogoutCommand:
    """Test cases for the logout command handler."""

    @pytest.fixture
    def mock_request(self) -> MagicMock:
        """Create a mock request object."""
        request = MagicMock()
        request.app = MagicMock()
        request.app.state = MagicMock()
        request.app.state.persistence = MagicMock()
        # Ensure code uses app.state.persistence (not container.async_persistence)
        request.app.state.container = None
        return request

    @pytest.fixture
    def mock_current_user(self) -> dict[str, str]:
        """Create a mock current user."""
        return {"username": "testplayer", "user_id": "123"}

    @pytest.fixture
    def mock_alias_storage(self) -> MagicMock:
        """Create a mock alias storage."""
        return MagicMock()

    @pytest.mark.asyncio
    async def test_logout_command_success(
        self,
        mock_request: MagicMock,
        mock_current_user: dict[str, Any],
        mock_alias_storage: MagicMock,
    ) -> None:
        """Test successful logout command execution."""
        # Mock the persistence layer
        mock_player = MagicMock()
        mock_player.name = "testplayer"
        mock_player.player_id = _TEST_PLAYER_UUID_STR
        mock_player.get_stats.return_value = {"position": "standing"}
        mock_request.app.state.persistence.get_player_by_name = AsyncMock(return_value=mock_player)
        mock_request.app.state.persistence.save_player = AsyncMock()

        # Mock the connection manager (_disconnect_player_connections uses async_persistence)
        mock_connection_manager = MagicMock()
        mock_connection_manager.force_disconnect_player = AsyncMock()
        mock_connection_manager.online_players = {}
        mock_connection_manager.get_online_player_by_display_name.return_value = None
        mock_connection_manager.async_persistence = MagicMock()
        mock_connection_manager.async_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
        mock_request.app.state.connection_manager = mock_connection_manager

        # Execute logout command
        result = await handle_logout_command(
            command_data={"args": []},
            current_user=mock_current_user,
            request=mock_request,
            _alias_storage=mock_alias_storage,
            player_name="testplayer",
        )

        # Verify result
        assert "result" in result
        assert "Logged out successfully" in result["result"]
        assert "session_terminated" in result
        assert "connections_closed" in result
        assert result["session_terminated"] is True
        assert result["connections_closed"] is True

        # Verify persistence operations
        mock_request.app.state.persistence.get_player_by_name.assert_called_once_with("testplayer")
        mock_request.app.state.persistence.save_player.assert_called_once()

        # Verify connection cleanup (implementation uses UUID, not display name)
        mock_connection_manager.force_disconnect_player.assert_called_once_with(_TEST_PLAYER_UUID)

    @pytest.mark.asyncio
    async def test_logout_command_persists_position(
        self,
        mock_request: MagicMock,
        mock_current_user: dict[str, Any],
        mock_alias_storage: MagicMock,
    ) -> None:
        """Ensure logout syncs in-memory position back to persistence."""
        mock_player = MagicMock()
        mock_player.name = "testplayer"
        mock_player.player_id = _TEST_PLAYER_UUID_STR
        mock_player.get_stats.return_value = {"position": "standing"}
        mock_request.app.state.persistence.get_player_by_name = AsyncMock(return_value=mock_player)
        mock_request.app.state.persistence.save_player = AsyncMock()

        mock_connection_manager = MagicMock()
        mock_connection_manager.force_disconnect_player = AsyncMock()
        mock_connection_manager.online_players = {_TEST_PLAYER_UUID_STR: {"position": "sitting"}}
        mock_connection_manager.get_online_player_by_display_name.return_value = None
        mock_connection_manager.async_persistence = MagicMock()
        mock_connection_manager.async_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
        mock_request.app.state.connection_manager = mock_connection_manager

        await handle_logout_command(
            command_data={"args": []},
            current_user=mock_current_user,
            request=mock_request,
            _alias_storage=mock_alias_storage,
            player_name="testplayer",
        )

        mock_player.set_stats.assert_called_once_with({"position": "sitting"})
        mock_request.app.state.persistence.save_player.assert_called_once_with(mock_player)

    @pytest.mark.asyncio
    async def test_logout_command_no_persistence(
        self,
        mock_current_user: dict[str, Any],
        mock_alias_storage: MagicMock,
    ) -> None:
        """Test logout command when persistence is not available."""
        mock_request = MagicMock()
        mock_request.app = None

        # Execute logout command
        result = await handle_logout_command(
            command_data={"args": []},
            current_user=mock_current_user,
            request=mock_request,
            _alias_storage=mock_alias_storage,
            player_name="testplayer",
        )

        # Verify result
        assert "result" in result
        assert "Logged out successfully" in result["result"]
        assert "session_terminated" in result
        assert "connections_closed" in result

    @pytest.mark.asyncio
    async def test_logout_command_persistence_error(
        self,
        mock_request: MagicMock,
        mock_current_user: dict[str, Any],
        mock_alias_storage: MagicMock,
    ) -> None:
        """Test logout command when persistence operations fail."""
        # Mock persistence to raise an error (async)
        mock_request.app.state.persistence.get_player_by_name = AsyncMock(side_effect=Exception("Database error"))

        # Mock the connection manager so force_disconnect can run (async_persistence for player_id)
        mock_connection_manager = MagicMock()
        mock_connection_manager.force_disconnect_player = AsyncMock()
        mock_connection_manager.online_players = {}
        mock_connection_manager.get_online_player_by_display_name.return_value = {
            "player_id": "12345678-1234-1234-1234-123456789012"
        }
        mock_connection_manager.async_persistence = MagicMock()
        mock_connection_manager.async_persistence.get_player_by_name = AsyncMock(return_value=None)
        mock_request.app.state.connection_manager = mock_connection_manager

        # Execute logout command
        result = await handle_logout_command(
            command_data={"args": []},
            current_user=mock_current_user,
            request=mock_request,
            _alias_storage=mock_alias_storage,
            player_name="testplayer",
        )

        # Verify result - should still succeed despite persistence error
        assert "result" in result
        assert "Logged out successfully" in result["result"]
        assert "session_terminated" in result
        assert "connections_closed" in result

        # Verify connection cleanup still happens (via fallback; implementation uses UUID)
        mock_connection_manager.force_disconnect_player.assert_called_once_with(_TEST_PLAYER_UUID)

    @pytest.mark.asyncio
    async def test_logout_command_connection_error(
        self,
        mock_request: MagicMock,
        mock_current_user: dict[str, Any],
        mock_alias_storage: MagicMock,
    ) -> None:
        """Test logout command when connection cleanup fails."""
        # Mock the persistence layer
        mock_player = MagicMock()
        mock_player.name = "testplayer"
        mock_player.player_id = _TEST_PLAYER_UUID_STR
        mock_request.app.state.persistence.get_player_by_name = AsyncMock(return_value=mock_player)
        mock_request.app.state.persistence.save_player = AsyncMock()

        # Mock the connection manager to raise an error (async_persistence so player_id is set)
        mock_connection_manager = MagicMock()
        mock_connection_manager.force_disconnect_player = AsyncMock(side_effect=Exception("Connection error"))
        mock_connection_manager.online_players = {}
        mock_connection_manager.get_online_player_by_display_name.return_value = None
        mock_connection_manager.async_persistence = MagicMock()
        mock_connection_manager.async_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
        mock_request.app.state.connection_manager = mock_connection_manager

        # Execute logout command
        result = await handle_logout_command(
            command_data={"args": []},
            current_user=mock_current_user,
            request=mock_request,
            _alias_storage=mock_alias_storage,
            player_name="testplayer",
        )

        # Verify result - should still succeed despite connection error
        assert "result" in result
        assert "Logged out successfully" in result["result"]
        assert "session_terminated" in result
        assert "connections_closed" in result

    @pytest.mark.asyncio
    async def test_logout_command_with_args(
        self,
        mock_request: MagicMock,
        mock_current_user: dict[str, Any],
        mock_alias_storage: MagicMock,
    ) -> None:
        """Test logout command with arguments (should be ignored)."""
        # Mock the persistence layer
        mock_player = MagicMock()
        mock_player.name = "testplayer"
        mock_player.player_id = _TEST_PLAYER_UUID_STR
        mock_request.app.state.persistence.get_player_by_name = AsyncMock(return_value=mock_player)
        mock_request.app.state.persistence.save_player = AsyncMock()

        # Mock the connection manager
        mock_connection_manager = MagicMock()
        mock_connection_manager.force_disconnect_player = AsyncMock()
        mock_connection_manager.online_players = {}
        mock_connection_manager.get_online_player_by_display_name.return_value = None
        mock_connection_manager.async_persistence = MagicMock()
        mock_connection_manager.async_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
        mock_request.app.state.connection_manager = mock_connection_manager

        # Execute logout command with arguments
        result = await handle_logout_command(
            command_data={"args": ["force", "now"]},
            current_user=mock_current_user,
            request=mock_request,
            _alias_storage=mock_alias_storage,
            player_name="testplayer",
        )

        # Verify result
        assert "result" in result
        assert "Logged out successfully" in result["result"]

    @pytest.mark.asyncio
    async def test_logout_command_player_not_found(
        self,
        mock_request: MagicMock,
        mock_current_user: dict[str, Any],
        mock_alias_storage: MagicMock,
    ) -> None:
        """Test logout command when player is not found in persistence."""
        # Mock persistence to return None (player not found)
        mock_request.app.state.persistence.get_player_by_name = AsyncMock(return_value=None)

        # Mock the connection manager; provide online_players so disconnect can resolve player_id
        mock_connection_manager = MagicMock()
        mock_connection_manager.force_disconnect_player = AsyncMock()
        mock_connection_manager.online_players = {}
        mock_connection_manager.async_persistence = AsyncMock(return_value=None)
        mock_connection_manager.get_online_player_by_display_name.return_value = {
            "player_id": "12345678-1234-1234-1234-123456789012"
        }
        mock_request.app.state.connection_manager = mock_connection_manager

        # Execute logout command
        result = await handle_logout_command(
            command_data={"args": []},
            current_user=mock_current_user,
            request=mock_request,
            _alias_storage=mock_alias_storage,
            player_name="testplayer",
        )

        # Verify result
        assert "result" in result
        assert "Logged out successfully" in result["result"]
        assert "session_terminated" in result
        assert "connections_closed" in result

        # Verify connection cleanup still happens via display name fallback
        mock_connection_manager.force_disconnect_player.assert_called_once()

    @pytest.mark.asyncio
    async def test_logout_command_general_error_handling(
        self,
        mock_request: MagicMock,
        mock_current_user: dict[str, Any],
        mock_alias_storage: MagicMock,
    ) -> None:
        """Test logout command with general error handling."""
        # Mock the persistence layer to raise an error (async)
        mock_request.app.state.persistence.get_player_by_name = AsyncMock(side_effect=Exception("Unexpected error"))

        # Mock the connection manager to raise an error (async_persistence for player_id path)
        mock_connection_manager = MagicMock()
        mock_connection_manager.force_disconnect_player = AsyncMock(side_effect=Exception("Connection error"))
        mock_connection_manager.online_players = {}
        mock_connection_manager.get_online_player_by_display_name.return_value = {
            "player_id": "12345678-1234-1234-1234-123456789012"
        }
        mock_connection_manager.async_persistence = MagicMock()
        mock_connection_manager.async_persistence.get_player_by_name = AsyncMock(return_value=None)
        mock_request.app.state.connection_manager = mock_connection_manager

        # Execute logout command
        result = await handle_logout_command(
            command_data={"args": []},
            current_user=mock_current_user,
            request=mock_request,
            _alias_storage=mock_alias_storage,
            player_name="testplayer",
        )

        # Verify result - should still return success message
        assert "result" in result
        assert "Logged out successfully" in result["result"]
        assert "session_terminated" in result
        assert "connections_closed" in result
