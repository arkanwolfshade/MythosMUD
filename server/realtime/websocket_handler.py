"""
WebSocket handler for MythosMUD real-time communication.

This module handles WebSocket message processing, command handling,
and real-time updates for the game. Callers should pass connection_manager
from the WebSocket pipeline when invoking handle_game_command,
process_websocket_command, or handle_chat_message.
"""

# pylint: disable=too-many-arguments,too-many-positional-arguments,too-many-locals,too-many-lines  # Reason: WebSocket handler requires many parameters and intermediate variables for complex message processing logic. WebSocket handler requires extensive message processing logic for comprehensive real-time communication.

import json
import time
import uuid
from collections.abc import Mapping
from typing import TYPE_CHECKING, Protocol, cast

from fastapi import WebSocket, WebSocketDisconnect
from structlog.stdlib import BoundLogger

from ..error_types import ErrorMessages, ErrorType, create_websocket_error_response
from ..models.room import Room
from ..structured_logging.enhanced_logging_config import get_logger
from .envelope import build_event
from .websocket_handler_app_state import resolve_and_setup_app_state_services
from .websocket_handler_commands import (
    handle_game_command,
    process_websocket_command,
    resolve_websocket_connection_manager,
    validate_player_and_persistence,
)
from .websocket_helpers import (
    check_shutdown_and_reject,
    is_client_disconnected_exception,
    is_websocket_disconnect_message,
    load_player_mute_data,
)
from .websocket_initial_state import (
    check_and_send_death_notification,
    send_initial_game_state,
    send_initial_room_state,
)
from .websocket_room_updates import broadcast_room_update

if TYPE_CHECKING:
    from .connection_manager import ConnectionManager
    from .message_validator import WebSocketMessageValidator


class _PlayerDisconnectService(Protocol):  # pylint: disable=too-few-public-methods
    """Notify subsystems when a WebSocket session ends for a player."""

    def on_player_disconnect(self, player_id: uuid.UUID) -> None: ...  # pylint: disable=missing-function-docstring


class _AsyncPersistenceRoomLookup(Protocol):  # pylint: disable=too-few-public-methods
    """Narrow persistence surface for loading ``Room`` by id in the WS handler."""

    def get_room_by_id(self, room_id: str) -> object | None: ...  # pylint: disable=missing-function-docstring


# AI Agent: Don't import app at module level - causes circular import!
#           Import locally in functions instead

# Re-export broadcast_room_update for backward compatibility
__all__ = [
    "handle_websocket_connection",
    "handle_websocket_message",
    "handle_game_command",
    "process_websocket_command",
    "handle_chat_message",
    "send_system_message",
    "broadcast_room_update",  # Re-exported from websocket_room_updates
]

logger: BoundLogger = cast(BoundLogger, get_logger(__name__))

# Test and legacy import names (basedpyright: public symbols from submodules, not private cross-imports).
_resolve_and_setup_app_state_services = resolve_and_setup_app_state_services
_validate_player_and_persistence = validate_player_and_persistence

# Backward-compatible names for tests and internal call sites (implementation in websocket_helpers).
_is_websocket_disconnected = is_websocket_disconnect_message
_is_client_gone_error = is_client_disconnected_exception


async def _check_rate_limit(
    websocket: WebSocket, connection_id: str | None, player_id_str: str, connection_manager: "ConnectionManager"
) -> bool:
    """
    Check rate limit and send error response if exceeded.

    Returns:
        True if rate limit check passed, False if exceeded
    """
    if not connection_id:
        return True

    if connection_manager.rate_limiter.check_message_rate_limit(connection_id):
        return True

    logger.warning("Message rate limit exceeded", player_id=player_id_str, connection_id=connection_id)
    rate_limit_info = connection_manager.rate_limiter.get_message_rate_limit_info(connection_id)
    rli: Mapping[str, object] = cast(Mapping[str, object], rate_limit_info)
    max_attempts_raw = rli.get("max_attempts", 0)
    reset_time_raw = rli.get("reset_time", 0.0)
    max_attempts = int(max_attempts_raw) if isinstance(max_attempts_raw, int | float) else 0
    reset_at = float(reset_time_raw) if isinstance(reset_time_raw, int | float) else 0.0
    retry_after = max(0, int(reset_at - time.time()))
    error_response = create_websocket_error_response(
        ErrorType.RATE_LIMIT_EXCEEDED,
        f"Message rate limit exceeded. Limit: {max_attempts} messages per minute. Try again in {retry_after} seconds.",
        ErrorMessages.RATE_LIMIT_EXCEEDED,
        {
            "player_id": player_id_str,
            "connection_id": connection_id,
            "rate_limit_info": rate_limit_info,
        },
    )
    await websocket.send_json(error_response)
    return False


