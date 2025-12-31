"""
Container API endpoints for unified container system.

As documented in the restricted archives of Miskatonic University, container
API endpoints provide secure access to environmental props, wearable gear,
and corpse storage systems. These endpoints enforce proper access control,
rate limiting, and mutation guards to prevent unauthorized artifact handling.
"""

from __future__ import annotations

from typing import Any, cast
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Request, status
from pydantic import BaseModel, Field, field_validator

from ..auth.users import get_current_user
from ..error_types import ErrorMessages
from ..exceptions import LoggedHTTPException, RateLimitError, ValidationError
from ..models.container import ContainerComponent
from ..models.user import User

# Removed: from ..persistence import get_persistence - now using async_persistence from request
from ..services.container_service import (
    ContainerAccessDeniedError,
    ContainerCapacityError,
    ContainerLockedError,
    ContainerNotFoundError,
    ContainerService,
    ContainerServiceError,
)
from ..services.container_websocket_events import (
    emit_container_closed,
    emit_container_opened,
    emit_container_opened_to_room,
    emit_container_updated,
)
from ..services.inventory_service import InventoryStack
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.audit_logger import audit_logger
from ..utils.error_logging import create_context_from_request
from ..utils.rate_limiter import RateLimiter

logger = get_logger(__name__)

# Create container router
container_router = APIRouter(prefix="/api/containers", tags=["containers"])

# Rate limiters for container operations
# Per-player rate limiting: 20 requests per 60 seconds
container_rate_limiter = RateLimiter(max_requests=20, window_seconds=60)

# Rate limiting metrics for telemetry
_container_rate_limit_metrics: dict[str, dict[str, int]] = {
    "total_requests": {},
    "rate_limited": {},
    "by_endpoint": {},
}


# Request/Response Models
class OpenContainerRequest(BaseModel):
    """Request model for opening a container."""

    __slots__ = ()  # Performance optimization

    container_id: UUID = Field(..., description="UUID of the container to open")


class TransferContainerRequest(BaseModel):
    """Request model for transferring items to/from container."""

    __slots__ = ()  # Performance optimization

    container_id: UUID = Field(..., description="UUID of the container")
    mutation_token: str = Field(..., description="Mutation token from open_container")
    direction: str = Field(..., description="Transfer direction: 'to_container' or 'to_player'")
    stack: dict[str, Any] = Field(..., description="Item stack to transfer")
    quantity: int = Field(..., ge=1, description="Quantity to transfer")

    @field_validator("direction")
    @classmethod
    def validate_direction(cls, v: str) -> str:
        """Validate transfer direction."""
        if v not in ("to_container", "to_player"):
            raise ValueError("direction must be 'to_container' or 'to_player'")
        return v


class CloseContainerRequest(BaseModel):
    """Request model for closing a container."""

    __slots__ = ()  # Performance optimization

    container_id: UUID = Field(..., description="UUID of the container to close")
    mutation_token: str = Field(..., description="Mutation token from open_container")


class LootAllRequest(BaseModel):
    """Request model for looting all items from a container."""

    __slots__ = ()  # Performance optimization

    container_id: UUID = Field(..., description="UUID of the container")
    mutation_token: str = Field(..., description="Mutation token from open_container")


def _create_error_context(request: Request | None, current_user: User | None, **metadata: Any) -> Any:
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


async def _get_player_id_from_user(current_user: User, persistence: Any) -> UUID:
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
            context=_create_error_context(None, current_user, operation="get_player_id"),
        )
    return UUID(str(player.player_id))


def _get_container_service(persistence: Any | None = None, request: Request | None = None) -> ContainerService:
    """
    Get ContainerService instance.

    Args:
        persistence: Async persistence layer instance (optional, will get from request if not provided)
        request: FastAPI Request object (required if persistence is None)

    Returns:
        ContainerService: Container service instance
    """
    if persistence is None:
        if request is None:
            raise ValueError("Either persistence or request must be provided")
        persistence = request.app.state.persistence  # Now async_persistence
    return ContainerService(persistence=persistence)


