"""
Centralized error handling for MythosMUD FastAPI application.

This module provides consistent error response handling and graceful
degradation strategies. As the Necronomicon teaches us, even in the
face of eldritch horrors, we must maintain order and structure.
"""

# pylint: disable=too-many-return-statements  # Reason: Error handlers require multiple return statements for different error type handling and response generation.

import traceback
from collections.abc import Awaitable, Callable, Generator
from contextlib import contextmanager
from datetime import datetime
from typing import Literal, Protocol, TypeVar, cast

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.responses import Response

from .error_types import (
    ErrorMessages,
    ErrorResponseDetailsInput,
    ErrorSeverity,
    ErrorType,
    HttpStandardErrorResponse,
    create_standard_error_response,
)
from .exceptions import (
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
    handle_exception,
)
from .legacy_error_sanitization import (
    sanitize_context,
    sanitize_html_content,
    sanitize_safe_details,
    sanitize_text_content,
)
from .structured_logging.enhanced_logging_config import get_logger

_CircuitBreakerResult = TypeVar("_CircuitBreakerResult")

__all__ = [
    "CircuitBreaker",
    "ErrorResponse",
    "create_error_response",
    "general_exception_handler",
    "graceful_degradation",
    "http_exception_handler",
    "logged_http_exception_handler",
    "mythos_exception_handler",
    "register_error_handlers",
    "sanitize_html_content",
    "sanitize_text_content",
]

logger = get_logger(__name__)

# Starlette types HTTP exception handlers as (Request, Exception) -> ...; narrower handlers are safe
# at runtime because the router only invokes them for the registered exception type.
HttpExceptionHandler = Callable[[Request, Exception], Awaitable[Response]]


class _AppStateWithLegacyConfig(Protocol):
    """Minimal app.state shape for legacy error-handler debug config."""

    config: dict[str, bool]


class _AppWithLegacyConfigState(Protocol):
    """Minimal FastAPI app shape for reading legacy config from state."""

    state: _AppStateWithLegacyConfig


def _include_error_details_from_request(request: Request) -> bool:
    """Safely read the debug flag from app.state.config; defaults to False."""
    try:
        app_state = cast(_AppWithLegacyConfigState, request.app).state
        return app_state.config.get("debug", False)
    except (AttributeError, KeyError):
        return False


class ErrorResponse:
    """
    Standardized error response format.

    Provides consistent error responses across all API endpoints,
    following the dimensional mapping principles for error categorization.
    """

    def __init__(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Error handler initialization requires many parameters for context and formatting
        self,
        error_type: ErrorType,
        message: str,
        details: ErrorResponseDetailsInput | None = None,
        user_friendly: str | None = None,
        status_code: int = 500,
        severity: ErrorSeverity = ErrorSeverity.MEDIUM,
    ) -> None:
        self.error_type: ErrorType = error_type
        self.message: str = message
        self.details: ErrorResponseDetailsInput = details if details is not None else {}
        self.user_friendly: str = user_friendly or message
        self.status_code: int = status_code
        self.severity: ErrorSeverity = severity

    def to_dict(self) -> HttpStandardErrorResponse:
        """Convert to dictionary for JSON response."""
        return create_standard_error_response(
            self.error_type,
            self.message,
            self.user_friendly,
            self.details,
            self.severity,
        )

    def to_response(self) -> JSONResponse:
        """Convert to FastAPI JSONResponse."""
        return JSONResponse(status_code=self.status_code, content=self.to_dict())


def create_error_response(error: MythosMUDError, include_details: bool = False) -> ErrorResponse:
    """
    Create a standardized error response from a MythosMUD error.

    Args:
        error: The MythosMUD error
        include_details: Whether to include detailed error information

    Returns:
        ErrorResponse object
    """
    # Map MythosMUD error types to standardized error types
    error_type = _map_error_type(error)

    # Determine status code based on error type
    status_code = _get_status_code_for_error(error)

    # Determine severity based on error type
    severity = _get_severity_for_error(error)

    # Create response details - always sanitize to prevent information exposure
    details: dict[str, object] = {}
    if include_details:
        # Only include safe, non-sensitive details
        details_source = cast(dict[str, object], error.details)
        safe_details = sanitize_safe_details(details_source)

        # Include sanitized context (only safe fields)
        safe_context = sanitize_context(error.context)

        details = safe_details
        if safe_context:
            details["context"] = safe_context

    return ErrorResponse(
        error_type=error_type,
        message=error.message,
        details=details,
        user_friendly=error.user_friendly,
        status_code=status_code,
        severity=severity,
    )


