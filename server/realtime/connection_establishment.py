"""
Connection establishment management for connection manager.

This module handles WebSocket connection establishment operations.
"""

import time
import uuid
from typing import Any

from fastapi import WebSocket

from ..exceptions import DatabaseError
from ..logging.enhanced_logging_config import get_logger
from .connection_models import ConnectionMetadata

logger = get_logger(__name__)


def _find_dead_connections(player_id: uuid.UUID, manager: Any) -> list[str]:
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

        existing_websocket = manager.active_websockets[conn_id]
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


def _remove_dead_connection(conn_id: str, manager: Any) -> None:
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


def _update_player_connection_list(player_id: uuid.UUID, manager: Any) -> None:
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


async def _cleanup_dead_connections(dead_connection_ids: list[str], player_id: uuid.UUID, manager: Any) -> None:
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


def _register_new_connection(websocket: WebSocket, player_id: uuid.UUID, manager: Any) -> str:
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
    manager: Any,
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


def _setup_session_tracking(connection_id: str, player_id: uuid.UUID, session_id: str | None, manager: Any) -> None:
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


async def _setup_player_and_room(player_id: uuid.UUID, manager: Any) -> tuple[bool, Any | None]:
    """
    Get player and setup room subscription.

    Args:
        player_id: The player's ID
        manager: ConnectionManager instance

    Returns:
        tuple: (success: bool, player: Any | None)
    """
    player = await manager._get_player(player_id)  # pylint: disable=protected-access
    if not player:
        if manager.async_persistence is None:
            logger.warning("Persistence not available, connecting without player tracking", player_id=player_id)
        else:
            logger.error("Player not found", player_id=player_id)
            return False, None

    canonical_room_id = getattr(player, "current_room_id", None)
    if canonical_room_id:
        manager.room_manager.subscribe_to_room(str(player_id), canonical_room_id)

    return True, player


async def _track_player_presence(player_id: uuid.UUID, player: Any, manager: Any) -> None:
    """
    Track player presence and broadcast connection message.

    Args:
        player_id: The player's ID
        player: The player object
        manager: ConnectionManager instance
    """
    if player_id not in manager.online_players:
        await manager._track_player_connected(player_id, player, "websocket")  # pylint: disable=protected-access
    else:
        logger.info(
            "Player already tracked as online, but broadcasting connection message for WebSocket",
            player_id=player_id,
        )
        await manager._broadcast_connection_message(player_id, player)  # pylint: disable=protected-access


def _cleanup_failed_connection(connection_id: str | None, player_id: uuid.UUID, manager: Any) -> None:
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


async def establish_websocket_connection(
    websocket: WebSocket,
    player_id: uuid.UUID,
    manager: Any,  # ConnectionManager - avoiding circular import
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
    connection_id = None

    try:
        # Check for dead connections BEFORE acquiring lock
        dead_connection_ids = _find_dead_connections(player_id, manager)

        # Clean up dead connections under lock
        await _cleanup_dead_connections(dead_connection_ids, player_id, manager)

        # Accept the WebSocket connection
        await websocket.accept()

        # Register new connection
        connection_id = _register_new_connection(websocket, player_id, manager)

        # Create connection metadata
        _setup_connection_metadata(connection_id, player_id, manager, session_id, token)

        # Track connection in session
        _setup_session_tracking(connection_id, player_id, session_id, manager)

        # Log connection
        existing_count = len(manager.player_websockets[player_id]) - 1
        logger.info(
            "WebSocket connected for player",
            player_id=player_id,
            connection_id=connection_id,
            session_id=session_id,
            existing_websocket_connections=existing_count,
            total_connections=existing_count + 1,
        )

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
