"""
Tests for local channel functionality.

This module tests the local channel implementation for the Advanced Chat Channels feature.
"""

from datetime import datetime
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.communication_commands import handle_local_command
from server.game.chat_service import ChatMessage, ChatService
from server.services.player_preferences_service import PlayerPreferencesService


class TestLocalChannelMessage:
    """Test local channel message creation and formatting."""

    def test_local_channel_message_creation(self):
        """Test creating a local channel message."""
        message = ChatMessage(
            sender_id="test-player-123", sender_name="TestPlayer", channel="local", content="Hello, local area!"
        )

        assert message.sender_id == "test-player-123"
        assert message.sender_name == "TestPlayer"
        assert message.channel == "local"
        assert message.content == "Hello, local area!"
        assert message.id is not None
        assert isinstance(message.timestamp, datetime)

    def test_local_channel_message_to_dict(self):
        """Test converting local channel message to dictionary."""
        message = ChatMessage(
            sender_id="test-player-123", sender_name="TestPlayer", channel="local", content="Hello, local area!"
        )

        message_dict = message.to_dict()

        assert message_dict["sender_id"] == "test-player-123"
        assert message_dict["sender_name"] == "TestPlayer"
        assert message_dict["channel"] == "local"
        assert message_dict["content"] == "Hello, local area!"
        assert "timestamp" in message_dict
        assert "id" in message_dict

    def test_local_channel_message_logging(self):
        """Test that local channel messages are logged correctly."""
        with patch("server.game.chat_service.logger") as mock_logger:
            message = ChatMessage(
                sender_id="test-player-123", sender_name="TestPlayer", channel="local", content="Hello, local area!"
            )

            message.log_message()

            mock_logger.info.assert_called_once()
            call_args = mock_logger.info.call_args
            assert call_args[0][0] == "CHAT MESSAGE"
            assert call_args[1]["channel"] == "local"
            assert call_args[1]["sender_name"] == "TestPlayer"


