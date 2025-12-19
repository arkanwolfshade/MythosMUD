"""
Tests for Enhanced Error Logging utilities.

This module tests the enhanced error logging functions that provide structured
logging and context management for better error tracking and debugging.

AI Agent: Tests for enhanced error logging covering exception wrapping,
         HTTP error logging, and security event logging with structured context.
"""


# pylint: disable=redefined-outer-name
# Justification: pytest fixtures redefine names

from unittest.mock import Mock, patch

import pytest
from fastapi import HTTPException

from server.exceptions import (
    AuthenticationError,
    ConfigurationError,
    DatabaseError,
    ErrorContext,
    MythosMUDError,
    NetworkError,
    ValidationError,
    create_error_context,
)
from server.utils.enhanced_error_logging import (
    THIRD_PARTY_EXCEPTION_MAPPING,
    create_enhanced_error_context,
    log_and_raise_enhanced,
    log_and_raise_http_enhanced,
    log_performance_metric,
    log_security_event_enhanced,
    log_structured_error,
    wrap_third_party_exception_enhanced,
)


class TestThirdPartyExceptionMapping:
    """Test third-party exception mapping constant."""

    def test_mapping_exists(self) -> None:
        """Test THIRD_PARTY_EXCEPTION_MAPPING is properly defined."""
        assert isinstance(THIRD_PARTY_EXCEPTION_MAPPING, dict)
        assert len(THIRD_PARTY_EXCEPTION_MAPPING) > 0

    def test_database_exceptions_mapped(self) -> None:
        """Test database exceptions are mapped to DatabaseError."""
        assert THIRD_PARTY_EXCEPTION_MAPPING["asyncpg.exceptions.PostgresError"] == DatabaseError
        assert THIRD_PARTY_EXCEPTION_MAPPING["sqlalchemy.exc.OperationalError"] == DatabaseError

    def test_auth_exceptions_mapped(self) -> None:
        """Test authentication exceptions are mapped to AuthenticationError."""
        assert THIRD_PARTY_EXCEPTION_MAPPING["argon2.exceptions.HashingError"] == AuthenticationError

    def test_network_exceptions_mapped(self) -> None:
        """Test network exceptions are mapped to NetworkError."""
        assert THIRD_PARTY_EXCEPTION_MAPPING["httpx.RequestError"] == NetworkError

    def test_validation_exceptions_mapped(self) -> None:
        """Test validation exceptions are mapped to ValidationError."""
        assert THIRD_PARTY_EXCEPTION_MAPPING["pydantic.ValidationError"] == ValidationError

    def test_config_exceptions_mapped(self) -> None:
        """Test configuration exceptions are mapped to ConfigurationError."""
        assert THIRD_PARTY_EXCEPTION_MAPPING["yaml.YAMLError"] == ConfigurationError


class TestLogAndRaiseEnhanced:
    """Test log_and_raise_enhanced function."""

    def test_raises_specified_exception(self) -> None:
        """Test function raises the specified exception class."""
        with pytest.raises(ValidationError) as exc_info:
            log_and_raise_enhanced(ValidationError, "Test error")

        assert "Test error" in str(exc_info.value)

    def test_raises_with_user_friendly_message(self) -> None:
        """Test exception includes user-friendly message."""
        context = create_error_context()

        with pytest.raises(DatabaseError) as exc_info:
            log_and_raise_enhanced(
                DatabaseError, "Technical database error", context=context, user_friendly="Database is unavailable"
            )

        assert exc_info.value.user_friendly == "Database is unavailable"

    def test_raises_with_details(self) -> None:
        """Test exception includes details."""
        details = {"table": "users", "operation": "INSERT"}

        with pytest.raises(DatabaseError) as exc_info:
            log_and_raise_enhanced(DatabaseError, "Insert failed", details=details)

        assert exc_info.value.details == details

    def test_creates_context_when_none_provided(self) -> None:
        """Test function creates context if not provided."""
        with pytest.raises(MythosMUDError) as exc_info:
            log_and_raise_enhanced(MythosMUDError, "Test error")

        assert exc_info.value.context is not None
        assert isinstance(exc_info.value.context, ErrorContext)


