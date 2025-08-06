"""
Tests for comprehensive exception handling system.

This module tests the exception hierarchy, error context, and response
handling for the MythosMUD system. As the Pnakotic Manuscripts teach us,
proper testing of error conditions is essential for maintaining dimensional
stability in our digital realm.
"""

from datetime import datetime
from unittest.mock import patch

import pytest

from ..error_handlers import (
    CircuitBreaker,
    ErrorResponse,
    _get_status_code_for_error,
    create_error_response,
    graceful_degradation,
)
from ..exceptions import (
    AuthenticationError,
    DatabaseError,
    ErrorContext,
    GameLogicError,
    MythosMUDError,
    NetworkError,
    RateLimitError,
    ResourceNotFoundError,
    ValidationError,
    create_error_context,
    handle_exception,
)


class TestErrorContext:
    """Test cases for ErrorContext class."""

    def test_error_context_creation(self):
        """Test creating ErrorContext with various parameters."""
        context = ErrorContext(user_id="testuser", room_id="test_room", command="look", session_id="session123")

        assert context.user_id == "testuser"
        assert context.room_id == "test_room"
        assert context.command == "look"
        assert context.session_id == "session123"
        assert isinstance(context.timestamp, datetime)
        assert context.metadata == {}

    def test_error_context_to_dict(self):
        """Test converting ErrorContext to dictionary."""
        context = ErrorContext(user_id="testuser", room_id="test_room", metadata={"test_key": "test_value"})

        context_dict = context.to_dict()

        assert context_dict["user_id"] == "testuser"
        assert context_dict["room_id"] == "test_room"
        assert context_dict["metadata"]["test_key"] == "test_value"
        assert "timestamp" in context_dict

    def test_create_error_context_helper(self):
        """Test the create_error_context helper function."""
        context = create_error_context(user_id="testuser", room_id="test_room", command="look")

        assert isinstance(context, ErrorContext)
        assert context.user_id == "testuser"
        assert context.room_id == "test_room"
        assert context.command == "look"


class TestMythosMUDError:
    """Test cases for base MythosMUDError class."""

    @patch("server.exceptions.logger")
    def test_mythos_error_creation(self, mock_logger):
        """Test creating MythosMUDError with various parameters."""
        context = create_error_context(user_id="testuser")
        error = MythosMUDError(
            message="Test error message",
            context=context,
            details={"test_detail": "value"},
            user_friendly="User-friendly message",
        )

        assert error.message == "Test error message"
        assert error.context.user_id == "testuser"
        assert error.details["test_detail"] == "value"
        assert error.user_friendly == "User-friendly message"
        assert isinstance(error.timestamp, datetime)

        # Verify logging was called
        mock_logger.error.assert_called_once()

    def test_mythos_error_to_dict(self):
        """Test converting MythosMUDError to dictionary."""
        context = create_error_context(user_id="testuser")
        error = MythosMUDError(message="Test error", context=context, details={"detail": "value"})

        error_dict = error.to_dict()

        assert error_dict["error_type"] == "MythosMUDError"
        assert error_dict["message"] == "Test error"
        assert error_dict["details"]["detail"] == "value"
        assert "timestamp" in error_dict
        assert "context" in error_dict


class TestSpecificErrors:
    """Test cases for specific error types."""

    def test_authentication_error(self):
        """Test AuthenticationError creation and properties."""
        context = create_error_context(user_id="testuser")
        error = AuthenticationError(message="Invalid credentials", context=context, auth_type="jwt")

        assert error.auth_type == "jwt"
        assert error.details["auth_type"] == "jwt"
        assert isinstance(error, MythosMUDError)

    def test_database_error(self):
        """Test DatabaseError creation and properties."""
        context = create_error_context(user_id="testuser")
        error = DatabaseError(message="Connection failed", context=context, operation="SELECT", table="players")

        assert error.operation == "SELECT"
        assert error.table == "players"
        assert error.details["operation"] == "SELECT"
        assert error.details["table"] == "players"

    def test_validation_error(self):
        """Test ValidationError creation and properties."""
        context = create_error_context(user_id="testuser")
        error = ValidationError(message="Invalid field", context=context, field="username", value="invalid@user")

        assert error.field == "username"
        assert error.value == "invalid@user"
        assert error.details["field"] == "username"
        assert error.details["value"] == "invalid@user"

    def test_game_logic_error(self):
        """Test GameLogicError creation and properties."""
        context = create_error_context(user_id="testuser")
        error = GameLogicError(message="Invalid move", context=context, game_action="move")

        assert error.game_action == "move"
        assert error.details["game_action"] == "move"

    def test_resource_not_found_error(self):
        """Test ResourceNotFoundError creation and properties."""
        context = create_error_context(user_id="testuser")
        error = ResourceNotFoundError(
            message="Room not found", context=context, resource_type="room", resource_id="nonexistent_room"
        )

        assert error.resource_type == "room"
        assert error.resource_id == "nonexistent_room"
        assert error.details["resource_type"] == "room"
        assert error.details["resource_id"] == "nonexistent_room"

    def test_rate_limit_error(self):
        """Test RateLimitError creation and properties."""
        context = create_error_context(user_id="testuser")
        error = RateLimitError(message="Too many requests", context=context, limit_type="api", retry_after=60)

        assert error.limit_type == "api"
        assert error.retry_after == 60
        assert error.details["limit_type"] == "api"
        assert error.details["retry_after"] == 60


