"""
Real-time communication API endpoints for MythosMUD server.

This module handles WebSocket connections for real-time game communication.
"""

# pylint: disable=too-many-lines  # Reason: WebSocket + session API surface; split when a second transport appears

import importlib
import os
import time
import uuid
from collections.abc import Awaitable, Callable
from typing import Protocol, cast
from unittest.mock import Mock

from fastapi import APIRouter, Request, WebSocket
from structlog.stdlib import BoundLogger

from ..auth_utils import decode_access_token
from ..exceptions import LoggedHTTPException
from ..models.player import Player
from ..schemas.realtime import (
    ConnectionStatisticsResponse,
    NewGameSessionResponse,
    PlayerConnectionsResponse,
    SessionInfo,
)
from ..schemas.realtime.presence_data import ErrorStatistics, PresenceStatistics, SessionStatistics
from ..schemas.realtime.realtime import HealthInfo, PresenceInfo


class _ConnectionManagerUtilsModule(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    def resolve_connection_manager(self, candidate: object | None = None) -> object | None:
        """Resolve the connection manager singleton (or optional candidate)."""


# pylint: disable=missing-function-docstring  # Reason: Protocol stub methods below
class _PlayerLookupPersistence(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """Minimal async persistence surface for WebSocket player resolution."""

    async def get_player_by_id(self, player_id: uuid.UUID) -> Player | None: ...

    async def get_player_by_user_id(self, user_id: str) -> Player | None: ...


class _RealtimeConnectionManager(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """Connection manager API used by realtime HTTP/WebSocket routes."""

    async_persistence: _PlayerLookupPersistence | None

    def get_player_presence_info(self, player_id: uuid.UUID) -> dict[str, object]: ...

    def get_player_session(self, player_id: uuid.UUID) -> str | None: ...

    def get_session_connections(self, session_id: str) -> list[str]: ...

    def validate_session(self, player_id: uuid.UUID, session_id: str) -> bool: ...

    async def check_connection_health(self, player_id: uuid.UUID) -> dict[str, object]: ...

    async def handle_new_game_session(self, player_id: uuid.UUID, new_session_id: str) -> dict[str, object]: ...

    def get_presence_statistics(self) -> dict[str, object]: ...

    def get_session_stats(self) -> dict[str, object]: ...

    def get_error_statistics(self) -> dict[str, object]: ...


# pylint: enable=missing-function-docstring


# Load websocket_handler through importlib; a static import cycles with app.factory.
class _WebSocketHandlerModule(Protocol):
    handle_websocket_connection: Callable[..., Awaitable[None]]


# Create real-time router
realtime_router = APIRouter(prefix="/api", tags=["realtime"])


def resolve_connection_manager(candidate: object | None = None) -> object | None:
    """Prefer the supplied manager; otherwise the container singleton.

    Static import of connection_manager_utils cycles factory -> this module.
    importlib keeps the lookup that API routes used before the GHSA cycle break.
    """
    if candidate is not None:
        return candidate
    loaded = cast(object, importlib.import_module("server.realtime.connection_manager_utils"))
    utils = cast(_ConnectionManagerUtilsModule, loaded)
    return utils.resolve_connection_manager(None)


async def _invoke_handle_websocket_connection(
    websocket: WebSocket,
    player_id: uuid.UUID,
    session_id: str | None,
    connection_manager: object | None,
    token: str | None,
) -> None:
    """Load the handler via importlib so basedpyright does not follow the factory cycle."""
    loaded = cast(object, importlib.import_module("server.realtime.websocket_handler"))
    module = cast(_WebSocketHandlerModule, loaded)
    await module.handle_websocket_connection(
        websocket,
        player_id,
        session_id,
        connection_manager=connection_manager,
        token=token,
    )


def _resolve_connection_manager_from_state(state: object | None) -> _RealtimeConnectionManager | None:
    if state is None:
        return None
    container: object | None = getattr(state, "container", None)
    candidate: object | None = None
    if container is not None:
        container_dict = getattr(container, "__dict__", None)
        if isinstance(container_dict, dict) and "connection_manager" in container_dict:
            candidate = cast(object, container_dict["connection_manager"])
        elif not isinstance(container, Mock):
            candidate = getattr(container, "connection_manager", None)
    manager = resolve_connection_manager(candidate)
    if manager is None:
        return None
    return cast(_RealtimeConnectionManager, manager)


def _app_state_from_request(request: Request) -> object | None:
    """Read Starlette app.state without treating Request.app as Any."""
    app: object = cast(object, request.app)
    return getattr(app, "state", None)


def _app_state_from_websocket(websocket: WebSocket) -> object | None:
    """Read Starlette app.state from a WebSocket connection."""
    websocket_obj: object = cast(object, websocket)
    websocket_app: object | None = getattr(websocket_obj, "app", None)
    if websocket_app is None:
        return None
    return getattr(websocket_app, "state", None)


def _ensure_connection_manager(request: Request) -> _RealtimeConnectionManager:
    """
    Ensure connection manager is available.
    Raises LoggedHTTPException with proper context if unavailable.
    """
    connection_manager = _resolve_connection_manager_from_state(_app_state_from_request(request))
    if connection_manager is None:
        raise LoggedHTTPException(
            status_code=503,
            detail="Service temporarily unavailable",
            operation="ensure_connection_manager",
        )
    return connection_manager


async def _validate_and_accept_websocket(
    websocket: WebSocket, connection_manager: _RealtimeConnectionManager | None
) -> bool:
    """
    Validate connection manager and accept WebSocket connection.
    Returns True if connection is valid, False otherwise.
    If invalid, sends error and closes connection.
    """
    # ARCHITECTURAL FIX: Check for async_persistence instead of old sync persistence
    if connection_manager is None or connection_manager.async_persistence is None:
        # CRITICAL FIX: Must accept WebSocket before closing or sending messages
        await websocket.accept()
        await websocket.send_json({"type": "error", "message": "Service temporarily unavailable"})
        await websocket.close(code=1013)
        return False
    return True


def _extract_bearer_token(parts: list[str]) -> str | None:
    """
    Extract bearer token from parsed subprotocol parts.

    If 'bearer' marker is present, prefer the next token-like value.
    Otherwise, use the last part.

    Args:
        parts: List of parsed subprotocol parts

    Returns:
        Token string if found, None otherwise
    """
    if "bearer" in [p.lower() for p in parts]:
        for p in parts:
            if p.lower() == "bearer":
                continue
            if p:
                return p
    elif parts:
        return parts[-1]
    return None


def _parse_subprotocol_token(subproto_header: str) -> str | None:
    """
    Parse token from WebSocket subprotocol header.

    Example formats: "bearer, <token>" or just "<token>"

    Args:
        subproto_header: The sec-websocket-protocol header value

    Returns:
        Token string if found, None otherwise
    """
    parts = [p.strip() for p in subproto_header.split(",") if p and p.strip()]
    return _extract_bearer_token(parts)


def _parse_websocket_token(websocket: WebSocket, logger: BoundLogger) -> str | None:
    """
    Parse token from WebSocket subprotocol (preferred) or query params (fallback).

    Args:
        websocket: WebSocket connection object
        logger: Logger instance for error reporting

    Returns:
        Token string if found, None otherwise
    """
    # Try query parameter first (fallback)
    token = websocket.query_params.get("token")

    # Try subprotocol header (preferred method)
    try:
        subproto_header = websocket.headers.get("sec-websocket-protocol")
        if subproto_header:
            subproto_token = _parse_subprotocol_token(subproto_header)
            if subproto_token:
                token = subproto_token
    except (ValueError, TypeError, AttributeError) as e:
        logger.error("Error parsing Authorization header", error=str(e), error_type=type(e).__name__)
        # Non-fatal: fall back to query param token

    return token


def websocket_player_id_fallback_allowed() -> bool:
    """Return True only when anonymous player_id query fallback is explicitly enabled.

    Default is off. Enable only for isolated test harnesses via
    MYTHOSMUD_ALLOW_WEBSOCKET_PLAYER_ID_FALLBACK=true. Never enable in production.
    """
    raw = os.environ.get("MYTHOSMUD_ALLOW_WEBSOCKET_PLAYER_ID_FALLBACK", "").strip().lower()
    return raw in {"1", "true", "yes", "on"}


async def _resolve_player_id_from_test(_websocket: WebSocket, player_id_str: str, logger: BoundLogger) -> uuid.UUID:
    """
    Resolve player ID from test player_id query parameter.
    Validates that the player exists before returning.
    """
    from ..container.async_persistence_access import get_container_async_persistence

    async_persistence = get_container_async_persistence()
    player_id_uuid = uuid.UUID(player_id_str)
    player = await async_persistence.get_player_by_id(player_id_uuid)
    if not player:
        logger.warning("WebSocket connection attempt for non-existent player", player_id=player_id_str)
        raise LoggedHTTPException(
            status_code=404,
            detail=f"Player {player_id_str} not found",
            user_id=player_id_str,
        )
    # Convert player_id to UUID for consistency
    # SQLAlchemy Column[str] returns UUID at runtime, cast for type checker
    player_id_uuid_value = cast(uuid.UUID | str, player.player_id)
    return uuid.UUID(str(player_id_uuid_value)) if isinstance(player_id_uuid_value, str) else player_id_uuid_value


async def _resolve_player_id_from_token(websocket: WebSocket, payload: dict[str, object]) -> uuid.UUID:
    """
    Resolve player ID from JWT token payload.
    Validates that the user has a player record before returning.

    MULTI-CHARACTER: If character_id is provided in query params, use that character.
    Otherwise, fall back to first active character (backward compatibility).
    """
    user_id = str(payload["sub"]).strip()
    from ..container.async_persistence_access import get_container_async_persistence

    async_persistence = get_container_async_persistence()

    # MULTI-CHARACTER: Check if character_id is provided in query params
    character_id_str = websocket.query_params.get("character_id")
    if character_id_str:
        try:
            character_uuid = uuid.UUID(character_id_str)
            # Validate the character belongs to the user
            player = await async_persistence.get_player_by_id(character_uuid)
            if not player:
                raise LoggedHTTPException(
                    status_code=404,
                    detail="Character not found",
                    user_id=user_id,
                )
            # Validate character belongs to user
            if str(player.user_id) != user_id:
                raise LoggedHTTPException(
                    status_code=403,
                    detail="Character does not belong to user",
                    user_id=user_id,
                )
            # Validate character is not deleted
            if player.is_deleted:
                raise LoggedHTTPException(
                    status_code=404,
                    detail="Character has been deleted",
                    user_id=user_id,
                )
            # Use the specified character
            player_id_value = cast(uuid.UUID | str, player.player_id)
            return uuid.UUID(str(player_id_value))
        except ValueError:
            # Invalid UUID format, fall through to default behavior
            pass

    # Fallback: Get first active character (backward compatibility)
    player = await async_persistence.get_player_by_user_id(user_id)

    if not player:
        raise LoggedHTTPException(
            status_code=401,
            detail="User has no player record",
            user_id=user_id,
        )
    # player.player_id is a SQLAlchemy Column[str] but returns UUID at runtime
    # Convert to UUID for type safety - always convert to string first
    # Cast to tell type checker that at runtime this is UUID or str, not Column
    player_id_value = cast(uuid.UUID | str, player.player_id)
    return uuid.UUID(str(player_id_value))


async def _resolve_player_id(websocket: WebSocket, token: str | None, logger: BoundLogger) -> uuid.UUID:
    """
    Resolve player ID from token or test player_id parameter.
    Handles both authenticated (JWT) and test (player_id query param) scenarios.
    """
    payload = decode_access_token(token)
    if not payload or "sub" not in payload:
        player_id_str = websocket.query_params.get("player_id")
        if not player_id_str or not websocket_player_id_fallback_allowed():
            raise LoggedHTTPException(status_code=401, detail="Invalid or missing token")
        return await _resolve_player_id_from_test(websocket, player_id_str, logger)
    return await _resolve_player_id_from_token(websocket, payload)


@realtime_router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket) -> None:
    """
    WebSocket endpoint for interactive commands and chat.
    Supports session tracking for dual connection management.
    """
    from ..structured_logging.enhanced_logging_config import get_logger

    logger = get_logger(__name__)

    websocket_state = _app_state_from_websocket(websocket)
    connection_manager = _resolve_connection_manager_from_state(websocket_state)

    if not await _validate_and_accept_websocket(websocket, connection_manager):
        return

    token = _parse_websocket_token(websocket, logger)
    session_id = websocket.query_params.get("session_id")
    player_id = await _resolve_player_id(websocket, token, logger)

    logger.info("WebSocket connection attempt", player_id=player_id, session_id=session_id)

    try:
        await _invoke_handle_websocket_connection(websocket, player_id, session_id, connection_manager, token)
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: WebSocket errors unpredictable, must log and re-raise
        from starlette.websockets import WebSocketDisconnect

        # Client disconnect (e.g. E2E tab close) is expected; log at debug to avoid polluting errors.log
        is_client_gone = isinstance(e, WebSocketDisconnect) or (
            isinstance(e, RuntimeError) and "close message has been sent" in str(e)
        )
        if is_client_gone:
            logger.debug("WebSocket client disconnected", player_id=player_id, error=str(e))
        else:
            logger.error("Error in WebSocket endpoint", player_id=player_id, error=str(e), exc_info=True)
        raise


@realtime_router.get("/connections/{player_id}", response_model=PlayerConnectionsResponse)
async def get_player_connections(player_id: uuid.UUID, request: Request) -> PlayerConnectionsResponse:
    """
    Get connection information for a player.
    Returns detailed connection metadata including session information.
    """
    from ..structured_logging.enhanced_logging_config import get_logger

    logger = get_logger(__name__)

    connection_manager = _ensure_connection_manager(request)

    # Get connection information
    presence_info = connection_manager.get_player_presence_info(player_id)

    # Get session information
    session_id = connection_manager.get_player_session(player_id)
    session_connections = connection_manager.get_session_connections(session_id) if session_id else []

    # Get connection health
    health_info = await connection_manager.check_connection_health(player_id)

    connection_data = PlayerConnectionsResponse(
        player_id=str(player_id),
        presence=PresenceInfo.model_validate(presence_info),
        session=SessionInfo(
            session_id=session_id,
            session_connections=session_connections,
            is_valid=connection_manager.validate_session(player_id, session_id) if session_id else False,
        ),
        health=HealthInfo.model_validate(health_info),
        timestamp=time.time(),
    )

    logger.info("Connection info requested", player_id=player_id)
    return connection_data


@realtime_router.post("/connections/{player_id}/session", response_model=NewGameSessionResponse)
async def handle_new_game_session(player_id: uuid.UUID, request: Request) -> NewGameSessionResponse:
    """
    Handle a new game session for a player.
    This will disconnect existing connections and establish a new session.
    """
    import json

    from ..structured_logging.enhanced_logging_config import get_logger

    logger = get_logger(__name__)

    connection_manager = _ensure_connection_manager(request)

    try:
        # Get new session ID from request body
        body_raw = cast(object, await request.json())
        if not isinstance(body_raw, dict):
            raise LoggedHTTPException(
                status_code=400,
                detail="Invalid JSON in request body",
                user_id=str(player_id),
            )
        body = cast(dict[str, object], body_raw)
        new_session_id_raw = body.get("session_id")
        if not isinstance(new_session_id_raw, str) or not new_session_id_raw:
            raise LoggedHTTPException(
                status_code=400,
                detail="session_id is required",
                user_id=str(player_id),
            )
        new_session_id = new_session_id_raw

        # Handle new game session
        session_results = await connection_manager.handle_new_game_session(player_id, new_session_id)

        logger.info("New game session handled", player_id=player_id, session_results=session_results)
        return NewGameSessionResponse.model_validate(session_results)

    except json.JSONDecodeError as e:
        raise LoggedHTTPException(
            status_code=400,
            detail="Invalid JSON in request body",
            user_id=str(player_id),
        ) from e
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Session handling errors unpredictable, must log and handle
        # Structlog handles UUID objects automatically, no need to convert to string
        logger.error("Error handling new game session", player_id=player_id, error=str(e), exc_info=True)
        raise LoggedHTTPException(
            status_code=500,
            detail=f"Error handling new game session: {str(e)}",
            user_id=str(player_id),
        ) from e


@realtime_router.get("/connections/stats", response_model=ConnectionStatisticsResponse)
async def get_connection_statistics(request: Request) -> ConnectionStatisticsResponse:
    """
    Get comprehensive connection statistics.
    Returns detailed statistics about all connections, sessions, and presence.
    """
    from ..structured_logging.enhanced_logging_config import get_logger

    logger = get_logger(__name__)

    connection_manager = _ensure_connection_manager(request)

    # Get various statistics
    presence_stats = connection_manager.get_presence_statistics()
    session_stats = connection_manager.get_session_stats()
    error_stats = connection_manager.get_error_statistics()

    statistics = ConnectionStatisticsResponse(
        presence=PresenceStatistics.model_validate(presence_stats),
        sessions=SessionStatistics.model_validate(session_stats),
        errors=ErrorStatistics.model_validate(error_stats),
        timestamp=time.time(),
    )

    logger.info("Connection statistics requested")
    return statistics


async def _validate_websocket_connection_manager(websocket: WebSocket) -> _RealtimeConnectionManager | None:
    """
    Validate and resolve connection manager for WebSocket.

    Args:
        websocket: WebSocket connection object

    Returns:
        Connection manager instance or None if unavailable
    """
    websocket_state = _app_state_from_websocket(websocket)
    connection_manager = _resolve_connection_manager_from_state(websocket_state)
    if connection_manager is None or connection_manager.async_persistence is None:
        await websocket.accept()
        await websocket.send_json({"type": "error", "message": "Service temporarily unavailable"})
        await websocket.close(code=1013)
        return None
    return connection_manager


async def _resolve_player_id_from_path_or_token(
    player_id: str,
    token: str | None,
    async_persistence: _PlayerLookupPersistence | None = None,
) -> uuid.UUID | None:
    """
    Resolve player ID from a valid JWT. Path UUID is an identity check, not a credential.

    Args:
        player_id: Player ID from path parameter
        token: JWT token from query parameters or subprotocol
        async_persistence: Async persistence layer. Required.

    Returns:
        Resolved player UUID or None if authentication fails
    """
    if not token or async_persistence is None:
        return None
    payload = decode_access_token(token)
    if not payload or "sub" not in payload:
        return None
    user_id = str(payload["sub"]).strip()
    player = await async_persistence.get_player_by_user_id(user_id)
    if not player:
        return None
    resolved = uuid.UUID(str(player.player_id))
    try:
        path_uuid = uuid.UUID(player_id)
    except (ValueError, AttributeError, TypeError):
        return resolved
    if path_uuid != resolved:
        return None
    return resolved


@realtime_router.websocket("/ws/{player_id}")
async def websocket_endpoint_route(websocket: WebSocket, player_id: str) -> None:  # pylint: disable=too-many-locals  # Reason: WebSocket endpoint requires many intermediate variables for connection management
    """
    Deprecated. Backward-compatible WebSocket endpoint that accepts a path player_id
    but prefers JWT token identity when provided. Supports session tracking.

    **Deprecation**: Use GET /api/ws with JWT (query param or subprotocol) instead.
    This route will be removed in a future release. Migrate clients to /api/ws.
    """
    from ..structured_logging.enhanced_logging_config import get_logger

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
        connection_manager = await _validate_websocket_connection_manager(websocket)
        if connection_manager is None:
            return

        token = _parse_websocket_token(websocket, logger)
        resolved_player_id = await _resolve_player_id_from_path_or_token(
            player_id, token, async_persistence=connection_manager.async_persistence
        )

        if not resolved_player_id:
            raise LoggedHTTPException(status_code=401, detail="Unable to resolve player ID")

        await _invoke_handle_websocket_connection(
            websocket,
            resolved_player_id,
            session_id,
            connection_manager,
            token,
        )
    except Exception as e:
        # Structlog handles UUID objects automatically, no need to convert to string
        logger.error("Error in WebSocket endpoint", player_id=player_id, error=str(e), exc_info=True)
        raise
