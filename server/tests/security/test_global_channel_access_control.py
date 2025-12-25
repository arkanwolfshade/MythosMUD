"""
Tests for Global Channel Access Control.

This module tests the level-based access control for the global channel,
including configuration validation, rate limiting, and permission checks.
"""

from unittest.mock import AsyncMock, Mock

import pytest

from server.config import get_config
from server.game.chat_service import ChatService
from server.game.player_service import PlayerService
from server.services.rate_limiter import RateLimiter
from server.services.user_manager import UserManager

pytestmark = pytest.mark.security


class TestGlobalChannelAccessControl:
    """Test global channel access control functionality."""

    @pytest.fixture
    def mock_player_service(self):
        """Create a mock player service."""
        service = Mock(spec=PlayerService)
        return service

    @pytest.fixture
    def mock_rate_limiter(self):
        """Create a mock rate limiter."""
        limiter = Mock(spec=RateLimiter)
        return limiter

    @pytest.fixture
    def mock_user_manager(self):
        """Create a mock user manager."""
        manager = Mock(spec=UserManager)
        return manager

    @pytest.fixture
    def chat_service(self, mock_player_service, mock_rate_limiter, mock_user_manager):
        """Create a chat service with mocked dependencies."""
        service = ChatService(persistence=Mock(), room_service=Mock(), player_service=mock_player_service)
        service.rate_limiter = mock_rate_limiter
        service.user_manager = mock_user_manager
        return service

    def test_global_channel_rate_limit_configuration(self) -> None:
        """Test that global channel rate limit is properly configured."""
        config = get_config()
        # Config is now a Pydantic object with attributes (config.chat.rate_limit_global)
        # Test environment sets rate_limit_global to 100 (via env.unit_test.example)
        assert config.chat.rate_limit_global == 100

    def test_global_channel_configuration_structure(self) -> None:
        """Test that global channel configuration structure exists."""
        config = get_config()
        # Config is now a Pydantic object with attributes
        assert hasattr(config, "chat")
        assert hasattr(config.chat, "rate_limit_global")
        assert hasattr(config.chat, "rate_limit_local")

    @pytest.mark.asyncio
    async def test_global_message_level_1_player_allowed(self, chat_service, mock_player_service):
        """Test that level 1 player can send global messages."""
        # Mock player with level 1
        mock_player = Mock()
        mock_player.level = 1
        mock_player.name = "TestPlayer"
        mock_player.current_room_id = "test_room"
        mock_player_service.get_player_by_id.return_value = mock_player

        # Mock rate limiter to allow message
        chat_service.rate_limiter.check_rate_limit.return_value = True

        # Mock user manager permissions
        chat_service.user_manager.is_channel_muted.return_value = False
        chat_service.user_manager.is_globally_muted.return_value = False
        chat_service.user_manager.can_send_message.return_value = True

        # Mock NATS service
        chat_service.nats_service = Mock()
        chat_service.nats_service.is_connected.return_value = True
        chat_service.nats_service.publish = AsyncMock(return_value=True)

        result = await chat_service.send_global_message("test_player_id", "Hello world!")

        assert result["success"] is True
        assert "message" in result

    @pytest.mark.asyncio
    async def test_global_message_level_0_player_denied(self, chat_service, mock_player_service):
        """Test that level 0 player cannot send global messages."""
        # Mock player with level 0
        mock_player = Mock()
        mock_player.level = 0
        mock_player.name = "TestPlayer"
        mock_player_service.get_player_by_id.return_value = mock_player

        result = await chat_service.send_global_message("test_player_id", "Hello world!")

        assert result["success"] is False
        assert "level" in result["error"].lower()

    @pytest.mark.asyncio
    async def test_global_message_rate_limit_exceeded(self, chat_service, mock_player_service):
        """Test that rate limited players cannot send global messages."""
        # Mock player with sufficient level
        mock_player = Mock()
        mock_player.level = 5
        mock_player.name = "TestPlayer"
        mock_player.current_room_id = "test_room"
        mock_player_service.get_player_by_id.return_value = mock_player

        # Mock rate limiter to deny message
        chat_service.rate_limiter.check_rate_limit.return_value = False

        result = await chat_service.send_global_message("test_player_id", "Hello world!")

        assert result["success"] is False
        assert "rate limit" in result["error"].lower()
        assert result["rate_limited"] is True

    @pytest.mark.asyncio
    async def test_global_message_channel_muted(self, chat_service, mock_player_service):
        """Test that muted players cannot send global messages."""
        # Mock player with sufficient level
        mock_player = Mock()
        mock_player.level = 5
        mock_player.name = "TestPlayer"
        mock_player.current_room_id = "test_room"
        mock_player_service.get_player_by_id.return_value = mock_player

        # Mock rate limiter to allow message
        chat_service.rate_limiter.check_rate_limit.return_value = True

        # Mock user manager to indicate channel is muted
        chat_service.user_manager.is_channel_muted.return_value = True

        result = await chat_service.send_global_message("test_player_id", "Hello world!")

        assert result["success"] is False
        assert "muted" in result["error"].lower()

    @pytest.mark.asyncio
    async def test_global_message_globally_muted(self, chat_service, mock_player_service):
        """Test that globally muted players cannot send global messages."""
        # Mock player with sufficient level
        mock_player = Mock()
        mock_player.level = 5
        mock_player.name = "TestPlayer"
        mock_player.current_room_id = "test_room"
        mock_player_service.get_player_by_id.return_value = mock_player

        # Mock rate limiter to allow message
        chat_service.rate_limiter.check_rate_limit.return_value = True

        # Mock user manager permissions
        chat_service.user_manager.is_channel_muted.return_value = False
        chat_service.user_manager.is_globally_muted.return_value = True

        result = await chat_service.send_global_message("test_player_id", "Hello world!")

        assert result["success"] is False
        assert "globally muted" in result["error"].lower()

    @pytest.mark.asyncio
    async def test_global_message_empty_content(self, chat_service):
        """Test that empty global messages are rejected."""
        result = await chat_service.send_global_message("test_player_id", "")

        assert result["success"] is False
        assert "empty" in result["error"].lower()

    @pytest.mark.asyncio
    async def test_global_message_too_long(self, chat_service):
        """Test that overly long global messages are rejected."""
        long_message = "x" * 1001  # Exceed 1000 character limit
        result = await chat_service.send_global_message("test_player_id", long_message)

        assert result["success"] is False
        assert "long" in result["error"].lower()

    @pytest.mark.asyncio
    async def test_global_message_player_not_found(self, chat_service, mock_player_service):
        """Test that non-existent players cannot send global messages."""
        mock_player_service.get_player_by_id.return_value = None

        result = await chat_service.send_global_message("nonexistent_player", "Hello world!")

        assert result["success"] is False
        assert "not found" in result["error"].lower()

    @pytest.mark.asyncio
    async def test_global_message_nats_publish_success(self, chat_service, mock_player_service):
        """Test successful global message publishing to NATS."""
        # Mock player with sufficient level
        mock_player = Mock()
        mock_player.level = 5
        mock_player.name = "TestPlayer"
        mock_player.current_room_id = "test_room"
        mock_player_service.get_player_by_id.return_value = mock_player

        # Mock rate limiter to allow message
        chat_service.rate_limiter.check_rate_limit.return_value = True

        # Mock user manager permissions
        chat_service.user_manager.is_channel_muted.return_value = False
        chat_service.user_manager.is_globally_muted.return_value = False
        chat_service.user_manager.can_send_message.return_value = True

        # Mock NATS service
        chat_service.nats_service = Mock()
        chat_service.nats_service.is_connected.return_value = True
        chat_service.nats_service.publish = AsyncMock(return_value=True)

        result = await chat_service.send_global_message("test_player_id", "Hello world!")

        assert result["success"] is True
        # Verify NATS publish was called
        chat_service.nats_service.publish.assert_called_once()

    @pytest.mark.asyncio
    async def test_global_message_nats_publish_failure(self, chat_service, mock_player_service):
        """Test handling of NATS publish failure for global messages."""
        # Mock player with sufficient level
        mock_player = Mock()
        mock_player.level = 5
        mock_player.name = "TestPlayer"
        mock_player.current_room_id = "test_room"
        mock_player_service.get_player_by_id.return_value = mock_player

        # Mock rate limiter to allow message
        chat_service.rate_limiter.check_rate_limit.return_value = True

        # Mock user manager permissions
        chat_service.user_manager.is_channel_muted.return_value = False
        chat_service.user_manager.is_globally_muted.return_value = False
        chat_service.user_manager.can_send_message.return_value = True

        # Mock NATS service to fail
        chat_service.nats_service = Mock()
        chat_service.nats_service.is_connected.return_value = True
        chat_service.nats_service.publish.return_value = False

        result = await chat_service.send_global_message("test_player_id", "Hello world!")

        assert result["success"] is False
        assert "unavailable" in result["error"].lower()

    def test_global_channel_configuration_validation(self) -> None:
        """Test that global channel configuration is properly validated."""
        config = get_config()

        # Test required configuration attributes exist (Pydantic structure)
        assert hasattr(config, "chat")
        assert hasattr(config.chat, "rate_limit_global")
        assert hasattr(config.chat, "rate_limit_local")

        # Test configuration values are valid
        # Pylint incorrectly infers config.chat as FieldInfo instead of ChatConfig.
        # This is a false positive - Pydantic models use dynamic attributes that pylint cannot infer.
        assert isinstance(config.chat.rate_limit_global, int)  # pylint: disable=no-member
        assert config.chat.rate_limit_global > 0  # pylint: disable=no-member

    @pytest.mark.asyncio
    async def test_global_message_rate_limiter_integration(self, chat_service, mock_player_service):
        """Test integration with rate limiter for global messages."""
        # Mock player with sufficient level
        mock_player = Mock()
        mock_player.level = 5
        mock_player.name = "TestPlayer"
        mock_player.current_room_id = "test_room"
        mock_player_service.get_player_by_id.return_value = mock_player

        # Mock user manager permissions
        chat_service.user_manager.is_channel_muted.return_value = False
        chat_service.user_manager.is_globally_muted.return_value = False
        chat_service.user_manager.can_send_message.return_value = True

        # Mock NATS service
        chat_service.nats_service = Mock()
        chat_service.nats_service.is_connected.return_value = True
        chat_service.nats_service.publish = AsyncMock(return_value=True)

        # Test rate limiter is called with correct parameters
        chat_service.rate_limiter.check_rate_limit.return_value = True

        await chat_service.send_global_message("test_player_id", "Hello world!")

        # Verify rate limiter was called with correct parameters
        chat_service.rate_limiter.check_rate_limit.assert_called_once_with("test_player_id", "global", "TestPlayer")

    @pytest.mark.asyncio
    async def test_global_message_user_manager_integration(self, chat_service, mock_player_service):
        """Test integration with user manager for global messages."""
        # Mock player with sufficient level
        mock_player = Mock()
        mock_player.level = 5
        mock_player.name = "TestPlayer"
        mock_player.current_room_id = "test_room"
        mock_player_service.get_player_by_id.return_value = mock_player

        # Mock rate limiter to allow message
        chat_service.rate_limiter.check_rate_limit.return_value = True

        # Mock user manager permissions
        chat_service.user_manager.is_channel_muted.return_value = False
        chat_service.user_manager.is_globally_muted.return_value = False
        chat_service.user_manager.can_send_message.return_value = True

        # Mock NATS service
        chat_service.nats_service = Mock()
        chat_service.nats_service.is_connected.return_value = True
        chat_service.nats_service.publish = AsyncMock(return_value=True)

        await chat_service.send_global_message("test_player_id", "Hello world!")

        # Verify user manager methods were called
        chat_service.user_manager.load_player_mutes.assert_called_once_with("test_player_id")
        chat_service.user_manager.is_channel_muted.assert_called_once_with("test_player_id", "global")
        chat_service.user_manager.is_globally_muted.assert_called_once_with("test_player_id")
        chat_service.user_manager.can_send_message.assert_called_once_with("test_player_id", channel="global")
