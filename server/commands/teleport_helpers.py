"""Helper functions for teleport command operations."""

# pylint: disable=too-many-arguments  # Reason: Teleport helpers require many parameters for context and validation

from typing import Any, cast

from ..structured_logging.admin_actions_logger import get_admin_actions_logger
from ..structured_logging.enhanced_logging_config import get_logger
from .admin_teleport_utils import (
    broadcast_teleport_effects,
    get_online_player_by_display_name,
    notify_player_of_teleport,
)

logger = get_logger(__name__)

# Direction opposites for teleport arrival messages
DIRECTION_OPPOSITES: dict[str, str] = {
    "north": "south",
    "south": "north",
    "east": "west",
    "west": "east",
    "up": "down",
    "down": "up",
    "northeast": "southwest",
    "southwest": "northeast",
    "northwest": "southeast",
    "southeast": "northwest",
}


async def resolve_teleport_services(app: Any, player_name: str) -> tuple[Any, Any, Any, Any] | dict[str, str]:
    """Resolve required services for teleport command."""
    if not app:
        logger.warning("Teleport command failed - no app context", player_name=player_name)
        return {"result": "Teleport functionality is not available."}

    player_service = app.state.player_service if app else None
    if not player_service:
        logger.warning("Teleport command failed - no player service", player_name=player_name)
        return {"result": "Player service not available."}

    connection_manager = app.state.connection_manager if app else None
    if not connection_manager:
        logger.warning("Teleport command failed - no connection manager", player_name=player_name)
        return {"result": "Connection manager not available."}

    persistence = getattr(app.state, "persistence", None)
    return player_service, connection_manager, persistence, app


def resolve_teleport_direction(
    direction_value: str | None, persistence: Any, current_player: Any, player_name: str
) -> tuple[str, str | None] | dict[str, str]:
    """Resolve target room ID from direction."""
    if not direction_value:
        return current_player.current_room_id, None

    if not persistence:
        logger.warning(
            "Teleport command failed - direction specified but persistence unavailable", player_name=player_name
        )
        return {"result": "World data is not available for directional teleportation."}

    admin_room = persistence.get_room_by_id(current_player.current_room_id) if persistence else None
    if not admin_room:
        logger.warning(
            "Teleport command failed - admin room not found",
            player_name=player_name,
            room_id=current_player.current_room_id,
        )
        return {"result": "Unable to determine your current location."}

    exits = getattr(admin_room, "exits", {}) or {}
    target_room_id = exits.get(direction_value)
    if not target_room_id:
        logger.warning(
            "Teleport command failed - invalid direction",
            player_name=player_name,
            direction=direction_value,
            room_id=current_player.current_room_id,
        )
        return {"result": f"There is no exit to the {direction_value} from here."}

    target_room_name = None
    target_room = persistence.get_room_by_id(target_room_id)
    if target_room and hasattr(target_room, "name"):
        target_room_name = target_room.name

    return target_room_id, target_room_name


async def resolve_target_player(
    player_service: Any,
    connection_manager: Any,
    target_player_name: str,
    current_player: Any,
    direction_value: str | None,
) -> tuple[Any, dict[str, Any]] | dict[str, str]:
    """Resolve target player for teleport command."""
    target_player_info = await get_online_player_by_display_name(target_player_name, connection_manager)
    if not target_player_info:
        return {"result": f"Player '{target_player_name}' is not online or not found."}

    target_player = await player_service.get_player_by_name(target_player_name)
    if not target_player:
        logger.warning(
            "Teleport command failed - target player not found in database", target_player_name=target_player_name
        )
        return {"result": f"Player '{target_player_name}' not found in database."}

    if not direction_value and target_player.current_room_id == current_player.current_room_id:
        return {"result": f"{target_player_name} is already in your location."}

    return target_player, target_player_info


