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

import bleach
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
    elif isinstance(value, int | float | bool):
        return value
    elif isinstance(value, dict):
        return {k: _sanitize_detail_value(v) for k, v in value.items() if _is_safe_detail_key(k)}
    elif isinstance(value, list):
        return [_sanitize_detail_value(v) for v in value]
    else:
        # Convert to string and sanitize
        str_value = str(value)
        if len(str_value) > 100:
            str_value = str_value[:100] + "..."
        return _sanitize_detail_value(str_value)


def _sanitize_context(context) -> dict[str, Any] | None:
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

    return sanitized


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

    return sanitized
