"""
Unit tests for NATS exception classes.

Tests the NATS exception hierarchy for proper error handling and context preservation.
"""

import pytest

from server.services.nats_exceptions import (
    NATSConnectionError,
    NATSError,
    NATSHealthCheckError,
    NATSPublishError,
    NATSSubscribeError,
)


class TestNATSError:
    """Test suite for NATSError base class."""

    def test_nats_error_creation(self):
        """Test NATSError can be created with a message."""
        error = NATSError("Test error message")
        assert str(error) == "Test error message"
        assert isinstance(error, Exception)

    def test_nats_error_inheritance(self):
        """Test NATSError inherits from Exception."""
        error = NATSError("Test")
        assert isinstance(error, Exception)


class TestNATSConnectionError:
    """Test suite for NATSConnectionError."""

    def test_connection_error_creation(self):
        """Test NATSConnectionError can be created with message."""
        error = NATSConnectionError("Connection failed")
        assert str(error) == "Connection failed"
        assert isinstance(error, NATSError)

    def test_connection_error_with_url(self):
        """Test NATSConnectionError stores URL."""
        error = NATSConnectionError("Connection failed", url="nats://localhost:4222")
        assert error.url == "nats://localhost:4222"

    def test_connection_error_with_original_error(self):
        """Test NATSConnectionError stores original error."""
        original = ValueError("Original error")
        error = NATSConnectionError("Connection failed", error=original)
        assert error.original_error is original

    def test_connection_error_with_all_parameters(self):
        """Test NATSConnectionError with all parameters."""
        original = ConnectionError("Network error")
        error = NATSConnectionError("Connection failed", url="nats://example.com:4222", error=original)
        assert str(error) == "Connection failed"
        assert error.url == "nats://example.com:4222"
        assert error.original_error is original


class TestNATSPublishError:
    """Test suite for NATSPublishError."""

    def test_publish_error_creation(self):
        """Test NATSPublishError can be created with message."""
        error = NATSPublishError("Publish failed")
        assert str(error) == "Publish failed"
        assert isinstance(error, NATSError)

    def test_publish_error_with_subject(self):
        """Test NATSPublishError stores subject."""
        error = NATSPublishError("Publish failed", subject="test.subject")
        assert error.subject == "test.subject"

    def test_publish_error_with_original_error(self):
        """Test NATSPublishError stores original error."""
        original = RuntimeError("Original error")
        error = NATSPublishError("Publish failed", error=original)
        assert error.original_error is original

    def test_publish_error_with_all_parameters(self):
        """Test NATSPublishError with all parameters."""
        original = ValueError("Network error")
        error = NATSPublishError("Publish failed", subject="game.events", error=original)
        assert str(error) == "Publish failed"
        assert error.subject == "game.events"
        assert error.original_error is original


class TestNATSSubscribeError:
    """Test suite for NATSSubscribeError."""

    def test_subscribe_error_creation(self):
        """Test NATSSubscribeError can be created with message."""
        error = NATSSubscribeError("Subscribe failed")
        assert str(error) == "Subscribe failed"
        assert isinstance(error, NATSError)

    def test_subscribe_error_with_subject(self):
        """Test NATSSubscribeError stores subject."""
        error = NATSSubscribeError("Subscribe failed", subject="test.subject")
        assert error.subject == "test.subject"

    def test_subscribe_error_with_original_error(self):
        """Test NATSSubscribeError stores original error."""
        original = KeyError("Original error")
        error = NATSSubscribeError("Subscribe failed", error=original)
        assert error.original_error is original

    def test_subscribe_error_with_all_parameters(self):
        """Test NATSSubscribeError with all parameters."""
        original = RuntimeError("Network error")
        error = NATSSubscribeError("Subscribe failed", subject="game.commands", error=original)
        assert str(error) == "Subscribe failed"
        assert error.subject == "game.commands"
        assert error.original_error is original


class TestNATSHealthCheckError:
    """Test suite for NATSHealthCheckError."""

    def test_health_check_error_creation(self):
        """Test NATSHealthCheckError can be created with message."""
        error = NATSHealthCheckError("Health check failed")
        assert str(error) == "Health check failed"
        assert isinstance(error, NATSError)

    def test_health_check_error_with_consecutive_failures(self):
        """Test NATSHealthCheckError stores consecutive failures count."""
        error = NATSHealthCheckError("Health check failed", consecutive_failures=5)
        assert error.consecutive_failures == 5

    def test_health_check_error_default_consecutive_failures(self):
        """Test NATSHealthCheckError defaults consecutive failures to 0."""
        error = NATSHealthCheckError("Health check failed")
        assert error.consecutive_failures == 0

    def test_health_check_error_with_high_failure_count(self):
        """Test NATSHealthCheckError with high failure count."""
        error = NATSHealthCheckError("Health check failed", consecutive_failures=100)
        assert error.consecutive_failures == 100


class TestExceptionHierarchy:
    """Test suite for exception hierarchy relationships."""

    def test_all_errors_inherit_from_nats_error(self):
        """Test all NATS exceptions inherit from NATSError."""
        connection_error = NATSConnectionError("Test")
        publish_error = NATSPublishError("Test")
        subscribe_error = NATSSubscribeError("Test")
        health_check_error = NATSHealthCheckError("Test")

        assert isinstance(connection_error, NATSError)
        assert isinstance(publish_error, NATSError)
        assert isinstance(subscribe_error, NATSError)
        assert isinstance(health_check_error, NATSError)

    def test_all_errors_inherit_from_exception(self):
        """Test all NATS exceptions inherit from Exception."""
        connection_error = NATSConnectionError("Test")
        publish_error = NATSPublishError("Test")
        subscribe_error = NATSSubscribeError("Test")
        health_check_error = NATSHealthCheckError("Test")

        assert isinstance(connection_error, Exception)
        assert isinstance(publish_error, Exception)
        assert isinstance(subscribe_error, Exception)
        assert isinstance(health_check_error, Exception)

    def test_exception_can_be_raised(self):
        """Test NATS exceptions can be raised and caught."""
        with pytest.raises(NATSConnectionError) as exc_info:
            raise NATSConnectionError("Test error")
        assert str(exc_info.value) == "Test error"

    def test_exception_can_be_caught_by_base(self):
        """Test NATS exceptions can be caught by NATSError."""
        with pytest.raises(NATSError):
            raise NATSPublishError("Test error")
