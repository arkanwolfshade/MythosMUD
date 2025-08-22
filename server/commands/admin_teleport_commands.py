"""
Admin teleport commands for MythosMUD.

This module contains handlers for admin teleport commands including
teleport and goto functionality with proper validation and security.
"""

from typing import Any

from ..alias_storage import AliasStorage
from ..logging.admin_actions_logger import get_admin_actions_logger
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
    try:
        if not player:
            logger.warning(f"Admin permission check failed - no player object for {player_name}")

            # Log the failed permission check
            admin_logger = get_admin_actions_logger()
            admin_logger.log_permission_check(
                player_name=player_name,
                action="admin_teleport",
                has_permission=False,
                additional_data={"error": "No player object"},
            )
            return False

        if not hasattr(player, "is_admin"):
            logger.warning(f"Admin permission check failed - player {player_name} has no is_admin attribute")

            # Log the failed permission check
            admin_logger = get_admin_actions_logger()
            admin_logger.log_permission_check(
                player_name=player_name,
                action="admin_teleport",
                has_permission=False,
                additional_data={"error": "No is_admin attribute", "player_type": type(player).__name__},
            )
            return False

        if not player.is_admin:
            logger.info(f"Admin permission denied for {player_name}")

            # Log the failed permission check
            admin_logger = get_admin_actions_logger()
            admin_logger.log_permission_check(
                player_name=player_name,
                action="admin_teleport",
                has_permission=False,
                additional_data={"player_type": type(player).__name__, "is_admin_value": player.is_admin},
            )
            return False

        # Log the successful permission check
        admin_logger = get_admin_actions_logger()
        admin_logger.log_permission_check(
            player_name=player_name,
            action="admin_teleport",
            has_permission=True,
            additional_data={"player_type": type(player).__name__, "is_admin_value": player.is_admin},
        )

        logger.debug(f"Admin permission granted for {player_name}")
        return True

    except Exception as e:
        logger.error(f"Error checking admin permissions for {player_name}: {str(e)}")

        # Log the failed permission check
        try:
            admin_logger = get_admin_actions_logger()
            admin_logger.log_permission_check(
                player_name=player_name,
                action="admin_teleport",
                has_permission=False,
                additional_data={"error": str(e), "player_type": type(player).__name__ if player else "None"},
            )
        except Exception as log_error:
            logger.error(f"Failed to log permission check error: {str(log_error)}")

        return False


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


async def broadcast_teleport_effects(
    connection_manager, player_name: str, from_room_id: str, to_room_id: str, teleport_type: str
) -> None:
    """
    Broadcast teleport visual effects to players in affected rooms.

    Args:
        connection_manager: Connection manager instance
        player_name: Name of the player being teleported
        from_room_id: Room ID the player is leaving
        to_room_id: Room ID the player is arriving at
        teleport_type: Type of teleport ('teleport' or 'goto')
    """
    try:
        # Create departure message for source room
        departure_message = create_teleport_effect_message(player_name, "departure")

        # Create arrival message for destination room
        arrival_message = create_teleport_effect_message(player_name, "arrival")

        # Broadcast departure effect to source room
        if hasattr(connection_manager, "broadcast_to_room"):
            await connection_manager.broadcast_to_room(from_room_id, departure_message, exclude_player=player_name)

        # Broadcast arrival effect to destination room
        if hasattr(connection_manager, "broadcast_to_room"):
            await connection_manager.broadcast_to_room(to_room_id, arrival_message, exclude_player=player_name)

        logger.debug(f"Teleport effects broadcast for {player_name} from {from_room_id} to {to_room_id}")

    except Exception as e:
        logger.error(f"Failed to broadcast teleport effects for {player_name}: {str(e)}")


