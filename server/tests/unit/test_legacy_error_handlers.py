"""
Unit tests for legacy error handlers.

Tests error handling, error response creation, circuit breaker,
and sanitization functions.
"""

from unittest.mock import Mock

import pytest
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from server.error_types import ErrorSeverity, ErrorType
from server.exceptions import (
    AuthenticationError,
    ConfigurationError,
    DatabaseError,
    GameLogicError,
    LoggedHTTPException,
    MythosMUDError,
    NetworkError,
    RateLimitError,
    ResourceNotFoundError,
    ValidationError,
    create_error_context,
)
from server.legacy_error_handlers import (
    CircuitBreaker,
    ErrorResponse,
    _get_severity_for_error,
    _get_status_code_for_error,
    _is_safe_detail_key,
    _map_error_type,
    _sanitize_context,
    _sanitize_detail_value,
    create_error_response,
    general_exception_handler,
    graceful_degradation,
    http_exception_handler,
    logged_http_exception_handler,
    mythos_exception_handler,
    register_error_handlers,
    sanitize_html_content,
    sanitize_text_content,
)


class TestErrorResponse:
    """Test ErrorResponse class."""

    def test_error_response_initialization(self):
        """Test ErrorResponse initialization."""
        response = ErrorResponse(
            error_type=ErrorType.AUTHENTICATION_FAILED,
            message="Test error",
            details={"key": "value"},
            user_friendly="User-friendly error",
            status_code=401,
            severity=ErrorSeverity.LOW,
        )
        assert response.error_type == ErrorType.AUTHENTICATION_FAILED
        assert response.message == "Test error"
        assert response.details == {"key": "value"}
        assert response.user_friendly == "User-friendly error"
        assert response.status_code == 401
        assert response.severity == ErrorSeverity.LOW

    def test_error_response_defaults(self):
        """Test ErrorResponse with default values."""
        response = ErrorResponse(
            error_type=ErrorType.INTERNAL_ERROR,
            message="Test error",
        )
        assert response.details == {}
        assert response.user_friendly == "Test error"
        assert response.status_code == 500
        assert response.severity == ErrorSeverity.MEDIUM

    def test_error_response_to_dict(self):
        """Test ErrorResponse.to_dict()."""
        response = ErrorResponse(
            error_type=ErrorType.VALIDATION_ERROR,
            message="Validation failed",
            details={"field": "email"},
            user_friendly="Please provide a valid email",
            status_code=400,
            severity=ErrorSeverity.LOW,
        )
        result = response.to_dict()
        assert isinstance(result, dict)
        assert "error" in result
        assert result["error"]["type"] == ErrorType.VALIDATION_ERROR.value
        assert result["error"]["message"] == "Validation failed"
        assert "details" in result["error"]

    def test_error_response_to_response(self):
        """Test ErrorResponse.to_response()."""
        response = ErrorResponse(
            error_type=ErrorType.RESOURCE_NOT_FOUND,
            message="Not found",
            status_code=404,
        )
        result = response.to_response()
        assert isinstance(result, JSONResponse)
        assert result.status_code == 404


