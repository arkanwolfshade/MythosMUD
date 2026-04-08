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
from ..structured_logging.enhanced_logging_config import get_logger
from .equipment_helpers import (
    handle_wearable_container_on_unequip,
    normalize_equipped_items,
    normalize_inventory_slots,
    resolve_unequip_slot,
)
from .inventory_command_contracts import CommandResponse
from .inventory_command_helpers import (
    build_and_broadcast_inventory_event,
    clone_inventory,
    persist_player,
    resolve_state_and_player,
)
from .inventory_service_helpers import get_shared_services

logger: BoundLogger = get_logger(__name__)


async def _unequip_persist_or_rollback(
    persistence: object,
    player: Player,
    previous_inventory: list[dict[str, object]],
    previous_equipped: Mapping[str, Mapping[str, object]],
) -> CommandResponse | None:
    persist_error = await persist_player(persistence, player)
    if persist_error:
        player.set_inventory(previous_inventory)
        player.set_equipped_items(previous_equipped)
        return persist_error
    return None


async def _unequip_run_mutation(
    inventory_service: InventoryService,
    equipment_service: EquipmentService,
    persistence: object,
    player: Player,
    resolved_slot: str,
    mutation_token: str | None,
    previous_inventory: list[dict[str, object]],
    previous_equipped: Mapping[str, Mapping[str, object]],
) -> CommandResponse | None:
    player_id_for_mutation: uuid.UUID | str = str(player.player_id)
    with inventory_service.begin_mutation(player_id_for_mutation, mutation_token) as decision:
        if not decision.should_apply:
            logger.info(
                "Unequip suppressed by mutation guard",
                player=player.name,
                player_id=player.player_id,
                slot=resolved_slot,
                room_id=str(player.current_room_id),
                mutation_token=mutation_token,
            )
            return {"result": "That action is already being processed."}

        equipped_for_service = cast(
            Mapping[str, Mapping[str, object]],
            player.get_equipped_items(),
        )
        try:
            new_inventory, new_equipped = equipment_service.unequip_to_inventory(
                player.get_inventory(),
                equipped_for_service,
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
        normalized_equipped = normalize_equipped_items(new_equipped)

        player.set_inventory(new_inventory)
        player.set_equipped_items(normalized_equipped)

        rollback = await _unequip_persist_or_rollback(persistence, player, previous_inventory, previous_equipped)
        if rollback:
            return rollback
    return None


async def _unequip_success_payload(
    request: object,
    connection_manager: object,
    player: Player,
    persistence: object,
    resolved_slot: str,
    previous_equipped: Mapping[str, Mapping[str, object]],
    mutation_token: str | None,
) -> CommandResponse:
    unequipped_item = cast(dict[str, object], previous_equipped.get(resolved_slot) or {})
    await handle_wearable_container_on_unequip(request, player, unequipped_item, persistence)

    item_name = unequipped_item.get("item_name") or unequipped_item.get("item_id", "item")
    room_id = str(player.current_room_id)

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

    persistence, connection_manager, player, error = await resolve_state_and_player(request, current_user, player_name)
    if error or not player:
        return error or {"result": "Player information not found."}

    equipped_mapping = player.get_equipped_items()
    resolved_slot, error_result = resolve_unequip_slot(command_data, equipped_mapping)
    if resolved_slot is None:
        return error_result or {"result": "Failed to resolve slot."}

    inventory_service, _, equipment_service = get_shared_services(request)
    mutation_token = cast(str | None, command_data.get("mutation_token"))

    previous_inventory = clone_inventory(player)
    previous_equipped = cast(
        dict[str, Mapping[str, object]],
        deepcopy(player.get_equipped_items()),
    )

    mutation_error = await _unequip_run_mutation(
        inventory_service,
        equipment_service,
        persistence,
        player,
        resolved_slot,
        mutation_token,
        previous_inventory,
        previous_equipped,
    )
    if mutation_error:
        return mutation_error

    return await _unequip_success_payload(
        request,
        connection_manager,
        player,
        persistence,
        resolved_slot,
        previous_equipped,
        mutation_token,
    )
