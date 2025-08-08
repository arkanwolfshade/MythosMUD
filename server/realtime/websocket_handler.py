"""
WebSocket handler for MythosMUD real-time communication.

This module handles WebSocket message processing, command handling,
and real-time updates for the game.
"""

import json

from fastapi import WebSocket, WebSocketDisconnect

from ..logging_config import get_logger
from .connection_manager import connection_manager

logger = get_logger(__name__)


async def handle_websocket_connection(websocket: WebSocket, player_id: str):
    """
    Handle a WebSocket connection for a player.

    Args:
        websocket: The WebSocket connection
        player_id: The player's ID
    """
    # Connect the WebSocket
    success = await connection_manager.connect_websocket(websocket, player_id)
    if not success:
        logger.error(f"Failed to connect WebSocket for player {player_id}")
        return

    try:
        # Send initial game state
        player = connection_manager._get_player(player_id)
        if player and hasattr(player, "current_room_id"):
            persistence = connection_manager.persistence
            if persistence:
                room = persistence.get_room(player.current_room_id)
                if room:
                    # Get room occupants
                    room_occupants = connection_manager.get_room_occupants(player.current_room_id)

                    game_state_event = {
                        "event_type": "game_state",
                        "timestamp": "2024-01-01T00:00:00Z",  # TODO: Use real timestamp
                        "sequence_number": 1,
                        "player_id": player_id,
                        "room_id": player.current_room_id,
                        "data": {
                            "player": {
                                "name": player.name,
                                "level": getattr(player, "level", 1),
                                "stats": getattr(player, "stats", {}),
                            },
                            "room": (room.to_dict() if hasattr(room, "to_dict") else room),
                            "occupants": room_occupants,
                            "occupant_count": len(room_occupants),
                        },
                    }
                    await websocket.send_json(game_state_event)

        # Send welcome message
        welcome_event = {
            "event_type": "welcome",
            "timestamp": "2024-01-01T00:00:00Z",  # TODO: Use real timestamp
            "sequence_number": 2,
            "player_id": player_id,
            "data": {"message": "Connected to MythosMUD"},
        }
        await websocket.send_json(welcome_event)

        # Main message loop
        while True:
            try:
                # Receive message from client
                data = await websocket.receive_text()
                message = json.loads(data)

                # Process the message
                await handle_websocket_message(websocket, player_id, message)

            except json.JSONDecodeError:
                logger.warning(f"Invalid JSON from player {player_id}")
                await websocket.send_json({"type": "error", "message": "Invalid JSON format"})

            except WebSocketDisconnect:
                logger.info(f"WebSocket disconnected for player {player_id}")
                break

            except Exception as e:
                logger.error(f"Error handling WebSocket message for {player_id}: {e}")
                await websocket.send_json({"type": "error", "message": "Internal server error"})

    finally:
        # Clean up connection
        await connection_manager.disconnect_websocket(player_id)


async def handle_websocket_message(websocket: WebSocket, player_id: str, message: dict):
    """
    Handle a WebSocket message from a player.

    Args:
        websocket: The WebSocket connection
        player_id: The player's ID
        message: The message data
    """
    try:
        message_type = message.get("type", "unknown")
        data = message.get("data", {})

        if message_type == "command":
            # Handle game command
            command = data.get("command", "")
            args = data.get("args", [])
            await handle_game_command(websocket, player_id, command, args)

        elif message_type == "chat":
            # Handle chat message
            chat_message = data.get("message", "")
            await handle_chat_message(websocket, player_id, chat_message)

        elif message_type == "ping":
            # Handle ping (keep-alive)
            await websocket.send_json({"type": "pong"})

        else:
            # Unknown message type
            logger.warning(f"Unknown message type '{message_type}' from player {player_id}")
            await websocket.send_json({"type": "error", "message": f"Unknown message type: {message_type}"})

    except Exception as e:
        logger.error(f"Error processing WebSocket message for {player_id}: {e}")
        await websocket.send_json({"type": "error", "message": "Error processing message"})


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
        # Parse command and arguments if args not provided
        if args is None:
            parts = command.strip().split()
            if not parts:
                await websocket.send_json({"type": "error", "message": "Empty command"})
                return

            cmd = parts[0].lower()
            args = parts[1:] if len(parts) > 1 else []
        else:
            cmd = command.lower()

        # Simple command processing for WebSocket
        result = await process_websocket_command(cmd, args, player_id)

        # Send the result back to the player
        response = {
            "event_type": "command_response",
            "timestamp": "2024-01-01T00:00:00Z",  # TODO: Use real timestamp
            "sequence_number": 3,
            "player_id": player_id,
            "data": result,
        }
        await websocket.send_json(response)

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
        await websocket.send_json(
            {
                "type": "error",
                "message": f"Error processing command: {str(e)}",
            }
        )


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
        room_id = player.current_room_id
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
        room_id = player.current_room_id
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
        from ..events import EventBus
        from ..game.movement_service import MovementService

        # Get the event bus from the app state or create a new one
        event_bus = getattr(connection_manager, "_event_bus", None)
        if not event_bus:
            event_bus = EventBus()

        movement_service = MovementService(event_bus)

        # Get the player's current room before moving
        from_room_id = player.current_room_id

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

    elif cmd == "say":
        message = " ".join(args).strip()
        if not message:
            return {"result": "You open your mouth, but no words come out"}
        return {"result": f"You say: {message}"}

    elif cmd == "help":
        if len(args) > 1:
            return {"result": "Too many arguments. Usage: help [command]"}
        command_name = args[0] if args else None
        return {"result": get_help_content(command_name)}

    else:
        return {"result": f"Unknown command: {cmd}"}


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
        chat_event = {
            "type": "chat",
            "player_id": player_id,
            "message": message,
            "timestamp": "2024-01-01T00:00:00Z",  # TODO: Use real timestamp
        }

        # Broadcast to room
        player = connection_manager._get_player(player_id)
        if player:
            await connection_manager.broadcast_to_room(player.current_room_id, chat_event, exclude_player=player_id)

        # Send confirmation to sender
        await websocket.send_json({"type": "chat_sent", "message": "Message sent"})

    except Exception as e:
        logger.error(f"Error handling chat message for {player_id}: {e}")
        await websocket.send_json({"type": "error", "message": "Error sending chat message"})


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

        # Create room update event
        update_event = {
            "event_type": "room_update",
            "timestamp": "2024-01-01T00:00:00Z",  # TODO: Use real timestamp
            "sequence_number": 4,
            "player_id": player_id,
            "room_id": room_id,
            "data": {
                "room": room.to_dict() if hasattr(room, "to_dict") else room,
                "entities": [],  # TODO: Add actual entities
            },
        }

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
        system_event = {
            "type": "system",
            "message": message,
            "message_type": message_type,
        }
        await websocket.send_json(system_event)

    except Exception as e:
        logger.error(f"Error sending system message: {e}")
