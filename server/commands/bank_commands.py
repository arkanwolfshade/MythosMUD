"""
Bank commands: bank, deposit, withdraw (#977).

All three act on the player's own deposit box at a bank room (rooms.attributes.bank = true). Only
that gate lives here; who may open the box is enforced by the container service (owner-only), and
the item moves reuse the put/get transfer helpers.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import cast
from uuid import UUID

from structlog.stdlib import BoundLogger

from ..alias_storage import AliasStorage
from ..models.player import Player
from ..models.room import Room
from ..services.bank_service import BANK_BOX_CAPACITY, BankBoxPersistence, get_or_create_bank_box, is_bank_room
from ..services.inventory_websocket_events import emit_inventory_updated
from ..structured_logging.enhanced_logging_config import get_logger
from .container_helpers_inventory import (
    find_item_in_container,
    parse_container_items,
    transfer_item_from_container,
    transfer_item_to_container,
    validate_get_command_inputs,
    validate_put_command_inputs,
)
from .inventory_command_contracts import CommandResponse
from .inventory_command_helpers import persist_player, remove_item_from_inventory, resolve_state_and_player

logger: BoundLogger = get_logger(__name__)

BANK_NAME = "Arkham Savings & Trust"
# The put/get validators want a container name; the box is the only one a bank command can mean.
_BOX_NAME = "deposit box"


@dataclass(frozen=True)
class _BankVisit:
    """A player standing in a bank, with their deposit box resolved."""

    persistence: object
    connection_manager: object
    player: Player
    box: dict[str, object]

    @property
    def box_id(self) -> UUID:
        """Container id of the deposit box."""
        return UUID(str(self.box["container_id"]))


async def _enter_bank(
    request: object, current_user: dict[str, object], player_name: str
) -> _BankVisit | CommandResponse:
    """Resolve the player, check they are in a bank room, and get (or create) their box."""
    persistence, connection_manager, player, error = await resolve_state_and_player(request, current_user, player_name)
    if error or not player:
        return error or {"result": "Player information not found."}
    get_room = getattr(persistence, "get_room_by_id", None)
    room = cast(Room | None, get_room(str(player.current_room_id))) if callable(get_room) else None
    if not is_bank_room(room):
        return {"result": "You must be at a bank to do that."}
    box = await get_or_create_bank_box(cast(BankBoxPersistence, persistence), UUID(str(player.player_id)))
    return _BankVisit(persistence, connection_manager, player, box)


def _display_name(item: dict[str, object]) -> object:
    return item.get("item_name") or item.get("item_id", "item")


async def handle_bank_command(
    _command_data: dict[str, object],
    current_user: dict[str, object],
    request: object,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> CommandResponse:
    """List what is in the player's deposit box."""
    visit = await _enter_bank(request, current_user, player_name)
    if not isinstance(visit, _BankVisit):
        return visit
    items, _ = parse_container_items(visit.box, visit.box_id, visit.player)
    if not items:
        return {"result": f"Your deposit box at {BANK_NAME} is empty."}
    capacity = cast(int, visit.box.get("capacity_slots") or BANK_BOX_CAPACITY)
    lines = [f"Your deposit box at {BANK_NAME} ({len(items)}/{capacity}):"]
    lines.extend(
        f"  {number}. {item.get('quantity', 1)}x {_display_name(item)}" for number, item in enumerate(items, 1)
    )
    return {"result": "\n".join(lines)}


async def handle_deposit_command(
    command_data: dict[str, object],
    current_user: dict[str, object],
    request: object,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> CommandResponse:
    """Deposit an inventory item into the player's deposit box."""
    visit = await _enter_bank(request, current_user, player_name)
    if not isinstance(visit, _BankVisit):
        return visit
    inputs = await validate_put_command_inputs(
        {**command_data, "container": _BOX_NAME}, visit.connection_manager, visit.player, visit.persistence
    )
    if isinstance(inputs, dict):
        return inputs
    _, _, quantity, container_service, _, item_found, item_index = inputs
    item = cast(dict[str, object], item_found)

    transfer = await transfer_item_to_container(
        container_service, visit.persistence, visit.player, visit.box_id, item, quantity
    )
    if "error" in transfer:
        return {"result": str(transfer["error"])}
    if not transfer.get("success"):
        return {"result": "Error: Failed to transfer item."}

    deposited = cast(int, transfer["transfer_quantity"])
    remove_item_from_inventory(visit.player, item_index, deposited)
    persist_error = await persist_player(visit.persistence, visit.player)
    if persist_error:
        return persist_error
    await emit_inventory_updated(visit.connection_manager, UUID(str(visit.player.player_id)), visit.player)
    return {
        "result": f"The clerk files {deposited}x {_display_name(item)} away in your deposit box.",
        "game_log_message": f"{visit.player.name} deposited {deposited}x {_display_name(item)} at {BANK_NAME}",
        "game_log_channel": "game-log",
    }


async def handle_withdraw_command(
    command_data: dict[str, object],
    current_user: dict[str, object],
    request: object,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> CommandResponse:
    """Withdraw an item from the player's deposit box into their inventory."""
    visit = await _enter_bank(request, current_user, player_name)
    if not isinstance(visit, _BankVisit):
        return visit
    inputs = await validate_get_command_inputs(
        {**command_data, "container": _BOX_NAME}, visit.connection_manager, visit.persistence
    )
    if isinstance(inputs, dict):
        return inputs
    item_name, _, quantity, container_service, _ = inputs

    items, _ = parse_container_items(visit.box, visit.box_id, visit.player)
    item, _ = find_item_in_container(items, item_name, visit.player, visit.box_id)
    if not item:
        return {"result": f"You don't have '{item_name}' in your deposit box."}

    transfer = await transfer_item_from_container(
        container_service, visit.persistence, visit.player, visit.box_id, item, quantity
    )
    if "error" in transfer:
        return {"result": str(transfer["error"])}
    if not transfer.get("success"):
        return {"result": "Error: Failed to transfer item."}

    await emit_inventory_updated(visit.connection_manager, UUID(str(visit.player.player_id)), visit.player)
    withdrawn = transfer["transfer_quantity"]
    return {
        "result": f"The clerk returns {withdrawn}x {transfer['item_display_name']} from your deposit box.",
        "game_log_message": f"{visit.player.name} withdrew {withdrawn}x {transfer['item_display_name']} at {BANK_NAME}",
        "game_log_channel": "game-log",
    }
