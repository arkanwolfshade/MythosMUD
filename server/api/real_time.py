"""
Real-time communication API endpoints for MythosMUD server.

This module handles WebSocket connections, Server-Sent Events,
and real-time game status endpoints.
"""

import datetime

from fastapi import APIRouter, Depends, HTTPException, Request, WebSocket
from fastapi.responses import StreamingResponse

from ..auth.users import get_current_user
from ..real_time import connection_manager, game_event_stream, websocket_endpoint

# Create real-time router
realtime_router = APIRouter(tags=["realtime"])


@realtime_router.get("/events/{player_id}")
async def game_events_stream(player_id: str, request: Request):
    """
    Server-Sent Events stream for real-time game updates.

    This endpoint provides a persistent connection for receiving game state updates,
    room changes, combat events, and other real-time information.

    Authentication is handled via JWT token in query parameter or Authorization header.
    The player_id parameter should be the player name, not the UUID.
    """
    # Extract token from query parameter or Authorization header
    token = request.query_params.get("token")
    if not token:
        auth_header = request.headers.get("Authorization")
        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header[7:]  # Remove "Bearer " prefix

    if not token:
        raise HTTPException(status_code=401, detail="Authentication token required")

    # Validate the token and get user information
    try:
        # TODO: Implement SSE token validation for new auth system
        user_info = {"user_id": "test_user"}  # Placeholder
        authenticated_username = user_info["username"]
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid authentication token") from None

    # Verify the authenticated user matches the requested player
    # Get the player from persistence to check if the player_id matches
    persistence = request.app.state.persistence
    player = persistence.get_player_by_name(authenticated_username)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found in database")

    # Compare the authenticated username with the requested player_id (which should be the player name)
    if authenticated_username != player_id:
        raise HTTPException(status_code=403, detail="Access denied: token does not match player ID")

    # Get security headers for SSE
    # TODO: Implement SSE auth headers for new auth system
    security_headers = {}  # Placeholder

    return StreamingResponse(
        game_event_stream(player_id),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Cache-Control",
            **security_headers,
        },
    )


@realtime_router.websocket("/ws/{player_id}")
async def websocket_endpoint_route(websocket: WebSocket, player_id: str):
    """
    WebSocket endpoint for interactive commands and chat.

    This endpoint handles bidirectional communication for:
    - Game commands (look, go, attack, etc.)
    - Chat messages
    - Real-time interactions

    Authentication is handled via JWT token in query parameter.
    The player_id parameter should be the player name, not the UUID.
    """
    # Extract token from query parameter
    token = websocket.query_params.get("token")
    if not token:
        await websocket.close(code=4001, reason="Authentication token required")
        return

    # Validate the token
    try:
        # TODO: Implement SSE token validation for new auth system
        user_info = {"user_id": "test_user"}  # Placeholder
        authenticated_username = user_info["username"]
    except Exception:
        await websocket.close(code=4001, reason="Invalid authentication token")
        return

    # Verify the authenticated user matches the requested player
    # Get the player from persistence to check if the player_id matches
    from ..persistence import get_persistence

    persistence = get_persistence()
    player = persistence.get_player_by_name(authenticated_username)
    if not player:
        await websocket.close(code=4004, reason="Player not found in database")
        return

    # Compare the authenticated username with the requested player_id (which should be the player name)
    if authenticated_username != player_id:
        await websocket.close(code=4003, reason="Access denied: token does not match player ID")
        return

    # Proceed with the WebSocket connection
    await websocket_endpoint(websocket, player_id)


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
