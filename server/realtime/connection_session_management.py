"""
Connection session management for connection manager.

This module handles WebSocket connection session management operations.
"""

import uuid
from typing import Any

from fastapi import WebSocket

from ..exceptions import DatabaseError
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


def _is_websocket_connected(websocket: WebSocket) -> bool:
    """
    Check if a WebSocket is connected.

    Args:
        websocket: The WebSocket to check

    Returns:
        bool: True if connected, False otherwise
    """
    try:
        return websocket.client_state.name == "CONNECTED"
    except (AttributeError, ValueError, TypeError):
        return False


async def _disconnect_connection_for_session(connection_id: str, player_id: uuid.UUID, manager: Any) -> bool:
    """
    Disconnect a single connection for a new game session.

    Args:
        connection_id: The connection ID to disconnect
        player_id: The player's ID
        manager: ConnectionManager instance

    Returns:
        bool: True if connection was disconnected
    """
    if connection_id not in manager.active_websockets:
        return False

    websocket = manager.active_websockets[connection_id]
    # Guard against None websocket (can happen during cleanup)
    if websocket is None:
        del manager.active_websockets[connection_id]
        return False
    disconnected = False

    try:
        if _is_websocket_connected(websocket):
            logger.info(
                "Closing WebSocket due to new game session (debug: mid-run drops)",
                disconnect_reason="new_game_session",
                connection_id=connection_id,
                player_id=player_id,
            )
            await websocket.close(code=1000, reason="New game session established")
            logger.info("Successfully closed WebSocket due to new game session", connection_id=connection_id)
        disconnected = True
    except (DatabaseError, AttributeError) as e:
        logger.debug("Non-critical error closing WebSocket", connection_id=connection_id, error=str(e))
        disconnected = True

    try:
        del manager.active_websockets[connection_id]
    except KeyError:
        pass

    return disconnected


async def _disconnect_all_connections_for_session(connection_ids: list[str], player_id: uuid.UUID, manager: Any) -> int:
    """
    Disconnect all connections for a new game session.

    Args:
        connection_ids: List of connection IDs to disconnect
        player_id: The player's ID
        manager: ConnectionManager instance

    Returns:
        int: Number of connections disconnected
    """
    disconnected_count = 0

    for connection_id in connection_ids:
        if await _disconnect_connection_for_session(connection_id, player_id, manager):
            disconnected_count += 1

        if connection_id in manager.connection_metadata:
            del manager.connection_metadata[connection_id]

    try:
        del manager.player_websockets[player_id]
    except KeyError:
        pass

    return disconnected_count


def _cleanup_old_session_tracking(player_id: uuid.UUID, manager: Any) -> None:
    """
    Clean up old session tracking.

    Args:
        player_id: The player's ID
        manager: ConnectionManager instance
    """
    if player_id not in manager.player_sessions:
        return

    old_session_id = manager.player_sessions[player_id]
    if old_session_id in manager.session_connections:
        try:
            del manager.session_connections[old_session_id]
        except KeyError:
            pass


def _cleanup_player_data_for_session(player_id: uuid.UUID, manager: Any) -> None:
    """
    Clean up player data for a new session.

    Args:
        player_id: The player's ID
        manager: ConnectionManager instance
    """
    manager.rate_limiter.remove_player_data(str(player_id))
    manager.message_queue.remove_player_messages(str(player_id))
    if player_id in manager.last_seen:
        del manager.last_seen[player_id]
    manager.last_active_update_times.pop(player_id, None)
    manager.room_manager.remove_player_from_all_rooms(str(player_id))


async def handle_new_game_session_impl(
    player_id: uuid.UUID,
    new_session_id: str,
    manager: Any,  # ConnectionManager
) -> dict[str, Any]:
    """
    Handle a new game session by disconnecting existing connections.

    Args:
        player_id: The player's ID
        new_session_id: The new session ID
        manager: ConnectionManager instance

    Returns:
        dict: Session handling results
    """
    session_results: dict[str, Any] = {
        "player_id": player_id,
        "new_session_id": new_session_id,
        "previous_session_id": None,
        "connections_disconnected": 0,
        "websocket_connections": 0,
        "success": False,
        "errors": [],
    }

    try:
        existing_count = len(manager.player_websockets.get(player_id, []))
        logger.info(
            "Handling new game session for player",
            new_session_id=new_session_id,
            player_id=player_id,
            existing_websocket_connections=existing_count,
            will_disconnect_all=True,
        )

        if player_id in manager.player_sessions:
            session_results["previous_session_id"] = manager.player_sessions[player_id]

        if player_id in manager.player_websockets:
            connection_ids = manager.player_websockets[player_id].copy()
            session_results["websocket_connections"] = len(connection_ids)
            session_results["connections_disconnected"] = await _disconnect_all_connections_for_session(
                connection_ids, player_id, manager
            )

        _cleanup_old_session_tracking(player_id, manager)

        manager.player_sessions[player_id] = new_session_id
        manager.session_connections[new_session_id] = []

        _cleanup_player_data_for_session(player_id, manager)

        session_results["success"] = True
        logger.info(
            "Disconnected connections for new game session",
            connections_disconnected=session_results["connections_disconnected"],
            new_session_id=new_session_id,
            player_id=player_id,
        )

    except (DatabaseError, AttributeError) as e:
        error_msg = f"Error handling new game session for player {player_id}: {e}"
        logger.error(error_msg, exc_info=True)
        session_results["errors"].append(error_msg)
        session_results["success"] = False

    return session_results
