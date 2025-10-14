"""
Tests for error handling and sanitization in MythosMUD.

These tests verify that error responses properly sanitize sensitive information
and prevent stack trace exposure to users.
"""

from datetime import UTC, datetime
from unittest.mock import Mock, patch

import pytest
from fastapi import FastAPI, Request
from fastapi.testclient import TestClient
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
    ConfigurationError,
    DatabaseError,
    ErrorContext,
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
from server.legacy_error_handlers import (
    ErrorResponse,
    _is_safe_detail_key,
    _sanitize_context,
    _sanitize_detail_value,
    create_error_response,
    general_exception_handler,
    mythos_exception_handler,
    sanitize_html_content,
    sanitize_text_content,
)
from server.models.alias import Alias
from server.models.command import SayCommand


class TestErrorSanitization:
    """Test error sanitization functions."""

    def test_safe_detail_keys(self):
        """Test that safe detail keys are allowed."""
        safe_keys = [
            "auth_type",
            "operation",
            "table",
            "field",
            "value",
            "game_action",
            "config_key",
            "connection_type",
            "resource_type",
            "resource_id",
            "limit_type",
            "retry_after",
        ]

        for key in safe_keys:
            assert _is_safe_detail_key(key), f"Key '{key}' should be safe"

    def test_unsafe_detail_keys(self):
        """Test that unsafe detail keys are blocked."""
        unsafe_keys = [
            "password",
            "secret_key",
            "api_token",
            "credentials",
            "file_path",
            "sql_query",
            "stack_trace",
            "debug_info",
            "internal_data",
            "sensitive_info",
            "private_key",
        ]

        for key in unsafe_keys:
            assert not _is_safe_detail_key(key), f"Key '{key}' should be unsafe"

    def test_sanitize_string_values(self):
        """Test that string values are properly sanitized."""
        # Safe strings should pass through
        assert _sanitize_detail_value("normal message") == "normal message"
        assert _sanitize_detail_value("auth_type") == "auth_type"

        # Strings with sensitive patterns should be redacted
        assert _sanitize_detail_value("File: /etc/passwd") == "[REDACTED]"
        assert _sanitize_detail_value("Traceback (most recent call last):") == "[REDACTED]"
        # "line" is not in our sensitive patterns, so it should pass through
        # Note: bleach removes HTML tags, so <module> becomes just the text
        assert _sanitize_detail_value("line 42 in <module>") == "line 42 in "
        assert _sanitize_detail_value("C:\\Users\\admin\\secret.txt") == "[REDACTED]"

    def test_sanitize_dict_values(self):
        """Test that dictionary values are properly sanitized."""
        test_dict = {
            "operation": "safe_value",
            "password": "secret123",
            "file_path": "/etc/passwd",
            "field": "normal_value",
        }

        sanitized = _sanitize_detail_value(test_dict)

        # Only safe keys should be included (operation and field are in safe_keys)
        assert "operation" in sanitized
        assert "field" in sanitized

        # Unsafe keys should be excluded
        assert "password" not in sanitized
        assert "file_path" not in sanitized

    def test_sanitize_context(self):
        """Test that error context is properly sanitized."""
        context = ErrorContext(
            user_id="user123",
            room_id="room456",
            command="look",
            session_id="session789",
            request_id="req123",
            metadata={"safe_meta": "safe_value", "password": "secret123", "file_path": "/etc/passwd"},
        )

        sanitized = _sanitize_context(context)

        # Safe fields should be included
        assert sanitized["user_id"] == "user123"
        assert sanitized["room_id"] == "room456"
        assert sanitized["command"] == "look"
        assert sanitized["session_id"] == "session789"
        assert sanitized["request_id"] == "req123"

        # Metadata should be sanitized
        assert "safe_meta" in sanitized["metadata"]
        assert "password" not in sanitized["metadata"]
        assert "file_path" not in sanitized["metadata"]


class TestErrorResponseCreation:
    """Test error response creation with sanitization."""

    def test_create_error_response_without_details(self):
        """Test error response creation without detailed information."""
        error = MythosValidationError(
            message="Invalid input", context=ErrorContext(user_id="user123"), field="username", value="invalid@#$%"
        )

        response = create_error_response(error, include_details=False)

        # Should not include details
        assert response.details == {}
        assert response.error_type.value == "validation_error"
        assert response.message == "Invalid input"

    def test_create_error_response_with_safe_details(self):
        """Test error response creation with safe detailed information."""
        error = MythosValidationError(
            message="Invalid input", context=ErrorContext(user_id="user123"), field="username", value="invalid@#$%"
        )

        response = create_error_response(error, include_details=True)

        # Should include safe details
        assert "field" in response.details
        assert "value" in response.details
        assert "context" in response.details
        assert response.details["field"] == "username"
        assert response.details["value"] == "invalid@#$%"

    def test_create_error_response_with_unsafe_details(self):
        """Test error response creation with unsafe detailed information."""
        error = DatabaseError(
            message="Database error",
            context=ErrorContext(user_id="user123"),
            operation="SELECT",
            table="users",
            details={
                "sql_query": "SELECT * FROM users WHERE password = 'secret123'",
                "file_path": "/etc/database.conf",
                "stack_trace": "Traceback (most recent call last):",
                "safe_field": "safe_value",
            },
        )

        response = create_error_response(error, include_details=True)

        # Should only include safe details
        assert "safe_field" in response.details
        assert response.details["safe_field"] == "safe_value"

        # Unsafe details should be excluded
        assert "sql_query" not in response.details
        assert "file_path" not in response.details
        assert "stack_trace" not in response.details

    def test_create_error_response_with_sensitive_context(self):
        """Test error response creation with sensitive context information."""
        context = ErrorContext(
            user_id="user123",
            metadata={
                "password": "secret123",
                "api_key": "sk-1234567890abcdef",
                "file_path": "/etc/passwd",
                "safe_meta": "safe_value",
            },
        )

        error = MythosMUDError(
            message="Test error", context=context, details={"safe_detail": "safe_value", "password": "secret123"}
        )

        response = create_error_response(error, include_details=True)

        # Should include safe context fields
        assert "context" in response.details
        context_data = response.details["context"]
        assert context_data["user_id"] == "user123"

        # Should include safe metadata
        assert "safe_meta" in context_data["metadata"]
        assert context_data["metadata"]["safe_meta"] == "safe_value"

        # Should exclude sensitive metadata
        assert "password" not in context_data["metadata"]
        assert "api_key" not in context_data["metadata"]
        assert "file_path" not in context_data["metadata"]

        # Should include safe details
        assert "safe_detail" in response.details
        assert response.details["safe_detail"] == "safe_value"

        # Should exclude sensitive details
        assert "password" not in response.details


