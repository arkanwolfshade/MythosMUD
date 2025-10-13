"""
Tests for legacy error handlers module.

This module tests the centralized error handling for the FastAPI application,
following the ancient principles of proper error categorization as outlined
in the Necronomicon of Software Testing.
"""

from unittest.mock import Mock, patch

import pytest
from fastapi import Request

from server.error_types import ErrorSeverity, ErrorType
from server.exceptions import (
    AuthenticationError,
    ConfigurationError,
    DatabaseError,
    GameLogicError,
    MythosMUDError,
    NetworkError,
    RateLimitError,
    ResourceNotFoundError,
    ValidationError,
    create_error_context,
)
from server.legacy_error_handlers import (
    ErrorResponse,
    create_error_response,
    general_exception_handler,
    mythos_exception_handler,
)


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
        response = ErrorResponse(
            error_type=ErrorType.AUTHENTICATION_FAILED, message="Auth failed", status_code=401
        )

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
        error = ValidationError("Invalid input", field="username")

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
        error = ValidationError("Invalid data", field="email", details={"field": "email"}, context=context)

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
        error = ValidationError("Test validation error")

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

        error = ValidationError("Test error")

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
