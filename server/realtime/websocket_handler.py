"""
WebSocket handler for MythosMUD real-time communication.

This module handles WebSocket message processing, command handling,
and real-time updates for the game.
"""

# pylint: disable=too-many-arguments,too-many-positional-arguments,too-many-locals,too-many-lines  # Reason: WebSocket handler requires many parameters and intermediate variables for complex message processing logic. WebSocket handler requires extensive message processing logic for comprehensive real-time communication.

import json
import time
import uuid
from typing import Any

from fastapi import WebSocket, WebSocketDisconnect

from ..error_types import ErrorMessages, ErrorType, create_websocket_error_response
from ..structured_logging.enhanced_logging_config import get_logger
from .envelope import build_event
from .websocket_helpers import check_shutdown_and_reject, load_player_mute_data
from .websocket_initial_state import (
    check_and_send_death_notification,
    send_initial_game_state,
    send_initial_room_state,
)
from .websocket_room_updates import broadcast_room_update

# AI Agent: Don't import app at module level - causes circular import!
#           Import locally in functions instead

# Re-export broadcast_room_update for backward compatibility
__all__ = [
    "handle_websocket_connection",
    "handle_websocket_message",
    "handle_game_command",
    "process_websocket_command",
    "handle_chat_message",
    "get_help_content",
    "send_system_message",
    "broadcast_room_update",  # Re-exported from websocket_room_updates
]

logger = get_logger(__name__)


def _is_websocket_disconnected(error_message: str) -> bool:
    """Check if error message indicates WebSocket disconnection."""
    return "WebSocket is not connected" in error_message or 'Need to call "accept" first' in error_message


