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
        # Send welcome message
        welcome_event = {
            "type": "welcome",
            "player_id": player_id,
            "message": "Connected to MythosMUD",
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
        connection_manager.disconnect_websocket(player_id)


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
            await handle_game_command(websocket, player_id, command)

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


async def handle_game_command(websocket: WebSocket, player_id: str, command: str):
    """
    Handle a game command from a player.

    Args:
        websocket: The WebSocket connection
        player_id: The player's ID
        command: The command string
    """
    try:
        # Parse command and arguments
        parts = command.strip().split()
        if not parts:
            await websocket.send_json({"type": "error", "message": "Empty command"})
            return

        cmd = parts[0].lower()
        args = parts[1:] if len(parts) > 1 else []

        # Simple command processing for WebSocket
        result = await process_websocket_command(cmd, args, player_id)

        # Send the result back to the player
        response = {
            "event_type": "command_response",
            "data": result,
        }
        await websocket.send_json(response)

        # Broadcast room updates if the command affected the room
        if result.get("room_changed"):
            await broadcast_room_update(player_id, result.get("room_id"))

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
    # Get player from connection manager
    player = connection_manager._get_player(player_id)
    if not player:
        return {"result": "Player not found"}

    # Get persistence from connection manager
    persistence = connection_manager.persistence
    if not persistence:
        return {"result": "Game system unavailable"}

    # Handle basic commands
    if cmd == "look":
        room_id = player.current_room_id
        room = persistence.get_room(room_id)
        if not room:
            return {"result": "You see nothing special."}

        if args:
            direction = args[0].lower()
            exits = room.get("exits", {})
            target_room_id = exits.get(direction)
            if target_room_id:
                target_room = persistence.get_room(target_room_id)
                if target_room:
                    name = target_room.get("name", "")
                    desc = target_room.get("description", "You see nothing special.")
                    return {"result": f"{name}\n{desc}"}
            return {"result": "You see nothing special that way."}

        name = room.get("name", "")
        desc = room.get("description", "You see nothing special.")
        exits = room.get("exits", {})
        valid_exits = [direction for direction, room_id in exits.items() if room_id is not None]
        exit_list = ", ".join(valid_exits) if valid_exits else "none"
        return {"result": f"{name}\n{desc}\n\nExits: {exit_list}"}

    elif cmd == "go":
        if not args:
            return {"result": "Go where? Usage: go <direction>"}

        direction = args[0].lower()
        room_id = player.current_room_id
        room = persistence.get_room(room_id)
        if not room:
            return {"result": "You can't go that way"}

        exits = room.get("exits", {})
        target_room_id = exits.get(direction)
        if not target_room_id:
            return {"result": "You can't go that way"}

        target_room = persistence.get_room(target_room_id)
        if not target_room:
            return {"result": "You can't go that way"}

        # Move the player
        player.current_room_id = target_room_id
        persistence.save_player(player)

        name = target_room.get("name", "")
        desc = target_room.get("description", "You see nothing special.")
        exits = target_room.get("exits", {})
        valid_exits = [direction for direction, room_id in exits.items() if room_id is not None]
        exit_list = ", ".join(valid_exits) if valid_exits else "none"
        return {"result": f"{name}\n{desc}\n\nExits: {exit_list}"}

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
    try:
        # Create room update event
        update_event = {
            "type": "room_update",
            "room_id": room_id,
            "triggered_by": player_id,
            "timestamp": "2024-01-01T00:00:00Z",  # TODO: Use real timestamp
        }

        # Broadcast to room
        await connection_manager.broadcast_to_room(room_id, update_event)

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