class TestLocalChannelService:
    """Test local channel service functionality."""

    @pytest.fixture
    def mock_persistence(self):
        """Create a mock persistence layer."""
        return MagicMock()

    @pytest.fixture
    def mock_room_service(self):
        """Create a mock room service."""
        return MagicMock()

    @pytest.fixture
    def mock_player_service(self):
        """Create a mock player service."""
        return AsyncMock()

    @pytest.fixture
    def mock_nats_service(self):
        """Create a mock NATS service."""
        mock_service = MagicMock()
        mock_service.is_connected.return_value = True
        mock_service.publish = AsyncMock(return_value=True)
        return mock_service

    @pytest.fixture
    def mock_chat_logger(self):
        """Create a mock chat logger."""
        return MagicMock()

    @pytest.fixture
    def mock_rate_limiter(self):
        """Create a mock rate limiter."""
        mock_limiter = MagicMock()
        mock_limiter.check_rate_limit.return_value = True
        mock_limiter.record_message = MagicMock()
        return mock_limiter

    @pytest.fixture
    def mock_user_manager(self):
        """Create a mock user manager."""
        mock_manager = MagicMock()
        mock_manager.load_player_mutes = MagicMock()
        mock_manager.is_channel_muted.return_value = False
        mock_manager.is_globally_muted.return_value = False
        mock_manager.can_send_message.return_value = True
        return mock_manager

    @pytest.fixture
    def chat_service(
        self,
        mock_persistence,
        mock_room_service,
        mock_player_service,
        mock_nats_service,
        mock_chat_logger,
        mock_rate_limiter,
        mock_user_manager,
    ):
        """Create a ChatService instance with mocked dependencies."""
        with (
            patch("server.services.nats_service.nats_service", mock_nats_service),
            patch("server.game.chat_service.chat_logger", mock_chat_logger),
            patch("server.game.chat_service.rate_limiter", mock_rate_limiter),
            patch("server.game.chat_service.user_manager", mock_user_manager),
        ):
            service = ChatService(mock_persistence, mock_room_service, mock_player_service)
            return service

    @pytest.fixture
    def mock_player(self):
        """Create a mock player object."""
        player = MagicMock()
        player.player_id = "test-player-123"
        player.name = "TestPlayer"
        player.current_room_id = "earth_arkhamcity_northside_intersection_derby_high"
        player.level = 1
        return player

    @pytest.mark.asyncio
    async def test_send_local_message_success(self, chat_service, mock_player_service, mock_player):
        """Test successful local message sending."""
        # Setup
        mock_player_service.get_player_by_id.return_value = mock_player

        # Execute
        result = await chat_service.send_local_message("test-player-123", "Hello, local area!")

        # Verify
        assert result["success"] is True
        assert result["message"]["channel"] == "local"
        assert result["message"]["content"] == "Hello, local area!"
        assert result["message"]["sender_name"] == "TestPlayer"
        assert "room_id" in result

    @pytest.mark.asyncio
    async def test_send_local_message_empty_content(self, chat_service):
        """Test local message with empty content."""
        result = await chat_service.send_local_message("test-player-123", "")

        assert result["success"] is False
        assert "empty" in result["error"].lower()

    @pytest.mark.asyncio
    async def test_send_local_message_too_long(self, chat_service):
        """Test local message with content too long."""
        long_message = "x" * 501
        result = await chat_service.send_local_message("test-player-123", long_message)

        assert result["success"] is False
        assert "too long" in result["error"].lower()

    @pytest.mark.asyncio
    async def test_send_local_message_player_not_found(self, chat_service, mock_player_service):
        """Test local message with non-existent player."""
        mock_player_service.get_player_by_id.return_value = None

        result = await chat_service.send_local_message("non-existent", "Hello!")

        assert result["success"] is False
        assert "not found" in result["error"].lower()

    @pytest.mark.asyncio
    async def test_send_local_message_player_not_in_room(self, chat_service, mock_player_service, mock_player):
        """Test local message when player is not in a room."""
        mock_player.current_room_id = None
        mock_player_service.get_player_by_id.return_value = mock_player

        result = await chat_service.send_local_message("test-player-123", "Hello!")

        assert result["success"] is False
        assert "not in a room" in result["error"].lower()

    @pytest.mark.asyncio
    async def test_send_local_message_rate_limited(
        self, chat_service, mock_player_service, mock_player, mock_rate_limiter
    ):
        """Test local message when rate limited."""
        mock_player_service.get_player_by_id.return_value = mock_player
        mock_rate_limiter.check_rate_limit.return_value = False

        result = await chat_service.send_local_message("test-player-123", "Hello!")

        assert result["success"] is False
        assert "rate limit" in result["error"].lower()
        assert result["rate_limited"] is True

    @pytest.mark.asyncio
    async def test_send_local_message_channel_muted(
        self, chat_service, mock_player_service, mock_player, mock_user_manager
    ):
        """Test local message when player is muted in local channel."""
        mock_player_service.get_player_by_id.return_value = mock_player
        mock_user_manager.is_channel_muted.return_value = True

        result = await chat_service.send_local_message("test-player-123", "Hello!")

        assert result["success"] is False
        assert "muted" in result["error"].lower()

    @pytest.mark.asyncio
    async def test_send_local_message_globally_muted(
        self, chat_service, mock_player_service, mock_player, mock_user_manager
    ):
        """Test local message when player is globally muted."""
        mock_player_service.get_player_by_id.return_value = mock_player
        mock_user_manager.is_globally_muted.return_value = True

        result = await chat_service.send_local_message("test-player-123", "Hello!")

        assert result["success"] is False
        assert "globally muted" in result["error"].lower()

    @pytest.mark.asyncio
    async def test_send_local_message_cannot_send(
        self, chat_service, mock_player_service, mock_player, mock_user_manager
    ):
        """Test local message when player cannot send messages."""
        mock_player_service.get_player_by_id.return_value = mock_player
        mock_user_manager.can_send_message.return_value = False

        result = await chat_service.send_local_message("test-player-123", "Hello!")

        assert result["success"] is False
        assert "cannot send" in result["error"].lower()

    @pytest.mark.asyncio
    async def test_send_local_message_nats_failure(
        self, chat_service, mock_player_service, mock_player, mock_nats_service
    ):
        """Test local message when NATS publishing fails."""
        mock_player_service.get_player_by_id.return_value = mock_player
        mock_nats_service.publish.return_value = False

        result = await chat_service.send_local_message("test-player-123", "Hello!")

        assert result["success"] is False
        assert "unavailable" in result["error"].lower()

    @pytest.mark.asyncio
    async def test_send_local_message_nats_not_connected(
        self, chat_service, mock_player_service, mock_player, mock_nats_service
    ):
        """Test local message when NATS is not connected."""
        mock_player_service.get_player_by_id.return_value = mock_player
        mock_nats_service.is_connected.return_value = False

        result = await chat_service.send_local_message("test-player-123", "Hello!")

        assert result["success"] is False
        assert "unavailable" in result["error"].lower()

    @pytest.mark.asyncio
    async def test_send_local_message_logging_and_rate_limiting(
        self, chat_service, mock_player_service, mock_player, mock_chat_logger, mock_rate_limiter
    ):
        """Test that local messages are logged and rate limited correctly."""
        mock_player_service.get_player_by_id.return_value = mock_player

        await chat_service.send_local_message("test-player-123", "Hello, local area!")

        # Verify logging
        mock_chat_logger.log_chat_message.assert_called_once()
        log_call = mock_chat_logger.log_chat_message.call_args[0][0]
        assert log_call["channel"] == "local"
        assert log_call["sender_name"] == "TestPlayer"
        assert log_call["content"] == "Hello, local area!"

        # Verify rate limiting
        mock_rate_limiter.record_message.assert_called_once_with("test-player-123", "local", "TestPlayer")

    @pytest.mark.asyncio
    async def test_send_local_message_room_history(self, chat_service, mock_player_service, mock_player):
        """Test that local messages are stored in room history."""
        mock_player_service.get_player_by_id.return_value = mock_player

        await chat_service.send_local_message("test-player-123", "Hello, local area!")

        # Verify message is stored in room history
        room_id = mock_player.current_room_id
        assert room_id in chat_service._room_messages
        assert len(chat_service._room_messages[room_id]) == 1
        assert chat_service._room_messages[room_id][0].channel == "local"
        assert chat_service._room_messages[room_id][0].content == "Hello, local area!"

    @pytest.mark.asyncio
    async def test_send_local_message_nats_subject(
        self, chat_service, mock_player_service, mock_player, mock_nats_service
    ):
        """Test that local messages use correct NATS subject."""
        mock_player_service.get_player_by_id.return_value = mock_player

        await chat_service.send_local_message("test-player-123", "Hello, local area!")

        # Verify NATS subject
        mock_nats_service.publish.assert_called_once()
        call_args = mock_nats_service.publish.call_args
        subject = call_args[0][0]
        # Local channel uses sub-zone based subjects, not full room ID
        assert subject == "chat.local.subzone.northside"