class TestErrorMapping:
    """Test error type and status code mapping functions."""

    def test_map_error_type_authentication(self):
        """Test _map_error_type for AuthenticationError."""
        error = AuthenticationError("Auth failed", details={})
        result = _map_error_type(error)
        assert result == ErrorType.AUTHENTICATION_FAILED

    def test_map_error_type_validation(self):
        """Test _map_error_type for ValidationError."""
        error = ValidationError("Invalid input", details={})
        result = _map_error_type(error)
        assert result == ErrorType.VALIDATION_ERROR

    def test_map_error_type_not_found(self):
        """Test _map_error_type for ResourceNotFoundError."""
        error = ResourceNotFoundError("Not found", details={})
        result = _map_error_type(error)
        assert result == ErrorType.RESOURCE_NOT_FOUND

    def test_map_error_type_rate_limit(self):
        """Test _map_error_type for RateLimitError."""
        error = RateLimitError("Too many requests", details={})
        result = _map_error_type(error)
        assert result == ErrorType.RATE_LIMIT_EXCEEDED

    def test_map_error_type_game_logic(self):
        """Test _map_error_type for GameLogicError."""
        error = GameLogicError("Game logic error", details={})
        result = _map_error_type(error)
        assert result == ErrorType.GAME_LOGIC_ERROR

    def test_map_error_type_database(self):
        """Test _map_error_type for DatabaseError."""
        error = DatabaseError("Database error", details={})
        result = _map_error_type(error)
        assert result == ErrorType.DATABASE_ERROR

    def test_map_error_type_network(self):
        """Test _map_error_type for NetworkError."""
        error = NetworkError("Network error", details={})
        result = _map_error_type(error)
        assert result == ErrorType.NETWORK_ERROR

    def test_map_error_type_configuration(self):
        """Test _map_error_type for ConfigurationError."""
        error = ConfigurationError("Config error", details={})
        result = _map_error_type(error)
        assert result == ErrorType.CONFIGURATION_ERROR

    def test_map_error_type_unknown(self):
        """Test _map_error_type for unknown error type."""
        error = MythosMUDError("Unknown error", details={})
        result = _map_error_type(error)
        assert result == ErrorType.INTERNAL_ERROR

    def test_get_severity_for_error_authentication(self):
        """Test _get_severity_for_error for AuthenticationError."""
        error = AuthenticationError("Auth failed", details={})
        result = _get_severity_for_error(error)
        assert result == ErrorSeverity.LOW

    def test_get_severity_for_error_database(self):
        """Test _get_severity_for_error for DatabaseError."""
        error = DatabaseError("Database error", details={})
        result = _get_severity_for_error(error)
        assert result == ErrorSeverity.HIGH

    def test_get_severity_for_error_configuration(self):
        """Test _get_severity_for_error for ConfigurationError."""
        error = ConfigurationError("Config error", details={})
        result = _get_severity_for_error(error)
        assert result == ErrorSeverity.CRITICAL

    def test_get_severity_for_error_unknown(self):
        """Test _get_severity_for_error for unknown error type."""
        error = MythosMUDError("Unknown error", details={})
        result = _get_severity_for_error(error)
        assert result == ErrorSeverity.MEDIUM

    def test_get_status_code_for_error_authentication(self):
        """Test _get_status_code_for_error for AuthenticationError."""
        error = AuthenticationError("Auth failed", details={})
        result = _get_status_code_for_error(error)
        assert result == 401

    def test_get_status_code_for_error_validation(self):
        """Test _get_status_code_for_error for ValidationError."""
        error = ValidationError("Invalid input", details={})
        result = _get_status_code_for_error(error)
        assert result == 400

    def test_get_status_code_for_error_not_found(self):
        """Test _get_status_code_for_error for ResourceNotFoundError."""
        error = ResourceNotFoundError("Not found", details={})
        result = _get_status_code_for_error(error)
        assert result == 404

    def test_get_status_code_for_error_rate_limit(self):
        """Test _get_status_code_for_error for RateLimitError."""
        error = RateLimitError("Too many requests", details={})
        result = _get_status_code_for_error(error)
        assert result == 429

    def test_get_status_code_for_error_database(self):
        """Test _get_status_code_for_error for DatabaseError."""
        error = DatabaseError("Database error", details={})
        result = _get_status_code_for_error(error)
        assert result == 503

    def test_get_status_code_for_error_unknown(self):
        """Test _get_status_code_for_error for unknown error type."""
        error = MythosMUDError("Unknown error", details={})
        result = _get_status_code_for_error(error)
        assert result == 500


class TestCreateErrorResponse:
    """Test create_error_response function."""

    def test_create_error_response_without_details(self):
        """Test create_error_response without including details."""
        error = ValidationError("Invalid input", details={"field": "email"})
        response = create_error_response(error, include_details=False)
        assert isinstance(response, ErrorResponse)
        assert response.error_type == ErrorType.VALIDATION_ERROR
        assert response.message == "Invalid input"
        assert response.details == {}

    def test_create_error_response_with_details(self):
        """Test create_error_response with details included."""
        error = ValidationError("Invalid input", details={"field": "email", "operation": "register"})
        response = create_error_response(error, include_details=True)
        assert isinstance(response, ErrorResponse)
        assert "field" in response.details
        assert "operation" in response.details

    def test_create_error_response_sanitizes_unsafe_keys(self):
        """Test create_error_response sanitizes unsafe detail keys."""
        error = ValidationError(
            "Invalid input",
            details={"field": "email", "password": "secret123", "operation": "register"},
        )
        response = create_error_response(error, include_details=True)
        assert "field" in response.details
        assert "operation" in response.details
        assert "password" not in response.details