async def update_teleport_location(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Teleport helpers require many parameters for context and location updates
    player_service: Any,
    target_player: Any,
    target_player_name: str,
    target_room_id: str,
    target_player_info: dict[str, Any],
    connection_manager: Any,
    persistence: Any | None,
) -> str | dict[str, str]:
    """Update target player location for teleport."""
    original_room_id = target_player.current_room_id
    success = await player_service.update_player_location(target_player_name, target_room_id)
    if not success:
        logger.error("Failed to update target player location", target_player_name=target_player_name)
        return {"result": f"Failed to teleport {target_player_name}: database update failed."}

    target_player.current_room_id = target_room_id

    target_player_identifier = (
        target_player_info.get("player_id")
        or getattr(target_player, "player_id", None)
        or getattr(target_player, "id", None)
    )
    if target_player_identifier is not None:
        target_player_identifier = str(target_player_identifier)
        target_player_info["current_room_id"] = target_room_id

        online_record = connection_manager.online_players.get(target_player_identifier)
        if online_record is not None:
            online_record["current_room_id"] = target_room_id

        await update_player_room_location(
            connection_manager, target_player_identifier, original_room_id, target_room_id, persistence
        )

    return cast("str | dict[str, str]", original_room_id)


async def update_player_room_location(
    connection_manager: Any,
    target_player_identifier: str,
    original_room_id: str,
    target_room_id: str,
    persistence: Any | None,
) -> None:
    """Update player location in room manager and persistence."""
    try:
        connection_manager.room_manager.remove_room_occupant(target_player_identifier, original_room_id)
    except (ValueError, TypeError, AttributeError, KeyError) as exc:
        logger.debug(
            "Failed to remove teleport target from prior room occupants",
            player_id=target_player_identifier,
            room_id=original_room_id,
            error=str(exc),
        )

    try:
        connection_manager.room_manager.add_room_occupant(target_player_identifier, target_room_id)
    except (ValueError, TypeError, AttributeError, KeyError) as exc:
        logger.debug(
            "Failed to add teleport target to destination room occupants",
            player_id=target_player_identifier,
            room_id=target_room_id,
            error=str(exc),
        )

    try:
        connection_manager.room_manager.reconcile_room_presence(original_room_id, connection_manager.online_players)
        connection_manager.room_manager.reconcile_room_presence(target_room_id, connection_manager.online_players)
    except (ValueError, TypeError, AttributeError, KeyError) as exc:
        logger.debug(
            "Failed to reconcile room presence after teleport", player_id=target_player_identifier, error=str(exc)
        )

    if persistence:
        try:
            source_room = persistence.get_room_by_id(original_room_id)
            if source_room:
                source_room.player_left(target_player_identifier)
        except (ValueError, AttributeError, TypeError) as exc:
            logger.debug(
                "Failed to mark teleport target as leaving source room",
                player_id=target_player_identifier,
                room_id=original_room_id,
                error=str(exc),
            )

        try:
            destination_room = persistence.get_room_by_id(target_room_id)
            if destination_room:
                destination_room.player_entered(target_player_identifier)
        except (ValueError, AttributeError, TypeError) as exc:
            logger.debug(
                "Failed to mark teleport target as entering destination room",
                player_id=target_player_identifier,
                room_id=target_room_id,
                error=str(exc),
            )


async def broadcast_teleport_updates(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Teleport helpers require many parameters for context and broadcasting
    connection_manager: Any,
    target_player_info: dict[str, Any],
    target_room_id: str,
    target_player_name: str,
    player_name: str,
    direction_value: str | None,
    target_room_name: str | None,
    original_room_id: str,
) -> None:
    """Broadcast teleport effects. Room state is notified via EventBus (Room.player_entered/player_left)."""
    arrival_direction = DIRECTION_OPPOSITES.get(direction_value) if direction_value else None
    await broadcast_teleport_effects(
        connection_manager,
        target_player_name,
        original_room_id,
        target_room_id,
        "teleport",
        direction=direction_value,
        arrival_direction=arrival_direction,
        target_player_id=str(target_player_info.get("player_id")) if target_player_info else None,
    )

    if direction_value:
        target_message = f"You are teleported to the {direction_value} by {player_name}."
    else:
        destination_name = target_room_name or f"{player_name}'s location"
        target_message = f"You are teleported to {destination_name}."

    await notify_player_of_teleport(
        connection_manager, target_player_name, player_name, "teleported_to", message=target_message
    )


def build_teleport_message(target_player_name: str, direction_value: str | None) -> str:
    """Build admin message for teleport command."""
    if direction_value:
        return f"You teleport {target_player_name} to the {direction_value}."
    return f"You teleport {target_player_name} to your location."