def _map_error_type(error: MythosMUDError) -> ErrorType:
    """Map MythosMUD error types to standardized error types."""
    # Error type mapping factory - provides O(1) lookup and easy extensibility
    # As noted in the restricted archives, this pattern eliminates the need for
    # lengthy if/elif chains while maintaining type safety
    error_type_mapping: dict[type[MythosMUDError], ErrorType] = {
        AuthenticationError: ErrorType.AUTHENTICATION_FAILED,
        ValidationError: ErrorType.VALIDATION_ERROR,
        ResourceNotFoundError: ErrorType.RESOURCE_NOT_FOUND,
        RateLimitError: ErrorType.RATE_LIMIT_EXCEEDED,
        GameLogicError: ErrorType.GAME_LOGIC_ERROR,
        DatabaseError: ErrorType.DATABASE_ERROR,
        NetworkError: ErrorType.NETWORK_ERROR,
        ConfigurationError: ErrorType.CONFIGURATION_ERROR,
    }

    return error_type_mapping.get(type(error), ErrorType.INTERNAL_ERROR)


def _get_severity_for_error(error: MythosMUDError) -> ErrorSeverity:
    """Get appropriate severity level for error type."""
    # Severity mapping factory - maps error types to their appropriate severity levels
    # This pattern allows for easy adjustment of severity levels without code changes
    severity_mapping: dict[type[MythosMUDError], ErrorSeverity] = {
        AuthenticationError: ErrorSeverity.LOW,
        ValidationError: ErrorSeverity.LOW,
        ResourceNotFoundError: ErrorSeverity.LOW,
        GameLogicError: ErrorSeverity.MEDIUM,
        RateLimitError: ErrorSeverity.MEDIUM,
        DatabaseError: ErrorSeverity.HIGH,
        NetworkError: ErrorSeverity.HIGH,
        ConfigurationError: ErrorSeverity.CRITICAL,
    }

    return severity_mapping.get(type(error), ErrorSeverity.MEDIUM)


def _get_status_code_for_error(error: MythosMUDError) -> int:
    """Get appropriate HTTP status code for error type."""
    # Status code mapping factory - provides consistent HTTP status code mapping
    # This eliminates the need for repetitive if/elif chains and centralizes status code logic
    status_code_mapping: dict[type[MythosMUDError], int] = {
        AuthenticationError: 401,
        ValidationError: 400,
        ResourceNotFoundError: 404,
        RateLimitError: 429,
        GameLogicError: 422,
        DatabaseError: 503,  # Service unavailable for database errors
        NetworkError: 503,
        ConfigurationError: 500,
    }

    return status_code_mapping.get(type(error), 500)


async def mythos_exception_handler(request: Request, exc: MythosMUDError) -> JSONResponse:
    """
    Handle MythosMUD-specific exceptions.

    Args:
        request: FastAPI request object
        exc: MythosMUD exception

    Returns:
        JSONResponse with error details
    """
    # Add request context to error
    if not exc.context.request_id:
        exc.context.request_id = str(request.url)

    # Create error response
    include_details = _include_error_details_from_request(request)
    error_response = create_error_response(exc, include_details=include_details)

    # Log the error with request context
    logger.error(
        "MythosMUD exception handled",
        error_type=exc.__class__.__name__,
        message=exc.message,
        path=str(request.url),
        method=request.method,
        status_code=error_response.status_code,
        context=exc.context.to_dict(),
    )

    return error_response.to_response()


