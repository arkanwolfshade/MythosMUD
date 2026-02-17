"""
Enhanced error logging utilities for MythosMUD server.

This module provides standardized error logging functions that ensure consistent
error handling and logging across the entire codebase. As the Pnakotic Manuscripts
teach us, proper categorization and documentation of anomalies is essential for
understanding the deeper mysteries of our digital realm.

Implementation is consolidated in enhanced_error_logging; this module re-exports
and provides thin wrappers (e.g. log_and_raise with legacy skip_log behavior) so
existing callers remain unchanged. See enhanced_error_logging for the canonical
implementation and THIRD_PARTY_EXCEPTION_MAPPING.
"""

from typing import Any, NoReturn

from fastapi import HTTPException, Request
from fastapi.websockets import WebSocket

from ..exceptions import ErrorContext, MythosMUDError, create_error_context
from .enhanced_error_logging import (
    THIRD_PARTY_EXCEPTION_MAPPING,
    create_enhanced_error_context,
    create_logged_http_exception_enhanced,
    log_and_raise_enhanced,
    log_and_raise_http_enhanced,
    log_structured_error,
    wrap_third_party_exception_enhanced,
)


def log_and_raise(
    exception_class: type[MythosMUDError],
    message: str,
    details: dict[str, Any] | None = None,
    user_friendly: str | None = None,
    logger_name: str | None = None,
    **kwargs: Any,
) -> NoReturn:
    """Log and raise; uses legacy behavior (no skip_log for ValidationError). Delegates to enhanced."""
    log_and_raise_enhanced(
        exception_class,
        message,
        details=details,
        user_friendly=user_friendly,
        logger_name=logger_name,
        skip_log_validation=False,
        **kwargs,
    )


def log_and_raise_http(
    status_code: int,
    detail: str,
    logger_name: str | None = None,
    **kwargs: Any,
) -> None:
    """Log HTTP error and raise HTTPException. Delegates to enhanced."""
    log_and_raise_http_enhanced(status_code, detail, logger_name=logger_name, **kwargs)


def create_context_from_request(request: Request | None) -> ErrorContext:
    """Create error context from a FastAPI request. Delegates to create_enhanced_error_context."""
    user_id = None
    session_id = None
    if request is not None and hasattr(request, "state"):
        if hasattr(request.state, "user_id"):
            user_id = getattr(request.state, "user_id", None)
        if hasattr(request.state, "session_id"):
            session_id = getattr(request.state, "session_id", None)
    return create_enhanced_error_context(request=request, user_id=user_id, session_id=session_id)


def create_context_from_websocket(websocket: WebSocket) -> ErrorContext:
    """Create error context from a WebSocket. Delegates to create_enhanced_error_context."""
    user_id = None
    session_id = None
    if hasattr(websocket, "state"):
        if hasattr(websocket.state, "user_id"):
            user_id = getattr(websocket.state, "user_id", None)
        if hasattr(websocket.state, "session_id"):
            session_id = getattr(websocket.state, "session_id", None)
    return create_enhanced_error_context(websocket=websocket, user_id=user_id, session_id=session_id)


def wrap_third_party_exception(
    exc: Exception,
    logger_name: str | None = None,
    **kwargs: Any,
) -> MythosMUDError:
    """Wrap a third-party exception in a MythosMUD error. Delegates to enhanced."""
    return wrap_third_party_exception_enhanced(exc, logger_name=logger_name, **kwargs)


def log_error_with_context(
    error: Exception,
    logger_name: str | None = None,
    level: str = "error",
    **kwargs: Any,
) -> None:
    """Log an error with structured context. Delegates to log_structured_error."""
    log_structured_error(error, logger_name=logger_name, level=level, **kwargs)


def create_logged_http_exception(
    status_code: int,
    detail: str,
    logger_name: str | None = None,
    **kwargs: Any,
) -> HTTPException:
    """Create an HTTPException with proper logging and return it. Delegates to enhanced."""
    return create_logged_http_exception_enhanced(status_code, detail, logger_name=logger_name, **kwargs)


__all__ = [
    "create_error_context",
    "create_context_from_request",
    "create_context_from_websocket",
    "create_logged_http_exception",
    "log_and_raise",
    "log_and_raise_http",
    "log_error_with_context",
    "wrap_third_party_exception",
    "THIRD_PARTY_EXCEPTION_MAPPING",
]
