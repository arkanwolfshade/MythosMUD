"""
WebSocket connection lifecycle: setup, welcome, and cleanup on disconnect.

Extracted from websocket_handler for Lizard file-nloc limits.
"""

import uuid
from typing import TYPE_CHECKING, Protocol, cast

from fastapi import WebSocket, WebSocketDisconnect
from structlog.stdlib import BoundLogger

from ..models.room import Room
from ..structured_logging.enhanced_logging_config import get_logger
from .envelope import build_event

if TYPE_CHECKING:
    from .connection_manager import ConnectionManager

logger: BoundLogger = get_logger(__name__)


class PlayerDisconnectService(Protocol):  # pylint: disable=too-few-public-methods
    """Notify subsystems when a WebSocket session ends for a player."""

    def on_player_disconnect(self, player_id: uuid.UUID) -> None: ...  # pylint: disable=missing-function-docstring


class AsyncPersistenceRoomLookup(Protocol):  # pylint: disable=too-few-public-methods
    """Narrow persistence surface for loading ``Room`` by id in the WS handler."""

    def get_room_by_id(self, room_id: str) -> object | None: ...  # pylint: disable=missing-function-docstring


async def cleanup_websocket_connection(
    player_id: uuid.UUID, player_id_str: str, connection_manager: "ConnectionManager"
) -> None:
    """Clean up connection, follow state, party state, and player mute data on disconnect."""
    try:
        from ..container import get_container

        container_raw = get_container()
        container: object | None = cast(object | None, container_raw)
        if container is not None:
            follow_svc = cast(object | None, getattr(container, "follow_service", None))
            if follow_svc is not None:
                cast(PlayerDisconnectService, follow_svc).on_player_disconnect(player_id)
            party_svc = cast(object | None, getattr(container, "party_service", None))
            if party_svc is not None:
                cast(PlayerDisconnectService, party_svc).on_player_disconnect(player_id)
    except (ImportError, AttributeError, RuntimeError) as e:
        logger.debug("Could not clean up follow/party state on disconnect", player_id=player_id, error=str(e))

    try:
        await connection_manager.disconnect_websocket(player_id)
    except (WebSocketDisconnect, RuntimeError) as e:
        logger.error("Error disconnecting WebSocket", player_id=player_id, error=str(e))

    try:
        from ..services.user_manager import user_manager

        _: bool = user_manager.cleanup_player_mutes(player_id_str)
        logger.info("Cleaned up mute data", player_id=player_id)
    except (WebSocketDisconnect, RuntimeError) as e:
        logger.error("Error cleaning up mute data", player_id=player_id, error=str(e))


async def setup_initial_connection_state(
    websocket: WebSocket,
    player_id: uuid.UUID,
    player_id_str: str,
    connection_manager: "ConnectionManager",
) -> tuple[str | None, bool]:
    """
    Set up initial connection state and send initial game state.

    Returns:
        Tuple of (canonical_room_id, should_exit)
    """
    from . import websocket_handler as ws_handler

    try:
        canonical_room_id, should_exit = await ws_handler.send_initial_game_state(
            websocket, player_id, player_id_str, connection_manager
        )
        if should_exit:
            return None, True

        if canonical_room_id:
            ap_raw = cast(object | None, getattr(connection_manager, "async_persistence", None))
            if ap_raw is not None:
                ap = cast(AsyncPersistenceRoomLookup, ap_raw)
                room = ap.get_room_by_id(canonical_room_id)
                if room is not None:
                    await ws_handler.check_and_send_death_notification(
                        websocket,
                        player_id,
                        player_id_str,
                        canonical_room_id,
                        cast(Room | dict[str, object], room),
                        connection_manager,
                    )
                    await ws_handler.send_initial_room_state(
                        websocket, player_id, player_id_str, canonical_room_id, connection_manager
                    )

        return canonical_room_id, False
    except WebSocketDisconnect as e:
        # Client closed during setup (e.g. page close, React unmount). Expected in e2e and dev.
        logger.debug(
            "Client disconnected during initial connection setup",
            player_id=player_id,
            code=getattr(e, "code", None),
            reason=getattr(e, "reason", None),
        )
        return None, True
    except RuntimeError as e:
        logger.error("Error in initial connection setup", player_id=player_id, error=str(e), exc_info=True)
        return None, True


async def send_welcome_event(websocket: WebSocket, player_id: uuid.UUID, player_id_str: str) -> bool:
    """
    Send welcome event to the client.

    Returns:
        True if successful, False if connection was closed
    """
    # Check if WebSocket is still connected before sending welcome event
    from starlette.websockets import WebSocketState

    ws_state = getattr(websocket, "application_state", None)
    if ws_state == WebSocketState.DISCONNECTED:
        logger.debug("WebSocket disconnected before welcome event, exiting", player_id=player_id)
        return False

    try:
        welcome_event = build_event("welcome", {"message": "Connected to MythosMUD"}, player_id=player_id_str)
        await websocket.send_json(welcome_event)
        return True
    except WebSocketDisconnect as e:
        # Client closed before/during welcome (e.g. tab close, E2E context close). Expected; do not log as error.
        logger.debug(
            "WebSocket closed before welcome event could be sent",
            player_id=player_id,
            code=getattr(e, "code", None),
            reason=getattr(e, "reason", None),
        )
        return False
    except RuntimeError as e:
        error_message = str(e)
        if "close message has been sent" in error_message or "Cannot call" in error_message:
            logger.debug("WebSocket closed before welcome event could be sent", player_id=player_id)
            return False
        raise
