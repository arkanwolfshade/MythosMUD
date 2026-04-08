"""Pickup command: move a stack from room drops into inventory."""

from __future__ import annotations

from dataclasses import dataclass
from typing import cast
from uuid import UUID

from structlog.stdlib import BoundLogger

from ..alias_storage import AliasStorage
from ..models.player import Player
from ..services.inventory_service import InventoryService
from ..structured_logging.enhanced_logging_config import get_logger
from .inventory_command_coercion import coerce_int
from .inventory_command_contracts import CommandResponse, RoomDropManager
from .inventory_command_helpers import (
    add_pickup_to_inventory,
    build_and_broadcast_inventory_event,
    clone_inventory,
    ensure_item_instance_for_pickup,
    get_room_manager,
    persist_player,
    prepare_extracted_stack,
    resolve_pickup_item_index,
    resolve_state_and_player,
)

logger: BoundLogger = get_logger(__name__)

_FloorPickupResolved = tuple[RoomDropManager, str, dict[str, object], int, UUID]


@dataclass(frozen=True)
class FloorPickupEnvironment:
    """Room-side context after a floor extract (persistence, drops, room id)."""

    persistence: object
    connection_manager: object
    room_id: str
    room_manager: RoomDropManager


@dataclass(frozen=True)
class FloorPickupPayload:
    """Player and stack data for completing a floor pickup."""

    player: Player
    extracted_stack: dict[str, object]
    qty: int
    player_id_uuid: UUID
    message_kind: str = "pickup"


@dataclass(init=False)
class FloorPickupAfterExtract:
    """Arguments for completing a floor pickup (keeps Lizard parameter count low)."""

    persistence: object
    connection_manager: object
    player: Player
    room_id: str
    room_manager: RoomDropManager
    extracted_stack: dict[str, object]
    qty: int
    player_id_uuid: UUID
    message_kind: str

    def __init__(self, env: FloorPickupEnvironment, payload: FloorPickupPayload) -> None:
        self.persistence = env.persistence
        self.connection_manager = env.connection_manager
        self.room_id = env.room_id
        self.room_manager = env.room_manager
        self.player = payload.player
        self.extracted_stack = payload.extracted_stack
        self.qty = payload.qty
        self.player_id_uuid = payload.player_id_uuid
        self.message_kind = payload.message_kind


def _pickup_quantity_or_error(
    command_data: dict[str, object], drop_list: list[dict[str, object]], idx0: int
) -> tuple[int | None, CommandResponse | None]:
    qty_raw = command_data.get("quantity")
    if qty_raw is None:
        return coerce_int(drop_list[idx0].get("quantity", 1), default=1), None
    if isinstance(qty_raw, int):
        return qty_raw, None
    try:
        qty = coerce_int(qty_raw, default=0)
    except (TypeError, ValueError):
        return None, {"result": "Quantity must be a positive number."}
    return qty, None


def _pickup_result_messages(player_name: str, quantity: object, item_name: object, *, kind: str) -> dict[str, str]:
    """Build result / room / game-log strings (pickup vs get-from-room wording)."""
    q = quantity
    n = item_name
    if kind == "get_from_room":
        return {
            "result": f"You get {q}x {n}.",
            "room_message": f"{player_name} gets {q}x {n}.",
            "game_log_message": f"{player_name} got {q}x {n}",
        }
    return {
        "result": f"You pick up {q}x {n}.",
        "room_message": f"{player_name} picks up {q}x {n}.",
        "game_log_message": f"{player_name} picked up {q}x {n}",
    }


def _pickup_resolve_floor_stack_or_error(
    command_data: dict[str, object],
    connection_manager: object,
    player: Player,
) -> CommandResponse | _FloorPickupResolved:
    room_manager_raw, room_error = get_room_manager(connection_manager, player)
    if room_error:
        return room_error
    room_manager = cast(RoomDropManager, room_manager_raw)

    room_id = str(player.current_room_id)
    drop_list = room_manager.list_room_drops(room_id)

    player_id_uuid = UUID(str(player.player_id))
    resolved_index_zero, _, index_error = resolve_pickup_item_index(
        command_data, drop_list, player.name, player_id_uuid, room_id
    )
    if index_error:
        return index_error

    idx0 = resolved_index_zero
    if idx0 is None:
        return {"result": "Could not resolve item to pick up."}

    qty, qty_error = _pickup_quantity_or_error(command_data, drop_list, idx0)
    if qty_error:
        return qty_error
    if qty is None:
        logger.error(
            "pickup quantity invariant failed after validation",
            player=player.name,
            player_id=str(player.player_id),
        )
        raise RuntimeError("pickup quantity is None after _pickup_quantity_or_error; internal error")

    if qty <= 0:
        return {"result": "Quantity must be a positive number."}

    extracted_stack = room_manager.take_room_drop(room_id, idx0, qty)
    if not extracted_stack:
        return {"result": "That item is no longer available."}

    return room_manager, room_id, extracted_stack, qty, player_id_uuid


