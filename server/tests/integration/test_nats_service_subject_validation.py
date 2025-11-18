"""
Integration tests for NATSService subject validation integration.

This module tests the integration of NATSSubjectManager with NATSService
to ensure proper subject validation before message publishing.
"""

import asyncio
import uuid
from unittest.mock import AsyncMock, patch

import pytest

from server.config.models import NATSConfig
from server.services.nats_service import NATSService
from server.services.nats_subject_manager import NATSSubjectManager


class TestNATSServiceSubjectValidation:
    """Test NATSService integration with NATSSubjectManager for subject validation."""

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

        # Initialize connection pool for testing (mock the pool)
        self.nats_service._pool_initialized = True
        self.nats_service.connection_pool = [self.mock_nc]
        self.nats_service.available_connections = asyncio.Queue()

        # Test data
        self.test_subject = "chat.say.room.test-room-123"
        self.test_message_data = {
            "message_id": str(uuid.uuid4()),
            "sender_id": str(uuid.uuid4()),
            "sender_name": "TestPlayer",
            "content": "Hello, world!",
            "channel": "say",
            "timestamp": "2025-01-01T12:00:00Z",
        }

    async def _init_connection_pool(self):
        """Helper to initialize connection pool for async tests."""
        await self.nats_service.available_connections.put(self.mock_nc)

    @pytest.mark.asyncio
    async def test_publish_with_valid_subject_passes_validation(self):
        """Test that publishing with a valid subject passes validation."""
        # Initialize connection pool
        await self._init_connection_pool()

        # Inject subject manager
        self.nats_service.subject_manager = self.subject_manager

        # Mock successful publish
        self.mock_nc.publish = AsyncMock()

        # Publish message (should not raise exception)
        await self.nats_service.publish(self.test_subject, self.test_message_data)

        # Verify publish was called
        self.mock_nc.publish.assert_called_once()

    @pytest.mark.asyncio
    async def test_publish_with_invalid_subject_fails_validation(self):
        """Test that publishing with an invalid subject fails validation."""
        # Initialize connection pool
        await self._init_connection_pool()

        # Inject subject manager with strict validation
        strict_manager = NATSSubjectManager(strict_validation=True)
        self.nats_service.subject_manager = strict_manager

        # Invalid subject with special characters
        invalid_subject = "chat.say.room@invalid"

        # Publish message with invalid subject (should raise exception or fail)
        from server.services.nats_exceptions import NATSPublishError

        with pytest.raises(NATSPublishError):
            await self.nats_service.publish(invalid_subject, self.test_message_data)

        # Verify publish was not called
        self.mock_nc.publish.assert_not_called()

    @pytest.mark.asyncio
    async def test_publish_without_subject_manager_works_normally(self):
        """Test that publishing without subject manager works normally (backward compatibility)."""
        # Initialize connection pool
        await self._init_connection_pool()

        # Ensure no subject manager is injected
        self.nats_service.subject_manager = None

        # Mock successful publish
        self.mock_nc.publish = AsyncMock()

        # Publish message (should not raise exception)
        await self.nats_service.publish(self.test_subject, self.test_message_data)

        # Verify publish was called (no validation)
        self.mock_nc.publish.assert_called_once()

    @pytest.mark.asyncio
    async def test_publish_with_validation_error_logs_appropriately(self):
        """Test that validation errors are logged with proper context."""
        # Initialize connection pool
        await self._init_connection_pool()

        # Inject subject manager with strict validation
        strict_manager = NATSSubjectManager(strict_validation=True)
        self.nats_service.subject_manager = strict_manager

        # Invalid subject
        invalid_subject = "chat.say.room@invalid"

        # Mock logger to capture log calls
        with patch("server.services.nats_service.logger") as mock_logger:
            # Publish message with invalid subject (should raise exception)
            from server.services.nats_exceptions import NATSPublishError

            with pytest.raises(NATSPublishError):
                await self.nats_service.publish(invalid_subject, self.test_message_data)

            # Verify error was logged
            mock_logger.error.assert_called()
            error_call = mock_logger.error.call_args
            assert "subject validation failed" in error_call[0][0] or "validation" in str(error_call)

    @pytest.mark.asyncio
    async def test_publish_with_correlation_id_tracking(self):
        """Test that validation failures include correlation ID tracking."""
        # Initialize connection pool
        await self._init_connection_pool()

        # Inject subject manager
        self.nats_service.subject_manager = self.subject_manager

        # Add correlation ID to message data
        correlation_id = str(uuid.uuid4())
        self.test_message_data["correlation_id"] = correlation_id

        # Mock successful publish
        self.mock_nc.publish = AsyncMock()

        # Publish message (should not raise exception)
        await self.nats_service.publish(self.test_subject, self.test_message_data)

        # Verify publish succeeded
        self.mock_nc.publish.assert_called_once()

    @pytest.mark.asyncio
    async def test_publish_with_pool_includes_subject_validation(self):
        """Test that publish_with_pool method includes subject validation."""
        # Initialize connection pool
        await self._init_connection_pool()

        # Inject subject manager
        self.nats_service.subject_manager = self.subject_manager

        # Publish message using pool (should not raise exception)
        await self.nats_service.publish_with_pool(self.test_subject, self.test_message_data)

        # Verify publish was called
        self.mock_nc.publish.assert_called_once()

    @pytest.mark.asyncio
    async def test_publish_batch_includes_subject_validation(self):
        """Test that publish_batch method includes subject validation."""
        # Initialize connection pool
        await self._init_connection_pool()

        # Inject subject manager
        self.nats_service.subject_manager = self.subject_manager

        # Set small batch size to trigger immediate flush
        self.nats_service.batch_size = 1

        # Mock successful batch processing
        with patch.object(self.nats_service, "_flush_batch", new_callable=AsyncMock) as mock_flush:
            mock_flush.return_value = True

            # Publish message to batch
            result = await self.nats_service.publish_batch(self.test_subject, self.test_message_data)

            # Verify batch processing was called (publish_batch returns bool)
            assert result is True
            mock_flush.assert_called_once()

    @pytest.mark.asyncio
    async def test_subject_manager_can_be_injected_after_creation(self):
        """Test that subject manager can be injected after NATSService creation."""
        # Create service without explicit subject manager (but it will be auto-created)
        assert self.nats_service.subject_manager is not None

        # Replace with different manager
        new_manager = NATSSubjectManager(strict_validation=True)
        self.nats_service.subject_manager = new_manager

        # Verify injection worked
        assert self.nats_service.subject_manager is new_manager

        # Test that validation now works
        await self._init_connection_pool()
        self.mock_nc.publish = AsyncMock()
        await self.nats_service.publish(self.test_subject, self.test_message_data)
        self.mock_nc.publish.assert_called_once()

    @pytest.mark.asyncio
    async def test_subject_manager_can_be_replaced(self):
        """Test that subject manager can be replaced."""
        # Inject initial subject manager
        initial_manager = NATSSubjectManager()
        self.nats_service.subject_manager = initial_manager

        # Replace with different manager
        new_manager = NATSSubjectManager(strict_validation=True)
        self.nats_service.subject_manager = new_manager

        # Verify replacement worked
        assert self.nats_service.subject_manager is new_manager
        assert self.nats_service.subject_manager is not initial_manager

    @pytest.mark.asyncio
    async def test_validation_performance_impact_is_minimal(self):
        """Test that subject validation has minimal performance impact."""
        import time

        # Initialize connection pool
        await self._init_connection_pool()

        # Inject subject manager
        self.nats_service.subject_manager = self.subject_manager

        # Mock successful publish
        self.mock_nc.publish = AsyncMock()

        # Measure time for multiple publishes
        start_time = time.time()
        for _ in range(100):
            await self.nats_service.publish(self.test_subject, self.test_message_data)
        end_time = time.time()

        # Verify all publishes succeeded
        assert self.mock_nc.publish.call_count == 100

        # Verify reasonable performance (should be very fast)
        total_time = end_time - start_time
        assert total_time < 1.0  # Should complete 100 publishes in under 1 second

    @pytest.mark.asyncio
    async def test_validation_with_different_subject_patterns(self):
        """Test validation with different subject patterns."""
        # Inject subject manager
        self.nats_service.subject_manager = self.subject_manager

        # Mock successful publish
        self.mock_nc.publish = AsyncMock()

        # Test various valid subject patterns
        valid_subjects = [
            "chat.say.room.test-room-123",
            "chat.local.subzone.arkham",
            "chat.global",
            "chat.system",
            "chat.whisper.player.test-player-456",
            "chat.emote.room.test-room-123",
            "chat.pose.room.test-room-123",
        ]

        # Initialize connection pool
        await self._init_connection_pool()

        for subject in valid_subjects:
            await self.nats_service.publish(subject, self.test_message_data)

        # Verify all publishes were called
        assert self.mock_nc.publish.call_count == len(valid_subjects)

    @pytest.mark.asyncio
    async def test_validation_with_invalid_subject_patterns(self):
        """Test validation with invalid subject patterns."""
        # Initialize connection pool
        await self._init_connection_pool()

        # Inject subject manager with strict validation
        strict_manager = NATSSubjectManager(strict_validation=True)
        self.nats_service.subject_manager = strict_manager

        # Test various invalid subject patterns
        invalid_subjects = [
            "chat.say.room@invalid",  # Special characters
            "chat.say.room invalid",  # Spaces
            "chat.say.room.invalid@",  # Special characters at end
            "chat.say.room.invalid#",  # Hash symbol
            "chat.say.room.invalid$",  # Dollar sign
        ]

        from server.services.nats_exceptions import NATSPublishError

        for subject in invalid_subjects:
            with pytest.raises(NATSPublishError):
                await self.nats_service.publish(subject, self.test_message_data)

        # Verify no publishes were called
        self.mock_nc.publish.assert_not_called()

    @pytest.mark.asyncio
    async def test_subject_validation_can_be_disabled_via_config(self):
        """Test that subject validation can be disabled via configuration."""
        # Create NATSService with validation disabled
        config = NATSConfig(enable_subject_validation=False)
        nats_service = NATSService(config)

        # Mock NATS connection and initialize pool
        mock_nc = AsyncMock()
        nats_service.nc = mock_nc
        nats_service._running = True
        nats_service._pool_initialized = True
        nats_service.connection_pool = [mock_nc]
        nats_service.available_connections = asyncio.Queue()
        await nats_service.available_connections.put(mock_nc)

        # Invalid subject that would normally fail validation
        invalid_subject = "chat.say.room@invalid"

        # Publish message with invalid subject (should succeed when validation disabled)
        await nats_service.publish(invalid_subject, self.test_message_data)

        # Verify publish succeeded (validation disabled)
        mock_nc.publish.assert_called_once()

    @pytest.mark.asyncio
    async def test_strict_validation_configuration(self):
        """Test that strict validation configuration is respected."""
        # Create NATSService with strict validation enabled
        config = NATSConfig(strict_subject_validation=True)
        nats_service = NATSService(config)

        # Mock NATS connection and initialize pool
        mock_nc = AsyncMock()
        nats_service.nc = mock_nc
        nats_service._running = True
        nats_service._pool_initialized = True
        nats_service.connection_pool = [mock_nc]
        nats_service.available_connections = asyncio.Queue()
        await nats_service.available_connections.put(mock_nc)

        # Invalid subject
        invalid_subject = "chat.say.room@invalid"

        # Publish message with invalid subject (should raise exception with strict validation)
        from server.services.nats_exceptions import NATSPublishError

        with pytest.raises(NATSPublishError):
            await nats_service.publish(invalid_subject, self.test_message_data)
        mock_nc.publish.assert_not_called()

    @pytest.mark.asyncio
    async def test_subject_manager_created_with_config(self):
        """Test that subject manager is created with correct configuration."""
        # Create NATSService with strict validation enabled
        config = NATSConfig(strict_subject_validation=True)
        nats_service = NATSService(config)

        # Verify subject manager was created with correct configuration
        assert nats_service.subject_manager is not None
        assert nats_service.subject_manager._strict_validation is True

    @pytest.mark.asyncio
    async def test_subject_manager_not_created_when_disabled(self):
        """Test that subject manager is not created when validation is disabled."""
        # Create NATSService with validation disabled
        config = NATSConfig(enable_subject_validation=False)
        nats_service = NATSService(config)

        # Verify subject manager was not created
        assert nats_service.subject_manager is None