async def _validate_message(
    websocket: WebSocket, data: str, player_id_str: str, validator: "WebSocketMessageValidator"
) -> dict[str, object] | None:
    """
    Validate message and send error response if validation fails.

    Returns:
        Validated message dict if successful, None if validation failed
    """
    from .message_validator import MessageValidationError

    try:
        csrf_token = None
        message = validator.parse_and_validate(data=data, player_id=player_id_str, schema=None, csrf_token=csrf_token)
        return message
    except MessageValidationError as e:
        logger.warning(
            "Message validation failed",
            player_id=player_id_str,
            error_type=e.error_type,
            error_message=e.message,
        )
        error_response = create_websocket_error_response(
            ErrorType.INVALID_FORMAT,
            f"Message validation failed: {e.message}",
            ErrorMessages.INVALID_FORMAT,
            {"player_id": player_id_str, "error_type": e.error_type},
        )
        await websocket.send_json(error_response)
        return None


async def _send_error_response(
    websocket: WebSocket, error_type: ErrorType, message: str, error_message: str, extra_data: dict[str, object]
) -> bool:
    """
    Send error response to client.

    Returns:
        True if sent successfully, False if WebSocket is disconnected
    """
    try:
        error_response = create_websocket_error_response(error_type, message, error_message, extra_data)
        await websocket.send_json(error_response)
        return True
    except (WebSocketDisconnect, RuntimeError) as send_error:
        send_error_msg = str(send_error)
        if _is_websocket_disconnected(send_error_msg) or "close message has been sent" in send_error_msg:
            return False
        logger.error("Failed to send error response to client", error=send_error_msg)
        return True


async def _handle_json_decode_error(websocket: WebSocket, player_id: uuid.UUID, player_id_str: str) -> None:
    """Handle JSON decode error."""
    logger.warning("Invalid JSON from player", player_id=player_id)
    _: bool = await _send_error_response(
        websocket,
        ErrorType.INVALID_FORMAT,
        "Invalid JSON format",
        ErrorMessages.INVALID_FORMAT,
        {"player_id": player_id_str},
    )


def _handle_websocket_disconnect(player_id_str: str, connection_id: str | None) -> bool:
    """
    Handle WebSocket disconnect.

    Returns:
        True to break the loop
    """
    logger.info("WebSocket disconnected", player_id=player_id_str, connection_id=connection_id)
    return True


def _handle_runtime_error(e: RuntimeError, player_id_str: str, connection_id: str | None) -> tuple[bool, bool]:
    """
    Handle RuntimeError.

    Returns:
        Tuple of (should_break, should_raise)
    """
    error_message = str(e)
    if _is_websocket_disconnected(error_message):
        logger.warning(
            "WebSocket connection lost (not connected)",
            player_id=player_id_str,
            connection_id=connection_id,
            error=error_message,
        )
        return True, False
    return False, True


async def _handle_generic_exception(
    websocket: WebSocket, e: Exception, player_id_str: str, connection_id: str | None
) -> bool:
    """
    Handle generic exception.

    Returns:
        True to break the loop
    """
    logger.error(
        "Error handling WebSocket message",
        player_id=player_id_str,
        connection_id=connection_id,
        error=str(e),
        error_type=type(e).__name__,
        exc_info=True,
    )
    should_break = not await _send_error_response(
        websocket,
        ErrorType.INTERNAL_ERROR,
        f"Internal server error: {str(e)}",
        ErrorMessages.INTERNAL_ERROR,
        {"player_id": player_id_str, "connection_id": connection_id, "error_type": type(e).__name__},
    )
    if should_break:
        logger.warning(
            "WebSocket closed, breaking message loop",
            player_id=player_id_str,
            connection_id=connection_id,
            original_error=str(e),
        )
    return should_break


