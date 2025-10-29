"""
Enhanced error logging utilities with structured logging and context management.

This module provides enhanced error logging functions that use proper structured
logging instead of the incorrect context parameter pattern. It integrates with
the enhanced logging system to provide better error tracking and debugging.

As the Pnakotic Manuscripts teach us, proper documentation of anomalies is
essential for understanding the deeper mysteries of our digital realm.
"""

import traceback
from typing import Any

from fastapi import HTTPException, Request
from fastapi.websockets import WebSocket

from ..exceptions import (
    AuthenticationError,
    ConfigurationError,
    DatabaseError,
    ErrorContext,
    MythosMUDError,
    NetworkError,
    ValidationError,
    create_error_context,
)
from ..logging.enhanced_logging_config import get_logger, log_with_context

logger = get_logger(__name__)

# Third-party exception mapping for proper error categorization
THIRD_PARTY_EXCEPTION_MAPPING = {
    # Database exceptions
    "sqlite3.Error": DatabaseError,
    "sqlite3.OperationalError": DatabaseError,
    "sqlite3.IntegrityError": DatabaseError,
    "sqlite3.DatabaseError": DatabaseError,
    "aiosqlite.Error": DatabaseError,
    "aiosqlite.OperationalError": DatabaseError,
    "aiosqlite.IntegrityError": DatabaseError,
    "aiosqlite.DatabaseError": DatabaseError,
    # Authentication exceptions
    "argon2.exceptions.HashingError": AuthenticationError,
    "argon2.exceptions.VerificationError": AuthenticationError,
    "argon2.exceptions.InvalidHash": AuthenticationError,
    "argon2.exceptions.VerifyMismatchError": AuthenticationError,
    # Network exceptions
    "httpx.RequestError": NetworkError,
    "httpx.TimeoutException": NetworkError,
    "httpx.ConnectError": NetworkError,
    "httpx.HTTPStatusError": NetworkError,
    # Validation exceptions
    "pydantic.ValidationError": ValidationError,
    "pydantic.error_wrappers.ValidationError": ValidationError,
    # Configuration exceptions
    "yaml.YAMLError": ConfigurationError,
    "yaml.scanner.ScannerError": ConfigurationError,
    "yaml.parser.ParserError": ConfigurationError,
}


def log_and_raise_enhanced(
    exception_class: type[MythosMUDError],
    message: str,
    context: ErrorContext | None = None,
    details: dict[str, Any] | None = None,
    user_friendly: str | None = None,
    logger_name: str | None = None,
    **kwargs,
) -> None:
    """
    Enhanced log and raise function with proper structured logging.

    This function provides a standardized way to log errors with proper context
    before raising exceptions, using structured logging instead of the incorrect
    context parameter pattern.

    Args:
        exception_class: The MythosMUD exception class to raise
        message: Technical error message
        context: Error context information
        details: Additional error details
        user_friendly: User-friendly error message
        logger_name: Specific logger name to use (defaults to current module)
        **kwargs: Additional structured logging data

    Raises:
        The specified MythosMUD exception
    """
    # Use specified logger or default to current module logger
    error_logger = get_logger(logger_name) if logger_name else logger

    # Create context if not provided
    if context is None:
        context = create_error_context()

    # Prepare structured log data
    log_data = {
        "error_type": exception_class.__name__,
        "error_message": message,
        "user_friendly": user_friendly,
        "context": context.to_dict() if context else {},
        "details": details or {},
        **kwargs,
    }

    # Log the error with structured data
    log_with_context(error_logger, "error", f"Error logged and exception raised: {message}", **log_data)

    # Raise the exception
    raise exception_class(
        message=message,
        context=context,
        details=details,
        user_friendly=user_friendly,
    )


