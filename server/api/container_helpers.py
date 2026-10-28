"""
Helper functions for container API endpoints.

This module contains utility functions, validation helpers, rate limiting,
and event emission helpers used by container API endpoints.
"""

from typing import Any, cast
from uuid import UUID

from fastapi import Request, status

from ..error_types import ErrorMessages
from ..exceptions import LoggedHTTPException, RateLimitError
from ..game.player_registry import PlayerRegistry
from ..models.user import User
from ..services.container_service import (
    ContainerService,
    ContainerServiceError,
)
from ..services.container_service import get_container_service as shared_container_service
from ..services.inventory_service import InventoryStack
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.rate_limiter import RateLimiter
from .container_models import TransferContainerRequest

logger = get_logger(__name__)

# Rate limiter for container operations (per-player: 20 requests per 60 seconds)
container_rate_limiter = RateLimiter(max_requests=20, window_seconds=60)


def create_error_context(_request: Request | None, current_user: User | None, **metadata: Any) -> dict[str, Any]:
    """
    Create error context dict from request and user.

    Helper function to reduce duplication in exception handling.
    Returns a dict suitable for passing as **kwargs to LoggedHTTPException.

    Args:
        _request: FastAPI Request object (unused; kept for API consistency with callers).
        current_user: Current user or None
        **metadata: Additional metadata to add to context

    Returns:
        dict: Error context dict with request and user information
    """
    context_dict: dict[str, Any] = {}
    if current_user:
        context_dict["user_id"] = str(current_user.id)
    context_dict.update(metadata)
    return context_dict


async def get_player_id_from_user(current_user: User, persistence: Any) -> UUID:
    """
    Get player_id from user.

    Args:
        current_user: Current authenticated user
        persistence: Async persistence layer instance

    Returns:
        UUID: Player UUID

    Raises:
        LoggedHTTPException: If player not found
    """
    player = await persistence.get_player_by_user_id(str(current_user.id))
    if not player:
        raise LoggedHTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Player not found for user",
            **create_error_context(None, current_user, operation="get_player_id"),
        )
    return UUID(str(player.player_id))


def get_container_service(persistence: Any) -> ContainerService:
    """
    Get the ContainerService for this persistence layer, reusing one across calls.

    ContainerService tracks open-container sessions and mutation tokens in an
    instance-level dict (see ContainerService._open_containers). A fresh instance per
    call -- which this used to construct unconditionally -- gives every HTTP request
    (and every text command) its own empty session store, so an open() from one
    request is invisible to the transfer()/close() of the next: the whole exclusivity
    and idempotent-reopen contract silently never worked outside a single call. Caching
    by persistence identity fixes that for the real server (one long-lived persistence
    singleton -> one shared ContainerService) while keeping unit tests isolated (each
    test's own mock persistence gets its own service).

    Args:
        persistence: Async persistence layer instance

    Returns:
        ContainerService: Container service instance, shared across calls for the same persistence
    """
    # The cache itself lives in the service layer so realtime disconnect cleanup can reach it (#964).
    return shared_container_service(cast(object, persistence))


def validate_user_for_open_container(current_user: User | None, _request: Request) -> None:
    """Validate user for container opening. Raises exception if invalid."""
    if not current_user:
        raise LoggedHTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=ErrorMessages.AUTHENTICATION_REQUIRED,
            operation="open_container",
        )


def apply_rate_limiting_for_open_container(current_user: User, _request: Request) -> None:
    """Apply rate limiting for container opening. Raises exception if rate limit exceeded."""
    try:
        container_rate_limiter.enforce_rate_limit(str(current_user.id))
    except RateLimitError as e:
        raise LoggedHTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail=f"Rate limit exceeded. Retry after {e.retry_after} seconds",
            user_id=str(current_user.id) if current_user else None,
            rate_limit_type="container_operation",
        ) from e


def validate_user_for_transfer(current_user: User | None, _request: Request) -> None:
    """Validate current_user for transfer operation."""
    if not current_user:
        raise LoggedHTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=ErrorMessages.AUTHENTICATION_REQUIRED,
            operation="transfer_items",
        )