class TestErrorHandlers:
    """Test error handler functions."""

    @pytest.mark.asyncio
    async def test_mythos_exception_handler(self):
        """Test mythos_exception_handler."""
        error = ValidationError("Invalid input", details={"field": "email"})
        request = Mock(spec=Request)
        request.url = Mock()
        request.url.__str__ = Mock(return_value="http://test.com/api")
        request.method = "POST"
        request.app.state = Mock()
        request.app.state.config = {"debug": False}

        result = await mythos_exception_handler(request, error)
        assert isinstance(result, JSONResponse)
        assert result.status_code == 400

    @pytest.mark.asyncio
    async def test_mythos_exception_handler_with_debug(self):
        """Test mythos_exception_handler with debug enabled."""
        error = ValidationError("Invalid input", details={"field": "email", "operation": "register"})
        request = Mock(spec=Request)
        request.url = Mock()
        request.url.__str__ = Mock(return_value="http://test.com/api")
        request.method = "POST"
        request.app.state = Mock()
        request.app.state.config = {"debug": True}

        result = await mythos_exception_handler(request, error)
        assert isinstance(result, JSONResponse)

    @pytest.mark.asyncio
    async def test_mythos_exception_handler_sets_request_id(self):
        """Test mythos_exception_handler sets request_id in context."""
        error = ValidationError("Invalid input", details={})
        error.context = create_error_context()
        request = Mock(spec=Request)
        request.url = Mock()
        request.url.__str__ = Mock(return_value="http://test.com/api")
        request.method = "POST"
        request.app.state = Mock()
        request.app.state.config = {"debug": False}

        await mythos_exception_handler(request, error)
        assert error.context.request_id == "http://test.com/api"

    @pytest.mark.asyncio
    async def test_general_exception_handler(self):
        """Test general_exception_handler."""
        # ValueError is converted to ValidationError (status 400), not 500
        # Use a different exception type that doesn't get converted
        error = RuntimeError("Test error")
        request = Mock(spec=Request)
        request.url = Mock()
        request.url.__str__ = Mock(return_value="http://test.com/api")
        request.method = "GET"
        request.headers = {"user-agent": "test-agent"}
        request.app.state = Mock()
        request.app.state.config = {"debug": False}

        result = await general_exception_handler(request, error)
        assert isinstance(result, JSONResponse)
        assert result.status_code == 500

    @pytest.mark.asyncio
    async def test_logged_http_exception_handler_401(self):
        """Test logged_http_exception_handler for 401."""
        error = LoggedHTTPException(status_code=401, detail="Unauthorized")
        request = Mock(spec=Request)
        request.url = Mock()
        request.url.__str__ = Mock(return_value="http://test.com/api")
        request.method = "GET"

        result = await logged_http_exception_handler(request, error)
        assert isinstance(result, JSONResponse)
        assert result.status_code == 401

    @pytest.mark.asyncio
    async def test_logged_http_exception_handler_404(self):
        """Test logged_http_exception_handler for 404."""
        error = LoggedHTTPException(status_code=404, detail="Not found")
        request = Mock(spec=Request)
        request.url = Mock()
        request.url.__str__ = Mock(return_value="http://test.com/api")
        request.method = "GET"

        result = await logged_http_exception_handler(request, error)
        assert isinstance(result, JSONResponse)
        assert result.status_code == 404

    @pytest.mark.asyncio
    async def test_logged_http_exception_handler_422(self):
        """Test logged_http_exception_handler for 422."""
        error = LoggedHTTPException(status_code=422, detail="Validation error")
        request = Mock(spec=Request)
        request.url = Mock()
        request.url.__str__ = Mock(return_value="http://test.com/api")
        request.method = "POST"

        result = await logged_http_exception_handler(request, error)
        assert isinstance(result, JSONResponse)
        assert result.status_code == 422

    @pytest.mark.asyncio
    async def test_logged_http_exception_handler_429(self):
        """Test logged_http_exception_handler for 429."""
        error = LoggedHTTPException(status_code=429, detail="Rate limit exceeded")
        request = Mock(spec=Request)
        request.url = Mock()
        request.url.__str__ = Mock(return_value="http://test.com/api")
        request.method = "GET"

        result = await logged_http_exception_handler(request, error)
        assert isinstance(result, JSONResponse)
        assert result.status_code == 429

    @pytest.mark.asyncio
    async def test_http_exception_handler_401(self):
        """Test http_exception_handler for 401."""
        from fastapi import HTTPException

        error = HTTPException(status_code=401, detail="Unauthorized")
        request = Mock(spec=Request)
        request.url = Mock()
        request.url.__str__ = Mock(return_value="http://test.com/api")
        request.method = "GET"

        result = await http_exception_handler(request, error)
        assert isinstance(result, JSONResponse)
        assert result.status_code == 401

    @pytest.mark.asyncio
    async def test_http_exception_handler_starlette(self):
        """Test http_exception_handler for StarletteHTTPException."""
        error = StarletteHTTPException(status_code=404, detail="Not found")
        request = Mock(spec=Request)
        request.url = Mock()
        request.url.__str__ = Mock(return_value="http://test.com/api")
        request.method = "GET"

        # Reason: Testing with starlette HTTPException to verify compatibility
        result = await http_exception_handler(request, error)  # type: ignore[arg-type]
        assert isinstance(result, JSONResponse)
        assert result.status_code == 404

    @pytest.mark.asyncio
    async def test_register_error_handlers(self):
        """Test register_error_handlers."""
        app = FastAPI()
        register_error_handlers(app)
        # Verify handlers are registered by checking exception handlers dict
        assert MythosMUDError in app.exception_handlers
        assert LoggedHTTPException in app.exception_handlers
        assert Exception in app.exception_handlers


