"""
Room and subscription utility helpers for connection manager.

This module provides helper functions for room-related operations
and subscription management.
"""

from typing import Any

from ..exceptions import DatabaseError
from ..logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


def canonical_room_id_impl(room_id: str | None, manager: Any) -> str | None:
    """
    Resolve a room id to the canonical Room.id value.

    Args:
        room_id: The room ID to resolve
        manager: ConnectionManager instance

    Returns:
        str | None: The canonical room ID or the original ID if resolution fails
    """
    try:
        if not room_id:
            return room_id

        # Try room manager's persistence first
        if manager.room_manager.async_persistence is not None:
            room = manager.room_manager.async_persistence.get_room_by_id(room_id)
            if room is not None and getattr(room, "id", None):
                return room.id

        # Fallback to main persistence layer
        if manager.async_persistence is not None:
            room = manager.async_persistence.get_room_by_id(room_id)
            if room is not None and getattr(room, "id", None):
                return room.id
    except (DatabaseError, AttributeError) as e:
        logger.error("Error resolving canonical room id", room_id=room_id, error=str(e))
    return room_id


def reconcile_room_presence_impl(room_id: str, manager: Any) -> None:
    """Ensure room_occupants only contains currently online players."""
    online_players_str = {str(k): v for k, v in manager.online_players.items()}
    manager.room_manager.reconcile_room_presence(room_id, online_players_str)


def prune_player_from_all_rooms_impl(player_id: Any, manager: Any) -> None:
    """Remove a player from all room subscriptions and occupant lists."""
    manager.room_manager.remove_player_from_all_rooms(str(player_id))
