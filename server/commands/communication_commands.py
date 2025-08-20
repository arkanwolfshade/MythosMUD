"""
Communication commands for MythosMUD.

This module contains handlers for communication-related commands like say, me, and pose.
"""

from typing import Any

from ..alias_storage import AliasStorage
from ..logging_config import get_logger

logger = get_logger(__name__)


def get_username_from_user(user_obj):
    """Safely extract username from user object or dictionary."""
    if hasattr(user_obj, "username"):
        return user_obj.username
    elif isinstance(user_obj, dict) and "username" in user_obj:
        return user_obj["username"]
    else:
        raise ValueError("User object must have username attribute or key")


async def handle_say_command(
    args: list, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """
    Handle the say command for speaking to other players.

    Args:
        args: Command arguments
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Say command result
    """
    logger.debug("Processing say command", player=player_name, args=args)

    if not args:
        logger.warning("Say command with no message", player=player_name)
        return {"result": "Say what? Usage: say <message>"}

    message = " ".join(args)
    logger.debug("Player saying message", player=player_name, message=message)

    # Get app state services for broadcasting
    app = request.app if request else None
    player_service = app.state.player_service if app else None

    if not player_service:
        logger.warning("Say command failed - no player service", player=player_name)
        return {"result": "Chat functionality is not available."}

    try:
        # Get current user ID
        current_user_id = get_username_from_user(current_user)

        # Get player object to find current room
        player_obj = player_service.resolve_player_name(player_name)
        if not player_obj:
            return {"result": "Player not found."}

        # Get the player's current room
        current_room_id = getattr(player_obj, "current_room_id", None)
        if not current_room_id:
            return {"result": "You are not in a room."}

        # Get the room to find other players
        from ..realtime.connection_manager import connection_manager

        room = connection_manager.persistence.get_room(current_room_id)
        if not room:
            return {"result": "Room not found."}

        # Get other players in the room
        room_players = room.get_players()
        other_players = [p for p in room_players if p.id != current_user_id]

        # Broadcast message to other players in the room
        if other_players:
            broadcast_message = f"{player_name} says: {message}"
            for other_player in other_players:
                await connection_manager.send_personal_message(
                    other_player.id, {"type": "chat_message", "message": broadcast_message}
                )
            logger.info(
                "Say message broadcasted to room",
                player=player_name,
                room=current_room_id,
                recipients=len(other_players),
            )
        else:
            logger.debug("No other players in room to broadcast to", player=player_name, room=current_room_id)

        # Return local confirmation
        return {"result": f"You say: {message}"}

    except Exception as e:
        logger.error("Say command error", player=player_name, error=str(e))
        return {"result": f"Error sending message: {str(e)}"}


async def handle_me_command(
    args: list, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """
    Handle the me command for performing actions/emotes.

    Args:
        args: Command arguments
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Me command result
    """
    logger.debug("Processing me command", player=player_name, args=args)

    if not args:
        logger.warning("Me command with no action", player=player_name)
        return {"result": "Do what? Usage: me <action>"}

    action = " ".join(args)
    logger.debug("Player performing action", player=player_name, action=action)

    # For now, return a simple response
    # In a full implementation, this would broadcast to other players in the room
    return {"result": f"{player_name} {action}"}


async def handle_pose_command(
    args: list, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """
    Handle the pose command for setting character description.

    Args:
        args: Command arguments
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Pose command result
    """
    logger.debug("Processing pose command", player=player_name, args=args)

    app = request.app if request else None
    persistence = app.state.persistence if app else None

    if not persistence:
        logger.warning("Pose command failed - no persistence layer", player=player_name)
        return {"result": "You cannot set your pose right now."}

    player = persistence.get_player_by_name(get_username_from_user(current_user))
    if not player:
        logger.warning("Pose command failed - player not found", player=player_name)
        return {"result": "You cannot set your pose right now."}

    if not args:
        # Clear pose
        player.pose = None
        persistence.save_player(player)
        logger.info("Player cleared pose", player=player_name)
        return {"result": "Your pose has been cleared."}

    pose_description = " ".join(args)
    logger.debug("Player setting pose", player=player_name, pose=pose_description)

    # Set the pose
    player.pose = pose_description
    persistence.save_player(player)

    logger.info("Player pose set", player=player_name, pose=pose_description)
    return {"result": f"Your pose is now: {pose_description}"}
