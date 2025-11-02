"""
Game mechanics API endpoints for MythosMUD server.

This module handles all game mechanics-related API operations including
game status, broadcasting, and real-time game state management.
"""

import datetime
from typing import Any

from fastapi import APIRouter, Depends, Request

from ..auth.users import get_current_user
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
def broadcast_message(
    message: str,
        request: Request = None,
    current_user: dict = Depends(get_current_user),
) -> dict[str, str]:
    """Broadcast a message to all connected players (admin only)."""
    logger.info("Broadcast message requested", user=current_user.get("username"), message=message)

    # TODO: Add admin role checking
    # For now, allow any authenticated user
    logger.warning(
        "Broadcast message sent without admin verification", user=current_user.get("username"), message=message
    )

    return {"message": f"Broadcast message: {message}"}
