"""
Connection establishment management for connection manager.

This module handles WebSocket connection establishment operations.
"""

import time
import uuid
from typing import Protocol

from anyio import Lock
from fastapi import WebSocket

from ..exceptions import DatabaseError
from ..models import Player
from ..structured_logging.enhanced_logging_config import get_logger
from .connection_models import ConnectionMetadata
from .connection_session_management import handle_new_game_session_impl
from .disconnect_grace_period import cancel_grace_period
from .message_queue import MessageQueue
from .monitoring.performance_tracker import PerformanceTracker
from .rate_limiter import RateLimiter
from .room_subscription_manager import RoomSubscriptionManager

logger = get_logger(__name__)

# Protocol stub bodies use Ellipsis per PEP 544; Pylint W2301 conflicts with pyright if replaced with pass.
# pylint: disable=unnecessary-ellipsis


class _EstablishmentConnectionManager(Protocol):  # pylint: disable=too-few-public-methods  # Reason: PEP 544 Protocol is a structural type, not a concrete class
    """Connection manager surface used by establishment helpers."""

    active_websockets: dict[str, WebSocket]
    connection_metadata: dict[str, ConnectionMetadata]
    player_websockets: dict[uuid.UUID, list[str]]
    disconnect_lock: Lock
    session_connections: dict[str, list[str]]
    player_sessions: dict[uuid.UUID, str]
    async_persistence: object | None
    room_manager: RoomSubscriptionManager
    online_players: dict[uuid.UUID, dict[str, object]]
    performance_tracker: PerformanceTracker
    session_disconnect_times: dict[str, float]
    last_seen: dict[uuid.UUID, float]
    last_active_update_times: dict[uuid.UUID, float]
    rate_limiter: RateLimiter
    message_queue: MessageQueue

    async def get_player(self, player_id: uuid.UUID) -> Player | None:
        """Load player from persistence."""
        ...

    async def track_player_connected(self, player_id: uuid.UUID, player: Player, connection_type: str) -> None:
        """Record a newly online player."""
        ...

    async def broadcast_connection_message(self, player_id: uuid.UUID, player: Player) -> None:
        """Broadcast presence for a player already in online_players."""
        ...


def _find_dead_connections(player_id: uuid.UUID, manager: _EstablishmentConnectionManager) -> list[str]:
    """
    Find dead WebSocket connections for a player before acquiring lock.

    Args:
        player_id: The player's ID
        manager: ConnectionManager instance

    Returns:
        List of dead connection IDs
    """
    dead_connection_ids: list[str] = []
    if player_id not in manager.player_websockets:
        return dead_connection_ids

    for conn_id in manager.player_websockets[player_id]:
        if conn_id not in manager.active_websockets:
            continue

        existing_websocket: WebSocket | None = manager.active_websockets.get(conn_id)
        if existing_websocket is None:
            del manager.active_websockets[conn_id]
            raise ConnectionError("WebSocket is None")
        try:
            if existing_websocket.client_state.name != "CONNECTED":
                raise ConnectionError("WebSocket not connected")
        except ConnectionError as ping_error:
            logger.warning(
                "Dead WebSocket connection, will clean up",
                connection_id=conn_id,
                player_id=player_id,
                ping_error=str(ping_error),
            )
            dead_connection_ids.append(conn_id)

    return dead_connection_ids


def _remove_dead_connection(conn_id: str, manager: _EstablishmentConnectionManager) -> None:
    """
    Remove a single dead connection from tracking structures.

    Args:
        conn_id: The connection ID to remove
        manager: ConnectionManager instance
    """
    if conn_id in manager.active_websockets:
        del manager.active_websockets[conn_id]
    if conn_id in manager.connection_metadata:
        del manager.connection_metadata[conn_id]


def _update_player_connection_list(player_id: uuid.UUID, manager: _EstablishmentConnectionManager) -> None:
    """
    Update player's connection list to only include active connections.

    Args:
        player_id: The player's ID
        manager: ConnectionManager instance
    """
    if player_id not in manager.player_websockets:
        return

    active_connection_ids = [cid for cid in manager.player_websockets[player_id] if cid in manager.active_websockets]
    if active_connection_ids:
        manager.player_websockets[player_id] = active_connection_ids
    else:
        del manager.player_websockets[player_id]


