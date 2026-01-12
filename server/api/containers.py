"""
Container API endpoints for unified container system.

As documented in the restricted archives of Miskatonic University, container
API endpoints provide secure access to environmental props, wearable gear,
and corpse storage systems. These endpoints enforce proper access control,
rate limiting, and mutation guards to prevent unauthorized artifact handling.
"""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Request, status

from ..auth.users import get_current_user
from ..exceptions import LoggedHTTPException, ValidationError
from ..models.container import ContainerComponent
from ..models.user import User
from ..services.container_service import (
    ContainerAccessDeniedError,
    ContainerCapacityError,
    ContainerLockedError,
    ContainerNotFoundError,
    ContainerServiceError,
)
from ..services.container_websocket_events import emit_container_closed
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.audit_logger import audit_logger
from .container_helpers import (
    apply_rate_limiting_for_close_container,
    apply_rate_limiting_for_loot_all,
    apply_rate_limiting_for_open_container,
    apply_rate_limiting_for_transfer,
    create_error_context,
    emit_container_opened_events,
    emit_loot_all_event,
    emit_transfer_event,
    execute_transfer,
    get_container_and_player_for_loot_all,
    get_container_service,
    get_player_id_from_user,
    handle_container_service_error,
    transfer_all_items_from_container,
    validate_user_for_close_container,
    validate_user_for_loot_all,
    validate_user_for_open_container,
    validate_user_for_transfer,
)
from .container_models import CloseContainerRequest, LootAllRequest, OpenContainerRequest, TransferContainerRequest

logger = get_logger(__name__)

# Create container router
container_router = APIRouter(prefix="/api/containers", tags=["containers"])

