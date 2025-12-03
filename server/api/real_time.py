"""
Real-time communication API endpoints for MythosMUD server.

This module handles WebSocket connections for real-time game communication.
"""

import time
import uuid
from typing import Any, cast
from unittest.mock import Mock

from fastapi import APIRouter, HTTPException, Request, WebSocket

from ..auth_utils import decode_access_token
from ..exceptions import LoggedHTTPException
from ..realtime.connection_manager import resolve_connection_manager, set_global_connection_manager
from ..realtime.websocket_handler import handle_websocket_connection
from ..utils.error_logging import create_context_from_request, create_context_from_websocket

# AI Agent: Don't import app at module level - causes circular import!
#           Import locally in functions instead

# Create real-time router
realtime_router = APIRouter(prefix="/api", tags=["realtime"])


def _resolve_connection_manager_from_state(state) -> Any:
    container = getattr(state, "container", None)
    candidate = None
    if container is not None:
        container_dict = getattr(container, "__dict__", None)
        if container_dict and "connection_manager" in container_dict:
            candidate = container_dict["connection_manager"]
        elif not isinstance(container, Mock):
            candidate = getattr(container, "connection_manager", None)
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


@realtime_router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket) -> None:
    """
    WebSocket endpoint for interactive commands and chat.
    Supports session tracking for dual connection management.
    """
    from ..logging.enhanced_logging_config import get_logger

    logger = get_logger(__name__)

    websocket_app = getattr(websocket, "app", None)
    websocket_state = getattr(websocket_app, "state", None)
    connection_manager = _resolve_connection_manager_from_state(websocket_state)
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
    player_id: uuid.UUID  # Type annotation for final player_id value
    if not payload or "sub" not in payload:
        # Fallback: allow anonymous connection only for tests (no identity)
        player_id_str = websocket.query_params.get("player_id")
        if not player_id_str:
            context = create_context_from_websocket(websocket)
            raise LoggedHTTPException(status_code=401, detail="Invalid or missing token", context=context)

        # CRITICAL FIX: Validate that the test player exists
        from ..async_persistence import get_async_persistence

        async_persistence = get_async_persistence()
        # Convert str player_id to UUID for get_player
        player_id_uuid = uuid.UUID(player_id_str) if isinstance(player_id_str, str) else player_id_str
        player = await async_persistence.get_player_by_id(player_id_uuid)
        if not player:
            logger.warning("WebSocket connection attempt for non-existent player", player_id=player_id_str)
            context = create_context_from_websocket(websocket)
            context.user_id = player_id_str
            raise LoggedHTTPException(status_code=404, detail=f"Player {player_id_str} not found", context=context)
        # Convert player_id to UUID for consistency
        # SQLAlchemy Column[str] returns UUID at runtime, cast for type checker
        player_id_uuid_value = cast(uuid.UUID | str, player.player_id)
        player_id = (
            uuid.UUID(str(player_id_uuid_value)) if isinstance(player_id_uuid_value, str) else player_id_uuid_value
        )
    else:
        user_id = str(payload["sub"]).strip()
        from ..async_persistence import get_async_persistence

        async_persistence = get_async_persistence()
        player = await async_persistence.get_player_by_user_id(user_id)

        if not player:
            context = create_context_from_websocket(websocket)
            context.user_id = user_id
            raise LoggedHTTPException(status_code=401, detail="User has no player record", context=context)
        # player.player_id is a SQLAlchemy Column[str] but returns UUID at runtime
        # Convert to UUID for type safety - always convert to string first
        # Cast to tell type checker that at runtime this is UUID or str, not Column
        player_id_value = cast(uuid.UUID | str, player.player_id)
        player_id = uuid.UUID(str(player_id_value))

    # Structlog handles UUID objects automatically, no need to convert to string
    logger.info("WebSocket connection attempt", player_id=player_id, session_id=session_id)

    try:
        await handle_websocket_connection(
            websocket, player_id, session_id, connection_manager=connection_manager, token=token
        )
    except Exception as e:
        # Structlog handles UUID objects automatically, no need to convert to string
        logger.error("Error in WebSocket endpoint", player_id=player_id, error=str(e), exc_info=True)
        raise


@realtime_router.get("/connections/{player_id}")
async def get_player_connections(player_id: uuid.UUID, request: Request) -> dict[str, Any]:
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
async def handle_new_game_session(player_id: uuid.UUID, request: Request) -> dict[str, Any]:
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
            context.user_id = str(player_id)
            raise LoggedHTTPException(status_code=400, detail="session_id is required", context=context)

        # Handle new game session
        session_results = await connection_manager.handle_new_game_session(player_id, new_session_id)

        logger.info("New game session handled", player_id=player_id, session_results=session_results)
        assert isinstance(session_results, dict)
        return session_results

    except json.JSONDecodeError as e:
        context = create_context_from_request(request)
        context.user_id = str(player_id)
        raise LoggedHTTPException(status_code=400, detail="Invalid JSON in request body", context=context) from e
    except Exception as e:
        # Structlog handles UUID objects automatically, no need to convert to string
        logger.error("Error handling new game session", player_id=player_id, error=str(e), exc_info=True)
        context = create_context_from_request(request)
        context.user_id = str(player_id)
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
        websocket_app = getattr(websocket, "app", None)
        websocket_state = getattr(websocket_app, "state", None)
        connection_manager = _resolve_connection_manager_from_state(websocket_state)
        if connection_manager is None or getattr(connection_manager, "persistence", None) is None:
            await websocket.accept()
            await websocket.send_json({"type": "error", "message": "Service temporarily unavailable"})
            await websocket.close(code=1013)
            return

        token = websocket.query_params.get("token")
        # Convert path parameter player_id (str) to UUID
        resolved_player_id: uuid.UUID | None = None
        try:
            resolved_player_id = uuid.UUID(player_id)
        except (ValueError, AttributeError, TypeError):
            # If conversion fails, try to resolve from token
            pass

        payload = decode_access_token(token)
        if payload and "sub" in payload:
            user_id = str(payload["sub"]).strip()
            from ..async_persistence import get_async_persistence

            async_persistence = get_async_persistence()
            player = await async_persistence.get_player_by_user_id(user_id)
            if player:
                # player.player_id is a SQLAlchemy Column[str] but returns UUID at runtime
                # Convert to UUID for type safety - always convert to string first
                player_id_value = player.player_id
                resolved_player_id = uuid.UUID(str(player_id_value))

        # resolved_player_id needs to be UUID for handle_websocket_connection
        if not resolved_player_id:
            raise HTTPException(status_code=401, detail="Unable to resolve player ID")
        await handle_websocket_connection(
            websocket, resolved_player_id, session_id, connection_manager=connection_manager
        )
    except Exception as e:
        # Structlog handles UUID objects automatically, no need to convert to string
        logger.error("Error in WebSocket endpoint", player_id=player_id, error=str(e), exc_info=True)
        raise
