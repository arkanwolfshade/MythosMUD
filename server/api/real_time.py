"""
Real-time communication API endpoints for MythosMUD server.

This module handles WebSocket connections and Server-Sent Events
for real-time game communication.
"""

import time
from typing import Any

from fastapi import APIRouter, HTTPException, Request, WebSocket
from fastapi.responses import StreamingResponse

from ..auth_utils import decode_access_token
from ..exceptions import LoggedHTTPException
from ..persistence import get_persistence
from ..realtime.connection_manager import resolve_connection_manager, set_global_connection_manager
from ..realtime.sse_handler import game_event_stream
from ..realtime.websocket_handler import handle_websocket_connection
from ..utils.error_logging import create_context_from_request, create_context_from_websocket

# AI Agent: Don't import app at module level - causes circular import!
#           Import locally in functions instead

# Create real-time router
realtime_router = APIRouter(prefix="/api", tags=["realtime"])


def _resolve_connection_manager_from_state(state) -> Any:
    container = getattr(state, "container", None)
    candidate = getattr(container, "connection_manager", None) if container else None
    manager = resolve_connection_manager(candidate)
    if manager is not None:
        set_global_connection_manager(manager)
    return manager


def _ensure_connection_manager(state) -> Any:
    connection_manager = _resolve_connection_manager_from_state(state)
    if connection_manager is None:
        raise HTTPException(status_code=503, detail="Service temporarily unavailable")
    set_global_connection_manager(connection_manager)
    return connection_manager


@realtime_router.get("/events/{player_id}")
async def sse_events(player_id: str, request: Request) -> StreamingResponse:
    """
    Server-Sent Events stream for real-time game updates.
    Supports session tracking for dual connection management.
    """
    # Get session parameter
    session_id = request.query_params.get("session_id")

    # TODO: Add authentication and player validation as needed
    # Note: CORS is handled by global middleware; avoid environment-specific logic here
    headers = {
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "Cache-Control",
    }

    connection_manager = _ensure_connection_manager(request.app.state)
    if getattr(connection_manager, "persistence", None) is None:
        raise HTTPException(status_code=503, detail="Service temporarily unavailable")

    return StreamingResponse(
        game_event_stream(player_id, session_id),
        media_type="text/event-stream",
        headers=headers,
    )


@realtime_router.get("/events")
async def sse_events_token(request: Request) -> StreamingResponse:
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
    player_id = str(player.player_id)
    logger.info("SSE connection attempt", player_id=player_id, session_id=session_id)

    # Note: CORS is handled by global middleware; avoid environment-specific logic here
    headers = {
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "Cache-Control",
    }

    connection_manager = _ensure_connection_manager(request.app.state)
    if getattr(connection_manager, "persistence", None) is None:
        raise HTTPException(status_code=503, detail="Service temporarily unavailable")

    return StreamingResponse(
        game_event_stream(player_id, session_id),
        media_type="text/event-stream",
        headers=headers,
    )


@realtime_router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket) -> None:
    """
    WebSocket endpoint for interactive commands and chat.
    Supports session tracking for dual connection management.
    """
    from ..logging.enhanced_logging_config import get_logger

    logger = get_logger(__name__)

    connection_manager = _resolve_connection_manager_from_state(websocket.app.state)
    if connection_manager is None or getattr(connection_manager, "persistence", None) is None:
        # CRITICAL FIX: Must accept WebSocket before closing or sending messages
        await websocket.accept()
        await websocket.send_json({"type": "error", "message": "Service temporarily unavailable"})
        await websocket.close(code=1013)
        return

    # Accept token via WebSocket subprotocol (preferred) or query token (fallback)
    token = websocket.query_params.get("token")
    try:
        subproto_header = websocket.headers.get("sec-websocket-protocol")
        if subproto_header:
            # Example formats observed: "bearer, <token>" or just "<token>"
            parts = [p.strip() for p in subproto_header.split(",") if p and p.strip()]
            # If 'bearer' marker present, prefer the next token-like value; else use the last part
            if "bearer" in [p.lower() for p in parts]:
                for p in parts:
                    if p.lower() == "bearer":
                        continue
                    if p:
                        token = p
                        break
            elif parts:
                token = parts[-1]
    except (ValueError, TypeError, AttributeError) as e:
        logger.error("Error parsing Authorization header", error=str(e), error_type=type(e).__name__)
        # Non-fatal: fall back to query param token
        pass
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
            logger.warning("WebSocket connection attempt for non-existent player", player_id=player_id)
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
        player_id = str(player.player_id)

    logger.info("WebSocket connection attempt", player_id=player_id, session_id=session_id)

    try:
        await handle_websocket_connection(websocket, player_id, session_id)
    except Exception as e:
        logger.error("Error in WebSocket endpoint", player_id=player_id, error=str(e), exc_info=True)
        raise


