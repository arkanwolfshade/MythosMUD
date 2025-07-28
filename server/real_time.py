"""
Real-time communication module for MythosMUD.

Handles Server-Sent Events (SSE) for game state updates and WebSockets for
interactive commands.
"""

import asyncio
import json
import logging
import os
import time
import uuid
from datetime import UTC, datetime
from typing import Any

from fastapi import WebSocket, WebSocketDisconnect
from pydantic import BaseModel, Field

from config_loader import get_config
from models import Player

logger = logging.getLogger(__name__)


def load_motd() -> str:
    """
    Load the Message of the Day from the configured file.

    Returns:
        str: The MOTD content, or a default message if file cannot be loaded
    """
    try:
        config = get_config()
        motd_file = config.get("motd_file", "./data/motd.txt")

        # Resolve relative path from server directory to project root
        server_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(server_dir)
        motd_path = os.path.join(project_root, motd_file.replace("./", ""))

        if os.path.exists(motd_path):
            with open(motd_path, encoding='utf-8') as f:
                return f.read().strip()
        else:
            logger.warning(f"MOTD file not found: {motd_path}")
            return ("Welcome to MythosMUD - Enter the realm of "
                    "forbidden knowledge...")

    except Exception as e:
        logger.error(f"Error loading MOTD: {e}")
        return ("Welcome to MythosMUD - Enter the realm of "
                "forbidden knowledge...")


class GameEvent(BaseModel):
    """Represents a game event that can be sent to clients."""

    event_type: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(UTC))
    sequence_number: int
    player_id: str | None = None
    room_id: str | None = None
    data: dict[str, Any] = Field(default_factory=dict)

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }


class ConnectionManager:
    """Manages real-time connections for the game."""

    def __init__(self):
        # Active WebSocket connections
        self.active_websockets: dict[str, WebSocket] = {}
        # Player ID to WebSocket mapping
        self.player_websockets: dict[str, str] = {}
        # Active SSE connections (player_id -> connection_id)
        self.active_sse_connections: dict[str, str] = {}
        # Room subscriptions (room_id -> set of player_ids)
        self.room_subscriptions: dict[str, set[str]] = {}
        # Global event sequence counter
        self.sequence_counter = 0
        # Pending messages for guaranteed delivery
        self.pending_messages: dict[str, list[GameEvent]] = {}
        # Reference to persistence layer (set during app startup)
        self.persistence = None

        # Rate limiting for connections
        self.connection_attempts: dict[str, list[float]] = {}
        self.max_connection_attempts = 5  # Max attempts per minute
        self.connection_window = 60  # Time window in seconds

    async def connect_websocket(self, websocket: WebSocket, player_id: str) -> bool:
        """Connect a WebSocket for a player."""
        try:
            await websocket.accept()
            connection_id = str(uuid.uuid4())
            self.active_websockets[connection_id] = websocket
            self.player_websockets[player_id] = connection_id

            # Subscribe to player's current room
            player = self._get_player(player_id)
            if player:
                await self.subscribe_to_room(player_id, player.current_room_id)

            logger.info(f"WebSocket connected for player {player_id}")
            return True
        except Exception as e:
            logger.error(f"Failed to connect WebSocket for player {player_id}: {e}")
            return False

    def disconnect_websocket(self, player_id: str):
        """Disconnect a WebSocket for a player."""
        connection_id = self.player_websockets.get(player_id)
        if connection_id:
            # Remove from active connections
            self.active_websockets.pop(connection_id, None)
            self.player_websockets.pop(player_id, None)

            # Unsubscribe from all rooms
            for room_id in list(self.room_subscriptions.keys()):
                self.room_subscriptions[room_id].discard(player_id)
                if not self.room_subscriptions[room_id]:
                    del self.room_subscriptions[room_id]

            logger.info(f"WebSocket disconnected for player {player_id}")

    def connect_sse(self, player_id: str) -> str:
        """Connect an SSE stream for a player."""
        # Disconnect any existing SSE connection for this player
        self.disconnect_sse(player_id)

        connection_id = str(uuid.uuid4())
        self.active_sse_connections[player_id] = connection_id

        logger.info(f"SSE connected for player {player_id}")
        return connection_id

    def disconnect_sse(self, player_id: str):
        """Disconnect an SSE stream for a player."""
        if player_id in self.active_sse_connections:
            self.active_sse_connections.pop(player_id)
            logger.info(f"SSE disconnected for player {player_id}")

    def get_active_connection_count(self) -> int:
        """Get the total number of active connections."""
        return len(self.active_websockets) + len(self.active_sse_connections)

    def check_rate_limit(self, player_id: str) -> bool:
        """
        Check if a player is within rate limits for connections.

        Args:
            player_id: The player ID to check

        Returns:
            bool: True if within rate limits, False if rate limited
        """
        current_time = time.time()

        # Initialize connection attempts for this player if not exists
        if player_id not in self.connection_attempts:
            self.connection_attempts[player_id] = []

        # Remove old attempts outside the time window
        self.connection_attempts[player_id] = [
            attempt_time for attempt_time in self.connection_attempts[player_id]
            if current_time - attempt_time < self.connection_window
        ]

        # Check if player has exceeded the rate limit
        if len(self.connection_attempts[player_id]) >= self.max_connection_attempts:
            return False

        # Add current attempt
        self.connection_attempts[player_id].append(current_time)
        return True

    def get_rate_limit_info(self, player_id: str) -> dict:
        """
        Get rate limit information for a player.

        Args:
            player_id: The player ID to check

        Returns:
            dict: Rate limit information
        """
        current_time = time.time()

        if player_id not in self.connection_attempts:
            return {
                "attempts": 0,
                "max_attempts": self.max_connection_attempts,
                "window_seconds": self.connection_window,
                "reset_time": current_time + self.connection_window
            }

        # Remove old attempts outside the time window
        self.connection_attempts[player_id] = [
            attempt_time for attempt_time in self.connection_attempts[player_id]
            if current_time - attempt_time < self.connection_window
        ]

        attempts_remaining = max(0, self.max_connection_attempts - len(self.connection_attempts[player_id]))

        return {
            "attempts": len(self.connection_attempts[player_id]),
            "max_attempts": self.max_connection_attempts,
            "window_seconds": self.connection_window,
            "attempts_remaining": attempts_remaining,
            "reset_time": current_time + self.connection_window
        }

    async def subscribe_to_room(self, player_id: str, room_id: str):
        """Subscribe a player to room updates."""
        if room_id not in self.room_subscriptions:
            self.room_subscriptions[room_id] = set()
        self.room_subscriptions[room_id].add(player_id)
        logger.debug(f"Player {player_id} subscribed to room {room_id}")

    async def unsubscribe_from_room(self, player_id: str, room_id: str):
        """Unsubscribe a player from room updates."""
        if room_id in self.room_subscriptions:
            self.room_subscriptions[room_id].discard(player_id)
            if not self.room_subscriptions[room_id]:
                del self.room_subscriptions[room_id]
        logger.debug(f"Player {player_id} unsubscribed from room {room_id}")

    def _get_next_sequence(self) -> int:
        """Get the next sequence number for message ordering."""
        self.sequence_counter += 1
        return self.sequence_counter

    async def send_personal_message(self, player_id: str, event: GameEvent) -> bool:
        """Send a message to a specific player."""
        connection_id = self.player_websockets.get(player_id)
        if not connection_id:
            # Store for later delivery if player reconnects
            if player_id not in self.pending_messages:
                self.pending_messages[player_id] = []
            self.pending_messages[player_id].append(event)
            return False

        websocket = self.active_websockets.get(connection_id)
        if websocket:
            try:
                await websocket.send_text(event.json())
                return True
            except Exception as e:
                logger.error(f"Failed to send message to player {player_id}: {e}")
                self.disconnect_websocket(player_id)
                return False
        return False

    async def broadcast_to_room(self, room_id: str, event: GameEvent, exclude_player: str | None = None):
        """Broadcast a message to all players in a room."""
        if room_id not in self.room_subscriptions:
            return

        for player_id in self.room_subscriptions[room_id]:
            if player_id != exclude_player:
                await self.send_personal_message(player_id, event)

    async def broadcast_global(self, event: GameEvent, exclude_player: str | None = None):
        """Broadcast a message to all connected players."""
        for player_id in list(self.player_websockets.keys()):
            if player_id != exclude_player:
                await self.send_personal_message(player_id, event)

    def get_pending_messages(self, player_id: str) -> list[GameEvent]:
        """Get pending messages for a player (for reconnection)."""
        return self.pending_messages.pop(player_id, [])

    def _get_player(self, player_id: str) -> Player | None:
        """Get player from persistence layer by ID or name."""
        if self.persistence:
            # First try to get by ID (UUID)
            player = self.persistence.get_player(player_id)
            if player:
                return player
            # If not found by ID, try by name (for backward compatibility)
            return self.persistence.get_player_by_name(player_id)
        return None


