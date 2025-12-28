"""
Comprehensive unit tests for exceptions module.

Tests exception classes, ErrorContext, and utility functions.
"""

from datetime import datetime
from unittest.mock import patch

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
    handle_exception,
)


def test_error_context():
    """Test ErrorContext can be instantiated."""
    context = ErrorContext(
        user_id="user_001",
        room_id="room_001",
        command="look",
    )

    assert context.user_id == "user_001"
    assert context.room_id == "room_001"
    assert context.command == "look"
    assert context.session_id is None
    assert context.request_id is None
    assert isinstance(context.timestamp, datetime)
    assert context.metadata == {}


def test_error_context_to_dict():
    """Test ErrorContext.to_dict() converts to dictionary."""
    context = ErrorContext(
        user_id="user_001",
        room_id="room_001",
        command="look",
        metadata={"key": "value"},
    )

    result = context.to_dict()

    assert result["user_id"] == "user_001"
    assert result["room_id"] == "room_001"
    assert result["command"] == "look"
    assert result["metadata"] == {"key": "value"}
    assert "timestamp" in result


def test_logged_exception():
    """Test LoggedException can be instantiated."""
    exc = LoggedException("Test error")

    assert str(exc) == "Test error"
    assert exc.already_logged is False


def test_logged_exception_mark_logged():
    """Test LoggedException.mark_logged() marks as logged."""
    exc = LoggedException("Test error")
    exc.mark_logged()

    assert exc.already_logged is True


def test_logged_exception_already_logged():
    """Test LoggedException can be created with already_logged=True."""
    exc = LoggedException("Test error", already_logged=True)

    assert exc.already_logged is True


def test_mythosmud_error():
    """Test MythosMUDError can be instantiated."""
    with patch("server.exceptions.logger"):
        context = ErrorContext(user_id="user_001")
        error = MythosMUDError("Test error", context=context)

        assert error.message == "Test error"
        assert error.context == context
        assert error.user_friendly == "Test error"
        assert error.details == {}
        assert isinstance(error.timestamp, datetime)
        assert error.already_logged is True


def test_mythosmud_error_to_dict():
    """Test MythosMUDError.to_dict() converts to dictionary."""
    with patch("server.exceptions.logger"):
        context = ErrorContext(user_id="user_001")
        error = MythosMUDError("Test error", context=context, details={"key": "value"})

        result = error.to_dict()

        assert result["error_type"] == "MythosMUDError"
        assert result["message"] == "Test error"
        assert result["user_friendly"] == "Test error"
        assert result["details"] == {"key": "value"}
        assert "timestamp" in result
        assert "context" in result


def test_authentication_error():
    """Test AuthenticationError can be instantiated."""
    with patch("server.exceptions.logger"):
        error = AuthenticationError("Auth failed", auth_type="password")

        assert error.message == "Auth failed"
        assert error.auth_type == "password"
        assert error.details["auth_type"] == "password"


def test_database_error():
    """Test DatabaseError can be instantiated."""
    with patch("server.exceptions.logger"):
        error = DatabaseError("DB error", operation="select")

        assert error.message == "DB error"
        assert error.operation == "select"
        assert error.details["operation"] == "select"


def test_validation_error():
    """Test ValidationError can be instantiated."""
    with patch("server.exceptions.logger"):
        error = ValidationError("Validation failed", field="name")

        assert error.message == "Validation failed"
        assert error.field == "name"
        assert error.details["field"] == "name"


def test_game_logic_error():
    """Test GameLogicError can be instantiated."""
    with patch("server.exceptions.logger"):
        error = GameLogicError("Logic error", game_action="move")

        assert error.message == "Logic error"
        assert error.game_action == "move"
        assert error.details["game_action"] == "move"


def test_configuration_error():
    """Test ConfigurationError can be instantiated."""
    with patch("server.exceptions.logger"):
        error = ConfigurationError("Config error", config_key="database_url")

        assert error.message == "Config error"
        assert error.config_key == "database_url"
        assert error.details["config_key"] == "database_url"


def test_network_error():
    """Test NetworkError can be instantiated."""
    with patch("server.exceptions.logger"):
        error = NetworkError("Network error", connection_type="websocket")

        assert error.message == "Network error"
        assert error.connection_type == "websocket"
        assert error.details["connection_type"] == "websocket"


def test_resource_not_found_error():
    """Test ResourceNotFoundError can be instantiated."""
    with patch("server.exceptions.logger"):
        error = ResourceNotFoundError("Not found", resource_type="player", resource_id="player_001")

        assert error.message == "Not found"
        assert error.resource_type == "player"
        assert error.resource_id == "player_001"
        assert error.details["resource_type"] == "player"
        assert error.details["resource_id"] == "player_001"


def test_rate_limit_error():
    """Test RateLimitError can be instantiated."""
    with patch("server.exceptions.logger"):
        error = RateLimitError("Rate limit exceeded", limit_type="api", retry_after=60)

        assert error.message == "Rate limit exceeded"
        assert error.limit_type == "api"
        assert error.retry_after == 60
        assert error.details["limit_type"] == "api"
        assert error.details["retry_after"] == 60


def test_create_error_context():
    """Test create_error_context() creates context with kwargs."""
    context = create_error_context(user_id="user_001", room_id="room_001")

    assert context.user_id == "user_001"
    assert context.room_id == "room_001"


def test_logged_http_exception():
    """Test LoggedHTTPException can be instantiated."""
    with patch("server.exceptions.logger"):
        exc = LoggedHTTPException(status_code=404, detail="Not found")

        assert exc.status_code == 404
        assert exc.detail == "Not found"
        assert exc.already_logged is True


def test_handle_exception_mythosmud_error():
    """Test handle_exception() returns MythosMUDError as-is."""
    with patch("server.exceptions.logger"):
        error = MythosMUDError("Test error")
        result = handle_exception(error)

        assert result == error


def test_handle_exception_standard_exception():
    """Test handle_exception() wraps standard exception."""
    with patch("server.exceptions.logger"):
        exc = ValueError("Test error")
        context = ErrorContext(user_id="user_001")
        result = handle_exception(exc, context=context)

        assert isinstance(result, ValidationError)
        assert "Test error" in result.message
        assert result.context == context
