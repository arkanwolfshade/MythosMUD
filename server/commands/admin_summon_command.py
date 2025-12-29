"""Administrative summon command implementation."""

from __future__ import annotations

from typing import Any

from ..alias_storage import AliasStorage
from ..commands.admin_commands import validate_admin_permission
from ..commands.inventory_commands import _broadcast_room_event, _resolve_player, _resolve_state
from ..exceptions import DatabaseError, ValidationError
from ..game.items.item_factory import ItemFactoryError
from ..monitoring.monitoring_dashboard import get_monitoring_dashboard
from ..realtime.envelope import build_event
from ..structured_logging.admin_actions_logger import get_admin_actions_logger
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


async def handle_summon_command(
    command_data: dict,
    current_user: dict,
    request: Any,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Handle the `/summon` administrative command."""

    persistence, connection_manager = _resolve_state(request)
    player, error = await _resolve_player(persistence, current_user, player_name)
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
    dashboard = get_monitoring_dashboard()

    player_name_value = player.name

    if not item_factory or not prototype_registry:
        logger.warning("Summon command unavailable - item services missing")
        admin_logger.log_admin_command(
            admin_name=player_name_value,
            command="summon",
            success=False,
            error_message="Item services unavailable",
            additional_data={
                "source": "admin_summon",
                "summoned_by": player_name_value,
            },
        )
        return {"result": "The summoning matrix is offline. Try again once prototype services are restored."}

    if not room_manager or not hasattr(room_manager, "add_room_drop"):
        logger.warning("Summon command unavailable - room manager missing", player=player_name_value)
        admin_logger.log_admin_command(
            admin_name=player_name_value,
            command="summon",
            success=False,
            error_message="Room inventory unavailable",
            additional_data={
                "source": "admin_summon",
                "summoned_by": player_name_value,
            },
        )
        return {"result": "Room inventory is unavailable; the ritual cannot anchor the summoned item."}

    prototype_id = command_data.get("prototype_id")
    quantity = int(command_data.get("quantity", 1))
    target_type = command_data.get("target_type", "item")
    room_id = str(player.current_room_id)

    if quantity >= int(dashboard.alert_thresholds.get("summon_quantity_warning", 5)):
        dashboard.record_summon_quantity_spike(
            admin_name=player_name_value,
            prototype_id=prototype_id,
            quantity=quantity,
            metadata={"room_id": room_id, "target_type": target_type},
        )

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
            additional_data={
                "prototype_id": prototype_id,
                "target_type": target_type,
                "quantity": quantity,
                "source": "admin_summon",
                "summoned_by": player_name_value,
                "room_id": room_id,
            },
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
            additional_data={
                "prototype_id": prototype_id,
                "target_type": target_type,
                "quantity": quantity,
                "source": "admin_summon",
                "summoned_by": player_name_value,
                "room_id": room_id,
            },
        )
        return {"result": f"Summoning failed: {exc}"}

    stack = item_instance.to_inventory_stack()
    stack.setdefault("origin", {}).update({"source": "admin_summon", "summoned_by": player_name_value})
    stack["quantity"] = quantity

    # Persist the item instance to the database to ensure referential integrity
    # This is required for container operations and other systems that reference item_instances
    try:
        persistence.create_item_instance(
            item_instance_id=item_instance.item_instance_id,
            prototype_id=item_instance.prototype_id,
            owner_type="room",
            owner_id=room_id,
            quantity=quantity,
            metadata=item_instance.metadata,
            origin_source="admin_summon",
            origin_metadata={"summoned_by": player_name_value},
        )
        logger.debug(
            "Item instance persisted for summoned item",
            item_instance_id=item_instance.item_instance_id,
            prototype_id=item_instance.prototype_id,
            room_id=room_id,
        )
    except (DatabaseError, ValidationError) as e:
        logger.error(
            "Failed to persist item instance for summoned item",
            item_instance_id=item_instance.item_instance_id,
            prototype_id=item_instance.prototype_id,
            error=str(e),
        )
        # Continue anyway - the item will still be added to room drops
        # but container operations may fail if the item instance doesn't exist

    room_manager.add_room_drop(room_id, stack)

    item_name = stack.get("item_name") or stack.get("item_id", "item")
    event = build_event(
        "admin_summon",
        {
            "player_name": player_name_value,
            "item_id": stack.get("item_id"),
            "item_name": item_name,
            "quantity": quantity,
            "summoned_by": player_name_value,
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
            "source": "admin_summon",
            "summoned_by": player_name_value,
            "target_type": target_type,
        },
    )

    logger.info(
        "Admin summoned item",
        player=player_name_value,
        prototype_id=prototype_id,
        quantity=quantity,
        room_id=room_id,
        summoned_by=player_name_value,
        target_type=target_type,
    )

    return {"result": f"You summon {quantity}x {item_name} into {room_id}."}
