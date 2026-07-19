"""
WebSocket handler for MythosMUD real-time communication.

This module handles WebSocket message processing, command handling,
and real-time updates for the game. Callers should pass connection_manager
from the WebSocket pipeline when invoking handle_game_command,
process_websocket_command, or handle_chat_message.
"""

import uuid
from typing import TYPE_CHECKING

from fastapi import WebSocket, WebSocketDisconnect
from structlog.stdlib import BoundLogger

from ..error_types import ErrorMessages, ErrorType, create_websocket_error_response
from ..structured_logging.enhanced_logging_config import get_logger
from .envelope import build_event
from .websocket_handler_app_state import resolve_and_setup_app_state_services
from .websocket_handler_commands import (
    handle_game_command,
    process_websocket_command,
    resolve_websocket_connection_manager,
    validate_player_and_persistence,
)
from .websocket_handler_connection import (
    cleanup_websocket_connection,
    send_welcome_event,
    setup_initial_connection_state,
)
from .websocket_handler_message_loop import (
    handle_json_decode_error,
    handle_message_loop_exception,
    handle_websocket_disconnect,
    handle_websocket_generic_exception,
    handle_websocket_message_loop,
    handle_websocket_runtime_error,
    process_exception_in_message_loop,
    process_websocket_inbound_message,
    send_websocket_error_response,
)
from .websocket_handler_validation import check_websocket_message_rate_limit, validate_websocket_message
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
    "send_initial_game_state",
    "check_and_send_death_notification",
    "send_initial_room_state",
]

logger: BoundLogger = get_logger(__name__)

# Test and legacy import names (basedpyright: public symbols from submodules, not private cross-imports).
_resolve_and_setup_app_state_services = resolve_and_setup_app_state_services
_validate_player_and_persistence = validate_player_and_persistence

# Backward-compatible names for tests and internal call sites (implementation in websocket_helpers).
_is_websocket_disconnected = is_websocket_disconnect_message
_is_client_gone_error = is_client_disconnected_exception

# Backward-compatible aliases for extracted validation helpers.
_check_rate_limit = check_websocket_message_rate_limit
_validate_message = validate_websocket_message

# Backward-compatible aliases for extracted message-loop helpers.
_send_error_response = send_websocket_error_response
_handle_json_decode_error = handle_json_decode_error
_handle_websocket_disconnect = handle_websocket_disconnect
_handle_runtime_error = handle_websocket_runtime_error
_handle_generic_exception = handle_websocket_generic_exception
_process_message = process_websocket_inbound_message
_handle_message_loop_exception = handle_message_loop_exception
_process_exception_in_message_loop = process_exception_in_message_loop
_handle_websocket_message_loop = handle_websocket_message_loop

# Backward-compatible aliases for extracted connection lifecycle helpers.
_cleanup_connection = cleanup_websocket_connection
_setup_initial_connection_state = setup_initial_connection_state
_send_welcome_event = send_welcome_event


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
