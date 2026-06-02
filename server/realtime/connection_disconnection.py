"""
Connection disconnection management for connection manager.

This module handles WebSocket connection disconnection operations.
"""

import uuid
from typing import Protocol

from anyio import Lock
from fastapi import WebSocket

from ..exceptions import DatabaseError
from ..structured_logging.enhanced_logging_config import get_logger
from .connection_manager_methods import safe_close_websocket_impl
from .connection_models import ConnectionMetadata
from .message_queue import MessageQueue
from .rate_limiter import RateLimiter
from .room_subscription_manager import RoomSubscriptionManager

logger = get_logger(__name__)


class _DisconnectConnectionManager(Protocol):
    """Connection manager surface used by disconnection helpers."""

    active_websockets: dict[str, WebSocket]
    connection_metadata: dict[str, ConnectionMetadata]
    player_websockets: dict[uuid.UUID, list[str]]
    rate_limiter: RateLimiter
    message_queue: MessageQueue
    room_manager: RoomSubscriptionManager
    processed_disconnects: set[uuid.UUID]
    last_seen: dict[uuid.UUID, float]
    last_active_update_times: dict[uuid.UUID, float]
    disconnect_lock: Lock
    processed_disconnect_lock: Lock

    def has_websocket_connection(self, player_id: uuid.UUID) -> bool:
        """Return True when the player still has at least one WebSocket connection."""
        ...


def _cleanup_connection_tracking(connection_id: str, manager: _DisconnectConnectionManager) -> None:
    """Remove connection registry entries; safe when already cleaned up elsewhere."""
    _ = manager.active_websockets.pop(connection_id, None)
    _ = manager.connection_metadata.pop(connection_id, None)
    manager.rate_limiter.remove_connection_message_data(connection_id)


async def _disconnect_single_websocket(
    connection_id: str, player_id: uuid.UUID, manager: _DisconnectConnectionManager
) -> None:
    """Close one WebSocket and clean tracking. Idempotent for duplicate disconnect calls."""
    websocket = manager.active_websockets.get(connection_id)
    if websocket is None:
        _cleanup_connection_tracking(connection_id, manager)
        return

    logger.info("DEBUG: Closing WebSocket", connection_id=connection_id, player_id=player_id)
    await safe_close_websocket_impl(manager, websocket, code=1000, reason="Connection closed")
    logger.info("Successfully closed WebSocket", connection_id=connection_id, player_id=player_id)
    _cleanup_connection_tracking(connection_id, manager)


async def _disconnect_all_websockets(
    connection_ids: list[str], player_id: uuid.UUID, manager: _DisconnectConnectionManager
) -> None:
    """
    Disconnect all WebSocket connections for a player.

    Args:
        connection_ids: List of connection IDs to disconnect
        player_id: The player's ID
        manager: ConnectionManager instance
    """
    for connection_id in connection_ids:
        await _disconnect_single_websocket(connection_id, player_id, manager)


async def _track_disconnect_if_needed(
    player_id: uuid.UUID, manager: _DisconnectConnectionManager, is_force_disconnect: bool
) -> bool:
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


def _cleanup_room_subscriptions(
    player_id: uuid.UUID, manager: _DisconnectConnectionManager, is_force_disconnect: bool
) -> None:
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

    _ = manager.room_manager.remove_player_from_all_rooms(str(player_id))


def _cleanup_player_data(player_id: uuid.UUID, manager: _DisconnectConnectionManager) -> None:
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
    _ = manager.last_active_update_times.pop(player_id, None)


async def cleanup_websocket_disconnect(
    player_id: uuid.UUID,
    manager: _DisconnectConnectionManager,
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


async def _disconnect_websocket_by_connection_id(
    connection_id: str, player_id: uuid.UUID, manager: _DisconnectConnectionManager
) -> None:
    """Close one WebSocket by connection ID and update player_websockets tracking."""
    websocket = manager.active_websockets.pop(connection_id, None)
    if websocket is not None:
        logger.info("DEBUG: Closing WebSocket by connection ID", connection_id=connection_id)
        await safe_close_websocket_impl(manager, websocket, code=1000, reason="Connection closed")
        logger.info("DEBUG: Successfully closed WebSocket by connection ID", connection_id=connection_id)

    if player_id in manager.player_websockets and connection_id in manager.player_websockets[player_id]:
        manager.player_websockets[player_id].remove(connection_id)
        if not manager.player_websockets[player_id]:
            del manager.player_websockets[player_id]


def _cleanup_fully_disconnected_player(player_id: uuid.UUID, manager: _DisconnectConnectionManager) -> None:
    """Remove player-scoped tracking when no websocket connections remain."""
    if manager.has_websocket_connection(player_id):
        return

    _cleanup_player_data(player_id, manager)
    _cleanup_room_subscriptions(player_id, manager, is_force_disconnect=False)
    logger.info("Player has no remaining connections, cleaned up player data", player_id=player_id)


async def disconnect_connection_by_id_impl(
    connection_id: str,
    manager: _DisconnectConnectionManager,
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

        metadata: ConnectionMetadata = manager.connection_metadata[connection_id]
        player_id = metadata.player_id
        connection_type = metadata.connection_type

        logger.info(
            "Disconnecting connection",
            connection_type=connection_type,
            connection_id=connection_id,
            player_id=player_id,
        )

        if connection_type == "websocket":
            await _disconnect_websocket_by_connection_id(connection_id, player_id, manager)

        _ = manager.connection_metadata.pop(connection_id, None)
        manager.rate_limiter.remove_connection_message_data(connection_id)
        _cleanup_fully_disconnected_player(player_id, manager)

        logger.info(
            "Successfully disconnected connection", connection_type=connection_type, connection_id=connection_id
        )
        return True

    except (DatabaseError, AttributeError) as e:
        logger.error("Error disconnecting connection", connection_id=connection_id, error=str(e), exc_info=True)
        return False