async def general_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    """
    Handle all other exceptions.

    Args:
        request: FastAPI request object
        exc: Generic exception

    Returns:
        JSONResponse with error details
    """
    # Convert to MythosMUD error
    context = create_error_context(
        request_id=str(request.url),
        metadata={
            "path": str(request.url),
            "method": request.method,
            "user_agent": request.headers.get("user-agent", ""),
        },
    )

    mythos_error = handle_exception(exc, context)

    # Create error response
    include_details = _include_error_details_from_request(request)
    error_response = create_error_response(mythos_error, include_details=include_details)

    # Log the error
    logger.error(
        "Unhandled exception converted to MythosMUD error",
        original_type=type(exc).__name__,
        original_message=str(exc),
        mythos_error_type=mythos_error.__class__.__name__,
        path=str(request.url),
        method=request.method,
        status_code=error_response.status_code,
        traceback=traceback.format_exc(),
    )

    return error_response.to_response()


async def logged_http_exception_handler(request: Request, exc: LoggedHTTPException) -> JSONResponse:
    """
    Handle LoggedHTTPException instances.

    Args:
        request: FastAPI request object
        exc: LoggedHTTPException instance

    Returns:
        JSONResponse with error details
    """
    # Map HTTP status codes to appropriate error types and messages
    if exc.status_code == 401:
        error_type = ErrorType.AUTHENTICATION_FAILED
        user_friendly = ErrorMessages.AUTHENTICATION_REQUIRED
    elif exc.status_code == 404:
        error_type = ErrorType.RESOURCE_NOT_FOUND
        user_friendly = ErrorMessages.PLAYER_NOT_FOUND
    elif exc.status_code == 422:
        error_type = ErrorType.VALIDATION_ERROR
        user_friendly = ErrorMessages.INVALID_INPUT
    elif exc.status_code == 429:
        error_type = ErrorType.RATE_LIMIT_EXCEEDED
        user_friendly = ErrorMessages.TOO_MANY_REQUESTS
    else:
        error_type = ErrorType.INTERNAL_ERROR
        user_friendly = ErrorMessages.INTERNAL_ERROR

    # Create standardized error response
    error_response = create_standard_error_response(
        error_type=error_type,
        message=str(exc.detail),
        user_friendly=user_friendly,
        details={"status_code": exc.status_code},
        severity=ErrorSeverity.MEDIUM,
    )

    # Handle WebSocket vs HTTP request differences
    method = getattr(request, "method", "WEBSOCKET") if hasattr(request, "method") else "WEBSOCKET"

    # LoggedHTTPException already logs the error, so we just log the handling
    logger.info(
        "LoggedHTTPException handled",
        status_code=exc.status_code,
        detail=exc.detail,
        path=str(request.url),
        method=method,
        error_type=error_type.value,
    )

    return JSONResponse(status_code=exc.status_code, content=error_response)


async def http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
    """
    Handle FastAPI HTTP exceptions.

    Args:
        request: FastAPI request object
        exc: HTTP exception

    Returns:
        JSONResponse with error details
    """

    # Map HTTP status codes to appropriate error types and messages
    if exc.status_code == 401:
        error_type = ErrorType.AUTHENTICATION_FAILED
        user_friendly = ErrorMessages.AUTHENTICATION_REQUIRED
    elif exc.status_code == 404:
        error_type = ErrorType.RESOURCE_NOT_FOUND
        user_friendly = ErrorMessages.PLAYER_NOT_FOUND
    elif exc.status_code == 422:
        error_type = ErrorType.VALIDATION_ERROR
        user_friendly = ErrorMessages.INVALID_INPUT
    elif exc.status_code == 429:
        error_type = ErrorType.RATE_LIMIT_EXCEEDED
        user_friendly = ErrorMessages.TOO_MANY_REQUESTS
    else:
        error_type = ErrorType.INTERNAL_ERROR
        user_friendly = ErrorMessages.INTERNAL_ERROR

    # Create standardized error response
    error_response = create_standard_error_response(
        error_type=error_type,
        message=str(exc.detail),
        user_friendly=user_friendly,
        details={"status_code": exc.status_code},
        severity=ErrorSeverity.MEDIUM,
    )

    # Handle WebSocket vs HTTP request differences
    method = getattr(request, "method", "WEBSOCKET") if hasattr(request, "method") else "WEBSOCKET"

    logger.warning(
        "HTTP exception handled",
        status_code=exc.status_code,
        detail=exc.detail,
        path=str(request.url),
        method=method,
        error_type=error_type.value,
    )

    return JSONResponse(status_code=exc.status_code, content=error_response)


