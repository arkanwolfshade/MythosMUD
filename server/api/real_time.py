"""
Real-time communication API endpoints for MythosMUD server.

This module handles WebSocket connections and Server-Sent Events
for real-time game communication.
"""

from fastapi import APIRouter, HTTPException, Request, WebSocket
from fastapi.responses import StreamingResponse

from ..auth_utils import decode_access_token
from ..persistence import get_persistence
from ..realtime.sse_handler import game_event_stream
from ..realtime.websocket_handler import handle_websocket_connection

# Create real-time router
realtime_router = APIRouter(prefix="/api", tags=["realtime"])


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


@realtime_router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """
    WebSocket endpoint for interactive commands and chat.
    """
    from ..logging_config import get_logger

    logger = get_logger(__name__)
    # Accept query token, resolve to user and then to player_id
    token = websocket.query_params.get("token")
    payload = decode_access_token(token)
    if not payload or "sub" not in payload:
        # Fallback: allow anonymous connection only for tests (no identity)
        player_id = websocket.query_params.get("player_id")
        if not player_id:
            raise HTTPException(status_code=401, detail="Invalid or missing token")
    else:
        user_id = str(payload["sub"]).strip()
        persistence = get_persistence()
        player = persistence.get_player_by_user_id(user_id)
        if not player:
            raise HTTPException(status_code=401, detail="User has no player record")
        player_id = player.player_id
    logger.info(f"WebSocket connection attempt for player {player_id}")

    try:
        await handle_websocket_connection(websocket, player_id)
    except Exception as e:
        logger.error(f"Error in WebSocket endpoint for player {player_id}: {e}", exc_info=True)
        raise


@realtime_router.websocket("/ws/{player_id}")
async def websocket_endpoint_route(websocket: WebSocket, player_id: str):
    """
    Backward-compatible WebSocket endpoint that accepts a path player_id but
    prefers JWT token identity when provided.
    """
    from ..logging_config import get_logger

    logger = get_logger(__name__)
    logger.info(f"WebSocket (compat) connection attempt for player {player_id}")

    try:
        token = websocket.query_params.get("token")
        resolved_player_id = player_id
        payload = decode_access_token(token)
        if payload and "sub" in payload:
            user_id = str(payload["sub"]).strip()
            persistence = get_persistence()
            player = persistence.get_player_by_user_id(user_id)
            if player:
                resolved_player_id = player.player_id
        await handle_websocket_connection(websocket, resolved_player_id)
    except Exception as e:
        logger.error(f"Error in WebSocket endpoint for player {player_id}: {e}", exc_info=True)
        raise
