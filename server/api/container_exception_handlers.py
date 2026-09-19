"""
Exception handlers for container API endpoints.

This module contains functions to handle exceptions raised during container operations,
converting them to appropriate HTTP exceptions with proper error context.
"""

from typing import Any
from uuid import UUID

from fastapi import Request, status

from ..exceptions import LoggedHTTPException
from ..models.user import User
from ..services.container_service import ContainerCapacityError, ContainerServiceError
from ..structured_logging.enhanced_logging_config import get_logger
from .container_helpers import create_error_context

logger = get_logger(__name__)


def _raise_container_http(status_code: int, detail: str, context_kwargs: dict[str, Any], exc: Exception) -> None:
    raise LoggedHTTPException(status_code=status_code, detail=detail, **context_kwargs) from exc


def _raise_unexpected_container_error(
    exc: Exception,
    # Reason: SERIALIZATION_BOUNDARY - matches _raise_container_http's own established,
    # unsuppressed dict[str, Any] parameter above.
    # Appropriate because: context_kwargs is a **kwargs bag forwarded to LoggedHTTPException/logger.
    context_kwargs: dict[str, Any],  # pyright: ignore[reportExplicitAny]
) -> None:
    # context_kwargs already carries "operation" from create_error_context.
    logger.error("Unexpected error in operation", error=str(exc), exc_info=True, **context_kwargs)
    _raise_container_http(status.HTTP_500_INTERNAL_SERVER_ERROR, "Internal server error", context_kwargs, exc)


def handle_open_container_exceptions(
    e: Exception,
    request: Request,
    current_user: User,
    container_id: UUID,
) -> None:
    """
    Handle exceptions for open_container endpoint.

    Args:
        e: The exception that occurred
        request: FastAPI Request object
        current_user: Current authenticated user
        container_id: Container UUID

    Raises:
        LoggedHTTPException: With appropriate status code based on exception type
    """
    from ..services.container_service import (
        ContainerAccessDeniedError,
        ContainerLockedError,
        ContainerNotFoundError,
    )

    context_kwargs = create_error_context(
        request, current_user, container_id=str(container_id), operation="open_container"
    )

    if isinstance(e, ContainerNotFoundError):
        _raise_container_http(status.HTTP_404_NOT_FOUND, "Container not found", context_kwargs, e)

    if isinstance(e, ContainerLockedError):
        _raise_container_http(status.HTTP_423_LOCKED, "Container is locked", context_kwargs, e)

    if isinstance(e, ContainerAccessDeniedError):
        _raise_container_http(status.HTTP_403_FORBIDDEN, "Access denied", context_kwargs, e)

    if isinstance(e, ContainerServiceError):
        error_str = str(e).lower()
        if "already" in error_str or "open" in error_str:
            _raise_container_http(status.HTTP_409_CONFLICT, "Container is already open", context_kwargs, e)
        _raise_container_http(status.HTTP_500_INTERNAL_SERVER_ERROR, "Failed to open container", context_kwargs, e)

    _raise_unexpected_container_error(e, context_kwargs)


def _raise_for_transfer_service_error(
    error_str: str,
    # Reason: SERIALIZATION_BOUNDARY - matches _raise_container_http/_raise_unexpected_container_error
    # above; context_kwargs is a **kwargs bag forwarded to LoggedHTTPException.
    # Appropriate because: same unsuppressed dict[str, Any] convention used by the two sibling
    # helpers already in this module; a TypedDict is out of scope for this complexity extraction.
    context_kwargs: dict[str, Any],  # pyright: ignore[reportExplicitAny]
    exc: Exception,
) -> None:
    """Classify a ContainerServiceError message for the transfer_items endpoint."""
    if "stale" in error_str or "token" in error_str or "mutation" in error_str:
        _raise_container_http(
            status.HTTP_412_PRECONDITION_FAILED,
            "Stale mutation token. Please reopen the container.",
            context_kwargs,
            exc,
        )
    if "invalid" in error_str or "stack" in error_str:
        _raise_container_http(status.HTTP_400_BAD_REQUEST, "Invalid item stack", context_kwargs, exc)
    _raise_container_http(status.HTTP_500_INTERNAL_SERVER_ERROR, "Failed to transfer items", context_kwargs, exc)