async def _pickup_commit_inventory_after_floor_extract(
    persistence: object,
    player: Player,
    room_id: str,
    room_manager: RoomDropManager,
    extracted_stack: dict[str, object],
    player_id_uuid: UUID,
) -> tuple[CommandResponse | None, dict[str, object] | None]:
    """Apply stack to player inventory and persist. Returns (error, None) or (None, prepared_stack)."""
    prepared_stack = prepare_extracted_stack(extracted_stack, player.name, player_id_uuid)

    await ensure_item_instance_for_pickup(persistence, prepared_stack, player, room_id)

    previous_inventory = clone_inventory(player)

    inventory_service = InventoryService()
    updated_inventory, inventory_error = await add_pickup_to_inventory(
        inventory_service, player, prepared_stack, room_manager, room_id
    )
    if inventory_error:
        return inventory_error, None

    if updated_inventory is None:
        return {"result": "Failed to update inventory."}, None
    player.set_inventory(updated_inventory)
    logger.info(
        "Pickup: inventory after set_inventory",
        player=player.name,
        player_id=str(player.player_id),
        inventory_length=len(updated_inventory),
    )
    persist_error = await persist_player(persistence, player)
    if persist_error:
        room_manager.add_room_drop(room_id, prepared_stack)
        player.set_inventory(previous_inventory)
        return persist_error, None
    return None, prepared_stack


async def _pickup_broadcast_success(
    connection_manager: object,
    player: Player,
    room_id: str,
    extracted_stack: dict[str, object],
    qty: int,
    *,
    message_kind: str,
) -> CommandResponse:
    quantity = extracted_stack.get("quantity", qty)
    item_name = extracted_stack.get("item_name") or extracted_stack.get("item_id", "item")

    await build_and_broadcast_inventory_event(
        connection_manager,
        player,
        room_id,
        "inventory_pickup",
        {
            "player_name": player.name,
            "item_id": extracted_stack.get("item_id"),
            "item_name": item_name,
            "quantity": quantity,
        },
    )

    logger.info(
        "Item picked up",
        player=player.name,
        player_id=str(player.player_id),
        item_id=extracted_stack.get("item_id"),
        quantity=quantity,
        room_id=room_id,
    )
    texts = _pickup_result_messages(player.name, quantity, item_name, kind=message_kind)
    return {**texts, "game_log_channel": "game-log"}


async def complete_pickup_after_floor_extract(ctx: FloorPickupAfterExtract) -> CommandResponse:
    """Persist pickup, broadcast, and build player-facing messages."""
    commit_err, prepared_stack = await _pickup_commit_inventory_after_floor_extract(
        ctx.persistence,
        ctx.player,
        ctx.room_id,
        ctx.room_manager,
        ctx.extracted_stack,
        ctx.player_id_uuid,
    )
    if commit_err:
        return commit_err
    # commit_err is None only when prepared_stack is present by contract.
    prepared_stack = cast(dict[str, object], prepared_stack)
    return await _pickup_broadcast_success(
        ctx.connection_manager,
        ctx.player,
        ctx.room_id,
        prepared_stack,
        ctx.qty,
        message_kind=ctx.message_kind,
    )


async def handle_pickup_command(
    command_data: dict[str, object],
    current_user: dict[str, object],
    request: object,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> CommandResponse:
    """Move an item stack from room drops into the player's inventory."""

    persistence, connection_manager, player, error = await resolve_state_and_player(request, current_user, player_name)
    if error or not player:
        return error or {"result": "Player information not found."}

    resolved = _pickup_resolve_floor_stack_or_error(command_data, connection_manager, player)
    if not isinstance(resolved, tuple):
        return resolved

    room_manager, room_id, extracted_stack, qty, player_id_uuid = resolved

    logger.debug("Pickup: extracted_stack before processing", player=player.name, player_id=str(player.player_id))

    return await complete_pickup_after_floor_extract(
        FloorPickupAfterExtract(
            FloorPickupEnvironment(
                persistence=persistence,
                connection_manager=connection_manager,
                room_id=room_id,
                room_manager=room_manager,
            ),
            FloorPickupPayload(
                player=player,
                extracted_stack=extracted_stack,
                qty=qty,
                player_id_uuid=player_id_uuid,
            ),
        )
    )
