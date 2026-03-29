"""Get command: take items from a container or from the room floor."""

from __future__ import annotations

from dataclasses import dataclass
from typing import cast
from uuid import UUID

from structlog.stdlib import BoundLogger

from ..alias_storage import AliasStorage
from ..models.player import Player
from ..structured_logging.enhanced_logging_config import get_logger
from .container_helpers_inventory import (
    find_container_in_room,
    find_item_in_container,
    find_wearable_container,
    parse_container_items,
    resolve_container_id,
    transfer_item_from_container,
    validate_get_command_inputs,
)
from .inventory_command_coercion import coerce_int
from .inventory_command_contracts import CommandResponse, RoomDropManager
from .inventory_command_helpers import resolve_pickup_item_index, resolve_state_and_player
from .inventory_pickup_command import (
    FloorPickupAfterExtract,
    FloorPickupEnvironment,
    FloorPickupPayload,
    complete_pickup_after_floor_extract,
)

logger: BoundLogger = cast(BoundLogger, get_logger(__name__))


@dataclass(frozen=True)
class GetCommandRuntime:
    """Shared services and request for get-from-container / get-from-room routing."""

    persistence: object
    connection_manager: object
    request: object
    container_service: object
    room_manager: object


@dataclass(frozen=True)
class GetItemSpec:
    """Validated item/container/quantity from the get command."""

    player: Player
    item_name: str
    container_name: str
    quantity: object


async def _handle_get_from_room(
    persistence: object,
    connection_manager: object,
    player: Player,
    room_id: str,
    item_name: str,
    quantity: int | None,
    room_manager: object,
) -> CommandResponse:
    """Handle get-from-room (pickup from floor) path."""
    rm = cast(RoomDropManager, room_manager)
    player_id_uuid = UUID(str(player.player_id))
    drop_list = rm.list_room_drops(room_id)
    pickup_command_data: dict[str, object] = {"search_term": item_name, "quantity": quantity}
    resolved_index_zero, _, index_error = resolve_pickup_item_index(
        pickup_command_data, drop_list, player.name, player_id_uuid, room_id
    )
    if index_error:
        return index_error
    idx0 = resolved_index_zero
    if idx0 is None:
        return {"result": "Could not resolve item to get."}
    if quantity is None:
        qty = coerce_int(drop_list[idx0].get("quantity", 1), default=1)
    else:
        qty = quantity
    if qty <= 0:
        return {"result": "Quantity must be a positive number."}
    extracted_stack = rm.take_room_drop(room_id, idx0, qty)
    if not extracted_stack:
        return {"result": "That item is no longer available."}
    env = FloorPickupEnvironment(
        persistence=persistence,
        connection_manager=connection_manager,
        room_id=room_id,
        room_manager=rm,
    )
    payload = FloorPickupPayload(
        player=player,
        extracted_stack=extracted_stack,
        qty=qty,
        player_id_uuid=player_id_uuid,
        message_kind="get_from_room",
    )
    return await complete_pickup_after_floor_extract(FloorPickupAfterExtract(env=env, payload=payload))


def _container_transfer_messages(
    player_name: str,
    container_name: str,
    transfer_quantity: object,
    item_display_name: object,
) -> dict[str, str]:
    tq = transfer_quantity
    dn = item_display_name
    return {
        "result": f"You get {tq}x {dn} from {container_name}.",
        "room_message": f"{player_name} gets {tq}x {dn} from {container_name}.",
        "game_log_message": f"{player_name} got {tq}x {dn} from {container_name}",
    }


async def _get_transfer_out_of_container(
    container_service: object,
    persistence: object,
    player: Player,
    container_id: UUID,
    item_found: dict[str, object],
    quantity: object,
    container_name: str,
) -> CommandResponse:
    transfer_result = await transfer_item_from_container(
        container_service, persistence, player, container_id, item_found, quantity
    )

    if "error" in transfer_result:
        return {"result": transfer_result["error"]}

    if not transfer_result.get("success"):
        return {"result": "Error: Failed to transfer item."}

    transfer_quantity = transfer_result["transfer_quantity"]
    item_display_name = transfer_result["item_display_name"]

    texts = _container_transfer_messages(player.name, container_name, transfer_quantity, item_display_name)
    return {**texts, "game_log_channel": "game-log"}


async def _get_from_container_path(rt: GetCommandRuntime, spec: GetItemSpec) -> CommandResponse:
    """Resolve room container / wearable container and transfer into inventory."""
    room_id = str(spec.player.current_room_id)
    container_found, container_id = find_container_in_room(rt.room_manager, room_id, spec.container_name)

    if not container_found:
        container_found, container_id = await find_wearable_container(
            rt.persistence, rt.request, spec.player, spec.container_name
        )

    if not container_found:
        return {"result": f"You don't see any '{spec.container_name}' here."}

    container_items, container_id = parse_container_items(container_found, container_id, spec.player)
    if not container_items and container_id:
        return {"result": "Error: Invalid container data format."}

    item_found, _ = find_item_in_container(container_items, spec.item_name, spec.player, container_id)
    if not item_found:
        return {"result": f"You don't see '{spec.item_name}' in {spec.container_name}."}

    container_id = resolve_container_id(container_found, container_id)
    if not container_id:
        return {"result": "Error: Could not determine container ID."}

    return await _get_transfer_out_of_container(
        rt.container_service,
        rt.persistence,
        spec.player,
        container_id,
        item_found,
        spec.quantity,
        spec.container_name,
    )


async def _get_route_after_validation(rt: GetCommandRuntime, spec: GetItemSpec) -> CommandResponse:
    room_id = str(spec.player.current_room_id)
    if spec.container_name.lower() == "room":
        return await _handle_get_from_room(
            rt.persistence,
            rt.connection_manager,
            spec.player,
            room_id,
            spec.item_name,
            cast(int | None, spec.quantity),
            rt.room_manager,
        )
    return await _get_from_container_path(rt, spec)


async def handle_get_command(
    command_data: dict[str, object],
    current_user: dict[str, object],
    request: object,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> CommandResponse:
    """Get an item from a container into inventory."""

    persistence, connection_manager, player, error = await resolve_state_and_player(request, current_user, player_name)
    if error or not player:
        return error or {"result": "Player information not found."}

    validation_result = await validate_get_command_inputs(command_data, request, connection_manager)
    if isinstance(validation_result, dict):
        return validation_result

    item_name, container_name, quantity, container_service, room_manager = validation_result

    logger.debug(
        "Get command received",
        player=player.name,
        item_name=item_name,
        container_name=container_name,
        quantity=quantity,
    )

    return await _get_route_after_validation(
        GetCommandRuntime(
            persistence=persistence,
            connection_manager=connection_manager,
            request=request,
            container_service=container_service,
            room_manager=room_manager,
        ),
        GetItemSpec(player=player, item_name=item_name, container_name=container_name, quantity=quantity),
    )
