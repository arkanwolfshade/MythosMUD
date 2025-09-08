"""
Administrative commands for MythosMUD.

This module contains handlers for administrative commands including:
- Mute/unmute functionality
- Admin management
- Teleport and goto functionality with proper validation and security
"""

from typing import Any

from ..alias_storage import AliasStorage
from ..logging.admin_actions_logger import get_admin_actions_logger
from ..logging_config import get_logger
from ..realtime.websocket_handler import broadcast_room_update
from ..utils.command_parser import get_username_from_user

logger = get_logger(__name__)


# --- Admin Permission Validation ---


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

        # Check if player has admin privileges
        if not hasattr(player, "is_admin") or not player.is_admin:
            # Determine the specific reason for failure
            if not hasattr(player, "is_admin"):
                error_msg = "No is_admin attribute"
                logger.warning(f"Admin permission check failed - player {player_name} has no is_admin attribute")
                additional_data = {"error": error_msg, "player_type": type(player).__name__}
            else:
                error_msg = f"is_admin value: {player.is_admin}"
                logger.info(f"Admin permission denied for {player_name} - {error_msg}")
                additional_data = {"player_type": type(player).__name__, "is_admin_value": player.is_admin}

            # Log the failed permission check
            admin_logger = get_admin_actions_logger()
            admin_logger.log_permission_check(
                player_name=player_name,
                action="admin_teleport",
                has_permission=False,
                additional_data=additional_data,
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

        logger.info(f"Admin permission granted for {player_name} - is_admin value: {player.is_admin}")
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


# --- Teleport Utility Functions ---


async def get_online_player_by_display_name(display_name: str, connection_manager) -> dict | None:
    """
    Get online player information by display name.

    Args:
        display_name: Display name to search for
        connection_manager: Connection manager instance

    Returns:
        dict: Player information if found, None otherwise
    """
    if not connection_manager:
        logger.warning("Connection manager not available for online player lookup")
        return None

    return connection_manager.get_online_player_by_display_name(display_name)


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

        # Broadcast teleport effects to rooms
        if hasattr(connection_manager, "broadcast_to_room"):
            # Broadcast departure effect to source room
            await connection_manager.broadcast_to_room(from_room_id, departure_message, exclude_player=player_name)
            # Broadcast arrival effect to destination room
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
        target_player_info = connection_manager.get_online_player_by_display_name(target_player_name)
        if target_player_info:
            player_id = target_player_info.get("player_id")
            if player_id and hasattr(connection_manager, "send_to_player"):
                await connection_manager.send_to_player(player_id, message)

        logger.debug(f"Teleport notification sent to {target_player_name} by {admin_name}")

    except Exception as e:
        logger.error(f"Failed to notify {target_player_name} of teleport: {str(e)}")


# --- Mute Command Handlers ---


async def handle_mute_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """
    Handle the mute command for muting other players.

    Args:
        command_data: Command data dictionary containing validated command information
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Mute command result
    """
    logger.debug(f"Processing mute command for {player_name} with command_data: {command_data}")

    app = request.app if request else None
    user_manager = app.state.user_manager if app else None

    if not user_manager:
        logger.warning(f"Mute command failed - no user manager for {player_name}")
        return {"result": "Mute functionality is not available."}

    # Extract target player and duration from command_data
    # For now, the target player might be in different fields - let's check
    target_player = command_data.get("target_player") or command_data.get("target_name")
    duration_minutes = command_data.get("duration_minutes")

    if not target_player:
        # If target player is not in command_data, this is a validation issue
        logger.warning(f"Mute command with no target player for {player_name}, command_data: {command_data}")
        return {"result": "Usage: mute <player_name> [duration_in_minutes]"}

    duration = int(duration_minutes) if duration_minutes else None  # None means permanent

    try:
        # Get current user ID and name
        current_user_id = get_username_from_user(current_user)

        # Get player service from app state
        player_service = app.state.player_service if app else None
        if not player_service:
            return {"result": "Player service not available."}

        # Resolve target player name to Player object
        target_player_obj = player_service.resolve_player_name(target_player)
        if not target_player_obj:
            return {"result": f"Player '{target_player}' not found."}

        success = user_manager.mute_player(
            muter_id=current_user_id,
            muter_name=player_name,
            target_id=target_player_obj.id,
            target_name=target_player,
            duration_minutes=duration,
            reason="",
        )
        if success:
            duration_text = f"for {duration} minutes" if duration else "permanently"
            logger.info(f"Player muted successfully - {player_name} muted {target_player} for {duration_text}")
            return {"result": f"You have muted {target_player} {duration_text}."}
        else:
            logger.warning(f"Mute command failed - {player_name} tried to mute {target_player}")
            return {"result": f"Failed to mute {target_player}."}
    except Exception as e:
        logger.error(f"Mute command error - {player_name} tried to mute {target_player}: {str(e)}")
        return {"result": f"Error muting {target_player}: {str(e)}"}


async def handle_unmute_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """
    Handle the unmute command for unmuting other players.

    Args:
        command_data: Command data dictionary containing validated command information
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Unmute command result
    """
    logger.debug(f"Processing unmute command for {player_name} with command_data: {command_data}")

    app = request.app if request else None
    user_manager = app.state.user_manager if app else None

    if not user_manager:
        logger.warning(f"Unmute command failed - no user manager for {player_name}")
        return {"result": "Unmute functionality is not available."}

    # Extract target player from command_data
    target_player = command_data.get("target_player")

    if not target_player:
        # If target player is not in command_data, this is a validation issue
        logger.warning(f"Unmute command with no target player for {player_name}, command_data: {command_data}")
        return {"result": "Usage: unmute <player_name>"}

    try:
        # Get current user ID and name
        current_user_id = get_username_from_user(current_user)

        # Get player service from app state
        player_service = app.state.player_service if app else None
        if not player_service:
            return {"result": "Player service not available."}

        # Resolve target player name to Player object
        target_player_obj = player_service.resolve_player_name(target_player)
        if not target_player_obj:
            return {"result": f"Player '{target_player}' not found."}

        success = user_manager.unmute_player(
            unmuter_id=current_user_id,
            unmuter_name=player_name,
            target_id=target_player_obj.id,
            target_name=target_player,
        )
        if success:
            logger.info(f"Player unmuted successfully - {player_name} unmuted {target_player}")
            return {"result": f"You have unmuted {target_player}."}
        else:
            logger.warning(f"Unmute command failed - {player_name} tried to unmute {target_player}")
            return {"result": f"Failed to unmute {target_player}."}
    except Exception as e:
        logger.error(f"Unmute command error - {player_name} tried to unmute {target_player}: {str(e)}")
        return {"result": f"Error unmuting {target_player}: {str(e)}"}


async def handle_mute_global_command(
    args: list, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """
    Handle the mute_global command for global muting.

    Args:
        args: Command arguments
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Mute global command result
    """
    logger.debug(f"Processing mute_global command for {player_name} with args: {args}")

    app = request.app if request else None
    user_manager = app.state.user_manager if app else None

    if not user_manager:
        logger.warning(f"Mute global command failed - no user manager for {player_name}")
        return {"result": "Global mute functionality is not available."}

    try:
        success = user_manager.mute_global(get_username_from_user(current_user))
        if success:
            logger.info(f"Global mute activated by {player_name}")
            return {"result": "Global mute has been activated."}
        else:
            logger.warning(f"Global mute command failed for {player_name}")
            return {"result": "Failed to activate global mute."}
    except Exception as e:
        logger.error(f"Global mute command error for {player_name}: {str(e)}")
        return {"result": f"Error activating global mute: {str(e)}"}


async def handle_unmute_global_command(
    args: list, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """
    Handle the unmute_global command for removing global mute.

    Args:
        args: Command arguments
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Unmute global command result
    """
    logger.debug(f"Processing unmute_global command for {player_name} with args: {args}")

    app = request.app if request else None
    user_manager = app.state.user_manager if app else None

    if not user_manager:
        logger.warning(f"Unmute global command failed - no user manager for {player_name}")
        return {"result": "Global unmute functionality is not available."}

    try:
        success = user_manager.unmute_global(get_username_from_user(current_user))
        if success:
            logger.info(f"Global mute deactivated by {player_name}")
            return {"result": "Global mute has been deactivated."}
        else:
            logger.warning(f"Global unmute command failed for {player_name}")
            return {"result": "Failed to deactivate global mute."}
    except Exception as e:
        logger.error(f"Global unmute command error for {player_name}: {str(e)}")
        return {"result": f"Error deactivating global mute: {str(e)}"}


async def handle_add_admin_command(
    args: list, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """
    Handle the add_admin command for adding administrators.

    Args:
        args: Command arguments
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Add admin command result
    """
    logger.debug(f"Processing add_admin command for {player_name} with args: {args}")

    app = request.app if request else None
    user_manager = app.state.user_manager if app else None

    if not user_manager:
        logger.warning(f"Add admin command failed - no user manager for {player_name}")
        return {"result": "Admin management is not available."}

    if len(args) < 1:
        logger.warning(f"Add admin command with insufficient arguments for {player_name}, args: {args}")
        return {"result": "Usage: add_admin <player_name>"}

    target_player = args[0]

    try:
        success = user_manager.add_admin(target_player, get_username_from_user(current_user))
        if success:
            logger.info(f"Admin added successfully - {player_name} added {target_player}")
            return {"result": f"{target_player} has been granted administrator privileges."}
        else:
            logger.warning(f"Add admin command failed - {player_name} tried to add {target_player}")
            return {"result": f"Failed to grant administrator privileges to {target_player}."}
    except Exception as e:
        logger.error(f"Add admin command error - {player_name} tried to add {target_player}: {str(e)}")
        return {"result": f"Error granting administrator privileges: {str(e)}"}


async def handle_mutes_command(
    args: list, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """
    Handle the mutes command for listing current mutes.

    Args:
        args: Command arguments
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Mutes command result
    """
    logger.debug(f"Processing mutes command for {player_name} with args: {args}")

    app = request.app if request else None
    user_manager = app.state.user_manager if app else None

    if not user_manager:
        logger.warning(f"Mutes command failed - no user manager for {player_name}")
        return {"result": "Mute information is not available."}

    try:
        mutes = user_manager.get_player_mutes(get_username_from_user(current_user))
        if mutes:
            mute_list = []
            for mute in mutes:
                if mute.get("expires_at"):
                    mute_list.append(f"{mute['target_player']} (expires: {mute['expires_at']})")
                else:
                    mute_list.append(f"{mute['target_player']} (permanent)")

            result = "Current mutes:\n" + "\n".join(mute_list)
            logger.debug(f"Mutes listed successfully for {player_name}, count: {len(mutes)}")
            return {"result": result}
        else:
            logger.debug(f"No mutes found for {player_name}")
            return {"result": "No active mutes found."}
    except Exception as e:
        logger.error(f"Mutes command error for {player_name}: {str(e)}")
        return {"result": f"Error retrieving mute information: {str(e)}"}


# --- Teleport Command Handlers ---


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

    try:
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

        # TODO: Add confirmation dialog as future feature for enhanced safety
        # For now, execute teleport immediately for testing and development

        try:
            # Store original location for visual effects
            original_room_id = target_player.current_room_id
            target_room_id = current_player.current_room_id

            # Update target player's location using PlayerService
            success = player_service.update_player_location(target_player_name, target_room_id)
            if not success:
                logger.error(f"Failed to update target player location: {target_player_name}")
                return {"result": f"Failed to teleport {target_player_name}: database update failed."}

            # Update connection manager's online player info
            if target_player_info:
                target_player_info["room_id"] = target_room_id

            # Broadcast room update to the teleported player
            await broadcast_room_update(target_player_info["player_id"], target_room_id)

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
    except Exception as e:
        logger.error(f"Exception in teleport command handler: {str(e)}", exc_info=True)
        return {"result": f"Error processing teleport command: {str(e)}"}


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

    # Execute goto immediately without confirmation
    try:
        # Store original location for visual effects
        original_room_id = current_player.current_room_id
        target_room_id = target_player.current_room_id

        # Update admin player's location using PlayerService
        success = player_service.update_player_location(player_name, target_room_id)
        if not success:
            logger.error(f"Failed to update admin player location: {player_name}")
            return {"result": f"Failed to teleport to {target_player_name}: database update failed."}

        # Update connection manager's online player info for admin
        admin_player_info = connection_manager.get_online_player_by_display_name(player_name)
        if admin_player_info:
            admin_player_info["room_id"] = target_room_id

        # Broadcast room update to the admin player
        await broadcast_room_update(admin_player_info["player_id"], target_room_id)

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

    try:
        # Store original location for visual effects
        original_room_id = target_player.current_room_id
        target_room_id = current_player.current_room_id

        # Update target player's location using PlayerService
        success = player_service.update_player_location(target_player_name, target_room_id)
        if not success:
            logger.error(f"Failed to update target player location: {target_player_name}")
            return {"result": f"Failed to teleport {target_player_name}: database update failed."}

        # Update connection manager's online player info
        if target_player_info:
            target_player_info["room_id"] = target_room_id

        # Broadcast room update to the teleported player
        await broadcast_room_update(target_player_info["player_id"], target_room_id)

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

    try:
        # Store original location for visual effects
        original_room_id = current_player.current_room_id
        target_room_id = target_player.current_room_id

        # Update admin player's location using PlayerService
        success = player_service.update_player_location(player_name, target_room_id)
        if not success:
            logger.error(f"Failed to update admin player location: {player_name}")
            return {"result": f"Failed to teleport to {target_player_name}: database update failed."}

        # Update connection manager's online player info for admin
        admin_player_info = connection_manager.get_online_player_by_display_name(player_name)
        if admin_player_info:
            admin_player_info["room_id"] = target_room_id

        # Broadcast room update to the admin player
        await broadcast_room_update(admin_player_info["player_id"], target_room_id)

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