class TestLocalChannelSubZoneExtraction:
    """Test sub-zone extraction for local channel functionality."""

    def test_extract_subzone_from_room_id(self):
        """Test extracting sub-zone from room ID."""
        room_id = "earth_arkhamcity_northside_intersection_derby_high"
        subzone = self._extract_subzone(room_id)
        assert subzone == "northside"

    def test_extract_subzone_from_different_room(self):
        """Test extracting sub-zone from different room ID."""
        room_id = "earth_arkhamcity_downtown_market_square"
        subzone = self._extract_subzone(room_id)
        assert subzone == "downtown"

    def test_extract_subzone_from_campus_room(self):
        """Test extracting sub-zone from campus room."""
        room_id = "earth_arkhamcity_campus_library_main"
        subzone = self._extract_subzone(room_id)
        assert subzone == "campus"

    def test_extract_subzone_invalid_format(self):
        """Test extracting sub-zone from invalid room ID format."""
        room_id = "invalid_room_id"
        subzone = self._extract_subzone(room_id)
        assert subzone is None

    def test_extract_subzone_empty_string(self):
        """Test extracting sub-zone from empty string."""
        room_id = ""
        subzone = self._extract_subzone(room_id)
        assert subzone is None

    def test_extract_subzone_none(self):
        """Test extracting sub-zone from None."""
        room_id = None
        subzone = self._extract_subzone(room_id)
        assert subzone is None

    def _extract_subzone(self, room_id: str) -> str | None:
        """
        Extract sub-zone from room ID.

        Room ID format: {plane}_{zone}_{sub_zone}_{room_name}
        Example: earth_arkhamcity_northside_intersection_derby_high
        """
        if not room_id:
            return None

        parts = room_id.split("_")
        if len(parts) < 4:
            return None

        # The sub-zone is the third part (index 2) for arkhamcity format
        # Format: earth_arkhamcity_northside_intersection_derby_high
        # Parts: [0]earth [1]arkhamcity [2]northside [3]intersection [4]derby [5]high
        return parts[2]


