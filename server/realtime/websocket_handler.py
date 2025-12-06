"""
WebSocket handler for MythosMUD real-time communication.

This module handles WebSocket message processing, command handling,
and real-time updates for the game.
"""

import json
import time
import uuid
from typing import Any

from fastapi import WebSocket, WebSocketDisconnect

from ..error_types import ErrorMessages, ErrorType, create_websocket_error_response
from ..logging.enhanced_logging_config import get_logger
from ..utils.room_renderer import build_room_drop_summary, clone_room_drops
from .envelope import build_event

# AI Agent: Don't import app at module level - causes circular import!
#           Import locally in functions instead

logger = get_logger(__name__)


def _get_npc_name_from_instance(npc_id: str) -> str | None:
    """
    Get NPC name from the actual NPC instance, preserving original case from database.

    This is the proper way to get NPC names - directly from the database via the NPC instance.

    Args:
        npc_id: The NPC ID

    Returns:
        NPC name from the database, or None if instance not found
    """
    try:
        # Get the NPC instance from the spawning service
        from ..services.npc_instance_service import get_npc_instance_service

        npc_instance_service = get_npc_instance_service()
        if hasattr(npc_instance_service, "lifecycle_manager"):
            lifecycle_manager = npc_instance_service.lifecycle_manager
            if lifecycle_manager and npc_id in lifecycle_manager.active_npcs:
                npc_instance = lifecycle_manager.active_npcs[npc_id]
                name = getattr(npc_instance, "name", None)
                return name

        return None
    except Exception as e:
        logger.debug("Error getting NPC name from instance", npc_id=npc_id, error=str(e))
        return None


async def _check_shutdown_and_reject(websocket: WebSocket, player_id: uuid.UUID) -> bool:
    """Check if server is shutting down and reject connection if so. Returns True if rejected."""
    from ..commands.admin_shutdown_command import get_shutdown_blocking_message, is_shutdown_pending

    try:
        if hasattr(websocket, "app") and is_shutdown_pending(websocket.app):
            error_message = get_shutdown_blocking_message("motd_progression")
            await websocket.send_json({"type": "error", "message": error_message})
            logger.info("DEBUG: Closing WebSocket due to server shutdown", player_id=player_id)
            await websocket.close(code=1001, reason="Server shutting down")
            logger.info("Rejected WebSocket connection - server shutting down", player_id=player_id)
            return True
    except Exception as e:
        logger.debug("Could not check shutdown status in WebSocket connection", error=str(e))
    return False


def _load_player_mute_data(player_id_str: str) -> None:
    """Load player mute data when they connect."""
    try:
        from ..services.user_manager import user_manager

        user_manager.load_player_mutes(player_id_str)
        logger.info("Loaded mute data", player_id=player_id_str)
    except Exception as e:
        logger.error("Error loading mute data", player_id=player_id_str, error=str(e))


def _validate_occupant_name(name: str) -> bool:
    """Validate that a name is not a UUID string."""
    if not name or not isinstance(name, str):
        return False
    is_uuid = len(name) == 36 and name.count("-") == 4 and all(c in "0123456789abcdefABCDEF-" for c in name)
    return not is_uuid


async def _get_occupant_names(room_occupants: list[dict[str, Any]], room_id: str) -> list[str]:
    """Extract and validate occupant names from room occupants list."""
    occupant_names = []
    try:
        for occ in room_occupants or []:
            name = occ.get("player_name") or occ.get("name")
            if name and _validate_occupant_name(name):
                occupant_names.append(name)
            elif name:
                logger.warning("Skipping UUID as player name", name=name, room_id=room_id)
    except Exception as e:
        logger.error("Error transforming occupants", room_id=room_id, error=str(e))
    return occupant_names


