"""
Real-time communication API endpoints for MythosMUD server.

This module handles WebSocket connections and Server-Sent Events
for real-time game communication.
"""

from fastapi import APIRouter, Request, WebSocket
from fastapi.responses import StreamingResponse

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
