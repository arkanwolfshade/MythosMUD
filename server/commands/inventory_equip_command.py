"""Equip command: move an item from inventory to an equipment slot."""

from __future__ import annotations

import uuid
from collections.abc import Mapping
from copy import deepcopy
from dataclasses import dataclass
from typing import cast

from structlog.stdlib import BoundLogger

from ..alias_storage import AliasStorage
from ..models.player import Player
from ..services.equipment_service import EquipmentCapacityError, EquipmentService, SlotValidationError
from ..services.inventory_service import InventoryCapacityError, InventoryService, InventoryStack
from ..structured_logging.enhanced_logging_config import get_logger
from .equipment_helpers import (
    find_equipped_item_after_equip,
    handle_wearable_container_on_equip,
    normalize_equipped_items,
    normalize_inventory_slots,
    resolve_equip_item_index,
)
from .inventory_command_contracts import CommandResponse
from .inventory_command_helpers import (
    build_and_broadcast_inventory_event,
    clone_inventory,
    persist_player,
    resolve_state_and_player,
)
from .inventory_command_prototype import infer_equip_slot_from_prototype
from .inventory_item_matching import normalize_slot_name
from .inventory_service_helpers import get_shared_services

logger: BoundLogger = get_logger(__name__)


@dataclass
class EquipCommandRuntime:
    """Request-scoped services and player for equip."""

    persistence: object
    connection_manager: object
    player: Player
    room_id: str
    inventory_service: InventoryService
    equipment_service: EquipmentService
    mutation_token: str | None
    command_data: dict[str, object]


@dataclass
class EquipCommandInventoryStep:
    """Inventory indices, slot choice, and rollback snapshot for equip."""

    inventory: list[dict[str, object]]
    resolved_index_zero: int
    selected_stack: dict[str, object] | None
    target_slot: str | None
    previous_inventory: list[dict[str, object]]
    previous_equipped: dict[str, Mapping[str, object]]


@dataclass(init=False)
class EquipCommandWork:
    """Bundled state for equip mutation (keeps handler and Lizard-friendly)."""

    persistence: object
    connection_manager: object
    player: Player
    inventory: list[dict[str, object]]
    resolved_index_zero: int
    selected_stack: dict[str, object] | None
    target_slot: str | None
    room_id: str
    inventory_service: InventoryService
    equipment_service: EquipmentService
    mutation_token: str | None
    command_data: dict[str, object]
    previous_inventory: list[dict[str, object]]
    previous_equipped: dict[str, Mapping[str, object]]

    def __init__(self, runtime: EquipCommandRuntime, inv_step: EquipCommandInventoryStep) -> None:
        self.persistence = runtime.persistence
        self.connection_manager = runtime.connection_manager
        self.player = runtime.player
        self.room_id = runtime.room_id
        self.inventory_service = runtime.inventory_service
        self.equipment_service = runtime.equipment_service
        self.mutation_token = runtime.mutation_token
        self.command_data = runtime.command_data
        self.inventory = inv_step.inventory
        self.resolved_index_zero = inv_step.resolved_index_zero
        self.selected_stack = inv_step.selected_stack
        self.target_slot = inv_step.target_slot
        self.previous_inventory = inv_step.previous_inventory
        self.previous_equipped = inv_step.previous_equipped


def _equip_target_slot_or_error(
    request: object,
    selected_stack: dict[str, object] | None,
    target_slot: str | None,
) -> tuple[str | None, CommandResponse | None]:
    if target_slot is not None:
        return target_slot, None
    if selected_stack is None:
        return None, None
    inferred = infer_equip_slot_from_prototype(request, selected_stack)
    if inferred:
        return inferred, None
    if selected_stack.get("slot_type") == "inventory":
        return None, {
            "result": ("Specify which slot to equip to (e.g. equip 1 main_hand or equip switchblade main_hand)."),
        }
    return None, None


