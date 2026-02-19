"""
Enhanced error logging utilities with structured logging and context management.

This module provides enhanced error logging functions that use proper structured
logging instead of the incorrect context parameter pattern. It integrates with
the enhanced logging system to provide better error tracking and debugging.

As the Pnakotic Manuscripts teach us, proper documentation of anomalies is
essential for understanding the deeper mysteries of our digital realm.
"""

# pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Error logging requires many parameters for complete error context

import traceback
from typing import Any, NoReturn, cast

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
from ..structured_logging.enhanced_logging_config import get_logger, log_with_context

logger = get_logger(__name__)

# Third-party exception mapping for proper error categorization
THIRD_PARTY_EXCEPTION_MAPPING = {
    # Database exceptions - PostgreSQL/asyncpg
    "asyncpg.exceptions.PostgresError": DatabaseError,
    "asyncpg.exceptions.OperationalError": DatabaseError,
    "asyncpg.exceptions.IntegrityConstraintViolationError": DatabaseError,
    "asyncpg.exceptions.DatabaseError": DatabaseError,
    "asyncpg.exceptions.InvalidPasswordError": DatabaseError,
    "asyncpg.exceptions.ConnectionDoesNotExistError": DatabaseError,
    "asyncpg.exceptions.TooManyConnectionsError": DatabaseError,
    # Database exceptions - SQLAlchemy (wraps asyncpg)
    "sqlalchemy.exc.OperationalError": DatabaseError,
    "sqlalchemy.exc.IntegrityError": DatabaseError,
    "sqlalchemy.exc.DatabaseError": DatabaseError,
    "sqlalchemy.exc.ProgrammingError": DatabaseError,
    "sqlalchemy.exc.DataError": DatabaseError,
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


def log_and_raise_enhanced(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Error logging requires many parameters for complete error context
    exception_class: type[MythosMUDError],
    message: str,
    details: dict[str, Any] | None = None,
    user_friendly: str | None = None,
    logger_name: str | None = None,
    skip_log_validation: bool = True,
    log_as_error: bool = False,
    **kwargs: Any,
) -> NoReturn:
    """
    Enhanced log and raise function with proper structured logging.

    This function provides a standardized way to log errors with proper context
    before raising exceptions, using structured logging instead of the incorrect
    context parameter pattern.

    Args:
        exception_class: The MythosMUD exception class to raise
        message: Technical error message
        details: Additional error details
        user_friendly: User-friendly error message
        logger_name: Specific logger name to use (defaults to current module)
        log_as_error: If True, log at error level even for ValidationError (so entry goes to errors.log)
        **kwargs: Additional structured logging data (e.g., operation, user_id, etc.)

    Raises:
        The specified MythosMUD exception
    """
    # Use specified logger or default to current module logger
    error_logger = get_logger(logger_name) if logger_name else logger

    # Create ErrorContext internally from kwargs for exception object
    # Extract common context fields from kwargs
    context_metadata = {
        k: v for k, v in kwargs.items() if k not in ["error_type", "error_message", "details", "user_friendly"]
    }
    context = create_error_context(
        user_id=kwargs.get("user_id"),
        session_id=kwargs.get("session_id"),
        request_id=kwargs.get("request_id"),
        metadata=context_metadata,
    )

    # Prepare structured log data
    log_data = {
        "error_type": exception_class.__name__,
        "error_message": message,
        "user_friendly": user_friendly,
        "details": details or {},
        **kwargs,
    }

    # ValidationError is normally expected user input (e.g. empty local); log as warning.
    # Use error level when log_as_error=True so command-usage failures go to errors.log.
    log_level = "error" if (log_as_error or exception_class is not ValidationError) else "warning"
    log_with_context(error_logger, log_level, "Error logged and exception raised", **log_data)

    # Increment exception counter for monitoring
    from ..monitoring.exception_metrics import increment_exception

    try:
        increment_exception(exception_class.__name__)
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Monitoring errors must never break error propagation
        # nosec B110 - Intentional silent handling: Monitoring errors must never break error propagation
        logger.debug("Failed to increment exception counter, continuing with error propagation", exc_info=e)

    # Raise the exception (skip_log=True for ValidationError when skip_log_validation: we already logged above).
    raise exception_class(
        message=message,
        context=context,
        details=details,
        user_friendly=user_friendly,
        skip_log=skip_log_validation and exception_class is ValidationError,
    )


def _log_http_error(
    status_code: int,
    detail: str,
    logger_name: str | None = None,
    raise_it: bool = True,
    **kwargs: Any,
) -> HTTPException:
    """Log HTTP error and optionally raise or return HTTPException. Shared by raise vs return variants."""
    error_logger = get_logger(logger_name) if logger_name else logger
    log_data = {
        "error_type": "HTTPException",
        "status_code": status_code,
        "detail": detail,
        **kwargs,
    }
    log_with_context(error_logger, "warning", "HTTP error logged and exception raised", **log_data)
    ex = HTTPException(status_code=status_code, detail=detail)
    if raise_it:
        raise ex
    return ex


def log_and_raise_http_enhanced(status_code: int, detail: str, logger_name: str | None = None, **kwargs: Any) -> None:
    """
    Enhanced HTTP error logging with structured logging.

    This function provides a standardized way to log HTTP errors with proper
    context before raising HTTPExceptions, using structured logging.

    Args:
        status_code: HTTP status code
        detail: Error detail message
        logger_name: Specific logger name to use (defaults to current module)
        **kwargs: Additional structured logging data (e.g., path, method, user_id, etc.)

    Raises:
        HTTPException with the specified status code and detail
    """
    _log_http_error(status_code, detail, logger_name=logger_name, raise_it=True, **kwargs)


def create_logged_http_exception_enhanced(
    status_code: int,
    detail: str,
    logger_name: str | None = None,
    **kwargs: Any,
) -> HTTPException:
    """Create an HTTPException with proper logging and return it (caller raises when appropriate)."""
    return _log_http_error(status_code, detail, logger_name=logger_name, raise_it=False, **kwargs)


def log_structured_error(
    error: Exception,
    logger_name: str | None = None,
    level: str = "error",
    **kwargs: Any,
) -> None:
    """
    Log an error with structured context information.

    This function provides a standardized way to log errors with comprehensive
    context information for debugging and monitoring.

    Args:
        error: The exception to log
        logger_name: Specific logger name to use (defaults to current module)
        level: Log level (debug, info, warning, error, critical)
        **kwargs: Additional structured logging data (e.g., operation, user_id, etc.)
    """
    # Use specified logger or default to current module logger
    error_logger = get_logger(logger_name) if logger_name else logger

    # Prepare structured log data
    log_data = {
        "error_type": error.__class__.__name__,
        "error_message": str(error),
        "traceback": traceback.format_exc(),
        **kwargs,
    }

    # Log with structured data
    log_with_context(error_logger, level, "Error logged with context", **log_data)

    # Increment exception counter for monitoring
    from ..monitoring.exception_metrics import increment_exception

    try:
        increment_exception(error.__class__.__name__)
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Monitoring errors must never break error propagation
        # nosec B110 - Intentional silent handling: Monitoring errors must never break error propagation
        logger.debug("Failed to increment exception counter, continuing with error propagation", exc_info=e)


def wrap_third_party_exception_enhanced(
    exc: Exception, logger_name: str | None = None, **kwargs: Any
) -> MythosMUDError:
    """
    Enhanced wrapper for third-party exceptions with structured logging.

    This function converts external library exceptions to our internal error
    taxonomy, ensuring consistent error handling and logging.

    Args:
        exc: The original third-party exception
        logger_name: Specific logger name to use (defaults to current module)
        **kwargs: Additional structured logging data (e.g., operation, user_id, etc.)

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

    # Create ErrorContext internally from kwargs for exception object
    context_metadata = {
        k: v for k, v in kwargs.items() if k not in ["original_type", "original_message", "mythos_type"]
    }
    context = create_error_context(
        user_id=kwargs.get("user_id"),
        session_id=kwargs.get("session_id"),
        request_id=kwargs.get("request_id"),
        metadata=context_metadata,
    )

    # Add original exception details
    details = {
        "original_type": exc_class_name,
        "original_message": str(exc),
        "traceback": traceback.format_exc(),
        **{k: v for k, v in kwargs.items() if k not in ["user_id", "session_id", "request_id"]},
    }

    # Log the conversion with structured data
    log_with_context(
        error_logger,
        "info",
        "Third-party exception wrapped",
        original_type=exc_class_name,
        mythos_type=mythos_error_class.__name__,
        **kwargs,
    )

    # Create and return the MythosMUD error
    result: MythosMUDError = cast(
        MythosMUDError,
        mythos_error_class(
            message=f"Third-party exception: {str(exc)}",
            context=context,
            details=details,
            user_friendly="An internal error occurred. Please try again.",
        ),
    )
    return result


def create_enhanced_error_context(
    request: Request | None = None,
    websocket: WebSocket | None = None,
    user_id: str | None = None,
    session_id: str | None = None,
    **kwargs: Any,
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
    logger_name: str | None = None,
    **kwargs: Any,
) -> None:
    """
    Log performance metrics with structured data.

    This function logs performance metrics for monitoring and optimization.

    Args:
        operation: Name of the operation being measured
        duration_ms: Duration in milliseconds
        success: Whether the operation was successful
        logger_name: Specific logger name to use (defaults to current module)
        **kwargs: Additional structured logging data (e.g., user_id, request_id, etc.)
    """
    # Use specified logger or default to current module logger
    metric_logger = get_logger(logger_name) if logger_name else logger

    # Prepare structured log data
    log_data = {
        "metric_type": "performance",
        "operation": operation,
        "duration_ms": duration_ms,
        "success": success,
        **kwargs,
    }

    # Log the performance metric
    log_with_context(metric_logger, "info", "Performance metric logged", **log_data)


def log_security_event_enhanced(
    event_type: str,
    severity: str = "medium",
    user_id: str | None = None,
    logger_name: str | None = None,
    **kwargs: Any,
) -> None:
    """
    Log security events with structured data.

    This function logs security events for monitoring and incident response.

    Args:
        event_type: Type of security event
        severity: Severity level (low, medium, high, critical)
        user_id: User ID if available
        logger_name: Specific logger name to use (defaults to current module)
        **kwargs: Additional structured logging data (e.g., operation, request_id, etc.)
    """
    # Use specified logger or default to current module logger
    security_logger = get_logger(logger_name) if logger_name else logger

    # Prepare structured log data
    log_data = {
        "event_type": "security_event",
        "security_event_type": event_type,
        "severity": severity,
        "user_id": user_id,
        **kwargs,
    }

    # Log at appropriate level based on severity
    level = "critical" if severity == "critical" else "warning"

    log_with_context(security_logger, level, "Security event logged", **log_data)


__all__ = [
    "create_error_context",
    "create_enhanced_error_context",
    "create_logged_http_exception_enhanced",
    "log_and_raise_enhanced",
    "log_and_raise_http_enhanced",
    "THIRD_PARTY_EXCEPTION_MAPPING",
]
