"""
Exploration commands for MythosMUD.

This module contains handlers for exploration-related commands like look and go.
"""

from typing import Any

from ..alias_storage import AliasStorage
from ..logging_config import get_logger

logger = get_logger(__name__)


def get_username_from_user(user_obj):
    """Safely extract username from user object or dictionary."""
    if hasattr(user_obj, "username"):
        return user_obj.username
    elif hasattr(user_obj, "name"):
        return user_obj.name
    elif isinstance(user_obj, dict) and "username" in user_obj:
        return user_obj["username"]
    elif isinstance(user_obj, dict) and "name" in user_obj:
        return user_obj["name"]
    else:
        raise ValueError("User object must have username or name attribute or key")


async def handle_look_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """
    Handle the look command for examining surroundings.

    Args:
        command_data: Command data dictionary containing validated command information
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Look command result
    """
    logger.debug("Processing look command", player=player_name, args=command_data)

    app = request.app if request else None
    persistence = app.state.persistence if app else None

    if not persistence:
        logger.warning("Look command failed - no persistence layer", player=player_name)
        return {"result": "You see nothing special."}

    player = persistence.get_player_by_name(get_username_from_user(current_user))
    if not player:
        logger.warning("Look command failed - player not found", player=player_name)
        return {"result": "You see nothing special."}

    room_id = player.current_room_id
    room = persistence.get_room(room_id)
    if not room:
        logger.warning("Look command failed - room not found", player=player_name, room_id=room_id)
        return {"result": "You see nothing special."}

    # Extract direction from command_data
    direction = command_data.get("direction")
    if direction:
        direction = direction.lower()
        logger.debug("Looking in direction", player=player_name, direction=direction, room_id=room_id)
        exits = room.exits
        target_room_id = exits.get(direction)
        if target_room_id:
            target_room = persistence.get_room(target_room_id)
            if target_room:
                name = target_room.name
                desc = target_room.description
                logger.debug(
                    "Looked at room in direction",
                    player=player_name,
                    direction=direction,
                    target_room_id=target_room_id,
                )
                return {"result": f"{name}\n{desc}"}
        logger.debug("No valid exit in direction", player=player_name, direction=direction, room_id=room_id)
        return {"result": "You see nothing special that way."}

    # Look at current room
    name = room.name
    desc = room.description
    exits = room.exits
    # Only include exits that have valid room IDs (not null)
    valid_exits = [direction for direction, room_id in exits.items() if room_id is not None]
    exit_list = ", ".join(valid_exits) if valid_exits else "none"
    logger.debug("Looked at current room", player=player_name, room_id=room_id, exits=valid_exits)
    return {"result": f"{name}\n{desc}\n\nExits: {exit_list}"}


async def handle_go_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
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
    logger.debug("Processing go command", player=player_name, args=command_data)

    app = request.app if request else None
    persistence = app.state.persistence if app else None

    if not persistence:
        logger.warning("Go command failed - no persistence layer", player=player_name)
        return {"result": "You can't go that way"}

    # Extract direction from command_data
    direction = command_data.get("direction")
    if not direction:
        logger.warning("Go command failed - no direction specified", player=player_name, command_data=command_data)
        return {"result": "Go where? Usage: go <direction>"}

    direction = direction.lower()
    logger.debug("Player attempting to move", player=player_name, direction=direction)

    player = persistence.get_player_by_name(get_username_from_user(current_user))
    if not player:
        logger.warning("Go command failed - player not found", player=player_name)
        return {"result": "You can't go that way"}

    room_id = player.current_room_id
    room = persistence.get_room(room_id)
    if not room:
        logger.warning("Go command failed - current room not found", player=player_name, room_id=room_id)
        return {"result": "You can't go that way"}

    exits = room.exits
    target_room_id = exits.get(direction)
    if not target_room_id:
        logger.debug("No exit in direction", player=player_name, direction=direction, room_id=room_id)
        return {"result": "You can't go that way"}

    target_room = persistence.get_room(target_room_id)
    if not target_room:
        logger.warning("Go command failed - target room not found", player=player_name, target_room_id=target_room_id)
        return {"result": "You can't go that way"}

    # Use movement service for the actual movement
    from ..game.movement_service import MovementService

    try:
        # Pass the same event bus that persistence uses to ensure events are published correctly
        movement_service = MovementService(persistence._event_bus)
        success = movement_service.move_player(str(player.player_id), room_id, target_room_id)

        if success:
            logger.info(f"Player moved successfully for {player_name}: from {room_id} to {target_room_id}")
            return {"result": "You move to the new location."}
        else:
            logger.warning(f"Movement service failed for {player_name}: from {room_id} to {target_room_id}")
            return {"result": "You can't go that way."}

    except Exception as e:
        logger.error(f"Go command error for {player_name}: {str(e)}")
        return {"result": f"Error during movement: {str(e)}"}