class TestErrorHandlerIntegration:
    """Test error handler integration with FastAPI."""

    def test_error_handler_registration(self):
        """Test that error handlers are properly registered."""
        app = FastAPI()

        # Import and register error handlers from middleware
        from server.middleware.error_handling_middleware import register_error_handlers

        register_error_handlers(app, include_details=True)

        client = TestClient(app)

        # Create a test endpoint that raises our custom validation error
        @app.get("/test-error")
        def test_error():
            raise MythosValidationError("Test validation error", field="test_field")

        # Test that the error is handled properly
        response = client.get("/test-error")

        # MythosValidationError inherits from MythosMUDError which FastAPI treats as
        # a validation error (422) or application error (400) depending on handler registration
        # Accept either status code as both are valid for validation errors
        assert response.status_code in [400, 422], f"Expected 400 or 422, got {response.status_code}"
        data = response.json()

        # Should not expose sensitive information
        assert "error" in data
        # The error type will be validation_error
        assert "type" in data["error"]
        # Should have a message
        assert "message" in data["error"]

        # Should not include stack traces or sensitive details
        error_data = data["error"]
        assert "stack_trace" not in error_data
        assert "file_path" not in error_data
        assert "password" not in error_data


class TestBleachSanitization:
    """Test bleach-based sanitization functions."""

    def test_sanitize_html_content_basic(self):
        """Test basic HTML sanitization."""
        # Safe HTML should pass through
        safe_html = "<p>Hello <strong>world</strong></p>"
        sanitized = sanitize_html_content(safe_html)
        assert "<p>" in sanitized
        assert "<strong>" in sanitized
        assert "Hello" in sanitized
        assert "world" in sanitized

    def test_sanitize_html_content_remove_unsafe_tags(self):
        """Test that unsafe HTML tags are removed."""
        unsafe_html = "<script>alert('xss')</script><p>Hello</p>"
        sanitized = sanitize_html_content(unsafe_html)
        assert "<script>" not in sanitized
        # Bleach removes script tags but keeps the content
        assert "alert('xss')" in sanitized
        assert "<p>Hello</p>" in sanitized

    def test_sanitize_html_content_remove_unsafe_attributes(self):
        """Test that unsafe HTML attributes are removed."""
        unsafe_html = '<p onclick="alert(\'xss\')" class="safe">Hello</p>'
        sanitized = sanitize_html_content(unsafe_html)
        assert "onclick=" not in sanitized
        assert 'class="safe"' in sanitized
        assert "Hello" in sanitized

    def test_sanitize_html_content_custom_tags(self):
        """Test HTML sanitization with custom allowed tags."""
        html = "<div><span>Hello</span><script>alert('xss')</script></div>"
        sanitized = sanitize_html_content(html, allow_tags=["div", "span"])
        assert "<div>" in sanitized
        assert "<span>" in sanitized
        assert "<script>" not in sanitized
        # Bleach removes script tags but keeps the content
        assert "alert('xss')" in sanitized

    def test_sanitize_text_content_basic(self):
        """Test basic text sanitization."""
        # Plain text should pass through
        text = "Hello world"
        sanitized = sanitize_text_content(text)
        assert sanitized == "Hello world"

    def test_sanitize_text_content_remove_html(self):
        """Test that HTML is removed from text content."""
        text_with_html = "<p>Hello <script>alert('xss')</script> world</p>"
        sanitized = sanitize_text_content(text_with_html)
        assert "<p>" not in sanitized
        assert "<script>" not in sanitized
        # Bleach removes tags but keeps text content
        assert "Hello" in sanitized
        assert "alert('xss')" in sanitized
        assert "world" in sanitized

    def test_sanitize_text_content_length_limit(self):
        """Test that text content is limited to specified length."""
        long_text = "A" * 2000
        sanitized = sanitize_text_content(long_text, max_length=100)
        assert len(sanitized) == 103  # 100 + "..."
        assert sanitized.endswith("...")

    def test_sanitize_detail_value_with_html(self):
        """Test that _sanitize_detail_value handles HTML content."""
        html_content = "<script>alert('xss')</script>Hello world"
        sanitized = _sanitize_detail_value(html_content)
        assert "<script>" not in sanitized
        # The content contains "script" which triggers our redaction
        assert sanitized == "[REDACTED]"

    def test_sanitize_detail_value_with_sensitive_patterns(self):
        """Test that _sanitize_detail_value redacts sensitive patterns."""
        sensitive_content = "Traceback (most recent call last):\n  File '/etc/passwd'"
        sanitized = _sanitize_detail_value(sensitive_content)
        assert sanitized == "[REDACTED]"

    def test_sanitize_detail_value_with_mixed_content(self):
        """Test that _sanitize_detail_value handles mixed content properly."""
        mixed_content = "Hello <script>alert('xss')</script> world"
        sanitized = _sanitize_detail_value(mixed_content)
        # The content contains "script" which triggers our redaction
        assert sanitized == "[REDACTED]"