class TestLogAndRaiseHttpEnhanced:
    """Test log_and_raise_http_enhanced function."""

    def test_raises_http_exception(self) -> None:
        """Test function raises HTTPException."""
        with pytest.raises(HTTPException) as exc_info:
            log_and_raise_http_enhanced(404, "Not found")

        assert exc_info.value.status_code == 404
        assert exc_info.value.detail == "Not found"

    def test_raises_http_exception_with_context(self) -> None:
        """Test HTTP exception logging includes context."""
        context = create_error_context(user_id="user123")

        with pytest.raises(HTTPException) as exc_info:
            log_and_raise_http_enhanced(403, "Forbidden", context=context)

        assert exc_info.value.status_code == 403

    def test_creates_context_when_none_provided(self) -> None:
        """Test creates context if not provided."""
        # Should not raise due to missing context
        with pytest.raises(HTTPException):
            log_and_raise_http_enhanced(500, "Internal error")


class TestLogStructuredError:
    """Test log_structured_error function."""

    @patch("server.utils.enhanced_error_logging.log_with_context")
    def test_logs_error_with_context(self, mock_log_with_context):
        """Test function logs error with structured context."""
        error = ValueError("Test error")
        context = create_error_context(user_id="user123")

        log_structured_error(error, context=context)

        mock_log_with_context.assert_called_once()
        call_kwargs = mock_log_with_context.call_args[1]
        assert call_kwargs["error_type"] == "ValueError"
        assert call_kwargs["error_message"] == "Test error"

    @patch("server.utils.enhanced_error_logging.log_with_context")
    def test_logs_error_without_context(self, mock_log_with_context):
        """Test function creates context if not provided."""
        error = RuntimeError("Test runtime error")

        log_structured_error(error)

        mock_log_with_context.assert_called_once()
        call_kwargs = mock_log_with_context.call_args[1]
        assert call_kwargs["error_type"] == "RuntimeError"

    @patch("server.utils.enhanced_error_logging.log_with_context")
    def test_logs_at_specified_level(self, mock_log_with_context):
        """Test function logs at specified level."""
        error = Warning("Test warning")

        log_structured_error(error, level="warning")

        mock_log_with_context.assert_called_once()
        # Verify level parameter was passed
        assert mock_log_with_context.call_args[0][1] == "warning"


class TestWrapThirdPartyException:
    """Test wrap_third_party_exception_enhanced function."""

    @patch("server.utils.enhanced_error_logging.log_with_context")
    def test_wraps_mapped_exception(self, _mock_log_with_context):
        """Test function wraps mapped third-party exceptions."""

        # Create a custom exception class to simulate asyncpg.PostgresError
        class PostgresError(Exception):
            __module__ = "asyncpg.exceptions"

        exc = PostgresError("Database connection failed")

        result = wrap_third_party_exception_enhanced(exc)

        assert isinstance(result, DatabaseError)
        assert "Third-party exception" in result.message
        assert "Database connection failed" in result.message

    @patch("server.utils.enhanced_error_logging.log_with_context")
    def test_wraps_unmapped_exception_as_generic(self, _mock_log_with_context):
        """Test unmapped exceptions become generic MythosMUDError."""
        exc = Exception("Unknown error")

        result = wrap_third_party_exception_enhanced(exc)

        assert isinstance(result, MythosMUDError)
        assert "Third-party exception" in result.message

    @patch("server.utils.enhanced_error_logging.log_with_context")
    def test_wraps_with_context(self, _mock_log_with_context):
        """Test wrapping includes provided context."""
        exc = Exception("Error with context")
        context = create_error_context(user_id="user123")

        result = wrap_third_party_exception_enhanced(exc, context=context)

        assert result.context == context


