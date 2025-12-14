"""
Context management utilities for enhanced logging.

This module provides functions for managing logging context, including
request context binding, clearing, and context-aware logging.
"""

import uuid
from typing import Any

import structlog
from structlog.contextvars import bind_contextvars, clear_contextvars
from structlog.stdlib import BoundLogger


def bind_request_context(
    correlation_id: str | None = None,
    user_id: str | None = None,
    session_id: str | None = None,
    request_id: str | None = None,
    **kwargs,
) -> None:
    """
    Bind request context to the current logging context.

    This function sets up the logging context for a request, ensuring all
    subsequent log entries include the request context.

    Args:
        correlation_id: Unique correlation ID for the request
        user_id: User ID if available
        session_id: Session ID if available
        request_id: Request ID if available
        **kwargs: Additional context variables
    """
    if correlation_id is None:
        correlation_id = str(uuid.uuid4())

    context_vars = {
        "correlation_id": correlation_id,
        "user_id": user_id,
        "session_id": session_id,
        "request_id": request_id,
        **kwargs,
    }

    # Remove None values
    context_vars = {k: v for k, v in context_vars.items() if v is not None}

    bind_contextvars(**context_vars)


def clear_request_context() -> None:
    """Clear the current request context from logging."""
    clear_contextvars()


def get_current_context() -> dict[str, Any]:
    """Get the current logging context."""
    try:
        # Use get_contextvars() to get the current context-local context
        return structlog.contextvars.get_contextvars()
    except (AttributeError, KeyError):
        # If there's no bound context, return empty dict
        return {}


def log_with_context(bound_logger: BoundLogger, level: str, message: str, **kwargs) -> None:
    """
    Log a message with the current context automatically included.

    Args:
        bound_logger: Structlog logger instance
        level: Log level (debug, info, warning, error, critical)
        message: Log message
        **kwargs: Additional log data
    """
    # Get current context and merge with additional kwargs
    current_context = get_current_context()
    log_data = {**current_context, **kwargs}

    # Log at the specified level
    log_method = getattr(bound_logger, level.lower(), bound_logger.info)
    log_method(message, **log_data)