def handle_transfer_items_exceptions(
    e: Exception,
    request: Request,
    current_user: User,
    container_id: UUID,
) -> None:
    """
    Handle exceptions for transfer_items endpoint.

    Args:
        e: The exception that occurred
        request: FastAPI Request object
        current_user: Current authenticated user
        container_id: Container UUID

    Raises:
        LoggedHTTPException: With appropriate status code based on exception type
    """
    from ..exceptions import ValidationError
    from ..services.container_service import (
        ContainerAccessDeniedError,
        ContainerNotFoundError,
    )

    context_kwargs = create_error_context(
        request, current_user, container_id=str(container_id), operation="transfer_items"
    )

    if isinstance(e, ContainerNotFoundError):
        _raise_container_http(status.HTTP_404_NOT_FOUND, "Container not found", context_kwargs, e)

    if isinstance(e, ContainerCapacityError):
        _raise_container_http(status.HTTP_409_CONFLICT, "Capacity exceeded", context_kwargs, e)

    if isinstance(e, ContainerAccessDeniedError):
        _raise_container_http(status.HTTP_403_FORBIDDEN, "Access denied", context_kwargs, e)

    if isinstance(e, ContainerServiceError):
        _raise_for_transfer_service_error(str(e).lower(), context_kwargs, e)

    if isinstance(e, ValidationError):
        _raise_container_http(status.HTTP_400_BAD_REQUEST, f"Validation error: {str(e)}", context_kwargs, e)

    _raise_unexpected_container_error(e, context_kwargs)


def handle_close_container_exceptions(
    e: Exception,
    request: Request,
    current_user: User,
    container_id: UUID,
) -> None:
    """
    Handle exceptions for close_container endpoint.

    Args:
        e: The exception that occurred
        request: FastAPI Request object
        current_user: Current authenticated user
        container_id: Container UUID

    Raises:
        LoggedHTTPException: With appropriate status code based on exception type
    """
    from ..services.container_service import ContainerNotFoundError

    context_kwargs = create_error_context(
        request, current_user, container_id=str(container_id), operation="close_container"
    )

    if isinstance(e, ContainerNotFoundError):
        _raise_container_http(status.HTTP_404_NOT_FOUND, "Container not found", context_kwargs, e)

    if isinstance(e, ContainerServiceError):
        error_str = str(e).lower()
        if "token" in error_str or "invalid" in error_str:
            _raise_container_http(status.HTTP_400_BAD_REQUEST, "Invalid mutation token", context_kwargs, e)
        _raise_container_http(status.HTTP_500_INTERNAL_SERVER_ERROR, "Failed to close container", context_kwargs, e)

    _raise_unexpected_container_error(e, context_kwargs)


def handle_loot_all_exceptions(
    e: Exception,
    request: Request,
    current_user: User,
    container_id: UUID,
) -> None:
    """
    Handle exceptions for loot_all_items endpoint.

    Args:
        e: The exception that occurred
        request: FastAPI Request object
        current_user: Current authenticated user
        container_id: Container UUID

    Raises:
        LoggedHTTPException: With appropriate status code based on exception type
    """
    from ..services.container_service import (
        ContainerAccessDeniedError,
        ContainerLockedError,
        ContainerNotFoundError,
    )

    context_kwargs = create_error_context(request, current_user, container_id=str(container_id), operation="loot_all")

    if isinstance(e, ContainerNotFoundError):
        _raise_container_http(status.HTTP_404_NOT_FOUND, "Container not found", context_kwargs, e)

    if isinstance(e, ContainerLockedError):
        _raise_container_http(status.HTTP_423_LOCKED, "Container is locked", context_kwargs, e)

    if isinstance(e, ContainerAccessDeniedError):
        _raise_container_http(status.HTTP_403_FORBIDDEN, "Access denied", context_kwargs, e)

    if isinstance(e, ContainerCapacityError):
        _raise_container_http(status.HTTP_409_CONFLICT, "Player inventory capacity exceeded", context_kwargs, e)

    if isinstance(e, ContainerServiceError):
        _raise_container_http(
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            "Failed to loot items from container",
            context_kwargs,
            e,
        )

    logger.error("Unexpected error in loot-all", error=str(e), **context_kwargs)
    _raise_container_http(status.HTTP_500_INTERNAL_SERVER_ERROR, "Internal server error", context_kwargs, e)
