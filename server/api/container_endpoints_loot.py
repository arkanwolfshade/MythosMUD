"""
Container loot-all endpoint.

Handles the convenience action to transfer all eligible items from a container
to the player's inventory in a single operation.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, cast

from fastapi import APIRouter, Depends, HTTPException, Request

from ..auth.users import get_current_user
from ..dependencies import AsyncPersistenceDep, ConnectionManagerDep
from ..exceptions import LoggedHTTPException
from ..models.container import ContainerComponent
from ..models.user import User
from ..schemas.containers import ContainerLootAllResponse
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.audit_logger import audit_logger
from .container_events import emit_loot_all_event
from .container_exception_handlers import handle_loot_all_exceptions
from .container_helpers import (
    apply_rate_limiting_for_loot_all,
    get_container_and_player_for_loot_all,
    get_container_service,
    get_player_id_from_user,
    transfer_all_items_from_container,
    validate_user_for_loot_all,
)
from .container_models import LootAllRequest

if TYPE_CHECKING:
    from ..async_persistence import AsyncPersistenceLayer
    from ..realtime.connection_manager import ConnectionManager

logger = get_logger(__name__)


async def loot_all_items(
    request_data: LootAllRequest,
    request: Request,
    current_user: User = Depends(get_current_user),
    persistence: AsyncPersistenceLayer = AsyncPersistenceDep,
    connection_manager: ConnectionManager = ConnectionManagerDep,
) -> ContainerLootAllResponse:
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
        # Get player_id from user
        player_id = await get_player_id_from_user(current_user, persistence)

        # Get container service
        container_service = get_container_service(persistence)

        # Get container and player data
        container, player, player_inventory = await get_container_and_player_for_loot_all(
            persistence, request_data, player_id, request, current_user
        )

        # Transfer all items from container to player
        _, player_inventory = await transfer_all_items_from_container(
            container_service, request_data, player_id, container, player_inventory
        )

        # Get final container state
        final_container_data = await persistence.get_container(request_data.container_id)
        if final_container_data:
            final_container = ContainerComponent.model_validate(final_container_data)
        else:
            final_container = container

        # Emit WebSocket event for container update
        await emit_loot_all_event(connection_manager, request_data, final_container, player_id, container)

        items_looted = len(container.items) - len(final_container.items)

        logger.info(
            "Loot-all completed",
            container_id=str(request_data.container_id),
            player_id=str(player_id),
            items_transferred=items_looted,
        )

        # Audit log container loot_all
        try:
            audit_logger.log_container_interaction(
                player_id=str(player_id),
                player_name=str(player.name),
                container_id=str(request_data.container_id),
                event_type="container_loot_all",
                source_type=final_container.source_type.value,
                room_id=final_container.room_id,
                items_count=items_looted,
                success=True,
            )
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Audit log errors unpredictable, must not fail request
            logger.warning("Failed to log container loot_all to audit log", error=str(e))

        # Convert container and inventory dicts to models
        from .container_endpoints_basic import (
            _convert_container_dict_to_container_data,
            _convert_inventory_list_to_inventory_stacks,
        )

        container_data = _convert_container_dict_to_container_data(final_container.model_dump())
        # Cast: inventory_service.InventoryStack (TypedDict) is dict at runtime; conversion expects list[dict]
        player_inventory_stacks = _convert_inventory_list_to_inventory_stacks(
            cast(list[dict[str, Any]], player_inventory)
        )

        return ContainerLootAllResponse(
            container=container_data,
            player_inventory=player_inventory_stacks,
            items_looted=items_looted,
        )

    except (LoggedHTTPException, HTTPException):
        # Re-raise HTTP exceptions (including LoggedHTTPException) to let FastAPI handle them
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Container operation errors unpredictable, must create error context
        handle_loot_all_exceptions(e, request, current_user, request_data.container_id)
        raise AssertionError(
            "handle_loot_all_exceptions should always raise"
        ) from e  # Reason: Exception handler always raises, but mypy needs explicit return path


def register_loot_endpoints(router: APIRouter) -> None:
    """Register loot-all endpoint to the router."""
    router.post("/loot-all", response_model=ContainerLootAllResponse)(loot_all_items)
