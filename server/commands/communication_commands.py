"""
Communication commands for MythosMUD.

This module contains handlers for communication-related commands like say, me, and pose.
"""

from typing import Any

from ..alias_storage import AliasStorage
from ..logging_config import get_logger
from ..utils.command_parser import get_username_from_user

logger = get_logger(__name__)


async def handle_say_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """
    Handle the say command for speaking to other players.

    Args:
        command_data: Command data dictionary containing validated command information
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Say command result
    """
    logger.debug(f"Processing say command for {player_name} with command_data: {command_data}")

    # Extract message from command data
    message = command_data.get("message")
    if not message:
        logger.warning(f"Say command with no message for {player_name}, command_data: {command_data}")
        return {"result": "Say what? Usage: say <message>"}

    # message is already a complete string from the validation system
    logger.debug(f"Player {player_name} saying message: {message}")

    # Get app state services for broadcasting
    app = request.app if request else None
    player_service = app.state.player_service if app else None
    chat_service = app.state.chat_service if app else None

    if not player_service:
        logger.warning(f"Say command failed - no player service for {player_name}")
        return {"result": "Chat functionality is not available."}

    if not chat_service:
        logger.warning(f"Say command failed - no chat service for {player_name}")
        return {"result": "Chat functionality is not available."}

    try:
        # Get player object to find current room
        player_obj = player_service.resolve_player_name(player_name)
        if not player_obj:
            return {"result": "Player not found."}

        # Get the player's current room
        current_room_id = getattr(player_obj, "current_room_id", None)
        if not current_room_id:
            return {"result": "You are not in a room."}

        # Use the chat service to send the say message
        # This will handle NATS publishing and proper broadcasting
        # Use the player object's ID instead of the username
        player_id = getattr(player_obj, "id", None) or getattr(player_obj, "player_id", None)
        if not player_id:
            return {"result": "Player ID not found."}

        result = await chat_service.send_say_message(player_id, message)

        if result.get("success"):
            logger.info(
                f"Say message sent successfully for {player_name}",
                room=current_room_id,
                message_id=result.get("message", {}).get("id"),
            )
            return {"result": f"You say: {message}"}
        else:
            error_msg = result.get("error", "Unknown error")
            logger.warning(f"Say command failed for {player_name}: {error_msg}")
            return {"result": f"Error sending message: {error_msg}"}

    except Exception as e:
        logger.error(f"Say command error for {player_name}: {str(e)}")
        return {"result": f"Error sending message: {str(e)}"}


async def handle_me_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """
    Handle the me command for performing actions/emotes.

    Args:
        command_data: Command data dictionary containing validated command information
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Me command result
    """
    logger.debug(f"Processing me command for {player_name} with command_data: {command_data}")

    # Extract action from command data
    action = command_data.get("action")
    if not action:
        logger.warning(f"Me command with no action for {player_name}, command_data: {command_data}")
        return {"result": "Do what? Usage: me <action>"}

    # action is already a complete string from the validation system
    logger.debug(f"Player {player_name} performing action: {action}")

    # For now, return a simple response
    # In a full implementation, this would broadcast to other players in the room
    return {"result": f"{player_name} {action}"}


async def handle_pose_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """
    Handle the pose command for setting character description.

    Args:
        command_data: Command data dictionary containing validated command information
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Pose command result
    """
    logger.debug(f"Processing pose command for {player_name} with command_data: {command_data}")

    app = request.app if request else None
    persistence = app.state.persistence if app else None

    if not persistence:
        logger.warning(f"Pose command failed - no persistence layer for {player_name}")
        return {"result": "You cannot set your pose right now."}

    player = persistence.get_player_by_name(get_username_from_user(current_user))
    if not player:
        logger.warning(f"Pose command failed - player not found for {player_name}")
        return {"result": "You cannot set your pose right now."}

    # Extract pose from command data
    pose = command_data.get("pose")
    if not pose:
        # Clear pose
        player.pose = None
        persistence.save_player(player)
        logger.info(f"Player {player_name} cleared pose")
        return {"result": "Your pose has been cleared."}

    pose_description = pose
    logger.debug(f"Player {player_name} setting pose: {pose_description}")

    # Set the pose
    player.pose = pose_description
    persistence.save_player(player)

    logger.info(f"Player {player_name} pose set: {pose_description}")
    return {"result": f"Your pose is now: {pose_description}"}
