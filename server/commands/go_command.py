"""
Go command for MythosMUD.

This module handles the go command for player movement.
"""

# pylint: disable=too-many-arguments,too-many-locals  # Reason: Movement commands require many parameters and intermediate variables for complex movement logic

import uuid
from typing import Any

from ..alias_storage import AliasStorage
from ..commands.rest_command import _cancel_rest_countdown, is_player_resting
from ..exceptions import DatabaseError, ValidationError
from ..game.movement_service import MovementService
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.command_parser import get_username_from_user

logger = get_logger(__name__)


async def _setup_go_command(
    request: Any, current_user: dict, player_name: str
) -> tuple[Any, Any, Any, Any, str] | None:
    """Setup and validate go command prerequisites."""
    app = request.app if request else None
    persistence = app.state.persistence if app else None

    if not persistence:
        logger.warning("Go command failed - no persistence layer", player=player_name)
        return None

    player = await persistence.get_player_by_name(get_username_from_user(current_user))
    if not player:
        logger.warning("Go command failed - player not found", player=player_name)
        return None

    room_id = player.current_room_id
    room = persistence.get_room_by_id(room_id)
    if not room:
        logger.warning("Go command failed - current room not found", player=player_name, room_id=room_id)
        return None

    if room.id != room_id:
        logger.warning(
            "Room ID mismatch detected",
            player=player_name,
            player_room_id=room_id,
            room_object_id=room.id,
        )
        room_id = room.id

    return (app, persistence, player, room, room_id)


def _validate_player_posture(player: Any, player_name: str, room_id: str) -> tuple[bool, str]:
    """Validate that player is in a valid posture for movement."""
    position = "standing"
    if hasattr(player, "get_stats"):
        try:
            stats = player.get_stats() or {}
            position = str(stats.get("position", "standing") or "standing").lower()
        except (AttributeError, TypeError, ValueError) as exc:  # pragma: no cover - defensive logging path
            logger.warning(
                "Failed to read player stats during go command",
                player=player_name,
                error=str(exc),
                room_id=room_id,
            )
            position = "standing"

    if position != "standing":
        logger.info(
            "Movement blocked - player not standing",
            player=player_name,
            position=position,
            room_id=room_id,
        )
        return (False, "You need to stand up before moving.")
    return (True, "")


def _validate_exit(direction: str, room: Any, persistence: Any, player_name: str, room_id: str) -> str | None:
    """Validate that exit exists and target room is valid."""
    exits = room.exits
    if not exits:
        exits = {}
        logger.warning(
            "Room has no exits dictionary",
            player=player_name,
            room_id=room_id,
            room_object_id=room.id,
        )

    logger.info(
        "DEBUG: Movement attempt",
        player=player_name,
        room_object_id=room.id,
        room_id_used=room_id,
        direction=direction,
        exits_dict=exits,
        exits_dict_keys=list(exits.keys()) if exits else [],
        exits_dict_type=type(exits).__name__,
    )
    target_room_id = exits.get(direction)
    if not target_room_id:
        return None

    # Validate that target room exists
    if not persistence.get_room_by_id(target_room_id):
        logger.warning("Go command failed - target room not found", player=player_name, target_room_id=target_room_id)
        return None

    return target_room_id


async def _execute_movement(  # pylint: disable=too-many-arguments,too-many-positional-arguments,too-many-locals  # Reason: Movement execution requires many parameters and intermediate variables for complex movement logic
    player: Any,
    room_id: str,
    target_room_id: str,
    app: Any,
    persistence: Any,
    player_name: str,
    direction: str,
) -> dict[str, Any]:
    """Execute player movement using movement service."""
    try:
        player_combat_service = getattr(app.state, "player_combat_service", None) if app else None
        event_bus = getattr(app.state, "event_bus", None) if app else None

        # Get MovementService from container
        if app and hasattr(app.state, "container"):
            movement_service = app.state.container.movement_service
        else:
            # Fallback for tests or other environments where container might not be fully initialized
            movement_service = MovementService(
                event_bus, player_combat_service=player_combat_service, async_persistence=persistence
            )
        success = await movement_service.move_player(player.player_id, room_id, target_room_id)

        if success:
            logger.info("Player moved successfully", player=player_name, from_room=room_id, to_room=target_room_id)
            return {
                "result": f"You go {direction}.",
                "room_changed": True,
                "room_id": target_room_id,
            }
        logger.warning("Movement service failed", player=player_name, from_room=room_id, to_room=target_room_id)
        return {"result": "You can't go that way."}

    except (ValidationError, ValueError, RuntimeError, DatabaseError, AttributeError, TypeError) as e:
        logger.error(
            "Go command error",
            player=player_name,
            room_id=room_id,
            target_room_id=target_room_id,
            error_type=type(e).__name__,
            error_message=str(e),
            exc_info=True,
        )
        return {"result": f"Error during movement: {str(e)}"}


async def handle_go_command(  # pylint: disable=too-many-arguments,too-many-locals  # Reason: Go command requires many parameters and intermediate variables for complex movement logic
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage | None, player_name: str
) -> dict[str, Any]:
    """
    Handle the go command for movement.

    Args:
        command_data: Command data dictionary containing validated command information
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Go command result
    """
    _ = alias_storage  # Intentionally unused - part of standard command handler interface
    logger.debug("Processing go command", player=player_name, args=command_data)

    direction = command_data.get("direction")
    if not direction:
        logger.warning("Go command failed - no direction specified", player=player_name, command_data=command_data)
        return {"result": "Go where? Usage: go <direction>"}

    direction = direction.lower()
    logger.debug("Player attempting to move", player=player_name, direction=direction)

    setup_result = await _setup_go_command(request, current_user, player_name)
    if not setup_result:
        return {"result": "You can't go that way"}

    app, persistence, player, room, room_id = setup_result

    valid_posture, posture_message = _validate_player_posture(player, player_name, room_id)
    if not valid_posture:
        return {"result": posture_message}

    # Check if player is resting and interrupt rest
    connection_manager = getattr(app.state, "connection_manager", None) if app else None
    if connection_manager:
        player_id = uuid.UUID(player.player_id) if isinstance(player.player_id, str) else player.player_id

        if is_player_resting(player_id, connection_manager):
            await _cancel_rest_countdown(player_id, connection_manager)
            logger.info(
                "Rest interrupted by movement", player_id=player_id, player_name=player_name, direction=direction
            )
            return {"result": "Your rest is interrupted as you begin to move."}

    target_room_id = _validate_exit(direction, room, persistence, player_name, room_id)
    if not target_room_id:
        return {"result": "You can't go that way"}

    return await _execute_movement(player, room_id, target_room_id, app, persistence, player_name, direction)