# Rate limiting metrics for telemetry
_container_rate_limit_metrics: dict[str, dict[str, int]] = {
    "total_requests": {},
    "rate_limited": {},
    "by_endpoint": {},
}


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
    validate_user_for_open_container(current_user, request)
    apply_rate_limiting_for_open_container(current_user, request)

    try:
        persistence = request.app.state.persistence
        player_id = await get_player_id_from_user(current_user, persistence)
        container_service = get_container_service(persistence, request)

        result = await container_service.open_container(request_data.container_id, player_id)

        await emit_container_opened_events(request, result, player_id, request_data.container_id)

        logger.info(
            "Container opened",
            container_id=str(request_data.container_id),
            player_id=str(player_id),
            user_id=str(current_user.id),
        )

        return result

    except ContainerNotFoundError as e:
        context = create_error_context(
            request, current_user, container_id=str(request_data.container_id), operation="open_container"
        )
        raise LoggedHTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Container not found",
            context=context,
        ) from e

    except ContainerLockedError as e:
        context = create_error_context(
            request, current_user, container_id=str(request_data.container_id), operation="open_container"
        )
        raise LoggedHTTPException(
            status_code=status.HTTP_423_LOCKED,
            detail="Container is locked",
            context=context,
        ) from e

    except ContainerAccessDeniedError as e:
        context = create_error_context(
            request, current_user, container_id=str(request_data.container_id), operation="open_container"
        )
        raise LoggedHTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied",
            context=context,
        ) from e

    except ContainerServiceError as e:
        context = create_error_context(
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

    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Container operation errors unpredictable, must create error context
        context = create_error_context(
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
    validate_user_for_transfer(current_user, request)
    apply_rate_limiting_for_transfer(current_user, request)

    try:
        persistence = request.app.state.persistence
        player_id = await get_player_id_from_user(current_user, persistence)
        container_service = get_container_service(persistence, request)

        result = await execute_transfer(container_service, request_data, player_id)
        await emit_transfer_event(request, request_data, result, player_id)

        logger.info(
            "Items transferred",
            container_id=str(request_data.container_id),
            player_id=str(player_id),
            direction=request_data.direction,
            quantity=request_data.quantity,
        )

        return result

    except ContainerNotFoundError as e:
        context = create_error_context(
            request, current_user, container_id=str(request_data.container_id), operation="transfer_items"
        )
        raise LoggedHTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Container not found",
            context=context,
        ) from e

    except ContainerCapacityError as e:
        context = create_error_context(
            request, current_user, container_id=str(request_data.container_id), operation="transfer_items"
        )
        raise LoggedHTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Capacity exceeded",
            context=context,
        ) from e

    except ContainerAccessDeniedError as e:
        context = create_error_context(
            request, current_user, container_id=str(request_data.container_id), operation="transfer_items"
        )
        raise LoggedHTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied",
            context=context,
        ) from e

    except ContainerServiceError as e:
        # handle_container_service_error always raises LoggedHTTPException, so this path never returns
        handle_container_service_error(e, request, current_user, request_data)
        raise AssertionError(
            "handle_container_service_error should always raise"
        ) from e  # Defensive: should never execute

    except ValidationError as e:
        context = create_error_context(
            request, current_user, container_id=str(request_data.container_id), operation="transfer_items"
        )
        raise LoggedHTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Validation error: {str(e)}",
            context=context,
        ) from e

    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Container operation errors unpredictable, must create error context
        context = create_error_context(
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
    validate_user_for_close_container(current_user, request)
    apply_rate_limiting_for_close_container(current_user, request)

    try:
        # Get persistence from request (now async_persistence)
        persistence = request.app.state.persistence

        # Get player_id from user
        player_id = await get_player_id_from_user(current_user, persistence)

        # Get container service
        container_service = get_container_service(persistence, request)

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
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Event emission errors unpredictable, must not fail request
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
        context = create_error_context(
            request, current_user, container_id=str(request_data.container_id), operation="close_container"
        )
        raise LoggedHTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Container not found",
            context=context,
        ) from e

    except ContainerServiceError as e:
        context = create_error_context(
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

    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Container operation errors unpredictable, must create error context
        context = create_error_context(
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
    validate_user_for_loot_all(current_user, request)
    apply_rate_limiting_for_loot_all(current_user, request)

    try:
        # Get persistence from request (now async_persistence)
        persistence = request.app.state.persistence

        # Get player_id from user
        player_id = await get_player_id_from_user(current_user, persistence)

        # Get container service
        container_service = get_container_service(persistence, request)

        # Get container and player data
        container, player, player_inventory = await get_container_and_player_for_loot_all(
            persistence, request_data, player_id, request, current_user
        )

        # Transfer all items from container to player
        _, player_inventory = await transfer_all_items_from_container(
            container_service, request_data, player_id, container, player_inventory
        )

        # Get final container state
        final_container_data = persistence.get_container(request_data.container_id)
        if final_container_data:
            final_container = ContainerComponent.model_validate(final_container_data)
        else:
            final_container = container

        # Emit WebSocket event for container update
        await emit_loot_all_event(request, request_data, final_container, player_id, container)

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
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Audit log errors unpredictable, must not fail request
            logger.warning("Failed to log container loot_all to audit log", error=str(e))

        return {
            "container": final_container.model_dump(),
            "player_inventory": player_inventory,
        }

    except ContainerNotFoundError as e:
        context = create_error_context(
            request, current_user, container_id=str(request_data.container_id), operation="loot_all"
        )
        raise LoggedHTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Container not found",
            context=context,
        ) from e

    except ContainerLockedError as e:
        context = create_error_context(
            request, current_user, container_id=str(request_data.container_id), operation="loot_all"
        )
        raise LoggedHTTPException(
            status_code=status.HTTP_423_LOCKED,
            detail="Container is locked",
            context=context,
        ) from e

    except ContainerAccessDeniedError as e:
        context = create_error_context(
            request, current_user, container_id=str(request_data.container_id), operation="loot_all"
        )
        raise LoggedHTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied",
            context=context,
        ) from e

    except ContainerCapacityError as e:
        context = create_error_context(
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
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Container operation errors unpredictable, must create error context
        context = create_error_context(
            request, current_user, container_id=str(request_data.container_id), operation="loot_all"
        )
        # Use error=str(e) instead of exc_info=True to avoid Unicode encoding issues on Windows
        logger.error("Unexpected error in loot-all", error=str(e), **context.to_dict())
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
            context=context,
        ) from e
