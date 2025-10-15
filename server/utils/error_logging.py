"""
Enhanced error logging utilities for MythosMUD server.

This module provides standardized error logging functions that ensure consistent
error handling and logging across the entire codebase. As the Pnakotic Manuscripts
teach us, proper categorization and documentation of anomalies is essential for
understanding the deeper mysteries of our digital realm.
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
from ..logging_config import get_logger

logger = get_logger(__name__)

# Third-party exception mapping for proper error categorization
# As noted in the restricted archives, this mapping ensures that external
# library exceptions are properly converted to our internal error taxonomy
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


def log_and_raise(
    exception_class: type[MythosMUDError],
    message: str,
    context: ErrorContext | None = None,
    details: dict[str, Any] | None = None,
    user_friendly: str | None = None,
    logger_name: str | None = None,
) -> None:
    """
    Log an error and raise a MythosMUD exception.

    This function provides a standardized way to log errors with proper context
    before raising exceptions, ensuring consistent error handling across the codebase.

    Args:
        exception_class: The MythosMUD exception class to raise
        message: Technical error message
        context: Error context information
        details: Additional error details
        user_friendly: User-friendly error message
        logger_name: Specific logger name to use (defaults to current module)

    Raises:
        The specified MythosMUD exception
    """
    # Use specified logger or default to current module logger
    error_logger = get_logger(logger_name) if logger_name else logger

    # Create context if not provided
    if context is None:
        context = create_error_context()

    # Log the error with full context
    error_logger.error(
        f"Error logged and exception raised: {message}",
        error_type=exception_class.__name__,
        details=details or {},
        user_friendly=user_friendly,
    )

    # Raise the exception
    raise exception_class(
        message=message,
        context=context,
        details=details,
        user_friendly=user_friendly,
    )


def log_and_raise_http(
    status_code: int,
    detail: str,
    context: ErrorContext | None = None,
    logger_name: str | None = None,
) -> None:
    """
    Log an HTTP error and raise an HTTPException.

    This function provides a standardized way to log HTTP errors with proper
    context before raising HTTPExceptions, ensuring consistent error handling
    for API endpoints.

    Args:
        status_code: HTTP status code
        detail: Error detail message
        context: Error context information
        logger_name: Specific logger name to use (defaults to current module)

    Raises:
        HTTPException with the specified status code and detail
    """
    # Use specified logger or default to current module logger
    error_logger = get_logger(logger_name) if logger_name else logger

    # Create context if not provided
    if context is None:
        context = create_error_context()

    # Log the HTTP error with full context
    log_data = {
        "error_type": "HTTPException",
        "status_code": status_code,
        "detail": detail,
        "context": context.to_dict(),
    }

    error_logger.warning("HTTP error logged and exception raised", **log_data)

    # Raise the HTTPException
    raise HTTPException(status_code=status_code, detail=detail)


def create_context_from_request(request: Request | None) -> ErrorContext:
    """
    Create error context from a FastAPI request.

    Extracts relevant information from the request to create a comprehensive
    error context for logging and debugging.

    Args:
        request: FastAPI request object (can be None for testing)

    Returns:
        ErrorContext with request information
    """
    # Handle None request (for testing scenarios)
    if request is None:
        metadata = {
            "path": "unknown",
            "method": "unknown",
            "user_agent": "",
            "content_type": "",
            "content_length": "",
            "remote_addr": "",
        }
    else:
        # Extract request metadata
        metadata = {
            "path": str(request.url),
            "method": request.method,
            "user_agent": request.headers.get("user-agent", ""),
            "content_type": request.headers.get("content-type", ""),
            "content_length": request.headers.get("content-length", ""),
            "remote_addr": getattr(request.client, "host", "") if request.client else "",
        }

    # Extract user information if available
    user_id = None
    session_id = None

    # Try to get user info from request state (if authentication middleware has set it)
    if request and hasattr(request, "state"):
        if hasattr(request.state, "user_id"):
            user_id = request.state.user_id
        if hasattr(request.state, "session_id"):
            session_id = request.state.session_id

    return create_error_context(
        user_id=user_id,
        session_id=session_id,
        request_id=str(request.url) if request else "unknown",
        metadata=metadata,
    )


def create_context_from_websocket(websocket: WebSocket) -> ErrorContext:
    """
    Create error context from a WebSocket connection.

    Extracts relevant information from the WebSocket to create a comprehensive
    error context for logging and debugging.

    Args:
        websocket: FastAPI WebSocket object

    Returns:
        ErrorContext with WebSocket information
    """
    # Extract WebSocket metadata
    metadata = {
        "path": str(websocket.url),
        "connection_type": "websocket",
        "user_agent": websocket.headers.get("user-agent", ""),
        "remote_addr": getattr(websocket.client, "host", "") if websocket.client else "",
    }

    # Extract user information if available
    user_id = None
    session_id = None

    # Try to get user info from WebSocket state (if authentication middleware has set it)
    if hasattr(websocket, "state") and hasattr(websocket.state, "user_id"):
        user_id = websocket.state.user_id
    if hasattr(websocket, "state") and hasattr(websocket.state, "session_id"):
        session_id = websocket.state.session_id

    return create_error_context(
        user_id=user_id,
        session_id=session_id,
        request_id=str(websocket.url),
        metadata=metadata,
    )


def wrap_third_party_exception(
    exc: Exception,
    context: ErrorContext | None = None,
    logger_name: str | None = None,
) -> MythosMUDError:
    """
    Wrap a third-party exception in a MythosMUD error.

    This function converts external library exceptions to our internal error
    taxonomy, ensuring consistent error handling and logging.

    Args:
        exc: The original third-party exception
        context: Error context information
        logger_name: Specific logger name to use (defaults to current module)

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
        error_logger.warning(
            "Unmapped third-party exception",
            original_type=exc_class_name,
            original_message=str(exc),
        )

    # Create context if not provided
    if context is None:
        context = create_error_context()

    # Add original exception details
    details = {
        "original_type": exc_class_name,
        "original_message": str(exc),
        "traceback": traceback.format_exc(),
    }

    # Log the conversion
    error_logger.info(
        "Third-party exception wrapped",
        original_type=exc_class_name,
        mythos_type=mythos_error_class.__name__,
        context=context.to_dict(),
    )

    # Create and return the MythosMUD error
    return mythos_error_class(
        message=f"Third-party exception: {str(exc)}",
        context=context,
        details=details,
        user_friendly="An internal error occurred. Please try again.",
    )


