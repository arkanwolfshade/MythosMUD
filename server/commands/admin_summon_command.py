"""Administrative summon command implementation."""

# pylint: disable=too-many-locals,too-many-return-statements  # Reason: Command handlers require many intermediate variables for complex game logic and multiple return statements for early validation returns

from __future__ import annotations

from typing import Any

from ..alias_storage import AliasStorage
from ..commands.admin_permission_utils import validate_admin_permission
from ..commands.inventory_command_helpers import broadcast_room_event, resolve_player, resolve_state
from ..exceptions import DatabaseError, ValidationError
from ..game.items.item_factory import ItemFactoryError
from ..monitoring.monitoring_dashboard import get_monitoring_dashboard
from ..realtime.envelope import build_event
from ..structured_logging.admin_actions_logger import get_admin_actions_logger
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


def _validate_summon_prerequisites(
    state: Any,
    connection_manager: Any,
    player_name_value: str,
    admin_logger: Any,
) -> dict[str, str] | None:
    """Return an error result dict if item services or room manager are missing; otherwise None."""
    item_factory = getattr(state, "item_factory", None)
    prototype_registry = getattr(state, "prototype_registry", None)
    if not item_factory or not prototype_registry:
        logger.warning("Summon command unavailable - item services missing")
        admin_logger.log_admin_command(
            admin_name=player_name_value,
            command="summon",
            success=False,
            error_message="Item services unavailable",
            additional_data={"source": "admin_summon", "summoned_by": player_name_value},
        )
        return {"result": "The summoning matrix is offline. Try again once prototype services are restored."}
    room_manager = getattr(connection_manager, "room_manager", None)
    if not room_manager or not hasattr(room_manager, "add_room_drop"):
        logger.warning("Summon command unavailable - room manager missing", player=player_name_value)
        admin_logger.log_admin_command(
            admin_name=player_name_value,
            command="summon",
            success=False,
            error_message="Room inventory unavailable",
            additional_data={"source": "admin_summon", "summoned_by": player_name_value},
        )
        return {"result": "Room inventory is unavailable; the ritual cannot anchor the summoned item."}
    return None


def _summon_npc_stub_response(
    prototype_id: str,
    target_type: str,
    quantity: int,
    room_id: str,
    player_name_value: str,
    admin_logger: Any,
) -> dict[str, str] | None:
    """If target_type is 'npc', log and return stub message; otherwise return None."""
    if target_type != "npc":
        return None
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


def _create_summon_item_instance(
    item_factory: Any,
    prototype_id: str,
    quantity: int,
    player_name_value: str,
    admin_logger: Any,
    room_id: str,
    target_type: str,
) -> tuple[Any | None, dict[str, str] | None]:
    """Create item instance via factory. Returns (instance, None) or (None, error_dict)."""
    try:
        item_instance = item_factory.create_instance(
            prototype_id,
            quantity=quantity,
            origin={"source": "admin_summon", "summoned_by": player_name_value},
        )
        return item_instance, None
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
        return None, {"result": f"Summoning failed: {exc}"}


