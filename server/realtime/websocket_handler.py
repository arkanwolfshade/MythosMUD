"""
WebSocket handler for MythosMUD real-time communication.

This module handles WebSocket message processing, command handling,
and real-time updates for the game.
"""

import json

from fastapi import WebSocket, WebSocketDisconnect

from ..error_types import ErrorMessages, ErrorType, create_websocket_error_response
from ..logging.enhanced_logging_config import get_logger
from .connection_manager import connection_manager
from .envelope import build_event

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
        if hasattr(npc_instance_service, "spawning_service"):
            spawning_service = npc_instance_service.spawning_service
            if npc_id in spawning_service.active_npc_instances:
                npc_instance = spawning_service.active_npc_instances[npc_id]
                name = getattr(npc_instance, "name", None)
                return name

        return None
    except Exception as e:
        logger.debug("Error getting NPC name from instance", npc_id=npc_id, error=str(e))
        return None


async def handle_websocket_connection(websocket: WebSocket, player_id: str, session_id: str | None = None):
    """
    Handle a WebSocket connection for a player.

    Args:
        websocket: The WebSocket connection
        player_id: The player's ID
        session_id: Optional session ID for dual connection management
    """
    # Check if server is shutting down - prevent new connections
    # Import here to avoid circular imports
    from ..commands.admin_shutdown_command import get_shutdown_blocking_message, is_shutdown_pending

    # Try to get app from websocket state (may not always be available)
    try:
        if hasattr(websocket, "app") and is_shutdown_pending(websocket.app):
            error_message = get_shutdown_blocking_message("motd_progression")
            await websocket.send_json({"type": "error", "message": error_message})
            logger.info("DEBUG: Closing WebSocket due to server shutdown", player_id=player_id)
            await websocket.close(code=1001, reason="Server shutting down")
            logger.info("Rejected WebSocket connection - server shutting down", player_id=player_id)
            return
    except Exception as e:
        logger.debug("Could not check shutdown status in WebSocket connection", error=str(e))

    # Convert player_id to string to ensure JSON serialization compatibility
    player_id_str = str(player_id)

    # Connect the WebSocket with session tracking
    success = await connection_manager.connect_websocket(websocket, player_id_str, session_id)
    if not success:
        logger.error("Failed to connect WebSocket", player_id=player_id_str)
        return

    # Load player mute data when they connect to the game
    try:
        from ..services.user_manager import user_manager

        user_manager.load_player_mutes(player_id_str)
        logger.info("Loaded mute data", player_id=player_id_str)
    except Exception as e:
        logger.error("Error loading mute data", player_id=player_id_str, error=str(e))

    try:
        # Send initial game state
        player = connection_manager._get_player(player_id_str)
        if player and hasattr(player, "current_room_id"):
            persistence = connection_manager.persistence
            if persistence:
                room = persistence.get_room(player.current_room_id)
                if room:
                    # Ensure player is added to their current room and track if we actually added them
                    logger.info("DEBUG: Room object ID before player_entered", room_id=id(room))
                    if not room.has_player(player_id_str):
                        logger.info("Adding player to room", player_id=player_id_str, room_id=player.current_room_id)
                        room.player_entered(player_id_str)
                        logger.info(
                            f"DEBUG: After player_entered, room {player.current_room_id} has players: {room.get_players()}"
                        )
                        logger.info("DEBUG: Room object ID after player_entered", room_id=id(room))
                    else:
                        logger.info(
                            f"DEBUG: Player {player_id_str} already in room {player.current_room_id}, players: {room.get_players()}"
                        )
                        logger.info("DEBUG: Room object ID (already in room)", room_id=id(room))

                    # Use canonical room id for subscriptions and broadcasts
                    canonical_room_id = getattr(room, "id", None) or player.current_room_id

                    # Get room occupants
                    room_occupants = connection_manager.get_room_occupants(canonical_room_id)

                    # Transform to list of player names for client (UI expects string[])
                    occupant_names = []
                    try:
                        for occ in room_occupants or []:
                            if isinstance(occ, dict):
                                name = occ.get("player_name") or occ.get("name")
                                if name:
                                    occupant_names.append(name)
                            elif isinstance(occ, str):
                                occupant_names.append(occ)
                    except Exception as e:
                        logger.error(
                            "Error transforming game_state occupants", room_id=player.current_room_id, error=str(e)
                        )

                    # Get room data and ensure UUIDs are converted to strings
                    room_data = room.to_dict() if hasattr(room, "to_dict") else room

                    # Ensure all UUID objects are converted to strings for JSON serialization
                    def convert_uuids_to_strings(obj):
                        if isinstance(obj, dict):
                            return {k: convert_uuids_to_strings(v) for k, v in obj.items()}
                        elif isinstance(obj, list):
                            return [convert_uuids_to_strings(item) for item in obj]
                        elif hasattr(obj, "__class__") and "UUID" in obj.__class__.__name__:
                            return str(obj)
                        else:
                            return obj

                    room_data = convert_uuids_to_strings(room_data)

                    # Prepare player stats as a JSON object (not raw string)
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
                    except Exception:
                        stats_data = {}

                    # Normalize health field for client (current_health expected)
                    if "current_health" not in stats_data and "health" in stats_data:
                        try:
                            stats_data["current_health"] = stats_data.get("health")
                        except Exception:
                            pass

                    # Get complete player data with profession information using PlayerService
                    # This ensures the Status panel displays profession info automatically
                    try:
                        # Access app state through connection manager (same pattern as process_websocket_command)
                        app_state = connection_manager.app.state if connection_manager.app else None
                        player_service = getattr(app_state, "player_service", None) if app_state else None

                        if player_service:
                            # Use PlayerService to get complete player data with profession
                            complete_player_data = await player_service._convert_player_to_schema(player)
                            logger.debug(
                                "WebSocket handler: Retrieved complete player data with profession",
                                player_id=player_id_str,
                                has_profession=bool(getattr(complete_player_data, "profession_name", None)),
                            )

                            # Convert PlayerRead object to dictionary for JSON serialization
                            player_data_for_client = (
                                complete_player_data.model_dump(mode="json")
                                if hasattr(complete_player_data, "model_dump")
                                else complete_player_data.dict()
                            )
                            # Map experience_points to xp for client compatibility
                            if "experience_points" in player_data_for_client:
                                player_data_for_client["xp"] = player_data_for_client["experience_points"]
                        else:
                            # Fallback to basic player data if PlayerService not available
                            logger.warning(
                                "PlayerService not available in websocket handler, using basic player data",
                                player_id=player_id_str,
                            )
                            player_data_for_client = {
                                "name": player.name,
                                "level": getattr(player, "level", 1),
                                "xp": getattr(player, "experience_points", 0),
                                "stats": stats_data,
                            }
                    except Exception as e:
                        logger.error("Error getting complete player data", error=str(e), player_id=player_id_str)
                        # Fallback to basic player data
                        player_data_for_client = {
                            "name": player.name,
                            "level": getattr(player, "level", 1),
                            "xp": getattr(player, "experience_points", 0),
                            "stats": stats_data,
                        }

                    game_state_event = build_event(
                        "game_state",
                        {
                            "player": player_data_for_client,
                            "room": room_data,
                            "occupants": occupant_names,
                            "occupant_count": len(occupant_names),
                        },
                        player_id=player_id_str,
                        room_id=canonical_room_id,
                    )
                    await websocket.send_json(game_state_event)

                    # Proactively broadcast a room update so existing occupants see the new player
                    try:
                        await broadcast_room_update(player_id_str, canonical_room_id)
                    except Exception as e:
                        logger.error("Error broadcasting initial room update", player_id=player_id_str, error=str(e))

                    # Note: Removed synthetic player_entered event generation to prevent duplicates
                    # The natural PlayerEnteredRoom event from Room.player_entered() will handle
                    # the notification to other players when a player is added to the room

        # Send welcome message
        welcome_event = build_event(
            "welcome",
            {"message": "Connected to MythosMUD"},
            player_id=player_id_str,
        )
        await websocket.send_json(welcome_event)

        # Main message loop
        while True:
            try:
                # Receive message from client
                data = await websocket.receive_text()
                message = json.loads(data)

                # CRITICAL FIX: Handle wrapped message format from useWebSocketConnection
                # The client wraps messages in {message, csrfToken, timestamp} structure
                if "message" in message and isinstance(message["message"], str):
                    try:
                        # Unwrap the inner message
                        inner_message = json.loads(message["message"])
                        # Verify CSRF token if present
                        # TODO: Implement CSRF validation
                        message = inner_message
                    except json.JSONDecodeError:
                        # If inner message is not JSON, use it as-is
                        pass

                # Mark presence on any inbound message
                connection_manager.mark_player_seen(player_id_str)

                # Process the message
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
                logger.info("WebSocket disconnected", player_id=player_id_str)
                break

            except Exception as e:
                logger.error("Error handling WebSocket message", player_id=player_id_str, error=str(e))
                error_response = create_websocket_error_response(
                    ErrorType.INTERNAL_ERROR,
                    f"Internal server error: {str(e)}",
                    ErrorMessages.INTERNAL_ERROR,
                    {"player_id": player_id_str},
                )
                await websocket.send_json(error_response)

    finally:
        # Clean up connection
        await connection_manager.disconnect_websocket(player_id_str)

        # Clean up player mute data when they disconnect
        try:
            from ..services.user_manager import user_manager

            user_manager.cleanup_player_mutes(player_id_str)
            logger.info("Cleaned up mute data", player_id=player_id_str)
        except Exception as e:
            logger.error("Error cleaning up mute data", player_id=player_id_str, error=str(e))


