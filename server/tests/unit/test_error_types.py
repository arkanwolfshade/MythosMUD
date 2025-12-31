"""
Unit tests for error types and error response creation.

Tests the error type enums and error response creation functions.
"""

from datetime import UTC, datetime

from server.error_types import (
    ErrorMessages,
    ErrorSeverity,
    ErrorType,
    create_sse_error_response,
    create_standard_error_response,
    create_websocket_error_response,
)


def test_error_type_enum_values():
    """Test that ErrorType enum contains expected values."""
    assert ErrorType.AUTHENTICATION_FAILED.value == "authentication_failed"
    assert ErrorType.AUTHORIZATION_DENIED.value == "authorization_denied"
    assert ErrorType.VALIDATION_ERROR.value == "validation_error"
    assert ErrorType.RESOURCE_NOT_FOUND.value == "resource_not_found"
    assert ErrorType.DATABASE_ERROR.value == "database_error"
    assert ErrorType.WEBSOCKET_ERROR.value == "websocket_error"


def test_error_severity_enum_values():
    """Test that ErrorSeverity enum contains expected values."""
    assert ErrorSeverity.LOW.value == "low"
    assert ErrorSeverity.MEDIUM.value == "medium"
    assert ErrorSeverity.HIGH.value == "high"
    assert ErrorSeverity.CRITICAL.value == "critical"


def test_create_standard_error_response_basic():
    """Test create_standard_error_response with basic parameters."""
    response = create_standard_error_response(ErrorType.VALIDATION_ERROR, "Test error message")

    assert "error" in response
    error = response["error"]
    assert error["type"] == "validation_error"
    assert error["message"] == "Test error message"
    assert error["user_friendly"] == "Test error message"
    assert error["severity"] == "medium"
    assert "timestamp" in error
    assert isinstance(error["details"], dict)


def test_create_standard_error_response_with_user_friendly():
    """Test create_standard_error_response with user-friendly message."""
    response = create_standard_error_response(
        ErrorType.AUTHENTICATION_FAILED, "Technical error", user_friendly="Please log in again"
    )

    error = response["error"]
    assert error["message"] == "Technical error"
    assert error["user_friendly"] == "Please log in again"


def test_create_standard_error_response_with_details():
    """Test create_standard_error_response with additional details."""
    details = {"field": "username", "reason": "too short"}
    response = create_standard_error_response(ErrorType.INVALID_INPUT, "Validation failed", details=details)

    error = response["error"]
    assert error["details"] == details


def test_create_standard_error_response_with_severity():
    """Test create_standard_error_response with custom severity."""
    response = create_standard_error_response(ErrorType.SYSTEM_ERROR, "Critical error", severity=ErrorSeverity.CRITICAL)

    error = response["error"]
    assert error["severity"] == "critical"


def test_create_standard_error_response_timestamp():
    """Test that create_standard_error_response includes timestamp."""
    before = datetime.now(UTC)
    response = create_standard_error_response(ErrorType.INTERNAL_ERROR, "Error")
    after = datetime.now(UTC)

    timestamp_str = response["error"]["timestamp"]
    timestamp = datetime.fromisoformat(timestamp_str.replace("Z", "+00:00"))

    assert before <= timestamp <= after


def test_create_websocket_error_response_basic():
    """Test create_websocket_error_response with basic parameters."""
    response = create_websocket_error_response(ErrorType.WEBSOCKET_ERROR, "Connection failed")

    assert response["type"] == "error"
    assert response["error_type"] == "websocket_error"
    assert response["message"] == "Connection failed"
    assert response["user_friendly"] == "Connection failed"
    assert isinstance(response["details"], dict)


def test_create_websocket_error_response_with_user_friendly():
    """Test create_websocket_error_response with user-friendly message."""
    response = create_websocket_error_response(
        ErrorType.CONNECTION_ERROR, "Technical message", user_friendly="Unable to connect"
    )

    assert response["message"] == "Technical message"
    assert response["user_friendly"] == "Unable to connect"


def test_create_websocket_error_response_with_details():
    """Test create_websocket_error_response with additional details."""
    details = {"code": 1006, "reason": "abnormal closure"}
    response = create_websocket_error_response(ErrorType.WEBSOCKET_ERROR, "Connection closed", details=details)

    assert response["details"] == details


def test_create_sse_error_response_basic():
    """Test create_sse_error_response with basic parameters."""
    response = create_sse_error_response(ErrorType.SSE_ERROR, "SSE connection failed")

    assert response["type"] == "error"
    assert response["error_type"] == "sse_error"
    assert response["message"] == "SSE connection failed"
    assert response["user_friendly"] == "SSE connection failed"
    assert isinstance(response["details"], dict)


def test_create_sse_error_response_same_format_as_websocket():
    """Test that SSE error response has same format as WebSocket."""
    ws_response = create_websocket_error_response(ErrorType.WEBSOCKET_ERROR, "Test message")
    sse_response = create_sse_error_response(ErrorType.SSE_ERROR, "Test message")

    # Should have same structure (except error_type value)
    assert set(ws_response.keys()) == set(sse_response.keys())
    assert ws_response["type"] == sse_response["type"]
    assert ws_response["message"] == sse_response["message"]


def test_error_messages_class_attributes():
    """Test that ErrorMessages class has expected attributes."""
    assert ErrorMessages.AUTHENTICATION_REQUIRED == "Authentication required"
    assert ErrorMessages.INVALID_CREDENTIALS == "Invalid username or password"
    assert ErrorMessages.TOKEN_EXPIRED == "Your session has expired. Please log in again."
    assert ErrorMessages.INVALID_INPUT == "Invalid input provided"
    assert ErrorMessages.RESOURCE_NOT_FOUND == "Resource not found"
    assert ErrorMessages.PLAYER_NOT_FOUND == "Player not found"
    assert ErrorMessages.ROOM_NOT_FOUND == "Room not found"
    assert ErrorMessages.INVALID_COMMAND == "Invalid command"
    assert ErrorMessages.CONNECTION_ERROR == "Connection error occurred"
    assert ErrorMessages.INTERNAL_ERROR == "An internal error occurred"
    assert ErrorMessages.WEBSOCKET_ERROR == "WebSocket connection error"
    assert ErrorMessages.RATE_LIMIT_EXCEEDED == "Rate limit exceeded. Please slow down your requests."