@container_router.post("/open")
async def open_container(
    request_data: OpenContainerRequest,
    request: Request,
    current_user: User = Depends(get_current_user),
) -> dict[str, Any]:
    """
    Open a container for interaction.

    Initiates interaction with a container in the player's current room or inventory.
    Returns container data and a mutation token for subsequent operations.

    Rate limited to 20 requests per 60 seconds per player.

    Args:
        request_data: OpenContainerRequest with container_id
        request: FastAPI Request object
        current_user: Current authenticated user
        persistence: Persistence layer instance

    Returns:
        dict containing container data and mutation_token

    Raises:
        HTTPException(404): Container not found
        HTTPException(403): Access denied
        HTTPException(409): Container already open
        HTTPException(423): Container is locked
        HTTPException(429): Rate limit exceeded
    """
    if not current_user:
        context = _create_error_context(request, current_user, operation="open_container")
        raise LoggedHTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=ErrorMessages.AUTHENTICATION_REQUIRED,
            context=context,
        )

    # Apply rate limiting
    try:
        container_rate_limiter.enforce_rate_limit(str(current_user.id))
    except RateLimitError as e:
        context = _create_error_context(request, current_user, rate_limit_type="container_operation")
        raise LoggedHTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail=f"Rate limit exceeded. Retry after {e.retry_after} seconds",
            context=context,
        ) from e

    try:
        # Get persistence from request (now async_persistence)
        persistence = request.app.state.persistence

        # Get player_id from user
        player_id = await _get_player_id_from_user(current_user, persistence)

        # Get container service
        container_service = _get_container_service(persistence, request)

        # Open container
        result = await container_service.open_container(request_data.container_id, player_id)

        # Emit WebSocket event
        try:
            connection_manager = request.app.state.connection_manager
            if connection_manager:
                from datetime import UTC, datetime, timedelta

                container = ContainerComponent.model_validate(result["container"])
                mutation_token = result["mutation_token"]
                expires_at = datetime.now(UTC) + timedelta(minutes=5)  # TODO: Get actual expiry from mutation guard

                # Emit to opening player
                await emit_container_opened(
                    connection_manager=connection_manager,
                    container=container,
                    player_id=player_id,
                    mutation_token=mutation_token,
                    expires_at=expires_at,
                )

                # If environmental container, also broadcast to room
                if container.room_id:
                    await emit_container_opened_to_room(
                        connection_manager=connection_manager,
                        container=container,
                        room_id=container.room_id,
                        actor_id=player_id,
                        mutation_token=mutation_token,
                        expires_at=expires_at,
                    )
        except Exception as e:
            # Log but don't fail the request if event emission fails
            logger.warning(
                "Failed to emit container.opened event",
                error=str(e),
                container_id=str(request_data.container_id),
                player_id=str(player_id),
            )

        logger.info(
            "Container opened",
            container_id=str(request_data.container_id),
            player_id=str(player_id),
            user_id=str(current_user.id),
        )

        return result

    except ContainerNotFoundError as e:
        context = _create_error_context(
            request, current_user, container_id=str(request_data.container_id), operation="open_container"
        )
        raise LoggedHTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Container not found",
            context=context,
        ) from e

    except ContainerLockedError as e:
        context = _create_error_context(
            request, current_user, container_id=str(request_data.container_id), operation="open_container"
        )
        raise LoggedHTTPException(
            status_code=status.HTTP_423_LOCKED,
            detail="Container is locked",
            context=context,
        ) from e

    except ContainerAccessDeniedError as e:
        context = _create_error_context(
            request, current_user, container_id=str(request_data.container_id), operation="open_container"
        )
        raise LoggedHTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied",
            context=context,
        ) from e

    except ContainerServiceError as e:
        context = _create_error_context(
            request, current_user, container_id=str(request_data.container_id), operation="open_container"
        )
        # Check if it's an "already open" error
        if "already" in str(e).lower() or "open" in str(e).lower():
            raise LoggedHTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Container is already open",
                context=context,
            ) from e
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to open container",
            context=context,
        ) from e

    except Exception as e:
        context = _create_error_context(
            request, current_user, container_id=str(request_data.container_id), operation="open_container"
        )
        logger.error("Unexpected error opening container", error=str(e), exc_info=True, **context.to_dict())
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
            context=context,
        ) from e