async def handle_websocket_message(websocket: WebSocket, player_id: str, message: dict):
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


async def handle_game_command(websocket: WebSocket, player_id: str, command: str, args: list = None):
    """
    Handle a game command from a player.

    Args:
        websocket: The WebSocket connection
        player_id: The player's ID
        command: The command string
        args: Command arguments (optional, will parse from command if not provided)
    """
    try:
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
        result = await process_websocket_command(cmd, args, player_id)

        # Send the result back to the player
        logger.info(
            f"🚨 SERVER DEBUG: Sending command_response event for player {player_id}",
            {"command": cmd, "result": result, "player_id": player_id},
        )
        await websocket.send_json(build_event("command_response", result, player_id=player_id))
        logger.info("SERVER DEBUG: command_response event sent successfully", player_id=player_id)

        # Handle broadcasting if the command result includes broadcast data
        if result.get("broadcast") and result.get("broadcast_type"):
            logger.debug("Broadcasting message to room", broadcast_type=result.get("broadcast_type"), player=player_id)
            player = connection_manager._get_player(player_id)
            if player and hasattr(player, "current_room_id"):
                room_id = player.current_room_id
                broadcast_event = build_event("command_response", {"result": result["broadcast"]}, player_id=player_id)
                await connection_manager.broadcast_to_room(room_id, broadcast_event, exclude_player=player_id)
                logger.debug(
                    "Broadcasted message to room", broadcast_type=result.get("broadcast_type"), room_id=room_id
                )
            else:
                logger.warning("Player not found or missing current_room_id for broadcast", player_id=player_id)

        # Broadcast room updates if the command affected the room
        logger.debug("Command result", result=result)
        if result.get("room_changed"):
            logger.debug("Room changed detected, broadcasting update", room_id=result.get("room_id"))
            await broadcast_room_update(player_id, result.get("room_id"))
        elif cmd == "go" and result.get("result"):
            # Send room update after movement
            logger.debug("Go command detected, broadcasting update", player_id=player_id)
            player = connection_manager._get_player(player_id)
            if player and hasattr(player, "current_room_id"):
                logger.debug("Broadcasting room update", room_id=player.current_room_id)
                await broadcast_room_update(player_id, player.current_room_id)
            else:
                logger.warning("Player not found or missing current_room_id", player_id=player_id)

    except Exception as e:
        logger.error("Error processing command", command=command, player_id=player_id, error=str(e))
        error_response = create_websocket_error_response(
            ErrorType.MESSAGE_PROCESSING_ERROR,
            f"Error processing command: {str(e)}",
            ErrorMessages.MESSAGE_PROCESSING_ERROR,
            {"player_id": player_id, "command": command},
        )
        await websocket.send_json(error_response)


