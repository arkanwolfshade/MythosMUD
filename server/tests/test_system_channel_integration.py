"""
Integration tests for System Channel functionality.

This module tests the complete system channel flow including:
- Command processing
- NATS integration
- Logging
- Admin access control
"""

import uuid
from unittest.mock import AsyncMock, Mock, patch

import pytest

from ..commands.command_service import CommandService
from ..game.chat_service import ChatService


class TestSystemChannelIntegration:
    """Integration tests for system channel functionality."""

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

        # Create test players
        class MockPlayer:
            def __init__(self, player_id, name, level, room_id):
                self.id = player_id
                self.name = name
                self.level = level
                self.current_room_id = room_id

        self.admin_player = MockPlayer(str(uuid.uuid4()), "AdminUser", 10, "arkham_1")

        self.regular_player = MockPlayer(str(uuid.uuid4()), "RegularUser", 1, "arkham_1")

        # Chat service will be created in individual test methods with mocked dependencies

        # Create command service
        self.command_service = CommandService()

    def _create_chat_service_with_mocks(self, mock_user_manager, mock_rate_limiter, mock_nats_service):
        """Helper method to create ChatService with mocked dependencies."""
        chat_service = ChatService(
            persistence=self.mock_persistence,
            room_service=self.mock_room_service,
            player_service=self.mock_player_service,
            user_manager_instance=mock_user_manager,
        )

        # Replace services with mocks
        chat_service.nats_service = mock_nats_service
        chat_service.rate_limiter = mock_rate_limiter

        return chat_service

    def teardown_method(self):
        """Clean up test fixtures."""
        # Stop patches
        self.nats_patcher.stop()
        self.chat_logger_patcher.stop()
        self.rate_limiter_patcher.stop()
        self.user_manager_patcher.stop()

    @pytest.mark.asyncio
    async def test_system_command_integration_admin_success(self):
        """Test complete system command flow for admin user."""
        # Create chat service with mocked user manager
        chat_service = self._create_chat_service_with_mocks(
            self.mock_user_manager, self.mock_rate_limiter, self.mock_nats_service
        )

        # Setup mocks
        self.mock_player_service.resolve_player_name.return_value = self.admin_player
        self.mock_player_service.get_player_by_id.return_value = self.admin_player
        self.mock_user_manager.is_admin.return_value = True

        # Set up the player object to return the correct name
        self.admin_player.name = "AdminUser"

        # Create mock request context
        mock_request = Mock()
        mock_request.app = Mock()
        mock_request.app.state = Mock()
        mock_request.app.state.player_service = self.mock_player_service
        mock_request.app.state.chat_service = chat_service
        mock_request.app.state.user_manager = self.mock_user_manager

        # Test system command
        command_data = {"command_type": "system", "message": "Server maintenance in 5 minutes"}

        result = await self.command_service.process_validated_command(
            command_data=command_data,
            current_user=self.admin_player,
            request=mock_request,
            alias_storage=None,
            player_name="AdminUser",
        )

        # Verify command was processed successfully
        assert result["result"] == "You system: Server maintenance in 5 minutes"

        # Verify NATS was called
        self.mock_nats_service.publish.assert_called_once()
        call_args = self.mock_nats_service.publish.call_args
        assert call_args[0][0] == "chat.system"  # NATS subject
        published_data = call_args[0][1]
        assert published_data["channel"] == "system"
        assert published_data["content"] == "Server maintenance in 5 minutes"
        assert published_data["sender_name"] == "AdminUser"

        # Verify logging was called
        self.mock_chat_logger.log_system_channel_message.assert_called_once()

    @pytest.mark.asyncio
    async def test_system_command_integration_non_admin_denied(self):
        """Test system command flow for non-admin user."""
        # Create chat service with mocked user manager
        chat_service = self._create_chat_service_with_mocks(
            self.mock_user_manager, self.mock_rate_limiter, self.mock_nats_service
        )

        # Setup mocks
        self.mock_player_service.resolve_player_name.return_value = self.regular_player
        self.mock_user_manager.is_admin.return_value = False

        # Create mock request context
        mock_request = Mock()
        mock_request.app = Mock()
        mock_request.app.state = Mock()
        mock_request.app.state.player_service = self.mock_player_service
        mock_request.app.state.chat_service = chat_service
        mock_request.app.state.user_manager = self.mock_user_manager

        # Test system command
        command_data = {"command_type": "system", "message": "This should be denied"}

        result = await self.command_service.process_validated_command(
            command_data=command_data,
            current_user=self.regular_player,
            request=mock_request,
            alias_storage=None,
            player_name="RegularUser",
        )

        # Verify command was denied
        assert result["result"] == "You must be an admin to send system messages."

        # Verify NATS was not called
        self.mock_nats_service.publish.assert_not_called()

        # Verify logging was not called
        self.mock_chat_logger.log_system_channel_message.assert_not_called()

    @pytest.mark.asyncio
    async def test_system_command_integration_empty_message(self):
        """Test system command with empty message."""
        # Create chat service with mocked user manager
        chat_service = self._create_chat_service_with_mocks(
            self.mock_user_manager, self.mock_rate_limiter, self.mock_nats_service
        )

        # Setup mocks
        self.mock_player_service.resolve_player_name.return_value = self.admin_player
        self.mock_user_manager.is_admin.return_value = True

        # Create mock request context
        mock_request = Mock()
        mock_request.app = Mock()
        mock_request.app.state = Mock()
        mock_request.app.state.player_service = self.mock_player_service
        mock_request.app.state.chat_service = chat_service
        mock_request.app.state.user_manager = self.mock_user_manager

        # Test system command with empty message
        command_data = {"command_type": "system", "message": ""}

        result = await self.command_service.process_validated_command(
            command_data=command_data,
            current_user=self.admin_player,
            request=mock_request,
            alias_storage=None,
            player_name="AdminUser",
        )

        # Verify command was rejected
        assert result["result"] == "System what? Usage: system <message>"

        # Verify NATS was not called
        self.mock_nats_service.publish.assert_not_called()

        # Verify logging was not called
        self.mock_chat_logger.log_system_channel_message.assert_not_called()

    @pytest.mark.asyncio
    async def test_system_command_integration_nats_failure(self):
        """Test system command when NATS publishing fails."""
        # Create chat service with mocked user manager
        chat_service = self._create_chat_service_with_mocks(
            self.mock_user_manager, self.mock_rate_limiter, self.mock_nats_service
        )

        # Setup mocks
        self.mock_player_service.resolve_player_name.return_value = self.admin_player
        self.mock_user_manager.is_admin.return_value = True
        self.mock_nats_service.publish = AsyncMock(return_value=False)

        # Create mock request context
        mock_request = Mock()
        mock_request.app = Mock()
        mock_request.app.state = Mock()
        mock_request.app.state.player_service = self.mock_player_service
        mock_request.app.state.chat_service = chat_service
        mock_request.app.state.user_manager = self.mock_user_manager

        # Test system command
        command_data = {"command_type": "system", "message": "Test message"}

        result = await self.command_service.process_validated_command(
            command_data=command_data,
            current_user=self.admin_player,
            request=mock_request,
            alias_storage=None,
            player_name="AdminUser",
        )

        # Verify command failed due to NATS
        assert "Error sending system message" in result["result"]

        # Verify NATS was called but failed
        self.mock_nats_service.publish.assert_called_once()

        # Verify logging was called (logging happens before NATS check)
        self.mock_chat_logger.log_system_channel_message.assert_called_once()

    @pytest.mark.asyncio
    async def test_system_command_integration_nats_not_connected(self):
        """Test system command when NATS is not connected."""
        # Create chat service with mocked user manager
        chat_service = self._create_chat_service_with_mocks(
            self.mock_user_manager, self.mock_rate_limiter, self.mock_nats_service
        )

        # Setup mocks
        self.mock_player_service.resolve_player_name.return_value = self.admin_player
        self.mock_user_manager.is_admin.return_value = True
        self.mock_nats_service.is_connected.return_value = False

        # Create mock request context
        mock_request = Mock()
        mock_request.app = Mock()
        mock_request.app.state = Mock()
        mock_request.app.state.player_service = self.mock_player_service
        mock_request.app.state.chat_service = chat_service
        mock_request.app.state.user_manager = self.mock_user_manager

        # Test system command
        command_data = {"command_type": "system", "message": "Test message"}

        result = await self.command_service.process_validated_command(
            command_data=command_data,
            current_user=self.admin_player,
            request=mock_request,
            alias_storage=None,
            player_name="AdminUser",
        )

        # Verify command failed due to NATS not connected
        assert "Error sending system message" in result["result"]

        # Verify NATS was not called
        self.mock_nats_service.publish.assert_not_called()

        # Verify logging was called (logging happens before NATS check)
        self.mock_chat_logger.log_system_channel_message.assert_called_once()

    @pytest.mark.asyncio
    async def test_system_command_integration_message_structure(self):
        """Test that system messages have correct structure."""
        # Create chat service with mocked user manager
        chat_service = self._create_chat_service_with_mocks(
            self.mock_user_manager, self.mock_rate_limiter, self.mock_nats_service
        )

        # Setup mocks
        self.mock_player_service.resolve_player_name.return_value = self.admin_player
        self.mock_player_service.get_player_by_id.return_value = self.admin_player
        self.mock_user_manager.is_admin.return_value = True

        # Create mock request context
        mock_request = Mock()
        mock_request.app = Mock()
        mock_request.app.state = Mock()
        mock_request.app.state.player_service = self.mock_player_service
        mock_request.app.state.chat_service = chat_service
        mock_request.app.state.user_manager = self.mock_user_manager

        # Test system command
        test_message = "Important announcement: Server restart scheduled"
        command_data = {"command_type": "system", "message": test_message}

        result = await self.command_service.process_validated_command(
            command_data=command_data,
            current_user=self.admin_player,
            request=mock_request,
            alias_storage=None,
            player_name="AdminUser",
        )

        # Verify command was processed successfully
        assert result["result"] == f"You system: {test_message}"

        # Verify NATS was called with correct structure
        self.mock_nats_service.publish.assert_called_once()
        call_args = self.mock_nats_service.publish.call_args
        published_data = call_args[0][1]

        # Check required fields
        assert "message_id" in published_data
        assert "channel" in published_data
        assert "sender_id" in published_data
        assert "sender_name" in published_data
        assert "content" in published_data
        assert "timestamp" in published_data

        # Check field values
        assert published_data["channel"] == "system"
        assert published_data["sender_name"] == "AdminUser"
        assert published_data["content"] == test_message
        assert published_data["sender_id"] == self.admin_player.id

        # Verify logging was called with correct data
        self.mock_chat_logger.log_system_channel_message.assert_called_once()
        log_call_args = self.mock_chat_logger.log_system_channel_message.call_args
        log_data = log_call_args[0][0]
        assert log_data["channel"] == "system"
        assert log_data["sender_name"] == "AdminUser"
        assert log_data["content"] == test_message

    @pytest.mark.asyncio
    async def test_system_command_integration_rate_limiting(self):
        """Test that system commands respect rate limiting."""
        # Create chat service with mocked user manager
        chat_service = self._create_chat_service_with_mocks(
            self.mock_user_manager, self.mock_rate_limiter, self.mock_nats_service
        )

        # Setup mocks
        self.mock_player_service.resolve_player_name.return_value = self.admin_player
        self.mock_user_manager.is_admin.return_value = True
        self.mock_rate_limiter.check_rate_limit.return_value = False  # Rate limited

        # Create mock request context
        mock_request = Mock()
        mock_request.app = Mock()
        mock_request.app.state = Mock()
        mock_request.app.state.player_service = self.mock_player_service
        mock_request.app.state.chat_service = chat_service
        mock_request.app.state.user_manager = self.mock_user_manager

        # Test system command
        command_data = {"command_type": "system", "message": "Rate limited message"}

        result = await self.command_service.process_validated_command(
            command_data=command_data,
            current_user=self.admin_player,
            request=mock_request,
            alias_storage=None,
            player_name="AdminUser",
        )

        # Verify command was rate limited
        assert "rate limit" in result["result"].lower()

        # Verify NATS was not called
        self.mock_nats_service.publish.assert_not_called()

        # Verify logging was not called (rate limiting happens before logging)
        self.mock_chat_logger.log_system_channel_message.assert_not_called()

        # Verify rate limiter was checked
        self.mock_rate_limiter.check_rate_limit.assert_called_once()
        rate_limit_call_args = self.mock_rate_limiter.check_rate_limit.call_args
        assert rate_limit_call_args[0][0] == self.admin_player.id  # player_id
        assert rate_limit_call_args[0][1] == "system"  # channel