async def notify_player_of_teleport(
    connection_manager, target_player_name: str, admin_name: str, notification_type: str
) -> None:
    """
    Notify a player that they are being teleported by an admin.

    Args:
        connection_manager: Connection manager instance
        target_player_name: Name of the player being teleported
        admin_name: Name of the admin performing the teleport
        notification_type: Type of notification ('teleported_to' or 'teleported_from')
    """
    try:
        if notification_type == "teleported_to":
            message = f"You have been teleported to {admin_name}'s location by an administrator."
        else:
            message = f"You have been teleported away from {admin_name} by an administrator."

        # Find the target player's connection and send them a direct message
        for player_id, player_info in connection_manager.online_players.items():
            if player_info.get("display_name", "").lower() == target_player_name.lower():
                # Send system notification to the target player
                if hasattr(connection_manager, "send_to_player"):
                    await connection_manager.send_to_player(player_id, message)
                break

        logger.debug(f"Teleport notification sent to {target_player_name} by {admin_name}")

    except Exception as e:
        logger.error(f"Failed to notify {target_player_name} of teleport: {str(e)}")


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

    # Store target player for confirmation
    command_data["target_player"] = target_player_name

    logger.info(f"Teleport confirmation requested - {player_name} wants to teleport {target_player_name}")
    return {
        "result": f"Are you sure you want to teleport {target_player_name} to your location? Type 'confirm teleport {target_player_name}' to proceed."
    }