# ============================================================================
# Tests merged from test_standardized_error_handling_legacy.py
# ============================================================================


"""
Tests for standardized error handling and user-friendly messages.

This module tests the comprehensive error handling strategy to ensure
consistent error responses, proper user-friendly messages, and effective
error categorization across all application layers.
"""


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


# ============================================================================
# Tests merged from test_legacy_error_handlers_legacy.py
# ============================================================================


"""
Tests for legacy error handlers module.

This module tests the centralized error handling for the FastAPI application,
following the ancient principles of proper error categorization as outlined
in the Necronomicon of Software Testing.
"""


class TestErrorResponse:
    """Test ErrorResponse class."""

    def test_error_response_initialization(self):
        """Test ErrorResponse initializes correctly."""
        response = ErrorResponse(
            error_type=ErrorType.INTERNAL_ERROR,
            message="Test error",
            details={"key": "value"},
            user_friendly="User-friendly message",
            status_code=500,
            severity=ErrorSeverity.HIGH,
        )

        assert response.error_type == ErrorType.INTERNAL_ERROR
        assert response.message == "Test error"
        assert response.details == {"key": "value"}
        assert response.user_friendly == "User-friendly message"
        assert response.status_code == 500
        assert response.severity == ErrorSeverity.HIGH

    def test_error_response_defaults(self):
        """Test ErrorResponse uses default values."""
        response = ErrorResponse(error_type=ErrorType.INTERNAL_ERROR, message="Test error")

        assert response.details == {}
        assert response.user_friendly == "Test error"
        assert response.status_code == 500
        assert response.severity == ErrorSeverity.MEDIUM

    def test_error_response_to_dict(self):
        """Test ErrorResponse.to_dict() method."""
        response = ErrorResponse(
            error_type=ErrorType.VALIDATION_ERROR,
            message="Validation failed",
            user_friendly="Please check your input",
            severity=ErrorSeverity.LOW,
        )

        result = response.to_dict()

        assert "error" in result
        assert result["error"]["type"] == "validation_error"
        assert result["error"]["message"] == "Validation failed"
        assert result["error"]["user_friendly"] == "Please check your input"

    def test_error_response_to_response(self):
        """Test ErrorResponse.to_response() method."""
        response = ErrorResponse(error_type=ErrorType.AUTHENTICATION_FAILED, message="Auth failed", status_code=401)

        json_response = response.to_response()

        assert json_response.status_code == 401
        assert "error" in json_response.body.decode()


class TestCreateErrorResponse:
    """Test create_error_response function."""

    def test_create_error_response_authentication_error(self):
        """Test creating error response for AuthenticationError."""
        error = AuthenticationError("Invalid credentials")

        response = create_error_response(error, include_details=False)

        assert response.error_type == ErrorType.AUTHENTICATION_FAILED
        assert response.message == "Invalid credentials"
        assert response.status_code == 401
        assert response.severity == ErrorSeverity.LOW

    def test_create_error_response_validation_error(self):
        """Test creating error response for ValidationError."""
        error = MythosValidationError("Invalid input", field="username")

        response = create_error_response(error, include_details=False)

        assert response.error_type == ErrorType.VALIDATION_ERROR
        assert response.status_code == 400
        assert response.severity == ErrorSeverity.LOW

    def test_create_error_response_database_error(self):
        """Test creating error response for DatabaseError."""
        error = DatabaseError("Connection failed", operation="select")

        response = create_error_response(error, include_details=False)

        assert response.error_type == ErrorType.DATABASE_ERROR
        assert response.status_code == 503
        assert response.severity == ErrorSeverity.HIGH

    def test_create_error_response_rate_limit_error(self):
        """Test creating error response for RateLimitError."""
        error = RateLimitError("Too many requests", limit_type="api", retry_after=60)

        response = create_error_response(error, include_details=False)

        assert response.error_type == ErrorType.RATE_LIMIT_EXCEEDED
        assert response.status_code == 429
        assert response.severity == ErrorSeverity.MEDIUM

    def test_create_error_response_resource_not_found(self):
        """Test creating error response for ResourceNotFoundError."""
        error = ResourceNotFoundError("Player not found", resource_type="player", resource_id="123")

        response = create_error_response(error, include_details=False)

        assert response.error_type == ErrorType.RESOURCE_NOT_FOUND
        assert response.status_code == 404
        assert response.severity == ErrorSeverity.LOW

    def test_create_error_response_game_logic_error(self):
        """Test creating error response for GameLogicError."""
        error = GameLogicError("Invalid move", game_action="teleport")

        response = create_error_response(error, include_details=False)

        assert response.error_type == ErrorType.GAME_LOGIC_ERROR
        assert response.status_code == 422
        assert response.severity == ErrorSeverity.MEDIUM

    def test_create_error_response_network_error(self):
        """Test creating error response for NetworkError."""
        error = NetworkError("Connection timeout")

        response = create_error_response(error, include_details=False)

        assert response.error_type == ErrorType.NETWORK_ERROR
        assert response.status_code == 503
        assert response.severity == ErrorSeverity.HIGH

    def test_create_error_response_configuration_error(self):
        """Test creating error response for ConfigurationError."""
        error = ConfigurationError("Missing config key", config_key="database_url")

        response = create_error_response(error, include_details=False)

        assert response.error_type == ErrorType.CONFIGURATION_ERROR
        assert response.status_code == 500
        assert response.severity == ErrorSeverity.CRITICAL

    def test_create_error_response_generic_mythos_error(self):
        """Test creating error response for generic MythosMUDError."""
        error = MythosMUDError("Generic error")

        response = create_error_response(error, include_details=False)

        assert response.error_type == ErrorType.INTERNAL_ERROR
        assert response.status_code == 500
        assert response.severity == ErrorSeverity.MEDIUM

    def test_create_error_response_with_details_excluded(self):
        """Test that details are excluded when include_details=False."""
        error = DatabaseError("DB error", operation="insert", details={"table": "players", "error_code": "1234"})

        response = create_error_response(error, include_details=False)

        assert response.details == {}

    def test_create_error_response_with_details_included(self):
        """Test that sanitized details are included when include_details=True."""
        context = create_error_context(user_id="test-user-123")
        error = MythosValidationError("Invalid data", field="email", details={"field": "email"}, context=context)

        response = create_error_response(error, include_details=True)

        # Should include sanitized details
        assert isinstance(response.details, dict)


