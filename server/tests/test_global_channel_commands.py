"""
Tests for global channel command functionality.

This module tests the global channel command parsing, validation, and integration
with the chat service and player management systems.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.communication_commands import handle_global_command
from server.game.chat_service import ChatService
from server.services.player_preferences_service import PlayerPreferencesService


def create_mock_player(player_id="player123", room_id="earth_arkhamcity_northside_intersection_derby_high"):
    """Create a properly configured mock player object."""
    mock_player = MagicMock()
    mock_player.id = player_id
    mock_player.current_room_id = room_id
    mock_player.player_id = player_id
    mock_player.level = 5  # Global channel requires level 1+
    return mock_player


class TestGlobalChannelCommandParsing:
    """Test global channel command parsing and validation."""

    @pytest.fixture
    def mock_services(self):
        """Create mock services for testing."""
        mock_chat_service = AsyncMock(spec=ChatService)
        mock_preferences_service = AsyncMock(spec=PlayerPreferencesService)
        return mock_chat_service, mock_preferences_service

    @pytest.fixture
    def mock_request(self):
        """Create mock request with app state."""
        mock_app = MagicMock()
        mock_app.state.chat_service = AsyncMock(spec=ChatService)
        mock_app.state.player_service = MagicMock()
        mock_app.state.player_preferences_service = AsyncMock(spec=PlayerPreferencesService)

        mock_request = MagicMock()
        mock_request.app = mock_app
        return mock_request

    @pytest.mark.asyncio
    async def test_global_command_parsing_valid_message(self, mock_services, mock_request):
        """Test parsing a valid global channel message."""
        mock_chat_service, mock_preferences_service = mock_services

        command_data = {
            "command_type": "global",
            "message": "Hello, investigators worldwide!",
            "args": ["Hello,", "investigators", "worldwide!"],
        }
        current_user = {"username": "testuser"}
        alias_storage = None
        player_name = "testuser"

        # Mock the player service to return a valid player
        mock_player = create_mock_player()
        mock_request.app.state.player_service.resolve_player_name = AsyncMock(return_value=mock_player)

        # Mock successful chat service call
        mock_request.app.state.chat_service.send_global_message = AsyncMock(
            return_value={
                "success": True,
                "message": {"id": "msg123", "content": "Hello, investigators worldwide!"},
            }
        )

        with patch("server.commands.communication_commands.get_username_from_user", return_value="testuser"):
            result = await handle_global_command(command_data, current_user, mock_request, alias_storage, player_name)

        # Verify the result
        assert result["result"] == "You say (global): Hello, investigators worldwide!"
        mock_request.app.state.chat_service.send_global_message.assert_called_once_with(
            "player123", "Hello, investigators worldwide!"
        )

    @pytest.mark.asyncio
    async def test_global_command_parsing_empty_message(self, mock_services, mock_request):
        """Test parsing a global channel command with no message."""
        command_data = {"command_type": "global", "message": "", "args": []}
        current_user = {"username": "testuser"}
        alias_storage = None
        player_name = "testuser"

        result = await handle_global_command(command_data, current_user, mock_request, alias_storage, player_name)

        assert result["result"] == "Say what? Usage: global <message> or /g <message>"

    @pytest.mark.asyncio
    async def test_global_command_parsing_whitespace_only(self, mock_services, mock_request):
        """Test parsing a global channel command with only whitespace."""
        command_data = {"command_type": "global", "message": "   ", "args": ["   "]}
        current_user = {"username": "testuser"}
        alias_storage = None
        player_name = "testuser"

        # Mock the player service to return a valid player
        mock_player = create_mock_player()
        mock_request.app.state.player_service.resolve_player_name = AsyncMock(return_value=mock_player)

        # Mock successful chat service call
        mock_request.app.state.chat_service.send_global_message = AsyncMock(
            return_value={
                "success": True,
                "message": {"id": "msg123", "content": "   "},
            }
        )

        result = await handle_global_command(command_data, current_user, mock_request, alias_storage, player_name)

        assert result["result"] == "Say what? Usage: global <message> or /g <message>"

    @pytest.mark.asyncio
    async def test_global_command_parsing_long_message(self, mock_services, mock_request):
        """Test parsing a long global channel message."""
        long_message = (
            "This is a very long message that should be handled properly by the global channel command parser. " * 5
        )

        command_data = {"command_type": "global", "message": long_message, "args": long_message.split()}
        current_user = {"username": "testuser"}
        alias_storage = None
        player_name = "testuser"

        # Mock the player service to return a valid player
        mock_player = create_mock_player()
        mock_request.app.state.player_service.resolve_player_name = AsyncMock(return_value=mock_player)

        # Mock successful chat service call
        mock_request.app.state.chat_service.send_global_message = AsyncMock(
            return_value={
                "success": True,
                "message": {"id": "msg123", "content": long_message},
            }
        )

        with patch("server.commands.communication_commands.get_username_from_user", return_value="testuser"):
            result = await handle_global_command(command_data, current_user, mock_request, alias_storage, player_name)

        assert result["result"] == f"You say (global): {long_message}"
        mock_request.app.state.chat_service.send_global_message.assert_called_once_with("player123", long_message)

    @pytest.mark.asyncio
    async def test_global_command_parsing_special_characters(self, mock_services, mock_request):
        """Test parsing global channel messages with special characters."""
        special_message = "Hello! @#$%^&*()_+-=[]{}|;':\",./<>?`~"

        command_data = {"command_type": "global", "message": special_message, "args": [special_message]}
        current_user = {"username": "testuser"}
        alias_storage = None
        player_name = "testuser"

        # Mock the player service to return a valid player
        mock_player = create_mock_player()
        mock_request.app.state.player_service.resolve_player_name = AsyncMock(return_value=mock_player)

        # Mock successful chat service call
        mock_request.app.state.chat_service.send_global_message = AsyncMock(
            return_value={
                "success": True,
                "message": {"id": "msg123", "content": special_message},
            }
        )

        with patch("server.commands.communication_commands.get_username_from_user", return_value="testuser"):
            result = await handle_global_command(command_data, current_user, mock_request, alias_storage, player_name)

        assert result["result"] == f"You say (global): {special_message}"
        mock_request.app.state.chat_service.send_global_message.assert_called_once_with("player123", special_message)


class TestGlobalChannelCommandIntegration:
    """Test global channel command integration with services."""

    @pytest.fixture
    def mock_request(self):
        """Create mock request with app state."""
        mock_app = MagicMock()
        mock_app.state.chat_service = AsyncMock(spec=ChatService)
        mock_app.state.player_service = MagicMock()
        mock_app.state.player_preferences_service = AsyncMock(spec=PlayerPreferencesService)

        mock_request = MagicMock()
        mock_request.app = mock_app
        return mock_request

    @pytest.mark.asyncio
    async def test_global_command_integration_player_not_found(self, mock_request):
        """Test global command when player is not found."""
        command_data = {"command_type": "global", "message": "Hello, world!", "args": ["Hello,", "world!"]}

        current_user = {"username": "testuser"}
        alias_storage = None
        player_name = "testuser"

        # Mock player service to return None (player not found)
        mock_request.app.state.player_service.resolve_player_name = AsyncMock(return_value=None)

        result = await handle_global_command(command_data, current_user, mock_request, alias_storage, player_name)

        assert result["result"] == "Player not found."
        mock_request.app.state.chat_service.send_global_message.assert_not_called()

    @pytest.mark.asyncio
    async def test_global_command_integration_no_player_id(self, mock_request):
        """Test global command when player has no ID."""
        command_data = {"command_type": "global", "message": "Hello, world!", "args": ["Hello,", "world!"]}
        current_user = {"username": "testuser"}
        alias_storage = None
        player_name = "testuser"

        # Mock player service to return player with no ID
        mock_player = MagicMock()
        mock_player.current_room_id = "earth_arkhamcity_northside_intersection_derby_high"
        mock_player.level = 5
        # Remove id and player_id attributes
        del mock_player.id
        del mock_player.player_id
        mock_request.app.state.player_service.resolve_player_name = AsyncMock(return_value=mock_player)

        result = await handle_global_command(command_data, current_user, mock_request, alias_storage, player_name)

        assert result["result"] == "Player ID not found."
        mock_request.app.state.chat_service.send_global_message.assert_not_called()

    @pytest.mark.asyncio
    async def test_global_command_integration_low_level_player(self, mock_request):
        """Test global command when player has insufficient level."""
        command_data = {"command_type": "global", "message": "Hello, world!", "args": ["Hello,", "world!"]}
        current_user = {"username": "testuser"}
        alias_storage = None
        player_name = "testuser"

        # Mock player service to return player with level 0 (below minimum)
        mock_player = MagicMock()
        mock_player.id = "player123"
        mock_player.current_room_id = "earth_arkhamcity_northside_intersection_derby_high"
        mock_player.level = 0  # Below minimum level 1
        mock_player.player_id = "player123"
        mock_request.app.state.player_service.resolve_player_name = AsyncMock(return_value=mock_player)

        result = await handle_global_command(command_data, current_user, mock_request, alias_storage, player_name)

        assert result["result"] == "You must be at least level 1 to use global chat."
        mock_request.app.state.chat_service.send_global_message.assert_not_called()

    @pytest.mark.asyncio
    async def test_global_command_integration_chat_service_error(self, mock_request):
        """Test global command when chat service returns an error."""
        command_data = {"command_type": "global", "message": "Hello, world!", "args": ["Hello,", "world!"]}
        current_user = {"username": "testuser"}
        alias_storage = None
        player_name = "testuser"

        # Mock the player service to return a valid player
        mock_player = create_mock_player()
        mock_request.app.state.player_service.resolve_player_name = AsyncMock(return_value=mock_player)

        # Mock chat service to return an error
        mock_request.app.state.chat_service.send_global_message = AsyncMock(
            return_value={
                "success": False,
                "error": "Rate limit exceeded",
            }
        )

        result = await handle_global_command(command_data, current_user, mock_request, alias_storage, player_name)

        assert result["result"] == "Error sending message: Rate limit exceeded"
        mock_request.app.state.chat_service.send_global_message.assert_called_once_with("player123", "Hello, world!")

    @pytest.mark.asyncio
    async def test_global_command_integration_chat_service_exception(self, mock_request):
        """Test global command when chat service raises an exception."""
        command_data = {"command_type": "global", "message": "Hello, world!", "args": ["Hello,", "world!"]}
        current_user = {"username": "testuser"}
        alias_storage = None
        player_name = "testuser"

        # Mock the player service to return a valid player
        mock_player = create_mock_player()
        mock_request.app.state.player_service.resolve_player_name = AsyncMock(return_value=mock_player)

        # Mock chat service to raise an exception
        mock_request.app.state.chat_service.send_global_message = AsyncMock(
            side_effect=Exception("Database connection failed")
        )

        result = await handle_global_command(command_data, current_user, mock_request, alias_storage, player_name)

        assert result["result"] == "Error sending message: Database connection failed"
        mock_request.app.state.chat_service.send_global_message.assert_called_once_with("player123", "Hello, world!")

    @pytest.mark.asyncio
    async def test_global_command_integration_no_chat_service(self, mock_request):
        """Test global command when chat service is not available."""
        command_data = {"command_type": "global", "message": "Hello, world!", "args": ["Hello,", "world!"]}
        current_user = {"username": "testuser"}
        alias_storage = None
        player_name = "testuser"

        # Configure mock to return None for chat_service
        mock_request.app.state.chat_service = None

        result = await handle_global_command(command_data, current_user, mock_request, alias_storage, player_name)

        assert result["result"] == "Chat functionality is not available."

    @pytest.mark.asyncio
    async def test_global_command_integration_no_player_service(self, mock_request):
        """Test global command when player service is not available."""
        command_data = {"command_type": "global", "message": "Hello, world!", "args": ["Hello,", "world!"]}
        current_user = {"username": "testuser"}
        alias_storage = None
        player_name = "testuser"

        # Configure mock to return None for player_service
        mock_request.app.state.player_service = None

        result = await handle_global_command(command_data, current_user, mock_request, alias_storage, player_name)

        assert result["result"] == "Chat functionality is not available."


class TestGlobalChannelCommandAliases:
    """Test global channel command aliases and shortcuts."""

    @pytest.fixture
    def mock_request(self):
        """Create mock request with app state."""
        mock_app = MagicMock()
        mock_app.state.chat_service = AsyncMock(spec=ChatService)
        mock_app.state.player_service = MagicMock()
        mock_app.state.player_preferences_service = AsyncMock(spec=PlayerPreferencesService)

        mock_request = MagicMock()
        mock_request.app = mock_app
        return mock_request

    @pytest.mark.asyncio
    async def test_global_command_alias_g(self, mock_request):
        """Test that /g command works as an alias for /global."""
        command_data = {"command_type": "g", "message": "Quick global message", "args": ["Quick", "global", "message"]}
        current_user = {"username": "testuser"}
        alias_storage = None
        player_name = "testuser"

        # Mock the player service to return a valid player
        mock_player = create_mock_player()
        mock_request.app.state.player_service.resolve_player_name = AsyncMock(return_value=mock_player)

        # Mock successful chat service call
        mock_request.app.state.chat_service.send_global_message = AsyncMock(
            return_value={
                "success": True,
                "message": {"id": "msg123", "content": "Quick global message"},
            }
        )

        with patch("server.commands.communication_commands.get_username_from_user", return_value="testuser"):
            result = await handle_global_command(command_data, current_user, mock_request, alias_storage, player_name)

        assert result["result"] == "You say (global): Quick global message"
        mock_request.app.state.chat_service.send_global_message.assert_called_once_with(
            "player123", "Quick global message"
        )

    @pytest.mark.asyncio
    async def test_global_command_alias_case_insensitive(self, mock_request):
        """Test that global command is case insensitive."""
        command_data = {
            "command_type": "GLOBAL",
            "message": "Case insensitive global message",
            "args": ["Case", "insensitive", "global", "message"],
        }
        current_user = {"username": "testuser"}
        alias_storage = None
        player_name = "testuser"

        # Mock the player service to return a valid player
        mock_player = create_mock_player()
        mock_request.app.state.player_service.resolve_player_name = AsyncMock(return_value=mock_player)

        # Mock successful chat service call
        mock_request.app.state.chat_service.send_global_message = AsyncMock(
            return_value={
                "success": True,
                "message": {"id": "msg123", "content": "Case insensitive global message"},
            }
        )

        with patch("server.commands.communication_commands.get_username_from_user", return_value="testuser"):
            result = await handle_global_command(command_data, current_user, mock_request, alias_storage, player_name)

        assert result["result"] == "You say (global): Case insensitive global message"
        mock_request.app.state.chat_service.send_global_message.assert_called_once_with(
            "player123", "Case insensitive global message"
        )