# Global connection manager instance
connection_manager = ConnectionManager()


async def game_event_stream(player_id: str):
    """Generate Server-Sent Events stream for a player."""
    # Check rate limiting before allowing connection
    if not connection_manager.check_rate_limit(player_id):
        rate_limit_info = connection_manager.get_rate_limit_info(player_id)
        error_event = GameEvent(
            event_type="error",
            sequence_number=connection_manager._get_next_sequence(),
            player_id=player_id,
            data={
                "error": "rate_limited",
                "message": "Too many connection attempts",
                "rate_limit_info": rate_limit_info
            }
        )
        yield f"data: {error_event.json()}\n\n"
        return

    # Register this SSE connection
    connection_manager.connect_sse(player_id)

    try:
        # Send initial game state
        player = connection_manager._get_player(player_id)
        if player:
            initial_event = GameEvent(
                event_type="game_state",
                sequence_number=connection_manager._get_next_sequence(),
                player_id=player_id,
                room_id=player.current_room_id,
                data={
                    "player": player.dict(),
                    "room": get_room_data(player.current_room_id)
                }
            )
            yield f"data: {initial_event.json()}\n\n"

        # Send any pending messages
        pending = connection_manager.get_pending_messages(player_id)
        for event in pending:
            yield f"data: {event.json()}\n\n"

        # Send MOTD
        motd_content = load_motd()
        motd_event = GameEvent(
            event_type="motd",
            sequence_number=connection_manager._get_next_sequence(),
            player_id=player_id,
            data={"message": motd_content}
        )
        yield f"data: {motd_event.json()}\n\n"

        # Keep connection alive with heartbeat
        while True:
            await asyncio.sleep(30)  # Heartbeat every 30 seconds
            heartbeat = GameEvent(
                event_type="heartbeat",
                sequence_number=connection_manager._get_next_sequence(),
                player_id=player_id
            )
            yield f"data: {heartbeat.json()}\n\n"

    except asyncio.CancelledError:
        logger.info(f"SSE stream cancelled for player {player_id}")
    except Exception as e:
        logger.error(f"Error in SSE stream for player {player_id}: {e}")
    finally:
        # Always clean up the connection
        connection_manager.disconnect_sse(player_id)


def get_room_data(room_id: str) -> dict[str, Any]:
    """Get room data from persistence layer."""
    if connection_manager.persistence:
        room = connection_manager.persistence.get_room(room_id)
        if room:
            return room
    return {"id": room_id, "name": "Unknown Room", "description": "A mysterious place..."}


# WebSocket connection handler
async def websocket_endpoint(websocket: WebSocket, player_id: str):
    """Handle WebSocket connections for interactive commands."""
    await connection_manager.connect_websocket(websocket, player_id)

    try:
        while True:
            # Receive command from client
            data = await websocket.receive_text()
            command_data = json.loads(data)

            # Process command and generate response
            response_event = await process_command(player_id, command_data)

            # Send response back to client
            await websocket.send_text(response_event.json())

    except WebSocketDisconnect:
        connection_manager.disconnect_websocket(player_id)
    except Exception as e:
        logger.error(f"WebSocket error for player {player_id}: {e}")
        connection_manager.disconnect_websocket(player_id)


