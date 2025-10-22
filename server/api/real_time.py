"""
Real-time communication API endpoints for MythosMUD server.

This module handles WebSocket connections and Server-Sent Events
for real-time game communication.
"""

import time

from fastapi import APIRouter, Request, WebSocket
from fastapi.responses import StreamingResponse

from ..auth_utils import decode_access_token
from ..exceptions import LoggedHTTPException
from ..persistence import get_persistence
from ..realtime.sse_handler import game_event_stream
from ..realtime.websocket_handler import handle_websocket_connection
from ..utils.error_logging import create_context_from_request, create_context_from_websocket

# Create real-time router
realtime_router = APIRouter(prefix="/api", tags=["realtime"])


@realtime_router.get("/events/{player_id}")
async def sse_events(player_id: str, request: Request):
    """
    Server-Sent Events stream for real-time game updates.
    Supports session tracking for dual connection management.
    """
    # Get session parameter
    session_id = request.query_params.get("session_id")

    # TODO: Add authentication and player validation as needed
    return StreamingResponse(
        game_event_stream(player_id, session_id),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Cache-Control",
        },
    )


@realtime_router.get("/events")
async def sse_events_token(request: Request):
    """
    Token-authenticated SSE stream. Resolves player_id from JWT token (query param 'token').
    Supports session tracking for dual connection management.
    """
    from ..logging.enhanced_logging_config import get_logger

    logger = get_logger(__name__)
    token = request.query_params.get("token")
    session_id = request.query_params.get("session_id")  # New session parameter

    payload = decode_access_token(token)
    if not payload or "sub" not in payload:
        context = create_context_from_request(request)
        raise LoggedHTTPException(status_code=401, detail="Invalid or missing token", context=context)
    user_id = str(payload["sub"]).strip()
    persistence = get_persistence()
    player = persistence.get_player_by_user_id(user_id)
    if not player:
        context = create_context_from_request(request)
        context.user_id = user_id
        raise LoggedHTTPException(status_code=401, detail="User has no player record", context=context)
    player_id = player.player_id
    logger.info(f"SSE connection attempt for player {player_id} with session {session_id}")

    return StreamingResponse(
        game_event_stream(player_id, session_id),
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
    Supports session tracking for dual connection management.
    """
    from ..logging.enhanced_logging_config import get_logger

    logger = get_logger(__name__)

    # Accept query token, resolve to user and then to player_id
    token = websocket.query_params.get("token")
    session_id = websocket.query_params.get("session_id")  # New session parameter

    payload = decode_access_token(token)
    if not payload or "sub" not in payload:
        # Fallback: allow anonymous connection only for tests (no identity)
        player_id = websocket.query_params.get("player_id")
        if not player_id:
            context = create_context_from_websocket(websocket)
            raise LoggedHTTPException(status_code=401, detail="Invalid or missing token", context=context)

        # CRITICAL FIX: Validate that the test player exists
        persistence = get_persistence()
        player = persistence.get_player(player_id)
        if not player:
            logger.warning(f"WebSocket connection attempt for non-existent player: {player_id}")
            context = create_context_from_websocket(websocket)
            context.user_id = player_id
            raise LoggedHTTPException(status_code=404, detail=f"Player {player_id} not found", context=context)
    else:
        user_id = str(payload["sub"]).strip()
        persistence = get_persistence()
        player = persistence.get_player_by_user_id(user_id)
        if not player:
            context = create_context_from_websocket(websocket)
            context.user_id = user_id
            raise LoggedHTTPException(status_code=401, detail="User has no player record", context=context)
        player_id = player.player_id

    logger.info(f"WebSocket connection attempt for player {player_id} with session {session_id}")

    try:
        await handle_websocket_connection(websocket, player_id, session_id)
    except Exception as e:
        logger.error(f"Error in WebSocket endpoint for player {player_id}: {e}", exc_info=True)
        raise


@realtime_router.get("/connections/{player_id}")
async def get_player_connections(player_id: str, request: Request):
    """
    Get connection information for a player.
    Returns detailed connection metadata including session information.
    """
    from ..logging.enhanced_logging_config import get_logger
    from ..realtime.connection_manager import connection_manager

    logger = get_logger(__name__)

    # Get connection information
    presence_info = connection_manager.get_player_presence_info(player_id)

    # Get session information
    session_id = connection_manager.get_player_session(player_id)
    session_connections = connection_manager.get_session_connections(session_id) if session_id else []

    # Get connection health
    health_info = await connection_manager.check_connection_health(player_id)

    connection_data = {
        "player_id": player_id,
        "presence": presence_info,
        "session": {
            "session_id": session_id,
            "session_connections": session_connections,
            "is_valid": connection_manager.validate_session(player_id, session_id) if session_id else False,
        },
        "health": health_info,
        "timestamp": time.time(),
    }

    logger.info(f"Connection info requested for player {player_id}")
    return connection_data


@realtime_router.post("/connections/{player_id}/session")
async def handle_new_game_session(player_id: str, request: Request):
    """
    Handle a new game session for a player.
    This will disconnect existing connections and establish a new session.
    """
    import json

    from ..logging.enhanced_logging_config import get_logger
    from ..realtime.connection_manager import connection_manager

    logger = get_logger(__name__)

    try:
        # Get new session ID from request body
        body = await request.json()
        new_session_id = body.get("session_id")

        if not new_session_id:
            context = create_context_from_request(request)
            context.user_id = player_id
            raise LoggedHTTPException(status_code=400, detail="session_id is required", context=context)

        # Handle new game session
        session_results = await connection_manager.handle_new_game_session(player_id, new_session_id)

        logger.info(f"New game session handled for player {player_id}: {session_results}")
        return session_results

    except json.JSONDecodeError as e:
        context = create_context_from_request(request)
        context.user_id = player_id
        raise LoggedHTTPException(status_code=400, detail="Invalid JSON in request body", context=context) from e
    except Exception as e:
        logger.error(f"Error handling new game session for player {player_id}: {e}", exc_info=True)
        context = create_context_from_request(request)
        context.user_id = player_id
        raise LoggedHTTPException(
            status_code=500, detail=f"Error handling new game session: {str(e)}", context=context
        ) from e


@realtime_router.get("/connections/stats")
async def get_connection_statistics(request: Request):
    """
    Get comprehensive connection statistics.
    Returns detailed statistics about all connections, sessions, and presence.
    """
    from ..logging.enhanced_logging_config import get_logger
    from ..realtime.connection_manager import connection_manager

    logger = get_logger(__name__)

    # Get various statistics
    presence_stats = connection_manager.get_presence_statistics()
    session_stats = connection_manager.get_session_stats()
    error_stats = connection_manager.get_error_statistics()

    statistics = {
        "presence": presence_stats,
        "sessions": session_stats,
        "errors": error_stats,
        "timestamp": time.time(),
    }

    logger.info("Connection statistics requested")
    return statistics


@realtime_router.websocket("/ws/{player_id}")
async def websocket_endpoint_route(websocket: WebSocket, player_id: str):
    """
    Backward-compatible WebSocket endpoint that accepts a path player_id but
    prefers JWT token identity when provided.
    Supports session tracking for dual connection management.
    """
    from ..logging.enhanced_logging_config import get_logger

    logger = get_logger(__name__)

    # Get session parameter
    session_id = websocket.query_params.get("session_id")
    logger.info(f"WebSocket (compat) connection attempt for player {player_id} with session {session_id}")

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
        await handle_websocket_connection(websocket, resolved_player_id, session_id)
    except Exception as e:
        logger.error(f"Error in WebSocket endpoint for player {player_id}: {e}", exc_info=True)
        raise