async def _process_message(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Message processing requires many parameters for context and message handling
    websocket: WebSocket,
    data: str,
    player_id: uuid.UUID,
    player_id_str: str,
    connection_id: str | None,
    connection_manager: "ConnectionManager",
    validator: "WebSocketMessageValidator",
) -> bool:
    """
    Process a single WebSocket message.

    Returns:
        True to continue loop, False to break
    """
    if not await _check_rate_limit(websocket, connection_id, player_id_str, connection_manager):
        return True

    message = await _validate_message(websocket, data, player_id_str, validator)
    if message is None:
        return True

    connection_manager.mark_player_seen(player_id)
    await handle_websocket_message(websocket, player_id_str, message)
    return True


async def _handle_message_loop_exception(
    websocket: WebSocket,
    e: Exception,
    player_id: uuid.UUID,
    player_id_str: str,
    connection_id: str | None,
) -> tuple[bool, bool]:
    """
    Handle exception in message loop.

    Returns:
        Tuple of (should_break, should_raise)
    """
    if isinstance(e, json.JSONDecodeError):
        await _handle_json_decode_error(websocket, player_id, player_id_str)
        return False, False

    if isinstance(e, WebSocketDisconnect):
        return _handle_websocket_disconnect(player_id_str, connection_id), False

    if isinstance(e, RuntimeError):
        return _handle_runtime_error(e, player_id_str, connection_id)

    should_break = await _handle_generic_exception(websocket, e, player_id_str, connection_id)
    return should_break, False


async def _process_exception_in_message_loop(
    websocket: WebSocket, e: Exception, player_id: uuid.UUID, player_id_str: str, connection_id: str
) -> tuple[bool, bool]:
    """Process exception in message loop and return (should_break, should_raise)."""
    should_break, should_raise = await _handle_message_loop_exception(
        websocket, e, player_id, player_id_str, connection_id
    )
    return should_break, should_raise


async def _handle_websocket_message_loop(
    websocket: WebSocket, player_id: uuid.UUID, player_id_str: str, connection_manager: "ConnectionManager"
) -> None:
    """Handle the main WebSocket message loop."""
    from .message_validator import get_message_validator

    validator = get_message_validator()
    connection_id = connection_manager.get_connection_id_from_websocket(websocket)
    # connection_id can be None if websocket is not connected, use empty string as fallback
    connection_id_str = connection_id if connection_id is not None else ""

    while True:
        try:
            data = await websocket.receive_text()
            _: bool = await _process_message(
                websocket, data, player_id, player_id_str, connection_id, connection_manager, validator
            )
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Message loop errors unpredictable, must prevent crash
            # Handle all exceptions uniformly through the exception handler
            # This consolidates multiple exception handlers into one to reduce complexity
            should_break, should_raise = await _process_exception_in_message_loop(
                websocket, e, player_id, player_id_str, connection_id_str
            )
            if should_break:
                break
            if should_raise:
                raise