async def process_command(player_id: str, command_data: dict[str, Any]) -> GameEvent:
    """Process a command from a client and return a response event."""
    command = command_data.get("command", "")
    args = command_data.get("args", [])

    # Get player from persistence
    player = connection_manager._get_player(player_id)
    if not player:
        return GameEvent(
            event_type="command_response",
            sequence_number=connection_manager._get_next_sequence(),
            player_id=player_id,
            data={
                "command": command,
                "result": "Player not found",
                "success": False
            }
        )

    # Process command using similar logic to command_handler
    if command == "look":
        room_id = player.current_room_id
        room = get_room_data(room_id)
        if args:
            direction = args[0].lower()
            exits = room.get("exits", {})
            target_room_id = exits.get(direction)
            if target_room_id:
                target_room = get_room_data(target_room_id)
                if target_room:
                    name = target_room.get("name", "")
                    desc = target_room.get("description", "You see nothing special.")
                    result = f"{name}\n{desc}"
                else:
                    result = "You see nothing special that way."
            else:
                result = "You see nothing special that way."
        else:
            name = room.get("name", "")
            result = name

    elif command == "go":
        if not args:
            result = "Go where? Usage: go <direction>"
        else:
            direction = args[0].lower()
            room_id = player.current_room_id
            room = get_room_data(room_id)
            exits = room.get("exits", {})
            target_room_id = exits.get(direction)
            if not target_room_id:
                result = "You can't go that way"
            else:
                target_room = get_room_data(target_room_id)
                if not target_room:
                    result = "You can't go that way"
                else:
                    # Move the player
                    player.current_room_id = target_room_id
                    if connection_manager.persistence:
                        connection_manager.persistence.save_player(player)

                    name = target_room.get("name", "")
                    result = name

                    # Send room update to the moving player
                    room_update_event = GameEvent(
                        event_type="room_update",
                        sequence_number=connection_manager._get_next_sequence(),
                        player_id=player_id,
                        room_id=target_room_id,
                        data={
                            "room": {
                                "name": target_room.get("name", ""),
                                "description": target_room.get("description", "You see nothing special.")
                            },
                            "entities": []  # TODO: Add entities when implemented
                        }
                    )
                    await connection_manager.send_personal_message(player_id, room_update_event)

                    # Broadcast room change to other players in the room (exclude the moving player)
                    await broadcast_room_event(
                        target_room_id,
                        "player_entered",
                        {"player_name": player.name, "player_id": player_id},
                        exclude_player=player_id
                    )

    elif command == "say":
        message = " ".join(args).strip()
        if not message:
            result = "You open your mouth, but no words come out"
        else:
            result = f"You say: {message}"
            # Broadcast to other players in the room
            await broadcast_room_event(
                player.current_room_id,
                "chat_message",
                {"channel": "room", "player_name": player.name, "message": message},
                exclude_player=player_id
            )

    else:
        result = f"Unknown command: {command}"

    return GameEvent(
        event_type="command_response",
        sequence_number=connection_manager._get_next_sequence(),
        player_id=player_id,
        data={
            "command": command,
            "result": result,
            "success": True
        }
    )


# Game tick integration
async def broadcast_game_tick(tick_data: dict[str, Any]):
    """Broadcast game tick updates to all connected players."""
    event = GameEvent(
        event_type="game_tick",
        sequence_number=connection_manager._get_next_sequence(),
        data=tick_data
    )
    await connection_manager.broadcast_global(event)


async def broadcast_room_event(room_id: str, event_type: str, event_data: dict[str, Any], exclude_player: str | None = None):
    """Broadcast a room-specific event to all players in that room."""
    event = GameEvent(
        event_type=event_type,
        sequence_number=connection_manager._get_next_sequence(),
        room_id=room_id,
        data=event_data
    )
    await connection_manager.broadcast_to_room(room_id, event, exclude_player)