def log_and_raise_http_enhanced(
    status_code: int, detail: str, context: ErrorContext | None = None, logger_name: str | None = None, **kwargs
) -> None:
    """
    Enhanced HTTP error logging with structured logging.

    This function provides a standardized way to log HTTP errors with proper
    context before raising HTTPExceptions, using structured logging.

    Args:
        status_code: HTTP status code
        detail: Error detail message
        context: Error context information
        logger_name: Specific logger name to use (defaults to current module)
        **kwargs: Additional structured logging data

    Raises:
        HTTPException with the specified status code and detail
    """
    # Use specified logger or default to current module logger
    error_logger = get_logger(logger_name) if logger_name else logger

    # Create context if not provided
    if context is None:
        context = create_error_context()

    # Prepare structured log data
    log_data = {
        "error_type": "HTTPException",
        "status_code": status_code,
        "detail": detail,
        "context": context.to_dict() if context else {},
        **kwargs,
    }

    # Log the HTTP error with structured data
    log_with_context(error_logger, "warning", f"HTTP error logged and exception raised: {detail}", **log_data)

    # Raise the HTTPException
    raise HTTPException(status_code=status_code, detail=detail)


def log_structured_error(
    error: Exception,
    context: ErrorContext | None = None,
    logger_name: str | None = None,
    level: str = "error",
    **kwargs,
) -> None:
    """
    Log an error with structured context information.

    This function provides a standardized way to log errors with comprehensive
    context information for debugging and monitoring.

    Args:
        error: The exception to log
        context: Error context information
        logger_name: Specific logger name to use (defaults to current module)
        level: Log level (debug, info, warning, error, critical)
        **kwargs: Additional structured logging data
    """
    # Use specified logger or default to current module logger
    error_logger = get_logger(logger_name) if logger_name else logger

    # Create context if not provided
    if context is None:
        context = create_error_context()

    # Prepare structured log data
    log_data = {
        "error_type": error.__class__.__name__,
        "error_message": str(error),
        "context": context.to_dict() if context else {},
        "traceback": traceback.format_exc(),
        **kwargs,
    }

    # Log with structured data
    log_with_context(error_logger, level, f"Error logged with context: {str(error)}", **log_data)


def wrap_third_party_exception_enhanced(
    exc: Exception, context: ErrorContext | None = None, logger_name: str | None = None, **kwargs
) -> MythosMUDError:
    """
    Enhanced wrapper for third-party exceptions with structured logging.

    This function converts external library exceptions to our internal error
    taxonomy, ensuring consistent error handling and logging.

    Args:
        exc: The original third-party exception
        context: Error context information
        logger_name: Specific logger name to use (defaults to current module)
        **kwargs: Additional structured logging data

    Returns:
        MythosMUDError instance
    """
    # Use specified logger or default to current module logger
    error_logger = get_logger(logger_name) if logger_name else logger

    # Get the full class name for mapping lookup
    exc_class_name = f"{exc.__class__.__module__}.{exc.__class__.__name__}"

    # Find the appropriate MythosMUD error class
    mythos_error_class = THIRD_PARTY_EXCEPTION_MAPPING.get(exc_class_name)

    if mythos_error_class is None:
        # Try to find by just the class name if full name not found
        mythos_error_class = THIRD_PARTY_EXCEPTION_MAPPING.get(exc.__class__.__name__)

    if mythos_error_class is None:
        # Default to generic MythosMUD error for unmapped exceptions
        mythos_error_class = MythosMUDError
        log_with_context(
            error_logger,
            "warning",
            "Unmapped third-party exception",
            original_type=exc_class_name,
            original_message=str(exc),
            **kwargs,
        )

    # Create context if not provided
    if context is None:
        context = create_error_context()

    # Add original exception details
    details = {
        "original_type": exc_class_name,
        "original_message": str(exc),
        "traceback": traceback.format_exc(),
        **kwargs,
    }

    # Log the conversion with structured data
    log_with_context(
        error_logger,
        "info",
        "Third-party exception wrapped",
        original_type=exc_class_name,
        mythos_type=mythos_error_class.__name__,
        context=context.to_dict() if context else {},
        **kwargs,
    )

    # Create and return the MythosMUD error
    return mythos_error_class(
        message=f"Third-party exception: {str(exc)}",
        context=context,
        details=details,
        user_friendly="An internal error occurred. Please try again.",
    )


