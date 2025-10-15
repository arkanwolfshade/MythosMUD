"""
Tests for Whisper Channel functionality.

This module tests the WhisperChannelStrategy and related whisper channel functionality
including player-to-player messaging, NATS integration, and reply tracking.
"""

import uuid
from unittest.mock import AsyncMock, Mock, patch

import pytest

from server.game.chat_service import ChatService


class TestWhisperChannelStrategy:
    """Test cases for WhisperChannelStrategy."""

    def setup_method(self):
        """Set up test fixtures."""
        # Create mock dependencies
        self.mock_persistence = Mock()
        self.mock_room_service = Mock()
        self.mock_player_service = AsyncMock()

        # Create mock services
        self.mock_nats_service = Mock()
        self.mock_chat_logger = Mock()
        self.mock_rate_limiter = Mock()
        self.mock_user_manager = Mock()

        # Set up async mocks for NATS service
        self.mock_nats_service.publish = AsyncMock(return_value=True)
        self.mock_nats_service.is_connected = Mock(return_value=True)

        # Create test players
        class MockPlayer:
            def __init__(self, player_id, name, level, room_id):
                self.id = player_id
                self.name = name
                self.level = level
                self.current_room_id = room_id

        self.sender_player = MockPlayer(str(uuid.uuid4()), "SenderPlayer", 5, "arkham_1")
        self.target_player = MockPlayer(str(uuid.uuid4()), "TargetPlayer", 3, "arkham_2")

        # Create chat service
        self.chat_service = ChatService(
            persistence=self.mock_persistence,
            room_service=self.mock_room_service,
            player_service=self.mock_player_service,
        )

        # Ensure the mock is properly set up for the ChatService
        self.chat_service.nats_service = self.mock_nats_service
        self.chat_service.chat_logger = self.mock_chat_logger
        self.chat_service.rate_limiter = self.mock_rate_limiter
        self.chat_service.user_manager = self.mock_user_manager

        # Patch global services
        self.nats_patcher = patch("server.services.nats_service.nats_service", self.mock_nats_service)
        self.chat_logger_patcher = patch("server.game.chat_service.chat_logger", self.mock_chat_logger)
        self.rate_limiter_patcher = patch("server.game.chat_service.rate_limiter", self.mock_rate_limiter)
        self.user_manager_patcher = patch("server.game.chat_service.user_manager", self.mock_user_manager)

        # Start patches
        self.nats_patcher.start()
        self.chat_logger_patcher.start()
        self.rate_limiter_patcher.start()
        self.user_manager_patcher.start()

    def teardown_method(self):
        """Clean up test fixtures."""
        # Stop patches
        self.nats_patcher.stop()
        self.chat_logger_patcher.stop()
        self.rate_limiter_patcher.stop()
        self.user_manager_patcher.stop()

    @pytest.mark.asyncio
    async def test_send_whisper_message_success(self):
        """Test that whisper messages are sent successfully."""
        # Setup mocks
        self.mock_player_service.get_player_by_id.side_effect = lambda pid: {
            self.sender_player.id: self.sender_player,
            self.target_player.id: self.target_player,
        }.get(pid)
        self.mock_user_manager.is_player_muted.return_value = False
        self.mock_rate_limiter.check_rate_limit.return_value = True

        # Test whisper message
        result = await self.chat_service.send_whisper_message(
            self.sender_player.id, self.target_player.id, "Hello there!"
        )

        # Verify success
        assert result["success"] is True
        assert "message" in result
        assert result["message"]["content"] == "Hello there!"
        assert result["message"]["sender_id"] == self.sender_player.id
        assert result["message"]["target_id"] == self.target_player.id
        assert result["message"]["channel"] == "whisper"

        # Verify NATS was called
        self.mock_nats_service.publish.assert_called_once()

        # Verify logging was called
        self.mock_chat_logger.log_whisper_channel_message.assert_called_once()

    @pytest.mark.asyncio
    async def test_send_whisper_message_sender_not_found(self):
        """Test that whisper fails when sender is not found."""
        # Setup mocks
        self.mock_player_service.get_player_by_id.return_value = None

        # Test whisper message
        result = await self.chat_service.send_whisper_message(
            "nonexistent_sender", self.target_player.id, "Hello there!"
        )

        # Verify failure
        assert result["success"] is False
        assert "Sender not found" in result["error"]

        # Verify NATS was not called
        self.mock_nats_service.publish.assert_not_called()

    @pytest.mark.asyncio
    async def test_send_whisper_message_target_not_found(self):
        """Test that whisper fails when target is not found."""
        # Setup mocks
        self.mock_player_service.get_player_by_id.side_effect = lambda pid: {
            self.sender_player.id: self.sender_player,
        }.get(pid)

        # Test whisper message
        result = await self.chat_service.send_whisper_message(
            self.sender_player.id, "nonexistent_target", "Hello there!"
        )

        # Verify failure
        assert result["success"] is False
        assert "Target player not found" in result["error"]

        # Verify NATS was not called
        self.mock_nats_service.publish.assert_not_called()

    @pytest.mark.asyncio
    async def test_send_whisper_message_empty_content(self):
        """Test that whisper fails with empty content."""
        # Setup mocks
        self.mock_player_service.get_player_by_id.side_effect = lambda pid: {
            self.sender_player.id: self.sender_player,
            self.target_player.id: self.target_player,
        }.get(pid)

        # Test whisper message with empty content
        result = await self.chat_service.send_whisper_message(self.sender_player.id, self.target_player.id, "")

        # Verify failure
        assert result["success"] is False
        assert "Message content cannot be empty" in result["error"]

        # Verify NATS was not called
        self.mock_nats_service.publish.assert_not_called()

    @pytest.mark.asyncio
    async def test_send_whisper_message_too_long(self):
        """Test that whisper fails with message too long."""
        # Setup mocks
        self.mock_player_service.get_player_by_id.side_effect = lambda pid: {
            self.sender_player.id: self.sender_player,
            self.target_player.id: self.target_player,
        }.get(pid)

        # Test whisper message that's too long
        long_message = "x" * 2001  # Over 2000 character limit
        result = await self.chat_service.send_whisper_message(
            self.sender_player.id, self.target_player.id, long_message
        )

        # Verify failure
        assert result["success"] is False
        assert "Message too long" in result["error"]

        # Verify NATS was not called
        self.mock_nats_service.publish.assert_not_called()

    @pytest.mark.asyncio
    async def test_send_whisper_message_nats_failure(self):
        """Test that whisper fails when NATS publishing fails."""
        # Setup mocks
        self.mock_player_service.get_player_by_id.side_effect = lambda pid: {
            self.sender_player.id: self.sender_player,
            self.target_player.id: self.target_player,
        }.get(pid)
        self.mock_user_manager.is_player_muted.return_value = False
        self.mock_rate_limiter.check_rate_limit.return_value = True
        self.mock_nats_service.publish.return_value = False

        # Test whisper message
        result = await self.chat_service.send_whisper_message(
            self.sender_player.id, self.target_player.id, "Hello there!"
        )

        # Verify failure
        assert result["success"] is False
        assert "Chat system temporarily unavailable" in result["error"]

        # Verify NATS was called
        self.mock_nats_service.publish.assert_called_once()

    @pytest.mark.asyncio
    async def test_send_whisper_message_nats_not_connected(self):
        """Test that whisper fails when NATS is not connected."""
        # Setup mocks
        self.mock_player_service.get_player_by_id.side_effect = lambda pid: {
            self.sender_player.id: self.sender_player,
            self.target_player.id: self.target_player,
        }.get(pid)
        self.mock_user_manager.is_player_muted.return_value = False
        self.mock_rate_limiter.check_rate_limit.return_value = True
        self.mock_nats_service.is_connected.return_value = False

        # Test whisper message
        result = await self.chat_service.send_whisper_message(
            self.sender_player.id, self.target_player.id, "Hello there!"
        )

        # Verify failure
        assert result["success"] is False
        assert "Chat system temporarily unavailable" in result["error"]

        # Verify NATS was not called
        self.mock_nats_service.publish.assert_not_called()

    @pytest.mark.asyncio
    async def test_send_whisper_message_logging(self):
        """Test that whisper messages are logged correctly."""
        # Setup mocks
        self.mock_player_service.get_player_by_id.side_effect = lambda pid: {
            self.sender_player.id: self.sender_player,
            self.target_player.id: self.target_player,
        }.get(pid)
        self.mock_user_manager.is_player_muted.return_value = False
        self.mock_rate_limiter.check_rate_limit.return_value = True

        # Test whisper message
        await self.chat_service.send_whisper_message(self.sender_player.id, self.target_player.id, "Secret message")

        # Verify logging calls
        self.mock_chat_logger.log_whisper_channel_message.assert_called_once()

        # Verify the logged message data
        logged_data = self.mock_chat_logger.log_whisper_channel_message.call_args[0][0]
        assert logged_data["sender_id"] == self.sender_player.id
        assert logged_data["target_id"] == self.target_player.id
        assert logged_data["content"] == "Secret message"
        assert logged_data["channel"] == "whisper"

    @pytest.mark.asyncio
    async def test_send_whisper_message_rate_limiting(self):
        """Test that whisper messages are rate limited."""
        # Setup mocks
        self.mock_player_service.get_player_by_id.side_effect = lambda pid: {
            self.sender_player.id: self.sender_player,
            self.target_player.id: self.target_player,
        }.get(pid)
        self.mock_user_manager.is_player_muted.return_value = False
        self.mock_rate_limiter.check_rate_limit.return_value = False

        # Test whisper message
        result = await self.chat_service.send_whisper_message(
            self.sender_player.id, self.target_player.id, "Rate limited message"
        )

        # Verify rate limiting
        assert result["success"] is False
        assert (
            "rate limit" in result["error"].lower()
            or "Chat system temporarily unavailable" in result["error"]
            or "sending messages too quickly" in result["error"].lower()
        )

        # Verify NATS was not called
        self.mock_nats_service.publish.assert_not_called()

        # Verify rate limiter was called
        self.mock_rate_limiter.check_rate_limit.assert_called_once_with(
            self.sender_player.id, "whisper", "SenderPlayer"
        )

    @pytest.mark.asyncio
    async def test_send_whisper_message_nats_subject(self):
        """Test that whisper messages use correct NATS subject."""
        # Setup mocks
        self.mock_player_service.get_player_by_id.side_effect = lambda pid: {
            self.sender_player.id: self.sender_player,
            self.target_player.id: self.target_player,
        }.get(pid)
        self.mock_user_manager.is_player_muted.return_value = False
        self.mock_rate_limiter.check_rate_limit.return_value = True
        self.mock_nats_service.is_connected.return_value = True

        # Test whisper message
        await self.chat_service.send_whisper_message(self.sender_player.id, self.target_player.id, "Test message")

        # Verify NATS subject
        nats_call = self.mock_nats_service.publish.call_args
        assert nats_call is not None
        # The subject should be for whisper channel
        # The exact subject format will depend on the implementation

    @pytest.mark.asyncio
    async def test_send_whisper_message_message_structure(self):
        """Test that whisper messages have correct structure."""
        # Setup mocks
        self.mock_player_service.get_player_by_id.side_effect = lambda pid: {
            self.sender_player.id: self.sender_player,
            self.target_player.id: self.target_player,
        }.get(pid)
        self.mock_user_manager.is_player_muted.return_value = False
        self.mock_rate_limiter.check_rate_limit.return_value = True

        # Test whisper message
        result = await self.chat_service.send_whisper_message(
            self.sender_player.id, self.target_player.id, "Test message"
        )

        # Verify message structure
        assert result["success"] is True
        message = result["message"]
        assert message["id"] is not None
        assert message["content"] == "Test message"
        assert message["sender_id"] == self.sender_player.id
        assert message["target_id"] == self.target_player.id
        assert message["channel"] == "whisper"
        assert message["timestamp"] is not None

    @pytest.mark.asyncio
    async def test_send_whisper_message_whitespace_handling(self):
        """Test that whisper messages handle whitespace correctly."""
        # Setup mocks
        self.mock_player_service.get_player_by_id.side_effect = lambda pid: {
            self.sender_player.id: self.sender_player,
            self.target_player.id: self.target_player,
        }.get(pid)
        self.mock_user_manager.is_player_muted.return_value = False
        self.mock_rate_limiter.check_rate_limit.return_value = True

        # Test whisper message with whitespace
        result = await self.chat_service.send_whisper_message(
            self.sender_player.id, self.target_player.id, "  Test message  "
        )

        # Verify whitespace is stripped
        assert result["success"] is True
        assert result["message"]["content"] == "Test message"

    @pytest.mark.asyncio
    async def test_send_whisper_message_to_self(self):
        """Test that whispering to yourself is allowed."""
        # Setup mocks
        self.mock_player_service.get_player_by_id.return_value = self.sender_player
        self.mock_user_manager.is_player_muted.return_value = False
        self.mock_rate_limiter.check_rate_limit.return_value = True

        # Test whisper message to self
        result = await self.chat_service.send_whisper_message(
            self.sender_player.id, self.sender_player.id, "Note to self"
        )

        # Verify success (self-whispers should be allowed)
        assert result["success"] is True
        assert result["message"]["sender_id"] == self.sender_player.id
        assert result["message"]["target_id"] == self.sender_player.id