class TestExceptionHandling:
    """Test cases for exception handling utilities."""

    def test_handle_exception_mythos_error(self):
        """Test handling of existing MythosMUDError."""
        original_error = AuthenticationError("Test auth error")
        handled_error = handle_exception(original_error)

        assert handled_error is original_error

    def test_handle_exception_value_error(self):
        """Test converting ValueError to ValidationError."""
        context = create_error_context(user_id="testuser")
        original_error = ValueError("Invalid value")
        handled_error = handle_exception(original_error, context)

        assert isinstance(handled_error, ValidationError)
        assert handled_error.message == "Invalid value"
        assert handled_error.context.user_id == "testuser"
        assert handled_error.details["original_type"] == "ValueError"

    def test_handle_exception_file_not_found(self):
        """Test converting FileNotFoundError to ResourceNotFoundError."""
        context = create_error_context(user_id="testuser")
        original_error = FileNotFoundError("File not found")
        handled_error = handle_exception(original_error, context)

        assert isinstance(handled_error, ResourceNotFoundError)
        assert handled_error.message == "File not found"
        assert handled_error.details["original_type"] == "FileNotFoundError"

    def test_handle_exception_connection_error(self):
        """Test converting ConnectionError to NetworkError."""
        context = create_error_context(user_id="testuser")
        original_error = ConnectionError("Connection failed")
        handled_error = handle_exception(original_error, context)

        assert isinstance(handled_error, NetworkError)
        assert handled_error.message == "Connection failed"
        assert handled_error.details["original_type"] == "ConnectionError"

    def test_handle_exception_generic(self):
        """Test converting generic exception to MythosMUDError."""
        context = create_error_context(user_id="testuser")
        original_error = Exception("Generic error")
        handled_error = handle_exception(original_error, context)

        assert isinstance(handled_error, MythosMUDError)
        assert handled_error.message == "Generic error"
        assert "traceback" in handled_error.details


class TestErrorResponse:
    """Test cases for ErrorResponse class."""

    def test_error_response_creation(self):
        """Test creating ErrorResponse with various parameters."""
        response = ErrorResponse(
            error_type="TestError",
            message="Test message",
            details={"detail": "value"},
            user_friendly="User message",
            status_code=400,
        )

        assert response.error_type == "TestError"
        assert response.message == "Test message"
        assert response.details["detail"] == "value"
        assert response.user_friendly == "User message"
        assert response.status_code == 400

    def test_error_response_to_dict(self):
        """Test converting ErrorResponse to dictionary."""
        response = ErrorResponse(error_type="TestError", message="Test message", details={"detail": "value"})

        response_dict = response.to_dict()

        assert response_dict["error"]["type"] == "TestError"
        assert response_dict["error"]["message"] == "Test message"
        assert response_dict["error"]["details"]["detail"] == "value"

    def test_error_response_to_response(self):
        """Test converting ErrorResponse to FastAPI JSONResponse."""
        response = ErrorResponse(error_type="TestError", message="Test message", status_code=400)

        json_response = response.to_response()

        assert json_response.status_code == 400
        assert (
            json_response.body.decode()
            == '{"error":{"type":"TestError","message":"Test message","user_friendly":"Test message","details":{}}}'
        )


