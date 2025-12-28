"""
Unit tests for exception classes and error handling.

Tests the exception hierarchy and error context handling.
"""

from datetime import datetime
from unittest.mock import patch

from fastapi import HTTPException

from server.exceptions import (
    AuthenticationError,
    ConfigurationError,
    DatabaseError,
    ErrorContext,
    GameLogicError,
    LoggedException,
    LoggedHTTPException,
    MythosMUDError,
    NetworkError,
    RateLimitError,
    ResourceNotFoundError,
    ValidationError,
    create_error_context,
)


def test_error_context_initialization():
    """Test ErrorContext initialization with default values."""
    context = ErrorContext()
    assert context.user_id is None
    assert context.room_id is None
    assert context.command is None
    assert context.session_id is None
    assert context.request_id is None
    assert isinstance(context.timestamp, datetime)
    assert isinstance(context.metadata, dict)
    assert len(context.metadata) == 0


def test_error_context_with_values():
    """Test ErrorContext initialization with specific values."""
    context = ErrorContext(
        user_id="user123",
        room_id="room456",
        command="look",
        session_id="session789",
        request_id="req001",
        metadata={"key": "value"},
    )
    assert context.user_id == "user123"
    assert context.room_id == "room456"
    assert context.command == "look"
    assert context.session_id == "session789"
    assert context.request_id == "req001"
    assert context.metadata == {"key": "value"}


def test_error_context_to_dict():
    """Test ErrorContext.to_dict() conversion."""
    context = ErrorContext(user_id="user123", room_id="room456", command="look")
    result = context.to_dict()

    assert result["user_id"] == "user123"
    assert result["room_id"] == "room456"
    assert result["command"] == "look"
    assert "timestamp" in result
    assert isinstance(result["timestamp"], str)
    assert isinstance(result["metadata"], dict)


def test_logged_exception_initialization():
    """Test LoggedException initialization."""
    exc = LoggedException("Test error")
    assert str(exc) == "Test error"
    assert exc.already_logged is False


def test_logged_exception_already_logged():
    """Test LoggedException with already_logged flag."""
    exc = LoggedException("Test error", already_logged=True)
    assert exc.already_logged is True


def test_logged_exception_mark_logged():
    """Test LoggedException.mark_logged() method."""
    exc = LoggedException("Test error")
    assert exc.already_logged is False
    exc.mark_logged()
    assert exc.already_logged is True


def test_mythos_mud_error_initialization():
    """Test MythosMUDError initialization."""
    with patch("server.exceptions.logger") as mock_logger:
        error = MythosMUDError("Test error message")

        assert error.message == "Test error message"
        assert error.user_friendly == "Test error message"
        assert isinstance(error.context, ErrorContext)
        assert isinstance(error.details, dict)
        assert isinstance(error.timestamp, datetime)
        assert error.already_logged is True
        mock_logger.error.assert_called_once()


def test_mythos_mud_error_with_context():
    """Test MythosMUDError with custom context."""
    context = ErrorContext(user_id="user123", room_id="room456")
    with patch("server.exceptions.logger"):
        error = MythosMUDError("Test error", context=context)

        assert error.context.user_id == "user123"
        assert error.context.room_id == "room456"


def test_mythos_mud_error_with_details():
    """Test MythosMUDError with additional details."""
    details = {"field": "username", "reason": "invalid"}
    with patch("server.exceptions.logger"):
        error = MythosMUDError("Validation failed", details=details)

        assert error.details == details


def test_mythos_mud_error_with_user_friendly():
    """Test MythosMUDError with user-friendly message."""
    with patch("server.exceptions.logger"):
        error = MythosMUDError("Technical error", user_friendly="Something went wrong")

        assert error.message == "Technical error"
        assert error.user_friendly == "Something went wrong"


def test_mythos_mud_error_to_dict():
    """Test MythosMUDError.to_dict() conversion."""
    context = ErrorContext(user_id="user123", command="look")
    with patch("server.exceptions.logger"):
        error = MythosMUDError("Test error", context=context, details={"key": "value"})
        result = error.to_dict()

        assert result["error_type"] == "MythosMUDError"
        assert result["message"] == "Test error"
        assert result["user_friendly"] == "Test error"
        assert "context" in result
        assert result["details"] == {"key": "value"}
        assert "timestamp" in result


def test_authentication_error_initialization():
    """Test AuthenticationError initialization."""
    with patch("server.exceptions.logger"):
        error = AuthenticationError("Auth failed", auth_type="password")

        assert error.message == "Auth failed"
        assert error.auth_type == "password"
        assert error.details["auth_type"] == "password"


def test_database_error_initialization():
    """Test DatabaseError initialization."""
    with patch("server.exceptions.logger"):
        error = DatabaseError("DB error", operation="SELECT", table="players")

        assert error.message == "DB error"
        assert error.operation == "SELECT"
        assert error.table == "players"
        assert error.details["operation"] == "SELECT"
        assert error.details["table"] == "players"