def apply_rate_limiting_for_transfer(current_user: User, _request: Request) -> None:
    """Apply rate limiting for transfer operation."""
    try:
        container_rate_limiter.enforce_rate_limit(str(current_user.id))
    except RateLimitError as e:
        raise LoggedHTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail=f"Rate limit exceeded. Retry after {e.retry_after} seconds",
            user_id=str(current_user.id) if current_user else None,
            rate_limit_type="container_operation",
        ) from e


async def execute_transfer(
    container_service: ContainerService,
    request_data: TransferContainerRequest,
    player_id: UUID,
    registry: PlayerRegistry,
) -> dict[str, object]:
    """Execute the transfer operation based on direction; the registry commits player and container together."""
    if request_data.direction == "to_container":
        return await container_service.transfer_to_container(
            request_data.container_id,
            player_id,
            request_data.mutation_token,
            cast(InventoryStack, request_data.stack),
            request_data.quantity,
            registry=registry,
        )
    # to_player
    return await container_service.transfer_from_container(
        request_data.container_id,
        player_id,
        request_data.mutation_token,
        cast(InventoryStack, request_data.stack),
        request_data.quantity,
        registry=registry,
    )


# (keywords to match in the lowercased error message, status code, detail message)
_TRANSFER_SERVICE_ERROR_RULES: tuple[tuple[tuple[str, ...], int, str], ...] = (
    (
        ("stale", "token", "mutation"),
        status.HTTP_412_PRECONDITION_FAILED,
        "Stale mutation token. Please reopen the container.",
    ),
    (("invalid", "stack"), status.HTTP_400_BAD_REQUEST, "Invalid item stack"),
)


def _classify_transfer_service_error(error_str: str) -> tuple[int, str]:
    """Map a ContainerServiceError message to (status_code, detail) for transfer_items."""
    for keywords, status_code, detail in _TRANSFER_SERVICE_ERROR_RULES:
        if any(keyword in error_str for keyword in keywords):
            return status_code, detail
    return status.HTTP_500_INTERNAL_SERVER_ERROR, "Failed to transfer items"


def handle_container_service_error(
    e: ContainerServiceError,
    _request: Request,
    current_user: User,
    request_data: TransferContainerRequest | None = None,
    container_id: UUID | None = None,
) -> None:
    """
    Handle ContainerServiceError with appropriate status codes.

    Args:
        e: ContainerServiceError exception
        _request: FastAPI Request object (unused; kept for API consistency with callers).
        current_user: Current authenticated user
        request_data: Transfer request data (optional, for backward compatibility)
        container_id: Container UUID (optional, used if request_data is None)

    Raises:
        LoggedHTTPException: With appropriate status code based on error message
    """
    container_id_str = (
        str(request_data.container_id) if request_data else (str(container_id) if container_id else "unknown")
    )
    status_code, detail = _classify_transfer_service_error(str(e).lower())
    raise LoggedHTTPException(
        status_code=status_code,
        detail=detail,
        user_id=str(current_user.id) if current_user else None,
        container_id=container_id_str,
        operation="transfer_items",
    ) from e


def validate_user_for_close_container(current_user: User | None, _request: Request) -> None:
    """Validate current_user for close_container operation."""
    if not current_user:
        raise LoggedHTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=ErrorMessages.AUTHENTICATION_REQUIRED,
            operation="close_container",
        )


def apply_rate_limiting_for_close_container(current_user: User, _request: Request) -> None:
    """Apply rate limiting for close_container operation."""
    try:
        container_rate_limiter.enforce_rate_limit(str(current_user.id))
    except RateLimitError as e:
        raise LoggedHTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail=f"Rate limit exceeded. Retry after {e.retry_after} seconds",
            user_id=str(current_user.id) if current_user else None,
            rate_limit_type="container_operation",
        ) from e


def validate_user_for_loot_all(current_user: User | None, _request: Request) -> None:
    """Validate current_user for loot_all operation."""
    if not current_user:
        raise LoggedHTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=ErrorMessages.AUTHENTICATION_REQUIRED,
            operation="loot_all",
        )


def apply_rate_limiting_for_loot_all(current_user: User, _request: Request) -> None:
    """Apply rate limiting for loot_all operation."""
    try:
        container_rate_limiter.enforce_rate_limit(str(current_user.id))
    except RateLimitError as e:
        raise LoggedHTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail=f"Rate limit exceeded. Retry after {e.retry_after} seconds",
            user_id=str(current_user.id) if current_user else None,
            rate_limit_type="container_operation",
        ) from e