class TestLocalChannelIntegration:
    """Integration tests for local channel functionality."""

    @pytest.fixture
    def mock_persistence(self):
        """Create a mock persistence layer."""
        return MagicMock()

    @pytest.fixture
    def mock_room_service(self):
        """Create a mock room service."""
        return MagicMock()

    @pytest.fixture
    def mock_player_service(self):
        """Create a mock player service."""
        return AsyncMock()

    @pytest.fixture
    def mock_nats_service(self):
        """Create a mock NATS service."""
        mock_service = MagicMock()
        mock_service.is_connected.return_value = True
        mock_service.publish = AsyncMock(return_value=True)
        return mock_service

    @pytest.fixture
    def mock_chat_logger(self):
        """Create a mock chat logger."""
        return MagicMock()

    @pytest.fixture
    def mock_rate_limiter(self):
        """Create a mock rate limiter."""
        mock_limiter = MagicMock()
        mock_limiter.check_rate_limit.return_value = True
        mock_limiter.record_message = MagicMock()
        return mock_limiter

    @pytest.fixture
    def mock_user_manager(self):
        """Create a mock user manager."""
        mock_manager = MagicMock()
        mock_manager.load_player_mutes = MagicMock()
        mock_manager.is_channel_muted.return_value = False
        mock_manager.is_globally_muted.return_value = False
        mock_manager.can_send_message.return_value = True
        return mock_manager

    @pytest.fixture
    def chat_service(
        self,
        mock_persistence,
        mock_room_service,
        mock_player_service,
        mock_nats_service,
        mock_chat_logger,
        mock_rate_limiter,
        mock_user_manager,
    ):
        """Create a ChatService instance with mocked dependencies."""
        with (
            patch("server.services.nats_service.nats_service", mock_nats_service),
            patch("server.game.chat_service.chat_logger", mock_chat_logger),
            patch("server.game.chat_service.rate_limiter", mock_rate_limiter),
            patch("server.game.chat_service.user_manager", mock_user_manager),
        ):
            service = ChatService(mock_persistence, mock_room_service, mock_player_service)
            return service

    @pytest.mark.asyncio
    async def test_local_channel_with_preferences(self, chat_service, mock_player_service):
        """Test local channel with player preferences."""
        # Create mock player
        player = MagicMock()
        player.player_id = "test-player-123"
        player.name = "TestPlayer"
        player.current_room_id = "earth_arkhamcity_northside_intersection_derby_high"
        player.level = 1
        mock_player_service.get_player_by_id.return_value = player

        # Test local message
        result = await chat_service.send_local_message("test-player-123", "Hello, northside!")

        assert result["success"] is True
        assert result["message"]["channel"] == "local"
        assert result["message"]["content"] == "Hello, northside!"

    @pytest.mark.asyncio
    async def test_local_channel_different_subzones(self, chat_service, mock_player_service):
        """Test local channel with different sub-zones."""
        # Test northside
        player1 = MagicMock()
        player1.player_id = "player1"
        player1.name = "Player1"
        player1.current_room_id = "earth_arkhamcity_northside_room_high_ln_001"
        player1.level = 1

        # Test downtown
        player2 = MagicMock()
        player2.player_id = "player2"
        player2.name = "Player2"
        player2.current_room_id = "earth_arkhamcity_downtown_market_square"
        player2.level = 1

        # Send messages from different sub-zones
        mock_player_service.get_player_by_id.side_effect = [player1, player2]

        result1 = await chat_service.send_local_message("player1", "Hello from northside!")
        result2 = await chat_service.send_local_message("player2", "Hello from downtown!")

        assert result1["success"] is True
        assert result2["success"] is True

        # Verify different NATS subjects for different sub-zones
        nats_calls = chat_service.nats_service.publish.call_args_list
        assert len(nats_calls) == 2
        assert "northside" in nats_calls[0][0][0]  # First call subject
        assert "downtown" in nats_calls[1][0][0]  # Second call subject


# ============================================================================
# Tests merged from test_local_channel_commands_legacy.py
# ============================================================================


"""
Tests for local channel command parsing and handling.

This module tests the local channel command functionality including
command parsing, validation, and integration with the command processor.
"""


def create_mock_player(player_id="player123", room_id="earth_arkhamcity_northside_intersection_derby_high"):
    """Create a properly configured mock player object."""
    mock_player = MagicMock()
    mock_player.id = player_id
    mock_player.current_room_id = room_id
    mock_player.player_id = player_id
    return mock_player


