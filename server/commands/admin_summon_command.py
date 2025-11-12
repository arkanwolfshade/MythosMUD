"""Administrative summon command implementation."""

from __future__ import annotations

from typing import Any, cast

from ..alias_storage import AliasStorage
from ..commands.admin_commands import validate_admin_permission
from ..commands.inventory_commands import _broadcast_room_event, _resolve_player, _resolve_state
from ..game.items.item_factory import ItemFactoryError
from ..logging.admin_actions_logger import get_admin_actions_logger
from ..logging.enhanced_logging_config import get_logger
from ..realtime.envelope import build_event

logger = get_logger(__name__)


async def handle_summon_command(
    command_data: dict,
    current_user: dict,
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Handle the `/summon` administrative command."""

    persistence, connection_manager = _resolve_state(request)
    player, error = _resolve_player(persistence, current_user, player_name)
    if error or not player:
        return error or {"result": "Player information not found."}

    if not await validate_admin_permission(player, player_name):
        return {
            "result": (
                "The Restricted Archives remain sealed. You do not currently possess the "
                "necessary administrative clearance to perform that ritual."
            )
        }

    state = getattr(getattr(request, "app", None), "state", None)
    item_factory = getattr(state, "item_factory", None)
    prototype_registry = getattr(state, "prototype_registry", None)
    room_manager = getattr(connection_manager, "room_manager", None)
    admin_logger = get_admin_actions_logger()

    player_name_value = cast(str, player.name)

    if not item_factory or not prototype_registry:
        logger.warning("Summon command unavailable - item services missing")
        admin_logger.log_admin_command(
            admin_name=player_name_value,
            command="summon",
            success=False,
            error_message="Item services unavailable",
        )
        return {"result": "The summoning matrix is offline. Try again once prototype services are restored."}

    if not room_manager or not hasattr(room_manager, "add_room_drop"):
        logger.warning("Summon command unavailable - room manager missing", player=player_name_value)
        admin_logger.log_admin_command(
            admin_name=player_name_value,
            command="summon",
            success=False,
            error_message="Room inventory unavailable",
        )
        return {"result": "Room inventory is unavailable; the ritual cannot anchor the summoned item."}

    prototype_id = command_data.get("prototype_id")
    quantity = int(command_data.get("quantity", 1))
    target_type = command_data.get("target_type", "item")
    room_id = str(player.current_room_id)

    if target_type == "npc":
        message = (
            "NPC summoning is not yet bound to this ritual circle. "
            "Please use the `npc spawn` command while we finish tuning the containment wards."
        )
        admin_logger.log_admin_command(
        admin_name=player_name_value,
            command="summon",
            success=False,
            error_message="NPC summon stub invoked",
            additional_data={"prototype_id": prototype_id, "target_type": target_type},
        )
        return {"result": message}

    try:
        item_instance = item_factory.create_instance(
            prototype_id,
            quantity=quantity,
            origin={"source": "admin_summon", "summoned_by": player_name_value},
        )
    except ItemFactoryError as exc:
        logger.warning(
            "Admin summon failed during item creation",
            player=player_name_value,
            prototype_id=prototype_id,
            error=str(exc),
        )
        admin_logger.log_admin_command(
            admin_name=player_name_value,
            command="summon",
            success=False,
            error_message=str(exc),
            additional_data={"prototype_id": prototype_id, "target_type": target_type},
        )
        return {"result": f"Summoning failed: {exc}"}

    stack = item_instance.to_inventory_stack()
    stack.setdefault("origin", {}).update({"source": "admin_summon", "summoned_by": player_name_value})
    stack["quantity"] = quantity

    room_manager.add_room_drop(room_id, stack)

    item_name = stack.get("item_name") or stack.get("item_id", "item")
    event = build_event(
        "admin_summon",
        {
            "player_name": player_name_value,
            "item_id": stack.get("item_id"),
            "item_name": item_name,
            "quantity": quantity,
        },
        room_id=room_id,
        player_id=str(getattr(player, "player_id", "")),
        connection_manager=connection_manager,
    )

    await _broadcast_room_event(
        connection_manager,
        room_id,
        event,
        exclude_player=str(getattr(player, "player_id", "")) if getattr(player, "player_id", None) else None,
    )

    admin_logger.log_admin_command(
        admin_name=player_name_value,
        command="summon",
        success=True,
        additional_data={
            "prototype_id": prototype_id,
            "quantity": quantity,
            "room_id": room_id,
        },
    )

    logger.info(
        "Admin summoned item",
        player=player_name_value,
        prototype_id=prototype_id,
        quantity=quantity,
        room_id=room_id,
    )

    return {"result": f"You summon {quantity}x {item_name} into {room_id}."}
