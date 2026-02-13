"""
Exception handlers for container API endpoints.

This module contains functions to handle exceptions raised during container operations,
converting them to appropriate HTTP exceptions with proper error context.
"""

from uuid import UUID

from fastapi import Request, status

from ..exceptions import LoggedHTTPException
from ..models.user import User
from ..services.container_service import ContainerCapacityError, ContainerServiceError
from ..structured_logging.enhanced_logging_config import get_logger
from .container_helpers import create_error_context

logger = get_logger(__name__)


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
        raise LoggedHTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Container not found",
            **context_kwargs,
        ) from e

    if isinstance(e, ContainerLockedError):
        raise LoggedHTTPException(
            status_code=status.HTTP_423_LOCKED,
            detail="Container is locked",
            **context_kwargs,
        ) from e

    if isinstance(e, ContainerAccessDeniedError):
        raise LoggedHTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied",
            **context_kwargs,
        ) from e

    if isinstance(e, ContainerServiceError):
        # Check if it's an "already open" error
        error_str = str(e).lower()
        if "already" in error_str or "open" in error_str:
            raise LoggedHTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Container is already open",
                **context_kwargs,
            ) from e
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to open container",
            **context_kwargs,
        ) from e

    # Generic exception handler
    logger.error("Unexpected error opening container", error=str(e), exc_info=True, **context_kwargs)
    raise LoggedHTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="Internal server error",
        **context_kwargs,
    ) from e


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
        raise LoggedHTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Container not found",
            **context_kwargs,
        ) from e

    if isinstance(e, ContainerCapacityError):
        raise LoggedHTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Capacity exceeded",
            **context_kwargs,
        ) from e

    if isinstance(e, ContainerAccessDeniedError):
        raise LoggedHTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied",
            **context_kwargs,
        ) from e

    if isinstance(e, ContainerServiceError):
        # Check for specific ContainerServiceError cases that need special handling
        error_str = str(e).lower()
        if "stale" in error_str or "token" in error_str or "mutation" in error_str:
            raise LoggedHTTPException(
                status_code=status.HTTP_412_PRECONDITION_FAILED,
                detail="Stale mutation token. Please reopen the container.",
                **context_kwargs,
            ) from e
        if "invalid" in error_str or "stack" in error_str:
            raise LoggedHTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid item stack",
                **context_kwargs,
            ) from e
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to transfer items",
            **context_kwargs,
        ) from e

    if isinstance(e, ValidationError):
        raise LoggedHTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Validation error: {str(e)}",
            **context_kwargs,
        ) from e

    # Generic exception handler
    logger.error("Unexpected error transferring items", error=str(e), exc_info=True, **context_kwargs)
    raise LoggedHTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="Internal server error",
        **context_kwargs,
    ) from e


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
        raise LoggedHTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Container not found",
            **context_kwargs,
        ) from e

    if isinstance(e, ContainerServiceError):
        # Check for invalid token
        error_str = str(e).lower()
        if "token" in error_str or "invalid" in error_str:
            raise LoggedHTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid mutation token",
                **context_kwargs,
            ) from e
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to close container",
            **context_kwargs,
        ) from e

    # Generic exception handler
    logger.error("Unexpected error closing container", error=str(e), exc_info=True, **context_kwargs)
    raise LoggedHTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="Internal server error",
        **context_kwargs,
    ) from e


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
        raise LoggedHTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Container not found",
            **context_kwargs,
        ) from e

    if isinstance(e, ContainerLockedError):
        raise LoggedHTTPException(
            status_code=status.HTTP_423_LOCKED,
            detail="Container is locked",
            **context_kwargs,
        ) from e

    if isinstance(e, ContainerAccessDeniedError):
        raise LoggedHTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied",
            **context_kwargs,
        ) from e

    if isinstance(e, ContainerCapacityError):
        raise LoggedHTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Player inventory capacity exceeded",
            **context_kwargs,
        ) from e

    if isinstance(e, ContainerServiceError):
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to loot items from container",
            **context_kwargs,
        ) from e

    # Generic exception handler
    # Use error=str(e) instead of exc_info=True to avoid Unicode encoding issues on Windows
    logger.error("Unexpected error in loot-all", error=str(e), **context_kwargs)
    raise LoggedHTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="Internal server error",
        **context_kwargs,
    ) from e