@container_router.post("/transfer")
async def transfer_items(
    request_data: TransferContainerRequest,
    request: Request,
    current_user: User = Depends(get_current_user),
) -> dict[str, Any]:
    """
    Transfer items between container and player inventory.

    Moves items bidirectionally between container and player inventory.
    Requires a valid mutation token from open_container.

    Rate limited to 20 requests per 60 seconds per player.

    Args:
        request_data: TransferContainerRequest with container_id, mutation_token, direction, stack, quantity
        request: FastAPI Request object
        current_user: Current authenticated user
        persistence: Persistence layer instance

    Returns:
        dict containing updated container and player_inventory

    Raises:
        HTTPException(400): Invalid stack or token
        HTTPException(403): Access denied
        HTTPException(409): Capacity exceeded
        HTTPException(412): Stale mutation token
        HTTPException(429): Rate limit exceeded
    """
    if not current_user:
        context = _create_error_context(request, current_user, operation="transfer_items")
        raise LoggedHTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=ErrorMessages.AUTHENTICATION_REQUIRED,
            context=context,
        )

    # Apply rate limiting
    try:
        container_rate_limiter.enforce_rate_limit(str(current_user.id))
    except RateLimitError as e:
        context = _create_error_context(request, current_user, rate_limit_type="container_operation")
        raise LoggedHTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail=f"Rate limit exceeded. Retry after {e.retry_after} seconds",
            context=context,
        ) from e

    try:
        # Get persistence from request (now async_persistence)
        persistence = request.app.state.persistence

        # Get player_id from user
        player_id = await _get_player_id_from_user(current_user, persistence)

        # Get container service
        container_service = _get_container_service(persistence, request)

        # Transfer items
        if request_data.direction == "to_container":
            result = await container_service.transfer_to_container(
                request_data.container_id,
                player_id,
                request_data.mutation_token,
                cast(InventoryStack, request_data.stack),
                request_data.quantity,
            )
        else:  # to_player
            result = await container_service.transfer_from_container(
                request_data.container_id,
                player_id,
                request_data.mutation_token,
                cast(InventoryStack, request_data.stack),
                request_data.quantity,
            )

        # Emit WebSocket event for container update
        try:
            connection_manager = request.app.state.connection_manager
            if connection_manager and result.get("container"):
                container = ContainerComponent.model_validate(result["container"])
                if container.room_id:
                    # Calculate diff for the update
                    diff = {
                        "items": {
                            "direction": request_data.direction,
                            "stack": request_data.stack,
                            "quantity": request_data.quantity,
                        },
                    }
                    await emit_container_updated(
                        connection_manager=connection_manager,
                        container_id=request_data.container_id,
                        room_id=container.room_id,
                        diff=diff,
                        actor_id=player_id,
                    )
        except Exception as e:
            # Log but don't fail the request if event emission fails
            logger.warning(
                "Failed to emit container.updated event",
                error=str(e),
                container_id=str(request_data.container_id),
                player_id=str(player_id),
            )

        logger.info(
            "Items transferred",
            container_id=str(request_data.container_id),
            player_id=str(player_id),
            direction=request_data.direction,
            quantity=request_data.quantity,
        )

        return result

    except ContainerNotFoundError as e:
        context = _create_error_context(
            request, current_user, container_id=str(request_data.container_id), operation="transfer_items"
        )
        raise LoggedHTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Container not found",
            context=context,
        ) from e

    except ContainerCapacityError as e:
        context = _create_error_context(
            request, current_user, container_id=str(request_data.container_id), operation="transfer_items"
        )
        raise LoggedHTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Capacity exceeded",
            context=context,
        ) from e

    except ContainerAccessDeniedError as e:
        context = _create_error_context(
            request, current_user, container_id=str(request_data.container_id), operation="transfer_items"
        )
        raise LoggedHTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied",
            context=context,
        ) from e

    except ContainerServiceError as e:
        context = _create_error_context(
            request, current_user, container_id=str(request_data.container_id), operation="transfer_items"
        )
        # Check for stale mutation token
        if "stale" in str(e).lower() or "token" in str(e).lower() or "mutation" in str(e).lower():
            raise LoggedHTTPException(
                status_code=status.HTTP_412_PRECONDITION_FAILED,
                detail="Stale mutation token. Please reopen the container.",
                context=context,
            ) from e
        # Check for invalid stack
        if "invalid" in str(e).lower() or "stack" in str(e).lower():
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

    except ValidationError as e:
        context = _create_error_context(
            request, current_user, container_id=str(request_data.container_id), operation="transfer_items"
        )
        raise LoggedHTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Validation error: {str(e)}",
            context=context,
        ) from e

    except Exception as e:
        context = _create_error_context(
            request, current_user, container_id=str(request_data.container_id), operation="transfer_items"
        )
        logger.error("Unexpected error transferring items", error=str(e), exc_info=True, **context.to_dict())
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
            context=context,
        ) from e


