"""
Centralized error handling for MythosMUD FastAPI application.

This module provides consistent error response handling and graceful
degradation strategies. As the Necronomicon teaches us, even in the
face of eldritch horrors, we must maintain order and structure.
"""

# pylint: disable=too-many-return-statements,too-many-lines  # Reason: Error handlers require multiple return statements for different error type handling and response generation. Error handling module requires comprehensive coverage of all error scenarios.

import traceback
from collections.abc import Iterator
from contextlib import contextmanager
from datetime import datetime
from typing import Any

import bleach
from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from .error_types import ErrorMessages, ErrorSeverity, ErrorType, create_standard_error_response
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
from .structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


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
        details: dict[str, Any] | None = None,
        user_friendly: str | None = None,
        status_code: int = 500,
        severity: ErrorSeverity = ErrorSeverity.MEDIUM,
    ):
        self.error_type = error_type
        self.message = message
        self.details = details or {}
        self.user_friendly = user_friendly or message
        self.status_code = status_code
        self.severity = severity

    def to_dict(self) -> dict[str, Any]:
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
    details = {}
    if include_details:
        # Only include safe, non-sensitive details
        safe_details = {}
        for key, value in error.details.items():
            if _is_safe_detail_key(key):
                safe_details[key] = _sanitize_detail_value(value)

        # Include sanitized context (only safe fields)
        safe_context = _sanitize_context(error.context)

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
    error_type_mapping = {
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
    severity_mapping = {
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
    status_code_mapping = {
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
def graceful_degradation(fallback_value: Any, error_type: str = "unknown") -> Iterator[None]:
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


def register_error_handlers(app: Any) -> None:
    """
    Register all error handlers with the FastAPI application.

    Args:
        app: FastAPI application instance
    """
    # Register MythosMUD exception handler
    app.add_exception_handler(MythosMUDError, mythos_exception_handler)

    # Register LoggedHTTPException handler (must be before generic HTTPException)
    app.add_exception_handler(LoggedHTTPException, logged_http_exception_handler)

    # Register general exception handler
    app.add_exception_handler(Exception, general_exception_handler)

    # Register HTTP exception handler
    app.add_exception_handler(HTTPException, http_exception_handler)
    app.add_exception_handler(StarletteHTTPException, http_exception_handler)

    logger.info("Error handlers registered with FastAPI application")


class CircuitBreaker:  # pylint: disable=too-few-public-methods  # Reason: Utility class with focused responsibility, minimal public interface
    """
    Simple circuit breaker pattern implementation.

    Provides fault tolerance for external dependencies by temporarily
    failing fast when errors exceed thresholds.
    """

    def __init__(self, failure_threshold: int = 5, timeout: int = 60):
        self.failure_threshold = failure_threshold
        self.timeout = timeout
        self.failure_count = 0
        self.last_failure_time: datetime | None = None
        self.state = "CLOSED"  # CLOSED, OPEN, HALF_OPEN

    def call(self, func: Any, *args: Any, **kwargs: Any) -> Any:
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


def _is_safe_detail_key(key: str) -> bool:
    """
    Check if a detail key is safe to expose to users.

    Args:
        key: The detail key to check

    Returns:
        True if the key is safe to expose, False otherwise
    """
    # Safe keys that don't expose sensitive information
    safe_keys = {
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
    }

    # Block keys that might contain sensitive information
    unsafe_patterns = [
        "password",
        "secret",
        "key",
        "token",
        "credential",
        "path",
        "file",
        "sql",
        "query",
        "stack",
        "trace",
        "internal",
        "debug",
        "sensitive",
        "private",
    ]

    key_lower = key.lower()

    # Check if key is explicitly safe
    if key in safe_keys:
        return True

    # Check if key contains unsafe patterns
    for pattern in unsafe_patterns:
        if pattern in key_lower:
            return False

    return True


def _sanitize_detail_value(value: Any) -> Any:
    """
    Sanitize a detail value to prevent information exposure.

    Uses bleach for HTML sanitization and custom logic for error-specific patterns.

    Args:
        value: The value to sanitize

    Returns:
        Sanitized value safe for user exposure
    """
    if isinstance(value, str):
        # First check for sensitive patterns that should be redacted
        if any(pattern in value.lower() for pattern in ["traceback", "stack", "file:", "line:", "/", "\\"]):
            return "[REDACTED]"

        # Use bleach to sanitize any HTML content
        # This prevents XSS if error messages contain HTML
        sanitized = bleach.clean(
            value,
            tags=[],  # No HTML tags allowed
            attributes={},  # No attributes allowed
            strip=True,  # Strip all HTML
            strip_comments=True,  # Strip comments
        )

        # Limit length to prevent information disclosure
        if len(sanitized) > 100:
            return sanitized[:100] + "..."

        return sanitized
    if isinstance(value, int | float | bool):
        return value
    if isinstance(value, dict):
        return {k: _sanitize_detail_value(v) for k, v in value.items() if _is_safe_detail_key(k)}
    if isinstance(value, list):
        return [_sanitize_detail_value(v) for v in value]
    # Convert to string and sanitize
    str_value = str(value)
    if len(str_value) > 100:
        str_value = str_value[:100] + "..."
    return _sanitize_detail_value(str_value)


def _sanitize_context(context: Any) -> dict[str, Any] | None:
    """
    Sanitize error context to prevent information exposure.

    Args:
        context: The error context to sanitize

    Returns:
        Sanitized context dict or None if no safe fields
    """
    if not context:
        return None

    safe_context = {}

    # Only include safe, non-sensitive context fields
    safe_fields = ["user_id", "room_id", "command", "session_id", "request_id"]

    for field in safe_fields:
        if hasattr(context, field):
            value = getattr(context, field)
            if value is not None:
                safe_context[field] = _sanitize_detail_value(value)

    # Include timestamp if available
    if hasattr(context, "timestamp") and context.timestamp:
        safe_context["timestamp"] = context.timestamp.isoformat()

    # Sanitize metadata if present
    if hasattr(context, "metadata") and context.metadata:
        safe_metadata = {}
        for key, value in context.metadata.items():
            if _is_safe_detail_key(key):
                safe_metadata[key] = _sanitize_detail_value(value)
        if safe_metadata:
            safe_context["metadata"] = safe_metadata

    return safe_context if safe_context else None


def sanitize_html_content(content: str, allow_tags: list[str] | None = None) -> str:
    """
    Sanitize HTML content to prevent XSS attacks.

    This is a general utility function that can be used throughout the application
    for sanitizing user-provided HTML content.

    Args:
        content: The HTML content to sanitize
        allow_tags: List of allowed HTML tags (default: basic formatting only)

    Returns:
        Sanitized HTML content
    """
    if not content:
        return ""

    # Default safe tags for basic formatting
    if allow_tags is None:
        allow_tags = ["p", "br", "strong", "em", "u", "i", "b", "ul", "ol", "li", "h1", "h2", "h3", "h4", "h5", "h6"]

    # Default safe attributes
    safe_attributes = {
        "p": ["class"],
        "span": ["class"],
        "div": ["class"],
        "h1": ["class"],
        "h2": ["class"],
        "h3": ["class"],
        "h4": ["class"],
        "h5": ["class"],
        "h6": ["class"],
    }

    # Sanitize the content
    sanitized = bleach.clean(
        content,
        tags=allow_tags,
        attributes=safe_attributes,
        strip=True,
        strip_comments=True,
    )

    return str(sanitized)  # Explicit str for mypy no-any-return (bleach.clean returns str)


def sanitize_text_content(content: str, max_length: int = 1000) -> str:
    """
    Sanitize plain text content to prevent information exposure.

    Args:
        content: The text content to sanitize
        max_length: Maximum allowed length (default: 1000 characters)

    Returns:
        Sanitized text content
    """
    if not content:
        return ""

    # Remove any HTML tags
    sanitized = bleach.clean(content, tags=[], strip=True)

    # Limit length
    if len(sanitized) > max_length:
        sanitized = sanitized[:max_length] + "..."

    return str(sanitized)  # Explicit str for mypy no-any-return (bleach.clean returns str)