async def process_websocket_command(cmd: str, args: list, player_id: str) -> dict:
    """
    Process a command for WebSocket connections.

    Args:
        cmd: The command name
        args: Command arguments
        player_id: The player's ID

    Returns:
        dict: Command result
    """
    logger.info("SERVER DEBUG: process_websocket_command called", cmd=cmd, args=args, player_id=player_id)
    logger.debug("Processing command", cmd=cmd, args=args, player_id=player_id)

    # Get player from connection manager
    logger.debug("Getting player for ID", player_id=player_id, player_id_type=type(player_id))
    player = connection_manager._get_player(player_id)
    logger.debug("Player object", player=player, player_type=type(player))
    if not player:
        logger.warning("Player not found", player_id=player_id)
        return {"result": "Player not found"}

    # Check if player is actually a Player object
    if not hasattr(player, "current_room_id"):
        logger.error("Player object is not a Player instance", player_type=type(player))
        return {"result": "Player data error"}

    # Get persistence from connection manager
    persistence = connection_manager.persistence
    if not persistence:
        logger.warning("Persistence layer not available")
        return {"result": "Game system unavailable"}

    # Handle basic commands - use unified command handler for look to support targets
    if cmd == "look":
        # Use the unified command handler for look commands to support targets
        pass  # Fall through to unified command handler

    elif cmd == "go":
        logger.debug("Processing go command", args=args)
        if not args:
            logger.warning("Go command called without arguments")
            return {"result": "Go where? Usage: go <direction>"}

        direction = args[0].lower()
        logger.debug("Direction", direction=direction)
        # Use the connection manager's view of the player's current room
        room_id = getattr(player, "current_room_id", None)
        logger.debug("Current room ID", room_id=room_id)
        room = persistence.get_room(room_id)
        if not room:
            logger.warning("Room not found", room_id=room_id)
            return {"result": "You can't go that way"}

        exits = room.exits if hasattr(room, "exits") else {}
        target_room_id = exits.get(direction)
        if not target_room_id:
            return {"result": "You can't go that way"}

        target_room = persistence.get_room(target_room_id)
        if not target_room:
            return {"result": "You can't go that way"}

        # Use MovementService to move the player (this will trigger events)
        from ..game.movement_service import MovementService

        # Get the event bus from the connection manager (should be set during app startup)
        event_bus = getattr(connection_manager, "_event_bus", None)
        if not event_bus:
            logger.error("No EventBus available for player movement", player_id=player_id)
            return {"result": "Game system temporarily unavailable"}

        # Create MovementService with the same persistence layer as the connection manager
        movement_service = MovementService(event_bus)
        # Override the persistence layer to use the same instance as the connection manager
        if connection_manager.persistence:
            movement_service._persistence = connection_manager.persistence
            logger.debug("Overriding MovementService persistence with connection manager persistence")
            logger.debug("MovementService persistence ID", persistence_id=id(movement_service._persistence))
            logger.debug("Connection manager persistence ID", persistence_id=id(connection_manager.persistence))
        else:
            logger.error("Connection manager persistence is None!")

        # Get the player's current room before moving
        from_room_id = player.current_room_id

        # Debug: Check if the player is in the room according to both persistence layers
        from_room = connection_manager.persistence.get_room(from_room_id) if connection_manager.persistence else None
        if from_room:
            has_player = from_room.has_player(player_id)
            logger.debug("Player in room", player_id=player_id, room_id=from_room_id, has_player=has_player)
            logger.debug("Room players", room_id=from_room_id, players=list(from_room.get_players()))
        else:
            logger.error("Could not get room from connection manager persistence", room_id=from_room_id)

        logger.debug("Moving player", player_id=player_id, from_room_id=from_room_id, to_room_id=target_room_id)

        # Move the player using the movement service
        success = movement_service.move_player(player_id, from_room_id, target_room_id)

        logger.debug("Movement result", success=success)

        if not success:
            return {"result": "You can't go that way"}

        # Get updated room info
        updated_room = persistence.get_room(target_room_id)
        name = getattr(updated_room, "name", "")
        desc = getattr(updated_room, "description", "You see nothing special.")
        exits = updated_room.exits if hasattr(updated_room, "exits") else {}
        valid_exits = [direction for direction, room_id in exits.items() if room_id is not None]
        exit_list = ", ".join(valid_exits) if valid_exits else "none"
        return {"result": f"{name}\n{desc}\n\nExits: {exit_list}", "room_changed": True, "room_id": target_room_id}

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
        request=request_context,
        alias_storage=alias_storage,
        player_name=player_name,
    )
    return result


