"""
Public API utility functions for connection manager.

This module provides convenient wrapper functions for sending events
through the connection manager without requiring direct access to the
ConnectionManager instance.
"""

import uuid

from ..exceptions import DatabaseError
from ..structured_logging.enhanced_logging_config import get_logger
from .connection_manager import resolve_connection_manager

logger = get_logger(__name__)


async def send_game_event(player_id: uuid.UUID | str, event_type: str, data: dict) -> None:
    """
    Send a game event to a specific player via WebSocket.

    Args:
        player_id: The player's ID (UUID or string)
        event_type: The type of event
        data: The event data
    """
    try:
        from .envelope import build_event

        manager = resolve_connection_manager()
        if manager is None:
            raise RuntimeError("Connection manager not available")
        # Convert player_id to UUID if it's a string
        if isinstance(player_id, str):
            try:
                player_id_uuid = uuid.UUID(player_id)
            except (ValueError, AttributeError):
                logger.error("Invalid player_id format", player_id=player_id)
                return
        else:
            player_id_uuid = player_id
        # Pass UUID object directly to build_event (it accepts UUID | str)
        await manager.send_personal_message(player_id_uuid, build_event(event_type, data, player_id=player_id_uuid))

    except (DatabaseError, AttributeError) as e:
        logger.error("Error sending game event", player_id=player_id, error=str(e))


async def broadcast_game_event(event_type: str, data: dict, exclude_player: str | None = None) -> None:
    """
    Broadcast a game event to all connected players.

    Args:
        event_type: The type of event
        data: The event data
        exclude_player: Player ID to exclude from broadcast
    """
    try:
        from .envelope import build_event

        manager = resolve_connection_manager()
        if manager is None:
            raise RuntimeError("Connection manager not available")
        await manager.broadcast_global(build_event(event_type, data), exclude_player)

    except (DatabaseError, AttributeError) as e:
        logger.error("Error broadcasting game event", error=str(e))


async def send_room_event(room_id: str, event_type: str, data: dict, exclude_player: str | None = None) -> None:
    """
    Send a room event to all players in a specific room.

    Args:
        room_id: The room's ID
        event_type: The type of event
        data: The event data
        exclude_player: Player ID to exclude from broadcast
    """
    try:
        from .envelope import build_event

        manager = resolve_connection_manager()
        if manager is None:
            raise RuntimeError("Connection manager not available")
        await manager.broadcast_to_room(
            room_id,
            build_event(event_type, data, room_id=room_id),
            exclude_player,
        )

    except (DatabaseError, AttributeError) as e:
        logger.error("Error sending room event", room_id=room_id, error=str(e))


async def send_system_notification(player_id: uuid.UUID | str, message: str, notification_type: str = "info") -> None:
    """
    Send a system notification to a player.

    Args:
        player_id: The player's ID
        message: The notification message
        notification_type: The type of notification (info, warning, error)
    """
    try:
        notification_data = {
            "message": message,
            "notification_type": notification_type,
        }

        await send_game_event(player_id, "system_notification", notification_data)

    except (DatabaseError, AttributeError) as e:
        logger.error("Error sending system notification", player_id=player_id, error=str(e))


async def send_player_status_update(player_id: uuid.UUID | str, status_data: dict) -> None:
    """
    Send a player status update to a player.

    Args:
        player_id: The player's ID
        status_data: The status data to send
    """
    try:
        await send_game_event(player_id, "player_status", status_data)

    except (DatabaseError, AttributeError) as e:
        logger.error("Error sending status update", player_id=player_id, error=str(e))


async def send_room_description(player_id: uuid.UUID | str, room_data: dict) -> None:
    """
    Send room description to a player.

    Args:
        player_id: The player's ID
        room_data: The room data to send
    """
    try:
        await send_game_event(player_id, "room_description", room_data)

    except (DatabaseError, AttributeError) as e:
        logger.error("Error sending room description", player_id=player_id, error=str(e))