async def _cleanup_dead_connections(
    dead_connection_ids: list[str], player_id: uuid.UUID, manager: _EstablishmentConnectionManager
) -> None:
    """
    Clean up dead connections under lock.

    Args:
        dead_connection_ids: List of dead connection IDs to clean up
        player_id: The player's ID
        manager: ConnectionManager instance
    """
    if not dead_connection_ids:
        return

    async with manager.disconnect_lock:
        for conn_id in dead_connection_ids:
            _remove_dead_connection(conn_id, manager)

        _update_player_connection_list(player_id, manager)


def _register_new_connection(
    websocket: WebSocket, player_id: uuid.UUID, manager: _EstablishmentConnectionManager
) -> str:
    """
    Register a new WebSocket connection.

    Args:
        websocket: The WebSocket connection
        player_id: The player's ID
        manager: ConnectionManager instance

    Returns:
        The new connection ID
    """
    connection_id = str(uuid.uuid4())
    manager.active_websockets[connection_id] = websocket

    if player_id not in manager.player_websockets:
        manager.player_websockets[player_id] = []
    manager.player_websockets[player_id].append(connection_id)

    return connection_id


def _setup_connection_metadata(
    connection_id: str,
    player_id: uuid.UUID,
    manager: _EstablishmentConnectionManager,
    session_id: str | None,
    token: str | None,
) -> None:
    """
    Create and store connection metadata.

    Args:
        connection_id: The connection ID
        player_id: The player's ID
        manager: ConnectionManager instance
        session_id: Optional session ID
        token: Optional JWT token
    """
    current_time = time.time()
    manager.connection_metadata[connection_id] = ConnectionMetadata(
        connection_id=connection_id,
        player_id=player_id,
        connection_type="websocket",
        established_at=current_time,
        last_seen=current_time,
        is_healthy=True,
        session_id=session_id,
        token=token,
        last_token_validation=current_time if token else None,
    )


def _setup_session_tracking(
    connection_id: str, player_id: uuid.UUID, session_id: str | None, manager: _EstablishmentConnectionManager
) -> None:
    """
    Track connection in session.

    Args:
        connection_id: The connection ID
        player_id: The player's ID
        session_id: Optional session ID
        manager: ConnectionManager instance
    """
    if not session_id:
        return

    if session_id not in manager.session_connections:
        manager.session_connections[session_id] = []
    manager.session_connections[session_id].append(connection_id)
    if player_id not in manager.player_sessions or manager.player_sessions[player_id] == session_id:
        manager.player_sessions[player_id] = session_id


def _bind_accepted_websocket(
    websocket: WebSocket,
    player_id: uuid.UUID,
    manager: _EstablishmentConnectionManager,
    session_id: str | None,
    token: str | None,
) -> str:
    """Register an accepted socket and attach session metadata."""
    connection_id = _register_new_connection(websocket, player_id, manager)
    _setup_connection_metadata(connection_id, player_id, manager, session_id, token)
    _setup_session_tracking(connection_id, player_id, session_id, manager)
    existing_count = len(manager.player_websockets[player_id]) - 1
    logger.info(
        "WebSocket connected for player",
        player_id=player_id,
        connection_id=connection_id,
        session_id=session_id,
        existing_websocket_connections=existing_count,
        total_connections=existing_count + 1,
    )
    return connection_id


async def _setup_player_and_room(
    player_id: uuid.UUID, manager: _EstablishmentConnectionManager
) -> tuple[bool, Player | None]:
    """
    Get player and setup room subscription.

    Args:
        player_id: The player's ID
        manager: ConnectionManager instance

    Returns:
        tuple: (success: bool, player: Player | None)
    """
    player = await manager.get_player(player_id)
    if player is None:
        if manager.async_persistence is None:
            logger.warning("Persistence not available, connecting without player tracking", player_id=player_id)
        else:
            logger.error("Player not found", player_id=player_id)
            return False, None
        return True, None

    if not hasattr(player, "current_room_id"):
        return True, player
    canonical_room_id = player.current_room_id
    if canonical_room_id:
        _ = manager.room_manager.subscribe_to_room(str(player_id), str(canonical_room_id))

    return True, player


