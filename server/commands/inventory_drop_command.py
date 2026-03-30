"""Drop command: move an inventory stack to the room floor."""

from __future__ import annotations

from copy import deepcopy
from typing import cast

from structlog.stdlib import BoundLogger

from ..alias_storage import AliasStorage
from ..models.player import Player
from ..structured_logging.enhanced_logging_config import get_logger
from .inventory_command_coercion import coerce_int
from .inventory_command_contracts import CommandResponse, RoomDropManager
from .inventory_command_helpers import (
    build_and_broadcast_inventory_event,
    clone_inventory,
    get_room_manager,
    persist_player,
    resolve_state_and_player,
)

logger: BoundLogger = cast(BoundLogger, get_logger(__name__))

_DropResolved = tuple[RoomDropManager, str, dict[str, object], int, list[dict[str, object]], int]


def _drop_quantity_or_error(
    command_data: dict[str, object], stack: dict[str, object]
) -> tuple[int | None, CommandResponse | None]:
    q_raw = command_data.get("quantity")
    if q_raw is None:
        return coerce_int(stack.get("quantity", 1), default=1), None
    if isinstance(q_raw, int):
        return q_raw, None
    try:
        q = coerce_int(q_raw, default=0)
    except (TypeError, ValueError):
        return None, {"result": "Quantity must be a positive number."}
    return q, None


def _inventory_rows_after_drop(
    previous_inventory: list[dict[str, object]], index: int, quantity: int, stack_qty: int
) -> list[dict[str, object]]:
    """Apply partial or full removal of one inventory slot (1-based index)."""
    if quantity == stack_qty:
        return previous_inventory[: index - 1] + previous_inventory[index:]
    updated_inventory = deepcopy(previous_inventory)
    updated_inventory[index - 1]["quantity"] = (
        coerce_int(previous_inventory[index - 1].get("quantity", 1), default=1) - quantity
    )
    return updated_inventory


def _drop_slot_index_or_error(command_data: dict[str, object], inventory_len: int) -> CommandResponse | int:
    """Resolve 1-based inventory slot from command data or return a usage / range error."""
    index = command_data.get("index")
    if not isinstance(index, int) or index < 1:
        return {"result": "Usage: drop <inventory-number> [quantity]"}
    if index > inventory_len:
        return {"result": "You do not have an item in that slot."}
    return index


def _drop_quantity_bounds_or_error(quantity: int, stack_qty: int) -> CommandResponse | None:
    """Return an error response if drop quantity is out of range for the stack."""
    if quantity <= 0:
        return {"result": "Quantity must be a positive number."}
    if quantity > stack_qty:
        return {"result": "You do not have that many to drop."}
    return None


def _drop_parsed_quantity_or_error(
    command_data: dict[str, object],
    stack: dict[str, object],
    player: Player,
) -> CommandResponse | int:
    """Parse quantity from command + stack; return error dict or a validated int (may still exceed stack)."""
    quantity, q_err = _drop_quantity_or_error(command_data, stack)
    if q_err:
        return q_err
    if quantity is None:
        logger.error(
            "drop quantity invariant failed after validation",
            player=player.name,
            player_id=str(player.player_id),
        )
        raise RuntimeError("drop quantity is None after _drop_quantity_or_error; internal error")
    return quantity


def _drop_resolve_stack_or_error(
    command_data: dict[str, object],
    connection_manager: object,
    player: Player,
) -> CommandResponse | _DropResolved:
    room_manager_raw, room_error = get_room_manager(connection_manager, player)
    if room_error:
        return room_error
    room_manager = cast(RoomDropManager, room_manager_raw)

    room_id = str(player.current_room_id)
    current_inventory = player.get_inventory()
    index_or_err = _drop_slot_index_or_error(command_data, len(current_inventory))
    if not isinstance(index_or_err, int):
        return index_or_err
    index = index_or_err

    stack = deepcopy(current_inventory[index - 1])
    quantity_or_err = _drop_parsed_quantity_or_error(command_data, stack, player)
    if not isinstance(quantity_or_err, int):
        return quantity_or_err
    quantity = quantity_or_err

    stack_qty = coerce_int(stack.get("quantity", 1), default=1)
    bounds_err = _drop_quantity_bounds_or_error(quantity, stack_qty)
    if bounds_err:
        return bounds_err

    previous_inventory = clone_inventory(player)
    return room_manager, room_id, stack, quantity, previous_inventory, index


async def _drop_finish_after_persist(
    connection_manager: object,
    player: Player,
    room_id: str,
    room_manager: RoomDropManager,
    drop_stack: dict[str, object],
    quantity: int,
) -> CommandResponse:
    room_manager.add_room_drop(room_id, drop_stack)

    item_name = str(drop_stack.get("item_name") or drop_stack.get("item_id", "item"))

    await build_and_broadcast_inventory_event(
        connection_manager,
        player,
        room_id,
        "inventory_drop",
        {
            "player_name": player.name,
            "item_id": drop_stack.get("item_id"),
            "item_name": item_name,
            "quantity": quantity,
        },
    )

    logger.info(
        "Item dropped",
        player=player.name,
        player_id=str(player.player_id),
        item_id=drop_stack.get("item_id"),
        quantity=quantity,
        room_id=room_id,
    )
    return {
        "result": f"You drop {quantity}x {item_name}.",
        "room_message": f"{player.name} drops {quantity}x {item_name}.",
        "game_log_message": f"{player.name} dropped {quantity}x {item_name}",
        "game_log_channel": "game-log",
    }


async def handle_drop_command(
    command_data: dict[str, object],
    current_user: dict[str, object],
    request: object,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> CommandResponse:
    """Drop an inventory stack into the current room."""

    persistence, connection_manager, player, error = await resolve_state_and_player(request, current_user, player_name)
    if error or not player:
        return error or {"result": "Player information not found."}

    resolved = _drop_resolve_stack_or_error(command_data, connection_manager, player)
    if not isinstance(resolved, tuple):
        return resolved

    room_manager, room_id, stack, quantity, previous_inventory, index = resolved
    stack_qty = coerce_int(stack.get("quantity", 1), default=1)

    updated_inventory = _inventory_rows_after_drop(previous_inventory, index, quantity, stack_qty)

    player.set_inventory(updated_inventory)

    drop_stack = deepcopy(stack)
    drop_stack["quantity"] = quantity

    persist_error = await persist_player(persistence, player)
    if persist_error:
        player.set_inventory(previous_inventory)
        return persist_error

    return await _drop_finish_after_persist(connection_manager, player, room_id, room_manager, drop_stack, quantity)
