"""Use command: consume one item from an inventory stack and apply its effect (#870)."""

from __future__ import annotations

from typing import cast
from uuid import UUID

from structlog.stdlib import BoundLogger

from ..alias_storage import AliasStorage
from ..game.items.item_effects import ItemEffectHandler, ItemUseContext, find_effect
from ..game.items.models import ItemPrototypeModel
from ..models.player import Player
from ..services.inventory_websocket_events import emit_inventory_updated
from ..structured_logging.enhanced_logging_config import get_logger
from .equipment_helpers import resolve_equip_item_index
from .inventory_command_contracts import CommandResponse
from .inventory_command_helpers import (
    clone_inventory,
    persist_player,
    remove_item_from_inventory,
    resolve_state_and_player,
)
from .inventory_command_prototype import prototype_from_registry, prototype_registry_from_request

logger: BoundLogger = get_logger(__name__)

CONSUMABLE_ITEM_TYPE = "consumable"

_UsableItem = tuple[int, ItemPrototypeModel, ItemEffectHandler]


def _consumable_prototype(request: object, stack: dict[str, object]) -> ItemPrototypeModel | None:
    """Prototype of the stack's item, or None when it can't be resolved."""
    prototype_id = stack.get("prototype_id") or stack.get("item_id")
    registry = prototype_registry_from_request(request)
    if registry is None or not isinstance(prototype_id, str):
        return None
    prototype = prototype_from_registry(registry, prototype_id)
    return prototype if isinstance(prototype, ItemPrototypeModel) else None


def _resolve_usable_or_error(
    request: object, command_data: dict[str, object], player: Player, room_id: str
) -> CommandResponse | _UsableItem:
    """Resolve the item to use: its 0-based inventory index, prototype and effect handler, or an error reply."""
    resolved_index, stack_or_error = resolve_equip_item_index(command_data, player.get_inventory(), player, room_id)
    if resolved_index is None or stack_or_error is None:
        return stack_or_error or {"result": "You do not have that item."}

    prototype = _consumable_prototype(request, stack_or_error)
    if prototype is None or prototype.item_type != CONSUMABLE_ITEM_TYPE:
        return {"result": "You can't use that."}
    effect = find_effect(prototype)
    if effect is None:
        logger.warning("Consumable has no registered effect", prototype_id=prototype.prototype_id)
        return {"result": "Nothing happens."}
    return resolved_index, prototype, effect


async def _spend_one(
    persistence: object,
    connection_manager: object,
    player: Player,
    inventory_index: int,
    prototype: ItemPrototypeModel,
) -> None:
    """Remove one of the item after its effect happened; a failed save puts it back (the effect stands)."""
    player_id = UUID(str(player.player_id))
    previous_inventory = clone_inventory(player)
    remove_item_from_inventory(player, inventory_index, 1)
    persist_error = await persist_player(persistence, player)
    if persist_error:
        player.set_inventory(previous_inventory)
        logger.error(
            "Consumable effect applied but inventory decrement failed to persist",
            player_id=str(player_id),
            prototype_id=prototype.prototype_id,
        )
        return
    await emit_inventory_updated(connection_manager, player_id, player)


async def handle_use_command(
    command_data: dict[str, object],
    current_user: dict[str, object],
    request: object,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> CommandResponse:
    """Use (drink, quaff) one consumable from inventory; the item is spent only if its effect happens."""

    persistence, connection_manager, player, error = await resolve_state_and_player(request, current_user, player_name)
    if error or not player:
        return error or {"result": "Player information not found."}

    room_id = str(player.current_room_id)
    usable = _resolve_usable_or_error(request, command_data, player, room_id)
    if not isinstance(usable, tuple):
        return usable
    inventory_index, prototype, effect = usable

    player_id = UUID(str(player.player_id))
    outcome = await effect(
        ItemUseContext(
            app=cast(object, getattr(request, "app", None)), player_id=player_id, room_id=room_id, prototype=prototype
        )
    )
    if not outcome.ok:
        return {"result": outcome.message}

    await _spend_one(persistence, connection_manager, player, inventory_index, prototype)

    item_name = prototype.name.lower()
    logger.info("Item used", player=player.name, player_id=str(player_id), prototype_id=prototype.prototype_id)
    return {
        "result": outcome.message,
        "room_message": f"{player.name} drinks a {item_name}.",
        "game_log_message": f"{player.name} used {item_name}",
        "game_log_channel": "game-log",
    }
