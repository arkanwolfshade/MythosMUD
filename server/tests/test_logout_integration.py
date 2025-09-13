"""
Integration tests for logout functionality.
"""

import pytest
from unittest.mock import AsyncMock, MagicMock, patch

from server.command_handler_unified import process_command_unified


class TestLogoutIntegration:
    """Integration tests for logout command processing."""

    @pytest.fixture
    def mock_current_user(self):
        """Create a mock current user."""
        return {"username": "testplayer", "user_id": "123"}

    @pytest.fixture
    def mock_request(self):
        """Create a mock request object."""
        request = MagicMock()
        request.app = MagicMock()
        request.app.state = MagicMock()
        request.app.state.persistence = MagicMock()
        return request

    @pytest.mark.asyncio
    async def test_logout_command_through_unified_handler(self, mock_current_user, mock_request):
        """Test logout command processing through the unified command handler."""
        # Mock the persistence layer
        mock_player = MagicMock()
        mock_player.name = "testplayer"
        mock_request.app.state.persistence.get_player_by_name.return_value = mock_player
        mock_request.app.state.persistence.save_player = AsyncMock()

        # Mock the connection manager
        mock_connection_manager = MagicMock()
        mock_connection_manager.force_disconnect_player = AsyncMock()
        mock_request.app.state.connection_manager = mock_connection_manager

        # Process logout command through unified handler
        result = await process_command_unified(
            command_line="logout", current_user=mock_current_user, request=mock_request, player_name="testplayer"
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
    async def test_logout_command_with_arguments(self, mock_current_user, mock_request):
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

        # Process logout command with arguments
        result = await process_command_unified(
            command_line="logout force now",
            current_user=mock_current_user,
            request=mock_request,
            player_name="testplayer",
        )

        # Verify result
        assert "result" in result
        assert "Logged out successfully" in result["result"]
        assert "session_terminated" in result
        assert "connections_closed" in result

    @pytest.mark.asyncio
    async def test_logout_command_with_slash_prefix(self, mock_current_user, mock_request):
        """Test logout command with slash prefix (should be normalized)."""
        # Mock the persistence layer
        mock_player = MagicMock()
        mock_player.name = "testplayer"
        mock_request.app.state.persistence.get_player_by_name.return_value = mock_player
        mock_request.app.state.persistence.save_player = AsyncMock()

        # Mock the connection manager
        mock_connection_manager = MagicMock()
        mock_connection_manager.force_disconnect_player = AsyncMock()
        mock_request.app.state.connection_manager = mock_connection_manager

        # Process logout command with slash prefix
        result = await process_command_unified(
            command_line="/logout", current_user=mock_current_user, request=mock_request, player_name="testplayer"
        )

        # Verify result
        assert "result" in result
        assert "Logged out successfully" in result["result"]
        assert "session_terminated" in result
        assert "connections_closed" in result

    @pytest.mark.asyncio
    async def test_logout_command_error_handling(self, mock_current_user, mock_request):
        """Test logout command error handling and graceful degradation."""
        # Mock persistence to raise an error
        mock_request.app.state.persistence.get_player_by_name.side_effect = Exception("Database error")

        # Mock the connection manager to raise an error
        mock_connection_manager = MagicMock()
        mock_connection_manager.force_disconnect_player = AsyncMock(side_effect=Exception("Connection error"))
        mock_request.app.state.connection_manager = mock_connection_manager

        # Process logout command
        result = await process_command_unified(
            command_line="logout", current_user=mock_current_user, request=mock_request, player_name="testplayer"
        )

        # Verify result - should still succeed despite errors
        assert "result" in result
        assert "Logged out successfully" in result["result"]
        assert "session_terminated" in result
        assert "connections_closed" in result

    @pytest.mark.asyncio
    async def test_logout_command_no_connection_manager(self, mock_current_user, mock_request):
        """Test logout command when connection manager is not available."""
        # Mock the persistence layer
        mock_player = MagicMock()
        mock_player.name = "testplayer"
        mock_request.app.state.persistence.get_player_by_name.return_value = mock_player
        mock_request.app.state.persistence.save_player = AsyncMock()

        # Don't set connection manager (simulate it not being available)
        mock_request.app.state.connection_manager = None

        # Process logout command
        result = await process_command_unified(
            command_line="logout", current_user=mock_current_user, request=mock_request, player_name="testplayer"
        )

        # Verify result - should still succeed
        assert "result" in result
        assert "Logged out successfully" in result["result"]
        assert "session_terminated" in result
        assert "connections_closed" in result

    @pytest.mark.asyncio
    async def test_logout_command_case_insensitive(self, mock_current_user, mock_request):
        """Test logout command is case insensitive."""
        # Mock the persistence layer
        mock_player = MagicMock()
        mock_player.name = "testplayer"
        mock_request.app.state.persistence.get_player_by_name.return_value = mock_player
        mock_request.app.state.persistence.save_player = AsyncMock()

        # Mock the connection manager
        mock_connection_manager = MagicMock()
        mock_connection_manager.force_disconnect_player = AsyncMock()
        mock_request.app.state.connection_manager = mock_connection_manager

        # Test various case combinations
        test_cases = ["LOGOUT", "Logout", "lOgOuT", "logout"]

        for command in test_cases:
            # Reset mocks
            mock_connection_manager.reset_mock()
            mock_request.app.state.persistence.reset_mock()

            # Process logout command
            result = await process_command_unified(
                command_line=command, current_user=mock_current_user, request=mock_request, player_name="testplayer"
            )

            # Verify result
            assert "result" in result
            assert "Logged out successfully" in result["result"]
            assert "session_terminated" in result
            assert "connections_closed" in result
