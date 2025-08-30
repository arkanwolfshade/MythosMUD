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


async def handle_local_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """
    Handle the local command for speaking in the local channel.

    Args:
        command_data: Command data dictionary containing validated command information
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Local command result
    """
    logger.debug(f"Processing local command for {player_name} with command_data: {command_data}")

    # Extract message from command data
    message = command_data.get("message")
    if not message or not message.strip():
        logger.warning(f"Local command with no message for {player_name}, command_data: {command_data}")
        return {"result": "Say what? Usage: local <message> or /l <message>"}

    # message is already a complete string from the validation system
    logger.debug(f"Player {player_name} saying local message: {message}")

    # Get app state services for broadcasting
    app = request.app if request else None
    player_service = app.state.player_service if app else None
    chat_service = app.state.chat_service if app else None

    if not player_service:
        logger.warning(f"Local command failed - no player service for {player_name}")
        return {"result": "Chat functionality is not available."}

    if not chat_service:
        logger.warning(f"Local command failed - no chat service for {player_name}")
        return {"result": "Chat functionality is not available."}

    try:
        # Get player object to find current room
        player_obj = player_service.resolve_player_name(player_name)
        logger.debug(f"Player {player_name} resolved player_obj: {player_obj}")
        if not player_obj:
            return {"result": "Player not found."}

        # Get the player's current room
        current_room_id = getattr(player_obj, "current_room_id", None)
        logger.debug(f"Player {player_name} current_room_id: {current_room_id}")
        if not current_room_id:
            return {"result": "You are not in a room."}

        # Use the chat service to send the local message
        # This will handle NATS publishing and proper broadcasting
        # Use the player object's ID instead of the username
        player_id = getattr(player_obj, "id", None) or getattr(player_obj, "player_id", None)
        if not player_id:
            return {"result": "Player ID not found."}

        result = await chat_service.send_local_message(player_id, message)

        if result.get("success"):
            logger.info(
                f"Local message sent successfully for {player_name}",
                room=current_room_id,
                message_id=result.get("message", {}).get("id"),
            )
            return {"result": f"You say (local): {message}"}
        else:
            error_msg = result.get("error", "Unknown error")
            logger.warning(f"Local command failed for {player_name}: {error_msg}")
            return {"result": f"Error sending message: {error_msg}"}

    except Exception as e:
        logger.error(f"Local command error for {player_name}: {str(e)}")
        return {"result": f"Error sending message: {str(e)}"}


async def handle_global_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """
    Handle the global command for speaking in the global channel.

    Args:
        command_data: Command data dictionary containing validated command information
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Global command result
    """
    logger.debug(f"Processing global command for {player_name} with command_data: {command_data}")

    # Extract message from command data
    message = command_data.get("message")
    if not message or not message.strip():
        logger.warning(f"Global command with no message for {player_name}, command_data: {command_data}")
        return {"result": "Say what? Usage: global <message> or /g <message>"}

    # message is already a complete string from the validation system
    logger.debug(f"Player {player_name} saying global message: {message}")

    # Get app state services for broadcasting
    app = request.app if request else None
    player_service = app.state.player_service if app else None
    chat_service = app.state.chat_service if app else None

    if not player_service:
        logger.warning(f"Global command failed - no player service for {player_name}")
        return {"result": "Chat functionality is not available."}

    if not chat_service:
        logger.warning(f"Global command failed - no chat service for {player_name}")
        return {"result": "Chat functionality is not available."}

    try:
        # Get player object to check level and get player ID
        player_obj = player_service.resolve_player_name(player_name)
        logger.debug(f"Player {player_name} resolved player_obj: {player_obj}")
        if not player_obj:
            return {"result": "Player not found."}

        # Check player level (global channel requires level 1+)
        player_level = getattr(player_obj, "level", 0)
        if player_level < 1:
            return {"result": "You must be at least level 1 to use global chat."}

        # Use the chat service to send the global message
        # This will handle NATS publishing and proper broadcasting
        # Use the player object's ID instead of the username
        player_id = getattr(player_obj, "id", None) or getattr(player_obj, "player_id", None)
        if not player_id:
            return {"result": "Player ID not found."}

        result = await chat_service.send_global_message(player_id, message)

        if result.get("success"):
            logger.info(
                f"Global message sent successfully for {player_name}",
                player_level=player_level,
                message_id=result.get("message", {}).get("id"),
            )
            return {"result": f"You say (global): {message}"}
        else:
            error_msg = result.get("error", "Unknown error")
            logger.warning(f"Global command failed for {player_name}: {error_msg}")
            return {"result": f"Error sending message: {error_msg}"}

    except Exception as e:
        logger.error(f"Global command error for {player_name}: {str(e)}")
        return {"result": f"Error sending message: {str(e)}"}