class TestMythosExceptionHandler:
    """Test mythos_exception_handler function."""

    @pytest.mark.asyncio
    async def test_mythos_exception_handler_basic(self):
        """Test basic mythos exception handling."""
        # Create mock request
        mock_request = Mock(spec=Request)
        mock_request.url = Mock()
        mock_request.url.__str__ = Mock(return_value="http://test.com/api/test")
        mock_request.method = "GET"
        mock_request.app = Mock()
        mock_request.app.state = Mock()
        mock_request.app.state.config = {"debug": False}

        # Create exception
        error = MythosValidationError("Test validation error")

        with patch("server.legacy_error_handlers.logger") as mock_logger:
            response = await mythos_exception_handler(mock_request, error)

            # Verify response
            assert response.status_code == 400

            # Verify logging occurred
            mock_logger.error.assert_called_once()
            call_args = mock_logger.error.call_args
            assert "MythosMUD exception handled" in call_args[0][0]

    @pytest.mark.asyncio
    async def test_mythos_exception_handler_with_debug(self):
        """Test mythos exception handler with debug mode enabled."""
        mock_request = Mock(spec=Request)
        mock_request.url = Mock()
        mock_request.url.__str__ = Mock(return_value="http://test.com/api/test")
        mock_request.method = "POST"
        mock_request.app = Mock()
        mock_request.app.state = Mock()
        mock_request.app.state.config = {"debug": True}

        error = DatabaseError("Database connection failed")

        with patch("server.legacy_error_handlers.logger"):
            response = await mythos_exception_handler(mock_request, error)

            assert response.status_code == 503

    @pytest.mark.asyncio
    async def test_mythos_exception_handler_missing_request_id(self):
        """Test handler adds request ID when missing."""
        mock_request = Mock(spec=Request)
        mock_request.url = Mock()
        mock_request.url.__str__ = Mock(return_value="http://test.com/api/endpoint")
        mock_request.method = "PUT"
        mock_request.app = Mock()
        mock_request.app.state = Mock()
        mock_request.app.state.config = {}

        # Create error with context that has no request_id
        context = create_error_context()
        context.request_id = None
        error = AuthenticationError("Auth failed", context=context)

        with patch("server.legacy_error_handlers.logger"):
            response = await mythos_exception_handler(mock_request, error)

            assert response.status_code == 401
            # request_id should now be set
            assert error.context.request_id is not None

    @pytest.mark.asyncio
    async def test_mythos_exception_handler_config_access_error(self):
        """Test handler handles config access errors gracefully."""
        mock_request = Mock(spec=Request)
        mock_request.url = Mock()
        mock_request.url.__str__ = Mock(return_value="http://test.com/api/test")
        mock_request.method = "GET"
        # Simulate AttributeError when accessing config
        mock_request.app = Mock()
        mock_request.app.state = Mock(spec=[])  # No config attribute

        error = MythosValidationError("Test error")

        with patch("server.legacy_error_handlers.logger"):
            response = await mythos_exception_handler(mock_request, error)

            # Should handle the error and default to include_details=False
            assert response.status_code == 400


class TestGeneralExceptionHandler:
    """Test general_exception_handler function."""

    @pytest.mark.asyncio
    async def test_general_exception_handler_value_error(self):
        """Test general exception handler with ValueError."""
        mock_request = Mock(spec=Request)
        mock_request.url = Mock()
        mock_request.url.__str__ = Mock(return_value="http://test.com/api/test")
        mock_request.method = "GET"
        mock_request.headers = {"user-agent": "test-agent"}
        mock_request.app = Mock()
        mock_request.app.state = Mock()
        mock_request.app.state.config = {}

        exc = ValueError("Invalid value")

        with patch("server.legacy_error_handlers.logger") as mock_logger:
            response = await general_exception_handler(mock_request, exc)

            # ValueError gets converted to ValidationError (400) by handle_exception
            assert response.status_code == 400

            # Should log the error
            mock_logger.error.assert_called_once()

    @pytest.mark.asyncio
    async def test_general_exception_handler_runtime_error(self):
        """Test general exception handler with RuntimeError."""
        mock_request = Mock(spec=Request)
        mock_request.url = Mock()
        mock_request.url.__str__ = Mock(return_value="http://test.com/api/endpoint")
        mock_request.method = "POST"
        mock_request.headers = {}
        mock_request.app = Mock()
        mock_request.app.state = Mock()
        mock_request.app.state.config = {"debug": False}

        exc = RuntimeError("Runtime error occurred")

        with patch("server.legacy_error_handlers.logger"):
            response = await general_exception_handler(mock_request, exc)

            assert response.status_code == 500

    @pytest.mark.asyncio
    async def test_general_exception_handler_creates_context(self):
        """Test that general handler creates proper error context."""
        mock_request = Mock(spec=Request)
        mock_request.url = Mock()
        mock_request.url.__str__ = Mock(return_value="http://test.com/api/test")
        mock_request.method = "DELETE"
        mock_request.headers = {"user-agent": "test-browser/1.0"}
        mock_request.app = Mock()
        mock_request.app.state = Mock()
        mock_request.app.state.config = {}

        exc = Exception("Generic exception")

        with patch("server.legacy_error_handlers.logger") as mock_logger:
            response = await general_exception_handler(mock_request, exc)

            assert response.status_code == 500

            # Verify logging includes context
            mock_logger.error.assert_called_once()
            call_args = mock_logger.error.call_args
            assert "Unhandled exception converted to MythosMUD error" in call_args[0][0]

    @pytest.mark.asyncio
    async def test_general_exception_handler_config_error(self):
        """Test general handler handles config access errors."""
        mock_request = Mock(spec=Request)
        mock_request.url = Mock()
        mock_request.url.__str__ = Mock(return_value="http://test.com/api/test")
        mock_request.method = "GET"
        mock_request.headers = {}
        # Simulate missing config
        mock_request.app = Mock()
        mock_request.app.state = Mock(spec=[])

        exc = KeyError("Missing key")

        with patch("server.legacy_error_handlers.logger"):
            response = await general_exception_handler(mock_request, exc)

            # Should handle gracefully and default to include_details=False
            assert response.status_code == 500