async def _cleanup_connection(
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
                cast(_PlayerDisconnectService, follow_svc).on_player_disconnect(player_id)
            party_svc = cast(object | None, getattr(container, "party_service", None))
            if party_svc is not None:
                cast(_PlayerDisconnectService, party_svc).on_player_disconnect(player_id)
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


async def _setup_initial_connection_state(
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
    try:
        canonical_room_id, should_exit = await send_initial_game_state(
            websocket, player_id, player_id_str, connection_manager
        )
        if should_exit:
            return None, True

        if canonical_room_id:
            ap_raw = cast(object | None, getattr(connection_manager, "async_persistence", None))
            if ap_raw is not None:
                ap = cast(_AsyncPersistenceRoomLookup, ap_raw)
                room = ap.get_room_by_id(canonical_room_id)
                if room is not None:
                    await check_and_send_death_notification(
                        websocket,
                        player_id,
                        player_id_str,
                        canonical_room_id,
                        cast(Room | dict[str, object], room),
                        connection_manager,
                    )
                    await send_initial_room_state(
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


async def _send_welcome_event(websocket: WebSocket, player_id: uuid.UUID, player_id_str: str) -> bool:
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


async def handle_websocket_connection(
    websocket: WebSocket,
    player_id: uuid.UUID,
    session_id: str | None = None,
    connection_manager: "ConnectionManager | None" = None,
    token: str | None = None,
) -> None:
    """
    Handle a WebSocket connection for a player.

    Args:
        websocket: The WebSocket connection
        player_id: The player's ID
        session_id: Optional session ID for dual connection management
        connection_manager: ConnectionManager instance (injected from endpoint)

    AI Agent: connection_manager now injected as parameter instead of global import
    """
    if await check_shutdown_and_reject(websocket, player_id):
        return

    if connection_manager is None:
        logger.error("ConnectionManager not available for WebSocket connection", player_id=player_id)
        await websocket.close(code=1008, reason="Server configuration error")
        return

    success = await connection_manager.connect_websocket(websocket, player_id, session_id, token=token)
    if not success:
        logger.error("Failed to connect WebSocket", player_id=player_id)
        return

    player_id_str = str(player_id)
    await load_player_mute_data(player_id_str)

    _, should_exit = await _setup_initial_connection_state(websocket, player_id, player_id_str, connection_manager)
    if should_exit:
        await _cleanup_connection(player_id, player_id_str, connection_manager)
        return

    if not await _send_welcome_event(websocket, player_id, player_id_str):
        await _cleanup_connection(player_id, player_id_str, connection_manager)
        return

    try:
        await _handle_websocket_message_loop(websocket, player_id, player_id_str, connection_manager)
    finally:
        await _cleanup_connection(player_id, player_id_str, connection_manager)


async def handle_websocket_message(websocket: WebSocket, player_id: str, message: dict[str, object]) -> None:
    """
    Handle a WebSocket message from a player.

    Args:
        websocket: The WebSocket connection
        player_id: The player's ID
        message: The message data
    """
    try:
        # Use the message handler factory to route messages
        from .message_handler_factory import message_handler_factory

        await message_handler_factory.handle_message(websocket, player_id, message)

    except (WebSocketDisconnect, RuntimeError) as e:
        if _is_client_gone_error(e):
            logger.debug("Client disconnected during message processing", player_id=player_id, error=str(e))
        else:
            logger.error("Error processing WebSocket message", player_id=player_id, error=str(e))
        error_response = create_websocket_error_response(
            ErrorType.MESSAGE_PROCESSING_ERROR,
            f"Error processing message: {str(e)}",
            ErrorMessages.MESSAGE_PROCESSING_ERROR,
            {"player_id": player_id},
        )
        try:
            await websocket.send_json(error_response)
        except (WebSocketDisconnect, RuntimeError) as send_err:
            if not _is_client_gone_error(send_err):
                raise
            logger.debug("Could not send error response; client already disconnected", player_id=player_id)


async def handle_chat_message(
    websocket: WebSocket, player_id: str, message: str, connection_manager: "ConnectionManager | None" = None
) -> None:
    """
    Handle a chat message from a player.

    Args:
        websocket: The WebSocket connection
        player_id: The player's ID
        message: The chat message
        connection_manager: ConnectionManager instance (optional, will resolve from app.state if not provided)
    """
    try:
        connection_manager = resolve_websocket_connection_manager(connection_manager)

        # Create chat event
        chat_event = build_event(
            "chat",
            {"player_id": player_id, "message": message},
            player_id=player_id,
        )

        # Broadcast to room
        player_id_uuid = uuid.UUID(player_id)
        player = await connection_manager.get_player(player_id_uuid)
        if player:
            _ = await connection_manager.broadcast_to_room(
                str(player.current_room_id), chat_event, exclude_player=player_id
            )

        # Send confirmation to sender
        chat_sent_event = build_event("chat_sent", {"message": "Message sent"}, player_id=player_id)
        await websocket.send_json(chat_sent_event)

    except (WebSocketDisconnect, RuntimeError) as e:
        logger.error("Error handling chat message", player_id=player_id, error=str(e))
        error_response = create_websocket_error_response(
            ErrorType.MESSAGE_PROCESSING_ERROR,
            f"Error sending chat message: {str(e)}",
            ErrorMessages.MESSAGE_PROCESSING_ERROR,
            {"player_id": player_id},
        )
        await websocket.send_json(error_response)


async def send_system_message(websocket: WebSocket, message: str, message_type: str = "info") -> None:
    """
    Send a system message to a player.

    Args:
        websocket: The WebSocket connection
        message: The message text
        message_type: The type of message (info, warning, error)
    """
    try:
        system_event = build_event(
            "system",
            {
                "message": message,
                "message_type": message_type,
            },
        )
        await websocket.send_json(system_event)

    except (WebSocketDisconnect, RuntimeError) as e:
        logger.error("Error sending system message", error=str(e))