async def _equip_persist_or_rollback(
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


def _equip_try_inventory_swap(
    work: EquipCommandWork,
) -> CommandResponse | tuple[object, object]:
    equipped_for_service = cast(
        Mapping[str, Mapping[str, object]],
        work.player.get_equipped_items(),
    )
    try:
        new_inventory, new_equipped = work.equipment_service.equip_from_inventory(
            work.inventory,
            equipped_for_service,
            slot_index=work.resolved_index_zero,
            target_slot=work.target_slot,
        )
        return (new_inventory, new_equipped)
    except (SlotValidationError, EquipmentCapacityError, InventoryCapacityError) as exc:
        logger.info(
            "Equip rejected",
            player=work.player.name,
            player_id=work.player.player_id,
            reason=str(exc),
            requested_slot=work.target_slot,
            inventory_index=work.command_data.get("index"),
            room_id=work.room_id,
        )
        return {"result": str(exc)}


async def _equip_run_mutation(work: EquipCommandWork) -> CommandResponse | None:
    player = work.player
    player_id_for_mutation: uuid.UUID | str = str(player.player_id)
    with work.inventory_service.begin_mutation(player_id_for_mutation, work.mutation_token) as decision:
        if not decision.should_apply:
            logger.info(
                "Equip suppressed by mutation guard",
                player=player.name,
                player_id=player.player_id,
                requested_slot=work.target_slot,
                inventory_index=work.command_data.get("index"),
                room_id=work.room_id,
                mutation_token=work.mutation_token,
            )
            return {"result": "That action is already being processed."}

        swap = _equip_try_inventory_swap(work)
        if isinstance(swap, dict):
            return swap
        new_inventory_raw, new_equipped_raw = swap
        new_inventory = cast(list[dict[str, object]], new_inventory_raw)
        new_equipped = cast(dict[str, InventoryStack], new_equipped_raw)

        normalize_inventory_slots(new_inventory)
        normalized_equipped = normalize_equipped_items(new_equipped)

        player.set_inventory(new_inventory)
        player.set_equipped_items(normalized_equipped)

        rollback = await _equip_persist_or_rollback(
            work.persistence, player, work.previous_inventory, work.previous_equipped
        )
        if rollback:
            return rollback
    return None


async def _equip_success_payload(
    request: object,
    connection_manager: object,
    player: Player,
    room_id: str,
    target_slot: str | None,
    selected_stack: dict[str, object],
    mutation_token: str | None,
) -> CommandResponse:
    equipped_mapping = player.get_equipped_items()
    equipped_slot, equipped_item = find_equipped_item_after_equip(target_slot, selected_stack, equipped_mapping)

    await handle_wearable_container_on_equip(request, player, equipped_item)

    item_payload: dict[str, object] = dict(equipped_item) if equipped_item is not None else {}

    item_name = str(item_payload.get("item_name") or item_payload.get("item_id", "item"))

    await build_and_broadcast_inventory_event(
        connection_manager,
        player,
        room_id,
        "inventory_equip",
        {
            "player_name": player.name,
            "item_id": item_payload.get("item_id"),
            "item_name": item_name,
            "slot": equipped_slot,
        },
    )

    logger.info(
        "Item equipped",
        player=player.name,
        player_id=str(player.player_id),
        item_id=item_payload.get("item_id"),
        slot=equipped_slot,
        room_id=room_id,
        mutation_token=mutation_token,
    )
    return {
        "result": f"You equip {item_name}.",
        "room_message": f"{player.name} equips {item_name}.",
        "game_log_message": f"{player.name} equipped {item_name}",
        "game_log_channel": "game-log",
    }


def _equip_inventory_rollback_snapshot(
    player: Player,
) -> tuple[list[dict[str, object]], dict[str, Mapping[str, object]]]:
    return clone_inventory(player), cast(dict[str, Mapping[str, object]], deepcopy(player.get_equipped_items()))


async def _equip_build_work(
    command_data: dict[str, object],
    current_user: dict[str, object],
    request: object,
    player_name: str,
) -> CommandResponse | EquipCommandWork:
    persistence, connection_manager, player, error = await resolve_state_and_player(request, current_user, player_name)
    if error or not player:
        return error or {"result": "Player information not found."}

    inventory = player.get_inventory()
    normalize_inventory_slots(inventory)

    room_id = str(player.current_room_id)
    target_slot = normalize_slot_name(cast(str | None, command_data.get("target_slot")))

    resolved_index_zero, error_or_stack = resolve_equip_item_index(command_data, inventory, player, room_id)
    if resolved_index_zero is None:
        return error_or_stack or {"result": "Failed to resolve item index."}
    selected_stack = error_or_stack

    slot_or_err = _equip_target_slot_or_error(request, selected_stack, target_slot)
    target_slot, slot_error = slot_or_err
    if slot_error:
        return slot_error

    inventory_service, _, equipment_service = get_shared_services(request)
    mutation_token = cast(str | None, command_data.get("mutation_token"))

    previous_inventory, previous_equipped = _equip_inventory_rollback_snapshot(player)

    runtime = EquipCommandRuntime(
        persistence=persistence,
        connection_manager=connection_manager,
        player=player,
        room_id=room_id,
        inventory_service=inventory_service,
        equipment_service=equipment_service,
        mutation_token=mutation_token,
        command_data=command_data,
    )
    inv_step = EquipCommandInventoryStep(
        inventory=inventory,
        resolved_index_zero=resolved_index_zero,
        selected_stack=selected_stack,
        target_slot=target_slot,
        previous_inventory=previous_inventory,
        previous_equipped=previous_equipped,
    )
    return EquipCommandWork(runtime=runtime, inv_step=inv_step)


async def handle_equip_command(
    command_data: dict[str, object],
    current_user: dict[str, object],
    request: object,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> CommandResponse:
    """Equip an item from inventory."""

    work = await _equip_build_work(command_data, current_user, request, player_name)
    if not isinstance(work, EquipCommandWork):
        return work

    mutation_error = await _equip_run_mutation(work)
    if mutation_error:
        return mutation_error

    if work.selected_stack is None:
        return {"result": "Selected item is invalid."}
    return await _equip_success_payload(
        request,
        work.connection_manager,
        work.player,
        work.room_id,
        work.target_slot,
        work.selected_stack,
        work.mutation_token,
    )
