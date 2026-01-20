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
from ..models.container import ContainerComponent
from ..models.user import User
from ..services.container_service import (
    ContainerCapacityError,
    ContainerService,
    ContainerServiceError,
)
from ..services.inventory_service import InventoryStack
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.error_logging import create_context_from_request
from ..utils.rate_limiter import RateLimiter
from .container_models import LootAllRequest, TransferContainerRequest

logger = get_logger(__name__)

# Rate limiter for container operations (per-player: 20 requests per 60 seconds)
container_rate_limiter = RateLimiter(max_requests=20, window_seconds=60)


def create_error_context(request: Request | None, current_user: User | None, **metadata: Any) -> Any:
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
            context=create_error_context(None, current_user, operation="get_player_id"),
        )
    return UUID(str(player.player_id))


def get_container_service(persistence: Any) -> ContainerService:
    """
    Get ContainerService instance.

    Args:
        persistence: Async persistence layer instance

    Returns:
        ContainerService: Container service instance

    AI: Updated to require persistence parameter instead of accessing app.state.
        This enables proper dependency injection and testability.
    """
    return ContainerService(persistence=persistence)


def validate_user_for_open_container(current_user: User | None, request: Request) -> None:
    """Validate user for container opening. Raises exception if invalid."""
    if not current_user:
        context = create_error_context(request, current_user, operation="open_container")
        raise LoggedHTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=ErrorMessages.AUTHENTICATION_REQUIRED,
            context=context,
        )


def apply_rate_limiting_for_open_container(current_user: User, request: Request) -> None:
    """Apply rate limiting for container opening. Raises exception if rate limit exceeded."""
    try:
        container_rate_limiter.enforce_rate_limit(str(current_user.id))
    except RateLimitError as e:
        context = create_error_context(request, current_user, rate_limit_type="container_operation")
        raise LoggedHTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail=f"Rate limit exceeded. Retry after {e.retry_after} seconds",
            context=context,
        ) from e


def validate_user_for_transfer(current_user: User | None, request: Request) -> None:
    """Validate current_user for transfer operation."""
    if not current_user:
        context = create_error_context(request, current_user, operation="transfer_items")
        raise LoggedHTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=ErrorMessages.AUTHENTICATION_REQUIRED,
            context=context,
        )


def apply_rate_limiting_for_transfer(current_user: User, request: Request) -> None:
    """Apply rate limiting for transfer operation."""
    try:
        container_rate_limiter.enforce_rate_limit(str(current_user.id))
    except RateLimitError as e:
        context = create_error_context(request, current_user, rate_limit_type="container_operation")
        raise LoggedHTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail=f"Rate limit exceeded. Retry after {e.retry_after} seconds",
            context=context,
        ) from e


async def execute_transfer(
    container_service: ContainerService,
    request_data: TransferContainerRequest,
    player_id: UUID,
) -> dict[str, Any]:
    """Execute the transfer operation based on direction."""
    if request_data.direction == "to_container":
        return await container_service.transfer_to_container(
            request_data.container_id,
            player_id,
            request_data.mutation_token,
            cast(InventoryStack, request_data.stack),
            request_data.quantity,
        )
    # to_player
    return await container_service.transfer_from_container(
        request_data.container_id,
        player_id,
        request_data.mutation_token,
        cast(InventoryStack, request_data.stack),
        request_data.quantity,
    )


def handle_container_service_error(
    e: ContainerServiceError,
    request: Request,
    current_user: User,
    request_data: TransferContainerRequest | None = None,
    container_id: UUID | None = None,
) -> None:
    """
    Handle ContainerServiceError with appropriate status codes.

    Args:
        e: ContainerServiceError exception
        request: FastAPI Request object
        current_user: Current authenticated user
        request_data: Transfer request data (optional, for backward compatibility)
        container_id: Container UUID (optional, used if request_data is None)

    Raises:
        LoggedHTTPException: With appropriate status code based on error message
    """
    container_id_str = (
        str(request_data.container_id) if request_data else (str(container_id) if container_id else "unknown")
    )
    context = create_error_context(request, current_user, container_id=container_id_str, operation="transfer_items")
    error_str = str(e).lower()
    if "stale" in error_str or "token" in error_str or "mutation" in error_str:
        raise LoggedHTTPException(
            status_code=status.HTTP_412_PRECONDITION_FAILED,
            detail="Stale mutation token. Please reopen the container.",
            context=context,
        ) from e
    if "invalid" in error_str or "stack" in error_str:
        raise LoggedHTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid item stack",
            context=context,
        ) from e
    raise LoggedHTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="Failed to transfer items",
        context=context,
    ) from e


