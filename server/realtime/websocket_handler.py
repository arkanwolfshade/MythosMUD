"""
WebSocket handler for MythosMUD real-time communication.

This module handles WebSocket message processing, command handling,
and real-time updates for the game.
"""

import json

from fastapi import WebSocket, WebSocketDisconnect

from ..error_types import ErrorMessages, ErrorType, create_websocket_error_response
from ..logging_config import get_logger
from .connection_manager import connection_manager
from .envelope import build_event

logger = get_logger(__name__)


async def handle_websocket_connection(websocket: WebSocket, player_id: str, session_id: str | None = None):
    """
    Handle a WebSocket connection for a player.

    Args:
        websocket: The WebSocket connection
        player_id: The player's ID
        session_id: Optional session ID for dual connection management
    """
    # Convert player_id to string to ensure JSON serialization compatibility
    player_id_str = str(player_id)

    # Connect the WebSocket with session tracking
    success = await connection_manager.connect_websocket(websocket, player_id_str, session_id)
    if not success:
        logger.error(f"Failed to connect WebSocket for player {player_id_str}")
        return

    # Load player mute data when they connect to the game
    try:
        from ..services.user_manager import user_manager

        user_manager.load_player_mutes(player_id_str)
        logger.info(f"Loaded mute data for player {player_id_str}")
    except Exception as e:
        logger.error(f"Error loading mute data for player {player_id_str}: {e}")

    try:
        # Send initial game state
        player = connection_manager._get_player(player_id_str)
        if player and hasattr(player, "current_room_id"):
            persistence = connection_manager.persistence
            if persistence:
                room = persistence.get_room(player.current_room_id)
                if room:
                    # Ensure player is added to their current room and track if we actually added them
                    logger.info(f"🔍 DEBUG: Room object ID before player_entered: {id(room)}")
                    if not room.has_player(player_id_str):
                        logger.info(f"Adding player {player_id_str} to room {player.current_room_id}")
                        room.player_entered(player_id_str)
                        logger.info(
                            f"🔍 DEBUG: After player_entered, room {player.current_room_id} has players: {room.get_players()}"
                        )
                        logger.info(f"🔍 DEBUG: Room object ID after player_entered: {id(room)}")
                    else:
                        logger.info(
                            f"🔍 DEBUG: Player {player_id_str} already in room {player.current_room_id}, players: {room.get_players()}"
                        )
                        logger.info(f"🔍 DEBUG: Room object ID (already in room): {id(room)}")

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
                        logger.error(f"Error transforming game_state occupants for room {player.current_room_id}: {e}")

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

                    game_state_event = build_event(
                        "game_state",
                        {
                            "player": {
                                "name": player.name,
                                "level": getattr(player, "level", 1),
                                "stats": stats_data,
                            },
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
                        logger.error(f"Error broadcasting initial room update for {player_id_str}: {e}")

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
                # Mark presence on any inbound message
                connection_manager.mark_player_seen(player_id_str)

                # Process the message
                await handle_websocket_message(websocket, player_id_str, message)

            except json.JSONDecodeError:
                logger.warning(f"Invalid JSON from player {player_id}")
                error_response = create_websocket_error_response(
                    ErrorType.INVALID_FORMAT,
                    "Invalid JSON format",
                    ErrorMessages.INVALID_FORMAT,
                    {"player_id": player_id_str},
                )
                await websocket.send_json(error_response)

            except WebSocketDisconnect:
                logger.info(f"WebSocket disconnected for player {player_id_str}")
                break

            except Exception as e:
                logger.error(f"Error handling WebSocket message for {player_id_str}: {e}")
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
            logger.info(f"Cleaned up mute data for player {player_id_str}")
        except Exception as e:
            logger.error(f"Error cleaning up mute data for player {player_id_str}: {e}")


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
        logger.error(f"Error processing WebSocket message for {player_id}: {e}")
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
        logger.info("🚨 SERVER DEBUG: handle_game_command called", command=command, args=args, player_id=player_id)
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
        logger.info(f"🚨 SERVER DEBUG: command_response event sent successfully for player {player_id}")

        # Handle broadcasting if the command result includes broadcast data
        if result.get("broadcast") and result.get("broadcast_type"):
            logger.debug(f"Broadcasting {result.get('broadcast_type')} message to room", player=player_id)
            player = connection_manager._get_player(player_id)
            if player and hasattr(player, "current_room_id"):
                room_id = player.current_room_id
                broadcast_event = build_event("command_response", {"result": result["broadcast"]}, player_id=player_id)
                await connection_manager.broadcast_to_room(room_id, broadcast_event, exclude_player=player_id)
                logger.debug(f"Broadcasted {result.get('broadcast_type')} message to room {room_id}")
            else:
                logger.warning(f"Player not found or missing current_room_id for broadcast: {player_id}")

        # Broadcast room updates if the command affected the room
        logger.debug(f"Command result: {result}")
        if result.get("room_changed"):
            logger.debug(f"Room changed detected, broadcasting update for room: {result.get('room_id')}")
            await broadcast_room_update(player_id, result.get("room_id"))
        elif cmd == "go" and result.get("result"):
            # Send room update after movement
            logger.debug(f"Go command detected, broadcasting update for player: {player_id}")
            player = connection_manager._get_player(player_id)
            if player and hasattr(player, "current_room_id"):
                logger.debug(f"Broadcasting room update for room: {player.current_room_id}")
                await broadcast_room_update(player_id, player.current_room_id)
            else:
                logger.warning(f"Player not found or missing current_room_id for: {player_id}")

    except Exception as e:
        logger.error(f"Error processing command '{command}' for {player_id}: {e}")
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
    logger.info("🚨 SERVER DEBUG: process_websocket_command called", command=cmd, args=args, player_id=player_id)
    logger.debug(f"Processing command: {cmd} with args: {args} for player: {player_id}")

    # Get player from connection manager
    logger.debug(f"Getting player for ID: {player_id} (type: {type(player_id)})")
    player = connection_manager._get_player(player_id)
    logger.debug(f"Player object: {player} (type: {type(player)})")
    if not player:
        logger.warning(f"Player not found: {player_id}")
        return {"result": "Player not found"}

    # Check if player is actually a Player object
    if not hasattr(player, "current_room_id"):
        logger.error(f"Player object is not a Player instance: {type(player)}")
        return {"result": "Player data error"}

    # Get persistence from connection manager
    persistence = connection_manager.persistence
    if not persistence:
        logger.warning("Persistence layer not available")
        return {"result": "Game system unavailable"}

    # Handle basic commands
    if cmd == "look":
        # Prefer the connection manager's tracked room (real-time canonical)
        room_id = getattr(player, "current_room_id", None)
        room = persistence.get_room(room_id)
        if not room:
            return {"result": "You see nothing special."}

        if args:
            direction = args[0].lower()
            exits = room.exits if hasattr(room, "exits") else {}
            target_room_id = exits.get(direction)
            if target_room_id:
                target_room = persistence.get_room(target_room_id)
                if target_room:
                    name = getattr(target_room, "name", "")
                    desc = getattr(target_room, "description", "You see nothing special.")
                    return {"result": f"{name}\n{desc}"}
            return {"result": "You see nothing special that way."}

        name = getattr(room, "name", "")
        desc = getattr(room, "description", "You see nothing special.")
        exits = room.exits if hasattr(room, "exits") else {}
        valid_exits = [direction for direction, room_id in exits.items() if room_id is not None]
        exit_list = ", ".join(valid_exits) if valid_exits else "none"
        return {"result": f"{name}\n{desc}\n\nExits: {exit_list}"}

    elif cmd == "go":
        logger.debug(f"Processing go command with args: {args}")
        if not args:
            logger.warning("Go command called without arguments")
            return {"result": "Go where? Usage: go <direction>"}

        direction = args[0].lower()
        logger.debug(f"Direction: {direction}")
        # Use the connection manager's view of the player's current room
        room_id = getattr(player, "current_room_id", None)
        logger.debug(f"Current room ID: {room_id}")
        room = persistence.get_room(room_id)
        if not room:
            logger.warning(f"Room not found: {room_id}")
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
            logger.error(f"No EventBus available for player {player_id} movement")
            return {"result": "Game system temporarily unavailable"}

        # Create MovementService with the same persistence layer as the connection manager
        movement_service = MovementService(event_bus)
        # Override the persistence layer to use the same instance as the connection manager
        if connection_manager.persistence:
            movement_service._persistence = connection_manager.persistence
            logger.debug("Overriding MovementService persistence with connection manager persistence")
            logger.debug(f"MovementService persistence ID: {id(movement_service._persistence)}")
            logger.debug(f"Connection manager persistence ID: {id(connection_manager.persistence)}")
        else:
            logger.error("Connection manager persistence is None!")

        # Get the player's current room before moving
        from_room_id = player.current_room_id

        # Debug: Check if the player is in the room according to both persistence layers
        from_room = connection_manager.persistence.get_room(from_room_id) if connection_manager.persistence else None
        if from_room:
            has_player = from_room.has_player(player_id)
            logger.debug(f"Player {player_id} in room {from_room_id}: {has_player}")
            logger.debug(f"Room {from_room_id} players: {list(from_room.get_players())}")
        else:
            logger.error(f"Could not get room {from_room_id} from connection manager persistence")

        logger.debug(f"Moving player {player_id} from {from_room_id} to {target_room_id}")

        # Move the player using the movement service
        success = movement_service.move_player(player_id, from_room_id, target_room_id)

        logger.debug(f"Movement result: {success}")

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

    # Create alias storage
    alias_storage = AliasStorage()
    request_context.set_alias_storage(alias_storage)

    # Verify app state services are available (they should already be in the real app state)
    player_service = getattr(app_state, "player_service", None)
    user_manager = getattr(app_state, "user_manager", None)
    logger.debug(f"App state services available - player_service: {player_service}, user_manager: {user_manager}")

    if not player_service or not user_manager:
        logger.warning("Missing required app state services - player_service or user_manager not available")

    # Process the command using the unified command handler
    result = await process_command_unified(
        command_line=f"{cmd} {' '.join(args)}".strip(),
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
        logger.error(f"Error handling chat message for {player_id}: {e}")
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
    logger.debug(f"broadcast_room_update called with player_id: {player_id}, room_id: {room_id}")
    try:
        # Get room data
        persistence = connection_manager.persistence
        if not persistence:
            logger.warning("Persistence layer not available for room update")
            return

        room = persistence.get_room(room_id)
        if not room:
            logger.warning(f"Room not found for update: {room_id}")
            return

        logger.debug(f"🔍 DEBUG: broadcast_room_update - Room object ID: {id(room)}")
        logger.debug(f"🔍 DEBUG: broadcast_room_update - Room players before any processing: {room.get_players()}")

        # Get room occupants (server-side structs)
        room_occupants = connection_manager.get_room_occupants(room_id)

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
            logger.error(f"Error transforming room occupants for room {room_id}: {e}")

        # Create room update event
        room_data = room.to_dict() if hasattr(room, "to_dict") else room

        # Debug: Log the room's actual occupants
        logger.debug(f"🔍 DEBUG: Room {room_id} occupants breakdown:")
        logger.debug(f"  - Room object ID: {id(room)}")
        logger.debug(f"  - Players: {room.get_players()}")
        logger.debug(f"  - Objects: {room.get_objects()}")
        logger.debug(f"  - NPCs: {room.get_npcs()}")
        logger.debug(f"  - Total occupant_count: {room.get_occupant_count()}")

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

        logger.debug(f"Room update event created: {update_event}")

        # Update player's room subscription
        player = connection_manager._get_player(player_id)
        if player:
            # Unsubscribe from old room
            if hasattr(player, "current_room_id") and player.current_room_id and player.current_room_id != room_id:
                await connection_manager.unsubscribe_from_room(player_id, player.current_room_id)
                logger.debug(f"Player {player_id} unsubscribed from old room {player.current_room_id}")

            # Subscribe to new room
            await connection_manager.subscribe_to_room(player_id, room_id)
            logger.debug(f"Player {player_id} subscribed to new room {room_id}")

            # Update player's current room
            player.current_room_id = room_id

        # Broadcast to room
        logger.debug(f"Broadcasting room update to room: {room_id}")
        await connection_manager.broadcast_to_room(room_id, update_event)
        logger.debug(f"Room update broadcast completed for room: {room_id}")

    except Exception as e:
        logger.error(f"Error broadcasting room update for room {room_id}: {e}")


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
        logger.error(f"Error sending system message: {e}")