class TestCreateEnhancedErrorContext:
    """Test create_enhanced_error_context function."""

    def test_creates_context_with_request(self) -> None:
        """Test creating context with FastAPI request."""
        mock_request = Mock()
        mock_request.url = "http://localhost/api/test"
        mock_request.method = "GET"
        mock_request.headers = {"user-agent": "Test Agent"}
        mock_request.query_params = {"param": "value"}
        mock_request.client = Mock(host="127.0.0.1")

        context = create_enhanced_error_context(request=mock_request, user_id="user123")

        assert context.user_id == "user123"
        assert "path" in context.metadata
        assert context.metadata["method"] == "GET"

    def test_creates_context_with_websocket(self) -> None:
        """Test creating context with WebSocket connection."""
        mock_websocket = Mock()
        mock_websocket.url = "ws://localhost/ws"
        mock_websocket.headers = {"user-agent": "WS Client"}
        mock_websocket.query_params = {}
        mock_websocket.client = Mock(host="127.0.0.1")

        context = create_enhanced_error_context(websocket=mock_websocket, session_id="session123")

        assert context.session_id == "session123"
        assert context.metadata["connection_type"] == "websocket"

    def test_creates_context_without_request_or_websocket(self) -> None:
        """Test creating context without request or websocket."""
        context = create_enhanced_error_context(user_id="user123")

        assert context.user_id == "user123"
        assert context.metadata["path"] == "unknown"
        assert context.metadata["method"] == "unknown"

    def test_includes_additional_kwargs(self) -> None:
        """Test context includes additional kwargs in metadata."""
        context = create_enhanced_error_context(custom_field="custom_value", another_field=123)

        assert context.metadata["custom_field"] == "custom_value"
        assert context.metadata["another_field"] == 123


class TestLogPerformanceMetric:
    """Test log_performance_metric function."""

    @patch("server.utils.enhanced_error_logging.log_with_context")
    def test_logs_performance_metric(self, mock_log_with_context):
        """Test function logs performance metric with structured data."""
        log_performance_metric("database_query", 125.5, success=True)

        mock_log_with_context.assert_called_once()
        call_kwargs = mock_log_with_context.call_args[1]
        assert call_kwargs["metric_type"] == "performance"
        assert call_kwargs["operation"] == "database_query"
        assert call_kwargs["duration_ms"] == 125.5
        assert call_kwargs["success"] is True

    @patch("server.utils.enhanced_error_logging.log_with_context")
    def test_logs_failed_operation(self, mock_log_with_context):
        """Test logging failed operation."""
        log_performance_metric("api_call", 500.0, success=False)

        call_kwargs = mock_log_with_context.call_args[1]
        assert call_kwargs["success"] is False

    @patch("server.utils.enhanced_error_logging.log_with_context")
    def test_logs_with_context(self, mock_log_with_context):
        """Test logging with error context."""
        context = create_error_context(user_id="user123")

        log_performance_metric("operation", 100.0, context=context)

        call_kwargs = mock_log_with_context.call_args[1]
        assert "context" in call_kwargs


class TestLogSecurityEventEnhanced:
    """Test log_security_event_enhanced function."""

    @patch("server.utils.enhanced_error_logging.log_with_context")
    def test_logs_security_event(self, mock_log_with_context):
        """Test function logs security event with structured data."""
        log_security_event_enhanced("FAILED_LOGIN", severity="medium", user_id="user123")

        mock_log_with_context.assert_called_once()
        call_kwargs = mock_log_with_context.call_args[1]
        assert call_kwargs["event_type"] == "security_event"
        assert call_kwargs["security_event_type"] == "FAILED_LOGIN"
        assert call_kwargs["severity"] == "medium"
        assert call_kwargs["user_id"] == "user123"

    @patch("server.utils.enhanced_error_logging.log_with_context")
    def test_critical_severity_uses_critical_level(self, mock_log_with_context):
        """Test critical severity uses critical log level."""
        log_security_event_enhanced("INJECTION_ATTEMPT", severity="critical")

        # Verify critical level was used
        assert mock_log_with_context.call_args[0][1] == "critical"

    @patch("server.utils.enhanced_error_logging.log_with_context")
    def test_non_critical_severity_uses_warning_level(self, mock_log_with_context):
        """Test non-critical severity uses warning log level."""
        log_security_event_enhanced("SUSPICIOUS_ACTIVITY", severity="low")

        # Verify warning level was used
        assert mock_log_with_context.call_args[0][1] == "warning"

    @patch("server.utils.enhanced_error_logging.log_with_context")
    def test_logs_with_context(self, mock_log_with_context):
        """Test logging with error context."""
        context = create_error_context(session_id="session123")

        log_security_event_enhanced("ACCESS_DENIED", context=context)

        call_kwargs = mock_log_with_context.call_args[1]
        assert "context" in call_kwargs