class TestLoggedHTTPExceptionHandler:
    """Test logged_http_exception_handler function."""

    @pytest.mark.asyncio
    async def test_logged_http_exception_handler_401(self):
        """Test handler with 401 Unauthorized."""
        from server.exceptions import LoggedHTTPException
        from server.legacy_error_handlers import logged_http_exception_handler

        mock_request = Mock(spec=Request)
        mock_request.url = Mock()
        mock_request.url.__str__ = Mock(return_value="http://test.com/api/auth")
        mock_request.method = "POST"

        exc = LoggedHTTPException(status_code=401, detail="Unauthorized access")

        with patch("server.legacy_error_handlers.logger") as mock_logger:
            response = await logged_http_exception_handler(mock_request, exc)

            assert response.status_code == 401
            mock_logger.info.assert_called_once()
            call_args = mock_logger.info.call_args
            assert "LoggedHTTPException handled" in call_args[0][0]

    @pytest.mark.asyncio
    async def test_logged_http_exception_handler_404(self):
        """Test handler with 404 Not Found."""
        from server.exceptions import LoggedHTTPException
        from server.legacy_error_handlers import logged_http_exception_handler

        mock_request = Mock(spec=Request)
        mock_request.url = Mock()
        mock_request.url.__str__ = Mock(return_value="http://test.com/api/player/999")
        mock_request.method = "GET"

        exc = LoggedHTTPException(status_code=404, detail="Player not found")

        with patch("server.legacy_error_handlers.logger"):
            response = await logged_http_exception_handler(mock_request, exc)

            assert response.status_code == 404

    @pytest.mark.asyncio
    async def test_logged_http_exception_handler_422(self):
        """Test handler with 422 Unprocessable Entity."""
        from server.exceptions import LoggedHTTPException
        from server.legacy_error_handlers import logged_http_exception_handler

        mock_request = Mock(spec=Request)
        mock_request.url = Mock()
        mock_request.url.__str__ = Mock(return_value="http://test.com/api/action")
        mock_request.method = "POST"

        exc = LoggedHTTPException(status_code=422, detail="Invalid action")

        with patch("server.legacy_error_handlers.logger"):
            response = await logged_http_exception_handler(mock_request, exc)

            assert response.status_code == 422

    @pytest.mark.asyncio
    async def test_logged_http_exception_handler_429(self):
        """Test handler with 429 Too Many Requests."""
        from server.exceptions import LoggedHTTPException
        from server.legacy_error_handlers import logged_http_exception_handler

        mock_request = Mock(spec=Request)
        mock_request.url = Mock()
        mock_request.url.__str__ = Mock(return_value="http://test.com/api/endpoint")
        mock_request.method = "POST"

        exc = LoggedHTTPException(status_code=429, detail="Rate limit exceeded")

        with patch("server.legacy_error_handlers.logger"):
            response = await logged_http_exception_handler(mock_request, exc)

            assert response.status_code == 429

    @pytest.mark.asyncio
    async def test_logged_http_exception_handler_other_status(self):
        """Test handler with other status codes."""
        from server.exceptions import LoggedHTTPException
        from server.legacy_error_handlers import logged_http_exception_handler

        mock_request = Mock(spec=Request)
        mock_request.url = Mock()
        mock_request.url.__str__ = Mock(return_value="http://test.com/api/test")
        mock_request.method = "GET"

        exc = LoggedHTTPException(status_code=503, detail="Service unavailable")

        with patch("server.legacy_error_handlers.logger"):
            response = await logged_http_exception_handler(mock_request, exc)

            assert response.status_code == 503

    @pytest.mark.asyncio
    async def test_logged_http_exception_handler_websocket(self):
        """Test handler with WebSocket request."""
        from server.exceptions import LoggedHTTPException
        from server.legacy_error_handlers import logged_http_exception_handler

        # Create simple object without method attribute (simulating WebSocket)
        class WebSocketRequest:
            def __init__(self):
                self.url = Mock()
                self.url.__str__ = Mock(return_value="ws://test.com/ws/game")

        mock_request = WebSocketRequest()

        exc = LoggedHTTPException(status_code=403, detail="Forbidden")

        with patch("server.legacy_error_handlers.logger") as mock_logger:
            response = await logged_http_exception_handler(mock_request, exc)

            assert response.status_code == 403
            # Verify method was logged as WEBSOCKET
            call_args = mock_logger.info.call_args
            assert call_args[1]["method"] == "WEBSOCKET"


