"""
Game mechanics API endpoints for MythosMUD server.

This module handles all game mechanics-related API operations including
game status, broadcasting, and real-time game state management.
"""

import datetime
from typing import Any

from fastapi import APIRouter, Depends, Request

from ..auth.dependencies import get_current_superuser
from ..logging.enhanced_logging_config import get_logger
from ..realtime.connection_manager import connection_manager

logger = get_logger(__name__)

# Create game router
game_router = APIRouter(prefix="/game", tags=["game"])

logger.info("Game API router initialized", prefix="/game")


@game_router.get("/status")
def get_game_status(request: Request) -> dict[str, Any]:
    """Get current game status and connection information."""
    logger.debug("Game status requested")

    status_data = {
        "active_connections": connection_manager.get_active_connection_count(),
        "active_players": len(connection_manager.player_websockets),
        "room_subscriptions": len(connection_manager.room_subscriptions),
        "server_time": datetime.datetime.now(datetime.UTC).isoformat(),
    }

    logger.debug(
        "Game status returned",
        active_connections=status_data["active_connections"],
        active_players=status_data["active_players"],
        room_subscriptions=status_data["room_subscriptions"],
    )

    return status_data


@game_router.post("/broadcast")
async def broadcast_message(
    message: str,
    current_user: Any = Depends(get_current_superuser),
) -> dict[str, str | int]:
    """
    Broadcast a message to all connected players (admin only).

    Requires superuser privileges. Returns 403 for non-admin users.
    """
    logger.info(
        "Admin broadcast message requested",
        admin_username=current_user.username,
        admin_id=str(current_user.id),
        message=message,
    )

    # Broadcast to all connected players via connection manager
    # Use broadcast_global_event to send a system broadcast
    broadcast_stats = await connection_manager.broadcast_global_event(
        event_type="system_broadcast",
        data={
            "message": message,
            "broadcaster": current_user.username,
            "broadcaster_id": str(current_user.id),
        },
    )

    recipients = broadcast_stats.get("successful_deliveries", 0)

    logger.info(
        "Admin broadcast completed",
        admin_username=current_user.username,
        recipients=recipients,
        message=message,
        broadcast_stats=broadcast_stats,
    )

    return {
        "message": message,
        "recipients": recipients,
        "broadcaster": current_user.username,
        "broadcast_stats": broadcast_stats,
    }
