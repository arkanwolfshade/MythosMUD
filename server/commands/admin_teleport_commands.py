"""
Admin teleport commands for MythosMUD.

This module contains handlers for admin teleport commands including
teleport and goto functionality with proper validation and security.
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


async def validate_admin_permission(player, player_name: str) -> bool:
    """
    Validate that a player has admin permissions.

    Args:
        player: Player object to check
        player_name: Player name for logging

    Returns:
        bool: True if player has admin permissions, False otherwise
    """
    if not player:
        logger.warning(f"Admin permission check failed - no player object for {player_name}")
        return False

    if not hasattr(player, "is_admin"):
        logger.warning(f"Admin permission check failed - player {player_name} has no is_admin attribute")
        return False

    if not player.is_admin:
        logger.info(f"Admin permission denied for {player_name}")
        return False

    logger.debug(f"Admin permission granted for {player_name}")
    return True


async def get_online_player_by_display_name(display_name: str, connection_manager) -> dict | None:
    """
    Get online player information by display name.

    Args:
        display_name: Display name to search for
        connection_manager: Connection manager instance

    Returns:
        dict: Player information if found, None otherwise
    """
    if not connection_manager or not hasattr(connection_manager, "online_players"):
        logger.warning("Connection manager not available for online player lookup")
        return None

    # Case-insensitive search
    display_name_lower = display_name.lower()

    for player_id, player_info in connection_manager.online_players.items():
        if player_info.get("display_name", "").lower() == display_name_lower:
            logger.debug(f"Found online player {display_name} with ID {player_id}")
            return player_info

    logger.debug(f"Online player {display_name} not found")
    return None


def create_teleport_effect_message(player_name: str, effect_type: str) -> str:
    """
    Create teleport effect message for visual display.

    Args:
        player_name: Name of the player being teleported
        effect_type: Type of effect ('arrival' or 'departure')

    Returns:
        str: Formatted teleport effect message
    """
    if effect_type == "arrival":
        return f"*{player_name} materializes in a swirl of eldritch energy*"
    elif effect_type == "departure":
        return f"*{player_name} vanishes into the shadows with a whisper*"
    else:
        return f"*{player_name} is affected by mysterious forces*"


async def handle_teleport_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """
    Handle the teleport command for bringing a player to the admin's location.

    Args:
        command_data: Command data dictionary containing validated command information
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Teleport command result
    """
    logger.debug(f"Processing teleport command for {player_name} with command_data: {command_data}")

    app = request.app if request else None
    if not app:
        logger.warning(f"Teleport command failed - no app context for {player_name}")
        return {"result": "Teleport functionality is not available."}

    # Get player service
    player_service = app.state.player_service if app else None
    if not player_service:
        logger.warning(f"Teleport command failed - no player service for {player_name}")
        return {"result": "Player service not available."}

    # Get current player and validate admin permissions
    current_player = player_service.get_player_by_name(player_name)
    if not current_player:
        logger.warning(f"Teleport command failed - current player not found for {player_name}")
        return {"result": "Player not found."}

    is_admin = await validate_admin_permission(current_player, player_name)
    if not is_admin:
        return {"result": "You do not have permission to use teleport commands."}

    # Extract target player from command data
    target_player_name = command_data.get("target_player")
    if not target_player_name:
        return {"result": "Usage: teleport <player_name>"}

    # Get connection manager
    connection_manager = app.state.connection_manager if app else None
    if not connection_manager:
        logger.warning(f"Teleport command failed - no connection manager for {player_name}")
        return {"result": "Connection manager not available."}

    # Find target player online
    target_player_info = await get_online_player_by_display_name(target_player_name, connection_manager)
    if not target_player_info:
        return {"result": f"Player '{target_player_name}' is not online or not found."}

    # Get target player object
    target_player = player_service.get_player_by_name(target_player_name)
    if not target_player:
        logger.warning(f"Teleport command failed - target player not found in database: {target_player_name}")
        return {"result": f"Player '{target_player_name}' not found in database."}

    # Check if target is already in the same room
    if target_player.current_room_id == current_player.current_room_id:
        return {"result": f"{target_player_name} is already in your location."}

    # Return confirmation message
    confirmation_message = (
        f"Are you sure you want to teleport {target_player_name} to your location? "
        f"Type 'confirm teleport {target_player_name}' to proceed."
    )

    logger.info(f"Teleport confirmation requested - {player_name} wants to teleport {target_player_name}")
    return {"result": confirmation_message}


async def handle_goto_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """
    Handle the goto command for moving the admin to a player's location.

    Args:
        command_data: Command data dictionary containing validated command information
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Goto command result
    """
    logger.debug(f"Processing goto command for {player_name} with command_data: {command_data}")

    app = request.app if request else None
    if not app:
        logger.warning(f"Goto command failed - no app context for {player_name}")
        return {"result": "Goto functionality is not available."}

    # Get player service
    player_service = app.state.player_service if app else None
    if not player_service:
        logger.warning(f"Goto command failed - no player service for {player_name}")
        return {"result": "Player service not available."}

    # Get current player and validate admin permissions
    current_player = player_service.get_player_by_name(player_name)
    if not current_player:
        logger.warning(f"Goto command failed - current player not found for {player_name}")
        return {"result": "Player not found."}

    is_admin = await validate_admin_permission(current_player, player_name)
    if not is_admin:
        return {"result": "You do not have permission to use goto commands."}

    # Extract target player from command data
    target_player_name = command_data.get("target_player")
    if not target_player_name:
        return {"result": "Usage: goto <player_name>"}

    # Get connection manager
    connection_manager = app.state.connection_manager if app else None
    if not connection_manager:
        logger.warning(f"Goto command failed - no connection manager for {player_name}")
        return {"result": "Connection manager not available."}

    # Find target player online
    target_player_info = await get_online_player_by_display_name(target_player_name, connection_manager)
    if not target_player_info:
        return {"result": f"Player '{target_player_name}' is not online or not found."}

    # Get target player object
    target_player = player_service.get_player_by_name(target_player_name)
    if not target_player:
        logger.warning(f"Goto command failed - target player not found in database: {target_player_name}")
        return {"result": f"Player '{target_player_name}' not found in database."}

    # Check if admin is already in the same room
    if current_player.current_room_id == target_player.current_room_id:
        return {"result": f"You are already in the same location as {target_player_name}."}

    # Return confirmation message
    confirmation_message = (
        f"Are you sure you want to teleport to {target_player_name}'s location? "
        f"Type 'confirm goto {target_player_name}' to proceed."
    )

    logger.info(f"Goto confirmation requested - {player_name} wants to goto {target_player_name}")
    return {"result": confirmation_message}


async def handle_confirm_teleport_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """
    Handle the confirm teleport command for executing the actual teleportation.

    Args:
        command_data: Command data dictionary containing validated command information
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Teleport confirmation result
    """
    logger.debug(f"Processing confirm teleport command for {player_name} with command_data: {command_data}")

    # This will be implemented in Phase 2
    # For now, return a placeholder message
    return {"result": "Teleport confirmation functionality will be implemented in Phase 2."}


async def handle_confirm_goto_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """
    Handle the confirm goto command for executing the actual teleportation.

    Args:
        command_data: Command data dictionary containing validated command information
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Goto confirmation result
    """
    logger.debug(f"Processing confirm goto command for {player_name} with command_data: {command_data}")

    # This will be implemented in Phase 2
    # For now, return a placeholder message
    return {"result": "Goto confirmation functionality will be implemented in Phase 2."}