def test_database_error_without_table():
    """Test DatabaseError without table specified."""
    with patch("server.exceptions.logger"):
        error = DatabaseError("DB error", operation="INSERT")

        assert error.operation == "INSERT"
        assert error.table is None
        assert "table" not in error.details


def test_validation_error_initialization():
    """Test ValidationError initialization."""
    with patch("server.exceptions.logger"):
        error = ValidationError("Invalid input", field="username", value="test")

        assert error.message == "Invalid input"
        assert error.field == "username"
        assert error.value == "test"
        assert error.details["field"] == "username"
        assert error.details["value"] == "test"


def test_validation_error_without_field():
    """Test ValidationError without field specified."""
    with patch("server.exceptions.logger"):
        error = ValidationError("Invalid input")

        assert error.field is None
        assert error.value is None
        assert "field" not in error.details


def test_game_logic_error_initialization():
    """Test GameLogicError initialization."""
    with patch("server.exceptions.logger"):
        error = GameLogicError("Invalid move", game_action="go north")

        assert error.message == "Invalid move"
        assert error.game_action == "go north"
        assert error.details["game_action"] == "go north"


def test_configuration_error_initialization():
    """Test ConfigurationError initialization."""
    with patch("server.exceptions.logger"):
        error = ConfigurationError("Config error", config_key="database.url")

        assert error.message == "Config error"
        assert error.config_key == "database.url"
        assert error.details["config_key"] == "database.url"


def test_network_error_initialization():
    """Test NetworkError initialization."""
    with patch("server.exceptions.logger"):
        error = NetworkError("Connection failed", connection_type="websocket")

        assert error.message == "Connection failed"
        assert error.connection_type == "websocket"
        assert error.details["connection_type"] == "websocket"


def test_network_error_default_connection_type():
    """Test NetworkError with default connection type."""
    with patch("server.exceptions.logger"):
        error = NetworkError("Connection failed")

        assert error.connection_type == "unknown"
        assert error.details["connection_type"] == "unknown"


def test_resource_not_found_error_initialization():
    """Test ResourceNotFoundError initialization."""
    with patch("server.exceptions.logger"):
        error = ResourceNotFoundError("Not found", resource_type="player", resource_id="player123")

        assert error.message == "Not found"
        assert error.resource_type == "player"
        assert error.resource_id == "player123"
        assert error.details["resource_type"] == "player"
        assert error.details["resource_id"] == "player123"


def test_resource_not_found_error_partial():
    """Test ResourceNotFoundError with partial information."""
    with patch("server.exceptions.logger"):
        error = ResourceNotFoundError("Not found", resource_type="player")

        assert error.resource_type == "player"
        assert error.resource_id is None
        assert "resource_id" not in error.details


def test_rate_limit_error_initialization():
    """Test RateLimitError initialization."""
    with patch("server.exceptions.logger"):
        error = RateLimitError("Rate limited", limit_type="command", retry_after=60)

        assert error.message == "Rate limited"
        assert error.limit_type == "command"
        assert error.retry_after == 60
        assert error.details["limit_type"] == "command"
        assert error.details["retry_after"] == 60


def test_rate_limit_error_without_retry_after():
    """Test RateLimitError without retry_after."""
    with patch("server.exceptions.logger"):
        error = RateLimitError("Rate limited", limit_type="command")

        assert error.retry_after is None
        assert "retry_after" not in error.details


def test_create_error_context():
    """Test create_error_context helper function."""
    context = create_error_context(user_id="user123", room_id="room456", command="look")

    assert isinstance(context, ErrorContext)
    assert context.user_id == "user123"
    assert context.room_id == "room456"
    assert context.command == "look"


def test_logged_http_exception_initialization():
    """Test LoggedHTTPException initialization."""
    with patch("server.exceptions.logger") as mock_logger:
        exc = LoggedHTTPException(status_code=404, detail="Not found", context=ErrorContext(user_id="user123"))

        assert exc.status_code == 404
        assert exc.detail == "Not found"
        assert isinstance(exc, HTTPException)
        assert isinstance(exc, LoggedException)
        mock_logger.warning.assert_called_once()


def test_logged_http_exception_with_logger_name():
    """Test LoggedHTTPException with custom logger name."""
    with patch("server.exceptions.get_logger") as mock_get_logger:
        mock_logger = mock_get_logger.return_value
        exc = LoggedHTTPException(status_code=500, detail="Server error", logger_name="custom.logger")

        assert exc.status_code == 500
        mock_get_logger.assert_called_once_with("custom.logger")
        mock_logger.warning.assert_called_once()


def test_logged_http_exception_inheritance():
    """Test that LoggedHTTPException inherits from both classes."""
    with patch("server.exceptions.logger"):
        exc = LoggedHTTPException(status_code=400, detail="Bad request")

        assert isinstance(exc, HTTPException)
        assert isinstance(exc, LoggedException)
        # Should be able to use HTTPException methods
        assert hasattr(exc, "status_code")
        assert hasattr(exc, "detail")
        # Should be able to use LoggedException methods
        assert hasattr(exc, "mark_logged")
        assert hasattr(exc, "already_logged")
