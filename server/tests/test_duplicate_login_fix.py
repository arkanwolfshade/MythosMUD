"""
Test for duplicate login bug fix.

This test verifies that when a player logs in multiple times, the server
properly disconnects existing sessions to prevent duplicate logins.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from ..models import Player, User
from ..realtime.connection_manager import ConnectionManager


class TestDuplicateLoginFix:
    """Test cases for the duplicate login bug fix."""

    @pytest.fixture
    def mock_user(self):
        """Create a mock user for testing."""
        user = MagicMock(spec=User)
        user.id = "test-user-id"
        user.username = "testuser"
        user.email = "test@example.com"
        user.is_active = True
        user.is_verified = True
        return user

    @pytest.fixture
    def mock_player(self):
        """Create a mock player for testing."""
        player = MagicMock(spec=Player)
        player.player_id = "test-player-id"
        player.name = "testuser"
        player.user_id = "test-user-id"
        return player

    @pytest.fixture
    def mock_connection_manager(self):
        """Create a mock connection manager."""
        manager = MagicMock(spec=ConnectionManager)
        manager.handle_new_game_session = AsyncMock()
        return manager

    @pytest.fixture
    def mock_persistence(self):
        """Create a mock persistence layer."""
        persistence = MagicMock()
        persistence.get_player_by_user_id = MagicMock()
        return persistence

    @pytest.mark.asyncio
    async def test_login_disconnects_existing_sessions(
        self, mock_user, mock_player, mock_connection_manager, mock_persistence
    ):
        """
        Test that login disconnects existing sessions for the same player.

        This test verifies the core fix for the duplicate login bug where
        the same player could be logged in multiple times simultaneously.
        """
        # Setup mocks
        mock_persistence.get_player_by_user_id.return_value = mock_player
        mock_connection_manager.handle_new_game_session.return_value = {
            "success": True,
            "connections_disconnected": 2,
            "errors": []
        }

        # Mock the connection manager import - patch the import inside the function
        with patch("server.realtime.connection_manager.connection_manager", mock_connection_manager):
            with patch("server.auth.endpoints.get_persistence", return_value=mock_persistence):
                with patch("server.auth.endpoints.user_manager") as mock_user_manager:
                    # Mock user authentication
                    mock_user_manager.authenticate_user.return_value = mock_user

                    # Mock JWT token generation
                    with patch("server.auth.endpoints.generate_jwt", return_value="mock-jwt-token"):
                        # Import the login function
                        from fastapi import Request

                        from ..auth.endpoints import login_user
                        from ..auth.schemas import LoginRequest

                        # Create test request
                        login_request = LoginRequest(username="testuser", password="testpass")
                        mock_request = MagicMock(spec=Request)

                        # Call the login function
                        result = await login_user(
                            request=login_request,
                            http_request=mock_request,
                            user_manager=mock_user_manager,
                            session=MagicMock()
                        )

                        # Verify the result
                        assert result.access_token == "mock-jwt-token"
                        assert result.user_id == "test-user-id"
                        assert result.has_character is True
                        assert result.character_name == "testuser"

                        # Verify that handle_new_game_session was called
                        mock_connection_manager.handle_new_game_session.assert_called_once()

                        # Verify the call arguments
                        call_args = mock_connection_manager.handle_new_game_session.call_args
                        assert call_args[0][0] == "test-player-id"  # player_id
                        assert call_args[0][1].startswith("login_")  # session_id starts with "login_"

    @pytest.mark.asyncio
    async def test_login_without_character_skips_session_management(
        self, mock_user, mock_connection_manager, mock_persistence
    ):
        """
        Test that login without a character skips session management.

        This ensures that users without characters don't trigger session
        management, which would be unnecessary.
        """
        # Setup mocks - no player exists
        mock_persistence.get_player_by_user_id.return_value = None

        # Mock the connection manager import - patch the import inside the function
        with patch("server.realtime.connection_manager.connection_manager", mock_connection_manager):
            with patch("server.auth.endpoints.get_persistence", return_value=mock_persistence):
                with patch("server.auth.endpoints.user_manager") as mock_user_manager:
                    # Mock user authentication
                    mock_user_manager.authenticate_user.return_value = mock_user

                    # Mock JWT token generation
                    with patch("server.auth.endpoints.generate_jwt", return_value="mock-jwt-token"):
                        # Import the login function
                        from fastapi import Request

                        from ..auth.endpoints import login_user
                        from ..auth.schemas import LoginRequest

                        # Create test request
                        login_request = LoginRequest(username="testuser", password="testpass")
                        mock_request = MagicMock(spec=Request)

                        # Call the login function
                        result = await login_user(
                            request=login_request,
                            http_request=mock_request,
                            user_manager=mock_user_manager,
                            session=MagicMock()
                        )

                        # Verify the result
                        assert result.access_token == "mock-jwt-token"
                        assert result.user_id == "test-user-id"
                        assert result.has_character is False
                        assert result.character_name is None

                        # Verify that handle_new_game_session was NOT called
                        mock_connection_manager.handle_new_game_session.assert_not_called()

    @pytest.mark.asyncio
    async def test_login_session_management_error_handling(
        self, mock_user, mock_player, mock_connection_manager, mock_persistence
    ):
        """
        Test that login handles session management errors gracefully.

        This ensures that if session management fails, the login still succeeds
        but logs appropriate warnings.
        """
        # Setup mocks
        mock_persistence.get_player_by_user_id.return_value = mock_player
        mock_connection_manager.handle_new_game_session.return_value = {
            "success": False,
            "connections_disconnected": 0,
            "errors": ["Connection timeout"]
        }

        # Mock the connection manager import - patch the import inside the function
        with patch("server.realtime.connection_manager.connection_manager", mock_connection_manager):
            with patch("server.auth.endpoints.get_persistence", return_value=mock_persistence):
                with patch("server.auth.endpoints.user_manager") as mock_user_manager:
                    # Mock user authentication
                    mock_user_manager.authenticate_user.return_value = mock_user

                    # Mock JWT token generation
                    with patch("server.auth.endpoints.generate_jwt", return_value="mock-jwt-token"):
                        # Import the login function
                        from fastapi import Request

                        from ..auth.endpoints import login_user
                        from ..auth.schemas import LoginRequest

                        # Create test request
                        login_request = LoginRequest(username="testuser", password="testpass")
                        mock_request = MagicMock(spec=Request)

                        # Call the login function
                        result = await login_user(
                            request=login_request,
                            http_request=mock_request,
                            user_manager=mock_user_manager,
                            session=MagicMock()
                        )

                        # Verify the result - login should still succeed
                        assert result.access_token == "mock-jwt-token"
                        assert result.user_id == "test-user-id"
                        assert result.has_character is True
                        assert result.character_name == "testuser"

                        # Verify that handle_new_game_session was called
                        mock_connection_manager.handle_new_game_session.assert_called_once()

    def test_connection_manager_handle_new_game_session_signature(self):
        """
        Test that the connection manager's handle_new_game_session method
        has the expected signature and behavior.

        This is a regression test to ensure the method exists and works
        as expected for the duplicate login fix.
        """
        from ..realtime.connection_manager import ConnectionManager

        # Verify the method exists
        assert hasattr(ConnectionManager, 'handle_new_game_session')

        # Verify it's an async method
        import inspect
        method = ConnectionManager.handle_new_game_session
        assert inspect.iscoroutinefunction(method)

        # Verify the method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        assert 'self' in params
        assert 'player_id' in params
        assert 'new_session_id' in params
