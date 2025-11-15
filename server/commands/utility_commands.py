"""
Utility commands for MythosMUD.

This module contains handlers for utility commands like who, quit, and other system utilities.
"""

from typing import Any

from ..alias_storage import AliasStorage
from ..logging.enhanced_logging_config import get_logger
from ..utils.command_parser import get_username_from_user
from ..utils.player_cache import cache_player, get_cached_player

logger = get_logger(__name__)


def filter_players_by_name(players: list, filter_term: str) -> list:
    """
    Filter players by case-insensitive partial name matching.

    Args:
        players: List of player objects
        filter_term: Search term

    Returns:
        list: Filtered player list
    """
    if not filter_term:
        return players

    filter_lower = filter_term.lower()
    return [player for player in players if filter_lower in player.name.lower()]


def format_player_location(room_id: str) -> str:
    """
    Format player location as Zone: Sub-zone: Room from room ID.

    Args:
        room_id: Room ID in format earth_arkhamcity_northside_intersection_derby_high

    Returns:
        str: Formatted location string
    """
    # Defensive check: ensure room_id is a valid string
    if not room_id or not isinstance(room_id, str):
        logger.warning("Invalid room_id provided", room_id=room_id, room_id_type=type(room_id).__name__)
        return "Unknown Location"

    try:
        # Parse room ID: earth_arkhamcity_northside_intersection_derby_high
        parts = room_id.split("_")
        if len(parts) >= 4:
            # Extract zone and sub-zone
            zone = parts[1]  # arkhamcity
            sub_zone = parts[2]  # northside
            room_name = "_".join(parts[3:])  # intersection_derby_high

            # Convert to readable format
            zone_display = zone.replace("_", " ").title()
            sub_zone_display = sub_zone.replace("_", " ").title()
            room_display = room_name.replace("_", " ").title()

            return f"{zone_display}: {sub_zone_display}: {room_display}"
        else:
            # Fallback for unexpected format
            return room_id.replace("_", " ").title()
    except (ValueError, TypeError, AttributeError) as e:
        logger.error("Error parsing room ID", room_id=room_id, error=str(e), error_type=type(e).__name__)
        # Safe fallback that doesn't depend on room_id being a valid string
        return "Unknown Location"


def format_player_entry(player) -> str:
    """
    Format a single player entry for the who command output.

    Args:
        player: Player object

    Returns:
        str: Formatted player entry
    """
    try:
        # Base format: PlayerName [Level] - Location
        location = format_player_location(player.current_room_id)
        base_entry = f"{player.name} [{player.level}] - {location}"
    except Exception as e:
        logger.error("Error formatting player entry", player_name=player.name, error=str(e))
        # Fallback formatting
        location = "Unknown location"
        base_entry = f"{player.name} [{player.level}] - {location}"

    # Add admin indicator if player is admin
    if player.is_admin:
        base_entry = f"{player.name} [{player.level}] [ADMIN] - {location}"

    return base_entry


