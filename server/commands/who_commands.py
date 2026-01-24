"""
Who command handlers and utilities for MythosMUD.

This module contains the who command handler and related helper functions.
"""

# pylint: disable=too-many-locals,too-many-return-statements  # Reason: Who commands require many intermediate variables for complex player listing logic and multiple return statements for early validation returns

from typing import TYPE_CHECKING, Any

from ..structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from ..models.player import Player

logger = get_logger(__name__)


def filter_players_by_name(players: list[Any], filter_term: str) -> list[Any]:
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
        # If parts < 4, return unknown location
        return "Unknown Location"
    except (ValueError, TypeError, AttributeError) as e:
        logger.error("Error parsing room ID", room_id=room_id, error=str(e), error_type=type(e).__name__)
        # Safe fallback that doesn't depend on room_id being a valid string
        return "Unknown Location"


def format_player_entry(player: "Player") -> str:
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
    except (AttributeError, TypeError, ValueError) as e:
        # Safely get player name for logging (may also fail)
        player_name = getattr(player, "name", "Unknown")
        logger.error("Error formatting player entry", player_name=player_name, error=str(e))
        # Fallback formatting with safe attribute access
        location = "Unknown location"
        player_name_safe = getattr(player, "name", "Unknown Player")
        player_level_safe = getattr(player, "level", 0)
        base_entry = f"{player_name_safe} [{player_level_safe}] - {location}"

    # Add admin indicator if player is admin
    if player.is_admin:
        base_entry = f"{player.name} [{player.level}] [ADMIN] - {location}"

    return base_entry


def parse_last_active_datetime(last_active: Any) -> Any:
    """
    Parse last_active from string or datetime object to timezone-aware datetime.

    Args:
        last_active: String or datetime object representing last active time

    Returns:
        datetime: Timezone-aware datetime object, or None if parsing fails
    """
    from datetime import UTC, datetime

    if not last_active:
        return None

    if isinstance(last_active, str):
        try:
            last_active_str = last_active.strip()
            if last_active_str.endswith("Z"):
                return datetime.fromisoformat(last_active_str[:-1] + "+00:00")
            if "+" in last_active_str or "-" in last_active_str[-6:]:
                return datetime.fromisoformat(last_active_str)
            return datetime.fromisoformat(last_active_str).replace(tzinfo=UTC)
        except (ValueError, AttributeError) as e:
            logger.warning("Failed to parse last_active string", last_active=last_active, error=str(e))
            return None

    # Ensure datetime is timezone-aware
    if last_active.tzinfo is None:
        return last_active.replace(tzinfo=UTC)

    return last_active


async def filter_online_players(players: list[Any], online_threshold: Any) -> list[Any]:
    """
    Filter players to only those who are online (active within threshold).

    Args:
        players: List of player objects
        online_threshold: Datetime threshold for considering players online

    Returns:
        list: List of online players
    """
    online_players = []
    logger.debug("Who command - checking players", player_count=len(players), threshold=online_threshold)

    for player in players:
        if not player.last_active:
            logger.debug("Player has no last_active timestamp", player_name=player.name)
            continue

        last_active = parse_last_active_datetime(player.last_active)
        if last_active and last_active > online_threshold:
            online_players.append(player)

    logger.debug("Who command - found online players", online_count=len(online_players), total_count=len(players))
    return online_players


def format_who_result(players: list[Any], filter_term: str | None = None) -> str:
    """
    Format the who command result message.

    Args:
        players: List of player objects to format
        filter_term: Optional filter term for filtered results

    Returns:
        str: Formatted result message
    """
    if not players:
        if filter_term:
            return f"No players found matching '{filter_term}'. Try 'who' to see all online players."
        return "No players are currently online."

    sorted_players = sorted(players, key=lambda p: p.name.lower())
    player_entries = [format_player_entry(player) for player in sorted_players]
    player_list = ", ".join(player_entries)

    if filter_term:
        return f"Players matching '{filter_term}' ({len(players)}): {player_list}"

    return f"Online Players ({len(players)}): {player_list}"


def get_players_for_who(online_players: list[Any], filter_term: str) -> tuple[list[Any], str | None]:
    """
    Get the list of players to show and the effective filter term.

    Args:
        online_players: List of online players
        filter_term: Optional filter term

    Returns:
        tuple: (players_to_show, effective_filter_term)
    """
    if filter_term:
        filtered = filter_players_by_name(online_players, filter_term)
        return filtered, filter_term
    return online_players, None


async def handle_who_command(
    command_data: dict[str, Any],
    _current_user: dict[str, Any],
    request: Any,
    _alias_storage: Any | None,
    player_name: str,
) -> dict[str, str]:
    """
    Handle the who command for listing online players.

    Args:
        command_data: Command data dictionary containing validated command information
        _current_user: Current user information (unused, required for interface compatibility)
        request: FastAPI request object
        _alias_storage: Alias storage instance (unused, required for interface compatibility)
        player_name: Player name for logging

    Returns:
        dict: Who command result
    """
    logger.debug("Processing who command", player=player_name)

    filter_term = command_data.get("target_player", "")

    app = request.app if request else None
    # Prefer container, fallback to app.state for backward compatibility
    persistence = None
    if app and hasattr(app.state, "container") and app.state.container:
        persistence = app.state.container.async_persistence
    elif app:
        persistence = getattr(app.state, "persistence", None)

    if not persistence:
        logger.warning("Who command failed - no persistence layer")
        return {"result": "Player information is not available."}

    try:
        players = await persistence.list_players()
        if not players:
            logger.debug("No players found in database", player=player_name)
            return {"result": "No players found."}

        # Filter to only show online players (those with recent activity)
        from datetime import UTC, datetime, timedelta

        now = datetime.now(UTC)
        online_threshold = now - timedelta(minutes=5)  # Consider players online if active in last 5 minutes

        online_players = await filter_online_players(players, online_threshold)

        # Apply name filtering if provided, otherwise use all online players
        players_to_show, effective_filter = get_players_for_who(online_players, filter_term)
        result = format_who_result(players_to_show, effective_filter)

        logger.debug(
            "Who command completed",
            player=player_name,
            filter=effective_filter,
            count=len(players_to_show),
        )
        return {"result": result}

    except (AttributeError, KeyError, TypeError, ValueError, RuntimeError) as e:
        logger.error(
            "Who command error",
            player=player_name,
            command_data=command_data,
            error_type=type(e).__name__,
            error_message=str(e),
            exc_info=True,
        )
        return {"result": f"Error retrieving player list: {str(e)}"}
