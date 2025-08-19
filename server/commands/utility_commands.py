"""
Utility commands for MythosMUD.

This module contains handlers for utility commands like who, quit, and other system utilities.
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


async def handle_who_command(
    args: list, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """
    Handle the who command for listing online players.

    Args:
        args: Command arguments
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Who command result
    """
    logger.debug("Processing who command", player=player_name, args=args)

    app = request.app if request else None
    persistence = app.state.persistence if app else None

    if not persistence:
        logger.warning("Who command failed - no persistence layer", player=player_name)
        return {"result": "Player information is not available."}

    try:
        players = persistence.list_players()
        if players:
            # Filter to only show online players (those with recent activity)
            from datetime import datetime, timedelta

            now = datetime.utcnow()
            online_threshold = now - timedelta(minutes=5)  # Consider players online if active in last 5 minutes

            online_players = []
            for player in players:
                if player.last_active and player.last_active > online_threshold:
                    online_players.append(player.username)

            if online_players:
                player_list = ", ".join(sorted(online_players))
                result = f"Online players ({len(online_players)}): {player_list}"
                logger.debug("Who command successful", player=player_name, count=len(online_players))
                return {"result": result}
            else:
                logger.debug("No online players found", player=player_name)
                return {"result": "No players are currently online."}
        else:
            logger.debug("No players found", player=player_name)
            return {"result": "No players found."}
    except Exception as e:
        logger.error("Who command error", player=player_name, error=str(e))
        return {"result": f"Error retrieving player information: {str(e)}"}


async def handle_quit_command(
    args: list, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """
    Handle the quit command for disconnecting from the game.

    Args:
        args: Command arguments
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Quit command result
    """
    logger.debug("Processing quit command", player=player_name, args=args)

    # Update last active timestamp before quitting
    app = request.app if request else None
    persistence = app.state.persistence if app else None

    if persistence:
        try:
            player = persistence.get_player_by_name(get_username_from_user(current_user))
            if player:
                from datetime import datetime

                player.last_active = datetime.utcnow()
                persistence.save_player(player)
                logger.info("Player quit - updated last active", player=player_name)
        except Exception as e:
            logger.error("Error updating last active on quit", player=player_name, error=str(e))

    logger.info("Player quitting", player=player_name)
    return {"result": "Goodbye! You have been disconnected from the game."}


async def handle_status_command(
    args: list, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """
    Handle the status command for showing player status.

    Args:
        args: Command arguments
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Status command result
    """
    logger.debug("Processing status command", player=player_name, args=args)

    app = request.app if request else None
    persistence = app.state.persistence if app else None

    if not persistence:
        logger.warning("Status command failed - no persistence layer", player=player_name)
        return {"result": "Status information is not available."}

    try:
        player = persistence.get_player_by_name(get_username_from_user(current_user))
        if not player:
            logger.warning("Status command failed - player not found", player=player_name)
            return {"result": "Player information not found."}

        # Get current room information
        room = persistence.get_room(player.current_room_id) if player.current_room_id else None
        room_name = room.name if room else "Unknown location"

        # Build status information
        status_lines = [
            f"Name: {player.username}",
            f"Location: {room_name}",
            f"Health: {player.stats.health}/{player.stats.max_health}",
            f"Sanity: {player.stats.sanity}/{player.stats.max_sanity}",
        ]

        # Add additional stats if available
        if hasattr(player.stats, "fear") and player.stats.fear > 0:
            status_lines.append(f"Fear: {player.stats.fear}")

        if hasattr(player.stats, "corruption") and player.stats.corruption > 0:
            status_lines.append(f"Corruption: {player.stats.corruption}")

        if hasattr(player.stats, "occult_knowledge") and player.stats.occult_knowledge > 0:
            status_lines.append(f"Occult Knowledge: {player.stats.occult_knowledge}")

        # Add pose if set
        if player.pose:
            status_lines.append(f"Pose: {player.pose}")

        result = "\n".join(status_lines)
        logger.debug("Status command successful", player=player_name)
        return {"result": result}
    except Exception as e:
        logger.error("Status command error", player=player_name, error=str(e))
        return {"result": f"Error retrieving status information: {str(e)}"}


async def handle_inventory_command(
    args: list, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """
    Handle the inventory command for showing player inventory.

    Args:
        args: Command arguments
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Inventory command result
    """
    logger.debug("Processing inventory command", player=player_name, args=args)

    app = request.app if request else None
    persistence = app.state.persistence if app else None

    if not persistence:
        logger.warning("Inventory command failed - no persistence layer", player=player_name)
        return {"result": "Inventory information is not available."}

    try:
        player = persistence.get_player_by_name(get_username_from_user(current_user))
        if not player:
            logger.warning("Inventory command failed - player not found", player=player_name)
            return {"result": "Player information not found."}

        if player.inventory:
            item_list = []
            for item in player.inventory:
                item_desc = f"{item.name}"
                if hasattr(item, "description"):
                    description = item.description if item.description else "No description"
                    item_desc += f" - {description}"
                else:
                    item_desc += " - No description"
                item_list.append(item_desc)

            result = "You are carrying:\n" + "\n".join(item_list)
            logger.debug("Inventory command successful", player=player_name, count=len(player.inventory))
            return {"result": result}
        else:
            logger.debug("Empty inventory", player=player_name)
            return {"result": "You are not carrying anything."}
    except Exception as e:
        logger.error("Inventory command error", player=player_name, error=str(e))
        return {"result": f"Error retrieving inventory: {str(e)}"}


async def handle_emote_command(
    args: list, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """
    Handle the emote command for performing emotes.

    Args:
        args: Command arguments
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Emote command result
    """
    logger.debug("Processing emote command", player=player_name, args=args)

    if not args:
        logger.warning("Emote command with no action", player=player_name)
        return {"result": "Emote what? Usage: emote <action>"}

    action = " ".join(args)
    logger.debug("Player performing emote", player=player_name, action=action)

    # For now, return a simple response
    # In a full implementation, this would broadcast to other players in the room
    return {"result": f"{player_name} {action}"}
