"""Equip command: move an item from inventory to an equipment slot."""

from __future__ import annotations

import uuid
from collections.abc import Mapping
from dataclasses import dataclass
from typing import cast

from structlog.stdlib import BoundLogger

from ..alias_storage import AliasStorage
from ..models.player import Player
from ..services.equipment_service import EquipmentCapacityError, EquipmentService, SlotValidationError
from ..services.inventory_service import InventoryCapacityError, InventoryService, InventoryStack
from ..services.inventory_websocket_events import emit_inventory_updated
from ..structured_logging.enhanced_logging_config import get_logger
from .command_results import command_error
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
    change_inventory,
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
    """Inventory indices and slot choice for equip, resolved against the live inventory."""

    inventory: list[dict[str, object]]
    resolved_index_zero: int
    selected_stack: dict[str, object] | None
    target_slot: str | None


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


def _equip_apply_swap(work: EquipCommandWork) -> CommandResponse | None:
    """Move the stack into its slot on the player's working copy; change_inventory commits it."""
    swap = _equip_try_inventory_swap(work)
    if isinstance(swap, dict):
        return swap
    new_inventory_raw, new_equipped_raw = swap
    new_inventory = cast(list[dict[str, object]], new_inventory_raw)
    new_equipped = cast(dict[str, InventoryStack], new_equipped_raw)

    normalize_inventory_slots(new_inventory)
    work.player.set_inventory(new_inventory)
    work.player.set_equipped_items(normalize_equipped_items(new_equipped))
    return None


async def _equip_run_mutation(
    request: object, command_data: dict[str, object], runtime: EquipCommandRuntime
) -> CommandResponse | EquipCommandWork:
    """Under the mutation guard and the player's registry lock: resolve the item in the live inventory, swap, commit."""
    player = runtime.player
    work: list[EquipCommandWork] = []

    async def equip() -> CommandResponse | None:
        built = _equip_resolve_work(request, command_data, runtime)
        if not isinstance(built, EquipCommandWork):
            return built
        work.append(built)
        return _equip_apply_swap(built)

    async with runtime.inventory_service.begin_mutation(str(player.player_id), runtime.mutation_token) as decision:
        if not decision.should_apply:
            logger.info(
                "Equip suppressed by mutation guard",
                player=player.name,
                player_id=player.player_id,
                inventory_index=command_data.get("index"),
                room_id=runtime.room_id,
                mutation_token=runtime.mutation_token,
            )
            return {"result": "That action is already being processed."}
        change_error = await change_inventory(player, equip)
    if change_error:
        return change_error
    return work[0] if work else command_error("Failed to resolve item index.")


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

    await emit_inventory_updated(connection_manager, uuid.UUID(str(player.player_id)), player)
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


async def _equip_build_runtime(
    command_data: dict[str, object],
    current_user: dict[str, object],
    request: object,
    player_name: str,
) -> CommandResponse | EquipCommandRuntime:
    persistence, connection_manager, player, error = await resolve_state_and_player(request, current_user, player_name)
    if error or not player:
        return error or command_error("Player information not found.")

    inventory_service, _, equipment_service = get_shared_services(request)
    return EquipCommandRuntime(
        persistence=persistence,
        connection_manager=connection_manager,
        player=player,
        room_id=str(player.current_room_id),
        inventory_service=inventory_service,
        equipment_service=equipment_service,
        mutation_token=cast(str | None, command_data.get("mutation_token")),
        command_data=command_data,
    )


def _equip_resolve_work(
    request: object, command_data: dict[str, object], runtime: EquipCommandRuntime
) -> CommandResponse | EquipCommandWork:
    """Find the stack and its slot in the player's (live) inventory."""
    inventory = runtime.player.get_inventory()
    normalize_inventory_slots(inventory)

    target_slot = normalize_slot_name(cast(str | None, command_data.get("target_slot")))
    resolved_index_zero, error_or_stack = resolve_equip_item_index(
        command_data, inventory, runtime.player, runtime.room_id
    )
    if resolved_index_zero is None:
        return error_or_stack or command_error("Failed to resolve item index.")
    selected_stack = error_or_stack

    target_slot, slot_error = _equip_target_slot_or_error(request, selected_stack, target_slot)
    if slot_error:
        return slot_error

    inv_step = EquipCommandInventoryStep(
        inventory=inventory,
        resolved_index_zero=resolved_index_zero,
        selected_stack=selected_stack,
        target_slot=target_slot,
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

    runtime = await _equip_build_runtime(command_data, current_user, request, player_name)
    if not isinstance(runtime, EquipCommandRuntime):
        return runtime

    work = await _equip_run_mutation(request, command_data, runtime)
    if not isinstance(work, EquipCommandWork):
        return work

    if work.selected_stack is None:
        return command_error("Selected item is invalid.")
    return await _equip_success_payload(
        request,
        work.connection_manager,
        work.player,
        work.room_id,
        work.target_slot,
        work.selected_stack,
        work.mutation_token,
    )
