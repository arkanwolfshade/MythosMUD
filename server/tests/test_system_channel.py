"""
Tests for System Channel functionality.

This module tests the SystemChannelStrategy and related system channel functionality
including admin-only access, NATS integration, and logging.
"""

import uuid
from unittest.mock import AsyncMock, Mock

import pytest

from ..game.chat_service import ChatService


class TestSystemChannelStrategy:
    """Test cases for SystemChannelStrategy."""

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

        # Set up async mocks for NATS service
        self.mock_nats_service.publish = AsyncMock(return_value=True)
        self.mock_nats_service.is_connected = Mock(return_value=True)

        # Create the service instance
        self.chat_service = ChatService(self.mock_persistence, self.mock_room_service, self.mock_player_service)

        # Replace service dependencies with mocks
        self.chat_service.nats_service = self.mock_nats_service
        self.chat_service.chat_logger = self.mock_chat_logger
        self.chat_service.rate_limiter = self.mock_rate_limiter
        self.chat_service.user_manager = self.mock_user_manager

        # Create mock players for testing
        self.admin_player = Mock()
        self.admin_player.id = str(uuid.uuid4())
        self.admin_player.name = "AdminPlayer"
        self.admin_player.level = 10  # Admin level

        self.regular_player = Mock()
        self.regular_player.id = str(uuid.uuid4())
        self.regular_player.name = "RegularPlayer"
        self.regular_player.level = 1  # Regular player level

    @pytest.mark.asyncio
    async def test_send_system_message_admin_access(self):
        """Test that admin can send system messages."""
        # Setup mocks
        self.mock_player_service.get_player_by_id.return_value = self.admin_player
        self.mock_user_manager.is_admin.return_value = True
        # NATS service is already set up in setup_method with AsyncMock

        # Test system message
        result = await self.chat_service.send_system_message(self.admin_player.id, "System announcement")

        # Verify success
        assert result["success"] is True
        assert "message" in result
        assert result["message"]["channel"] == "system"
        assert result["message"]["content"] == "System announcement"
        assert result["message"]["sender_name"] == "AdminPlayer"

        # Verify NATS publishing
        self.mock_nats_service.publish.assert_called_once()

    @pytest.mark.asyncio
    async def test_send_system_message_non_admin_denied(self):
        """Test that non-admin players cannot send system messages."""
        # Setup mocks
        self.mock_player_service.get_player_by_id.return_value = self.regular_player
        self.mock_user_manager.is_admin.return_value = False

        # Test system message
        result = await self.chat_service.send_system_message(self.regular_player.id, "System announcement")

        # Verify failure
        assert result["success"] is False
        assert "admin" in result["error"].lower()

        # Verify no NATS publishing
        self.mock_nats_service.publish.assert_not_called()

    @pytest.mark.asyncio
    async def test_send_system_message_empty_content(self):
        """Test that empty system messages are rejected."""
        # Setup mocks
        self.mock_player_service.get_player_by_id.return_value = self.admin_player
        self.mock_user_manager.is_admin.return_value = True

        # Test empty message
        result = await self.chat_service.send_system_message(self.admin_player.id, "")

        # Verify failure
        assert result["success"] is False
        assert "empty" in result["error"].lower()

    @pytest.mark.asyncio
    async def test_send_system_message_too_long(self):
        """Test that overly long system messages are rejected."""
        # Setup mocks
        self.mock_player_service.get_player_by_id.return_value = self.admin_player
        self.mock_user_manager.is_admin.return_value = True

        # Test long message
        long_message = "A" * 2001  # Exceeds 2000 character limit
        result = await self.chat_service.send_system_message(self.admin_player.id, long_message)

        # Verify failure
        assert result["success"] is False
        assert "long" in result["error"].lower()

    @pytest.mark.asyncio
    async def test_send_system_message_player_not_found(self):
        """Test that system messages fail when player is not found."""
        # Setup mocks
        self.mock_player_service.get_player_by_id.return_value = None

        # Test system message
        result = await self.chat_service.send_system_message("invalid_id", "System announcement")

        # Verify failure
        assert result["success"] is False
        assert "not found" in result["error"].lower()

    @pytest.mark.asyncio
    async def test_send_system_message_nats_failure(self):
        """Test that system messages handle NATS failures gracefully."""
        # Setup mocks
        self.mock_player_service.get_player_by_id.return_value = self.admin_player
        self.mock_user_manager.is_admin.return_value = True
        self.mock_nats_service.is_connected.return_value = True
        self.mock_nats_service.publish.return_value = False

        # Test system message
        result = await self.chat_service.send_system_message(self.admin_player.id, "System announcement")

        # Verify failure
        assert result["success"] is False
        assert "unavailable" in result["error"].lower()

    @pytest.mark.asyncio
    async def test_send_system_message_nats_not_connected(self):
        """Test that system messages fail when NATS is not connected."""
        # Setup mocks
        self.mock_player_service.get_player_by_id.return_value = self.admin_player
        self.mock_user_manager.is_admin.return_value = True
        self.mock_nats_service.is_connected.return_value = False

        # Test system message
        result = await self.chat_service.send_system_message(self.admin_player.id, "System announcement")

        # Verify failure
        assert result["success"] is False
        assert "unavailable" in result["error"].lower()

    @pytest.mark.asyncio
    async def test_send_system_message_logging(self):
        """Test that system messages are properly logged."""
        # Setup mocks
        self.mock_player_service.get_player_by_id.return_value = self.admin_player
        self.mock_user_manager.is_admin.return_value = True
        self.mock_nats_service.is_connected.return_value = True
        self.mock_nats_service.publish.return_value = True

        # Test system message
        await self.chat_service.send_system_message(self.admin_player.id, "System announcement")

        # Verify logging calls
        self.mock_chat_logger.log_chat_message.assert_called_once()
        self.mock_chat_logger.log_system_channel_message.assert_called_once()

        # Verify log message content
        log_call = self.mock_chat_logger.log_chat_message.call_args[0][0]
        assert log_call["channel"] == "system"
        assert log_call["content"] == "System announcement"
        assert log_call["sender_name"] == "AdminPlayer"

    @pytest.mark.asyncio
    async def test_send_system_message_rate_limiting(self):
        """Test that system messages are subject to rate limiting."""
        # Setup mocks
        self.mock_player_service.get_player_by_id.return_value = self.admin_player
        self.mock_user_manager.is_admin.return_value = True
        self.mock_rate_limiter.check_rate_limit.return_value = False

        # Test system message
        result = await self.chat_service.send_system_message(self.admin_player.id, "System announcement")

        # Verify rate limiting
        assert result["success"] is False
        assert "rate limit" in result["error"].lower()
        assert result["rate_limited"] is True

        # Verify rate limiter was called
        self.mock_rate_limiter.check_rate_limit.assert_called_once_with(self.admin_player.id, "system", "AdminPlayer")

    @pytest.mark.asyncio
    async def test_send_system_message_globally_muted_admin(self):
        """Test that globally muted admins can still send system messages."""
        # Setup mocks
        self.mock_player_service.get_player_by_id.return_value = self.admin_player
        self.mock_user_manager.is_admin.return_value = True
        self.mock_user_manager.is_globally_muted.return_value = True
        # NATS service is already set up in setup_method with AsyncMock

        # Test system message
        result = await self.chat_service.send_system_message(self.admin_player.id, "System announcement")

        # Verify success (admins can send system messages even when globally muted)
        assert result["success"] is True

    @pytest.mark.asyncio
    async def test_send_system_message_nats_subject(self):
        """Test that system messages use correct NATS subject."""
        # Setup mocks
        self.mock_player_service.get_player_by_id.return_value = self.admin_player
        self.mock_user_manager.is_admin.return_value = True
        self.mock_nats_service.is_connected.return_value = True
        self.mock_nats_service.publish.return_value = True

        # Test system message
        await self.chat_service.send_system_message(self.admin_player.id, "System announcement")

        # Verify NATS subject
        nats_call = self.mock_nats_service.publish.call_args
        assert nats_call[0][0] == "chat.system"  # Correct subject for system channel

    @pytest.mark.asyncio
    async def test_send_system_message_message_structure(self):
        """Test that system messages have correct structure."""
        # Setup mocks
        self.mock_player_service.get_player_by_id.return_value = self.admin_player
        self.mock_user_manager.is_admin.return_value = True
        # NATS service is already set up in setup_method with AsyncMock

        # Test system message
        result = await self.chat_service.send_system_message(self.admin_player.id, "System announcement")

        # Verify message structure
        message = result["message"]
        assert message["sender_id"] == self.admin_player.id
        assert message["sender_name"] == "AdminPlayer"
        assert message["channel"] == "system"
        assert message["content"] == "System announcement"
        assert "id" in message
        assert "timestamp" in message

    @pytest.mark.asyncio
    async def test_send_system_message_whitespace_handling(self):
        """Test that system messages handle whitespace correctly."""
        # Setup mocks
        self.mock_player_service.get_player_by_id.return_value = self.admin_player
        self.mock_user_manager.is_admin.return_value = True
        # NATS service is already set up in setup_method with AsyncMock

        # Test system message with whitespace
        result = await self.chat_service.send_system_message(self.admin_player.id, "  System announcement  ")

        # Verify whitespace is stripped
        assert result["success"] is True
        assert result["message"]["content"] == "System announcement"