def _convert_uuids_to_strings(obj: Any) -> Any:
    """Recursively convert UUID objects to strings for JSON serialization."""
    if isinstance(obj, dict):
        return {k: _convert_uuids_to_strings(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [_convert_uuids_to_strings(item) for item in obj]
    elif hasattr(obj, "__class__") and "UUID" in obj.__class__.__name__:
        return str(obj)
    else:
        return obj


async def _prepare_player_data(player, player_id: uuid.UUID, connection_manager) -> dict[str, Any]:
    """Prepare complete player data with profession information for client."""
    try:
        app_state = None
        if hasattr(connection_manager, "app") and connection_manager.app:
            app_state = getattr(connection_manager.app, "state", None)
        player_service = getattr(app_state, "player_service", None) if app_state else None

        if player_service:
            complete_player_data = await player_service._convert_player_to_schema(player)
            player_data_for_client = (
                complete_player_data.model_dump(mode="json")
                if hasattr(complete_player_data, "model_dump")
                else complete_player_data.dict()
            )
            if "experience_points" in player_data_for_client:
                player_data_for_client["xp"] = player_data_for_client["experience_points"]
            return player_data_for_client
        else:
            logger.warning("PlayerService not available, using basic player data", player_id=player_id)
            stats_data = player.get_stats() if hasattr(player, "get_stats") else {}
            if isinstance(stats_data, str):
                stats_data = json.loads(stats_data)
            if "health" not in stats_data and "current_health" in stats_data:
                stats_data["health"] = stats_data.get("current_health")
            return {
                "name": player.name,
                "level": getattr(player, "level", 1),
                "xp": getattr(player, "experience_points", 0),
                "stats": stats_data,
            }
    except Exception as e:
        logger.error("Error getting complete player data", error=str(e), player_id=player_id, exc_info=True)
        stats_data = player.get_stats() if hasattr(player, "get_stats") else {}
        if isinstance(stats_data, str):
            stats_data = json.loads(stats_data)
        return {
            "name": player.name,
            "level": getattr(player, "level", 1),
            "xp": getattr(player, "experience_points", 0),
            "stats": stats_data,
        }


async def _send_initial_game_state(
    websocket: WebSocket, player_id: uuid.UUID, player_id_str: str, connection_manager
) -> tuple[str | None, bool]:
    """
    Send initial game state to connecting player.
    Returns tuple of (canonical_room_id, should_exit).
    """
    from starlette.websockets import WebSocketState

    try:
        player = await connection_manager._get_player(player_id)
        if not player or not hasattr(player, "current_room_id"):
            return None, False

        from ..async_persistence import get_async_persistence

        async_persistence = get_async_persistence()
        if not async_persistence:
            return None, False

        room = async_persistence.get_room_by_id(str(player.current_room_id))
        if not room:
            return None, False

        if not room.has_player(player_id_str):
            logger.info("Adding player to room", player_id=player_id, room_id=str(player.current_room_id))
            room.player_entered(player_id_str)

        canonical_room_id = getattr(room, "id", None) or player.current_room_id
        room_occupants = await connection_manager.get_room_occupants(str(canonical_room_id))
        occupant_names = await _get_occupant_names(room_occupants, str(canonical_room_id))

        room_data = room.to_dict() if hasattr(room, "to_dict") else room
        if isinstance(room_data, dict):
            room_data = await connection_manager._convert_room_players_uuids_to_names(room_data)
        room_data = _convert_uuids_to_strings(room_data)

        stats_data = {}
        try:
            if hasattr(player, "get_stats"):
                stats_data = player.get_stats()
            else:
                raw_stats = getattr(player, "stats", {})
                if isinstance(raw_stats, str):
                    stats_data = json.loads(raw_stats)
                elif isinstance(raw_stats, dict):
                    stats_data = raw_stats
        except (ValueError, TypeError, json.JSONDecodeError) as e:
            logger.error("Error parsing stats data", error=str(e), error_type=type(e).__name__)
            stats_data = {}

        if "health" not in stats_data and "current_health" in stats_data:
            try:
                stats_data["health"] = stats_data.get("current_health")
            except (KeyError, TypeError) as e:
                logger.debug("Error normalizing health field", error=str(e), error_type=type(e).__name__)

        player_data_for_client = await _prepare_player_data(player, player_id, connection_manager)

        game_state_event = build_event(
            "game_state",
            {
                "player": player_data_for_client,
                "room": room_data,
                "occupants": occupant_names,
                "occupant_count": len(occupant_names),
            },
            player_id=player_id_str,
            room_id=str(canonical_room_id),
        )

        ws_state = getattr(websocket, "application_state", None)
        if ws_state == WebSocketState.DISCONNECTED:
            logger.warning("WebSocket already disconnected, skipping game_state send", player_id=player_id_str)
            return canonical_room_id, True

        try:
            await websocket.send_json(game_state_event)
        except RuntimeError as send_err:
            if "close message has been sent" in str(send_err) or "Cannot call" in str(send_err):
                logger.warning(
                    "WebSocket closed during send, exiting connection handler",
                    player_id=player_id_str,
                    error=str(send_err),
                )
                return canonical_room_id, True
            raise

        return canonical_room_id, False
    except Exception as e:
        logger.error("Error sending initial game state", player_id=player_id, error=str(e), exc_info=True)
        return None, False


async def _check_and_send_death_notification(
    websocket: WebSocket, player_id: uuid.UUID, player_id_str: str, canonical_room_id: str, room, connection_manager
) -> None:
    """Check if player is dead and send death notification if needed."""
    from ..async_persistence import get_async_persistence
    from ..services.player_respawn_service import LIMBO_ROOM_ID

    async_persistence = get_async_persistence()
    fresh_player = await async_persistence.get_player_by_id(player_id)
    if fresh_player:
        player = fresh_player
        canonical_room_id = str(player.current_room_id) if hasattr(player, "current_room_id") else canonical_room_id
    else:
        player = await connection_manager._get_player(player_id)
        if not player:
            return

    stats = player.get_stats() if hasattr(player, "get_stats") else {}
    current_hp = stats.get("current_health", 100)
    if not isinstance(current_hp, int):
        current_hp = 100

    if current_hp <= -10 or str(canonical_room_id) == LIMBO_ROOM_ID:
        death_location_name = room.name if room else "Unknown Location"
        death_event = build_event(
            "player_died",
            {
                "player_id": player_id_str,
                "player_name": player.name,
                "death_location": death_location_name,
                "message": "You have died. The darkness claims you utterly.",
            },
            player_id=player_id_str,
        )
        await websocket.send_json(death_event)
        logger.info(
            "Sent death notification to player on login",
            player_id=player_id_str,
            current_hp=current_hp,
            in_limbo=str(canonical_room_id) == LIMBO_ROOM_ID,
        )


async def _send_initial_room_state(
    websocket: WebSocket, player_id: uuid.UUID, player_id_str: str, canonical_room_id: str, connection_manager
) -> None:
    """Send initial room state and occupants snapshot to connecting player."""
    try:
        from ..async_persistence import get_async_persistence

        async_persistence = get_async_persistence()
        room = async_persistence.get_room_by_id(canonical_room_id)
        if not room:
            return

        room_occupants = await connection_manager.get_room_occupants(str(canonical_room_id))
        occupant_names = await _get_occupant_names(room_occupants, canonical_room_id)

        if hasattr(connection_manager, "app") and hasattr(connection_manager.app.state, "npc_lifecycle_manager"):
            npc_lifecycle_manager = connection_manager.app.state.npc_lifecycle_manager
            npc_ids = room.get_npcs()
            for npc_id in npc_ids:
                npc = npc_lifecycle_manager.active_npcs.get(npc_id)
                if npc and hasattr(npc, "name"):
                    occupant_names.append(npc.name)
                    logger.info(
                        "Added NPC to room occupants display",
                        npc_name=npc.name,
                        npc_id=npc_id,
                        room_id=canonical_room_id,
                    )

        room_data_for_update = room.to_dict() if hasattr(room, "to_dict") else room
        if isinstance(room_data_for_update, dict):
            room_data_for_update = await connection_manager._convert_room_players_uuids_to_names(room_data_for_update)

        initial_state = build_event(
            "room_update",
            {"room": room_data_for_update, "entities": [], "occupants": occupant_names},
            player_id=player_id_str,
        )
        await websocket.send_json(initial_state)
        logger.debug(
            "Sent initial room state to connecting player", player_id=player_id_str, occupants_sent=occupant_names
        )

        event_handler = None
        if hasattr(connection_manager, "app") and connection_manager.app:
            event_handler = getattr(connection_manager.app.state, "event_handler", None)
        elif hasattr(websocket, "app") and websocket.app:
            event_handler = getattr(websocket.app.state, "event_handler", None)

        if event_handler and hasattr(event_handler, "_send_occupants_snapshot_to_player"):
            if room and room.has_player(player_id_str):
                await event_handler._send_occupants_snapshot_to_player(player_id, str(canonical_room_id))
                logger.debug(
                    "Sent room_occupants event to connecting player",
                    player_id=player_id_str,
                    room_id=str(canonical_room_id),
                )
    except Exception as e:
        logger.error("Error sending initial room state", player_id=player_id, error=str(e), exc_info=True)


async def _handle_websocket_message_loop(
    websocket: WebSocket, player_id: uuid.UUID, player_id_str: str, connection_manager
) -> None:
    """Handle the main WebSocket message loop."""
    from .message_validator import MessageValidationError, get_message_validator

    validator = get_message_validator()
    connection_id = connection_manager.get_connection_id_from_websocket(websocket)

    while True:
        try:
            data = await websocket.receive_text()

            if connection_id:
                if not connection_manager.rate_limiter.check_message_rate_limit(connection_id):
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
                    continue

            try:
                csrf_token = None
                message = validator.parse_and_validate(
                    data=data, player_id=player_id_str, schema=None, csrf_token=csrf_token
                )
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
                continue

            connection_manager.mark_player_seen(player_id)
            await handle_websocket_message(websocket, player_id_str, message)

        except json.JSONDecodeError:
            logger.warning("Invalid JSON from player", player_id=player_id)
            error_response = create_websocket_error_response(
                ErrorType.INVALID_FORMAT,
                "Invalid JSON format",
                ErrorMessages.INVALID_FORMAT,
                {"player_id": player_id_str},
            )
            await websocket.send_json(error_response)

        except WebSocketDisconnect:
            logger.info("WebSocket disconnected", player_id=player_id_str, connection_id=connection_id)
            break

        except RuntimeError as e:
            error_message = str(e)
            if "WebSocket is not connected" in error_message or 'Need to call "accept" first' in error_message:
                logger.warning(
                    "WebSocket connection lost (not connected)",
                    player_id=player_id_str,
                    connection_id=connection_id,
                    error=error_message,
                )
                break
            raise

        except Exception as e:
            logger.error(
                "Error handling WebSocket message",
                player_id=player_id_str,
                connection_id=connection_id,
                error=str(e),
                error_type=type(e).__name__,
                exc_info=True,
            )
            try:
                error_response = create_websocket_error_response(
                    ErrorType.INTERNAL_ERROR,
                    f"Internal server error: {str(e)}",
                    ErrorMessages.INTERNAL_ERROR,
                    {"player_id": player_id_str, "connection_id": connection_id, "error_type": type(e).__name__},
                )
                await websocket.send_json(error_response)
            except Exception as send_error:
                send_error_msg = str(send_error)
                if "WebSocket is not connected" in send_error_msg or "close message has been sent" in send_error_msg:
                    logger.warning(
                        "WebSocket closed, breaking message loop",
                        player_id=player_id_str,
                        connection_id=connection_id,
                        original_error=str(e),
                        send_error=send_error_msg,
                    )
                    break
                logger.error(
                    "Failed to send error response to client",
                    player_id=player_id_str,
                    connection_id=connection_id,
                    original_error=str(e),
                    send_error=send_error_msg,
                )


async def _cleanup_connection(player_id: uuid.UUID, player_id_str: str, connection_manager) -> None:
    """Clean up connection and player mute data on disconnect."""
    try:
        await connection_manager.disconnect_websocket(player_id)
    except Exception as e:
        logger.error("Error disconnecting WebSocket", player_id=player_id, error=str(e))

    try:
        from ..services.user_manager import user_manager

        user_manager.cleanup_player_mutes(player_id_str)
        logger.info("Cleaned up mute data", player_id=player_id)
    except Exception as e:
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
    if await _check_shutdown_and_reject(websocket, player_id):
        return

    success = await connection_manager.connect_websocket(websocket, player_id, session_id, token=token)
    if not success:
        logger.error("Failed to connect WebSocket", player_id=player_id)
        return

    player_id_str = str(player_id)
    _load_player_mute_data(player_id_str)

    try:
        canonical_room_id, should_exit = await _send_initial_game_state(
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
                    await _check_and_send_death_notification(
                        websocket, player_id, player_id_str, canonical_room_id, room, connection_manager
                    )
                    await _send_initial_room_state(
                        websocket, player_id, player_id_str, canonical_room_id, connection_manager
                    )
    except Exception as e:
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

    except Exception as e:
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

        logger.info(
            "🚨 SERVER DEBUG: handle_game_command called",
            command=command,
            args=args,
            player_id=player_id,
        )
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
        logger.info(
            "SERVER DEBUG: Sending command_response event for player",
            player_id=player_id,
            command=cmd,
            result=result,
        )
        await websocket.send_json(build_event("command_response", result, player_id=player_id))
        logger.info("SERVER DEBUG: command_response event sent successfully", player_id=player_id)

        # Handle broadcasting if the command result includes broadcast data
        if result.get("broadcast") and result.get("broadcast_type"):
            logger.debug("Broadcasting message to room", broadcast_type=result.get("broadcast_type"), player=player_id)
            player = await connection_manager._get_player(player_id)
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

    except Exception as e:
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
    logger.info("SERVER DEBUG: process_websocket_command called", cmd=cmd, args=args, player_id=player_id)
    logger.debug("Processing command", cmd=cmd, args=args, player_id=player_id)

    # Resolve connection_manager if not provided (backward compatibility)
    if connection_manager is None:
        from ..main import app

        connection_manager = app.state.container.connection_manager

    # Get player from connection manager
    logger.debug("Getting player for ID", player_id=player_id, player_id_type=type(player_id))
    player = await connection_manager._get_player(player_id)
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
    logger.info("SERVER DEBUG: Reconstructed command_line", command_line=command_line, cmd=cmd, args=args)
    result = await process_command_unified(
        command_line=command_line,
        current_user=player,
        # WebSocketRequestContext provides duck-typed Request interface but isn't a subclass
        # This is intentional - WebSocket contexts need different lifecycle than HTTP Requests
        request=request_context,  # type: ignore[arg-type]
        alias_storage=alias_storage,
        player_name=player_name,
    )
    assert isinstance(result, dict)
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
        player = await connection_manager._get_player(player_id)
        if player:
            await connection_manager.broadcast_to_room(
                str(player.current_room_id), chat_event, exclude_player=player_id
            )

        # Send confirmation to sender
        chat_sent_event = build_event("chat_sent", {"message": "Message sent"}, player_id=player_id)
        await websocket.send_json(chat_sent_event)

    except Exception as e:
        logger.error("Error handling chat message", player_id=player_id, error=str(e))
        error_response = create_websocket_error_response(
            ErrorType.MESSAGE_PROCESSING_ERROR,
            f"Error sending chat message: {str(e)}",
            ErrorMessages.MESSAGE_PROCESSING_ERROR,
            {"player_id": player_id},
        )
        await websocket.send_json(error_response)


async def broadcast_room_update(player_id: str, room_id: str, connection_manager=None) -> None:
    """
    Broadcast a room update to all players in the room.

    Args:
        player_id: The player who triggered the update
        room_id: The room's ID
        connection_manager: ConnectionManager instance (optional, will resolve from app.state if not provided)
    """
    logger.debug("broadcast_room_update called", player_id=player_id, room_id=room_id)
    try:
        # Resolve connection_manager if not provided (backward compatibility)
        if connection_manager is None:
            from ..main import app

            connection_manager = app.state.container.connection_manager

        # Get room data
        async_persistence = connection_manager.async_persistence
        if not async_persistence:
            logger.warning("Async persistence layer not available for room update")
            return

        from ..async_persistence import get_async_persistence

        async_persistence = get_async_persistence()
        room = async_persistence.get_room_by_id(room_id)
        if not room:
            logger.warning("Room not found for update", room_id=room_id)
            return

        logger.debug("DEBUG: broadcast_room_update - Room object ID", room_id=id(room))
        logger.debug("DEBUG: broadcast_room_update - Room players before any processing", players=room.get_players())

        # Get room occupants (players and NPCs)
        occupant_names = []

        # Get player occupants
        room_occupants = await connection_manager.get_room_occupants(room_id)
        try:
            for occ in room_occupants or []:
                name = occ.get("player_name") or occ.get("name")
                if name:
                    occupant_names.append(name)
        except Exception as e:
            logger.error("Error transforming room occupants", room_id=room_id, error=str(e))

        # CRITICAL FIX: Query NPCs from lifecycle manager instead of Room instance
        # Room instances are recreated from persistence and lose in-memory NPC tracking
        npc_ids: list[str] = []
        try:
            from ..services.npc_instance_service import get_npc_instance_service

            npc_instance_service = get_npc_instance_service()
            if npc_instance_service and hasattr(npc_instance_service, "lifecycle_manager"):
                lifecycle_manager = npc_instance_service.lifecycle_manager
                if lifecycle_manager and hasattr(lifecycle_manager, "active_npcs"):
                    active_npcs_dict = lifecycle_manager.active_npcs
                    # Query all active NPCs to find those in this room
                    # BUGFIX: Filter out dead NPCs (is_alive=False) to prevent showing dead NPCs in occupants
                    # As documented in investigation: 2025-11-30_session-001_npc-combat-start-failure.md
                    for npc_id, npc_instance in active_npcs_dict.items():
                        # Skip dead NPCs
                        if not getattr(npc_instance, "is_alive", True):
                            logger.debug(
                                "Skipping dead NPC from occupants",
                                npc_id=npc_id,
                                npc_name=getattr(npc_instance, "name", "unknown"),
                                room_id=room_id,
                            )
                            continue

                        # Check both current_room and current_room_id for compatibility
                        current_room = getattr(npc_instance, "current_room", None)
                        current_room_id = getattr(npc_instance, "current_room_id", None)
                        npc_room_id = current_room or current_room_id
                        if npc_room_id == room_id:
                            npc_ids.append(npc_id)

            logger.debug("DEBUG: Room has NPCs from lifecycle manager", room_id=room_id, npc_ids=npc_ids)
            for npc_id in npc_ids:
                # Get NPC name from the actual NPC instance, preserving original case from database
                npc_name = _get_npc_name_from_instance(npc_id)
                if npc_name:
                    logger.debug("DEBUG: Got NPC name from database", npc_name=npc_name, npc_id=npc_id)
                    occupant_names.append(npc_name)
                else:
                    # Log warning if NPC instance not found - this should not happen in normal operation
                    logger.warning("NPC instance not found for ID - skipping from room display", npc_id=npc_id)
        except Exception as npc_query_error:
            logger.warning(
                "Error querying NPCs from lifecycle manager, falling back to room.get_npcs()",
                room_id=room_id,
                error=str(npc_query_error),
            )
            # Fallback to room.get_npcs() if lifecycle manager query fails
            # BUGFIX: Filter fallback NPCs to only include alive NPCs from active_npcs
            # As documented in investigation: 2025-11-30_session-001_npc-combat-start-failure.md
            if async_persistence:
                room_npc_ids = room.get_npcs()
                logger.debug("DEBUG: Room has NPCs from fallback", room_id=room_id, npc_ids=room_npc_ids)

                # Filter fallback NPCs: only include those in active_npcs and alive
                filtered_npc_ids = []
                try:
                    from ..services.npc_instance_service import get_npc_instance_service

                    npc_instance_service = get_npc_instance_service()
                    if npc_instance_service and hasattr(npc_instance_service, "lifecycle_manager"):
                        lifecycle_manager = npc_instance_service.lifecycle_manager
                        if lifecycle_manager and hasattr(lifecycle_manager, "active_npcs"):
                            for npc_id in room_npc_ids:
                                if npc_id in lifecycle_manager.active_npcs:
                                    npc_instance = lifecycle_manager.active_npcs[npc_id]
                                    # Only include alive NPCs
                                    if getattr(npc_instance, "is_alive", True):
                                        filtered_npc_ids.append(npc_id)
                                    else:
                                        logger.debug(
                                            "Filtered dead NPC from fallback occupants",
                                            npc_id=npc_id,
                                            room_id=room_id,
                                        )
                except Exception as filter_error:
                    logger.warning(
                        "Error filtering fallback NPCs, using all room NPCs",
                        room_id=room_id,
                        error=str(filter_error),
                    )
                    filtered_npc_ids = room_npc_ids

                for npc_id in filtered_npc_ids:
                    npc_name = _get_npc_name_from_instance(npc_id)
                    if npc_name:
                        occupant_names.append(npc_name)

        # Create room update event
        room_data = room.to_dict() if hasattr(room, "to_dict") else room
        # CRITICAL: Convert player UUIDs to names - NEVER send UUIDs to client
        if isinstance(room_data, dict):
            room_data = await connection_manager._convert_room_players_uuids_to_names(room_data)

        # Debug: Log the room's actual occupants
        logger.debug("DEBUG: Room occupants breakdown", room_id=room_id)
        logger.debug("  - Room object ID", room_id=id(room))
        logger.debug("  - Players", players=room.get_players())
        logger.debug("  - Objects", objects=room.get_objects())
        logger.debug("  - NPCs", npcs=room.get_npcs())
        logger.debug("  - Total occupant_count", count=room.get_occupant_count())

        # Ensure all UUID objects are converted to strings for JSON serialization
        def convert_uuids_to_strings(obj: Any) -> Any:
            if isinstance(obj, dict):
                return {k: convert_uuids_to_strings(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [convert_uuids_to_strings(item) for item in obj]
            elif hasattr(obj, "__class__") and "UUID" in obj.__class__.__name__:
                return str(obj)
            else:
                return obj

        room_data = convert_uuids_to_strings(room_data)

        room_drops: list[dict[str, Any]] = []
        room_manager = getattr(connection_manager, "room_manager", None)
        if room_manager and hasattr(room_manager, "list_room_drops"):
            try:
                room_drops = clone_room_drops(room_manager.list_room_drops(room_id))
            except Exception as exc:  # pragma: no cover - defensive logging path
                logger.debug("Failed to collect room drops for broadcast", room_id=room_id, error=str(exc))

        drop_summary = build_room_drop_summary(room_drops)

        update_event = build_event(
            "room_update",
            {
                "room": room_data,
                "entities": [],
                "occupants": occupant_names,
                "occupant_count": len(occupant_names),
                "room_drops": room_drops,
                "drop_summary": drop_summary,
            },
            player_id=player_id,
            room_id=room_id,
        )

        logger.debug("Room update event created", update_event=update_event)

        # Update player's room subscription
        player = await connection_manager._get_player(player_id)
        if player:
            # Unsubscribe from old room
            if hasattr(player, "current_room_id") and player.current_room_id and player.current_room_id != room_id:
                await connection_manager.unsubscribe_from_room(player_id, str(player.current_room_id))
                logger.debug(
                    "Player unsubscribed from old room", player_id=player_id, old_room_id=player.current_room_id
                )

            # Subscribe to new room
            await connection_manager.subscribe_to_room(player_id, room_id)
            logger.debug("Player subscribed to new room", player_id=player_id, new_room_id=room_id)

            # Update player's current room
            player.current_room_id = room_id

        # Broadcast to room
        logger.debug("Broadcasting room update to room", room_id=room_id)
        await connection_manager.broadcast_to_room(room_id, update_event)
        logger.debug("Room update broadcast completed for room", room_id=room_id)

    except Exception as e:
        logger.error("Error broadcasting room update for room", room_id=room_id, error=str(e))


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

    except Exception as e:
        logger.error("Error sending system message", error=str(e))
