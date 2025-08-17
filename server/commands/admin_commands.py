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
    elif isinstance(user_obj, dict) and "username" in user_obj:
        return user_obj["username"]
    else:
        raise ValueError("User object must have username attribute or key")


async def handle_mute_command(
    args: list, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """
    Handle the mute command for muting other players.

    Args:
        args: Command arguments
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Mute command result
    """
    logger.debug("Processing mute command", player=player_name, args=args)

    app = request.app if request else None
    user_manager = app.state.user_manager if app else None

    if not user_manager:
        logger.warning("Mute command failed - no user manager", player=player_name)
        return {"result": "Mute functionality is not available."}

    if len(args) < 1:
        logger.warning("Mute command with insufficient arguments", player=player_name, args=args)
        return {"result": "Usage: mute <player_name> [duration_in_minutes]"}

    target_player = args[0]
    duration = int(args[1]) if len(args) > 1 else None  # None means permanent

    try:
        success = user_manager.mute_player(target_player, duration, get_username_from_user(current_user))
        if success:
            duration_text = f"for {duration} minutes" if duration else "permanently"
            logger.info("Player muted successfully", player=player_name, target=target_player, duration=duration_text)
            return {"result": f"You have muted {target_player} {duration_text}."}
        else:
            logger.warning("Mute command failed", player=player_name, target=target_player)
            return {"result": f"Failed to mute {target_player}."}
    except Exception as e:
        logger.error("Mute command error", player=player_name, target=target_player, error=str(e))
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
    logger.debug("Processing unmute command", player=player_name, args=args)

    app = request.app if request else None
    user_manager = app.state.user_manager if app else None

    if not user_manager:
        logger.warning("Unmute command failed - no user manager", player=player_name)
        return {"result": "Unmute functionality is not available."}

    if len(args) < 1:
        logger.warning("Unmute command with insufficient arguments", player=player_name, args=args)
        return {"result": "Usage: unmute <player_name>"}

    target_player = args[0]

    try:
        success = user_manager.unmute_player(target_player, get_username_from_user(current_user))
        if success:
            logger.info("Player unmuted successfully", player=player_name, target=target_player)
            return {"result": f"You have unmuted {target_player}."}
        else:
            logger.warning("Unmute command failed", player=player_name, target=target_player)
            return {"result": f"Failed to unmute {target_player}."}
    except Exception as e:
        logger.error("Unmute command error", player=player_name, target=target_player, error=str(e))
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
    logger.debug("Processing mute_global command", player=player_name, args=args)

    app = request.app if request else None
    user_manager = app.state.user_manager if app else None

    if not user_manager:
        logger.warning("Mute global command failed - no user manager", player=player_name)
        return {"result": "Global mute functionality is not available."}

    try:
        success = user_manager.mute_global(get_username_from_user(current_user))
        if success:
            logger.info("Global mute activated", player=player_name)
            return {"result": "Global mute has been activated."}
        else:
            logger.warning("Global mute command failed", player=player_name)
            return {"result": "Failed to activate global mute."}
    except Exception as e:
        logger.error("Global mute command error", player=player_name, error=str(e))
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
    logger.debug("Processing unmute_global command", player=player_name, args=args)

    app = request.app if request else None
    user_manager = app.state.user_manager if app else None

    if not user_manager:
        logger.warning("Unmute global command failed - no user manager", player=player_name)
        return {"result": "Global unmute functionality is not available."}

    try:
        success = user_manager.unmute_global(get_username_from_user(current_user))
        if success:
            logger.info("Global mute deactivated", player=player_name)
            return {"result": "Global mute has been deactivated."}
        else:
            logger.warning("Global unmute command failed", player=player_name)
            return {"result": "Failed to deactivate global mute."}
    except Exception as e:
        logger.error("Global unmute command error", player=player_name, error=str(e))
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
    logger.debug("Processing add_admin command", player=player_name, args=args)

    app = request.app if request else None
    user_manager = app.state.user_manager if app else None

    if not user_manager:
        logger.warning("Add admin command failed - no user manager", player=player_name)
        return {"result": "Admin management is not available."}

    if len(args) < 1:
        logger.warning("Add admin command with insufficient arguments", player=player_name, args=args)
        return {"result": "Usage: add_admin <player_name>"}

    target_player = args[0]

    try:
        success = user_manager.add_admin(target_player, get_username_from_user(current_user))
        if success:
            logger.info("Admin added successfully", player=player_name, target=target_player)
            return {"result": f"{target_player} has been granted administrator privileges."}
        else:
            logger.warning("Add admin command failed", player=player_name, target=target_player)
            return {"result": f"Failed to grant administrator privileges to {target_player}."}
    except Exception as e:
        logger.error("Add admin command error", player=player_name, target=target_player, error=str(e))
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
    logger.debug("Processing mutes command", player=player_name, args=args)

    app = request.app if request else None
    user_manager = app.state.user_manager if app else None

    if not user_manager:
        logger.warning("Mutes command failed - no user manager", player=player_name)
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
            logger.debug("Mutes listed successfully", player=player_name, count=len(mutes))
            return {"result": result}
        else:
            logger.debug("No mutes found", player=player_name)
            return {"result": "No active mutes found."}
    except Exception as e:
        logger.error("Mutes command error", player=player_name, error=str(e))
        return {"result": f"Error retrieving mute information: {str(e)}"}