@realtime_router.get("/connections/{player_id}")
async def get_player_connections(player_id: str, request: Request) -> dict[str, Any]:
    """
    Get connection information for a player.
    Returns detailed connection metadata including session information.
    """
    from ..logging.enhanced_logging_config import get_logger

    logger = get_logger(__name__)

    connection_manager = _ensure_connection_manager(request.app.state)

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

    logger.info("Connection info requested", player_id=player_id)
    return connection_data


@realtime_router.post("/connections/{player_id}/session")
async def handle_new_game_session(player_id: str, request: Request) -> dict[str, Any]:
    """
    Handle a new game session for a player.
    This will disconnect existing connections and establish a new session.
    """
    import json

    from ..logging.enhanced_logging_config import get_logger

    logger = get_logger(__name__)

    connection_manager = _ensure_connection_manager(request.app.state)

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

        logger.info("New game session handled", player_id=player_id, session_results=session_results)
        assert isinstance(session_results, dict)
        return session_results

    except json.JSONDecodeError as e:
        context = create_context_from_request(request)
        context.user_id = player_id
        raise LoggedHTTPException(status_code=400, detail="Invalid JSON in request body", context=context) from e
    except Exception as e:
        logger.error("Error handling new game session", player_id=player_id, error=str(e), exc_info=True)
        context = create_context_from_request(request)
        context.user_id = player_id
        raise LoggedHTTPException(
            status_code=500, detail=f"Error handling new game session: {str(e)}", context=context
        ) from e


@realtime_router.get("/connections/stats")
async def get_connection_statistics(request: Request) -> dict[str, Any]:
    """
    Get comprehensive connection statistics.
    Returns detailed statistics about all connections, sessions, and presence.
    """
    from ..logging.enhanced_logging_config import get_logger

    logger = get_logger(__name__)

    connection_manager = _ensure_connection_manager(request.app.state)

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
async def websocket_endpoint_route(websocket: WebSocket, player_id: str) -> None:
    """
    Backward-compatible WebSocket endpoint that accepts a path player_id but
    prefers JWT token identity when provided.
    Supports session tracking for dual connection management.
    """
    from ..logging.enhanced_logging_config import get_logger

    logger = get_logger(__name__)

    # Get session parameter
    session_id = websocket.query_params.get("session_id")
    logger.info("WebSocket (compat) connection attempt", player_id=player_id, session_id=session_id)
    # Deprecation notice: prefer /api/ws with JWT via subprotocols
    logger.warning(
        "Deprecated WebSocket route in use; migrate clients to /api/ws with JWT via subprotocols",
        player_id=player_id,
    )

    try:
        connection_manager = _resolve_connection_manager_from_state(websocket.app.state)
        if connection_manager is None or getattr(connection_manager, "persistence", None) is None:
            await websocket.accept()
            await websocket.send_json({"type": "error", "message": "Service temporarily unavailable"})
            await websocket.close(code=1013)
            return

        token = websocket.query_params.get("token")
        resolved_player_id = player_id
        payload = decode_access_token(token)
        if payload and "sub" in payload:
            user_id = str(payload["sub"]).strip()
            persistence = get_persistence()
            player = persistence.get_player_by_user_id(user_id)
            if player:
                resolved_player_id = str(player.player_id)
        await handle_websocket_connection(websocket, resolved_player_id, session_id)
    except Exception as e:
        logger.error("Error in WebSocket endpoint", player_id=player_id, error=str(e), exc_info=True)
        raise
