"""
Server-Sent Events handler for MythosMUD real-time communication.

This module handles SSE event streaming, connection management,
and real-time game updates for clients.
"""

import asyncio
import time
from collections.abc import AsyncGenerator

from ..error_types import ErrorMessages, ErrorType, create_sse_error_response
from ..logging_config import get_logger
from .connection_manager import connection_manager
from .envelope import build_event, sse_line

logger = get_logger(__name__)


async def game_event_stream(player_id: str) -> AsyncGenerator[str, None]:
    """
    Generate a stream of game events for a player.

    Args:
        player_id: The player's ID

    Yields:
        str: SSE event data
    """
    # Convert player_id to string to ensure JSON serialization compatibility
    player_id_str = str(player_id)

    # Connect the SSE connection
    connection_manager.connect_sse(player_id_str)

    try:
        # Send initial connection event
        yield sse_line(build_event("connected", {"player_id": player_id_str}, player_id=player_id_str))

        # Send immediate heartbeat to confirm connection is working
        yield sse_line(build_event("heartbeat", {"message": "Connection established"}, player_id=player_id_str))

        # Send pending messages
        pending_messages = connection_manager.get_pending_messages(player_id_str)
        for message in pending_messages:
            yield sse_line(build_event("pending_message", message, player_id=player_id_str))

        # Main event loop
        while True:
            try:
                # Send heartbeat every 30 seconds
                await asyncio.sleep(30)
                # Mark presence and send heartbeat
                connection_manager.mark_player_seen(player_id_str)
                connection_manager.prune_stale_players()
                # Clean up orphaned data every 5 minutes (10 heartbeats)
                if int(time.time() / 30) % 10 == 0:  # Every 5 minutes
                    await connection_manager.cleanup_orphaned_data()
                yield sse_line(build_event("heartbeat", {}, player_id=player_id_str))

            except asyncio.CancelledError:
                logger.info(f"SSE stream cancelled for player {player_id_str}")
                break

            except Exception as e:
                logger.error(f"Error in SSE stream for player {player_id_str}: {e}")
                error_response = create_sse_error_response(
                    ErrorType.SSE_ERROR,
                    f"Stream error occurred: {str(e)}",
                    ErrorMessages.SSE_ERROR,
                    {"player_id": player_id_str},
                )
                yield sse_line(build_event("error", error_response, player_id=player_id_str))
                break

    finally:
        # Clean up connection
        connection_manager.disconnect_sse(player_id_str)


def format_sse_event(event_type: str, data: dict) -> str:  # Backward compat shim
    """Deprecated: use sse_line(build_event(...))."""
    return sse_line(build_event(event_type, data))


async def send_game_event(player_id: str, event_type: str, data: dict):
    """
    Send a game event to a specific player via SSE.

    Args:
        player_id: The player's ID
        event_type: The type of event
        data: The event data
    """
    try:
        # Convert player_id to string to ensure JSON serialization compatibility
        player_id_str = str(player_id)
        await connection_manager.send_personal_message(
            player_id_str, build_event(event_type, data, player_id=player_id_str)
        )

    except Exception as e:
        logger.error(f"Error sending game event to {player_id}: {e}")


async def broadcast_game_event(event_type: str, data: dict, exclude_player: str = None):
    """
    Broadcast a game event to all connected players.

    Args:
        event_type: The type of event
        data: The event data
        exclude_player: Player ID to exclude from broadcast
    """
    try:
        await connection_manager.broadcast_global(build_event(event_type, data), exclude_player)

    except Exception as e:
        logger.error(f"Error broadcasting game event: {e}")


async def send_room_event(room_id: str, event_type: str, data: dict, exclude_player: str = None):
    """
    Send a room event to all players in a specific room.

    Args:
        room_id: The room's ID
        event_type: The type of event
        data: The event data
        exclude_player: Player ID to exclude from broadcast
    """
    try:
        await connection_manager.broadcast_to_room(
            room_id, build_event(event_type, data, room_id=room_id), exclude_player
        )

    except Exception as e:
        logger.error(f"Error sending room event to room {room_id}: {e}")


async def send_system_notification(player_id: str, message: str, notification_type: str = "info"):
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

    except Exception as e:
        logger.error(f"Error sending system notification to {player_id}: {e}")


async def send_player_status_update(player_id: str, status_data: dict):
    """
    Send a player status update to a player.

    Args:
        player_id: The player's ID
        status_data: The status data to send
    """
    try:
        await send_game_event(player_id, "player_status", status_data)

    except Exception as e:
        logger.error(f"Error sending status update to {player_id}: {e}")


async def send_room_description(player_id: str, room_data: dict):
    """
    Send room description to a player.

    Args:
        player_id: The player's ID
        room_data: The room data to send
    """
    try:
        await send_game_event(player_id, "room_description", room_data)

    except Exception as e:
        logger.error(f"Error sending room description to {player_id}: {e}")