@container_router.post("/close")
async def close_container(
    request_data: CloseContainerRequest,
    request: Request,
    current_user: User = Depends(get_current_user),
) -> dict[str, str]:
    """
    Close a container and release the mutation guard.

    Releases the mutation guard and closes the container UI.
    Requires a valid mutation token from open_container.

    Rate limited to 20 requests per 60 seconds per player.

    Args:
        request_data: CloseContainerRequest with container_id and mutation_token
        request: FastAPI Request object
        current_user: Current authenticated user
        persistence: Persistence layer instance

    Returns:
        dict with status="closed"

    Raises:
        HTTPException(400): Invalid token
        HTTPException(404): Container not found
        HTTPException(429): Rate limit exceeded
    """
    if not current_user:
        context = _create_error_context(request, current_user, operation="close_container")
        raise LoggedHTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=ErrorMessages.AUTHENTICATION_REQUIRED,
            context=context,
        )

    # Apply rate limiting
    try:
        container_rate_limiter.enforce_rate_limit(str(current_user.id))
    except RateLimitError as e:
        context = _create_error_context(request, current_user, rate_limit_type="container_operation")
        raise LoggedHTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail=f"Rate limit exceeded. Retry after {e.retry_after} seconds",
            context=context,
        ) from e

    try:
        # Get persistence from request (now async_persistence)
        persistence = request.app.state.persistence

        # Get player_id from user
        player_id = await _get_player_id_from_user(current_user, persistence)

        # Get container service
        container_service = _get_container_service(persistence, request)

        # Close container
        await container_service.close_container(request_data.container_id, player_id, request_data.mutation_token)

        # Emit WebSocket event
        try:
            connection_manager = request.app.state.connection_manager
            if connection_manager:
                # Get container to find room_id
                container_data = persistence.get_container(request_data.container_id)
                if container_data:
                    container = ContainerComponent.model_validate(container_data)
                    if container.room_id:
                        await emit_container_closed(
                            connection_manager=connection_manager,
                            container_id=request_data.container_id,
                            room_id=container.room_id,
                            player_id=player_id,
                        )
        except Exception as e:
            # Log but don't fail the request if event emission fails
            logger.warning(
                "Failed to emit container.closed event",
                error=str(e),
                container_id=str(request_data.container_id),
                player_id=str(player_id),
            )

        logger.info(
            "Container closed",
            container_id=str(request_data.container_id),
            player_id=str(player_id),
            user_id=str(current_user.id),
        )

        return {"status": "closed"}

    except ContainerNotFoundError as e:
        context = _create_error_context(
            request, current_user, container_id=str(request_data.container_id), operation="close_container"
        )
        raise LoggedHTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Container not found",
            context=context,
        ) from e

    except ContainerServiceError as e:
        context = _create_error_context(
            request, current_user, container_id=str(request_data.container_id), operation="close_container"
        )
        # Check for invalid token
        if "token" in str(e).lower() or "invalid" in str(e).lower():
            raise LoggedHTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid mutation token",
                context=context,
            ) from e
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to close container",
            context=context,
        ) from e

    except Exception as e:
        context = _create_error_context(
            request, current_user, container_id=str(request_data.container_id), operation="close_container"
        )
        logger.error("Unexpected error closing container", error=str(e), exc_info=True, **context.to_dict())
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
            context=context,
        ) from e


