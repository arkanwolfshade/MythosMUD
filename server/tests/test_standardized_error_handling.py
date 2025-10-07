"""
Tests for standardized error handling and user-friendly messages.

This module tests the comprehensive error handling strategy to ensure
consistent error responses, proper user-friendly messages, and effective
error categorization across all application layers.
"""

from datetime import UTC, datetime

import pytest
from pydantic import ValidationError

from server.error_types import (
    ErrorMessages,
    ErrorSeverity,
    ErrorType,
    create_sse_error_response,
    create_standard_error_response,
    create_websocket_error_response,
)
from server.exceptions import (
    AuthenticationError,
    DatabaseError,
    GameLogicError,
    LoggedHTTPException,
    MythosMUDError,
    NetworkError,
    RateLimitError,
    ResourceNotFoundError,
    create_error_context,
)
from server.exceptions import (
    ValidationError as MythosValidationError,
)
from server.models.alias import Alias
from server.models.command import SayCommand


class TestStandardizedErrorHandling:
    """Test standardized error handling and user-friendly messages."""

    def test_error_type_enum_completeness(self):
        """Test that ErrorType enum covers all necessary error categories."""
        # Authentication and Authorization
        assert ErrorType.AUTHENTICATION_FAILED
        assert ErrorType.AUTHORIZATION_DENIED
        assert ErrorType.INVALID_TOKEN
        assert ErrorType.TOKEN_EXPIRED

        # Validation Errors
        assert ErrorType.VALIDATION_ERROR
        assert ErrorType.INVALID_INPUT
        assert ErrorType.MISSING_REQUIRED_FIELD
        assert ErrorType.INVALID_FORMAT

        # Resource Errors
        assert ErrorType.RESOURCE_NOT_FOUND
        assert ErrorType.RESOURCE_ALREADY_EXISTS
        assert ErrorType.RESOURCE_CONFLICT

        # Game Logic Errors
        assert ErrorType.GAME_LOGIC_ERROR
        assert ErrorType.INVALID_COMMAND
        assert ErrorType.INVALID_MOVEMENT
        assert ErrorType.PLAYER_NOT_IN_ROOM

        # Database Errors
        assert ErrorType.DATABASE_ERROR
        assert ErrorType.DATABASE_CONNECTION_ERROR
        assert ErrorType.DATABASE_QUERY_ERROR

        # Network and Communication
        assert ErrorType.NETWORK_ERROR
        assert ErrorType.CONNECTION_ERROR
        assert ErrorType.TIMEOUT_ERROR

        # Rate Limiting
        assert ErrorType.RATE_LIMIT_EXCEEDED
        assert ErrorType.TOO_MANY_REQUESTS

        # Configuration and System
        assert ErrorType.CONFIGURATION_ERROR
        assert ErrorType.SYSTEM_ERROR
        assert ErrorType.INTERNAL_ERROR

        # Real-time Communication
        assert ErrorType.WEBSOCKET_ERROR
        assert ErrorType.SSE_ERROR
        assert ErrorType.MESSAGE_PROCESSING_ERROR

    def test_error_severity_enum_completeness(self):
        """Test that ErrorSeverity enum covers all necessary severity levels."""
        assert ErrorSeverity.LOW
        assert ErrorSeverity.MEDIUM
        assert ErrorSeverity.HIGH
        assert ErrorSeverity.CRITICAL

        # Test severity ordering
        severities = [ErrorSeverity.LOW, ErrorSeverity.MEDIUM, ErrorSeverity.HIGH, ErrorSeverity.CRITICAL]
        assert len(set(severities)) == 4  # All unique

    def test_standard_error_response_creation(self):
        """Test creation of standardized error responses."""
        error_response = create_standard_error_response(
            error_type=ErrorType.VALIDATION_ERROR,
            message="Test validation error",
            user_friendly="Please check your input",
            details={"field": "test_field"},
            severity=ErrorSeverity.MEDIUM,
        )

        assert "error" in error_response
        error = error_response["error"]

        assert error["type"] == "validation_error"
        assert error["message"] == "Test validation error"
        assert error["user_friendly"] == "Please check your input"
        assert error["details"] == {"field": "test_field"}
        assert error["severity"] == "medium"
        assert "timestamp" in error

    def test_websocket_error_response_creation(self):
        """Test creation of WebSocket error responses."""
        error_response = create_websocket_error_response(
            error_type=ErrorType.WEBSOCKET_ERROR,
            message="Connection lost",
            user_friendly="Your connection was lost. Please reconnect.",
            details={"reconnect_url": "/ws"},
        )

        assert error_response["type"] == "error"
        assert error_response["error_type"] == "websocket_error"
        assert error_response["message"] == "Connection lost"
        assert error_response["user_friendly"] == "Your connection was lost. Please reconnect."
        assert error_response["details"] == {"reconnect_url": "/ws"}

    def test_sse_error_response_creation(self):
        """Test creation of SSE error responses."""
        error_response = create_sse_error_response(
            error_type=ErrorType.SSE_ERROR,
            message="SSE connection failed",
            user_friendly="Real-time updates unavailable",
            details={"retry_after": 30},
        )

        assert error_response["type"] == "error"
        assert error_response["error_type"] == "sse_error"
        assert error_response["message"] == "SSE connection failed"
        assert error_response["user_friendly"] == "Real-time updates unavailable"
        assert error_response["details"] == {"retry_after": 30}

    def test_error_messages_consistency(self):
        """Test that ErrorMessages class provides consistent user-friendly messages."""
        # Authentication messages
        assert ErrorMessages.AUTHENTICATION_REQUIRED == "Authentication required"
        assert ErrorMessages.INVALID_CREDENTIALS == "Invalid username or password"
        assert ErrorMessages.TOKEN_EXPIRED == "Your session has expired. Please log in again."

        # Validation messages
        assert ErrorMessages.INVALID_INPUT == "Invalid input provided"
        assert ErrorMessages.MISSING_REQUIRED_FIELD == "Required field is missing"
        assert ErrorMessages.INVALID_FORMAT == "Invalid format provided"

        # Resource messages
        assert ErrorMessages.RESOURCE_NOT_FOUND == "Resource not found"
        assert ErrorMessages.PLAYER_NOT_FOUND == "Player not found"
        assert ErrorMessages.ROOM_NOT_FOUND == "Room not found"

        # Game logic messages
        assert ErrorMessages.INVALID_COMMAND == "Invalid command"
        assert ErrorMessages.INVALID_MOVEMENT == "You cannot move in that direction"
        assert ErrorMessages.PLAYER_NOT_IN_ROOM == "Player is not in the specified room"

        # System messages
        assert ErrorMessages.INTERNAL_ERROR == "An internal error occurred"
        assert ErrorMessages.TOO_MANY_REQUESTS == "Too many requests. Please try again later."

    def test_mythos_mud_error_creation(self):
        """Test creation and properties of MythosMUDError."""
        context = create_error_context(user_id="test_user", session_id="test_session", request_id="test_request")

        error = MythosMUDError(
            message="Test error message",
            context=context,
            details={"test_detail": "value"},
            user_friendly="User-friendly message",
        )

        assert error.message == "Test error message"
        assert error.user_friendly == "User-friendly message"
        assert error.details == {"test_detail": "value"}
        assert error.context == context
        assert isinstance(error.timestamp, datetime)

        # Test to_dict conversion
        error_dict = error.to_dict()
        assert error_dict["message"] == "Test error message"
        assert error_dict["user_friendly"] == "User-friendly message"
        assert error_dict["details"] == {"test_detail": "value"}
        assert "timestamp" in error_dict

    def test_error_context_creation(self):
        """Test creation and properties of ErrorContext."""
        context = create_error_context(
            user_id="test_user", session_id="test_session", request_id="test_request", metadata={"additional": "info"}
        )

        assert context.user_id == "test_user"
        assert context.session_id == "test_session"
        assert context.request_id == "test_request"
        assert context.metadata == {"additional": "info"}
        assert isinstance(context.timestamp, datetime)

        # Test to_dict conversion
        context_dict = context.to_dict()
        assert context_dict["user_id"] == "test_user"
        assert context_dict["session_id"] == "test_session"
        assert context_dict["request_id"] == "test_request"
        assert context_dict["metadata"] == {"additional": "info"}
        assert "timestamp" in context_dict

    def test_specific_error_types_inheritance(self):
        """Test that specific error types properly inherit from MythosMUDError."""
        # Test ValidationError
        validation_error = MythosValidationError("Validation failed")
        assert isinstance(validation_error, MythosMUDError)
        assert validation_error.message == "Validation failed"

        # Test AuthenticationError
        auth_error = AuthenticationError("Authentication failed")
        assert isinstance(auth_error, MythosMUDError)
        assert auth_error.message == "Authentication failed"

        # Test GameLogicError
        game_error = GameLogicError("Invalid game action")
        assert isinstance(game_error, MythosMUDError)
        assert game_error.message == "Invalid game action"

        # Test DatabaseError
        db_error = DatabaseError("Database operation failed")
        assert isinstance(db_error, MythosMUDError)
        assert db_error.message == "Database operation failed"

        # Test NetworkError
        network_error = NetworkError("Network connection failed")
        assert isinstance(network_error, MythosMUDError)
        assert network_error.message == "Network connection failed"

        # Test RateLimitError
        rate_error = RateLimitError("Rate limit exceeded")
        assert isinstance(rate_error, MythosMUDError)
        assert rate_error.message == "Rate limit exceeded"

        # Test ResourceNotFoundError
        resource_error = ResourceNotFoundError("Resource not found")
        assert isinstance(resource_error, MythosMUDError)
        assert resource_error.message == "Resource not found"

    def test_logged_http_exception_creation(self):
        """Test creation and properties of LoggedHTTPException."""
        context = create_error_context(user_id="test_user")

        http_exception = LoggedHTTPException(
            status_code=400, detail="Bad request", context=context, logger_name="test_logger"
        )

        assert http_exception.status_code == 400
        assert http_exception.detail == "Bad request"
        # Note: LoggedHTTPException doesn't store context as attribute, it just logs it

    def test_pydantic_validation_error_handling(self):
        """Test handling of Pydantic ValidationError with user-friendly messages."""
        # Test SayCommand validation error - missing required field
        with pytest.raises(ValidationError) as exc_info:
            SayCommand()  # Missing required message field should fail validation

        validation_error = exc_info.value
        assert isinstance(validation_error, ValidationError)

        # Test SayCommand with invalid message (empty string)
        with pytest.raises(ValidationError) as exc_info:
            SayCommand(message="")  # Empty message should fail validation

        validation_error = exc_info.value
        assert isinstance(validation_error, ValidationError)

        # Test Alias validation error - missing required fields
        with pytest.raises(ValidationError) as exc_info:
            Alias()  # Missing required name and command fields should fail validation

        validation_error = exc_info.value
        assert isinstance(validation_error, ValidationError)

        # Test Alias with invalid data types
        with pytest.raises(ValidationError) as exc_info:
            Alias(name=123, command=456)  # Wrong data types should fail validation

        validation_error = exc_info.value
        assert isinstance(validation_error, ValidationError)

    def test_error_response_format_consistency(self):
        """Test that all error response formats are consistent."""
        # Standard HTTP error response
        http_response = create_standard_error_response(ErrorType.VALIDATION_ERROR, "Test message", "Test user friendly")

        # WebSocket error response
        ws_response = create_websocket_error_response(ErrorType.WEBSOCKET_ERROR, "Test message", "Test user friendly")

        # SSE error response
        sse_response = create_sse_error_response(ErrorType.SSE_ERROR, "Test message", "Test user friendly")

        # All should have consistent fields
        assert "message" in http_response["error"]
        assert "user_friendly" in http_response["error"]

        assert "message" in ws_response
        assert "user_friendly" in ws_response

        assert "message" in sse_response
        assert "user_friendly" in sse_response

    def test_error_severity_mapping(self):
        """Test that error severities are properly mapped to appropriate types."""
        # Critical errors
        critical_errors = [ErrorType.SYSTEM_ERROR, ErrorType.DATABASE_CONNECTION_ERROR, ErrorType.INTERNAL_ERROR]

        # High severity errors
        high_errors = [ErrorType.AUTHENTICATION_FAILED, ErrorType.DATABASE_ERROR, ErrorType.CONFIGURATION_ERROR]

        # Medium severity errors
        medium_errors = [ErrorType.VALIDATION_ERROR, ErrorType.RESOURCE_NOT_FOUND, ErrorType.GAME_LOGIC_ERROR]

        # Low severity errors
        low_errors = [ErrorType.INVALID_FORMAT, ErrorType.TIMEOUT_ERROR]

        # Test that we can categorize errors appropriately
        for error_type in critical_errors:
            response = create_standard_error_response(
                error_type=error_type, message="Test", severity=ErrorSeverity.CRITICAL
            )
            assert response["error"]["severity"] == "critical"

        for error_type in high_errors:
            response = create_standard_error_response(
                error_type=error_type, message="Test", severity=ErrorSeverity.HIGH
            )
            assert response["error"]["severity"] == "high"

        for error_type in medium_errors:
            response = create_standard_error_response(
                error_type=error_type, message="Test", severity=ErrorSeverity.MEDIUM
            )
            assert response["error"]["severity"] == "medium"

        for error_type in low_errors:
            response = create_standard_error_response(error_type=error_type, message="Test", severity=ErrorSeverity.LOW)
            assert response["error"]["severity"] == "low"

    def test_user_friendly_message_generation(self):
        """Test that user-friendly messages are generated appropriately."""
        # Test that technical messages are converted to user-friendly ones
        technical_message = "ValidationError: field 'message' is required"
        user_friendly = "Please provide a message"

        response = create_standard_error_response(ErrorType.VALIDATION_ERROR, technical_message, user_friendly)

        assert response["error"]["message"] == technical_message
        assert response["error"]["user_friendly"] == user_friendly

    def test_error_context_metadata_handling(self):
        """Test that error context metadata is properly handled."""
        metadata = {
            "request_path": "/api/test",
            "user_agent": "test-agent",
            "ip_address": "127.0.0.1",
            "request_method": "POST",
        }

        context = create_error_context(user_id="test_user", metadata=metadata)

        error = MythosMUDError("Test error", context=context, details={"additional": "info"})

        error_dict = error.to_dict()
        assert error_dict["context"]["metadata"] == metadata
        assert error_dict["details"] == {"additional": "info"}

    def test_timestamp_consistency(self):
        """Test that timestamps are consistent across error responses."""
        before = datetime.now(UTC)

        response1 = create_standard_error_response(ErrorType.VALIDATION_ERROR, "Test message 1")

        response2 = create_standard_error_response(ErrorType.VALIDATION_ERROR, "Test message 2")

        after = datetime.now(UTC)

        # Parse timestamps
        timestamp1 = datetime.fromisoformat(response1["error"]["timestamp"].replace("Z", "+00:00"))
        timestamp2 = datetime.fromisoformat(response2["error"]["timestamp"].replace("Z", "+00:00"))

        # Timestamps should be between before and after
        assert before <= timestamp1 <= after
        assert before <= timestamp2 <= after

        # Timestamps should be close to each other
        time_diff = abs((timestamp2 - timestamp1).total_seconds())
        assert time_diff < 1.0  # Less than 1 second difference
