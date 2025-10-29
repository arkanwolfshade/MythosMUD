"""
Tests for enhanced logging configuration.
"""

from unittest.mock import Mock, patch

from server.logging.enhanced_logging_config import (
    add_correlation_id,
    add_request_context,
    bind_request_context,
    clear_request_context,
    get_current_context,
    get_enhanced_logger,
    sanitize_sensitive_data,
)


class TestEnhancedLoggingConfig:
    """Test enhanced logging configuration functionality."""

    def test_sanitize_sensitive_data(self):
        """Test that sensitive data is properly sanitized."""
        # Test data with sensitive information
        event_dict = {
            "user_id": "123",
            "password": "secret123",
            "token": "abc123",
            "api_key": "key456",
            "normal_field": "value",
        }

        result = sanitize_sensitive_data(None, None, event_dict)

        # Sensitive data should be redacted
        assert result["password"] == "[REDACTED]"
        assert result["token"] == "[REDACTED]"
        assert result["api_key"] == "[REDACTED]"

        # Normal data should remain unchanged
        assert result["user_id"] == "123"
        assert result["normal_field"] == "value"

    def test_sanitize_sensitive_data_case_insensitive(self):
        """Test that sensitive data sanitization is case insensitive."""
        event_dict = {
            "Password": "secret123",
            "API_KEY": "key456",
            "Secret": "hidden",
        }

        result = sanitize_sensitive_data(None, None, event_dict)

        assert result["Password"] == "[REDACTED]"
        assert result["API_KEY"] == "[REDACTED]"
        assert result["Secret"] == "[REDACTED]"

    def test_add_correlation_id(self):
        """Test that correlation IDs are added correctly."""
        event_dict = {"message": "test"}

        result = add_correlation_id(None, None, event_dict)

        assert "correlation_id" in result
        assert result["correlation_id"] is not None

    def test_add_request_context(self):
        """Test that request context is added correctly."""
        event_dict = {"message": "test"}

        result = add_request_context(None, None, event_dict)

        assert "request_id" in result
        assert result["request_id"] is not None

    @patch("server.logging.enhanced_logging_config.get_logger")
    @patch("server.logging.enhanced_logging_config.structlog.wrap_logger")
    def test_get_enhanced_logger(self, mock_wrap_logger, mock_get_logger):
        """Test that get_enhanced_logger returns an enhanced logger instance."""
        mock_base_logger = Mock()
        mock_enhanced_logger = Mock()
        mock_get_logger.return_value = mock_base_logger
        mock_wrap_logger.return_value = mock_enhanced_logger

        result = get_enhanced_logger("test")

        assert result == mock_enhanced_logger
        mock_get_logger.assert_called_once_with("test")
        mock_wrap_logger.assert_called_once_with(mock_base_logger)

    @patch("server.logging.enhanced_logging_config.bind_contextvars")
    def test_bind_request_context(self, mock_bind_contextvars):
        """Test that request context is bound correctly."""
        correlation_id = "test-correlation-id"
        user_id = "test-user-id"

        bind_request_context(correlation_id=correlation_id, user_id=user_id)

        mock_bind_contextvars.assert_called_once_with(correlation_id=correlation_id, user_id=user_id)

    def test_clear_request_context(self):
        """Test that request context is cleared correctly."""
        # This should not raise an exception
        clear_request_context()

    def test_get_current_context(self):
        """Test that current context is retrieved correctly."""
        context = get_current_context()
        assert isinstance(context, dict)