async def handle_who_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage | None, player_name: str
) -> dict[str, str]:
    """
    Handle the who command for listing online players.

    Args:
        command_data: Command data dictionary containing validated command information
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Who command result
    """
    logger.debug("Processing who command", player=player_name)

    # Extract filter term from command_data (use target_player for consistency with command service)
    filter_term = command_data.get("target_player", "")

    app = request.app if request else None
    persistence = app.state.persistence if app else None

    if not persistence:
        logger.warning("Who command failed - no persistence layer")
        return {"result": "Player information is not available."}

    try:
        players = persistence.list_players()
        if players:
            # Filter to only show online players (those with recent activity)
            from datetime import UTC, datetime, timedelta

            now = datetime.now(UTC)
            online_threshold = now - timedelta(minutes=5)  # Consider players online if active in last 5 minutes

            online_players = []
            logger.debug("Who command - checking players", player_count=len(players), threshold=online_threshold)

            # Pre-compile regex for better performance (if needed for string parsing)

            for player in players:
                # Ensure last_active is a datetime object for comparison
                if player.last_active:
                    last_active = None

                    # Handle case where last_active might be a string
                    if isinstance(player.last_active, str):
                        try:
                            # Optimized string parsing - handle common formats more efficiently
                            last_active_str = player.last_active.strip()
                            if last_active_str.endswith("Z"):
                                # Handle UTC format
                                last_active = datetime.fromisoformat(last_active_str[:-1] + "+00:00")
                            elif "+" in last_active_str or "-" in last_active_str[-6:]:
                                # Handle timezone format
                                last_active = datetime.fromisoformat(last_active_str)
                            else:
                                # Assume UTC if no timezone info
                                last_active = datetime.fromisoformat(last_active_str).replace(tzinfo=UTC)
                        except (ValueError, AttributeError) as e:
                            logger.warning("Failed to parse last_active string", player_name=player.name, error=str(e))
                            # Skip players with invalid last_active data
                            continue
                    else:
                        last_active = player.last_active
                        # Ensure both datetimes are timezone-aware for comparison
                        if last_active and last_active.tzinfo is None:
                            # Make naive datetime timezone-aware
                            last_active = last_active.replace(tzinfo=UTC)

                    if last_active and last_active > online_threshold:
                        online_players.append(player)
                else:
                    logger.debug("Player has no last_active timestamp", player_name=player.name)

            logger.debug(
                "Who command - found online players", online_count=len(online_players), total_count=len(players)
            )

            if online_players:
                # Apply name filtering if provided
                if filter_term:
                    filtered_players = filter_players_by_name(online_players, filter_term)
                    if filtered_players:
                        # Optimize sorting by using a more efficient key function
                        sorted_players = sorted(filtered_players, key=lambda p: p.name.lower())

                        # Optimize formatting by batching the operations
                        player_entries = []
                        for player in sorted_players:
                            player_entries.append(format_player_entry(player))

                        player_list = ", ".join(player_entries)
                        result = f"Players matching '{filter_term}' ({len(filtered_players)}): {player_list}"
                        logger.debug(
                            "Who command successful with filter",
                            player=player_name,
                            filter=filter_term,
                            count=len(filtered_players),
                        )
                        return {"result": result}
                    else:
                        # No matches found
                        result = f"No players found matching '{filter_term}'. Try 'who' to see all online players."
                        logger.debug(
                            "Who command - no matches for filter",
                            player=player_name,
                            filter=filter_term,
                        )
                        return {"result": result}
                else:
                    # No filter - show all online players
                    # Optimize sorting by using a more efficient key function
                    sorted_players = sorted(online_players, key=lambda p: p.name.lower())

                    # Optimize formatting by batching the operations
                    player_entries = []
                    for player in sorted_players:
                        player_entries.append(format_player_entry(player))

                    player_list = ", ".join(player_entries)
                    result = f"Online Players ({len(online_players)}): {player_list}"
                    logger.debug("Who command successful", player=player_name, count=len(online_players))
                    return {"result": result}
            else:
                logger.debug("No online players found", player=player_name)
                return {"result": "No players are currently online."}
        else:
            logger.debug("No players found in database", player=player_name)
            return {"result": "No players found."}
    except Exception as e:
        logger.error(
            "Who command error",
            player=player_name,
            command_data=command_data,
            error_type=type(e).__name__,
            error_message=str(e),
            exc_info=True,
        )
        return {"result": f"Error retrieving player list: {str(e)}"}


async def handle_quit_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage | None, player_name: str
) -> dict[str, str]:
    """
    Handle the quit command for disconnecting from the game.

    Args:
        command_data: Command data dictionary containing args and other info
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Quit command result
    """
    # Extract args from command_data (not used in this command)
    _args: list = command_data.get("args", [])

    logger.debug("Processing quit command")

    # Update last active timestamp before quitting
    app = request.app if request else None
    persistence = app.state.persistence if app else None

    if persistence:
        try:
            player = persistence.get_player_by_name(get_username_from_user(current_user))
            if player:
                from datetime import UTC, datetime

                player.last_active = datetime.now(UTC)
                persistence.save_player(player)
                logger.info("Player quit - updated last active")
        except (OSError, ValueError, TypeError, Exception) as e:
            logger.error("Error updating last active on quit", error=str(e), error_type=type(e).__name__)

    logger.info("Player quitting")
    return {"result": "Goodbye! You have been disconnected from the game."}


