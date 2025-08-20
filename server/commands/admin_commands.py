"""
Administrative commands for MythosMUD.

This module contains handlers for administrative commands like mute, unmute, and admin management.
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
    args: list, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """
    Handle the unmute command for unmuting other players.

    Args:
        args: Command arguments
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Unmute command result
    """
    logger.debug(f"Processing unmute command for {player_name} with args: {args}")

    app = request.app if request else None
    user_manager = app.state.user_manager if app else None

    if not user_manager:
        logger.warning(f"Unmute command failed - no user manager for {player_name}")
        return {"result": "Unmute functionality is not available."}

    if len(args) < 1:
        logger.warning(f"Unmute command with insufficient arguments for {player_name}, args: {args}")
        return {"result": "Usage: unmute <player_name>"}

    target_player = args[0]

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
