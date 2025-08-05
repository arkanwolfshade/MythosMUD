"""
Game mechanics API endpoints for MythosMUD server.

This module handles all game mechanics-related API operations including
game status, broadcasting, and real-time game state management.
"""

import datetime

from fastapi import APIRouter, Depends, Request

from ..auth.users import get_current_user
from ..realtime.connection_manager import connection_manager

# Create game router
game_router = APIRouter(prefix="/game", tags=["game"])


@game_router.get("/status")
def get_game_status(request: Request = None):
    """Get current game status and connection information."""
    return {
        "active_connections": connection_manager.get_active_connection_count(),
        "active_players": len(connection_manager.player_websockets),
        "room_subscriptions": len(connection_manager.room_subscriptions),
        "server_time": datetime.datetime.utcnow().isoformat(),
    }


@game_router.post("/broadcast")
def broadcast_message(
    message: str,
    current_user: dict = Depends(get_current_user),
    request: Request = None,
):
    """Broadcast a message to all connected players (admin only)."""
    # TODO: Add admin role checking
    # For now, allow any authenticated user
    return {"message": f"Broadcast message: {message}"}