@container_router.post("/loot-all")
async def loot_all_items(
    request_data: LootAllRequest,
    request: Request,
    current_user: User = Depends(get_current_user),
) -> dict[str, Any]:
    """
    Loot all eligible items from a container.

    Convenience action to move all eligible stacks from container to player inventory,
    subject to capacity constraints. Requires a valid mutation token from open_container.

    Rate limited to 20 requests per 60 seconds per player.

    Args:
        request_data: LootAllRequest with container_id and mutation_token
        request: FastAPI Request object
        current_user: Current authenticated user
        persistence: Persistence layer instance

    Returns:
        dict containing updated container and player_inventory

    Raises:
        HTTPException(403): Access denied
        HTTPException(409): Capacity exceeded
        HTTPException(423): Container is locked
        HTTPException(429): Rate limit exceeded
    """
    if not current_user:
        context = _create_error_context(request, current_user, operation="loot_all")
        raise LoggedHTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=ErrorMessages.AUTHENTICATION_REQUIRED,
            context=context,
        )

    # Apply rate limiting
    try:
        container_rate_limiter.enforce_rate_limit(str(current_user.id))
    except RateLimitError as e:
        context = _create_error_context(request, current_user, rate_limit_type="container_operation")
        raise LoggedHTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail=f"Rate limit exceeded. Retry after {e.retry_after} seconds",
            context=context,
        ) from e

    try:
        # Get persistence from request (now async_persistence)
        persistence = request.app.state.persistence

        # Get player_id from user
        player_id = await _get_player_id_from_user(current_user, persistence)

        # Get container service
        container_service = _get_container_service(persistence, request)

        # Get container to check items
        container_data = await persistence.get_container(request_data.container_id)
        if not container_data:
            context = _create_error_context(
                request, current_user, container_id=str(request_data.container_id), operation="loot_all"
            )
            raise LoggedHTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Container not found",
                context=context,
            )

        # Transfer all items from container to player
        container = ContainerComponent.model_validate(container_data)
        player_inventory: list[InventoryStack] = []

        # Get player inventory
        player = persistence.get_player(player_id)
        if not player:
            context = _create_error_context(request, current_user, player_id=str(player_id), operation="loot_all")
            raise LoggedHTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Player not found",
                context=context,
            )

        player_inventory = getattr(player, "inventory", [])

        # Try to transfer each item
        for item in container.items:
            try:
                result = await container_service.transfer_from_container(
                    request_data.container_id,
                    player_id,
                    request_data.mutation_token,
                    item,
                    item.get("quantity", 1),
                )
                # Update container and player inventory from result
                container_data = result.get("container", {})
                player_inventory = result.get("player_inventory", player_inventory)
            except ContainerCapacityError:
                # Stop if capacity exceeded
                logger.warning(
                    "Loot-all stopped due to capacity",
                    container_id=str(request_data.container_id),
                    player_id=str(player_id),
                )
                break
            except Exception as e:
                # Log but continue with other items
                logger.warning(
                    "Error transferring item during loot-all",
                    error=str(e),
                    container_id=str(request_data.container_id),
                    player_id=str(player_id),
                )
                continue

        # Get final container state
        final_container_data = persistence.get_container(request_data.container_id)
        if final_container_data:
            final_container = ContainerComponent.model_validate(final_container_data)
        else:
            final_container = container

        # Emit WebSocket event for container update
        try:
            connection_manager = request.app.state.connection_manager
            if connection_manager and final_container.room_id:
                diff = {
                    "items": {
                        "loot_all": True,
                        "items_removed": len(container.items) - len(final_container.items),
                    },
                }
                await emit_container_updated(
                    connection_manager=connection_manager,
                    container_id=request_data.container_id,
                    room_id=final_container.room_id,
                    diff=diff,
                    actor_id=player_id,
                )
        except Exception as e:
            # Log but don't fail the request if event emission fails
            logger.warning(
                "Failed to emit container.updated event for loot-all",
                error=str(e),
                container_id=str(request_data.container_id),
                player_id=str(player_id),
            )

        logger.info(
            "Loot-all completed",
            container_id=str(request_data.container_id),
            player_id=str(player_id),
            items_transferred=len(container.items) - len(final_container.items),
        )

        # Audit log container loot_all
        try:
            items_count = len(container.items) - len(final_container.items)
            audit_logger.log_container_interaction(
                player_id=str(player_id),
                player_name=str(player.name),
                container_id=str(request_data.container_id),
                event_type="container_loot_all",
                source_type=final_container.source_type.value,
                room_id=final_container.room_id,
                items_count=items_count,
                success=True,
            )
        except Exception as e:
            logger.warning("Failed to log container loot_all to audit log", error=str(e))

        return {
            "container": final_container.model_dump(),
            "player_inventory": player_inventory,
        }

    except ContainerNotFoundError as e:
        context = _create_error_context(
            request, current_user, container_id=str(request_data.container_id), operation="loot_all"
        )
        raise LoggedHTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Container not found",
            context=context,
        ) from e

    except ContainerLockedError as e:
        context = _create_error_context(
            request, current_user, container_id=str(request_data.container_id), operation="loot_all"
        )
        raise LoggedHTTPException(
            status_code=status.HTTP_423_LOCKED,
            detail="Container is locked",
            context=context,
        ) from e

    except ContainerAccessDeniedError as e:
        context = _create_error_context(
            request, current_user, container_id=str(request_data.container_id), operation="loot_all"
        )
        raise LoggedHTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied",
            context=context,
        ) from e

    except ContainerCapacityError as e:
        context = _create_error_context(
            request, current_user, container_id=str(request_data.container_id), operation="loot_all"
        )
        raise LoggedHTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Player inventory capacity exceeded",
            context=context,
        ) from e

    except (LoggedHTTPException, HTTPException):
        # Re-raise HTTP exceptions (including LoggedHTTPException) to let FastAPI handle them
        raise
    except Exception as e:
        context = _create_error_context(
            request, current_user, container_id=str(request_data.container_id), operation="loot_all"
        )
        # Use error=str(e) instead of exc_info=True to avoid Unicode encoding issues on Windows
        logger.error("Unexpected error in loot-all", error=str(e), **context.to_dict())
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
            context=context,
        ) from e
