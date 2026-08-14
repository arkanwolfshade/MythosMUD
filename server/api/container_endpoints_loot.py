"""
Container loot-all endpoint.

Handles the convenience action to transfer all eligible items from a container
to the player's inventory in a single operation.
"""

from __future__ import annotations

from typing import Any, cast

from fastapi import APIRouter, Depends, HTTPException, Request

from ..exceptions import LoggedHTTPException
from ..models.container import ContainerComponent
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

logger = get_logger(__name__)


async def _audit_loot_all(
    player_id: Any, player: Any, request_data: LootAllRequest, final_container: Any, items_looted: int
) -> None:
    try:
        audit_logger.log_container_interaction(
            player_id=str(player_id),
            player_name=str(player.name),
            container_id=str(request_data.container_id),
            event_type="container_loot_all",
            source_type=str(final_container.source_type.value),
            room_id=str(final_container.room_id),
            items_count=items_looted,
            success=True,
        )
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Audit log errors unpredictable, must not fail request
        logger.warning("Failed to log container loot_all to audit log", error=str(e))


def _build_loot_all_response(
    final_container: Any, player_inventory: Any, items_looted: int
) -> ContainerLootAllResponse:
    from .container_endpoints_basic import (
        _convert_container_dict_to_container_data,
        _convert_inventory_list_to_inventory_stacks,
    )

    container_data = _convert_container_dict_to_container_data(final_container.model_dump())
    player_inventory_stacks = _convert_inventory_list_to_inventory_stacks(cast(list[dict[str, Any]], player_inventory))
    return ContainerLootAllResponse(
        container=container_data,
        player_inventory=player_inventory_stacks,
        items_looted=items_looted,
    )


async def loot_all_items(
    request_data: LootAllRequest,
    request: Request,
    current_user: Any,
    persistence: Any,
    connection_manager: Any,
) -> ContainerLootAllResponse:
    """Loot all eligible items from a container."""
    validate_user_for_loot_all(current_user, request)
    apply_rate_limiting_for_loot_all(current_user, request)
    try:
        player_id = await get_player_id_from_user(current_user, persistence)
        container_service = get_container_service(persistence)
        container, player, player_inventory = await get_container_and_player_for_loot_all(
            persistence, request_data, player_id, request, current_user
        )
        _, player_inventory = await transfer_all_items_from_container(
            container_service, request_data, player_id, container, player_inventory
        )
        final_container_data = await persistence.get_container(request_data.container_id)
        final_container = ContainerComponent.model_validate(final_container_data) if final_container_data else container
        await emit_loot_all_event(connection_manager, request_data, final_container, player_id, container)
        items_looted = len(container.items) - len(final_container.items)
        logger.info(
            "Loot-all completed",
            container_id=str(request_data.container_id),
            player_id=str(player_id),
            items_transferred=items_looted,
        )
        await _audit_loot_all(player_id, player, request_data, final_container, items_looted)
        return _build_loot_all_response(final_container, player_inventory, items_looted)
    except (LoggedHTTPException, HTTPException):
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Container operation errors unpredictable, must create error context
        handle_loot_all_exceptions(e, request, current_user, request_data.container_id)
        raise AssertionError("handle_loot_all_exceptions should always raise") from e


def register_loot_endpoints(router: APIRouter) -> None:
    """Register loot-all endpoint to the router."""
    # Import here so this module does not top-level-import auth/deps (cycle via factory).
    from ..auth.users import get_current_user
    from ..dependencies import AsyncPersistenceDep, ConnectionManagerDep
    from ..models.user import User

    async def _loot_all_route(
        request_data: LootAllRequest,
        request: Request,
        current_user: User = Depends(get_current_user),
        persistence: Any = AsyncPersistenceDep,
        connection_manager: Any = ConnectionManagerDep,
    ) -> ContainerLootAllResponse:
        return await loot_all_items(request_data, request, current_user, persistence, connection_manager)

    router.post("/loot-all", response_model=ContainerLootAllResponse)(_loot_all_route)