def log_teleport_success(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Teleport helpers require many parameters for context and logging
    player_name: str,
    target_player_name: str,
    direction_value: str | None,
    target_room_id: str,
    original_room_id: str,
    admin_room_id: str,
) -> None:
    """Log successful teleport action."""
    try:
        admin_logger = get_admin_actions_logger()
        admin_logger.log_teleport_action(
            admin_name=player_name,
            target_player=target_player_name,
            action_type="teleport",
            from_room=original_room_id,
            to_room=target_room_id,
            success=True,
            additional_data={
                "admin_room_id": admin_room_id,
                "target_room_id": target_room_id,
                "direction": direction_value,
            },
        )
    except (OSError, AttributeError, TypeError) as log_exc:
        logger.warning("Failed to log teleport action", player_name=player_name, error=str(log_exc))

    logger.info(
        "Teleport executed successfully",
        admin_name=player_name,
        target_player=target_player_name,
        direction=direction_value,
        destination_room=target_room_id,
    )


async def validate_confirm_teleport_context(
    app: Any, player_service: Any, player_name: str
) -> tuple[Any | None, dict[str, str] | None]:
    """Validate app context and get current player with admin permissions. Returns (current_player, error_result)."""
    if not app:
        logger.warning("Confirm teleport command failed - no app context", player_name=player_name)
        return None, {"result": "Teleport functionality is not available."}

    if not player_service:
        logger.warning("Confirm teleport command failed - no player service", player_name=player_name)
        return None, {"result": "Player service not available."}

    current_player = await player_service.get_player_by_name(player_name)
    if not current_player:
        logger.warning("Confirm teleport command failed - current player not found", player_name=player_name)
        return None, {"result": "Player not found."}

    from .admin_permission_utils import validate_admin_permission

    is_admin = await validate_admin_permission(current_player, player_name)
    if not is_admin:
        return None, {"result": "You do not have permission to use teleport commands."}

    return current_player, None


async def resolve_target_player_for_teleport(
    target_player_name: str, connection_manager: Any, player_service: Any
) -> tuple[dict[str, Any] | None, Any | None, dict[str, str] | None]:
    """Resolve target player (online check and database lookup). Returns (target_player_info, target_player, error_result)."""
    target_player_info = await get_online_player_by_display_name(target_player_name, connection_manager)
    if not target_player_info:
        return None, None, {"result": f"Player '{target_player_name}' is not online or not found."}

    target_player = await player_service.get_player_by_name(target_player_name)
    if not target_player:
        logger.warning(
            "Confirm teleport command failed - target player not found in database",
            target_player_name=target_player_name,
        )
        return None, None, {"result": f"Player '{target_player_name}' not found in database."}

    return target_player_info, target_player, None


async def execute_confirm_teleport(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Teleport helpers require many parameters for context and teleport execution
    target_player_name: str,
    target_player: Any,
    target_player_info: dict[str, Any],
    current_player: Any,
    player_service: Any,
    connection_manager: Any,
    player_name: str,
    persistence: Any | None = None,
) -> dict[str, str]:
    """Execute the teleportation (update location, room occupancy via EventBus, effects, logging)."""
    original_room_id = target_player.current_room_id
    target_room_id = current_player.current_room_id

    success = await player_service.update_player_location(target_player_name, target_room_id)
    if not success:
        logger.error("Failed to update target player location", target_player_name=target_player_name)
        return {"result": f"Failed to teleport {target_player_name}: database update failed."}

    if target_player_info:
        target_player_info["room_id"] = target_room_id

    await update_player_room_location(
        connection_manager,
        str(target_player_info["player_id"]),
        original_room_id,
        target_room_id,
        persistence,
    )

    await broadcast_teleport_effects(
        connection_manager,
        target_player_name,
        original_room_id,
        target_room_id,
        "teleport",
        direction=None,
        arrival_direction=None,
        target_player_id=str(target_player_info.get("player_id")) if target_player_info else None,
    )

    await notify_player_of_teleport(
        connection_manager,
        target_player_name,
        player_name,
        "teleported_to",
        message=f"You are teleported to {player_name}'s location.",
    )

    admin_logger = get_admin_actions_logger()
    admin_logger.log_teleport_action(
        admin_name=player_name,
        target_player=target_player_name,
        action_type="teleport",
        from_room=original_room_id,
        to_room=target_room_id,
        success=True,
    )

    logger.info(
        "Teleport confirmed and executed",
        admin_name=player_name,
        target_player=target_player_name,
        from_room=original_room_id,
        to_room=target_room_id,
    )

    return {"result": f"Successfully teleported {target_player_name} to your location."}
