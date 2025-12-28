"""
Player disconnect handling functions.

This module handles broadcasting disconnect events and managing
player removal from rooms and tracking systems.
"""

import asyncio
import uuid
from typing import Any

from ..structured_logging.enhanced_logging_config import get_logger
from .player_presence_utils import extract_player_name

logger = get_logger(__name__)


async def handle_player_disconnect_broadcast(
    player_id: uuid.UUID,
    player_name: str,
    room_id: str | None,
    manager: Any,  # ConnectionManager - avoiding circular import
) -> None:
    """
    Handle broadcasting disconnect events when a player disconnects.

    Args:
        player_id: The player's ID
        player_name: The player's name
        room_id: The room ID (if any)
        manager: ConnectionManager instance
    """
    if room_id and manager.async_persistence:
        room = manager.async_persistence.get_room_by_id(room_id)  # Sync method, uses cache
        if room:
            player_id_str = str(player_id)
            if room.has_player(player_id_str):
                logger.debug("Calling room.player_left() before disconnect cleanup", player=player_id, room_id=room_id)
                room.player_left(player_id_str)
                # CRITICAL FIX: Wait for PlayerLeftRoom event to be processed
                await asyncio.sleep(0)  # Yield to event loop

    # Notify current room that player left the game
    if room_id:
        from .envelope import build_event

        safe_player_name = player_name if player_name else "Unknown Player"
        left_event = build_event(
            "player_left_game",
            {"player_id": player_id, "player_name": safe_player_name},
            room_id=room_id,
        )
        logger.info("Broadcasting player_left_game", player_id=player_id, room_id=room_id)
        await manager.broadcast_to_room(room_id, left_event, exclude_player=player_id)


def _collect_disconnect_keys(player_id: uuid.UUID, player: Any) -> tuple[set[uuid.UUID], set[str]]:
    """
    Collect all keys (UUID and string) that need to be removed for player disconnection.

    Args:
        player_id: The player's ID
        player: The player object (may be None)

    Returns:
        Tuple of (uuid_keys, string_keys) sets to remove
    """
    keys_to_remove = {player_id}
    keys_to_remove_str: set[str] = set()

    if player is None:
        return keys_to_remove, keys_to_remove_str

    canonical_id = getattr(player, "player_id", None) or getattr(player, "user_id", None)
    if canonical_id:
        if isinstance(canonical_id, uuid.UUID):
            keys_to_remove.add(canonical_id)
        else:
            keys_to_remove_str.add(str(canonical_id))

    player_name = extract_player_name(player, player_id)
    if player_name:
        keys_to_remove_str.add(player_name)

    return keys_to_remove, keys_to_remove_str


def _remove_player_from_online_tracking(
    keys_to_remove: set[uuid.UUID],
    keys_to_remove_str: set[str],
    manager: Any,
) -> None:
    """
    Remove player from online tracking and room presence.

    Args:
        keys_to_remove: Set of UUID keys to remove
        keys_to_remove_str: Set of string keys to remove
        manager: ConnectionManager instance
    """
    # Remove player from online_players AFTER broadcasting disconnect events
    for key in list(keys_to_remove):
        if key in manager.online_players:
            del manager.online_players[key]
        manager.room_manager.remove_player_from_all_rooms(str(key))

    # Remove string keys
    for str_key in keys_to_remove_str:
        manager.room_manager.remove_player_from_all_rooms(str_key)


def _cleanup_player_references(player_id: uuid.UUID, manager: Any) -> None:
    """
    Clean up all remaining player references.

    Args:
        player_id: The player's ID
        manager: ConnectionManager instance
    """
    if player_id in manager.online_players:
        del manager.online_players[player_id]
    if player_id in manager.last_seen:
        del manager.last_seen[player_id]
    manager.last_active_update_times.pop(player_id, None)
    manager.rate_limiter.remove_player_data(str(player_id))
    manager.message_queue.remove_player_messages(str(player_id))