class TestSanitization:
    """Test sanitization functions."""

    def test_is_safe_detail_key_safe(self):
        """Test _is_safe_detail_key with safe keys."""
        assert _is_safe_detail_key("auth_type") is True
        assert _is_safe_detail_key("operation") is True
        assert _is_safe_detail_key("table") is True
        assert _is_safe_detail_key("field") is True

    def test_is_safe_detail_key_unsafe(self):
        """Test _is_safe_detail_key with unsafe keys."""
        assert _is_safe_detail_key("password") is False
        assert _is_safe_detail_key("secret") is False
        assert _is_safe_detail_key("api_key") is False
        assert _is_safe_detail_key("token") is False
        assert _is_safe_detail_key("credential") is False

    def test_sanitize_detail_value_string(self):
        """Test _sanitize_detail_value with string."""
        result = _sanitize_detail_value("test value")
        assert result == "test value"

    def test_sanitize_detail_value_long_string(self):
        """Test _sanitize_detail_value with long string."""
        long_string = "a" * 150
        result = _sanitize_detail_value(long_string)
        assert len(result) <= 103  # 100 + "..."
        assert result.endswith("...")

    def test_sanitize_detail_value_traceback(self):
        """Test _sanitize_detail_value with traceback-like string."""
        traceback_string = "Traceback (most recent call last):\n  File test.py"
        result = _sanitize_detail_value(traceback_string)
        assert result == "[REDACTED]"

    def test_sanitize_detail_value_int(self):
        """Test _sanitize_detail_value with integer."""
        result = _sanitize_detail_value(42)
        assert result == 42

    def test_sanitize_detail_value_dict(self):
        """Test _sanitize_detail_value with dictionary."""
        # Use "field" which is a safe key according to _is_safe_detail_key()
        value = {"field": "value", "password": "secret"}
        result = _sanitize_detail_value(value)
        assert "field" in result
        assert "password" not in result

    def test_sanitize_detail_value_list(self):
        """Test _sanitize_detail_value with list."""
        value = ["item1", "item2"]
        result = _sanitize_detail_value(value)
        assert isinstance(result, list)
        assert len(result) == 2

    def test_sanitize_context_with_safe_fields(self):
        """Test _sanitize_context with safe fields."""
        context = create_error_context()
        context.user_id = "user123"
        context.room_id = "room456"
        context.command = "look"
        result = _sanitize_context(context)
        assert result is not None
        # Type narrowing: after assert result is not None, result is dict[str, Any]
        # Use .get() to avoid type checker issues with subscript notation
        # This is safe because we've asserted result is not None above
        assert result.get("user_id") == "user123"
        assert result.get("room_id") == "room456"
        assert result.get("command") == "look"

    def test_sanitize_context_none(self):
        """Test _sanitize_context with None."""
        result = _sanitize_context(None)
        assert result is None

    def test_sanitize_context_empty(self):
        """Test _sanitize_context with empty context."""
        context = create_error_context()
        result = _sanitize_context(context)
        # Should return None if no safe fields are present
        assert result is None or isinstance(result, dict)

    def test_sanitize_html_content(self):
        """Test sanitize_html_content."""
        content = "<p>Test</p><script>alert('xss')</script>"
        result = sanitize_html_content(content)
        assert "<p>Test</p>" in result
        assert "<script>" not in result

    def test_sanitize_html_content_with_allowed_tags(self):
        """Test sanitize_html_content with allowed tags."""
        content = "<p>Test</p><div>More</div>"
        result = sanitize_html_content(content, allow_tags=["p", "div"])
        assert "<p>Test</p>" in result
        assert "<div>More</div>" in result

    def test_sanitize_text_content(self):
        """Test sanitize_text_content."""
        content = "<p>Test</p>"
        result = sanitize_text_content(content)
        assert "<p>" not in result
        assert "Test" in result

    def test_sanitize_text_content_long(self):
        """Test sanitize_text_content with long content."""
        content = "a" * 1500
        result = sanitize_text_content(content, max_length=1000)
        assert len(result) <= 1003  # 1000 + "..."
        assert result.endswith("...")


