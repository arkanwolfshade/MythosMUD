"""
Middleware package for MythosMUD server.

This package contains middleware components for FastAPI integration,
including error handling, logging, and request tracking.
"""

from .error_handling_middleware import (
    ErrorHandlingMiddleware,
    add_error_handling_middleware,
    register_error_handlers,
    setup_error_handling,
)

__all__ = [
    "ErrorHandlingMiddleware",
    "add_error_handling_middleware",
    "register_error_handlers",
    "setup_error_handling",
]