def validate_user_for_close_container(current_user: User | None, request: Request) -> None:
    """Validate current_user for close_container operation."""
    if not current_user:
        context = create_error_context(request, current_user, operation="close_container")
        raise LoggedHTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=ErrorMessages.AUTHENTICATION_REQUIRED,
            context=context,
        )


def apply_rate_limiting_for_close_container(current_user: User, request: Request) -> None:
    """Apply rate limiting for close_container operation."""
    try:
        container_rate_limiter.enforce_rate_limit(str(current_user.id))
    except RateLimitError as e:
        context = create_error_context(request, current_user, rate_limit_type="container_operation")
        raise LoggedHTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail=f"Rate limit exceeded. Retry after {e.retry_after} seconds",
            context=context,
        ) from e


def validate_user_for_loot_all(current_user: User | None, request: Request) -> None:
    """Validate current_user for loot_all operation."""
    if not current_user:
        context = create_error_context(request, current_user, operation="loot_all")
        raise LoggedHTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=ErrorMessages.AUTHENTICATION_REQUIRED,
            context=context,
        )


def apply_rate_limiting_for_loot_all(current_user: User, request: Request) -> None:
    """Apply rate limiting for loot_all operation."""
    try:
        container_rate_limiter.enforce_rate_limit(str(current_user.id))
    except RateLimitError as e:
        context = create_error_context(request, current_user, rate_limit_type="container_operation")
        raise LoggedHTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail=f"Rate limit exceeded. Retry after {e.retry_after} seconds",
            context=context,
        ) from e


async def get_container_and_player_for_loot_all(
    persistence: Any, request_data: LootAllRequest, player_id: UUID, request: Request, current_user: User
) -> tuple[ContainerComponent, Any, list[InventoryStack]]:
    """Get container and player data for loot_all operation."""
    container_data = await persistence.get_container(request_data.container_id)
    if not container_data:
        context = create_error_context(
            request, current_user, container_id=str(request_data.container_id), operation="loot_all"
        )
        raise LoggedHTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Container not found",
            context=context,
        )

    container = ContainerComponent.model_validate(container_data)

    player = persistence.get_player(player_id)
    if not player:
        context = create_error_context(request, current_user, player_id=str(player_id), operation="loot_all")
        raise LoggedHTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Player not found",
            context=context,
        )

    player_inventory = getattr(player, "inventory", [])
    return container, player, player_inventory


async def transfer_all_items_from_container(
    container_service: ContainerService,
    request_data: LootAllRequest,
    player_id: UUID,
    container: ContainerComponent,
    player_inventory: list[InventoryStack],
) -> tuple[dict[str, Any], list[InventoryStack]]:
    """Transfer all items from container to player, returning updated container and inventory."""
    container_data = container.model_dump()
    updated_inventory = player_inventory

    for item in container.items:
        try:
            result = await container_service.transfer_from_container(
                request_data.container_id,
                player_id,
                request_data.mutation_token,
                item,
                item.get("quantity", 1),
            )
            container_data = result.get("container", container_data)
            updated_inventory = result.get("player_inventory", updated_inventory)
        except ContainerCapacityError:
            logger.warning(
                "Loot-all stopped due to capacity",
                container_id=str(request_data.container_id),
                player_id=str(player_id),
            )
            break
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Item transfer errors unpredictable, must continue with other items
            logger.warning(
                "Error transferring item during loot-all",
                error=str(e),
                container_id=str(request_data.container_id),
                player_id=str(player_id),
            )
            continue

    return container_data, updated_inventory
