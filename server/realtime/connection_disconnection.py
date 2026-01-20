"""
Connection disconnection management for connection manager.

This module handles WebSocket connection disconnection operations.
"""

import uuid
from typing import Any

from ..exceptions import DatabaseError
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


async def _disconnect_all_websockets(connection_ids: list[str], player_id: uuid.UUID, manager: Any) -> None:
    """
    Disconnect all WebSocket connections for a player.

    Args:
        connection_ids: List of connection IDs to disconnect
        player_id: The player's ID
        manager: ConnectionManager instance
    """
    for connection_id in connection_ids:
        if connection_id in manager.active_websockets:
            websocket = manager.active_websockets[connection_id]
            # Guard against None websocket (can happen during cleanup)
            if websocket is None:
                del manager.active_websockets[connection_id]
                return
            logger.info("DEBUG: Closing WebSocket", connection_id=connection_id, player_id=player_id)
            await manager._safe_close_websocket(websocket, code=1000, reason="Connection closed")  # pylint: disable=protected-access  # Reason: Accessing protected member _safe_close_websocket is necessary for connection disconnection implementation, this is part of the internal API
            logger.info("Successfully closed WebSocket", connection_id=connection_id, player_id=player_id)
            del manager.active_websockets[connection_id]

        # Clean up metadata and rate limiting
        if connection_id in manager.connection_metadata:
            del manager.connection_metadata[connection_id]
        manager.rate_limiter.remove_connection_message_data(connection_id)


async def _track_disconnect_if_needed(player_id: uuid.UUID, manager: Any, is_force_disconnect: bool) -> bool:
    """
    Track disconnection if needed.

    Args:
        player_id: The player's ID
        manager: ConnectionManager instance
        is_force_disconnect: If True, don't track disconnect

    Returns:
        bool: True if should track disconnect
    """
    if is_force_disconnect or manager.has_websocket_connection(player_id):
        return False

    async with manager.processed_disconnect_lock:
        if player_id not in manager.processed_disconnects:
            manager.processed_disconnects.add(player_id)
            return True

        logger.debug("Disconnect already processed, skipping", player_id=player_id)
        return False


def _cleanup_room_subscriptions(player_id: uuid.UUID, manager: Any, is_force_disconnect: bool) -> None:
    """
    Clean up room subscriptions if needed.

    Args:
        player_id: The player's ID
        manager: ConnectionManager instance
        is_force_disconnect: If True, preserve room membership
    """
    if is_force_disconnect or manager.has_websocket_connection(player_id):
        logger.debug("Preserving room membership during force disconnect", player_id=player_id)
        return

    manager.room_manager.remove_player_from_all_rooms(str(player_id))


def _cleanup_player_data(player_id: uuid.UUID, manager: Any) -> None:
    """
    Clean up rate limiting and message data for a player.

    Args:
        player_id: The player's ID
        manager: ConnectionManager instance
    """
    if manager.has_websocket_connection(player_id):
        return

    manager.rate_limiter.remove_player_data(str(player_id))
    manager.message_queue.remove_player_messages(str(player_id))
    if player_id in manager.last_seen:
        del manager.last_seen[player_id]
    manager.last_active_update_times.pop(player_id, None)


async def cleanup_websocket_disconnect(
    player_id: uuid.UUID,
    manager: Any,  # ConnectionManager
    is_force_disconnect: bool = False,
) -> bool:
    """
    Clean up WebSocket connections for a player.

    Args:
        player_id: The player's ID
        manager: ConnectionManager instance
        is_force_disconnect: If True, don't broadcast player_left_game

    Returns:
        bool: True if should track disconnect
    """
    should_track_disconnect = False

    async with manager.disconnect_lock:
        try:
            logger.info("Starting WebSocket disconnect", player_id=player_id, force_disconnect=is_force_disconnect)

            if player_id not in manager.player_websockets:
                return should_track_disconnect

            connection_ids = manager.player_websockets[player_id].copy()

            logger.info(
                "Found WebSocket connections",
                player_id=player_id,
                connection_count=len(connection_ids),
                connection_ids=connection_ids,
            )

            # Disconnect all WebSocket connections
            await _disconnect_all_websockets(connection_ids, player_id, manager)

            # Remove from tracking
            del manager.player_websockets[player_id]

            # Check if we need to track disconnection
            should_track_disconnect = await _track_disconnect_if_needed(player_id, manager, is_force_disconnect)

            # Clean up room subscriptions and player data
            _cleanup_room_subscriptions(player_id, manager, is_force_disconnect)

            # Clean up rate limiting and messages
            _cleanup_player_data(player_id, manager)

            logger.info("WebSocket disconnected", player_id=player_id)

        except (DatabaseError, AttributeError) as e:
            logger.error("Error during WebSocket disconnect", player_id=player_id, error=str(e), exc_info=True)

    return should_track_disconnect


async def disconnect_connection_by_id_impl(
    connection_id: str,
    manager: Any,  # ConnectionManager
) -> bool:
    """
    Disconnect a specific connection by its ID.

    Args:
        connection_id: The connection ID to disconnect
        manager: ConnectionManager instance

    Returns:
        bool: True if connection was found and disconnected
    """
    try:
        if connection_id not in manager.connection_metadata:
            logger.warning("Connection not found in metadata", connection_id=connection_id)
            return False

        metadata = manager.connection_metadata[connection_id]
        player_id = metadata.player_id
        connection_type = metadata.connection_type

        logger.info(
            "Disconnecting connection",
            connection_type=connection_type,
            connection_id=connection_id,
            player_id=player_id,
        )

        if connection_type == "websocket":
            if connection_id in manager.active_websockets:
                websocket = manager.active_websockets[connection_id]
                # Guard against None websocket (can happen during cleanup)
                if websocket is None:
                    del manager.active_websockets[connection_id]
                    return False
                logger.info("DEBUG: Closing WebSocket by connection ID", connection_id=connection_id)
                await manager._safe_close_websocket(websocket, code=1000, reason="Connection closed")  # pylint: disable=protected-access  # Reason: Accessing protected member _safe_close_websocket is necessary for connection disconnection implementation, this is part of the internal API
                logger.info("DEBUG: Successfully closed WebSocket by connection ID", connection_id=connection_id)
                del manager.active_websockets[connection_id]

            # Remove from player's connection list
            if player_id in manager.player_websockets and connection_id in manager.player_websockets[player_id]:
                manager.player_websockets[player_id].remove(connection_id)
                if not manager.player_websockets[player_id]:
                    del manager.player_websockets[player_id]

        # Clean up metadata
        del manager.connection_metadata[connection_id]

        # Clean up player data if no connections remain
        if not manager.has_websocket_connection(player_id):
            manager.rate_limiter.remove_player_data(str(player_id))
            manager.message_queue.remove_player_messages(str(player_id))
            if player_id in manager.last_seen:
                del manager.last_seen[player_id]
            manager.last_active_update_times.pop(player_id, None)
            manager.room_manager.remove_player_from_all_rooms(str(player_id))
            logger.info("Player has no remaining connections, cleaned up player data", player_id=player_id)

        logger.info(
            "Successfully disconnected connection", connection_type=connection_type, connection_id=connection_id
        )
        return True

    except (DatabaseError, AttributeError) as e:
        logger.error("Error disconnecting connection", connection_id=connection_id, error=str(e), exc_info=True)
        return False