async def _track_player_presence(
    player_id: uuid.UUID, player: Player | None, manager: _EstablishmentConnectionManager
) -> None:
    """
    Track player presence and broadcast connection message.

    Args:
        player_id: The player's ID
        player: The player object
        manager: ConnectionManager instance
    """
    # Orphan /rest countdown will force_disconnect the new socket if left running.
    # Inline import: rest_command -> combat -> ConnectionManager -> this module.
    from ..commands.rest_command import cancel_rest_countdown

    await cancel_rest_countdown(player_id, manager)
    if player is None:
        await cancel_grace_period(player_id, manager)
        return
    # track_player_connected uses grace_period_players to decide enter setup (add to room._players).
    # Cancelling grace first made linkdead reconnects skip occupancy and vanish from Occupants.
    await manager.track_player_connected(player_id, player, "websocket")
    await cancel_grace_period(player_id, manager)


def _cleanup_failed_connection(
    connection_id: str | None, player_id: uuid.UUID, manager: _EstablishmentConnectionManager
) -> None:
    """
    Cleanup connection on failure.

    Args:
        connection_id: The connection ID to clean up (may be None if connection wasn't registered)
        player_id: The player's ID
        manager: ConnectionManager instance
    """
    if not connection_id:
        return

    try:
        if connection_id in manager.active_websockets:
            del manager.active_websockets[connection_id]
        if connection_id in manager.connection_metadata:
            del manager.connection_metadata[connection_id]
    except (DatabaseError, AttributeError) as cleanup_error:
        logger.warning("Error during connection failure cleanup", player_id=player_id, cleanup_error=str(cleanup_error))


async def _reconcile_prior_session(
    player_id: uuid.UUID,
    session_id: str | None,
    manager: _EstablishmentConnectionManager,
) -> None:
    """Settle a differing prior session before a new socket is registered.

    ADR-018 replaces prior sockets when the session changes, but only while sockets still
    exist to replace. A mapping left behind by a client that vanished has nothing live
    behind it; replacing against it would tear down the socket being established and leave
    the player linkdead until a server restart, so drop it and let the new session own the
    player instead.
    """
    current_session = manager.player_sessions.get(player_id)
    if not session_id or current_session is None or current_session == session_id:
        return

    if manager.player_websockets.get(player_id):
        _ = await handle_new_game_session_impl(player_id, session_id, manager)
        return

    _ = manager.player_sessions.pop(player_id, None)
    _ = manager.session_connections.pop(current_session, None)


async def establish_websocket_connection(
    websocket: WebSocket,
    player_id: uuid.UUID,
    manager: _EstablishmentConnectionManager,
    session_id: str | None = None,
    token: str | None = None,
) -> tuple[bool, str | None]:
    """
    Establish a new WebSocket connection.

    Args:
        websocket: The WebSocket connection
        player_id: The player's ID
        manager: ConnectionManager instance
        session_id: Optional session ID
        token: Optional JWT token

    Returns:
        tuple: (success: bool, connection_id: str | None)
    """
    start_time = time.time()
    connection_id: str | None = None

    try:
        # Check for dead connections BEFORE acquiring lock
        dead_connection_ids = _find_dead_connections(player_id, manager)

        # Clean up dead connections under lock
        await _cleanup_dead_connections(dead_connection_ids, player_id, manager)

        await _reconcile_prior_session(player_id, session_id, manager)

        await websocket.accept()
        connection_id = _bind_accepted_websocket(websocket, player_id, manager, session_id, token)

        # Get player and setup room subscription
        success, player = await _setup_player_and_room(player_id, manager)
        if not success:
            return False, connection_id

        # Track player presence
        await _track_player_presence(player_id, player, manager)

        # Track performance metrics
        duration_ms = (time.time() - start_time) * 1000
        manager.performance_tracker.record_connection_establishment("websocket", duration_ms)

        return True, connection_id

    except (DatabaseError, AttributeError) as e:
        logger.error(
            "Error connecting WebSocket",
            player_id=player_id,
            session_id=session_id,
            has_token=bool(token),
            error=str(e),
            error_type=type(e).__name__,
            exc_info=True,
        )
        # Cleanup on failure
        _cleanup_failed_connection(connection_id, player_id, manager)
        return False, connection_id
