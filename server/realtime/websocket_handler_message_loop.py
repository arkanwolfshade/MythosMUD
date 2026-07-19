"""
WebSocket message loop, per-message processing, and loop exception handling.

Extracted from websocket_handler for Lizard file-nloc limits.
"""

import json
import uuid
from typing import TYPE_CHECKING

from fastapi import WebSocket, WebSocketDisconnect
from structlog.stdlib import BoundLogger

from ..error_types import ErrorMessages, ErrorType, create_websocket_error_response
from ..structured_logging.enhanced_logging_config import get_logger
from .websocket_helpers import is_websocket_disconnect_message

if TYPE_CHECKING:
    from .connection_manager import ConnectionManager
    from .message_validator import WebSocketMessageValidator

logger: BoundLogger = get_logger(__name__)


async def send_websocket_error_response(
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
        if is_websocket_disconnect_message(send_error_msg) or "close message has been sent" in send_error_msg:
            return False
        logger.error("Failed to send error response to client", error=send_error_msg)
        return True


async def handle_json_decode_error(websocket: WebSocket, player_id: uuid.UUID, player_id_str: str) -> None:
    """Handle JSON decode error."""
    from . import websocket_handler as ws_handler

    logger.warning("Invalid JSON from player", player_id=player_id)
    _: bool = await ws_handler._send_error_response(
        websocket,
        ErrorType.INVALID_FORMAT,
        "Invalid JSON format",
        ErrorMessages.INVALID_FORMAT,
        {"player_id": player_id_str},
    )


def handle_websocket_disconnect(player_id_str: str, connection_id: str | None) -> bool:
    """
    Handle WebSocket disconnect.

    Returns:
        True to break the loop
    """
    logger.info("WebSocket disconnected", player_id=player_id_str, connection_id=connection_id)
    return True


def handle_websocket_runtime_error(e: RuntimeError, player_id_str: str, connection_id: str | None) -> tuple[bool, bool]:
    """
    Handle RuntimeError.

    Returns:
        Tuple of (should_break, should_raise)
    """
    error_message = str(e)
    if is_websocket_disconnect_message(error_message):
        logger.warning(
            "WebSocket connection lost (not connected)",
            player_id=player_id_str,
            connection_id=connection_id,
            error=error_message,
        )
        return True, False
    return False, True


async def handle_websocket_generic_exception(
    websocket: WebSocket, e: Exception, player_id_str: str, connection_id: str | None
) -> bool:
    """
    Handle generic exception.

    Returns:
        True to break the loop
    """
    from . import websocket_handler as ws_handler

    logger.error(
        "Error handling WebSocket message",
        player_id=player_id_str,
        connection_id=connection_id,
        error=str(e),
        error_type=type(e).__name__,
        exc_info=True,
    )
    should_break = not await ws_handler._send_error_response(
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


async def process_websocket_inbound_message(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Message processing requires many parameters for context and message handling
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
    from . import websocket_handler as ws_handler

    if not await ws_handler._check_rate_limit(websocket, connection_id, player_id_str, connection_manager):
        return True

    message = await ws_handler._validate_message(
        websocket,
        data,
        player_id_str,
        validator,
        connection_manager=connection_manager,
    )
    if message is None:
        return True

    connection_manager.mark_player_seen(player_id)
    await ws_handler.handle_websocket_message(websocket, player_id_str, message)
    return True


async def handle_message_loop_exception(
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
        await handle_json_decode_error(websocket, player_id, player_id_str)
        return False, False

    if isinstance(e, WebSocketDisconnect):
        return handle_websocket_disconnect(player_id_str, connection_id), False

    if isinstance(e, RuntimeError):
        return handle_websocket_runtime_error(e, player_id_str, connection_id)

    should_break = await handle_websocket_generic_exception(websocket, e, player_id_str, connection_id)
    return should_break, False


async def process_exception_in_message_loop(
    websocket: WebSocket, e: Exception, player_id: uuid.UUID, player_id_str: str, connection_id: str
) -> tuple[bool, bool]:
    """Process exception in message loop and return (should_break, should_raise)."""
    from . import websocket_handler as ws_handler

    should_break, should_raise = await ws_handler._handle_message_loop_exception(
        websocket, e, player_id, player_id_str, connection_id
    )
    return should_break, should_raise


async def handle_websocket_message_loop(
    websocket: WebSocket, player_id: uuid.UUID, player_id_str: str, connection_manager: "ConnectionManager"
) -> None:
    """Handle the main WebSocket message loop."""
    from . import websocket_handler as ws_handler
    from .message_validator import get_message_validator

    validator = get_message_validator()
    connection_id = connection_manager.get_connection_id_from_websocket(websocket)
    # connection_id can be None if websocket is not connected, use empty string as fallback
    connection_id_str = connection_id if connection_id is not None else ""

    while True:
        try:
            data = await websocket.receive_text()
            _: bool = await ws_handler._process_message(
                websocket, data, player_id, player_id_str, connection_id, connection_manager, validator
            )
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Message loop errors unpredictable, must prevent crash
            # Handle all exceptions uniformly through the exception handler
            # This consolidates multiple exception handlers into one to reduce complexity
            should_break, should_raise = await ws_handler._process_exception_in_message_loop(
                websocket, e, player_id, player_id_str, connection_id_str
            )
            if should_break:
                break
            if should_raise:
                raise
