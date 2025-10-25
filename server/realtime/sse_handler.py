"""
Server-Sent Events handler for MythosMUD real-time communication.

This module handles SSE event streaming, connection management,
and real-time game updates for clients.
"""

import asyncio
import time
from collections.abc import AsyncGenerator

from ..error_types import ErrorMessages, ErrorType, create_sse_error_response
from ..logging.enhanced_logging_config import get_logger
from .connection_manager import connection_manager
from .envelope import build_event, sse_line

logger = get_logger(__name__)


async def game_event_stream(player_id: str, session_id: str | None = None) -> AsyncGenerator[str, None]:
    """
    Generate a stream of game events for a player.

    Args:
        player_id: The player's ID
        session_id: Optional session ID for dual connection management

    Yields:
        str: SSE event data
    """
    # Convert player_id to string to ensure JSON serialization compatibility
    player_id_str = str(player_id)

    # Connect the SSE connection with session tracking
    await connection_manager.connect_sse(player_id_str, session_id)

    try:
        # Send initial connection event
        yield sse_line(build_event("connected", {"player_id": player_id_str}, player_id=player_id_str))

        # Send immediate heartbeat to confirm connection is working
        logger.debug("DEBUG: SSE session established", player_id=player_id_str)
        yield sse_line(build_event("heartbeat", {"message": "Connection established"}, player_id=player_id_str))

        # Clear any pending messages to ensure fresh game state
        if player_id_str in connection_manager.pending_messages:
            del connection_manager.pending_messages[player_id_str]

        # Send pending messages (should be empty now)
        pending_messages = connection_manager.get_pending_messages(player_id_str)
        for message in pending_messages:
            yield sse_line(build_event("pending_message", message, player_id=player_id_str))

        # Main event loop with comprehensive cancellation boundaries
        while True:
            try:
                # Send heartbeat every 30 seconds with proper cancellation handling
                await asyncio.sleep(30)

                # Mark presence and send heartbeat with timeout protection
                logger.debug("DEBUG: SSE heartbeat", player_id=player_id_str)
                connection_manager.mark_player_seen(player_id_str)
                connection_manager.prune_stale_players()

                # Clean up orphaned data every 5 minutes (10 heartbeats) with timeout boundaries
                if int(time.time() / 30) % 10 == 0:  # Every 5 minutes
                    try:
                        await asyncio.wait_for(
                            connection_manager.cleanup_orphaned_data(),
                            timeout=5.0,  # 5-second timeout for cleanup operations
                        )
                    except TimeoutError:
                        logger.warning("Cleanup operation timed out", player_id=player_id_str)
                    except asyncio.CancelledError:
                        logger.info("Cleanup cancelled", player_id=player_id_str)
                        raise  # Re-raise cancelled error to properly handle in outer try/except
                    except Exception as cleanup_error:
                        logger.error("Cleanup error", player_id=player_id_str, error=str(cleanup_error))

                yield sse_line(build_event("heartbeat", {}, player_id=player_id_str))

            except asyncio.CancelledError:
                logger.info("SSE stream cancelled", player_id=player_id_str)
                break

            except Exception as e:
                logger.error("Error in SSE stream", player_id=player_id_str, error=str(e))
                error_response = create_sse_error_response(
                    ErrorType.SSE_ERROR,
                    f"Stream error occurred: {str(e)}",
                    ErrorMessages.SSE_ERROR,
                    {"player_id": player_id_str},
                )
                yield sse_line(build_event("error", error_response, player_id=player_id_str))
                break

    finally:
        # Clean up connection - ensure graceful disconnect with error handling
        try:
            connection_manager.disconnect_sse(player_id_str)
        except Exception as cleanup_error:
            logger.error("SSE disconnect error", player_id=player_id_str, error=str(cleanup_error))
            # Attempt final cleanup notwithstanding disconnect errors
            try:
                # Force disconnect without throwing exceptions to prevent finally block failure
                connection_manager.disconnect_sse(player_id_str)
            except Exception as final_error:
                logger.error("Final SSE cleanup failed", player_id=player_id_str, error=str(final_error))


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
        logger.error("Error sending game event", player_id=player_id, error=str(e))


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
        logger.error("Error broadcasting game event", error=str(e))


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
        logger.error("Error sending room event", room_id=room_id, error=str(e))


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
        logger.error("Error sending system notification", player_id=player_id, error=str(e))


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
        logger.error("Error sending status update", player_id=player_id, error=str(e))


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
        logger.error("Error sending room description", player_id=player_id, error=str(e))