@contextmanager
def graceful_degradation(fallback_value: object, error_type: str = "unknown") -> Generator[None]:
    """
    Context manager for graceful degradation.

    Provides fallback behavior when operations fail, following the
    principles of dimensional stability described in the restricted archives.

    Args:
        fallback_value: Value to return if operation fails
        error_type: Type of error for logging

    Yields:
        None
    """
    try:
        yield
    except Exception as exc:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Graceful degradation must catch all errors
        logger.warning(
            "Graceful degradation applied",
            error_type=error_type,
            original_error=str(exc),
            fallback_value=fallback_value,
        )
        # Return fallback value (this will be handled by the calling code)


def register_error_handlers(app: FastAPI) -> None:
    """
    Register all error handlers with the FastAPI application.

    Args:
        app: FastAPI application instance
    """
    # Register MythosMUD exception handler
    app.add_exception_handler(MythosMUDError, cast(HttpExceptionHandler, mythos_exception_handler))

    # Register LoggedHTTPException handler (must be before generic HTTPException)
    app.add_exception_handler(LoggedHTTPException, cast(HttpExceptionHandler, logged_http_exception_handler))

    # Register general exception handler
    app.add_exception_handler(Exception, general_exception_handler)

    # Register HTTP exception handler
    app.add_exception_handler(HTTPException, cast(HttpExceptionHandler, http_exception_handler))
    app.add_exception_handler(StarletteHTTPException, cast(HttpExceptionHandler, http_exception_handler))

    logger.info("Error handlers registered with FastAPI application")


class CircuitBreaker:  # pylint: disable=too-few-public-methods  # Reason: Utility class with focused responsibility, minimal public interface
    """
    Simple circuit breaker pattern implementation.

    Provides fault tolerance for external dependencies by temporarily
    failing fast when errors exceed thresholds.
    """

    def __init__(self, failure_threshold: int = 5, timeout: int = 60) -> None:
        self.failure_threshold: int = failure_threshold
        self.timeout: int = timeout
        self.failure_count: int = 0
        self.last_failure_time: datetime | None = None
        self.state: Literal["CLOSED", "OPEN", "HALF_OPEN"] = "CLOSED"

    def call(
        self,
        func: Callable[..., _CircuitBreakerResult],
        *args: object,
        **kwargs: object,
    ) -> _CircuitBreakerResult:
        """
        Execute function with circuit breaker protection.

        Args:
            func: Function to execute
            *args: Function arguments
            **kwargs: Function keyword arguments

        Returns:
            Function result

        Raises:
            Exception: If circuit breaker is open or function fails
        """
        if self.state == "OPEN":
            if self._should_attempt_reset():
                self.state = "HALF_OPEN"
            else:
                raise NetworkError("Circuit breaker is open", details={"circuit_state": self.state})

        try:
            result = func(*args, **kwargs)
            self._on_success()
            return result
        except Exception as exc:
            self._on_failure()
            raise exc

    def _on_success(self) -> None:
        """Handle successful operation."""
        self.failure_count = 0
        self.state = "CLOSED"

    def _on_failure(self) -> None:
        """Handle failed operation."""
        self.failure_count += 1
        self.last_failure_time = datetime.now()

        if self.failure_count >= self.failure_threshold:
            self.state = "OPEN"

    def _should_attempt_reset(self) -> bool:
        """Check if circuit breaker should attempt reset."""
        if not self.last_failure_time:
            return True

        time_since_failure = (datetime.now() - self.last_failure_time).total_seconds()
        return time_since_failure >= self.timeout
