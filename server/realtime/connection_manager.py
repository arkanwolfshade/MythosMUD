"""
Connection manager for MythosMUD real-time communication.

This module handles WebSocket and SSE connection management,
including connection tracking, rate limiting, and room subscriptions.
"""

import time
import uuid

from fastapi import WebSocket

from ..logging_config import get_logger
from ..models import Player

logger = get_logger(__name__)


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

        # Player presence tracking
        self.online_players: dict[str, dict] = {}  # player_id -> player_info
        self.room_occupants: dict[str, set[str]] = {}  # room_id -> set of player_ids

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
            logger.info(f"Attempting to accept WebSocket for player {player_id}")
            await websocket.accept()
            logger.info(f"WebSocket accepted for player {player_id}")

            connection_id = str(uuid.uuid4())
            self.active_websockets[connection_id] = websocket
            self.player_websockets[player_id] = connection_id

            # Subscribe to player's current room
            player = self._get_player(player_id)
            if player:
                await self.subscribe_to_room(player_id, player.current_room_id)

                # Track player presence
                await self._track_player_connected(player_id, player)

            logger.info(f"WebSocket connected for player {player_id}")
            return True
        except Exception as e:
            logger.error(f"Failed to connect WebSocket for player {player_id}: {e}", exc_info=True)
            # Clean up any partial state in case of failure
            if player_id in self.player_websockets:
                connection_id = self.player_websockets[player_id]
                if connection_id in self.active_websockets:
                    del self.active_websockets[connection_id]
                del self.player_websockets[player_id]
            return False

    async def disconnect_websocket(self, player_id: str):
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

            # Track player disconnection
            await self._track_player_disconnected(player_id)

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
            str: The SSE connection ID
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
        # On SSE disconnect, also reconcile presence (in case WS is closed too)
        self._prune_player_from_all_rooms(player_id)
        logger.info(f"SSE disconnected for player {player_id}")

    def _prune_player_from_all_rooms(self, player_id: str):
        """Remove a player from all in-memory room occupant sets."""
        try:
            for room_id in list(self.room_occupants.keys()):
                if player_id in self.room_occupants[room_id]:
                    self.room_occupants[room_id].discard(player_id)
                    if not self.room_occupants[room_id]:
                        del self.room_occupants[room_id]
        except Exception as e:
            logger.error(f"Error pruning player {player_id} from rooms: {e}")

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
            logger.warning(f"Persistence layer not initialized for player lookup: {player_id}")
            return None

        player = self.persistence.get_player(player_id)
        if player is None:
            # Fallback to get_player_by_name
            logger.info(f"Player not found by ID, trying by name: {player_id}")
            player = self.persistence.get_player_by_name(player_id)
            if player:
                logger.info(f"Player found by name: {player_id}")
            else:
                logger.warning(f"Player not found by name: {player_id}")
        return player

    async def _track_player_connected(self, player_id: str, player: Player):
        """
        Track when a player connects.

        Args:
            player_id: The player's ID
            player: The player object
        """
        try:
            player_info = {
                "player_id": player_id,
                "player_name": getattr(player, "name", player_id),
                "level": getattr(player, "level", 1),
                "current_room_id": getattr(player, "current_room_id", None),
                "connected_at": time.time(),
            }

            self.online_players[player_id] = player_info

            # Update room occupants
            room_id = getattr(player, "current_room_id", None)
            if room_id:
                if room_id not in self.room_occupants:
                    self.room_occupants[room_id] = set()
                self.room_occupants[room_id].add(player_id)

                # Prune any stale occupant ids not currently online
                self._reconcile_room_presence(room_id)

            logger.info(f"Player {player_id} presence tracked as connected")

        except Exception as e:
            logger.error(f"Error tracking player connection: {e}", exc_info=True)

    async def _track_player_disconnected(self, player_id: str):
        """
        Track when a player disconnects.

        Args:
            player_id: The player's ID
        """
        try:
            # Capture last known room and name from persistence
            room_id: str | None = None
            player_name: str | None = None
            if self.persistence is not None:
                pl = self.persistence.get_player(player_id)
                if pl is not None:
                    room_id = getattr(pl, "current_room_id", None)
                    player_name = getattr(pl, "name", None)

            # Remove from online and room presence
            if player_id in self.online_players:
                del self.online_players[player_id]

            self._prune_player_from_all_rooms(player_id)

            # Notify current room that player left the game and refresh occupants
            if room_id:
                # 1) left-game notification
                left_event = {
                    "event_type": "player_left_game",
                    "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                    "sequence_number": self._get_next_sequence(),
                    "room_id": room_id,
                    "data": {
                        "player_id": player_id,
                        "player_name": player_name or player_id,
                    },
                }
                await self.broadcast_to_room(room_id, left_event)

                # 2) occupants update (names only)
                occ_infos = self.get_room_occupants(room_id)
                names: list[str] = []
                for occ in occ_infos:
                    name = occ.get("player_name") if isinstance(occ, dict) else None
                    if name:
                        names.append(name)
                occ_event = {
                    "event_type": "room_occupants",
                    "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                    "sequence_number": self._get_next_sequence(),
                    "room_id": room_id,
                    "data": {"occupants": names, "count": len(names)},
                }
                await self.broadcast_to_room(room_id, occ_event)

            logger.info(f"Player {player_id} presence tracked as disconnected")

        except Exception as e:
            logger.error(f"Error tracking player disconnection: {e}", exc_info=True)

    def get_online_players(self) -> list[dict]:
        """
        Get list of online players.

        Returns:
            list[dict]: List of online player information
        """
        return list(self.online_players.values())

    def get_room_occupants(self, room_id: str) -> list[dict]:
        """
        Get list of occupants in a room.

        Args:
            room_id: The room ID

        Returns:
            list[dict]: List of occupant information
        """
        occupants: list[dict] = []

        # If we have no tracked occupants set for this room, treat as empty
        if room_id not in self.room_occupants:
            return occupants

        # Only include online players currently tracked in this room
        for player_id in self.room_occupants[room_id]:
            if player_id in self.online_players:
                occupants.append(self.online_players[player_id])

        return occupants

    def _reconcile_room_presence(self, room_id: str):
        """Ensure room_occupants only contains currently online players."""
        try:
            if room_id in self.room_occupants:
                current = self.room_occupants[room_id]
                pruned = {pid for pid in current if pid in self.online_players}
                self.room_occupants[room_id] = pruned
        except Exception as e:
            logger.error(f"Error reconciling room presence for {room_id}: {e}")


# Global connection manager instance
connection_manager = ConnectionManager()
