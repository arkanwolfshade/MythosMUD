"""
WebSocket game command processing (parse, unified handler, broadcast).

Extracted from websocket_handler for Lizard file/method limits and lower CCN.
"""

import uuid
from collections.abc import Awaitable, Callable
from typing import TYPE_CHECKING, cast

from fastapi import WebSocket, WebSocketDisconnect
from structlog.stdlib import BoundLogger

from ..error_types import ErrorMessages, ErrorType, create_websocket_error_response
from ..structured_logging.enhanced_logging_config import get_logger
from .envelope import build_event
from .websocket_handler_app_state import resolve_and_setup_app_state_services
from .websocket_helpers import is_client_disconnected_exception

if TYPE_CHECKING:
    from .connection_manager import ConnectionManager

logger: BoundLogger = cast(BoundLogger, get_logger(__name__))


def resolve_websocket_connection_manager(connection_manager: "ConnectionManager | None") -> "ConnectionManager":
    """
    Resolve ConnectionManager; fallback to app.state for backward compatibility.

    Callers should pass connection_manager from the WebSocket pipeline when invoking
    handle_game_command, process_websocket_command, or handle_chat_message.
    """
    if connection_manager is not None:
        return connection_manager
    from ..main import app

    st = cast(object | None, getattr(app, "state", None))
    container = cast(object | None, getattr(st, "container", None)) if st is not None else None
    cm = cast(object | None, getattr(container, "connection_manager", None)) if container is not None else None
    return cast("ConnectionManager", cm)


async def validate_player_and_persistence(
    connection_manager: "ConnectionManager", player_id: str
) -> tuple[object | None, str | None]:
    """Validate player and persistence availability."""
    logger.debug("Getting player for ID", player_id=player_id, player_id_type=type(player_id))
    player_id_uuid = uuid.UUID(player_id)
    player = await connection_manager.get_player(player_id_uuid)
    logger.debug("Player object", player=player, player_type=type(player))
    if not player:
        logger.warning("Player not found", player_id=player_id)
        return None, "Player not found"

    if not hasattr(player, "current_room_id"):
        logger.error("Player object is not a Player instance", player_type=type(player))
        return None, "Player data error"

    async_persistence = connection_manager.async_persistence
    if not async_persistence:
        logger.warning("Async persistence layer not available")
        return None, "Game system unavailable"

    return player, None


def _parse_game_command_tokens(command: str, args: list[object] | None) -> tuple[str, list[str]] | None:
    """
    Return (cmd_lower, arg_list) or None if command is empty after strip.

    When args is None, command string is split on whitespace.
    """
    if args is None:
        parts = command.strip().split()
        if not parts:
            return None
        cmd = parts[0].lower()
        rest = parts[1:] if len(parts) > 1 else []
        return cmd, rest
    return command.lower(), [str(a) for a in args]


async def _send_invalid_command_empty(websocket: WebSocket, player_id: str) -> None:
    error_response = create_websocket_error_response(
        ErrorType.INVALID_COMMAND, "Empty command", ErrorMessages.INVALID_COMMAND, {"player_id": player_id}
    )
    await websocket.send_json(error_response)


async def _broadcast_command_room_if_needed(
    connection_manager: "ConnectionManager",
    player_id: str,
    result: dict[str, object],
    cmd: str,
) -> None:
    """Broadcast command_response to room when result requests it."""
    if not (result.get("broadcast") and result.get("broadcast_type")):
        return

    logger.debug("Broadcasting message to room", broadcast_type=result.get("broadcast_type"), player=player_id)
    player_id_uuid = uuid.UUID(player_id)
    player = await connection_manager.get_player(player_id_uuid)
    if player and hasattr(player, "current_room_id"):
        room_id = player.current_room_id
        broadcast_event = build_event("command_response", {"result": result["broadcast"]}, player_id=player_id)
        _ = await connection_manager.broadcast_to_room(str(room_id), broadcast_event, exclude_player=player_id)
        logger.debug("Broadcasted message to room", broadcast_type=result.get("broadcast_type"), room_id=room_id)
    else:
        logger.warning("Player not found or missing current_room_id for broadcast", player_id=player_id)

    logger.debug("Command completed, room updates handled via EventBus flow", command=cmd)