def get_help_content(command_name: str = None) -> str:
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


async def handle_chat_message(websocket: WebSocket, player_id: str, message: str):
    """
    Handle a chat message from a player.

    Args:
        websocket: The WebSocket connection
        player_id: The player's ID
        message: The chat message
    """
    try:
        # Create chat event
        chat_event = build_event(
            "chat",
            {"player_id": player_id, "message": message},
            player_id=player_id,
        )

        # Broadcast to room
        player = connection_manager._get_player(player_id)
        if player:
            await connection_manager.broadcast_to_room(player.current_room_id, chat_event, exclude_player=player_id)

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


async def broadcast_room_update(player_id: str, room_id: str):
    """
    Broadcast a room update to all players in the room.

    Args:
        player_id: The player who triggered the update
        room_id: The room's ID
    """
    logger.debug("broadcast_room_update called", player_id=player_id, room_id=room_id)
    try:
        # Get room data
        persistence = connection_manager.persistence
        if not persistence:
            logger.warning("Persistence layer not available for room update")
            return

        room = persistence.get_room(room_id)
        if not room:
            logger.warning("Room not found for update", room_id=room_id)
            return

        logger.debug("DEBUG: broadcast_room_update - Room object ID", room_id=id(room))
        logger.debug("DEBUG: broadcast_room_update - Room players before any processing", players=room.get_players())

        # Get room occupants (players and NPCs)
        occupant_names = []

        # Get player occupants
        room_occupants = connection_manager.get_room_occupants(room_id)
        try:
            for occ in room_occupants or []:
                if isinstance(occ, dict):
                    name = occ.get("player_name") or occ.get("name")
                    if name:
                        occupant_names.append(name)
                elif isinstance(occ, str):
                    occupant_names.append(occ)
        except Exception as e:
            logger.error("Error transforming room occupants", room_id=room_id, error=str(e))

        # Get NPC occupants
        if persistence:
            npc_ids = room.get_npcs()
            logger.debug("DEBUG: Room has NPCs", room_id=room_id, npc_ids=npc_ids)
            for npc_id in npc_ids:
                # Get NPC name from the actual NPC instance, preserving original case from database
                npc_name = _get_npc_name_from_instance(npc_id)
                if npc_name:
                    logger.debug("DEBUG: Got NPC name from database", npc_name=npc_name, npc_id=npc_id)
                    occupant_names.append(npc_name)
                else:
                    # Log warning if NPC instance not found - this should not happen in normal operation
                    logger.warning("NPC instance not found for ID - skipping from room display", npc_id=npc_id)

        # Create room update event
        room_data = room.to_dict() if hasattr(room, "to_dict") else room

        # Debug: Log the room's actual occupants
        logger.debug("DEBUG: Room occupants breakdown", room_id=room_id)
        logger.debug("  - Room object ID", room_id=id(room))
        logger.debug("  - Players", players=room.get_players())
        logger.debug("  - Objects", objects=room.get_objects())
        logger.debug("  - NPCs", npcs=room.get_npcs())
        logger.debug("  - Total occupant_count", count=room.get_occupant_count())

        # Ensure all UUID objects are converted to strings for JSON serialization
        def convert_uuids_to_strings(obj):
            if isinstance(obj, dict):
                return {k: convert_uuids_to_strings(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [convert_uuids_to_strings(item) for item in obj]
            elif hasattr(obj, "__class__") and "UUID" in obj.__class__.__name__:
                return str(obj)
            else:
                return obj

        room_data = convert_uuids_to_strings(room_data)

        update_event = build_event(
            "room_update",
            {
                "room": room_data,
                "entities": [],
                "occupants": occupant_names,
                "occupant_count": len(occupant_names),
            },
            player_id=player_id,
            room_id=room_id,
        )

        logger.debug("Room update event created", update_event=update_event)

        # Update player's room subscription
        player = connection_manager._get_player(player_id)
        if player:
            # Unsubscribe from old room
            if hasattr(player, "current_room_id") and player.current_room_id and player.current_room_id != room_id:
                await connection_manager.unsubscribe_from_room(player_id, player.current_room_id)
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


async def send_system_message(websocket: WebSocket, message: str, message_type: str = "info"):
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
