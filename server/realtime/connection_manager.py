"""
Connection manager for MythosMUD real-time communication.

This module handles WebSocket and SSE connection management,
including connection tracking, rate limiting, and room subscriptions.
"""

import logging
import time
import uuid

from fastapi import WebSocket

from ..models import Player

logger = logging.getLogger(__name__)


class ConnectionManager:
    """Manages real-time connections for the game."""

    def __init__(self):
        """Initialize the connection manager."""
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
        self.pending_messages: dict[str, list[dict]] = {}
        # Reference to persistence layer (set during app startup)
        self.persistence = None

        # Rate limiting for connections
        self.connection_attempts: dict[str, list[float]] = {}
        self.max_connection_attempts = 5  # Max attempts per minute
        self.connection_window = 60  # Time window in seconds

    async def connect_websocket(self, websocket: WebSocket, player_id: str) -> bool:
        """
        Connect a WebSocket for a player.

        Args:
            websocket: The WebSocket connection
            player_id: The player's ID

        Returns:
            bool: True if connection successful, False otherwise
        """
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
            # Clean up any partial state in case of failure
            if player_id in self.player_websockets:
                connection_id = self.player_websockets[player_id]
                if connection_id in self.active_websockets:
                    del self.active_websockets[connection_id]
                del self.player_websockets[player_id]
            return False

    def disconnect_websocket(self, player_id: str):
        """
        Disconnect a WebSocket for a player.

        Args:
            player_id: The player's ID
        """
        if player_id in self.player_websockets:
            connection_id = self.player_websockets[player_id]
            if connection_id in self.active_websockets:
                del self.active_websockets[connection_id]
            del self.player_websockets[player_id]

            # Unsubscribe from all rooms
            for room_id in list(self.room_subscriptions.keys()):
                if player_id in self.room_subscriptions[room_id]:
                    self.room_subscriptions[room_id].discard(player_id)
                    if not self.room_subscriptions[room_id]:
                        del self.room_subscriptions[room_id]

            logger.info(f"WebSocket disconnected for player {player_id}")

    def connect_sse(self, player_id: str) -> str:
        """
        Connect an SSE connection for a player.

        Args:
            player_id: The player's ID

        Returns:
            str: The connection ID
        """
        connection_id = str(uuid.uuid4())
        self.active_sse_connections[player_id] = connection_id
        logger.info(f"SSE connected for player {player_id}")
        return connection_id

    def disconnect_sse(self, player_id: str):
        """
        Disconnect an SSE connection for a player.

        Args:
            player_id: The player's ID
        """
        if player_id in self.active_sse_connections:
            del self.active_sse_connections[player_id]
            logger.info(f"SSE disconnected for player {player_id}")

    def get_active_connection_count(self) -> int:
        """
        Get the total number of active connections.

        Returns:
            int: Number of active connections
        """
        return len(self.active_websockets) + len(self.active_sse_connections)

    def check_rate_limit(self, player_id: str) -> bool:
        """
        Check if a player has exceeded rate limits.

        Args:
            player_id: The player's ID

        Returns:
            bool: True if rate limit not exceeded, False if exceeded
        """
        current_time = time.time()
        if player_id not in self.connection_attempts:
            self.connection_attempts[player_id] = []

        # Remove old attempts outside the window
        self.connection_attempts[player_id] = [
            attempt_time
            for attempt_time in self.connection_attempts[player_id]
            if current_time - attempt_time < self.connection_window
        ]

        # Check if limit exceeded
        if len(self.connection_attempts[player_id]) >= self.max_connection_attempts:
            logger.warning(f"Rate limit exceeded for player {player_id}")
            return False

        # Add current attempt
        self.connection_attempts[player_id].append(current_time)
        return True

    def get_rate_limit_info(self, player_id: str) -> dict:
        """
        Get rate limit information for a player.

        Args:
            player_id: The player's ID

        Returns:
            dict: Rate limit information
        """
        current_time = time.time()
        attempts = self.connection_attempts.get(player_id, [])

        # Filter recent attempts
        recent_attempts = [
            attempt_time for attempt_time in attempts if current_time - attempt_time < self.connection_window
        ]

        return {
            "attempts": len(recent_attempts),
            "max_attempts": self.max_connection_attempts,
            "window_seconds": self.connection_window,
            "attempts_remaining": max(0, self.max_connection_attempts - len(recent_attempts)),
            "reset_time": current_time + self.connection_window if recent_attempts else 0,
        }

    async def subscribe_to_room(self, player_id: str, room_id: str):
        """
        Subscribe a player to a room.

        Args:
            player_id: The player's ID
            room_id: The room's ID
        """
        if room_id not in self.room_subscriptions:
            self.room_subscriptions[room_id] = set()
        self.room_subscriptions[room_id].add(player_id)
        logger.debug(f"Player {player_id} subscribed to room {room_id}")

    async def unsubscribe_from_room(self, player_id: str, room_id: str):
        """
        Unsubscribe a player from a room.

        Args:
            player_id: The player's ID
            room_id: The room's ID
        """
        if room_id in self.room_subscriptions:
            self.room_subscriptions[room_id].discard(player_id)
            if not self.room_subscriptions[room_id]:
                del self.room_subscriptions[room_id]
        logger.debug(f"Player {player_id} unsubscribed from room {room_id}")

    def _get_next_sequence(self) -> int:
        """
        Get the next sequence number for events.

        Returns:
            int: The next sequence number
        """
        self.sequence_counter += 1
        return self.sequence_counter

    async def send_personal_message(self, player_id: str, event: dict) -> bool:
        """
        Send a personal message to a player.

        Args:
            player_id: The player's ID
            event: The event data to send

        Returns:
            bool: True if sent successfully, False otherwise
        """
        try:
            # Try WebSocket first
            if player_id in self.player_websockets:
                connection_id = self.player_websockets[player_id]
                if connection_id in self.active_websockets:
                    websocket = self.active_websockets[connection_id]
                    await websocket.send_json(event)
                    return True

            # Fallback to pending messages
            if player_id not in self.pending_messages:
                self.pending_messages[player_id] = []
            self.pending_messages[player_id].append(event)
            return True

        except Exception as e:
            logger.error(f"Failed to send personal message to {player_id}: {e}")
            return False

    async def broadcast_to_room(self, room_id: str, event: dict, exclude_player: str = None):
        """
        Broadcast a message to all players in a room.

        Args:
            room_id: The room's ID
            event: The event data to send
            exclude_player: Player ID to exclude from broadcast
        """
        if room_id in self.room_subscriptions:
            for player_id in self.room_subscriptions[room_id]:
                if player_id != exclude_player:
                    await self.send_personal_message(player_id, event)

    async def broadcast_global(self, event: dict, exclude_player: str = None):
        """
        Broadcast a message to all connected players.

        Args:
            event: The event data to send
            exclude_player: Player ID to exclude from broadcast
        """
        for player_id in list(self.player_websockets.keys()):
            if player_id != exclude_player:
                await self.send_personal_message(player_id, event)

    def get_pending_messages(self, player_id: str) -> list[dict]:
        """
        Get pending messages for a player.

        Args:
            player_id: The player's ID

        Returns:
            list[dict]: List of pending messages
        """
        messages = self.pending_messages.get(player_id, [])
        if player_id in self.pending_messages:
            del self.pending_messages[player_id]
        return messages

    def _get_player(self, player_id: str) -> Player | None:
        """
        Get a player from the persistence layer.

        Args:
            player_id: The player's ID

        Returns:
            Player | None: The player object or None if not found
        """
        if self.persistence is None:
            return None

        player = self.persistence.get_player(player_id)
        if player is None:
            # Fallback to get_player_by_name
            player = self.persistence.get_player_by_name(player_id)
        return player


# Global connection manager instance
connection_manager = ConnectionManager()
