"""Put command: move inventory items into a container."""

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
    find_wearable_container_for_put,
    resolve_container_id,
    transfer_item_to_container,
    validate_put_command_inputs,
)
from .inventory_command_contracts import CommandResponse
from .inventory_command_helpers import persist_player, remove_item_from_inventory, resolve_state_and_player

logger: BoundLogger = cast(BoundLogger, get_logger(__name__))


@dataclass(frozen=True)
class PutCommandRuntime:
    """Services and request scope for put-after-validation."""

    persistence: object
    request: object
    container_service: object
    room_manager: object


@dataclass(frozen=True)
class PutValidatedWork:
    """Validated inventory item and command fields for put."""

    command_data: dict[str, object]
    player: Player
    item_name: str
    container_name: str
    quantity: object
    item_found: dict[str, object]
    item_index: int


async def _put_resolve_container_id(
    persistence: object,
    request: object,
    player: Player,
    room_manager: object,
    room_id: str,
    container_name: str,
) -> tuple[UUID | None, CommandResponse | None]:
    """Locate a room or wearable container id, or return an error response."""
    container_found, cid = find_container_in_room(room_manager, room_id, container_name)

    if not container_found:
        container_found, cid = await find_wearable_container_for_put(persistence, request, player, container_name)

    if not container_found:
        logger.debug("Container not found for put command", container_name=container_name, player=player.name)
        return None, {"result": f"You don't see any '{container_name}' here."}

    resolved = resolve_container_id(container_found, cid)
    if not resolved:
        logger.error(
            "Container found but container_id is None for put command",
            container_name=container_name,
            player=player.name,
        )
        return None, {"result": f"Error: Container '{container_name}' has no valid ID."}
    return resolved, None


async def _put_transfer_finish(
    container_service: object,
    persistence: object,
    player: Player,
    container_id: UUID,
    item_found: dict[str, object],
    item_index: int,
    quantity: object,
    container_name: str,
) -> CommandResponse:
    transfer_result = await transfer_item_to_container(
        container_service, persistence, player, container_id, item_found, quantity
    )

    if "error" in transfer_result:
        return {"result": transfer_result["error"]}

    if not transfer_result.get("success"):
        return {"result": "Error: Failed to transfer item."}

    transfer_quantity = cast(int, transfer_result["transfer_quantity"])
    remove_item_from_inventory(player, item_index, transfer_quantity)
    persist_error = await persist_player(persistence, player)
    if persist_error:
        return persist_error

    item_display_name = item_found.get("item_name") or item_found.get("item_id", "item")
    return {
        "result": f"You put {transfer_quantity}x {item_display_name} into {container_name}.",
        "room_message": f"{player.name} puts {transfer_quantity}x {item_display_name} into {container_name}.",
        "game_log_message": f"{player.name} put {transfer_quantity}x {item_display_name} into {container_name}",
        "game_log_channel": "game-log",
    }


async def _put_run_validated(rt: PutCommandRuntime, work: PutValidatedWork) -> CommandResponse:
    logger.debug(
        "Put command received",
        player=work.player.name,
        command_data_keys=list(work.command_data.keys()),
        item_name=work.item_name,
        container_name=work.container_name,
        quantity=work.quantity,
    )
    logger.debug(
        "Item found for put command",
        item_name=work.item_name,
        item_found=work.item_found.get("item_name"),
        player=work.player.name,
    )

    room_id = str(work.player.current_room_id)
    container_id, cid_error = await _put_resolve_container_id(
        rt.persistence, rt.request, work.player, rt.room_manager, room_id, work.container_name
    )
    if cid_error:
        return cid_error
    if container_id is None:
        logger.error(
            "put container_id invariant failed after resolution",
            player=work.player.name,
            player_id=str(work.player.player_id),
            container_name=work.container_name,
        )
        raise RuntimeError("container_id is None after _put_resolve_container_id; internal error")

    return await _put_transfer_finish(
        rt.container_service,
        rt.persistence,
        work.player,
        container_id,
        work.item_found,
        work.item_index,
        work.quantity,
        work.container_name,
    )


async def handle_put_command(
    command_data: dict[str, object],
    current_user: dict[str, object],
    request: object,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> CommandResponse:
    """Put an item from inventory into a container."""

    persistence, connection_manager, player, error = await resolve_state_and_player(request, current_user, player_name)
    if error or not player:
        return error or {"result": "Player information not found."}

    validation_result = await validate_put_command_inputs(command_data, request, connection_manager, player)
    if isinstance(validation_result, dict):
        return validation_result

    item_name, container_name, quantity, container_service, room_manager, item_found, item_index = validation_result
    item_found_valid = cast(dict[str, object], item_found)
    item_index_valid = cast(int, item_index)

    put_rt = PutCommandRuntime(
        persistence=persistence,
        request=request,
        container_service=container_service,
        room_manager=room_manager,
    )
    put_work = PutValidatedWork(
        command_data=command_data,
        player=player,
        item_name=item_name,
        container_name=container_name,
        quantity=quantity,
        item_found=item_found_valid,
        item_index=item_index_valid,
    )
    return await _put_run_validated(rt=put_rt, work=put_work)