class TestLocalChannelCommandParsing:
    """Test local channel command parsing and validation."""

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
    async def test_local_command_parsing_valid_message(self, mock_services, mock_request):
        """Test parsing a valid local channel message."""
        mock_chat_service, mock_preferences_service = mock_services

        command_data = {
            "command_type": "local",
            "message": "Hello, fellow investigators!",
            "args": ["Hello,", "fellow", "investigators!"],
        }
        current_user = {"username": "testuser"}
        alias_storage = None
        player_name = "testuser"

        # Mock the player service to return a valid player
        mock_player = create_mock_player()
        mock_request.app.state.player_service.resolve_player_name = AsyncMock(return_value=mock_player)

        # Mock successful chat service call
        mock_request.app.state.chat_service.send_local_message = AsyncMock(
            return_value={
                "success": True,
                "message": {"id": "msg123", "content": "Hello, fellow investigators!"},
            }
        )

        with patch("server.commands.communication_commands.get_username_from_user", return_value="testuser"):
            result = await handle_local_command(command_data, current_user, mock_request, alias_storage, player_name)

        # Verify the result
        assert result["result"] == "You say locally: Hello, fellow investigators!"
        mock_request.app.state.chat_service.send_local_message.assert_called_once_with(
            "player123", "Hello, fellow investigators!"
        )

    @pytest.mark.asyncio
    async def test_local_command_parsing_empty_message(self, mock_services, mock_request):
        """Test parsing a local channel command with no message."""
        command_data = {"command_type": "local", "message": "", "args": []}
        current_user = {"username": "testuser"}
        alias_storage = None
        player_name = "testuser"

        result = await handle_local_command(command_data, current_user, mock_request, alias_storage, player_name)

        assert result["result"] == "Say what? Usage: local <message> or /l <message>"

    @pytest.mark.asyncio
    async def test_local_command_parsing_whitespace_only(self, mock_services, mock_request):
        """Test parsing a local channel command with only whitespace."""
        command_data = {"command_type": "local", "message": "   ", "args": ["   "]}
        current_user = {"username": "testuser"}
        alias_storage = None
        player_name = "testuser"

        # Mock the player service to return a valid player
        mock_player = create_mock_player()
        mock_request.app.state.player_service.resolve_player_name = AsyncMock(return_value=mock_player)

        # Mock successful chat service call
        mock_request.app.state.chat_service.send_local_message = AsyncMock(
            return_value={
                "success": True,
                "message": {"id": "msg123", "content": "   "},
            }
        )

        result = await handle_local_command(command_data, current_user, mock_request, alias_storage, player_name)

        assert result["result"] == "Say what? Usage: local <message> or /l <message>"

    @pytest.mark.asyncio
    async def test_local_command_parsing_long_message(self, mock_services, mock_request):
        """Test parsing a long local channel message."""
        long_message = (
            "This is a very long message that should be handled properly by the local channel command parser. " * 5
        )

        command_data = {"command_type": "local", "message": long_message, "args": long_message.split()}
        current_user = {"username": "testuser"}
        alias_storage = None
        player_name = "testuser"

        # Mock the player service to return a valid player
        mock_player = create_mock_player()
        mock_request.app.state.player_service.resolve_player_name = AsyncMock(return_value=mock_player)

        # Mock successful chat service call
        mock_request.app.state.chat_service.send_local_message = AsyncMock(
            return_value={
                "success": True,
                "message": {"id": "msg123", "content": long_message},
            }
        )

        with patch("server.commands.communication_commands.get_username_from_user", return_value="testuser"):
            result = await handle_local_command(command_data, current_user, mock_request, alias_storage, player_name)

        assert result["result"] == f"You say locally: {long_message}"
        mock_request.app.state.chat_service.send_local_message.assert_called_once_with("player123", long_message)

    @pytest.mark.asyncio
    async def test_local_command_parsing_special_characters(self, mock_services, mock_request):
        """Test parsing local channel messages with special characters."""
        # Special characters allowed in messages (excluding HTML tags and command separators)
        special_message = "Hello! @#$%^&*()_+-=[]{}':\",.?`~"  # Removed <, >, ;, | as they're still blocked

        command_data = {"command_type": "local", "message": special_message, "args": [special_message]}
        current_user = {"username": "testuser"}
        alias_storage = None
        player_name = "testuser"

        # Mock the player service to return a valid player
        mock_player = create_mock_player()
        mock_request.app.state.player_service.resolve_player_name = AsyncMock(return_value=mock_player)

        # Mock successful chat service call
        mock_request.app.state.chat_service.send_local_message = AsyncMock(
            return_value={
                "success": True,
                "message": {"id": "msg123", "content": special_message},
            }
        )

        with patch("server.commands.communication_commands.get_username_from_user", return_value="testuser"):
            result = await handle_local_command(command_data, current_user, mock_request, alias_storage, player_name)

        assert result["result"] == f"You say locally: {special_message}"
        mock_request.app.state.chat_service.send_local_message.assert_called_once_with("player123", special_message)


