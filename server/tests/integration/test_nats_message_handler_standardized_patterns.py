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

pytestmark = pytest.mark.integration


class TestNATSMessageHandlerStandardizedPatterns:
    """Test NATSMessageHandler integration with NATSSubjectManager for standardized subscription patterns."""

    # Type annotations for instance attributes (satisfies linter without requiring __init__)
    # Attributes are initialized in setup_method() per pytest best practices
    test_config: NATSConfig
    nats_service: NATSService
    subject_manager: NATSSubjectManager
    mock_nc: AsyncMock

    def setup_method(self) -> None:
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
    async def test_message_handler_uses_standardized_patterns_with_subject_manager(self) -> None:
        """Test that NATSMessageHandler uses standardized patterns when subject manager is provided."""
        assert self.nats_service is not None
        assert self.subject_manager is not None
        # Create NATSMessageHandler with subject manager and connection manager
        from unittest.mock import MagicMock

        mock_connection_manager = MagicMock()
        handler = NATSMessageHandler(
            self.nats_service, self.subject_manager, connection_manager=mock_connection_manager
        )

        # Mock the subscribe method
        mock_subscribe = AsyncMock(return_value=True)
        self.nats_service.subscribe = mock_subscribe  # type: ignore[method-assign] # Mocking method for test

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
            # Note: chat.local.* is not used - replaced by chat.local.subzone.*
            # chat.party.* and chat.admin are not in NATSSubjectManager patterns
        ]

        # Check that subscribe was called with standardized patterns
        subscribe_calls = mock_subscribe.call_args_list
        subscribed_patterns = [call[0][0] for call in subscribe_calls]

        for pattern in expected_standardized_patterns:
            assert pattern in subscribed_patterns, f"Expected pattern {pattern} not found in subscriptions"

    @pytest.mark.asyncio
    async def test_message_handler_uses_legacy_patterns_without_subject_manager(self) -> None:
        """Test that NATSMessageHandler requires subject manager (legacy mode removed)."""
        assert self.nats_service is not None
        # Create NATSMessageHandler without subject manager
        from unittest.mock import MagicMock

        mock_connection_manager = MagicMock()
        handler = NATSMessageHandler(self.nats_service, None, connection_manager=mock_connection_manager)

        # Mock the subscribe method
        self.nats_service.subscribe = AsyncMock(return_value=True)  # type: ignore[method-assign] # Mocking method for test

        # Start the handler - should return False because subject_manager is required
        # (start() catches RuntimeError and returns False instead of raising)
        result = await handler.start()
        assert result is False, "Handler should fail to start without subject_manager"

    @pytest.mark.asyncio
    async def test_subscription_patterns_match_publishing_patterns(self) -> None:
        """Test that subscription patterns match the patterns used for publishing."""
        assert self.nats_service is not None
        assert self.subject_manager is not None
        # Create NATSMessageHandler with subject manager and connection manager
        from unittest.mock import MagicMock

        mock_connection_manager = MagicMock()
        handler = NATSMessageHandler(
            self.nats_service, self.subject_manager, connection_manager=mock_connection_manager
        )

        # Mock the subscribe method
        mock_subscribe = AsyncMock(return_value=True)
        self.nats_service.subscribe = mock_subscribe  # type: ignore[method-assign] # Mocking method for test

        # Start the handler
        await handler.start()

        # Get the patterns that were subscribed to
        subscribe_calls = mock_subscribe.call_args_list
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
    async def test_subscription_failure_handling(self) -> None:
        """Test that subscription failures are handled gracefully."""
        assert self.nats_service is not None
        assert self.subject_manager is not None
        # Create NATSMessageHandler with subject manager and connection manager
        from unittest.mock import MagicMock

        mock_connection_manager = MagicMock()
        handler = NATSMessageHandler(
            self.nats_service, self.subject_manager, connection_manager=mock_connection_manager
        )

        # Mock subscribe to raise exception for some patterns (subscribe now raises instead of returning False)
        from server.services.nats_exceptions import NATSSubscribeError

        async def mock_subscribe(subject, _callback):
            if "chat.say.room.*" in subject:
                raise NATSSubscribeError("Subscription failed", subject=subject)  # Simulate failure
            return True

        self.nats_service.subscribe = mock_subscribe  # type: ignore[method-assign] # Mocking method for test

        # Start the handler - should handle the exception gracefully
        await handler.start()

        # Verify that failed subscriptions are not tracked (exception prevents subscription)
        assert "chat.say.room.*" not in handler.subscriptions

    @pytest.mark.asyncio
    async def test_subject_manager_integration_with_nats_service(self) -> None:
        """Test that NATSMessageHandler integrates properly with NATSService subject manager."""
        assert self.test_config is not None
        assert self.subject_manager is not None
        # Create NATSService with subject manager
        nats_service_with_manager = NATSService(self.test_config, self.subject_manager)

        # Mock NATS connection
        mock_nc = AsyncMock()
        nats_service_with_manager.nc = mock_nc
        nats_service_with_manager._running = True

        # Create NATSMessageHandler with connection manager
        from unittest.mock import MagicMock

        mock_connection_manager = MagicMock()
        handler = NATSMessageHandler(
            nats_service_with_manager,
            nats_service_with_manager.subject_manager,
            connection_manager=mock_connection_manager,
        )

        # Mock the subscribe method
        nats_service_with_manager.subscribe = AsyncMock(return_value=True)  # type: ignore[method-assign] # Mocking method for test

        # Start the handler
        await handler.start()

        # Verify that the subject manager from NATSService is used
        assert handler.subject_manager is nats_service_with_manager.subject_manager

    @pytest.mark.asyncio
    async def test_backward_compatibility_without_subject_manager(self) -> None:
        """Test that the system requires subject manager (backward compatibility removed)."""
        assert self.nats_service is not None
        # Create NATSMessageHandler without subject manager
        from unittest.mock import MagicMock

        mock_connection_manager = MagicMock()
        handler = NATSMessageHandler(self.nats_service, None, connection_manager=mock_connection_manager)

        # Mock the subscribe method
        self.nats_service.subscribe = AsyncMock(return_value=True)  # type: ignore[method-assign] # Mocking method for test

        # Start the handler - should return False because subject_manager is required
        # (start() catches RuntimeError and returns False instead of raising)
        result = await handler.start()
        assert result is False, "Handler should fail to start without subject_manager"

    @pytest.mark.asyncio
    async def test_subscription_logging_includes_pattern_type(self) -> None:
        """Test that subscription logging includes information about pattern type."""
        assert self.nats_service is not None
        assert self.subject_manager is not None
        # Create NATSMessageHandler with subject manager and connection manager
        from unittest.mock import MagicMock

        mock_connection_manager = MagicMock()
        handler = NATSMessageHandler(
            self.nats_service, self.subject_manager, connection_manager=mock_connection_manager
        )

        # Mock the subscribe method
        self.nats_service.subscribe = AsyncMock(return_value=True)  # type: ignore[method-assign] # Mocking method for test

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
    async def test_subscription_patterns_are_valid_nats_subjects(self) -> None:
        """Test that all subscription patterns are valid NATS subjects."""
        assert self.nats_service is not None
        assert self.subject_manager is not None
        # Create NATSMessageHandler with subject manager and connection manager
        from unittest.mock import MagicMock

        mock_connection_manager = MagicMock()
        handler = NATSMessageHandler(
            self.nats_service, self.subject_manager, connection_manager=mock_connection_manager
        )

        # Mock the subscribe method
        mock_subscribe = AsyncMock(return_value=True)
        self.nats_service.subscribe = mock_subscribe  # type: ignore[method-assign] # Mocking method for test

        # Start the handler
        await handler.start()

        # Get the patterns that were subscribed to
        subscribe_calls = mock_subscribe.call_args_list
        subscribed_patterns = [call[0][0] for call in subscribe_calls]

        # Verify that all patterns are valid NATS subjects
        for pattern in subscribed_patterns:
            # Basic NATS subject validation
            assert isinstance(pattern, str), f"Pattern {pattern} should be a string"
            assert len(pattern) > 0, f"Pattern {pattern} should not be empty"
            assert not pattern.startswith("."), f"Pattern {pattern} should not start with dot"
            assert not pattern.endswith("."), f"Pattern {pattern} should not end with dot"
            assert ".." not in pattern, f"Pattern {pattern} should not contain consecutive dots"
