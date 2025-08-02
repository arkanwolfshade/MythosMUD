"""
Real-time communication API endpoints for MythosMUD server.

This module handles WebSocket connections, Server-Sent Events,
and real-time game status endpoints.
"""

import datetime

from fastapi import APIRouter, Depends, Request, WebSocket
from fastapi.responses import StreamingResponse

from ..auth.users import get_current_user
from ..realtime.connection_manager import connection_manager
from ..realtime.sse_handler import game_event_stream
from ..realtime.websocket_handler import handle_websocket_connection

# Create real-time router
realtime_router = APIRouter(tags=["realtime"])


@realtime_router.get("/events/{player_id}")
async def sse_events(player_id: str, request: Request):
    """
    Server-Sent Events stream for real-time game updates.
    """
    # TODO: Add authentication and player validation as needed
    return StreamingResponse(
        game_event_stream(player_id),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Cache-Control",
        },
    )


@realtime_router.websocket("/ws/{player_id}")
async def websocket_endpoint_route(websocket: WebSocket, player_id: str):
    """
    WebSocket endpoint for interactive commands and chat.
    """
    # TODO: Add authentication and player validation as needed
    await handle_websocket_connection(websocket, player_id)


@realtime_router.get("/game/status")
def get_game_status():
    """Get current game status and connection information."""
    return {
        "active_connections": connection_manager.get_active_connection_count(),
        "active_players": len(connection_manager.player_websockets),
        "room_subscriptions": len(connection_manager.room_subscriptions),
        "server_time": datetime.datetime.utcnow().isoformat(),
    }


@realtime_router.post("/game/broadcast")
def broadcast_message(message: str, current_user: dict = Depends(get_current_user)):
    """Broadcast a message to all connected players (admin only)."""
    # TODO: Add admin role checking
    # For now, allow any authenticated user
    return {"message": f"Broadcast message: {message}"}
