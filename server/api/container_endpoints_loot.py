"""
Container loot-all endpoint.

Handles the convenience action to transfer all eligible items from a container
to the player's inventory in a single operation (one player-registry unit of work, ADR-029).
"""

from __future__ import annotations

from typing import Any, cast

from fastapi import APIRouter, Depends, HTTPException, Request

from ..exceptions import LoggedHTTPException
from ..game.player_registry import PlayerRegistry
from ..models.container import ContainerComponent
from ..schemas.containers import ContainerLootAllResponse
from ..services.inventory_websocket_events import emit_inventory_snapshot
from ..structured_logging.enhanced_logging_config import get_logger
from .container_events import emit_loot_all_event
from .container_exception_handlers import handle_loot_all_exceptions
from .container_helpers import (
    apply_rate_limiting_for_loot_all,
    get_container_service,
    get_player_id_from_user,
    validate_user_for_loot_all,
)
from .container_models import LootAllRequest

logger = get_logger(__name__)


def _build_loot_all_response(
    final_container: ContainerComponent, player_inventory: list[dict[str, object]], items_looted: int
) -> ContainerLootAllResponse:
    from .container_endpoints_basic import (
        _convert_container_dict_to_container_data,
        _convert_inventory_list_to_inventory_stacks,
    )

    container_data = _convert_container_dict_to_container_data(final_container.model_dump())
    player_inventory_stacks = _convert_inventory_list_to_inventory_stacks(player_inventory)
    return ContainerLootAllResponse(
        container=container_data,
        player_inventory=player_inventory_stacks,
        items_looted=items_looted,
    )


async def loot_all_items(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: route handler forwards each of its injected dependencies
    request_data: LootAllRequest,
    request: Request,
    current_user: Any,
    persistence: Any,
    connection_manager: Any,
    player_registry: PlayerRegistry,
) -> ContainerLootAllResponse:
    """Loot all eligible items from a container."""
    validate_user_for_loot_all(current_user, request)
    apply_rate_limiting_for_loot_all(current_user, request)
    try:
        player_id = await get_player_id_from_user(current_user, persistence)
        container_service = get_container_service(persistence)
        result = await container_service.loot_all(
            request_data.container_id, player_id, request_data.mutation_token, registry=player_registry
        )
        # Inventory first, as for a single transfer: the client's transfer pane must not offer stale stacks.
        await emit_inventory_snapshot(
            cast(object, connection_manager), player_id, result.player_inventory, result.player_equipped
        )
        await emit_loot_all_event(connection_manager, request_data, result.container, player_id, result.items_looted)
        logger.info(
            "Loot-all completed",
            container_id=str(request_data.container_id),
            player_id=str(player_id),
            items_transferred=result.items_looted,
        )
        return _build_loot_all_response(result.container, result.player_inventory, result.items_looted)
    except LoggedHTTPException, HTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Container operation errors unpredictable, must create error context
        handle_loot_all_exceptions(e, request, current_user, request_data.container_id)
        raise AssertionError("handle_loot_all_exceptions should always raise") from e


def register_loot_endpoints(router: APIRouter) -> None:
    """Register loot-all endpoint to the router."""
    # Import here so this module does not top-level-import auth/deps (cycle via factory).
    from ..auth.users import get_current_user
    from ..dependencies import AsyncPersistenceDep, ConnectionManagerDep, get_player_registry
    from ..models.user import User

    async def _loot_all_route(
        request_data: LootAllRequest,
        request: Request,
        current_user: User = Depends(get_current_user),
        persistence: Any = AsyncPersistenceDep,
        connection_manager: Any = ConnectionManagerDep,
    ) -> ContainerLootAllResponse:
        # Not a Depends parameter: this module's annotations are strings, and FastAPI resolves them against module
        # globals, which never see this function's local imports.
        return await loot_all_items(
            request_data, request, current_user, persistence, connection_manager, get_player_registry(request)
        )

    router.post("/loot-all", response_model=ContainerLootAllResponse)(_loot_all_route)
