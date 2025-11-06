"""
Integration tests for NATSMessageHandler standardized subscription patterns.

This module tests the integration of NATSSubjectManager with NATSMessageHandler
to ensure proper subscription pattern usage.
"""

from unittest.mock import AsyncMock, patch

import pytest

from server.config.models import NATSConfig
from server.realtime.nats_message_handler import NATSMessageHandler
from server.services.nats_service import NATSService
from server.services.nats_subject_manager import NATSSubjectManager


class TestNATSMessageHandlerStandardizedPatterns:
    """Test NATSMessageHandler integration with NATSSubjectManager for standardized subscription patterns."""

    def setup_method(self):
        """Set up test fixtures."""
        # Create test configuration
        self.test_config = NATSConfig(
            host="localhost",
            port=4222,
            max_reconnect_attempts=3,
            connection_pool_size=2,
            batch_size=50,
            batch_timeout=0.05,
        )

        # Create NATSService instance
        self.nats_service = NATSService(self.test_config)

        # Create NATSSubjectManager instance
        self.subject_manager = NATSSubjectManager()

        # Mock NATS connection
        self.mock_nc = AsyncMock()
        self.nats_service.nc = self.mock_nc
        self.nats_service._running = True

    @pytest.mark.asyncio
    async def test_message_handler_uses_standardized_patterns_with_subject_manager(self):
        """Test that NATSMessageHandler uses standardized patterns when subject manager is provided."""
        # Create NATSMessageHandler with subject manager
        handler = NATSMessageHandler(self.nats_service, self.subject_manager)

        # Mock the subscribe method
        self.nats_service.subscribe = AsyncMock(return_value=True)

        # Start the handler
        await handler.start()

        # Verify standardized patterns were used
        expected_standardized_patterns = [
            "chat.say.room.*",
            "chat.local.subzone.*",
            "chat.global",
            "chat.whisper.player.*",
            "chat.system",
            "chat.emote.room.*",
            "chat.pose.room.*",
            "chat.local.*",  # Legacy compatibility
            "chat.party.*",
            "chat.admin",
        ]

        # Check that subscribe was called with standardized patterns
        subscribe_calls = self.nats_service.subscribe.call_args_list
        subscribed_patterns = [call[0][0] for call in subscribe_calls]

        for pattern in expected_standardized_patterns:
            assert pattern in subscribed_patterns, f"Expected pattern {pattern} not found in subscriptions"

    @pytest.mark.asyncio
    async def test_message_handler_uses_legacy_patterns_without_subject_manager(self):
        """Test that NATSMessageHandler uses legacy patterns when no subject manager is provided."""
        # Create NATSMessageHandler without subject manager
        handler = NATSMessageHandler(self.nats_service, None)

        # Mock the subscribe method
        self.nats_service.subscribe = AsyncMock(return_value=True)

        # Start the handler
        await handler.start()

        # Verify legacy patterns were used
        expected_legacy_patterns = [
            "chat.say.*",
            "chat.local.*",
            "chat.local.subzone.*",
            "chat.emote.*",
            "chat.pose.*",
            "chat.global",
            "chat.party.*",
            "chat.whisper.player.*",  # Standardized whisper pattern with player segment
            "chat.system",
            "chat.admin",
        ]

        # Check that subscribe was called with legacy patterns
        subscribe_calls = self.nats_service.subscribe.call_args_list
        subscribed_patterns = [call[0][0] for call in subscribe_calls]

        for pattern in expected_legacy_patterns:
            assert pattern in subscribed_patterns, f"Expected legacy pattern {pattern} not found in subscriptions"

    @pytest.mark.asyncio
    async def test_subscription_patterns_match_publishing_patterns(self):
        """Test that subscription patterns match the patterns used for publishing."""
        # Create NATSMessageHandler with subject manager
        handler = NATSMessageHandler(self.nats_service, self.subject_manager)

        # Mock the subscribe method
        self.nats_service.subscribe = AsyncMock(return_value=True)

        # Start the handler
        await handler.start()

        # Get the patterns that were subscribed to
        subscribe_calls = self.nats_service.subscribe.call_args_list
        subscribed_patterns = [call[0][0] for call in subscribe_calls]

        # Verify that subscription patterns are compatible with publishing patterns
        # This ensures messages published using NATSSubjectManager will be received
        compatible_patterns = [
            "chat.say.room.*",  # Matches chat.say.room.{room_id}
            "chat.local.subzone.*",  # Matches chat.local.subzone.{subzone}
            "chat.global",  # Matches chat.global
            "chat.whisper.player.*",  # Matches chat.whisper.player.{target_id}
            "chat.system",  # Matches chat.system
            "chat.emote.room.*",  # Matches chat.emote.room.{room_id}
            "chat.pose.room.*",  # Matches chat.pose.room.{room_id}
        ]

        for pattern in compatible_patterns:
            assert pattern in subscribed_patterns, f"Compatible pattern {pattern} not found in subscriptions"

    @pytest.mark.asyncio
    async def test_subscription_failure_handling(self):
        """Test that subscription failures are handled gracefully."""
        # Create NATSMessageHandler with subject manager
        handler = NATSMessageHandler(self.nats_service, self.subject_manager)

        # Mock subscribe to fail for some patterns
        async def mock_subscribe(subject, callback):
            if "chat.say.room.*" in subject:
                return False  # Simulate failure
            return True

        self.nats_service.subscribe = mock_subscribe

        # Start the handler
        await handler.start()

        # Verify that failed subscriptions are tracked
        assert "chat.say.room.*" not in handler.subscriptions or handler.subscriptions.get("chat.say.room.*") is False

    @pytest.mark.asyncio
    async def test_subject_manager_integration_with_nats_service(self):
        """Test that NATSMessageHandler integrates properly with NATSService subject manager."""
        # Create NATSService with subject manager
        nats_service_with_manager = NATSService(self.test_config, self.subject_manager)

        # Mock NATS connection
        mock_nc = AsyncMock()
        nats_service_with_manager.nc = mock_nc
        nats_service_with_manager._running = True

        # Create NATSMessageHandler
        handler = NATSMessageHandler(nats_service_with_manager, nats_service_with_manager.subject_manager)

        # Mock the subscribe method
        nats_service_with_manager.subscribe = AsyncMock(return_value=True)

        # Start the handler
        await handler.start()

        # Verify that the subject manager from NATSService is used
        assert handler.subject_manager is nats_service_with_manager.subject_manager

    @pytest.mark.asyncio
    async def test_backward_compatibility_without_subject_manager(self):
        """Test that the system maintains backward compatibility without subject manager."""
        # Create NATSMessageHandler without subject manager
        handler = NATSMessageHandler(self.nats_service, None)

        # Mock the subscribe method
        self.nats_service.subscribe = AsyncMock(return_value=True)

        # Start the handler
        await handler.start()

        # Verify that legacy patterns are still used
        subscribe_calls = self.nats_service.subscribe.call_args_list
        subscribed_patterns = [call[0][0] for call in subscribe_calls]

        # Should include legacy patterns
        legacy_patterns = ["chat.say.*", "chat.local.*", "chat.emote.*", "chat.pose.*"]
        for pattern in legacy_patterns:
            assert pattern in subscribed_patterns, f"Legacy pattern {pattern} not found in subscriptions"

    @pytest.mark.asyncio
    async def test_subscription_logging_includes_pattern_type(self):
        """Test that subscription logging includes information about pattern type."""
        # Create NATSMessageHandler with subject manager
        handler = NATSMessageHandler(self.nats_service, self.subject_manager)

        # Mock the subscribe method
        self.nats_service.subscribe = AsyncMock(return_value=True)

        # Mock logger to capture log calls
        with patch("server.realtime.nats_message_handler.logger") as mock_logger:
            # Start the handler
            await handler.start()

            # Verify that logging includes pattern type information
            log_calls = [call[0][0] for call in mock_logger.info.call_args_list]

            # Should log about standardized patterns
            standardized_logs = [log for log in log_calls if "standardized" in log.lower()]
            assert len(standardized_logs) > 0, "Should log about standardized patterns"

    @pytest.mark.asyncio
    async def test_subscription_patterns_are_valid_nats_subjects(self):
        """Test that all subscription patterns are valid NATS subjects."""
        # Create NATSMessageHandler with subject manager
        handler = NATSMessageHandler(self.nats_service, self.subject_manager)

        # Mock the subscribe method
        self.nats_service.subscribe = AsyncMock(return_value=True)

        # Start the handler
        await handler.start()

        # Get the patterns that were subscribed to
        subscribe_calls = self.nats_service.subscribe.call_args_list
        subscribed_patterns = [call[0][0] for call in subscribe_calls]

        # Verify that all patterns are valid NATS subjects
        for pattern in subscribed_patterns:
            # Basic NATS subject validation
            assert isinstance(pattern, str), f"Pattern {pattern} should be a string"
            assert len(pattern) > 0, f"Pattern {pattern} should not be empty"
            assert not pattern.startswith("."), f"Pattern {pattern} should not start with dot"
            assert not pattern.endswith("."), f"Pattern {pattern} should not end with dot"
            assert ".." not in pattern, f"Pattern {pattern} should not contain consecutive dots"