async def handle_game_command(
    websocket: WebSocket,
    player_id: str,
    command: str,
    args: list[object] | None = None,
    connection_manager: "ConnectionManager | None" = None,
) -> None:
    """
    Handle a game command from a player.

    Args:
        websocket: The WebSocket connection
        player_id: The player's ID
        command: The command string
        args: Command arguments (optional, will parse from command if not provided)
        connection_manager: ConnectionManager instance (optional; prefer passing from WebSocket pipeline)
    """
    try:
        cm = resolve_websocket_connection_manager(connection_manager)
        parsed = _parse_game_command_tokens(command, args)
        if parsed is None:
            await _send_invalid_command_empty(websocket, player_id)
            return
        cmd, cmd_args = parsed

        result = await process_websocket_command(cmd, cmd_args, player_id, connection_manager=cm)
        await websocket.send_json(build_event("command_response", result, player_id=player_id))
        await _broadcast_command_room_if_needed(cm, player_id, result, cmd)

    except (WebSocketDisconnect, RuntimeError) as e:
        if is_client_disconnected_exception(e):
            logger.debug("Client disconnected during command", command=command, player_id=player_id, error=str(e))
        else:
            logger.error("Error processing command", command=command, player_id=player_id, error=str(e))
        error_response = create_websocket_error_response(
            ErrorType.MESSAGE_PROCESSING_ERROR,
            f"Error processing command: {str(e)}",
            ErrorMessages.MESSAGE_PROCESSING_ERROR,
            {"player_id": player_id, "command": command},
        )
        try:
            await websocket.send_json(error_response)
        except (WebSocketDisconnect, RuntimeError) as send_err:
            if not is_client_disconnected_exception(send_err):
                raise
            logger.debug("Could not send command error response; client already disconnected", player_id=player_id)


async def _attach_room_state_to_result(result: dict[str, object], app_state: object, player_id: str) -> None:
    """Mutate result with room_state when player moved and handler supports it."""
    if not (result.get("room_changed") and result.get("room_id")):
        return
    event_handler = cast(object | None, getattr(app_state, "event_handler", None))
    if not event_handler or not hasattr(event_handler, "player_handler"):
        return
    try:
        eh: object = event_handler
        player_handler = cast(object | None, getattr(eh, "player_handler", None))
        if player_handler is None:
            return
        ph: object = player_handler
        get_room_raw = getattr(ph, "get_room_state_event", None)
        if not callable(get_room_raw):
            return
        get_room = cast(Callable[[str, object], Awaitable[object | None]], get_room_raw)
        room_state_event = await get_room(player_id, result["room_id"])
        if room_state_event:
            result["room_state"] = room_state_event
    except (TypeError, ValueError, AttributeError) as room_state_err:
        logger.debug(
            "Could not attach room_state to command_response",
            player_id=player_id,
            room_id=result.get("room_id"),
            error=str(room_state_err),
        )


async def process_websocket_command(
    cmd: str, args: list[str], player_id: str, connection_manager: "ConnectionManager | None" = None
) -> dict[str, object]:
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

    cm = resolve_websocket_connection_manager(connection_manager)
    player, error_result = await validate_player_and_persistence(cm, player_id)
    if error_result:
        return {"result": error_result}

    from ..alias_storage import AliasStorage
    from ..command_handler_unified import process_command_unified
    from ..config import get_config
    from ..realtime.request_context import create_websocket_request_context

    cm_app: object | None = getattr(cm, "app", None)
    app_state: object | None = getattr(cm_app, "state", None) if cm_app is not None else None
    if not app_state:
        logger.error("No app state available for WebSocket request context")
        return {"result": "Server configuration error. Please try again."}

    request_context = create_websocket_request_context(
        app_state=app_state,
        user=player,
    )
    player_name = cast(str, getattr(player, "name", "Unknown"))
    config = get_config()
    aliases_dir = config.game.aliases_dir
    alias_storage = AliasStorage(storage_dir=aliases_dir) if aliases_dir else AliasStorage()
    request_context.set_alias_storage(alias_storage)

    _ = resolve_and_setup_app_state_services(app_state, request_context)

    command_line = f"{cmd} {' '.join(str(a) for a in args)}".strip()
    unified_obj = cast(
        object,
        await process_command_unified(
            command_line=command_line,
            current_user=player,
            request=request_context,
            alias_storage=alias_storage,
            player_name=player_name,
        ),
    )
    if not isinstance(unified_obj, dict):
        raise TypeError("Command handler must return a dict")
    result = cast(dict[str, object], unified_obj)

    await _attach_room_state_to_result(result, app_state, player_id)
    return result