class TestLocalChannelCommandIntegration:
    """Test local channel command integration with command processor."""

    @pytest.fixture
    def mock_request(self):
        """Create mock request with app state."""
        mock_app = MagicMock()
        mock_app.state.chat_service = AsyncMock(spec=ChatService)
        mock_app.state.player_service = AsyncMock()
        mock_app.state.player_preferences_service = AsyncMock(spec=PlayerPreferencesService)

        mock_request = MagicMock()
        mock_request.app = mock_app
        return mock_request

    @pytest.mark.asyncio
    async def test_local_command_integration_player_not_found(self, mock_request):
        """Test local command when player is not found."""
        command_data = {"command_type": "local", "message": "Hello, world!", "args": ["Hello,", "world!"]}
        current_user = {"username": "testuser"}
        alias_storage = None
        player_name = "testuser"

        # Mock player service to return None (player not found)
        mock_request.app.state.player_service.resolve_player_name = AsyncMock(return_value=None)

        result = await handle_local_command(command_data, current_user, mock_request, alias_storage, player_name)

        assert result["result"] == "Player not found."
        mock_request.app.state.chat_service.send_local_message.assert_not_called()

    @pytest.mark.asyncio
    async def test_local_command_integration_no_room(self, mock_request):
        """Test local command when player has no current room."""
        command_data = {"command_type": "local", "message": "Hello, world!", "args": ["Hello,", "world!"]}
        current_user = {"username": "testuser"}
        alias_storage = None
        player_name = "testuser"

        # Mock player service to return player with no room
        mock_player = MagicMock()
        mock_player.id = "player123"
        mock_player.current_room_id = None
        mock_request.app.state.player_service.resolve_player_name = AsyncMock(return_value=mock_player)

        result = await handle_local_command(command_data, current_user, mock_request, alias_storage, player_name)

        assert result["result"] == "You are not in a room."
        mock_request.app.state.chat_service.send_local_message.assert_not_called()

    @pytest.mark.asyncio
    async def test_local_command_integration_no_player_id(self, mock_request):
        """Test local command when player has no ID."""
        command_data = {"command_type": "local", "message": "Hello, world!", "args": ["Hello,", "world!"]}
        current_user = {"username": "testuser"}
        alias_storage = None
        player_name = "testuser"

        # Mock player service to return player with no ID
        mock_player = MagicMock()
        mock_player.current_room_id = "earth_arkhamcity_northside_intersection_derby_high"
        # Remove id and player_id attributes
        del mock_player.id
        del mock_player.player_id
        mock_request.app.state.player_service.resolve_player_name = AsyncMock(return_value=mock_player)

        result = await handle_local_command(command_data, current_user, mock_request, alias_storage, player_name)

        assert result["result"] == "Player ID not found."
        mock_request.app.state.chat_service.send_local_message.assert_not_called()

    @pytest.mark.asyncio
    async def test_local_command_integration_chat_service_error(self, mock_request):
        """Test local command when chat service returns an error."""
        command_data = {"command_type": "local", "message": "Hello, world!", "args": ["Hello,", "world!"]}
        current_user = {"username": "testuser"}
        alias_storage = None
        player_name = "testuser"

        # Mock the player service to return a valid player
        mock_player = create_mock_player()
        mock_request.app.state.player_service.resolve_player_name = AsyncMock(return_value=mock_player)

        # Mock chat service to return an error
        mock_request.app.state.chat_service.send_local_message = AsyncMock(
            return_value={
                "success": False,
                "error": "Rate limit exceeded",
            }
        )

        result = await handle_local_command(command_data, current_user, mock_request, alias_storage, player_name)

        assert result["result"] == "Error sending message: Rate limit exceeded"
        mock_request.app.state.chat_service.send_local_message.assert_called_once_with("player123", "Hello, world!")

    @pytest.mark.asyncio
    async def test_local_command_integration_chat_service_exception(self, mock_request):
        """Test local command when chat service raises an exception."""
        command_data = {"command_type": "local", "message": "Hello, world!", "args": ["Hello,", "world!"]}
        current_user = {"username": "testuser"}
        alias_storage = None
        player_name = "testuser"

        # Mock the player service to return a valid player
        mock_player = create_mock_player()
        mock_request.app.state.player_service.resolve_player_name = AsyncMock(return_value=mock_player)

        # Mock chat service to raise an exception
        mock_request.app.state.chat_service.send_local_message = AsyncMock(
            side_effect=Exception("Database connection failed")
        )

        result = await handle_local_command(command_data, current_user, mock_request, alias_storage, player_name)

        assert result["result"] == "Error sending message: Database connection failed"
        mock_request.app.state.chat_service.send_local_message.assert_called_once_with("player123", "Hello, world!")

    @pytest.mark.asyncio
    async def test_local_command_integration_no_chat_service(self, mock_request):
        """Test local command when chat service is not available."""
        command_data = {"command_type": "local", "message": "Hello, world!", "args": ["Hello,", "world!"]}
        current_user = {"username": "testuser"}
        alias_storage = None
        player_name = "testuser"

        # Configure mock to return None for chat_service
        mock_request.app.state.chat_service = None

        result = await handle_local_command(command_data, current_user, mock_request, alias_storage, player_name)

        assert result["result"] == "Chat functionality is not available."

    @pytest.mark.asyncio
    async def test_local_command_integration_no_player_service(self, mock_request):
        """Test local command when player service is not available."""
        command_data = {"command_type": "local", "message": "Hello, world!", "args": ["Hello,", "world!"]}
        current_user = {"username": "testuser"}
        alias_storage = None
        player_name = "testuser"

        # Configure mock to return None for player_service
        mock_request.app.state.player_service = None

        result = await handle_local_command(command_data, current_user, mock_request, alias_storage, player_name)

        assert result["result"] == "Chat functionality is not available."


