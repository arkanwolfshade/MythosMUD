"""
Tests for the chat service module.

This module tests the ChatService class which handles all chat functionality
including message handling, channel management, and real-time communication.
"""

import uuid
from datetime import UTC, datetime
from unittest.mock import AsyncMock, Mock

import pytest

from ..game.chat_service import ChatMessage, ChatService


class TestChatMessage:
    """Test cases for ChatMessage class."""

    def test_chat_message_creation(self):
        """Test ChatMessage creation with all required fields."""
        sender_id = str(uuid.uuid4())
        sender_name = "TestPlayer"
        channel = "say"
        content = "Hello, world!"

        message = ChatMessage(sender_id, sender_name, channel, content)

        assert message.sender_id == sender_id
        assert message.sender_name == sender_name
        assert message.channel == channel
        assert message.content == content
        assert isinstance(message.id, str)
        assert isinstance(message.timestamp, datetime)
        assert message.timestamp.tzinfo == UTC

    def test_chat_message_to_dict(self):
        """Test ChatMessage serialization to dictionary."""
        sender_id = str(uuid.uuid4())
        sender_name = "TestPlayer"
        channel = "say"
        content = "Hello, world!"

        message = ChatMessage(sender_id, sender_name, channel, content)
        message_dict = message.to_dict()

        assert message_dict["sender_id"] == sender_id
        assert message_dict["sender_name"] == sender_name
        assert message_dict["channel"] == channel
        assert message_dict["content"] == content
        assert message_dict["id"] == message.id
        assert "timestamp" in message_dict
        assert isinstance(message_dict["timestamp"], str)

    def test_chat_message_log_message(self):
        """Test ChatMessage logging functionality."""
        sender_id = str(uuid.uuid4())
        sender_name = "TestPlayer"
        channel = "say"
        content = "Hello, world!"

        message = ChatMessage(sender_id, sender_name, channel, content)

        # This should not raise any exceptions
        message.log_message()