async def handle_logout_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage | None, player_name: str
) -> dict[str, Any]:
    """
    Handle the logout command for cleanly disconnecting from the game.

    This command performs a complete logout process including:
    - Updating player's last active timestamp
    - Cleaning up server-side session data
    - Disconnecting all connections
    - Returning success confirmation

    Args:
        command_data: Command data dictionary containing args and other info
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Logout command result with success status and metadata
    """
    # Extract args from command_data (not used in this command)
    _args: list = command_data.get("args", [])

    logger.debug("Processing logout command")

    try:
        # Update last active timestamp before logout
        app = request.app if request else None
        persistence = app.state.persistence if app else None

        connection_manager = app.state.connection_manager if app else None

        lookup_name = player_name or get_username_from_user(current_user)
        player = get_cached_player(request, lookup_name)

        if persistence and player is None:
            try:
                player = persistence.get_player_by_name(lookup_name)
                cache_player(request, lookup_name, player)
            except Exception as e:
                logger.error("Error updating last active on logout", error=str(e), error_type=type(e).__name__)
                player = None

        if player:
            # Synchronize current position from in-memory presence tracking
            position_value: str | None = None
            player_identifier = getattr(player, "player_id", None)
            if connection_manager:
                player_info = None
                if player_identifier:
                    player_info = connection_manager.online_players.get(str(player_identifier))
                if not player_info:
                    player_info = connection_manager.get_online_player_by_display_name(player_name)
                if player_info:
                    position_value = player_info.get("position")

            if position_value:
                stats = player.get_stats()
                if stats.get("position") != position_value:
                    stats["position"] = position_value
                    player.set_stats(stats)

            if persistence:
                from datetime import UTC, datetime

                player.last_active = datetime.now(UTC)
                persistence.save_player(player)
                logger.info("Player logout - updated last active")

        # Disconnect player from all connections
        try:
            if connection_manager:
                await connection_manager.force_disconnect_player(player_name)
                logger.info("Player disconnected from all connections")
            else:
                logger.warning("Connection manager not available for logout")
        except (AttributeError, RuntimeError) as e:
            logger.error("Error disconnecting player", error=str(e), error_type=type(e).__name__)

        logger.info("Player logged out successfully")

        return {
            "result": "Logged out successfully",
            "session_terminated": True,
            "connections_closed": True,
            "message": "You have been logged out and disconnected from the game.",
        }

    except Exception as e:
        logger.error("Unexpected error during logout", error=str(e), error_type=type(e).__name__, exc_info=True)

        # Even if there's an error, we should still indicate logout success
        # The client will handle the cleanup
        return {
            "result": "Logged out successfully",
            "session_terminated": True,
            "connections_closed": True,
            "message": "You have been logged out from the game.",
        }