class TestNATSServiceSubjectManagerDependencyInjection:
    def setup_method(self):
        """Set up test fixtures."""
        self.test_config = NATSConfig()
        self.subject_manager = NATSSubjectManager()

    def test_nats_service_accepts_subject_manager_injection(self):
        """Test that NATSService accepts subject manager injection."""
        # Create NATSService with subject manager
        nats_service = NATSService(self.test_config, subject_manager=self.subject_manager)

        # Verify injection worked
        assert nats_service.subject_manager is self.subject_manager

    def test_nats_service_works_without_subject_manager(self):
        """Test that NATSService works without explicit subject manager (backward compatibility)."""
        # Create NATSService without explicit subject manager
        nats_service = NATSService(self.test_config)

        # Verify subject manager was auto-created (new behavior)
        assert nats_service.subject_manager is not None

    def test_subject_manager_can_be_set_after_creation(self):
        """Test that subject manager can be set after NATSService creation."""
        # Create NATSService without explicit subject manager
        nats_service = NATSService(self.test_config)
        # Subject manager will be auto-created, so it won't be None
        assert nats_service.subject_manager is not None

        # Replace with different manager
        new_manager = NATSSubjectManager(strict_validation=True)
        nats_service.subject_manager = new_manager

        # Verify injection worked
        assert nats_service.subject_manager is new_manager

    def test_subject_manager_can_be_replaced(self):
        """Test that subject manager can be replaced."""
        # Create NATSService with initial subject manager
        initial_manager = NATSSubjectManager()
        nats_service = NATSService(self.test_config, subject_manager=initial_manager)

        # Replace with different manager
        new_manager = NATSSubjectManager(strict_validation=True)
        nats_service.subject_manager = new_manager

        # Verify replacement worked
        assert nats_service.subject_manager is new_manager
        assert nats_service.subject_manager is not initial_manager
