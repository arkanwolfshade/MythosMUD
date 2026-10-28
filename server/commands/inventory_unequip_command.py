"""Unequip command: move an equipped item back to inventory."""

from __future__ import annotations

import uuid
from collections.abc import Mapping
from copy import deepcopy
from typing import cast

from structlog.stdlib import BoundLogger

from ..alias_storage import AliasStorage
from ..models.player import Player
from ..services.equipment_service import EquipmentCapacityError, EquipmentService, SlotValidationError
from ..services.inventory_service import InventoryCapacityError, InventoryService
from ..services.inventory_websocket_events import emit_inventory_updated
from ..structured_logging.enhanced_logging_config import get_logger
from .command_results import command_error
from .equipment_helpers import (
    handle_wearable_container_on_unequip,
    normalize_equipped_items,
    normalize_inventory_slots,
    resolve_unequip_slot,
)
from .inventory_command_contracts import CommandResponse
from .inventory_command_helpers import (
    build_and_broadcast_inventory_event,
    change_inventory,
    resolve_state_and_player,
)
from .inventory_service_helpers import get_shared_services

logger: BoundLogger = get_logger(__name__)


def _unequip_apply(
    equipment_service: EquipmentService, player: Player, command_data: dict[str, object]
) -> CommandResponse | tuple[str, dict[str, object]]:
    """Resolve the slot in the player's (live) equipped stacks and move its stack back to the carried ones.

    Returns an error reply, or the slot and the stack that left it.
    """
    equipped = player.get_equipped_items()
    resolved_slot, error_result = resolve_unequip_slot(command_data, equipped)
    if resolved_slot is None:
        return error_result or command_error("Failed to resolve slot.")
    slot_stack = equipped.get(resolved_slot)
    unequipped_item: dict[str, object] = (
        deepcopy(cast(dict[str, object], slot_stack)) if isinstance(slot_stack, dict) else {}
    )
    try:
        new_inventory, new_equipped = equipment_service.unequip_to_inventory(
            player.get_inventory(),
            cast(Mapping[str, Mapping[str, object]], equipped),
            slot_type=resolved_slot,
        )
    except (SlotValidationError, EquipmentCapacityError, InventoryCapacityError) as exc:
        logger.info(
            "Unequip rejected",
            player=player.name,
            player_id=player.player_id,
            reason=str(exc),
            slot=resolved_slot,
            room_id=str(player.current_room_id),
        )
        return {"result": str(exc)}

    normalize_inventory_slots(cast(list[dict[str, object]], new_inventory))
    player.set_inventory(new_inventory)
    player.set_equipped_items(normalize_equipped_items(new_equipped))
    return resolved_slot, unequipped_item


async def _unequip_run_mutation(
    inventory_service: InventoryService,
    equipment_service: EquipmentService,
    player: Player,
    command_data: dict[str, object],
    mutation_token: str | None,
) -> CommandResponse | tuple[str, dict[str, object]]:
    """Under the mutation guard and the player's registry lock: unequip against the live inventory and commit."""
    unequipped: list[tuple[str, dict[str, object]]] = []

    async def unequip() -> CommandResponse | None:
        applied = _unequip_apply(equipment_service, player, command_data)
        if not isinstance(applied, tuple):
            return applied
        unequipped.append(applied)
        return None

    async with inventory_service.begin_mutation(str(player.player_id), mutation_token) as decision:
        if not decision.should_apply:
            logger.info(
                "Unequip suppressed by mutation guard",
                player=player.name,
                player_id=player.player_id,
                room_id=str(player.current_room_id),
                mutation_token=mutation_token,
            )
            return {"result": "That action is already being processed."}
        change_error = await change_inventory(player, unequip)
    if change_error:
        return change_error
    return unequipped[0] if unequipped else command_error("Failed to resolve slot.")


async def _unequip_success_payload(
    request: object,
    connection_manager: object,
    player: Player,
    resolved_slot: str,
    unequipped_item: dict[str, object],
    mutation_token: str | None,
) -> CommandResponse:
    await handle_wearable_container_on_unequip(request, player, unequipped_item)

    item_name = unequipped_item.get("item_name") or unequipped_item.get("item_id", "item")
    room_id = str(player.current_room_id)

    await emit_inventory_updated(connection_manager, uuid.UUID(str(player.player_id)), player)
    await build_and_broadcast_inventory_event(
        connection_manager,
        player,
        room_id,
        "inventory_unequip",
        {
            "player_name": player.name,
            "item_id": unequipped_item.get("item_id"),
            "item_name": item_name,
            "slot": resolved_slot,
        },
    )

    logger.info(
        "Item unequipped",
        player=player.name,
        player_id=str(player.player_id),
        slot=resolved_slot,
        item_id=unequipped_item.get("item_id"),
        room_id=room_id,
        mutation_token=mutation_token,
    )
    return {
        "result": f"You remove {item_name} from {resolved_slot}.",
        "room_message": f"{player.name} removes {item_name} from {resolved_slot}.",
        "game_log_message": f"{player.name} unequipped {item_name} from {resolved_slot}",
        "game_log_channel": "game-log",
    }


async def handle_unequip_command(
    command_data: dict[str, object],
    current_user: dict[str, object],
    request: object,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> CommandResponse:
    """Unequip an item into the player's inventory."""

    _persistence, connection_manager, player, error = await resolve_state_and_player(request, current_user, player_name)
    if error or not player:
        return error or command_error("Player information not found.")

    inventory_service, _, equipment_service = get_shared_services(request)
    mutation_token = cast(str | None, command_data.get("mutation_token"))

    outcome = await _unequip_run_mutation(inventory_service, equipment_service, player, command_data, mutation_token)
    if not isinstance(outcome, tuple):
        return outcome
    resolved_slot, unequipped_item = outcome

    return await _unequip_success_payload(
        request,
        connection_manager,
        player,
        resolved_slot,
        unequipped_item,
        mutation_token,
    )
