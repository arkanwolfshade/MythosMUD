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

    # For now, return a simple response
    # In a full implementation, this would broadcast to other players in the room
    return {"result": f"You say: {message}"}


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