class TestErrorResponseCreation:
    """Test cases for error response creation utilities."""

    def test_create_error_response_basic(self):
        """Test creating error response from MythosMUDError."""
        context = create_error_context(user_id="testuser")
        error = AuthenticationError("Auth failed", context)

        response = create_error_response(error)

        assert response.error_type == "AuthenticationError"
        assert response.message == "Auth failed"
        assert response.status_code == 401

    def test_create_error_response_with_details(self):
        """Test creating error response with detailed information."""
        context = create_error_context(user_id="testuser")
        error = ValidationError("Invalid input", context, field="username")

        response = create_error_response(error, include_details=True)

        assert response.error_type == "ValidationError"
        assert response.status_code == 400
        assert "context" in response.details

    def test_get_status_code_for_error(self):
        """Test status code mapping for different error types."""
        context = create_error_context()

        auth_error = AuthenticationError("Auth failed", context)
        assert _get_status_code_for_error(auth_error) == 401

        validation_error = ValidationError("Invalid input", context)
        assert _get_status_code_for_error(validation_error) == 400

        not_found_error = ResourceNotFoundError("Not found", context)
        assert _get_status_code_for_error(not_found_error) == 404

        rate_limit_error = RateLimitError("Too many requests", context)
        assert _get_status_code_for_error(rate_limit_error) == 429

        database_error = DatabaseError("DB failed", context)
        assert _get_status_code_for_error(database_error) == 503


class TestGracefulDegradation:
    """Test cases for graceful degradation utilities."""

    def test_graceful_degradation_success(self):
        """Test graceful degradation when operation succeeds."""

        def successful_operation():
            return "success"

        with graceful_degradation("fallback", "test"):
            result = successful_operation()
            assert result == "success"

    def test_graceful_degradation_failure(self):
        """Test graceful degradation when operation fails."""

        def failing_operation():
            raise ValueError("Operation failed")

        # This should not raise an exception due to graceful degradation
        # The fallback value would be handled by the calling code
        with graceful_degradation("fallback", "test"):
            try:
                failing_operation()
            except ValueError:
                pass  # Expected to fail, but graceful degradation prevents propagation


class TestCircuitBreaker:
    """Test cases for CircuitBreaker pattern."""

    def test_circuit_breaker_initial_state(self):
        """Test circuit breaker initial state."""
        breaker = CircuitBreaker()

        assert breaker.state == "CLOSED"
        assert breaker.failure_count == 0
        assert breaker.last_failure_time is None

    def test_circuit_breaker_successful_calls(self):
        """Test circuit breaker with successful calls."""
        breaker = CircuitBreaker(failure_threshold=3)

        def successful_func():
            return "success"

        # Multiple successful calls should keep circuit closed
        for _ in range(5):
            result = breaker.call(successful_func)
            assert result == "success"
            assert breaker.state == "CLOSED"
            assert breaker.failure_count == 0

    def test_circuit_breaker_failure_threshold(self):
        """Test circuit breaker opening after failure threshold."""
        breaker = CircuitBreaker(failure_threshold=2)

        def failing_func():
            raise ValueError("Test failure")

        # First failure
        with pytest.raises(ValueError):
            breaker.call(failing_func)
        assert breaker.state == "CLOSED"
        assert breaker.failure_count == 1

        # Second failure - should open circuit
        with pytest.raises(ValueError):
            breaker.call(failing_func)
        assert breaker.state == "OPEN"
        assert breaker.failure_count == 2

    def test_circuit_breaker_open_state(self):
        """Test circuit breaker behavior when open."""
        breaker = CircuitBreaker(failure_threshold=1, timeout=1)

        def failing_func():
            raise ValueError("Test failure")

        # Trigger failure to open circuit
        with pytest.raises(ValueError):
            breaker.call(failing_func)

        assert breaker.state == "OPEN"

        # Attempting to call when open should raise NetworkError
        with pytest.raises(NetworkError):
            breaker.call(failing_func)

    def test_circuit_breaker_reset_after_timeout(self):
        """Test circuit breaker reset after timeout period."""
        breaker = CircuitBreaker(failure_threshold=1, timeout=0.1)

        def failing_func():
            raise ValueError("Test failure")

        # Trigger failure to open circuit
        with pytest.raises(ValueError):
            breaker.call(failing_func)

        assert breaker.state == "OPEN"

        # Wait for timeout and test reset
        import time

        time.sleep(0.2)

        # Should be able to attempt reset
        assert breaker._should_attempt_reset() is True
