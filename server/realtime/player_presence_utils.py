"""
Utility functions for player presence tracking.

This module provides helper functions for extracting player information,
validating names, and getting player positions.
"""

import uuid
from typing import Any

from ..exceptions import DatabaseError
from ..logging.enhanced_logging_config import get_logger
from ..models import Player

logger = get_logger(__name__)


def _is_valid_name(name: Any) -> bool:
    """
    Check if a value is a valid non-empty string name.

    Args:
        name: Value to check

    Returns:
        True if name is a valid non-empty string, False otherwise
    """
    return isinstance(name, str) and bool(name.strip())


def _is_uuid_string(value: str) -> bool:
    """
    Check if a string is a UUID format.

    Args:
        value: String to check

    Returns:
        True if string matches UUID format, False otherwise
    """
    if len(value) != 36 or value.count("-") != 4:
        return False
    return all(c in "0123456789abcdefABCDEF-" for c in value)


def _get_name_from_user(player: Player) -> str | None:
    """
    Attempt to get player name from related User object.

    Args:
        player: The player object

    Returns:
        Player name from user if available, None otherwise
    """
    if not hasattr(player, "user"):
        return None

    try:
        user = getattr(player, "user", None)
        if not user:
            return None
        return getattr(user, "username", None) or getattr(user, "display_name", None)
    except (DatabaseError, AttributeError) as e:
        logger.debug("Error accessing user relationship for player name", error=str(e))
        return None


def extract_player_name(player: Player, player_id: uuid.UUID) -> str:
    """
    Extract and validate player name, ensuring it's never a UUID.

    Args:
        player: The player object
        player_id: The player's ID for logging

    Returns:
        str: Valid player name (never a UUID)
    """
    # CRITICAL: Extract player name - NEVER use player_id as fallback
    # Player model has a 'name' column that should always exist (nullable=False)
    player_name = getattr(player, "name", None)

    # If player.name is not valid, try to get from user object
    if not _is_valid_name(player_name):
        player_name = _get_name_from_user(player)

    # If still no valid name, use placeholder (NEVER use UUID)
    if not _is_valid_name(player_name):
        logger.warning(
            "Player name not found, using placeholder",
            player_id=player_id,
            has_name_attr=hasattr(player, "name"),
            name_value=getattr(player, "name", "NOT_FOUND"),
        )
        player_name = "Unknown Player"

    # CRITICAL: Final validation - ensure player_name is NEVER a UUID
    # This is a defensive check in case player.name somehow contains a UUID
    if isinstance(player_name, str) and _is_uuid_string(player_name):
        logger.error(
            "CRITICAL: Player name is a UUID string, this should never happen",
            player_id=player_id,
            player_name=player_name,
            player_name_from_db=getattr(player, "name", "NOT_FOUND"),
        )
        player_name = "Unknown Player"

    # Type narrowing: ensure we always return a string
    if not isinstance(player_name, str):
        player_name = "Unknown Player"

    return player_name


def get_player_position(player: Player, player_id: uuid.UUID) -> str:
    """
    Get player position from stats.

    Args:
        player: The player object
        player_id: The player's ID for logging

    Returns:
        str: Player position (defaults to "standing")
    """
    position = "standing"
    if hasattr(player, "get_stats"):
        try:
            stats = player.get_stats()
            if isinstance(stats, dict):
                position = stats.get("position", "standing")
        except (DatabaseError, AttributeError) as exc:
            logger.warning(
                "Failed to load player stats during connection",
                player_id=player_id,
                error=str(exc),
            )
    return position