async def handle_system_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """
    Handle the system command for sending system messages (admin only).

    Args:
        command_data: Command data dictionary containing validated command information
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: System command result
    """
    logger.debug(f"Processing system command for {player_name} with command_data: {command_data}")

    # Extract message from command data
    message = command_data.get("message")
    if not message or not message.strip():
        logger.warning(f"System command with no message for {player_name}, command_data: {command_data}")
        return {"result": "System what? Usage: system <message>"}

    # message is already a complete string from the validation system
    logger.debug(f"Player {player_name} sending system message: {message}")

    # Get app state services for broadcasting
    app = request.app if request else None
    player_service = app.state.player_service if app else None
    chat_service = app.state.chat_service if app else None
    user_manager = app.state.user_manager if app else None

    if not player_service:
        logger.warning(f"System command failed - no player service for {player_name}")
        return {"result": "Chat functionality is not available."}

    if not chat_service:
        logger.warning(f"System command failed - no chat service for {player_name}")
        return {"result": "Chat functionality is not available."}

    if not user_manager:
        logger.warning(f"System command failed - no user manager for {player_name}")
        return {"result": "Admin functionality is not available."}

    try:
        # Get player object to find current room
        player_obj = player_service.resolve_player_name(player_name)
        if not player_obj:
            return {"result": "Player not found."}

        # Use the player object's ID instead of the username
        player_id = getattr(player_obj, "id", None) or getattr(player_obj, "player_id", None)
        if not player_id:
            return {"result": "Player ID not found."}

        # Check if player is an admin
        if not user_manager.is_admin(player_id):
            logger.warning(f"Non-admin player {player_name} attempted to use system command")
            return {"result": "You must be an admin to send system messages."}

        # Use the chat service to send the system message
        # This will handle NATS publishing and proper broadcasting
        result = await chat_service.send_system_message(player_id, message)

        if result.get("success"):
            logger.info(
                f"System message sent successfully for {player_name}",
                message_id=result.get("message", {}).get("id"),
            )
            return {"result": f"You system: {message}"}
        else:
            error_msg = result.get("error", "Unknown error")
            logger.warning(f"System command failed for {player_name}: {error_msg}")
            return {"result": f"Error sending system message: {error_msg}"}

    except Exception as e:
        logger.error(f"System command error for {player_name}: {str(e)}")
        return {"result": f"Error sending system message: {str(e)}"}