def create_enhanced_error_context(
    request: Request | None = None,
    websocket: WebSocket | None = None,
    user_id: str | None = None,
    session_id: str | None = None,
    **kwargs,
) -> ErrorContext:
    """
    Create enhanced error context with structured information.

    This function creates a comprehensive error context with request information,
    user context, and additional metadata for better error tracking.

    Args:
        request: FastAPI request object (can be None for testing)
        websocket: WebSocket connection (can be None)
        user_id: User ID if available
        session_id: Session ID if available
        **kwargs: Additional context metadata

    Returns:
        Enhanced ErrorContext with comprehensive information
    """
    # Handle request context
    if request:
        metadata = {
            "path": str(request.url),
            "method": request.method,
            "user_agent": request.headers.get("user-agent", ""),
            "content_type": request.headers.get("content-type", ""),
            "content_length": request.headers.get("content-length", ""),
            "remote_addr": getattr(request.client, "host", "") if request.client else "",
            "query_params": dict(request.query_params),
            **kwargs,
        }
        request_id = str(request.url)
    elif websocket:
        metadata = {
            "path": str(websocket.url),
            "connection_type": "websocket",
            "user_agent": websocket.headers.get("user-agent", ""),
            "remote_addr": getattr(websocket.client, "host", "") if websocket.client else "",
            "query_params": dict(websocket.query_params),
            **kwargs,
        }
        request_id = str(websocket.url)
    else:
        metadata = {
            "path": "unknown",
            "method": "unknown",
            "user_agent": "",
            "content_type": "",
            "content_length": "",
            "remote_addr": "",
            **kwargs,
        }
        request_id = "unknown"

    return create_error_context(
        user_id=user_id,
        session_id=session_id,
        request_id=request_id,
        metadata=metadata,
    )


def log_performance_metric(
    operation: str,
    duration_ms: float,
    success: bool = True,
    context: ErrorContext | None = None,
    logger_name: str | None = None,
    **kwargs,
) -> None:
    """
    Log performance metrics with structured data.

    This function logs performance metrics for monitoring and optimization.

    Args:
        operation: Name of the operation being measured
        duration_ms: Duration in milliseconds
        success: Whether the operation was successful
        context: Error context information
        logger_name: Specific logger name to use (defaults to current module)
        **kwargs: Additional structured logging data
    """
    # Use specified logger or default to current module logger
    metric_logger = get_logger(logger_name) if logger_name else logger

    # Prepare structured log data
    log_data = {
        "metric_type": "performance",
        "operation": operation,
        "duration_ms": duration_ms,
        "success": success,
        "context": context.to_dict() if context else {},
        **kwargs,
    }

    # Log the performance metric
    log_with_context(metric_logger, "info", f"Performance metric: {operation}", **log_data)


def log_security_event_enhanced(
    event_type: str,
    severity: str = "medium",
    user_id: str | None = None,
    context: ErrorContext | None = None,
    logger_name: str | None = None,
    **kwargs,
) -> None:
    """
    Log security events with structured data.

    This function logs security events for monitoring and incident response.

    Args:
        event_type: Type of security event
        severity: Severity level (low, medium, high, critical)
        user_id: User ID if available
        context: Error context information
        logger_name: Specific logger name to use (defaults to current module)
        **kwargs: Additional structured logging data
    """
    # Use specified logger or default to current module logger
    security_logger = get_logger(logger_name) if logger_name else logger

    # Prepare structured log data
    log_data = {
        "event_type": "security_event",
        "security_event_type": event_type,
        "severity": severity,
        "user_id": user_id,
        "context": context.to_dict() if context else {},
        **kwargs,
    }

    # Log at appropriate level based on severity
    level = "critical" if severity == "critical" else "warning"

    log_with_context(security_logger, level, f"Security event: {event_type}", **log_data)
