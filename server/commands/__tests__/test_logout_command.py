"""
Unit tests for the logout command handler.
"""

from unittest.mock import AsyncMock, MagicMock

import pytest

from server.commands.utility_commands import handle_logout_command


class TestLogoutCommand:
    """Test cases for the logout command handler."""

    @pytest.fixture
    def mock_request(self):
        """Create a mock request object."""
        request = MagicMock()
        request.app = MagicMock()
        request.app.state = MagicMock()
        request.app.state.persistence = MagicMock()
        return request

    @pytest.fixture
    def mock_current_user(self):
        """Create a mock current user."""
        return {"username": "testplayer", "user_id": "123"}

    @pytest.fixture
    def mock_alias_storage(self):
        """Create a mock alias storage."""
        return MagicMock()

    @pytest.mark.asyncio
    async def test_logout_command_success(self, mock_request, mock_current_user, mock_alias_storage):
        """Test successful logout command execution."""
        # Mock the persistence layer
        mock_player = MagicMock()
        mock_player.name = "testplayer"
        mock_request.app.state.persistence.get_player_by_name.return_value = mock_player
        mock_request.app.state.persistence.save_player = AsyncMock()

        # Mock the connection manager
        mock_connection_manager = MagicMock()
        mock_connection_manager.force_disconnect_player = AsyncMock()
        mock_request.app.state.connection_manager = mock_connection_manager

        # Execute logout command
        result = await handle_logout_command(
            args=[],
            current_user=mock_current_user,
            request=mock_request,
            alias_storage=mock_alias_storage,
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

        # Verify connection cleanup
        mock_connection_manager.force_disconnect_player.assert_called_once_with("testplayer")

    @pytest.mark.asyncio
    async def test_logout_command_no_persistence(self, mock_current_user, mock_alias_storage):
        """Test logout command when persistence is not available."""
        mock_request = MagicMock()
        mock_request.app = None

        # Execute logout command
        result = await handle_logout_command(
            args=[],
            current_user=mock_current_user,
            request=mock_request,
            alias_storage=mock_alias_storage,
            player_name="testplayer",
        )

        # Verify result
        assert "result" in result
        assert "Logged out successfully" in result["result"]
        assert "session_terminated" in result
        assert "connections_closed" in result

    @pytest.mark.asyncio
    async def test_logout_command_persistence_error(self, mock_request, mock_current_user, mock_alias_storage):
        """Test logout command when persistence operations fail."""
        # Mock persistence to raise an error
        mock_request.app.state.persistence.get_player_by_name.side_effect = Exception("Database error")

        # Mock the connection manager
        mock_connection_manager = MagicMock()
        mock_connection_manager.force_disconnect_player = AsyncMock()
        mock_request.app.state.connection_manager = mock_connection_manager

        # Execute logout command
        result = await handle_logout_command(
            args=[],
            current_user=mock_current_user,
            request=mock_request,
            alias_storage=mock_alias_storage,
            player_name="testplayer",
        )

        # Verify result - should still succeed despite persistence error
        assert "result" in result
        assert "Logged out successfully" in result["result"]
        assert "session_terminated" in result
        assert "connections_closed" in result

        # Verify connection cleanup still happens
        mock_connection_manager.force_disconnect_player.assert_called_once_with("testplayer")

    @pytest.mark.asyncio
    async def test_logout_command_connection_error(self, mock_request, mock_current_user, mock_alias_storage):
        """Test logout command when connection cleanup fails."""
        # Mock the persistence layer
        mock_player = MagicMock()
        mock_player.name = "testplayer"
        mock_request.app.state.persistence.get_player_by_name.return_value = mock_player
        mock_request.app.state.persistence.save_player = AsyncMock()

        # Mock the connection manager to raise an error
        mock_connection_manager = MagicMock()
        mock_connection_manager.force_disconnect_player = AsyncMock(side_effect=Exception("Connection error"))
        mock_request.app.state.connection_manager = mock_connection_manager

        # Execute logout command
        result = await handle_logout_command(
            args=[],
            current_user=mock_current_user,
            request=mock_request,
            alias_storage=mock_alias_storage,
            player_name="testplayer",
        )

        # Verify result - should still succeed despite connection error
        assert "result" in result
        assert "Logged out successfully" in result["result"]
        assert "session_terminated" in result
        assert "connections_closed" in result

    @pytest.mark.asyncio
    async def test_logout_command_with_args(self, mock_request, mock_current_user, mock_alias_storage):
        """Test logout command with arguments (should be ignored)."""
        # Mock the persistence layer
        mock_player = MagicMock()
        mock_player.name = "testplayer"
        mock_request.app.state.persistence.get_player_by_name.return_value = mock_player
        mock_request.app.state.persistence.save_player = AsyncMock()

        # Mock the connection manager
        mock_connection_manager = MagicMock()
        mock_connection_manager.force_disconnect_player = AsyncMock()
        mock_request.app.state.connection_manager = mock_connection_manager

        # Execute logout command with arguments
        result = await handle_logout_command(
            args=["force", "now"],
            current_user=mock_current_user,
            request=mock_request,
            alias_storage=mock_alias_storage,
            player_name="testplayer",
        )

        # Verify result
        assert "result" in result
        assert "Logged out successfully" in result["result"]

    @pytest.mark.asyncio
    async def test_logout_command_player_not_found(self, mock_request, mock_current_user, mock_alias_storage):
        """Test logout command when player is not found in persistence."""
        # Mock persistence to return None (player not found)
        mock_request.app.state.persistence.get_player_by_name.return_value = None

        # Mock the connection manager
        mock_connection_manager = MagicMock()
        mock_connection_manager.force_disconnect_player = AsyncMock()
        mock_request.app.state.connection_manager = mock_connection_manager

        # Execute logout command
        result = await handle_logout_command(
            args=[],
            current_user=mock_current_user,
            request=mock_request,
            alias_storage=mock_alias_storage,
            player_name="testplayer",
        )

        # Verify result
        assert "result" in result
        assert "Logged out successfully" in result["result"]
        assert "session_terminated" in result
        assert "connections_closed" in result

        # Verify connection cleanup still happens
        mock_connection_manager.force_disconnect_player.assert_called_once_with("testplayer")

    @pytest.mark.asyncio
    async def test_logout_command_general_error_handling(self, mock_request, mock_current_user, mock_alias_storage):
        """Test logout command with general error handling."""
        # Mock the persistence layer to raise an error
        mock_request.app.state.persistence.get_player_by_name.side_effect = Exception("Unexpected error")

        # Mock the connection manager to raise an error
        mock_connection_manager = MagicMock()
        mock_connection_manager.force_disconnect_player = AsyncMock(side_effect=Exception("Connection error"))
        mock_request.app.state.connection_manager = mock_connection_manager

        # Execute logout command
        result = await handle_logout_command(
            args=[],
            current_user=mock_current_user,
            request=mock_request,
            alias_storage=mock_alias_storage,
            player_name="testplayer",
        )

        # Verify result - should still return success message
        assert "result" in result
        assert "Logged out successfully" in result["result"]
        assert "session_terminated" in result
        assert "connections_closed" in result