async def handle_goto_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """
    Handle the goto command for teleporting the admin to a player's location.

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

    # Store target player for confirmation
    command_data["target_player"] = target_player_name

    logger.info(f"Goto confirmation requested - {player_name} wants to goto {target_player_name}")
    return {
        "result": f"Are you sure you want to teleport to {target_player_name}'s location? Type 'confirm goto {target_player_name}' to proceed."
    }


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

    app = request.app if request else None
    if not app:
        logger.warning(f"Confirm teleport command failed - no app context for {player_name}")
        return {"result": "Teleport functionality is not available."}

    # Get player service
    player_service = app.state.player_service if app else None
    if not player_service:
        logger.warning(f"Confirm teleport command failed - no player service for {player_name}")
        return {"result": "Player service not available."}

    # Get current player and validate admin permissions
    current_player = player_service.get_player_by_name(player_name)
    if not current_player:
        logger.warning(f"Confirm teleport command failed - current player not found for {player_name}")
        return {"result": "Player not found."}

    is_admin = await validate_admin_permission(current_player, player_name)
    if not is_admin:
        return {"result": "You do not have permission to use teleport commands."}

    # Extract target player from command data
    target_player_name = command_data.get("target_player")
    if not target_player_name:
        return {"result": "Usage: confirm teleport <player_name>"}

    # Get connection manager
    connection_manager = app.state.connection_manager if app else None
    if not connection_manager:
        logger.warning(f"Confirm teleport command failed - no connection manager for {player_name}")
        return {"result": "Connection manager not available."}

    # Find target player online
    target_player_info = await get_online_player_by_display_name(target_player_name, connection_manager)
    if not target_player_info:
        return {"result": f"Player '{target_player_name}' is not online or not found."}

    # Get target player object
    target_player = player_service.get_player_by_name(target_player_name)
    if not target_player:
        logger.warning(f"Confirm teleport command failed - target player not found in database: {target_player_name}")
        return {"result": f"Player '{target_player_name}' not found in database."}

    # Check if target is already in the same room
    if target_player.current_room_id == current_player.current_room_id:
        return {"result": f"{target_player_name} is already in your location."}

    # Get persistence layer
    persistence = app.state.persistence if app else None
    if not persistence:
        logger.warning(f"Confirm teleport command failed - no persistence layer for {player_name}")
        return {"result": "Persistence layer not available."}

    try:
        # Store original location for visual effects
        original_room_id = target_player.current_room_id
        target_room_id = current_player.current_room_id

        # Update target player's location
        target_player.current_room_id = target_room_id

        # Persist the change to database
        persistence.save_player(target_player)

        # Update connection manager's online player info
        if target_player_info:
            target_player_info["room_id"] = target_room_id

        # Broadcast visual effects
        await broadcast_teleport_effects(
            connection_manager, target_player_name, original_room_id, target_room_id, "teleport"
        )

        # Notify target player
        await notify_player_of_teleport(connection_manager, target_player_name, player_name, "teleported_to")

        # Log the successful teleport action
        admin_logger = get_admin_actions_logger()
        admin_logger.log_teleport_action(
            admin_name=player_name,
            target_player=target_player_name,
            action_type="teleport",
            from_room=original_room_id,
            to_room=target_room_id,
            success=True,
            additional_data={
                "admin_room_id": current_player.current_room_id,
                "target_room_id": target_player.current_room_id,
            },
        )

        logger.info(
            f"Teleport executed successfully - {player_name} teleported {target_player_name} to {target_room_id}"
        )
        return {"result": f"You have successfully teleported {target_player_name} to your location."}

    except Exception as e:
        # Log the failed teleport action
        admin_logger = get_admin_actions_logger()
        admin_logger.log_teleport_action(
            admin_name=player_name,
            target_player=target_player_name,
            action_type="teleport",
            from_room=target_player.current_room_id,
            to_room=current_player.current_room_id,
            success=False,
            error_message=str(e),
            additional_data={
                "admin_room_id": current_player.current_room_id,
                "target_room_id": target_player.current_room_id,
            },
        )

        logger.error(f"Teleport execution failed - {player_name} tried to teleport {target_player_name}: {str(e)}")
        return {"result": f"Failed to teleport {target_player_name}: {str(e)}"}


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

    app = request.app if request else None
    if not app:
        logger.warning(f"Confirm goto command failed - no app context for {player_name}")
        return {"result": "Goto functionality is not available."}

    # Get player service
    player_service = app.state.player_service if app else None
    if not player_service:
        logger.warning(f"Confirm goto command failed - no player service for {player_name}")
        return {"result": "Player service not available."}

    # Get current player and validate admin permissions
    current_player = player_service.get_player_by_name(player_name)
    if not current_player:
        logger.warning(f"Confirm goto command failed - current player not found for {player_name}")
        return {"result": "Player not found."}

    is_admin = await validate_admin_permission(current_player, player_name)
    if not is_admin:
        return {"result": "You do not have permission to use goto commands."}

    # Extract target player from command data
    target_player_name = command_data.get("target_player")
    if not target_player_name:
        return {"result": "Usage: confirm goto <player_name>"}

    # Get connection manager
    connection_manager = app.state.connection_manager if app else None
    if not connection_manager:
        logger.warning(f"Confirm goto command failed - no connection manager for {player_name}")
        return {"result": "Connection manager not available."}

    # Find target player online
    target_player_info = await get_online_player_by_display_name(target_player_name, connection_manager)
    if not target_player_info:
        return {"result": f"Player '{target_player_name}' is not online or not found."}

    # Get target player object
    target_player = player_service.get_player_by_name(target_player_name)
    if not target_player:
        logger.warning(f"Confirm goto command failed - target player not found in database: {target_player_name}")
        return {"result": f"Player '{target_player_name}' not found in database."}

    # Check if admin is already in the same room
    if current_player.current_room_id == target_player.current_room_id:
        return {"result": f"You are already in the same location as {target_player_name}."}

    # Get persistence layer
    persistence = app.state.persistence if app else None
    if not persistence:
        logger.warning(f"Confirm goto command failed - no persistence layer for {player_name}")
        return {"result": "Persistence layer not available."}

    try:
        # Store original location for visual effects
        original_room_id = current_player.current_room_id
        target_room_id = target_player.current_room_id

        # Update admin player's location
        current_player.current_room_id = target_room_id

        # Persist the change to database
        persistence.save_player(current_player)

        # Update connection manager's online player info for admin
        admin_player_info = connection_manager.online_players.get(player_name, {})
        if admin_player_info:
            admin_player_info["room_id"] = target_room_id

        # Broadcast visual effects
        await broadcast_teleport_effects(connection_manager, player_name, original_room_id, target_room_id, "goto")

        # Log the successful goto action
        admin_logger = get_admin_actions_logger()
        admin_logger.log_teleport_action(
            admin_name=player_name,
            target_player=target_player_name,
            action_type="goto",
            from_room=original_room_id,
            to_room=target_room_id,
            success=True,
            additional_data={
                "admin_room_id": current_player.current_room_id,
                "target_room_id": target_player.current_room_id,
            },
        )

        logger.info(
            f"Goto executed successfully - {player_name} teleported to {target_player_name} at {target_room_id}"
        )
        return {"result": f"You have successfully teleported to {target_player_name}'s location."}

    except Exception as e:
        # Log the failed goto action
        admin_logger = get_admin_actions_logger()
        admin_logger.log_teleport_action(
            admin_name=player_name,
            target_player=target_player_name,
            action_type="goto",
            from_room=current_player.current_room_id,
            to_room=target_player.current_room_id,
            success=False,
            error_message=str(e),
            additional_data={
                "admin_room_id": current_player.current_room_id,
                "target_room_id": target_player.current_room_id,
            },
        )

        logger.error(f"Goto execution failed - {player_name} tried to goto {target_player_name}: {str(e)}")
        return {"result": f"Failed to teleport to {target_player_name}: {str(e)}"}