class TestChatService:
    """Test cases for ChatService class."""

    def setup_method(self):
        """Set up test fixtures."""
        # Create mock dependencies
        self.mock_persistence = Mock()
        self.mock_room_service = Mock()
        self.mock_player_service = Mock()

        # Create mock services
        self.mock_nats_service = Mock()
        self.mock_chat_logger = Mock()
        self.mock_rate_limiter = Mock()
        self.mock_user_manager = Mock()

        # Create the service instance
        self.chat_service = ChatService(self.mock_persistence, self.mock_room_service, self.mock_player_service)

        # Replace service dependencies with mocks
        self.chat_service.nats_service = self.mock_nats_service
        self.chat_service.chat_logger = self.mock_chat_logger
        self.chat_service.rate_limiter = self.mock_rate_limiter
        self.chat_service.user_manager = self.mock_user_manager

        # Create a mock player for testing
        self.mock_player = Mock()
        self.mock_player.id = str(uuid.uuid4())
        self.mock_player.name = "TestPlayer"
        self.mock_player.current_room_id = "room_001"

    def test_chat_service_initialization(self):
        """Test ChatService initialization."""
        assert self.chat_service.persistence == self.mock_persistence
        assert self.chat_service.room_service == self.mock_room_service
        assert self.chat_service.player_service == self.mock_player_service
        assert self.chat_service._room_messages == {}
        assert self.chat_service._max_messages_per_room == 100

    @pytest.mark.asyncio
    async def test_send_say_message_success(self):
        """Test successful say message sending."""
        # Setup
        player_id = str(uuid.uuid4())
        message = "Hello, world!"

        self.mock_player_service.get_player_by_id.return_value = self.mock_player
        self.mock_rate_limiter.check_rate_limit.return_value = True
        self.mock_user_manager.is_channel_muted.return_value = False
        self.mock_user_manager.is_globally_muted.return_value = False
        self.mock_user_manager.can_send_message.return_value = True
        self.mock_nats_service.is_connected.return_value = True
        self.mock_nats_service.publish = AsyncMock(return_value=True)

        # Execute
        result = await self.chat_service.send_say_message(player_id, message)

        # Verify
        assert result["success"] is True
        assert "message" in result
        assert result["room_id"] == "room_001"

        # Verify service calls
        self.mock_player_service.get_player_by_id.assert_called_once_with(player_id)
        self.mock_rate_limiter.check_rate_limit.assert_called_once_with(player_id, "say", "TestPlayer")
        self.mock_user_manager.load_player_mutes.assert_called_once_with(player_id)
        self.mock_chat_logger.log_chat_message.assert_called_once()
        self.mock_rate_limiter.record_message.assert_called_once_with(player_id, "say", "TestPlayer")

    @pytest.mark.asyncio
    async def test_send_say_message_empty_message(self):
        """Test say message with empty content."""
        # Setup
        player_id = str(uuid.uuid4())
        message = ""

        # Execute
        result = await self.chat_service.send_say_message(player_id, message)

        # Verify
        assert result["success"] is False
        assert result["error"] == "Message cannot be empty"

        # Verify no service calls were made
        self.mock_player_service.get_player_by_id.assert_not_called()

    @pytest.mark.asyncio
    async def test_send_say_message_whitespace_only(self):
        """Test say message with whitespace-only content."""
        # Setup
        player_id = str(uuid.uuid4())
        message = "   \n\t   "

        # Execute
        result = await self.chat_service.send_say_message(player_id, message)

        # Verify
        assert result["success"] is False
        assert result["error"] == "Message cannot be empty"

    @pytest.mark.asyncio
    async def test_send_say_message_too_long(self):
        """Test say message with content exceeding length limit."""
        # Setup
        player_id = str(uuid.uuid4())
        message = "x" * 501  # Exceeds 500 character limit

        # Execute
        result = await self.chat_service.send_say_message(player_id, message)

        # Verify
        assert result["success"] is False
        assert result["error"] == "Message too long (max 500 characters)"

    @pytest.mark.asyncio
    async def test_send_say_message_player_not_found(self):
        """Test say message when player is not found."""
        # Setup
        player_id = str(uuid.uuid4())
        message = "Hello, world!"

        self.mock_player_service.get_player_by_id.return_value = None

        # Execute
        result = await self.chat_service.send_say_message(player_id, message)

        # Verify
        assert result["success"] is False
        assert result["error"] == "Player not found"

    @pytest.mark.asyncio
    async def test_send_say_message_rate_limited(self):
        """Test say message when rate limit is exceeded."""
        # Setup
        player_id = str(uuid.uuid4())
        message = "Hello, world!"

        self.mock_player_service.get_player_by_id.return_value = self.mock_player
        self.mock_rate_limiter.check_rate_limit.return_value = False

        # Execute
        result = await self.chat_service.send_say_message(player_id, message)

        # Verify
        assert result["success"] is False
        assert result["error"] == "Rate limit exceeded. Please wait before sending another message."
        assert result["rate_limited"] is True

    @pytest.mark.asyncio
    async def test_send_say_message_player_not_in_room(self):
        """Test say message when player is not in a room."""
        # Setup
        player_id = str(uuid.uuid4())
        message = "Hello, world!"

        self.mock_player_service.get_player_by_id.return_value = self.mock_player
        self.mock_rate_limiter.check_rate_limit.return_value = True
        self.mock_player.current_room_id = None

        # Execute
        result = await self.chat_service.send_say_message(player_id, message)

        # Verify
        assert result["success"] is False
        assert result["error"] == "Player not in a room"

    @pytest.mark.asyncio
    async def test_send_say_message_channel_muted(self):
        """Test say message when player is muted in say channel."""
        # Setup
        player_id = str(uuid.uuid4())
        message = "Hello, world!"

        self.mock_player_service.get_player_by_id.return_value = self.mock_player
        self.mock_rate_limiter.check_rate_limit.return_value = True
        self.mock_user_manager.is_channel_muted.return_value = True

        # Execute
        result = await self.chat_service.send_say_message(player_id, message)

        # Verify
        assert result["success"] is False
        assert result["error"] == "You are muted in the say channel"

    @pytest.mark.asyncio
    async def test_send_say_message_globally_muted(self):
        """Test say message when player is globally muted."""
        # Setup
        player_id = str(uuid.uuid4())
        message = "Hello, world!"

        self.mock_player_service.get_player_by_id.return_value = self.mock_player
        self.mock_rate_limiter.check_rate_limit.return_value = True
        self.mock_user_manager.is_channel_muted.return_value = False
        self.mock_user_manager.is_globally_muted.return_value = True

        # Execute
        result = await self.chat_service.send_say_message(player_id, message)

        # Verify
        assert result["success"] is False
        assert result["error"] == "You are globally muted and cannot send messages"

    @pytest.mark.asyncio
    async def test_send_say_message_cannot_send(self):
        """Test say message when player cannot send messages."""
        # Setup
        player_id = str(uuid.uuid4())
        message = "Hello, world!"

        self.mock_player_service.get_player_by_id.return_value = self.mock_player
        self.mock_rate_limiter.check_rate_limit.return_value = True
        self.mock_user_manager.is_channel_muted.return_value = False
        self.mock_user_manager.is_globally_muted.return_value = False
        self.mock_user_manager.can_send_message.return_value = False

        # Execute
        result = await self.chat_service.send_say_message(player_id, message)

        # Verify
        assert result["success"] is False
        assert result["error"] == "You cannot send messages at this time"

    @pytest.mark.asyncio
    async def test_publish_chat_message_to_nats_success(self):
        """Test successful NATS message publishing."""
        # Setup
        chat_message = ChatMessage("sender_id", "TestPlayer", "say", "Hello")
        room_id = "room_001"

        self.mock_nats_service.is_connected.return_value = True
        self.mock_nats_service.publish = AsyncMock(return_value=True)

        # Execute
        result = await self.chat_service._publish_chat_message_to_nats(chat_message, room_id)

        # Verify
        assert result is True
        self.mock_nats_service.publish.assert_called_once()

    @pytest.mark.asyncio
    async def test_publish_chat_message_to_nats_not_connected(self):
        """Test NATS publishing when service is not connected."""
        # Setup
        chat_message = ChatMessage("sender_id", "TestPlayer", "say", "Hello")
        room_id = "room_001"

        self.mock_nats_service.is_connected.return_value = False

        # Execute
        result = await self.chat_service._publish_chat_message_to_nats(chat_message, room_id)

        # Verify
        assert result is False
        self.mock_nats_service.publish.assert_not_called()

    @pytest.mark.asyncio
    async def test_publish_chat_message_to_nats_publish_fails(self):
        """Test NATS publishing when publish operation fails."""
        # Setup
        chat_message = ChatMessage("sender_id", "TestPlayer", "say", "Hello")
        room_id = "room_001"

        self.mock_nats_service.is_connected.return_value = True
        self.mock_nats_service.publish.return_value = False

        # Execute
        result = await self.chat_service._publish_chat_message_to_nats(chat_message, room_id)

        # Verify
        assert result is False

    @pytest.mark.asyncio
    async def test_publish_chat_message_to_nats_exception(self):
        """Test NATS publishing when an exception occurs."""
        # Setup
        chat_message = ChatMessage("sender_id", "TestPlayer", "say", "Hello")
        room_id = "room_001"

        self.mock_nats_service.is_connected.return_value = True
        self.mock_nats_service.publish.side_effect = Exception("NATS error")

        # Execute
        result = await self.chat_service._publish_chat_message_to_nats(chat_message, room_id)

        # Verify
        assert result is False

    def test_mute_channel_success(self):
        """Test successful channel muting."""
        # Setup
        player_id = str(uuid.uuid4())
        channel = "say"

        self.mock_player_service.get_player_by_id.return_value = self.mock_player
        self.mock_user_manager.mute_channel.return_value = True

        # Execute
        result = self.chat_service.mute_channel(player_id, channel)

        # Verify
        assert result is True
        self.mock_user_manager.mute_channel.assert_called_once_with(player_id, "TestPlayer", channel)

    def test_mute_channel_failure(self):
        """Test channel muting when it fails."""
        # Setup
        player_id = str(uuid.uuid4())
        channel = "say"

        self.mock_player_service.get_player_by_id.return_value = self.mock_player
        self.mock_user_manager.mute_channel.return_value = False

        # Execute
        result = self.chat_service.mute_channel(player_id, channel)

        # Verify
        assert result is False

    def test_unmute_channel_success(self):
        """Test successful channel unmuting."""
        # Setup
        player_id = str(uuid.uuid4())
        channel = "say"

        self.mock_player_service.get_player_by_id.return_value = self.mock_player
        self.mock_user_manager.unmute_channel.return_value = True

        # Execute
        result = self.chat_service.unmute_channel(player_id, channel)

        # Verify
        assert result is True
        self.mock_user_manager.unmute_channel.assert_called_once_with(player_id, "TestPlayer", channel)

    def test_is_channel_muted(self):
        """Test channel mute status checking."""
        # Setup
        player_id = str(uuid.uuid4())
        channel = "say"

        self.mock_user_manager.is_channel_muted.return_value = True

        # Execute
        result = self.chat_service.is_channel_muted(player_id, channel)

        # Verify
        assert result is True
        self.mock_user_manager.is_channel_muted.assert_called_once_with(player_id, channel)

    def test_mute_player_success(self):
        """Test successful player muting."""
        # Setup
        muter_id = str(uuid.uuid4())
        target_player_name = "TargetPlayer"
        target_player = Mock()
        target_player.id = str(uuid.uuid4())

        self.mock_player_service.get_player_by_id.return_value = self.mock_player
        self.mock_player_service.resolve_player_name.return_value = target_player
        self.mock_user_manager.mute_player.return_value = True

        # Execute
        result = self.chat_service.mute_player(muter_id, target_player_name)

        # Verify
        assert result is True
        self.mock_user_manager.mute_player.assert_called_once_with(
            muter_id, "TestPlayer", target_player.id, target_player_name
        )

    def test_mute_player_target_not_found(self):
        """Test player muting when target player is not found."""
        # Setup
        muter_id = str(uuid.uuid4())
        target_player_name = "TargetPlayer"

        self.mock_player_service.get_player_by_id.return_value = self.mock_player
        self.mock_player_service.resolve_player_name.return_value = None

        # Execute
        result = self.chat_service.mute_player(muter_id, target_player_name)

        # Verify
        assert result is False
        self.mock_user_manager.mute_player.assert_not_called()

    def test_unmute_player_success(self):
        """Test successful player unmuting."""
        # Setup
        muter_id = str(uuid.uuid4())
        target_player_name = "TargetPlayer"
        target_player = Mock()
        target_player.id = str(uuid.uuid4())

        self.mock_player_service.get_player_by_id.return_value = self.mock_player
        self.mock_player_service.resolve_player_name.return_value = target_player
        self.mock_user_manager.unmute_player.return_value = True

        # Execute
        result = self.chat_service.unmute_player(muter_id, target_player_name)

        # Verify
        assert result is True
        self.mock_user_manager.unmute_player.assert_called_once_with(
            muter_id, "TestPlayer", target_player.id, target_player_name
        )

    def test_is_player_muted(self):
        """Test player mute status checking."""
        # Setup
        muter_id = str(uuid.uuid4())
        target_player_id = str(uuid.uuid4())

        self.mock_user_manager.is_player_muted.return_value = True

        # Execute
        result = self.chat_service.is_player_muted(muter_id, target_player_id)

        # Verify
        assert result is True
        self.mock_user_manager.is_player_muted.assert_called_once_with(muter_id, target_player_id)

    def test_mute_global_success(self):
        """Test successful global muting."""
        # Setup
        muter_id = str(uuid.uuid4())
        target_player_name = "TargetPlayer"
        target_player = Mock()
        target_player.id = str(uuid.uuid4())
        duration_minutes = 30
        reason = "Spam"

        self.mock_player_service.get_player_by_id.return_value = self.mock_player
        self.mock_player_service.resolve_player_name.return_value = target_player
        self.mock_user_manager.mute_global.return_value = True

        # Execute
        result = self.chat_service.mute_global(muter_id, target_player_name, duration_minutes, reason)

        # Verify
        assert result is True
        self.mock_user_manager.mute_global.assert_called_once_with(
            muter_id, "TestPlayer", target_player.id, target_player_name, duration_minutes, reason
        )

    def test_unmute_global_success(self):
        """Test successful global unmuting."""
        # Setup
        unmuter_id = str(uuid.uuid4())
        target_player_name = "TargetPlayer"
        target_player = Mock()
        target_player.id = str(uuid.uuid4())

        self.mock_player_service.get_player_by_id.return_value = self.mock_player
        self.mock_player_service.resolve_player_name.return_value = target_player
        self.mock_user_manager.unmute_global.return_value = True

        # Execute
        result = self.chat_service.unmute_global(unmuter_id, target_player_name)

        # Verify
        assert result is True
        self.mock_user_manager.unmute_global.assert_called_once_with(
            unmuter_id, "TestPlayer", target_player.id, target_player_name
        )

    def test_is_globally_muted(self):
        """Test global mute status checking."""
        # Setup
        player_id = str(uuid.uuid4())

        self.mock_user_manager.is_globally_muted.return_value = True

        # Execute
        result = self.chat_service.is_globally_muted(player_id)

        # Verify
        assert result is True
        self.mock_user_manager.is_globally_muted.assert_called_once_with(player_id)

    def test_add_admin_success(self):
        """Test successful admin addition."""
        # Setup
        player_id = str(uuid.uuid4())

        self.mock_player_service.get_player_by_id.return_value = self.mock_player

        # Execute
        result = self.chat_service.add_admin(player_id)

        # Verify
        assert result is True
        self.mock_user_manager.add_admin.assert_called_once_with(player_id, "TestPlayer")

    def test_remove_admin_success(self):
        """Test successful admin removal."""
        # Setup
        player_id = str(uuid.uuid4())

        self.mock_player_service.get_player_by_id.return_value = self.mock_player

        # Execute
        result = self.chat_service.remove_admin(player_id)

        # Verify
        assert result is True
        self.mock_user_manager.remove_admin.assert_called_once_with(player_id, "TestPlayer")

    def test_is_admin(self):
        """Test admin status checking."""
        # Setup
        player_id = str(uuid.uuid4())

        self.mock_user_manager.is_admin.return_value = True

        # Execute
        result = self.chat_service.is_admin(player_id)

        # Verify
        assert result is True
        self.mock_user_manager.is_admin.assert_called_once_with(player_id)

    def test_can_send_message(self):
        """Test message sending permission checking."""
        # Setup
        sender_id = str(uuid.uuid4())
        target_id = str(uuid.uuid4())
        channel = "say"

        self.mock_user_manager.can_send_message.return_value = True

        # Execute
        result = self.chat_service.can_send_message(sender_id, target_id, channel)

        # Verify
        assert result is True
        self.mock_user_manager.can_send_message.assert_called_once_with(sender_id, target_id, channel)

    def test_get_player_mutes(self):
        """Test getting player mutes."""
        # Setup
        player_id = str(uuid.uuid4())
        expected_mutes = {"player_mutes": {}, "global_mutes": {}}

        self.mock_user_manager.get_player_mutes.return_value = expected_mutes

        # Execute
        result = self.chat_service.get_player_mutes(player_id)

        # Verify
        assert result == expected_mutes
        self.mock_user_manager.get_player_mutes.assert_called_once_with(player_id)

    def test_get_user_management_stats(self):
        """Test getting user management statistics."""
        # Setup
        expected_stats = {"total_players": 100, "muted_players": 5}

        self.mock_user_manager.get_system_stats.return_value = expected_stats

        # Execute
        result = self.chat_service.get_user_management_stats()

        # Verify
        assert result == expected_stats
        self.mock_user_manager.get_system_stats.assert_called_once()

    def test_get_room_messages_empty(self):
        """Test getting room messages when none exist."""
        # Setup
        room_id = "room_001"

        # Execute
        result = self.chat_service.get_room_messages(room_id)

        # Verify
        assert result == []

    def test_get_room_messages_with_messages(self):
        """Test getting room messages when messages exist."""
        # Setup
        room_id = "room_001"
        message1 = ChatMessage("sender1", "Player1", "say", "Hello")
        message2 = ChatMessage("sender2", "Player2", "say", "World")

        self.chat_service._room_messages[room_id] = [message1, message2]

        # Execute
        result = self.chat_service.get_room_messages(room_id)

        # Verify
        assert len(result) == 2
        assert result[0]["sender_name"] == "Player1"
        assert result[1]["sender_name"] == "Player2"

    def test_get_room_messages_with_limit(self):
        """Test getting room messages with limit."""
        # Setup
        room_id = "room_001"
        messages = [ChatMessage(f"sender{i}", f"Player{i}", "say", f"Message{i}") for i in range(10)]

        self.chat_service._room_messages[room_id] = messages

        # Execute
        result = self.chat_service.get_room_messages(room_id, limit=5)

        # Verify
        assert len(result) == 5
        assert result[0]["sender_name"] == "Player5"  # Last 5 messages

    def test_get_mute_status_player_not_found(self):
        """Test getting mute status when player is not found."""
        # Setup
        player_id = str(uuid.uuid4())

        self.mock_player_service.get_player_by_id.return_value = None

        # Execute
        result = self.chat_service.get_mute_status(player_id)

        # Verify
        assert result == "Player not found."

    def test_get_mute_status_success(self):
        """Test getting mute status successfully."""
        # Setup
        player_id = str(uuid.uuid4())

        self.mock_player_service.get_player_by_id.return_value = self.mock_player
        self.mock_user_manager.get_player_mutes.return_value = {"player_mutes": {}, "global_mutes": {}}
        self.mock_user_manager.is_admin.return_value = False

        # Execute
        result = self.chat_service.get_mute_status(player_id)

        # Verify
        assert "MUTE STATUS FOR TESTPLAYER" in result
        assert "PLAYERS YOU HAVE MUTED: None" in result
        assert "PLAYERS YOU HAVE GLOBALLY MUTED: None" in result

    def test_get_mute_status_admin(self):
        """Test getting mute status for admin player."""
        # Setup
        player_id = str(uuid.uuid4())

        self.mock_player_service.get_player_by_id.return_value = self.mock_player
        self.mock_user_manager.get_player_mutes.return_value = {"player_mutes": {}, "global_mutes": {}}
        self.mock_user_manager.is_admin.return_value = True

        # Execute
        result = self.chat_service.get_mute_status(player_id)

        # Verify
        assert "ADMIN STATUS: You are an admin" in result

    def test_get_mute_status_with_mutes(self):
        """Test getting mute status with existing mutes."""
        # Setup
        player_id = str(uuid.uuid4())

        self.mock_player_service.get_player_by_id.return_value = self.mock_player
        self.mock_user_manager.get_player_mutes.return_value = {
            "player_mutes": {"target1": {"target_name": "TargetPlayer1", "expires_at": None, "reason": "Spam"}},
            "global_mutes": {
                "target2": {
                    "target_name": "TargetPlayer2",
                    "expires_at": "2024-12-31T23:59:59+00:00",
                    "reason": "Harassment",
                }
            },
        }
        self.mock_user_manager.is_admin.return_value = False

        # Execute
        result = self.chat_service.get_mute_status(player_id)

        # Verify
        assert "TargetPlayer1" in result
        assert "TargetPlayer2" in result
        assert "Spam" in result
        assert "Harassment" in result

    def test_get_mute_status_exception(self):
        """Test getting mute status when an exception occurs."""
        # Setup
        player_id = str(uuid.uuid4())

        self.mock_player_service.get_player_by_id.side_effect = Exception("Database error")

        # Execute
        result = self.chat_service.get_mute_status(player_id)

        # Verify
        assert result == "Error retrieving mute status."

    def test_room_message_history_limit(self):
        """Test that room message history respects the limit."""
        # Setup
        room_id = "room_001"

        # Add more messages than the limit
        messages = [
            ChatMessage(f"sender{i}", f"Player{i}", "say", f"Message{i}") for i in range(150)
        ]  # More than _max_messages_per_room (100)

        self.chat_service._room_messages[room_id] = messages

        # Execute
        result = self.chat_service.get_room_messages(room_id)

        # Verify
        assert len(result) == 50  # Should be limited to default limit
        assert result[0]["sender_name"] == "Player100"  # Last 50 messages
        assert result[-1]["sender_name"] == "Player149"
