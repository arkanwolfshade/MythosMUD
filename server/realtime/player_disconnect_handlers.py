"""
Player disconnect handling functions.

This module handles broadcasting disconnect events and managing
player removal from rooms and tracking systems.
"""

import time
import uuid
from typing import TYPE_CHECKING, cast

from anyio import sleep
from structlog.stdlib import BoundLogger

from ..async_persistence import AsyncPersistenceLayer
from ..models import Player
from ..models.room import Room
from ..structured_logging.enhanced_logging_config import get_logger
from .player_presence_utils import extract_player_name

if TYPE_CHECKING:
    from .connection_manager import ConnectionManager

logger: BoundLogger = get_logger(__name__)

# Sessions age off 5 minutes after disconnect; reconnects purge old sessions immediately
SESSION_AGE_OFF_SECONDS = 300


async def handle_player_disconnect_broadcast(
    player_id: uuid.UUID,
    player_name: str | None,
    room_id: str | None,
    manager: "ConnectionManager",
) -> None:
    """
    Handle broadcasting disconnect events when a player disconnects.

    Args:
        player_id: The player's ID
        player_name: The player's name
        room_id: The room ID (if any)
        manager: ConnectionManager instance
    """
    persistence = cast(AsyncPersistenceLayer | None, manager.async_persistence)
    if room_id and persistence:
        room: Room | None = persistence.get_room_by_id(room_id)  # Sync method, uses cache
        if room:
            player_id_str = str(player_id)
            if room.has_player(player_id_str):
                logger.debug("Calling room.player_left() before disconnect cleanup", player=player_id, room_id=room_id)
                room.player_left(player_id_str)
                # CRITICAL FIX: Wait for PlayerLeftRoom event to be processed
                await sleep(0)  # Yield to event loop

    # Notify current room that player left the game
    if room_id:
        from .envelope import build_event

        safe_player_name = player_name if player_name else "Unknown Player"
        left_event = build_event(
            "player_left_game",
            {"player_id": player_id, "player_name": safe_player_name},
            room_id=room_id,
        )
        logger.info(
            "Broadcasting player_left_game (debug: mid-run drops)",
            broadcast_event="player_left_game",
            player_id=player_id,
            room_id=room_id,
        )
        _ = await manager.broadcast_to_room(room_id, left_event, exclude_player=player_id)


def _collect_disconnect_keys(player_id: uuid.UUID, player: Player | None) -> tuple[set[uuid.UUID], set[str]]:
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
            keys_to_remove_str.add(str(cast(object, canonical_id)))

    player_name = extract_player_name(player, player_id)
    if player_name:
        keys_to_remove_str.add(player_name)

    return keys_to_remove, keys_to_remove_str


def _remove_player_from_online_tracking(
    keys_to_remove: set[uuid.UUID],
    keys_to_remove_str: set[str],
    manager: "ConnectionManager",
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
        _ = manager.room_manager.remove_player_from_all_rooms(str(key))

    # Remove string keys
    for str_key in keys_to_remove_str:
        _ = manager.room_manager.remove_player_from_all_rooms(str_key)


def _cleanup_player_references(player_id: uuid.UUID, manager: "ConnectionManager") -> None:
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
    _ = manager.last_active_update_times.pop(player_id, None)
    manager.rate_limiter.remove_player_data(str(player_id))
    manager.message_queue.remove_player_messages(str(player_id))

    # H2 fix: Mark session for aging (5 min TTL). Reconnects purge old sessions immediately.
    player_sessions = manager.player_sessions
    session_disconnect_times = manager.session_disconnect_times
    if player_id in player_sessions:
        session_id: str = player_sessions[player_id]
        session_disconnect_times[session_id] = time.time()
        # Keep player_sessions and session_connections; reconnect purges, else age off in cleanup

    # H1 fix: Allow processed_disconnects to shrink so it does not grow unbounded
    if player_id in manager.processed_disconnects:
        manager.processed_disconnects.discard(player_id)


# Referenced here so pyright sees use in-module; player_presence_tracker imports these names.
_DISCONNECT_HELPERS_FOR_EXPORT = (
    _collect_disconnect_keys,
    _remove_player_from_online_tracking,
    _cleanup_player_references,
)


def _get_session_maps_for_age_off(
    manager: object,
) -> tuple[dict[str, float], dict[uuid.UUID, str], dict[str, list[str]]] | None:
    """
    Return typed session maps for age-off, or None if the manager is not ready.

    Uses a single None membership check (not assert) so invariants hold under python -O.
    """
    session_disconnect_times = getattr(manager, "session_disconnect_times", None)
    player_sessions = getattr(manager, "player_sessions", None)
    session_connections = getattr(manager, "session_connections", None)
    if not all((session_disconnect_times, player_sessions, session_connections)):
        return None
    if None in (session_disconnect_times, player_sessions, session_connections):
        raise RuntimeError("session maps are None after truthiness check in age_off_disconnected_sessions")

    return (
        cast(dict[str, float], session_disconnect_times),
        cast(dict[uuid.UUID, str], player_sessions),
        cast(dict[str, list[str]], session_connections),
    )


def _session_ids_past_age_off(disconnect_times: dict[str, float], now: float) -> list[str]:
    """Session ids whose disconnect timestamp is older than SESSION_AGE_OFF_SECONDS."""
    expired: list[str] = []
    for session_id, disconnect_time in list(disconnect_times.items()):
        if now - disconnect_time >= SESSION_AGE_OFF_SECONDS:
            expired.append(session_id)
    return expired


def _purge_expired_sessions_from_maps(
    disconnect_times: dict[str, float],
    sessions_by_player: dict[uuid.UUID, str],
    connections_by_session: dict[str, list[str]],
    expired: list[str],
) -> None:
    """Remove expired session ids from disconnect_times, connections, and player_sessions."""
    for session_id in expired:
        _ = disconnect_times.pop(session_id, None)
        _ = connections_by_session.pop(session_id, None)
        for pid, sid in list(sessions_by_player.items()):
            if sid == session_id:
                del sessions_by_player[pid]
                break


def age_off_disconnected_sessions(manager: object) -> int:
    """
    Remove sessions that have been disconnected for more than SESSION_AGE_OFF_SECONDS.

    Reconnects purge old sessions immediately via _cleanup_old_session_tracking;
    this handles sessions that were never reconnected.

    Returns:
        Number of sessions aged off.
    """
    maps = _get_session_maps_for_age_off(manager)
    if maps is None:
        return 0
    disconnect_times, sessions_by_player, connections_by_session = maps

    now = time.time()
    expired = _session_ids_past_age_off(disconnect_times, now)
    _purge_expired_sessions_from_maps(disconnect_times, sessions_by_player, connections_by_session, expired)
    return len(expired)