class TestCircuitBreaker:
    """Test CircuitBreaker class."""

    def test_circuit_breaker_initialization(self):
        """Test CircuitBreaker initialization."""
        breaker = CircuitBreaker(failure_threshold=5, timeout=60)
        assert breaker.failure_threshold == 5
        assert breaker.timeout == 60
        assert breaker.failure_count == 0
        assert breaker.state == "CLOSED"

    def test_circuit_breaker_success(self):
        """Test CircuitBreaker with successful call."""
        breaker = CircuitBreaker(failure_threshold=3, timeout=60)

        def success_func():
            return "success"

        result = breaker.call(success_func)
        assert result == "success"
        assert breaker.state == "CLOSED"
        assert breaker.failure_count == 0

    def test_circuit_breaker_failure(self):
        """Test CircuitBreaker with failure."""
        breaker = CircuitBreaker(failure_threshold=2, timeout=60)

        def fail_func():
            raise ValueError("Test error")

        with pytest.raises(ValueError):
            breaker.call(fail_func)
        assert breaker.failure_count == 1
        assert breaker.state == "CLOSED"

    def test_circuit_breaker_opens_after_threshold(self):
        """Test CircuitBreaker opens after threshold."""
        breaker = CircuitBreaker(failure_threshold=2, timeout=60)

        def fail_func():
            raise ValueError("Test error")

        # Fail twice to open circuit
        with pytest.raises(ValueError):
            breaker.call(fail_func)
        with pytest.raises(ValueError):
            breaker.call(fail_func)

        assert breaker.state == "OPEN"
        assert breaker.failure_count == 2

    def test_circuit_breaker_open_raises_error(self):
        """Test CircuitBreaker raises error when open."""
        breaker = CircuitBreaker(failure_threshold=1, timeout=60)
        breaker.state = "OPEN"
        # Set last_failure_time to a recent time so _should_attempt_reset() returns False
        from datetime import datetime, timedelta

        breaker.last_failure_time = datetime.now() - timedelta(seconds=30)

        def success_func():
            return "success"

        with pytest.raises(NetworkError):
            breaker.call(success_func)

    def test_circuit_breaker_half_open_reset(self):
        """Test CircuitBreaker resets from half-open after success."""
        breaker = CircuitBreaker(failure_threshold=1, timeout=1)
        breaker.state = "HALF_OPEN"

        def success_func():
            return "success"

        result = breaker.call(success_func)
        assert result == "success"
        assert breaker.state == "CLOSED"
        assert breaker.failure_count == 0


class TestGracefulDegradation:
    """Test graceful_degradation context manager."""

    def test_graceful_degradation_success(self):
        """Test graceful_degradation with successful operation."""
        with graceful_degradation("fallback", "test_error"):
            pass  # No exception raised

    def test_graceful_degradation_failure(self):
        """Test graceful_degradation catches exceptions."""
        with graceful_degradation("fallback", "test_error"):
            raise ValueError("Test error")
        # Should not raise, but log the error
