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
    args: list, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """
    Handle the look command for examining surroundings.

    Args:
        args: Command arguments
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Look command result
    """
    logger.debug(f"Processing look command for {player_name} with args: {args}")

    app = request.app if request else None
    persistence = app.state.persistence if app else None

    if not persistence:
        logger.warning(f"Look command failed - no persistence layer for {player_name}")
        return {"result": "Room information is not available."}

    try:
        player = persistence.get_player_by_name(get_username_from_user(current_user))
        if not player:
            logger.warning(f"Look command failed - player not found for {player_name}")
            return {"result": "Player information not found."}

        room_id = player.current_room_id
        room = persistence.get_room(room_id)
        if not room:
            logger.warning(f"Look command failed - room not found for {player_name}, room_id: {room_id}")
            return {"result": "You are in an unknown location."}

        # Check if looking in a specific direction
        if args:
            direction = args[0].lower()
            logger.debug(f"Looking in direction for {player_name}: {direction}, room_id: {room_id}")

            # Check if the direction is valid
            if direction not in room.exits:
                logger.debug(f"No valid exit in direction for {player_name}: {direction}, room_id: {room_id}")
                return {"result": "You don't see an exit in that direction."}

            # Get the target room
            target_room_id = room.exits[direction]
            target_room = persistence.get_room(target_room_id)
            if target_room:
                result = f"You look {direction} and see:\n{target_room.name}\n{target_room.description}"
                return {"result": result}
            else:
                return {"result": f"You look {direction} but see only darkness."}

        # Looking at current room
        valid_exits = list(room.exits.keys())
        logger.debug(f"Looked at current room for {player_name}, room_id: {room_id}, exits: {valid_exits}")

        # Build room description
        result_lines = [room.name, room.description]

        # Add exit information
        if valid_exits:
            exit_list = ", ".join(valid_exits)
            result_lines.append(f"\nExits: {exit_list}")
        else:
            result_lines.append("\nThere are no visible exits.")

        result = "\n".join(result_lines)
        return {"result": result}

    except Exception as e:
        logger.error(f"Look command error for {player_name}: {str(e)}")
        return {"result": f"Error retrieving room information: {str(e)}"}


async def handle_go_command(
    args: list, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """
    Handle the go command for moving between rooms.

    Args:
        args: Command arguments
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Go command result
    """
    logger.debug(f"Processing go command for {player_name} with args: {args}, args_length: {len(args)}")

    app = request.app if request else None
    persistence = app.state.persistence if app else None

    if not persistence:
        logger.warning(f"Go command failed - no persistence layer for {player_name}")
        return {"result": "Movement is not available."}

    if not args:
        return {"result": "Go where? Usage: go <direction>"}

    direction = args[0].lower()
    logger.debug(f"Player attempting to move for {player_name}: {direction}")

    try:
        player = persistence.get_player_by_name(get_username_from_user(current_user))
        if not player:
            logger.warning(f"Go command failed - player not found for {player_name}")
            return {"result": "Player information not found."}

        room_id = player.current_room_id
        room = persistence.get_room(room_id)
        if not room:
            logger.warning(f"Go command failed - current room not found for {player_name}, room_id: {room_id}")
            return {"result": "You are in an unknown location."}

        # Check if the direction is valid
        if direction not in room.exits:
            logger.debug(f"No exit in direction for {player_name}: {direction}, room_id: {room_id}")
            return {"result": "You don't see an exit in that direction."}

        # Get the target room
        target_room_id = room.exits[direction]
        target_room = persistence.get_room(target_room_id)
        if not target_room:
            logger.warning(
                f"Go command failed - target room not found for {player_name}, target_room_id: {target_room_id}"
            )
            return {"result": "You cannot go that way."}

        # Move the player
        from ..game.movement_service import MovementService

        movement_service = MovementService(persistence)
        result = await movement_service.move_player(player, target_room_id)

        if result.get("success"):
            logger.info(f"Player moved successfully for {player_name}: from {room_id} to {target_room_id}")
            return result
        else:
            logger.warning(f"Movement service failed for {player_name}: from {room_id} to {target_room_id}")
            return result

    except Exception as e:
        logger.error(f"Go command error for {player_name}: {str(e)}")
        return {"result": f"Error during movement: {str(e)}"}
