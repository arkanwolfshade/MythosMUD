"""
Shared helper functions for player API endpoints.
"""

from typing import Any

from fastapi import Request

from ..exceptions import ErrorContext
from ..models.user import User
from ..utils.error_logging import create_context_from_request


def create_error_context(request: Request, current_user: User | None, **metadata: Any) -> ErrorContext:
    """
    Create error context from request and user.

    Helper function to reduce duplication in exception handling.

    Args:
        request: FastAPI Request object
        current_user: Current user or None
        **metadata: Additional metadata to add to context

    Returns:
        ErrorContext: Error context with request and user information
    """
    context = create_context_from_request(request)
    if current_user:
        context.user_id = str(current_user.id)
    context.metadata.update(metadata)
    return context