class TestHTTPExceptionHandler:
    """Test http_exception_handler function."""

    @pytest.mark.asyncio
    async def test_http_exception_handler_401(self):
        """Test handler with 401 Unauthorized."""
        from fastapi import HTTPException

        from server.legacy_error_handlers import http_exception_handler

        mock_request = Mock(spec=Request)
        mock_request.url = Mock()
        mock_request.url.__str__ = Mock(return_value="http://test.com/api/auth")
        mock_request.method = "POST"

        exc = HTTPException(status_code=401, detail="Authentication required")

        with patch("server.legacy_error_handlers.logger") as mock_logger:
            response = await http_exception_handler(mock_request, exc)

            assert response.status_code == 401
            mock_logger.warning.assert_called_once()

    @pytest.mark.asyncio
    async def test_http_exception_handler_404(self):
        """Test handler with 404 Not Found."""
        from fastapi import HTTPException

        from server.legacy_error_handlers import http_exception_handler

        mock_request = Mock(spec=Request)
        mock_request.url = Mock()
        mock_request.url.__str__ = Mock(return_value="http://test.com/api/resource")
        mock_request.method = "GET"

        exc = HTTPException(status_code=404, detail="Resource not found")

        with patch("server.legacy_error_handlers.logger"):
            response = await http_exception_handler(mock_request, exc)

            assert response.status_code == 404

    @pytest.mark.asyncio
    async def test_http_exception_handler_422(self):
        """Test handler with 422 Unprocessable Entity."""
        from fastapi import HTTPException

        from server.legacy_error_handlers import http_exception_handler

        mock_request = Mock(spec=Request)
        mock_request.url = Mock()
        mock_request.url.__str__ = Mock(return_value="http://test.com/api/data")
        mock_request.method = "POST"

        exc = HTTPException(status_code=422, detail="Validation failed")

        with patch("server.legacy_error_handlers.logger"):
            response = await http_exception_handler(mock_request, exc)

            assert response.status_code == 422

    @pytest.mark.asyncio
    async def test_http_exception_handler_429(self):
        """Test handler with 429 Too Many Requests."""
        from fastapi import HTTPException

        from server.legacy_error_handlers import http_exception_handler

        mock_request = Mock(spec=Request)
        mock_request.url = Mock()
        mock_request.url.__str__ = Mock(return_value="http://test.com/api/action")
        mock_request.method = "POST"

        exc = HTTPException(status_code=429, detail="Too many requests")

        with patch("server.legacy_error_handlers.logger"):
            response = await http_exception_handler(mock_request, exc)

            assert response.status_code == 429

    @pytest.mark.asyncio
    async def test_http_exception_handler_other_status(self):
        """Test handler with other status codes."""
        from fastapi import HTTPException

        from server.legacy_error_handlers import http_exception_handler

        mock_request = Mock(spec=Request)
        mock_request.url = Mock()
        mock_request.url.__str__ = Mock(return_value="http://test.com/api/test")
        mock_request.method = "GET"

        exc = HTTPException(status_code=500, detail="Internal server error")

        with patch("server.legacy_error_handlers.logger"):
            response = await http_exception_handler(mock_request, exc)

            assert response.status_code == 500

    @pytest.mark.asyncio
    async def test_http_exception_handler_websocket(self):
        """Test handler with WebSocket request."""
        from fastapi import HTTPException

        from server.legacy_error_handlers import http_exception_handler

        # Create simple object without method attribute (simulating WebSocket)
        class WebSocketRequest:
            def __init__(self):
                self.url = Mock()
                self.url.__str__ = Mock(return_value="ws://test.com/ws/chat")

        mock_request = WebSocketRequest()

        exc = HTTPException(status_code=403, detail="Access denied")

        with patch("server.legacy_error_handlers.logger") as mock_logger:
            response = await http_exception_handler(mock_request, exc)

            assert response.status_code == 403
            # Verify method was logged as WEBSOCKET
            call_args = mock_logger.warning.call_args
            assert call_args[1]["method"] == "WEBSOCKET"


class TestGracefulDegradation:
    """Test graceful_degradation context manager."""

    def test_graceful_degradation_success(self):
        """Test graceful degradation when operation succeeds."""
        from server.legacy_error_handlers import graceful_degradation

        with graceful_degradation(fallback_value="fallback", error_type="test_error"):
            # Operation succeeds, no exception
            result = "success"

        # Should use actual result, not fallback
        assert result == "success"

    def test_graceful_degradation_failure(self):
        """Test graceful degradation when operation fails."""
        from server.legacy_error_handlers import graceful_degradation

        with patch("server.legacy_error_handlers.logger") as mock_logger:
            with graceful_degradation(fallback_value="fallback", error_type="test_error"):
                # Simulate operation failure
                raise ValueError("Operation failed")

            # Should log the error
            mock_logger.warning.assert_called_once()
            call_args = mock_logger.warning.call_args
            assert "Graceful degradation applied" in call_args[0][0]
            assert call_args[1]["fallback_value"] == "fallback"

    def test_graceful_degradation_returns_fallback(self):
        """Test that graceful degradation suppresses exceptions."""
        from server.legacy_error_handlers import graceful_degradation

        with patch("server.legacy_error_handlers.logger"):
            try:
                with graceful_degradation(fallback_value=42, error_type="numeric_error"):
                    raise RuntimeError("Calculation failed")
                # Exception should be suppressed, execution continues
                success = True
            except Exception:
                success = False

            # Should not re-raise the exception
            assert success

    def test_graceful_degradation_logs_error_type(self):
        """Test that error type is logged correctly."""
        from server.legacy_error_handlers import graceful_degradation

        with patch("server.legacy_error_handlers.logger") as mock_logger:
            with graceful_degradation(fallback_value="default", error_type="custom_error"):
                raise KeyError("Missing key")

            # Verify error type was logged
            call_args = mock_logger.warning.call_args
            assert call_args[1]["error_type"] == "custom_error"