async def _check_rate_limit(
    websocket: WebSocket, connection_id: str | None, player_id_str: str, connection_manager
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
    error_response = create_websocket_error_response(
        ErrorType.RATE_LIMIT_EXCEEDED,
        f"Message rate limit exceeded. Limit: {rate_limit_info['max_attempts']} messages per minute. Try again in {int(rate_limit_info['reset_time'] - time.time())} seconds.",
        ErrorMessages.RATE_LIMIT_EXCEEDED,
        {
            "player_id": player_id_str,
            "connection_id": connection_id,
            "rate_limit_info": rate_limit_info,
        },
    )
    await websocket.send_json(error_response)
    return False


async def _validate_message(websocket: WebSocket, data: str, player_id_str: str, validator) -> dict | None:
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
    websocket: WebSocket, error_type: ErrorType, message: str, error_message: str, extra_data: dict
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
    await _send_error_response(
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
    connection_manager,
    validator,
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
    websocket: WebSocket, player_id: uuid.UUID, player_id_str: str, connection_manager
) -> None:
    """Handle the main WebSocket message loop."""
    from .message_validator import get_message_validator

    validator = get_message_validator()
    connection_id = connection_manager.get_connection_id_from_websocket(websocket)

    while True:
        try:
            data = await websocket.receive_text()
            await _process_message(
                websocket, data, player_id, player_id_str, connection_id, connection_manager, validator
            )
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Message loop errors unpredictable, must prevent crash
            # Handle all exceptions uniformly through the exception handler
            # This consolidates multiple exception handlers into one to reduce complexity
            should_break, should_raise = await _process_exception_in_message_loop(
                websocket, e, player_id, player_id_str, connection_id
            )
            if should_break:
                break
            if should_raise:
                raise


async def _cleanup_connection(player_id: uuid.UUID, player_id_str: str, connection_manager) -> None:
    """Clean up connection and player mute data on disconnect."""
    try:
        await connection_manager.disconnect_websocket(player_id)
    except (WebSocketDisconnect, RuntimeError) as e:
        logger.error("Error disconnecting WebSocket", player_id=player_id, error=str(e))

    try:
        from ..services.user_manager import user_manager

        user_manager.cleanup_player_mutes(player_id_str)
        logger.info("Cleaned up mute data", player_id=player_id)
    except (WebSocketDisconnect, RuntimeError) as e:
        logger.error("Error cleaning up mute data", player_id=player_id, error=str(e))


async def handle_websocket_connection(
    websocket: WebSocket,
    player_id: uuid.UUID,
    session_id: str | None = None,
    connection_manager=None,
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

    success = await connection_manager.connect_websocket(websocket, player_id, session_id, token=token)
    if not success:
        logger.error("Failed to connect WebSocket", player_id=player_id)
        return

    player_id_str = str(player_id)
    await load_player_mute_data(player_id_str)

    try:
        canonical_room_id, should_exit = await send_initial_game_state(
            websocket, player_id, player_id_str, connection_manager
        )
        if should_exit:
            return

        if canonical_room_id:
            from ..async_persistence import get_async_persistence

            async_persistence = get_async_persistence()
            if async_persistence:
                room = async_persistence.get_room_by_id(canonical_room_id)
                if room:
                    await check_and_send_death_notification(
                        websocket, player_id, player_id_str, canonical_room_id, room, connection_manager
                    )
                    await send_initial_room_state(
                        websocket, player_id, player_id_str, canonical_room_id, connection_manager
                    )
    except (WebSocketDisconnect, RuntimeError) as e:
        logger.error("Error in initial connection setup", player_id=player_id, error=str(e), exc_info=True)

    welcome_event = build_event("welcome", {"message": "Connected to MythosMUD"}, player_id=player_id_str)
    await websocket.send_json(welcome_event)

    try:
        await _handle_websocket_message_loop(websocket, player_id, player_id_str, connection_manager)
    finally:
        await _cleanup_connection(player_id, player_id_str, connection_manager)


async def handle_websocket_message(websocket: WebSocket, player_id: str, message: dict) -> None:
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
        logger.error("Error processing WebSocket message", player_id=player_id, error=str(e))
        error_response = create_websocket_error_response(
            ErrorType.MESSAGE_PROCESSING_ERROR,
            f"Error processing message: {str(e)}",
            ErrorMessages.MESSAGE_PROCESSING_ERROR,
            {"player_id": player_id},
        )
        await websocket.send_json(error_response)


async def handle_game_command(
    websocket: WebSocket,
    player_id: str,
    command: str,
    args: list[Any] | None = None,
    connection_manager=None,
) -> None:
    """
    Handle a game command from a player.

    Args:
        websocket: The WebSocket connection
        player_id: The player's ID
        command: The command string
        args: Command arguments (optional, will parse from command if not provided)
        connection_manager: ConnectionManager instance (optional, will resolve from app.state if not provided)
    """
    try:
        # Resolve connection_manager if not provided (backward compatibility)
        if connection_manager is None:
            from ..main import app

            connection_manager = app.state.container.connection_manager
        # Parse command and arguments if args not provided
        if args is None:
            parts = command.strip().split()
            if not parts:
                error_response = create_websocket_error_response(
                    ErrorType.INVALID_COMMAND, "Empty command", ErrorMessages.INVALID_COMMAND, {"player_id": player_id}
                )
                await websocket.send_json(error_response)
                return

            cmd = parts[0].lower()
            args = parts[1:] if len(parts) > 1 else []
        else:
            cmd = command.lower()

        # Simple command processing for WebSocket
        result = await process_websocket_command(cmd, args, player_id, connection_manager=connection_manager)

        # Send the result back to the player
        await websocket.send_json(build_event("command_response", result, player_id=player_id))

        # Handle broadcasting if the command result includes broadcast data
        if result.get("broadcast") and result.get("broadcast_type"):
            logger.debug("Broadcasting message to room", broadcast_type=result.get("broadcast_type"), player=player_id)
            player = await connection_manager.get_player(player_id)
            if player and hasattr(player, "current_room_id"):
                room_id = player.current_room_id
                broadcast_event = build_event("command_response", {"result": result["broadcast"]}, player_id=player_id)
                await connection_manager.broadcast_to_room(str(room_id), broadcast_event, exclude_player=player_id)
                logger.debug(
                    "Broadcasted message to room", broadcast_type=result.get("broadcast_type"), room_id=room_id
                )
            else:
                logger.warning("Player not found or missing current_room_id for broadcast", player_id=player_id)

        # ARCHITECTURE FIX: Removed duplicate broadcast_room_update() calls (Phase 1.2)
        # Room state updates now flow exclusively through EventBus:
        #   Movement → Room.player_entered() → PlayerEnteredRoom event
        #   → EventBus → RealTimeEventHandler → "player_entered" message to clients
        # This eliminates duplicate messages and ensures consistent event ordering
        #
        # Note: Moving player receives their updated room state via command_response
        # Other players receive "player_entered" notification via EventBus flow
        # No additional broadcast needed here
        logger.debug("Command completed, room updates handled via EventBus flow", command=cmd)

    except (WebSocketDisconnect, RuntimeError) as e:
        logger.error("Error processing command", command=command, player_id=player_id, error=str(e))
        error_response = create_websocket_error_response(
            ErrorType.MESSAGE_PROCESSING_ERROR,
            f"Error processing command: {str(e)}",
            ErrorMessages.MESSAGE_PROCESSING_ERROR,
            {"player_id": player_id, "command": command},
        )
        await websocket.send_json(error_response)


async def process_websocket_command(cmd: str, args: list, player_id: str, connection_manager=None) -> dict:
    """
    Process a command for WebSocket connections.

    Args:
        cmd: The command name
        args: Command arguments
        player_id: The player's ID
        connection_manager: ConnectionManager instance (optional, will resolve from app.state if not provided)

    Returns:
        dict: Command result
    """
    logger.debug("Processing command", cmd=cmd, args=args, player_id=player_id)

    # Resolve connection_manager if not provided (backward compatibility)
    if connection_manager is None:
        from ..main import app

        connection_manager = app.state.container.connection_manager

    # Get player from connection manager
    logger.debug("Getting player for ID", player_id=player_id, player_id_type=type(player_id))
    player = await connection_manager.get_player(player_id)
    logger.debug("Player object", player=player, player_type=type(player))
    if not player:
        logger.warning("Player not found", player_id=player_id)
        return {"result": "Player not found"}

    # Check if player is actually a Player object
    if not hasattr(player, "current_room_id"):
        logger.error("Player object is not a Player instance", player_type=type(player))
        return {"result": "Player data error"}

    # Get async persistence from connection manager
    async_persistence = connection_manager.async_persistence
    if not async_persistence:
        logger.warning("Async persistence layer not available")
        return {"result": "Game system unavailable"}

    # CRITICAL FIX: Removed special case for "go" command
    # The unified command handler (called below) will handle "go" commands
    # and apply all necessary checks including catatonia validation
    # The old special case bypassed catatonia checks, allowing catatonic players to move
    # All commands (including "go" and "look") now go through the unified handler

    # Use the unified command handler for all commands
    from ..alias_storage import AliasStorage
    from ..command_handler_unified import process_command_unified
    from ..config import get_config
    from ..realtime.request_context import create_websocket_request_context

    # Create proper request context for WebSocket using real app state
    app_state = connection_manager.app.state if hasattr(connection_manager, "app") and connection_manager.app else None
    if not app_state:
        logger.error("No app state available for WebSocket request context")
        return {"result": "Server configuration error. Please try again."}

    request_context = create_websocket_request_context(
        app_state=app_state,
        user=player,
    )

    # Get player name for the command handler
    player_name = getattr(player, "name", "Unknown")

    # Create alias storage with proper directory from config
    config = get_config()
    aliases_dir = config.game.aliases_dir
    alias_storage = AliasStorage(storage_dir=aliases_dir) if aliases_dir else AliasStorage()
    request_context.set_alias_storage(alias_storage)

    # Verify app state services are available (they should already be in the real app state)
    player_service = getattr(app_state, "player_service", None)
    user_manager = getattr(app_state, "user_manager", None)
    logger.debug("App state services available", player_service=player_service, user_manager=user_manager)

    if not player_service or not user_manager:
        logger.warning("Missing required app state services - player_service or user_manager not available")

    # Process the command using the unified command handler
    command_line = f"{cmd} {' '.join(args)}".strip()
    result = await process_command_unified(
        command_line=command_line,
        current_user=player,
        # WebSocketRequestContext provides duck-typed Request interface but isn't a subclass
        # This is intentional - WebSocket contexts need different lifecycle than HTTP Requests
        request=request_context,  # type: ignore[arg-type]  # Reason: WebSocketRequestContext provides duck-typed Request interface but isn't a subclass, WebSocket contexts need different lifecycle than HTTP Requests
        alias_storage=alias_storage,
        player_name=player_name,
    )
    if not isinstance(result, dict):
        raise TypeError("Command handler must return a dict")
    return result


def get_help_content(command_name: str | None = None) -> str:
    """Get help content for commands."""
    if command_name:
        # Return specific command help
        return f"Help for '{command_name}': Command not found or help not available."

    # Return general help
    return """
Available Commands:
- look [direction]: Examine your surroundings
- go <direction>: Move in a direction
- say <message>: Say something
- help [command]: Get help on commands

Directions: north, south, east, west
"""


async def handle_chat_message(websocket: WebSocket, player_id: str, message: str, connection_manager=None) -> None:
    """
    Handle a chat message from a player.

    Args:
        websocket: The WebSocket connection
        player_id: The player's ID
        message: The chat message
        connection_manager: ConnectionManager instance (optional, will resolve from app.state if not provided)
    """
    try:
        # Resolve connection_manager if not provided (backward compatibility)
        if connection_manager is None:
            from ..main import app

            connection_manager = app.state.container.connection_manager

        # Create chat event
        chat_event = build_event(
            "chat",
            {"player_id": player_id, "message": message},
            player_id=player_id,
        )

        # Broadcast to room
        player = await connection_manager.get_player(player_id)
        if player:
            await connection_manager.broadcast_to_room(
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