async def handle_whisper_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """
    Handle the whisper command for private messaging between players.

    Args:
        command_data: Command data dictionary containing validated command information
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Whisper command result
    """
    logger.debug(f"Processing whisper command for {player_name} with command_data: {command_data}")

    # Extract target and message from command data
    target = command_data.get("target")
    message = command_data.get("message")

    if not target or not message:
        logger.warning(
            f"Whisper command with missing target or message for {player_name}, command_data: {command_data}"
        )
        return {"result": "Say what? Usage: whisper <player> <message>"}

    # message is already a complete string from the validation system
    logger.debug(f"Player {player_name} whispering to {target}: {message}")

    # Get app state services for broadcasting
    app = request.app if request else None
    player_service = app.state.player_service if app else None
    chat_service = app.state.chat_service if app else None

    if not player_service:
        logger.warning(f"Whisper command failed - no player service for {player_name}")
        return {"result": "Chat functionality is not available."}

    if not chat_service:
        logger.warning(f"Whisper command failed - no chat service for {player_name}")
        return {"result": "Chat functionality is not available."}

    try:
        # Get sender player object
        sender_obj = player_service.resolve_player_name(player_name)
        if not sender_obj:
            return {"result": "Player not found."}

        # Get target player object
        target_obj = player_service.resolve_player_name(target)
        if not target_obj:
            return {"result": "You whisper into the aether."}

        # Check if trying to whisper to self
        if sender_obj.id == target_obj.id:
            return {"result": "You cannot whisper to yourself"}

        # Use the player object's ID instead of the username
        sender_id = getattr(sender_obj, "id", None) or getattr(sender_obj, "player_id", None)
        target_id = getattr(target_obj, "id", None) or getattr(target_obj, "player_id", None)

        if not sender_id or not target_id:
            return {"result": "Player ID not found."}

        # Use the chat service to send the whisper message
        # This will handle NATS publishing and proper broadcasting
        result = await chat_service.send_whisper_message(sender_id, target_id, message)

        if result.get("success"):
            logger.info(
                f"Whisper message sent successfully for {player_name} to {target}",
                message_id=result.get("message", {}).get("id"),
            )
            return {"result": f"You whisper to {target}: {message}"}
        else:
            error_msg = result.get("error", "Unknown error")
            logger.warning(f"Whisper command failed for {player_name}: {error_msg}")
            return {"result": f"Error sending whisper: {error_msg}"}

    except Exception as e:
        logger.error(f"Whisper command error for {player_name}: {str(e)}")
        return {"result": f"Error sending whisper: {str(e)}"}


async def handle_reply_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """
    Handle the reply command for responding to the last whisper received.

    Args:
        command_data: Command data dictionary containing validated command information
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Reply command result
    """
    logger.debug(f"Processing reply command for {player_name} with command_data: {command_data}")

    # Extract message from command data
    message = command_data.get("message")

    if not message:
        logger.warning(f"Reply command with no message for {player_name}, command_data: {command_data}")
        return {"result": "Say what? Usage: reply <message>"}

    # message is already a complete string from the validation system
    logger.debug(f"Player {player_name} replying to last whisper: {message}")

    # Get app state services for broadcasting
    app = request.app if request else None
    player_service = app.state.player_service if app else None
    chat_service = app.state.chat_service if app else None

    if not player_service:
        logger.warning(f"Reply command failed - no player service for {player_name}")
        return {"result": "Chat functionality is not available."}

    if not chat_service:
        logger.warning(f"Reply command failed - no chat service for {player_name}")
        return {"result": "Chat functionality is not available."}

    try:
        # Get sender player object
        sender_obj = player_service.resolve_player_name(player_name)
        if not sender_obj:
            return {"result": "Player not found."}

        # Get the last whisper sender for this player
        # This would need to be implemented in the chat service or a separate tracking service
        last_whisper_sender = chat_service.get_last_whisper_sender(player_name)
        if not last_whisper_sender:
            return {"result": "No one has whispered to you recently."}

        # Get target player object
        target_obj = player_service.resolve_player_name(last_whisper_sender)
        if not target_obj:
            return {"result": "The player you're trying to reply to is no longer available."}

        # Use the player object's ID instead of the username
        sender_id = getattr(sender_obj, "id", None) or getattr(sender_obj, "player_id", None)
        target_id = getattr(target_obj, "id", None) or getattr(target_obj, "player_id", None)

        if not sender_id or not target_id:
            return {"result": "Player ID not found."}

        # Use the chat service to send the whisper message
        # This will handle NATS publishing and proper broadcasting
        result = await chat_service.send_whisper_message(sender_id, target_id, message)

        if result.get("success"):
            logger.info(
                f"Reply message sent successfully for {player_name} to {last_whisper_sender}",
                message_id=result.get("message", {}).get("id"),
            )
            return {"result": f"You whisper to {last_whisper_sender}: {message}"}
        else:
            error_msg = result.get("error", "Unknown error")
            logger.warning(f"Reply command failed for {player_name}: {error_msg}")
            return {"result": f"Error sending reply: {error_msg}"}

    except Exception as e:
        logger.error(f"Reply command error for {player_name}: {str(e)}")
        return {"result": f"Error sending reply: {str(e)}"}