class TestRegisterErrorHandlers:
    """Test register_error_handlers function."""

    def test_register_error_handlers_adds_all_handlers(self):
        """Test that all error handlers are registered."""
        from fastapi import FastAPI, HTTPException
        from starlette.exceptions import HTTPException as StarletteHTTPException

        from server.exceptions import LoggedHTTPException
        from server.legacy_error_handlers import register_error_handlers

        app = FastAPI()

        with patch("server.legacy_error_handlers.logger") as mock_logger:
            register_error_handlers(app)

            # Verify all handlers were added
            assert MythosMUDError in app.exception_handlers
            assert LoggedHTTPException in app.exception_handlers
            assert Exception in app.exception_handlers
            assert HTTPException in app.exception_handlers
            assert StarletteHTTPException in app.exception_handlers

            # Verify registration was logged
            mock_logger.info.assert_called_once()
            call_args = mock_logger.info.call_args
            assert "Error handlers registered" in call_args[0][0]


class TestCircuitBreaker:
    """Test CircuitBreaker class."""

    def test_circuit_breaker_initialization(self):
        """Test CircuitBreaker initializes correctly."""
        from server.legacy_error_handlers import CircuitBreaker

        breaker = CircuitBreaker(failure_threshold=3, timeout=30)

        assert breaker.failure_threshold == 3
        assert breaker.timeout == 30
        assert breaker.failure_count == 0
        assert breaker.last_failure_time is None
        assert breaker.state == "CLOSED"

    def test_circuit_breaker_successful_call(self):
        """Test successful function call through circuit breaker."""
        from server.legacy_error_handlers import CircuitBreaker

        breaker = CircuitBreaker()

        def successful_func(x, y):
            return x + y

        result = breaker.call(successful_func, 5, 10)

        assert result == 15
        assert breaker.failure_count == 0
        assert breaker.state == "CLOSED"

    def test_circuit_breaker_failed_call(self):
        """Test failed function call through circuit breaker."""
        from server.legacy_error_handlers import CircuitBreaker

        breaker = CircuitBreaker(failure_threshold=2)

        def failing_func():
            raise ValueError("Function failed")

        # First failure
        with pytest.raises(ValueError):
            breaker.call(failing_func)

        assert breaker.failure_count == 1
        assert breaker.state == "CLOSED"

        # Second failure - should open circuit
        with pytest.raises(ValueError):
            breaker.call(failing_func)

        assert breaker.failure_count == 2
        assert breaker.state == "OPEN"

    def test_circuit_breaker_open_state_blocks_calls(self):
        """Test that open circuit breaker blocks calls."""
        from server.legacy_error_handlers import CircuitBreaker

        breaker = CircuitBreaker(failure_threshold=1)

        def failing_func():
            raise RuntimeError("Failure")

        # Trigger failure to open circuit
        with pytest.raises(RuntimeError):
            breaker.call(failing_func)

        assert breaker.state == "OPEN"

        # Next call should fail immediately with NetworkError
        def another_func():
            return "success"

        with pytest.raises(NetworkError) as exc_info:
            breaker.call(another_func)

        assert "Circuit breaker is open" in str(exc_info.value)

    def test_circuit_breaker_half_open_state(self):
        """Test circuit breaker transitions to half-open state after timeout."""
        import time

        from server.legacy_error_handlers import CircuitBreaker

        breaker = CircuitBreaker(failure_threshold=1, timeout=1)

        def failing_func():
            raise ValueError("Failure")

        # Open the circuit
        with pytest.raises(ValueError):
            breaker.call(failing_func)

        assert breaker.state == "OPEN"

        # Wait for timeout
        time.sleep(1.1)

        # Should transition to HALF_OPEN
        def successful_func():
            return "success"

        result = breaker.call(successful_func)

        assert result == "success"
        assert breaker.state == "CLOSED"
        assert breaker.failure_count == 0

    def test_circuit_breaker_reset_on_success(self):
        """Test that circuit breaker resets on success."""
        from server.legacy_error_handlers import CircuitBreaker

        breaker = CircuitBreaker(failure_threshold=5)
        breaker.failure_count = 3
        breaker.state = "CLOSED"

        def successful_func():
            return "ok"

        result = breaker.call(successful_func)

        assert result == "ok"
        assert breaker.failure_count == 0
        assert breaker.state == "CLOSED"

    def test_circuit_breaker_should_attempt_reset_no_failures(self):
        """Test _should_attempt_reset when no failures recorded."""
        from server.legacy_error_handlers import CircuitBreaker

        breaker = CircuitBreaker()

        # No failures yet
        assert breaker._should_attempt_reset() is True

    def test_circuit_breaker_should_attempt_reset_timeout_not_reached(self):
        """Test _should_attempt_reset when timeout not yet reached."""
        from datetime import datetime

        from server.legacy_error_handlers import CircuitBreaker

        breaker = CircuitBreaker(timeout=60)
        breaker.last_failure_time = datetime.now()

        # Just failed, timeout not reached
        assert breaker._should_attempt_reset() is False