async def _persist_summoned_item(
    persistence: Any,
    room_id: str,
    item_instance: Any,
    quantity: int,
    player_name_value: str,
) -> None:
    """Persist item instance to DB. Logs and continues on failure (room drop still added)."""
    try:
        await persistence.create_item_instance(
            item_instance.item_instance_id,
            item_instance.prototype_id,
            {
                "owner_type": "room",
                "owner_id": room_id,
                "quantity": quantity,
                "metadata": item_instance.metadata,
                "origin_source": "admin_summon",
                "origin_metadata": {"summoned_by": player_name_value},
            },
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


async def _resolve_summon_context(
    request: Any, player_name: str, current_user: dict[str, Any]
) -> tuple[dict[str, Any] | None, dict[str, str] | None]:
    """
    Resolve state, player, admin permission, and summon prerequisites.

    Returns (context, None) on success, (None, error_result) on failure.
    Context includes persistence, connection_manager, player, state, admin_logger, dashboard,
    player_name_value, room_id, item_factory, room_manager.
    """
    persistence, connection_manager = resolve_state(request)
    player, error = await resolve_player(persistence, current_user, player_name)
    if error or not player:
        return None, error or {"result": "Player information not found."}
    if not await validate_admin_permission(player, player_name):
        return None, {
            "result": (
                "The Restricted Archives remain sealed. You do not currently possess the "
                "necessary administrative clearance to perform that ritual."
            )
        }
    state = getattr(getattr(request, "app", None), "state", None)
    admin_logger = get_admin_actions_logger()
    dashboard = get_monitoring_dashboard()
    player_name_value = player.name
    err = _validate_summon_prerequisites(state, connection_manager, player_name_value, admin_logger)
    if err:
        return None, err
    item_factory = getattr(state, "item_factory", None)
    room_manager = getattr(connection_manager, "room_manager", None)
    room_id = str(player.current_room_id)
    context = {
        "persistence": persistence,
        "connection_manager": connection_manager,
        "player": player,
        "state": state,
        "admin_logger": admin_logger,
        "dashboard": dashboard,
        "player_name_value": player_name_value,
        "room_id": room_id,
        "item_factory": item_factory,
        "room_manager": room_manager,
    }
    return context, None


def _parse_summon_command_data(
    command_data: dict[str, Any], context: dict[str, Any]
) -> tuple[dict[str, Any] | None, dict[str, str] | None]:
    """
    Parse and validate command_data; optionally record quantity spike; check NPC stub.

    Returns (parsed, None) with prototype_id, quantity, target_type, or (None, error_result).
    """
    prototype_id_raw = command_data.get("prototype_id")
    if not isinstance(prototype_id_raw, str) or not prototype_id_raw:
        logger.warning(
            "Admin summon missing or invalid prototype_id",
            player=context["player_name_value"],
            prototype_id=prototype_id_raw,
        )
        return None, {"result": "You must specify a valid prototype_id to perform this summoning ritual."}
    prototype_id = prototype_id_raw
    quantity = int(command_data.get("quantity", 1))
    target_type = command_data.get("target_type", "item")
    room_id = context["room_id"]
    room_manager = context["room_manager"]
    if room_manager is None:
        logger.warning(
            "Summon command unavailable - room manager missing at execution",
            player=context["player_name_value"],
        )
        return None, {"result": "Room inventory is unavailable; the ritual cannot anchor the summoned item."}
    dashboard = context["dashboard"]
    if quantity >= int(dashboard.alert_thresholds.get("summon_quantity_warning", 5)):
        dashboard.record_summon_quantity_spike(
            admin_name=context["player_name_value"],
            prototype_id=prototype_id,
            quantity=quantity,
            metadata={"room_id": room_id, "target_type": target_type},
        )
    err = _summon_npc_stub_response(
        prototype_id, target_type, quantity, room_id, context["player_name_value"], context["admin_logger"]
    )
    if err:
        return None, err
    return {"prototype_id": prototype_id, "quantity": quantity, "target_type": target_type}, None


async def _broadcast_and_log_summon_success(
    context: dict[str, Any],
    parsed: dict[str, Any],
    stack: dict[str, Any],
    item_name: str,
) -> None:
    """Broadcast admin_summon event to room, then record success logs."""
    connection_manager = context["connection_manager"]
    player = context["player"]
    room_id = context["room_id"]
    player_name_value = context["player_name_value"]
    quantity = parsed["quantity"]
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
    exclude = str(getattr(player, "player_id", "")) if getattr(player, "player_id", None) else None
    await broadcast_room_event(connection_manager, room_id, event, exclude_player=exclude)
    _log_summon_success(context, parsed, item_name)


def _log_summon_success(context: dict[str, Any], parsed: dict[str, Any], item_name: str) -> None:
    """Log successful summon in admin logger and structured logs."""
    player_name_value = context["player_name_value"]
    admin_logger = context["admin_logger"]
    room_id = context["room_id"]
    prototype_id = parsed["prototype_id"]
    quantity = parsed["quantity"]
    target_type = parsed["target_type"]
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
            "item_name": item_name,
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
        item_name=item_name,
    )


async def _complete_summon(context: dict[str, Any], parsed: dict[str, Any]) -> dict[str, str]:
    """Create item, persist, add to room, broadcast event, log; return success message."""
    persistence = context["persistence"]
    room_id = context["room_id"]
    player_name_value = context["player_name_value"]
    room_manager = context["room_manager"]
    item_factory = context["item_factory"]
    admin_logger = context["admin_logger"]
    prototype_id = parsed["prototype_id"]
    quantity = parsed["quantity"]
    target_type = parsed["target_type"]

    item_instance, err = _create_summon_item_instance(
        item_factory, prototype_id, quantity, player_name_value, admin_logger, room_id, target_type
    )
    if err:
        return err
    if item_instance is None:
        logger.error(
            "Summon item instance creation returned no instance without error",
            player=player_name_value,
            prototype_id=prototype_id,
            quantity=quantity,
            room_id=room_id,
        )
        return {"result": "Summoning failed due to an internal error while shaping the item."}

    stack = item_instance.to_inventory_stack()
    stack.setdefault("origin", {}).update({"source": "admin_summon", "summoned_by": player_name_value})
    stack["quantity"] = quantity
    await _persist_summoned_item(persistence, room_id, item_instance, quantity, player_name_value)
    room_manager.add_room_drop(room_id, stack)
    item_name = stack.get("item_name") or stack.get("item_id", "item")
    await _broadcast_and_log_summon_success(context, parsed, stack, item_name)
    return {"result": f"You summon {quantity}x {item_name} into {room_id}."}


async def handle_summon_command(
    command_data: dict[str, Any],
    current_user: dict[str, Any],
    request: Any,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Handle the `/summon` administrative command."""
    context, err = await _resolve_summon_context(request, player_name, current_user)
    if err:
        return err
    if context is None:
        return {"result": "Summoning failed due to an internal error while resolving context."}

    parsed, err = _parse_summon_command_data(command_data, context)
    if err:
        return err
    if parsed is None:
        return {"result": "Summoning failed due to an internal error while parsing command data."}
    return await _complete_summon(context, parsed)
