"""
Centralized error handling for MythosMUD FastAPI application.

This module provides consistent error response handling and graceful
degradation strategies. As the Necronomicon teaches us, even in the
face of eldritch horrors, we must maintain order and structure.
"""

import traceback
from contextlib import contextmanager
from datetime import datetime
from typing import Any

from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from .exceptions import (
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
    handle_exception,
)
from .logging_config import get_logger

logger = get_logger(__name__)


class ErrorResponse:
    """
    Standardized error response format.

    Provides consistent error responses across all API endpoints,
    following the dimensional mapping principles for error categorization.
    """

    def __init__(
        self,
        error_type: str,
        message: str,
        details: dict[str, Any] | None = None,
        user_friendly: str | None = None,
        status_code: int = 500,
    ):
        self.error_type = error_type
        self.message = message
        self.details = details or {}
        self.user_friendly = user_friendly or message
        self.status_code = status_code

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary for JSON response."""
        return {
            "error": {
                "type": self.error_type,
                "message": self.message,
                "user_friendly": self.user_friendly,
                "details": self.details,
            }
        }

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
    # Determine status code based on error type
    status_code = _get_status_code_for_error(error)

    # Create response details
    details = {}
    if include_details:
        details = error.details.copy()
        details["context"] = error.context.to_dict()

    return ErrorResponse(
        error_type=error.__class__.__name__,
        message=error.message,
        details=details,
        user_friendly=error.user_friendly,
        status_code=status_code,
    )


def _get_status_code_for_error(error: MythosMUDError) -> int:
    """Get appropriate HTTP status code for error type."""
    if isinstance(error, AuthenticationError):
        return 401
    elif isinstance(error, ValidationError):
        return 400
    elif isinstance(error, ResourceNotFoundError):
        return 404
    elif isinstance(error, RateLimitError):
        return 429
    elif isinstance(error, GameLogicError):
        return 422
    elif isinstance(error, DatabaseError):
        return 503  # Service unavailable for database errors
    elif isinstance(error, NetworkError):
        return 503
    elif isinstance(error, ConfigurationError):
        return 500
    else:
        return 500


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
    # Safely get debug setting from app state, default to False
    try:
        include_details = request.app.state.config.get("debug", False)
    except (AttributeError, KeyError):
        include_details = False
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
    # Safely get debug setting from app state, default to False
    try:
        include_details = request.app.state.config.get("debug", False)
    except (AttributeError, KeyError):
        include_details = False
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


async def http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
    """
    Handle FastAPI HTTP exceptions.

    Args:
        request: FastAPI request object
        exc: HTTP exception

    Returns:
        JSONResponse with error details
    """
    context = create_error_context(
        request_id=str(request.url),
        metadata={
            "path": str(request.url),
            "method": request.method,
        },
    )

    # Convert to MythosMUD error
    if exc.status_code == 401:
        mythos_error = AuthenticationError(str(exc.detail), context)
    elif exc.status_code == 404:
        mythos_error = ResourceNotFoundError(str(exc.detail), context)
    elif exc.status_code == 422:
        mythos_error = ValidationError(str(exc.detail), context)
    else:
        mythos_error = MythosMUDError(str(exc.detail), context)

    # Create error response
    # Safely get debug setting from app state, default to False
    try:
        include_details = request.app.state.config.get("debug", False)
    except (AttributeError, KeyError):
        include_details = False
    error_response = create_error_response(mythos_error, include_details=include_details)

    # Override status code from HTTP exception
    error_response.status_code = exc.status_code

    logger.warning(
        "HTTP exception handled",
        status_code=exc.status_code,
        detail=exc.detail,
        path=str(request.url),
        method=request.method,
    )

    return error_response.to_response()


@contextmanager
def graceful_degradation(fallback_value: Any, error_type: str = "unknown"):
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
    except Exception as exc:
        logger.warning(
            "Graceful degradation applied",
            error_type=error_type,
            original_error=str(exc),
            fallback_value=fallback_value,
        )
        # Return fallback value (this will be handled by the calling code)


def register_error_handlers(app):
    """
    Register all error handlers with the FastAPI application.

    Args:
        app: FastAPI application instance
    """
    # Register MythosMUD exception handler
    app.add_exception_handler(MythosMUDError, mythos_exception_handler)

    # Register general exception handler
    app.add_exception_handler(Exception, general_exception_handler)

    # Register HTTP exception handler
    app.add_exception_handler(HTTPException, http_exception_handler)
    app.add_exception_handler(StarletteHTTPException, http_exception_handler)

    logger.info("Error handlers registered with FastAPI application")


class CircuitBreaker:
    """
    Simple circuit breaker pattern implementation.

    Provides fault tolerance for external dependencies by temporarily
    failing fast when errors exceed thresholds.
    """

    def __init__(self, failure_threshold: int = 5, timeout: int = 60):
        self.failure_threshold = failure_threshold
        self.timeout = timeout
        self.failure_count = 0
        self.last_failure_time = None
        self.state = "CLOSED"  # CLOSED, OPEN, HALF_OPEN

    def call(self, func, *args, **kwargs):
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

    def _on_success(self):
        """Handle successful operation."""
        self.failure_count = 0
        self.state = "CLOSED"

    def _on_failure(self):
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