async def handle_status_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage | None, player_name: str
) -> dict[str, str]:
    """
    Handle the status command for showing player status.

    Args:
        command_data: Command data dictionary containing args and other info
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Status command result
    """
    # Extract args from command_data (not used in this command)
    _args: list = command_data.get("args", [])

    logger.debug("Processing status command")

    app = request.app if request else None
    persistence = app.state.persistence if app else None

    if not persistence:
        logger.warning("Status command failed - no persistence layer")
        return {"result": "Status information is not available."}

    try:
        player = persistence.get_player_by_name(get_username_from_user(current_user))
        if not player:
            logger.warning("Status command failed - player not found")
            return {"result": "Player information not found."}

        # Get current room information
        room = persistence.get_room(player.current_room_id) if player.current_room_id else None
        room_name = room.name if room else "Unknown location"

        # Get player stats as dictionary
        stats = player.get_stats()

        # Get profession information following the same pattern as PlayerService._convert_player_to_schema
        profession_id = 0
        profession_name = None
        profession_description = None
        profession_flavor_text = None

        if hasattr(player, "profession_id"):
            profession_id = player.profession_id
        elif isinstance(player, dict):
            profession_id = player.get("profession_id", 0)

        # Fetch profession details from persistence
        if profession_id is not None:
            try:
                profession = persistence.get_profession_by_id(profession_id)
                if profession:
                    profession_name = profession.name
                    profession_description = profession.description
                    profession_flavor_text = profession.flavor_text
            except Exception as e:
                logger.warning("Failed to fetch profession", profession_id=profession_id, error=str(e))

        # Check if player is in combat
        combat_service = app.state.combat_service if app else None
        in_combat = False
        if combat_service:
            logger.debug("Checking combat status for player", player_id=player.player_id)
            combat = await combat_service.get_combat_by_participant(player.player_id)
            logger.debug("Combat result for player", player_id=player.player_id, combat=combat)
            in_combat = combat is not None
            logger.debug("Player combat status", player_id=player.player_id, in_combat=in_combat)
        else:
            logger.debug("No combat service available")

        # Determine current posture
        position_value = str(stats.get("position", "standing")).lower()
        position_label = position_value.replace("_", " ").capitalize()

        # Build status information
        status_lines = [
            f"Name: {player.name}",
            f"Location: {room_name}",
            f"Position: {position_label}",
            f"Health: {stats.get('current_health', 100)}/{stats.get('max_health', 100)}",
            f"Sanity: {stats.get('sanity', 100)}/{stats.get('max_sanity', 100)}",
            f"XP: {player.experience_points}",
            f"In Combat: {'Yes' if in_combat else 'No'}",
        ]

        # Add profession information if available
        if profession_name:
            status_lines.append(f"Profession: {profession_name}")
            if profession_description:
                status_lines.append(f"Description: {profession_description}")
            if profession_flavor_text:
                status_lines.append(f"Background: {profession_flavor_text}")

        # Add additional stats if available
        if stats.get("fear", 0) > 0:
            status_lines.append(f"Fear: {stats.get('fear', 0)}")

        if stats.get("corruption", 0) > 0:
            status_lines.append(f"Corruption: {stats.get('corruption', 0)}")

        if stats.get("occult_knowledge", 0) > 0:
            status_lines.append(f"Occult Knowledge: {stats.get('occult_knowledge', 0)}")

        result = "\n".join(status_lines)
        logger.debug("Status command successful")
        return {"result": result}
    except Exception as e:
        logger.error("Status command error")
        return {"result": f"Error retrieving status information: {str(e)}"}


async def handle_whoami_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage | None, player_name: str
) -> dict[str, str]:
    """
    Handle the whoami command as an alias for status.

    Mirrors handle_status_command while providing additional logging context.
    """
    logger.debug("Processing whoami command as status alias", player=player_name)

    result = await handle_status_command(command_data, current_user, request, alias_storage, player_name)
    # Annotate response to clarify alias usage
    if "result" in result and isinstance(result["result"], str):
        result["result"] = result["result"]
    logger.debug("Whoami command completed", player=player_name)
    return result


async def handle_emote_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage | None, player_name: str
) -> dict[str, str]:
    """
    Handle the emote command for performing emotes.

    Args:
        command_data: Command data dictionary containing validated command information
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Emote command result
    """
    logger.debug("Processing emote command", player=player_name)

    # Extract action from command_data
    action = command_data.get("action")
    if not action:
        parsed_command = command_data.get("parsed_command")
        if parsed_command is not None and hasattr(parsed_command, "action"):
            action = parsed_command.action
    if not action:
        logger.warning("Emote command with no action", player=player_name)
        return {"result": "Emote what? Usage: emote <action>"}

    logger.debug("Player performing emote", player=player_name)

    try:
        # Import and use the emote service
        from ..game.emote_service import EmoteService

        emote_service = EmoteService()

        # Check if this is a predefined emote
        if emote_service.is_emote_alias(action):
            # Get the emote definition and format messages
            self_message, other_message = emote_service.format_emote_messages(action, player_name)

            # Return both messages for broadcasting
            logger.debug("Predefined emote executed", player=player_name, emote=action, message=self_message)
            return {"result": self_message, "broadcast": other_message, "broadcast_type": "emote"}
        else:
            # Custom emote - use the action as provided
            logger.debug("Custom emote executed")
            return {
                "result": f"{player_name} {action}",
                "broadcast": f"{player_name} {action}",
                "broadcast_type": "emote",
            }

    except Exception as e:
        import traceback

        logger.error(
            "Emote command error", player=player_name, action=action, error=str(e), traceback=traceback.format_exc()
        )
        # Fallback to simple emote if emote service fails
        return {"result": f"{player_name} {action}"}