class TestLocalChannelCommandAliases:
    """Test local channel command aliases and shortcuts."""

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
    async def test_local_command_alias_l(self, mock_request):
        """Test that /l command works as an alias for /local."""
        command_data = {"command_type": "l", "message": "Quick message", "args": ["Quick", "message"]}
        current_user = {"username": "testuser"}
        alias_storage = None
        player_name = "testuser"

        # Mock the player service to return a valid player
        mock_player = create_mock_player()
        mock_request.app.state.player_service.resolve_player_name = AsyncMock(return_value=mock_player)

        # Mock successful chat service call
        mock_request.app.state.chat_service.send_local_message = AsyncMock(
            return_value={
                "success": True,
                "message": {"id": "msg123", "content": "Quick message"},
            }
        )

        with patch("server.commands.communication_commands.get_username_from_user", return_value="testuser"):
            result = await handle_local_command(command_data, current_user, mock_request, alias_storage, player_name)

        assert result["result"] == "You say locally: Quick message"
        mock_request.app.state.chat_service.send_local_message.assert_called_once_with("player123", "Quick message")

    @pytest.mark.asyncio
    async def test_local_command_alias_case_insensitive(self, mock_request):
        """Test that local command is case insensitive."""
        command_data = {
            "command_type": "LOCAL",
            "message": "Case insensitive message",
            "args": ["Case", "insensitive", "message"],
        }
        current_user = {"username": "testuser"}
        alias_storage = None
        player_name = "testuser"

        # Mock the player service to return a valid player
        mock_player = create_mock_player()
        mock_request.app.state.player_service.resolve_player_name = AsyncMock(return_value=mock_player)

        # Mock successful chat service call
        mock_request.app.state.chat_service.send_local_message = AsyncMock(
            return_value={
                "success": True,
                "message": {"id": "msg123", "content": "Case insensitive message"},
            }
        )

        with patch("server.commands.communication_commands.get_username_from_user", return_value="testuser"):
            result = await handle_local_command(command_data, current_user, mock_request, alias_storage, player_name)

        assert result["result"] == "You say locally: Case insensitive message"
        mock_request.app.state.chat_service.send_local_message.assert_called_once_with(
            "player123", "Case insensitive message"
        )
