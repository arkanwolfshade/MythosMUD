"""Inventory and equipment command handlers for MythosMUD.

Heavy handlers live in sibling modules to satisfy Lizard file/method limits; this package
re-exports the public API expected by command_service and tests.
"""

from __future__ import annotations

from copy import deepcopy
from typing import cast

from structlog.stdlib import BoundLogger

from ..alias_storage import AliasStorage
from ..structured_logging.enhanced_logging_config import get_logger
from .container_helpers_inventory import get_container_data_for_inventory, update_equipped_with_container_info
from .inventory_command_contracts import CommandResponse
from .inventory_command_helpers import resolve_state_and_player
from .inventory_display_helpers import render_inventory
from .inventory_drop_command import handle_drop_command
from .inventory_equip_command import handle_equip_command
from .inventory_get_command import handle_get_command
from .inventory_pickup_command import handle_pickup_command
from .inventory_put_command import handle_put_command
from .inventory_unequip_command import handle_unequip_command

logger: BoundLogger = get_logger(__name__)

__all__ = [
    "CommandResponse",
    "handle_drop_command",
    "handle_equip_command",
    "handle_get_command",
    "handle_inventory_command",
    "handle_pickup_command",
    "handle_put_command",
    "handle_unequip_command",
]


async def handle_inventory_command(
    _command_data: dict[str, object],  # pylint: disable=unused-argument  # Command data not used
    current_user: dict[str, object],
    request: object,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> CommandResponse:
    """Display the player's inventory and equipped items, including container contents."""

    _persistence, _connection_manager, player, error = await resolve_state_and_player(
        request, current_user, player_name
    )
    if error or not player:
        return error or {"result": "Player information not found."}

    inventory_view = player.get_inventory()
    equipped_view = player.get_equipped_items()
    equipped_for_containers = cast(dict[str, dict[str, object]], equipped_view)

    container_contents, container_capacities, container_lock_states = await get_container_data_for_inventory(
        request, player, equipped_for_containers
    )

    update_equipped_with_container_info(
        equipped_for_containers, container_contents, container_capacities, container_lock_states
    )

    logger.info(
        "Inventory displayed",
        player=player.name,
        slots_used=len(inventory_view),
        equipped_slots=len(equipped_view),
        containers_with_items=len(container_contents),
    )
    return {
        "result": render_inventory(
            inventory_view, equipped_view, container_contents, container_capacities, container_lock_states
        ),
        "inventory": deepcopy(inventory_view),
        "equipped": deepcopy(equipped_view),
    }