class TestSanitizationFunctions:
    """Test sanitization helper functions."""

    def test_sanitize_detail_value_long_string(self):
        """Test sanitizing long string values."""
        from server.legacy_error_handlers import _sanitize_detail_value

        long_string = "a" * 150  # 150 characters

        result = _sanitize_detail_value(long_string)

        # Should truncate to 100 chars with ellipsis
        assert len(result) == 103  # 100 + "..."
        assert result.endswith("...")

    def test_sanitize_detail_value_short_string(self):
        """Test sanitizing short string values."""
        from server.legacy_error_handlers import _sanitize_detail_value

        short_string = "short value"

        result = _sanitize_detail_value(short_string)

        assert result == "short value"

    def test_sanitize_detail_value_int(self):
        """Test sanitizing integer values."""
        from server.legacy_error_handlers import _sanitize_detail_value

        result = _sanitize_detail_value(42)

        assert result == 42

    def test_sanitize_detail_value_float(self):
        """Test sanitizing float values."""
        from server.legacy_error_handlers import _sanitize_detail_value

        result = _sanitize_detail_value(3.14159)

        assert result == 3.14159

    def test_sanitize_detail_value_bool(self):
        """Test sanitizing boolean values."""
        from server.legacy_error_handlers import _sanitize_detail_value

        assert _sanitize_detail_value(True) is True
        assert _sanitize_detail_value(False) is False

    def test_sanitize_detail_value_dict(self):
        """Test sanitizing dictionary values."""
        from server.legacy_error_handlers import _sanitize_detail_value

        test_dict = {
            "operation": "select",  # safe key from whitelist
            "field": "username",  # safe key from whitelist
            "password": "secret",  # Should be filtered (unsafe pattern)
            "count": 10,  # No unsafe patterns, kept
        }

        result = _sanitize_detail_value(test_dict)

        # Should filter based on safe whitelist and unsafe patterns
        assert isinstance(result, dict)
        assert "operation" in result
        assert "field" in result
        assert "password" not in result  # Filtered (unsafe pattern)
        assert "count" in result  # No unsafe patterns, so kept

    def test_sanitize_detail_value_list(self):
        """Test sanitizing list values."""
        from server.legacy_error_handlers import _sanitize_detail_value

        test_list = ["item1", 42, "item3"]

        result = _sanitize_detail_value(test_list)

        assert isinstance(result, list)
        assert len(result) == 3
        assert result[0] == "item1"
        assert result[1] == 42
        assert result[2] == "item3"

    def test_sanitize_detail_value_other_type(self):
        """Test sanitizing other types (converted to string)."""
        from server.legacy_error_handlers import _sanitize_detail_value

        class CustomObject:
            def __str__(self):
                return "custom object"

        obj = CustomObject()
        result = _sanitize_detail_value(obj)

        assert result == "custom object"

    def test_sanitize_detail_value_long_other_type(self):
        """Test sanitizing other types with long string representation."""
        from server.legacy_error_handlers import _sanitize_detail_value

        class LongObject:
            def __str__(self):
                return "x" * 150

        obj = LongObject()
        result = _sanitize_detail_value(obj)

        # Should truncate to 100 chars with ellipsis
        assert len(result) == 103
        assert result.endswith("...")

    def test_sanitize_context_none(self):
        """Test sanitizing None context."""
        from server.legacy_error_handlers import _sanitize_context

        result = _sanitize_context(None)

        assert result is None

    def test_sanitize_context_with_safe_fields(self):
        """Test sanitizing context with safe fields."""
        from server.legacy_error_handlers import _sanitize_context

        context = create_error_context(
            user_id="user-123", session_id="session-456", request_id="req-789", metadata={"safe_field": "value"}
        )

        result = _sanitize_context(context)

        assert result is not None
        assert result["user_id"] == "user-123"
        assert result["session_id"] == "session-456"
        assert result["request_id"] == "req-789"
        assert "timestamp" in result

    def test_sanitize_html_content_empty(self):
        """Test sanitizing empty HTML content."""
        from server.legacy_error_handlers import sanitize_html_content

        result = sanitize_html_content("")

        assert result == ""

    def test_sanitize_html_content_none(self):
        """Test sanitizing None HTML content."""
        from server.legacy_error_handlers import sanitize_html_content

        result = sanitize_html_content(None)

        assert result == ""

    def test_sanitize_html_content_with_allowed_tags(self):
        """Test sanitizing HTML with allowed tags."""
        from server.legacy_error_handlers import sanitize_html_content

        html = "<p>Hello <strong>world</strong></p><script>alert('xss')</script>"

        result = sanitize_html_content(html)

        # Should keep allowed tags, remove script tags but preserve text content
        assert "<p>" in result
        assert "<strong>" in result
        assert "<script>" not in result
        # Note: bleach removes tags but keeps content, so "alert" text remains
        assert "Hello" in result
        assert "world" in result

    def test_sanitize_html_content_custom_tags(self):
        """Test sanitizing HTML with custom allowed tags."""
        from server.legacy_error_handlers import sanitize_html_content

        html = "<div>Content</div><span>Text</span>"

        result = sanitize_html_content(html, allow_tags=["div"])

        # Should keep only div tags
        assert "<div>" in result
        assert "</div>" in result
        # span should be stripped but content preserved
        assert "Text" in result

    def test_sanitize_text_content_empty(self):
        """Test sanitizing empty text content."""
        from server.legacy_error_handlers import sanitize_text_content

        result = sanitize_text_content("")

        assert result == ""

    def test_sanitize_text_content_none(self):
        """Test sanitizing None text content."""
        from server.legacy_error_handlers import sanitize_text_content

        result = sanitize_text_content(None)

        assert result == ""

    def test_sanitize_text_content_long_text(self):
        """Test sanitizing long text content."""
        from server.legacy_error_handlers import sanitize_text_content

        long_text = "x" * 1500

        result = sanitize_text_content(long_text, max_length=1000)

        # Should truncate to max_length
        assert len(result) == 1003  # 1000 + "..."
        assert result.endswith("...")

    def test_sanitize_text_content_removes_html(self):
        """Test that text sanitization removes HTML."""
        from server.legacy_error_handlers import sanitize_text_content

        text = "Normal text <script>alert('xss')</script> more text"

        result = sanitize_text_content(text)

        # Should remove HTML tags
        assert "<script>" not in result
        assert "Normal text" in result
        assert "more text" in result