def log_error_with_context(
    error: Exception,
    context: ErrorContext | None = None,
    logger_name: str | None = None,
    level: str = "error",
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
    """
    # Use specified logger or default to current module logger
    error_logger = get_logger(logger_name) if logger_name else logger

    # Create context if not provided
    if context is None:
        context = create_error_context()

    # Prepare log data
    log_data = {
        "error_type": error.__class__.__name__,
        "error_message": str(error),
        "context": context.to_dict(),
        "traceback": traceback.format_exc(),
    }

    # Log at the specified level
    log_method = getattr(error_logger, level.lower(), error_logger.error)
    log_method("Error logged with context", **log_data)


def create_logged_http_exception(
    status_code: int,
    detail: str,
    context: ErrorContext | None = None,
    logger_name: str | None = None,
) -> HTTPException:
    """
    Create an HTTPException with proper logging.

    This function creates an HTTPException and logs it with proper context
    before returning it, allowing the caller to raise it when appropriate.

    Args:
        status_code: HTTP status code
        detail: Error detail message
        context: Error context information
        logger_name: Specific logger name to use (defaults to current module)

    Returns:
        HTTPException with the specified status code and detail
    """
    # Use specified logger or default to current module logger
    error_logger = get_logger(logger_name) if logger_name else logger

    # Create context if not provided
    if context is None:
        context = create_error_context()

    # Log the HTTP error with full context
    log_data = {
        "error_type": "HTTPException",
        "status_code": status_code,
        "detail": detail,
        "context": context.to_dict(),
    }

    error_logger.warning("HTTP error created and logged", **log_data)

    # Create and return the HTTPException
    return HTTPException(status_code=status_code, detail=detail)
