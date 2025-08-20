"""
Connection manager for MythosMUD real-time communication.

This module handles WebSocket and SSE connection management,
including connection tracking, rate limiting, and room subscriptions.
"""

import gc
import time
import uuid

import psutil
from fastapi import WebSocket

from ..game.movement_service import MovementService
from ..logging_config import get_logger
from ..models import Player

logger = get_logger(__name__)


class MemoryMonitor:
    """Monitor memory usage and trigger cleanup when needed."""

    def __init__(self):
        self.last_cleanup_time = time.time()
        self.cleanup_interval = 300  # 5 minutes
        self.memory_threshold = 0.8  # 80% memory usage triggers cleanup
        self.max_connection_age = 300  # 5 minutes
        self.max_pending_messages = 1000  # Max pending messages per player
        self.max_rate_limit_entries = 1000  # Max rate limit entries per player

    def should_cleanup(self) -> bool:
        """Check if cleanup should be triggered."""
        current_time = time.time()
        memory_usage = self.get_memory_usage()

        # Time-based cleanup
        if current_time - self.last_cleanup_time > self.cleanup_interval:
            return True

        # Memory-based cleanup
        if memory_usage > self.memory_threshold:
            logger.warning(f"Memory usage high ({memory_usage:.2%}), triggering cleanup")
            return True

        return False

    def get_memory_usage(self) -> float:
        """Get current memory usage as percentage."""
        try:
            process = psutil.Process()
            memory_percent = process.memory_percent()
            return memory_percent / 100.0
        except Exception as e:
            logger.error(f"Error getting memory usage: {e}")
            return 0.0

    def get_memory_stats(self) -> dict:
        """Get detailed memory statistics."""
        try:
            process = psutil.Process()
            memory_info = process.memory_info()
            return {
                "rss_mb": memory_info.rss / 1024 / 1024,
                "vms_mb": memory_info.vms / 1024 / 1024,
                "percent": process.memory_percent(),
                "available_mb": psutil.virtual_memory().available / 1024 / 1024,
                "total_mb": psutil.virtual_memory().total / 1024 / 1024,
            }
        except Exception as e:
            logger.error(f"Error getting memory stats: {e}")
            return {}


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
        # player_id -> player_info
        self.online_players: dict[str, dict] = {}
        # room_id -> set of player_ids
        self.room_occupants: dict[str, set[str]] = {}
        # player_id -> last seen unix timestamp
        self.last_seen: dict[str, float] = {}

        # Rate limiting for connections
        self.connection_attempts: dict[str, list[float]] = {}
        self.max_connection_attempts = 5  # Max attempts per minute
        self.connection_window = 60  # Time window in seconds

        # Memory monitoring
        self.memory_monitor = MemoryMonitor()

        # Connection tracking with timestamps
        self.connection_timestamps: dict[str, float] = {}

        # Cleanup counters
        self.cleanup_stats = {
            "last_cleanup": time.time(),
            "cleanups_performed": 0,
            "memory_cleanups": 0,
            "time_cleanups": 0,
        }

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

            # Check if player already has an active connection and terminate it
            if player_id in self.player_websockets or player_id in self.active_sse_connections:
                logger.info(f"Player {player_id} has existing connection, terminating it")
                await self.force_disconnect_player(player_id)

            await websocket.accept()
            logger.info(f"WebSocket accepted for player {player_id}")

            connection_id = str(uuid.uuid4())
            self.active_websockets[connection_id] = websocket
            self.player_websockets[player_id] = connection_id
            self.connection_timestamps[connection_id] = time.time()

            # Subscribe to player's current room (canonical room id)
            player = self._get_player(player_id)
            if player:
                canonical_room_id = None
                if self.persistence:
                    room = self.persistence.get_room(player.current_room_id)
                    if room:
                        canonical_room_id = getattr(room, "id", None) or player.current_room_id
                await self.subscribe_to_room(player_id, canonical_room_id or player.current_room_id)

                # Track player presence
                await self._track_player_connected(player_id, player)

            # Check if cleanup is needed
            await self._check_and_cleanup()

            logger.info(f"WebSocket connected for player {player_id}")
            return True
        except Exception as e:
            logger.error(
                f"Failed to connect WebSocket for player {player_id}: {e}",
                exc_info=True,
            )
            # Clean up any partial state in case of failure
            if player_id in self.player_websockets:
                await self.disconnect_websocket(player_id)
            return False

    async def disconnect_websocket(self, player_id: str):
        """
        Disconnect a WebSocket for a player.

        Args:
            player_id: The player's ID
        """
        try:
            if player_id in self.player_websockets:
                connection_id = self.player_websockets[player_id]
                if connection_id in self.active_websockets:
                    websocket = self.active_websockets[connection_id]
                    # Properly close the WebSocket connection
                    try:
                        await websocket.close(code=1000, reason="New connection established")
                    except Exception as e:
                        logger.warning(f"Error closing WebSocket for {player_id}: {e}")
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

                # Clean up rate limiting data
                if player_id in self.connection_attempts:
                    del self.connection_attempts[player_id]

                # Clean up pending messages
                if player_id in self.pending_messages:
                    del self.pending_messages[player_id]

                # Clean up last seen data
                if player_id in self.last_seen:
                    del self.last_seen[player_id]

                logger.info(f"WebSocket disconnected for player {player_id}")
        except Exception as e:
            logger.error(f"Error during WebSocket disconnect for {player_id}: {e}", exc_info=True)

    async def force_disconnect_player(self, player_id: str):
        """
        Force disconnect a player from all connections (WebSocket and SSE).
        This is used when a new connection is established for the same player.

        Args:
            player_id: The player's ID
        """
        try:
            logger.info(f"Force disconnecting player {player_id} from all connections")

            # Disconnect WebSocket if active
            if player_id in self.player_websockets:
                await self.disconnect_websocket(player_id)

            # Disconnect SSE if active
            if player_id in self.active_sse_connections:
                self.disconnect_sse(player_id)

            logger.info(f"Player {player_id} force disconnected from all connections")
        except Exception as e:
            logger.error(f"Error force disconnecting player {player_id}: {e}", exc_info=True)

    def connect_sse(self, player_id: str) -> str:
        """
        Connect an SSE connection for a player.

        Args:
            player_id: The player's ID

        Returns:
            str: The SSE connection ID
        """
        # Check if player already has an active connection and terminate it
        if player_id in self.player_websockets or player_id in self.active_sse_connections:
            logger.info(f"Player {player_id} has existing connection, terminating it")
            # Use async version if we're in an async context
            try:
                import asyncio

                loop = asyncio.get_running_loop()
                loop.create_task(self.force_disconnect_player(player_id))
            except RuntimeError:
                # No running loop, run synchronously
                import asyncio

                asyncio.run(self.force_disconnect_player(player_id))

        connection_id = str(uuid.uuid4())
        self.active_sse_connections[player_id] = connection_id
        logger.info(f"SSE connected for player {player_id}")

        # Track presence on SSE as well so occupants reflect players who have only SSE connected
        try:
            player = self._get_player(player_id)
            if player:
                # Resolve canonical room id
                room_id = getattr(player, "current_room_id", None)
                if self.persistence and room_id:
                    try:
                        room = self.persistence.get_room(room_id)
                        if room and getattr(room, "id", None):
                            room_id = room.id
                    except Exception as e:
                        logger.error(f"Error resolving canonical room for SSE connect {player_id}: {e}")

                # Schedule async presence updates
                import asyncio

                try:
                    loop = asyncio.get_running_loop()
                    # Subscribe to room first so subsequent broadcasts reach this player
                    if room_id:
                        loop.create_task(self.subscribe_to_room(player_id, room_id))
                    loop.create_task(self._track_player_connected(player_id, player))
                except RuntimeError:
                    # No running loop; run synchronously
                    if room_id:
                        asyncio.run(self.subscribe_to_room(player_id, room_id))
                    asyncio.run(self._track_player_connected(player_id, player))
        except Exception as e:
            logger.error(f"Error tracking SSE connect for {player_id}: {e}", exc_info=True)

        return connection_id

    def disconnect_sse(self, player_id: str):
        """
        Disconnect an SSE connection for a player.

        Args:
            player_id: The player's ID
        """
        try:
            if player_id in self.active_sse_connections:
                del self.active_sse_connections[player_id]

            # Clean up rate limiting data
            if player_id in self.connection_attempts:
                del self.connection_attempts[player_id]

            # Clean up pending messages
            if player_id in self.pending_messages:
                del self.pending_messages[player_id]

            # Clean up last seen data
            if player_id in self.last_seen:
                del self.last_seen[player_id]

            # Delegate to unified disconnect logic. If no running loop, run synchronously.
            try:
                import asyncio

                try:
                    loop = asyncio.get_running_loop()
                    loop.create_task(self._track_player_disconnected(player_id))
                except RuntimeError:
                    # No running loop in this thread; execute synchronously
                    asyncio.run(self._track_player_disconnected(player_id))
            except Exception as e:
                logger.error(f"Error handling SSE disconnect for {player_id}: {e}")

            logger.info(f"SSE disconnected for player {player_id}")
        except Exception as e:
            logger.error(f"Error during SSE disconnect for {player_id}: {e}", exc_info=True)

    def mark_player_seen(self, player_id: str):
        """Update last-seen timestamp for a player."""
        try:
            self.last_seen[player_id] = time.time()
        except Exception as e:
            logger.error(f"Error marking player {player_id} seen: {e}")

    def prune_stale_players(self, max_age_seconds: int = 90):
        """Remove players whose presence is stale beyond the threshold.

        This prunes `online_players` and `room_occupants` and broadcasts an
        occupants update when appropriate on next room broadcast.
        """
        try:
            now_ts = time.time()
            stale_ids: list[str] = []
            for pid, last in list(self.last_seen.items()):
                if now_ts - last > max_age_seconds:
                    stale_ids.append(pid)

            for pid in stale_ids:
                if pid in self.online_players:
                    del self.online_players[pid]
                if pid in self.player_websockets:
                    # forget websocket mapping; socket likely already dead
                    conn_id = self.player_websockets.pop(pid, None)
                    if conn_id and conn_id in self.active_websockets:
                        del self.active_websockets[conn_id]
                # remove from rooms
                self._prune_player_from_all_rooms(pid)
                # forget last_seen entry
                if pid in self.last_seen:
                    del self.last_seen[pid]
                # Clean up other references
                if pid in self.connection_attempts:
                    del self.connection_attempts[pid]
                if pid in self.pending_messages:
                    del self.pending_messages[pid]
                if pid in self.active_sse_connections:
                    del self.active_sse_connections[pid]
            if stale_ids:
                logger.info(f"Pruned stale players: {stale_ids}")
        except Exception as e:
            logger.error(f"Error pruning stale players: {e}")

    async def cleanup_orphaned_data(self):
        """Clean up orphaned data that might accumulate over time."""
        try:
            now_ts = time.time()
            cleanup_stats = {
                "orphaned_attempts": 0,
                "orphaned_messages": 0,
                "stale_connections": 0,
                "large_message_queues": 0,
                "large_rate_limits": 0,
            }

            # Clean up orphaned connection attempts (older than 1 hour)
            orphaned_attempts = []
            for player_id, attempts in list(self.connection_attempts.items()):
                # Remove attempts older than 1 hour
                self.connection_attempts[player_id] = [
                    attempt_time
                    for attempt_time in attempts
                    if now_ts - attempt_time < 3600  # 1 hour
                ]

                # Limit rate limit entries per player
                if len(self.connection_attempts[player_id]) > self.memory_monitor.max_rate_limit_entries:
                    self.connection_attempts[player_id] = self.connection_attempts[player_id][
                        -self.memory_monitor.max_rate_limit_entries :
                    ]
                    cleanup_stats["large_rate_limits"] += 1

                # Remove empty entries
                if not self.connection_attempts[player_id]:
                    orphaned_attempts.append(player_id)

            for player_id in orphaned_attempts:
                del self.connection_attempts[player_id]
                cleanup_stats["orphaned_attempts"] += 1

            # Clean up orphaned pending messages (older than 1 hour)
            orphaned_messages = []
            for player_id, messages in list(self.pending_messages.items()):
                # Remove messages older than 1 hour
                self.pending_messages[player_id] = [
                    msg
                    for msg in messages
                    if self._is_message_recent(msg, now_ts)  # 1 hour
                ]

                # Limit pending messages per player
                if len(self.pending_messages[player_id]) > self.memory_monitor.max_pending_messages:
                    self.pending_messages[player_id] = self.pending_messages[player_id][
                        -self.memory_monitor.max_pending_messages :
                    ]
                    cleanup_stats["large_message_queues"] += 1

                # Remove empty entries
                if not self.pending_messages[player_id]:
                    orphaned_messages.append(player_id)

            for player_id in orphaned_messages:
                del self.pending_messages[player_id]
                cleanup_stats["orphaned_messages"] += 1

            # Clean up stale connections
            stale_connections = []
            for connection_id, timestamp in list(self.connection_timestamps.items()):
                if now_ts - timestamp > self.memory_monitor.max_connection_age:
                    stale_connections.append(connection_id)

            for connection_id in stale_connections:
                if connection_id in self.active_websockets:
                    try:
                        websocket = self.active_websockets[connection_id]
                        await websocket.close(code=1000, reason="Connection timeout")
                    except Exception as e:
                        logger.warning(f"Error closing stale connection {connection_id}: {e}")
                    del self.active_websockets[connection_id]
                del self.connection_timestamps[connection_id]
                cleanup_stats["stale_connections"] += 1

            # Update cleanup stats
            self.cleanup_stats["cleanups_performed"] += 1
            self.memory_monitor.last_cleanup_time = now_ts

            if any(cleanup_stats.values()):
                logger.info(
                    f"Memory cleanup completed: {cleanup_stats['orphaned_attempts']} attempts, "
                    f"{cleanup_stats['orphaned_messages']} message queues, "
                    f"{cleanup_stats['stale_connections']} stale connections, "
                    f"{cleanup_stats['large_message_queues']} large queues, "
                    f"{cleanup_stats['large_rate_limits']} large rate limits"
                )

        except Exception as e:
            logger.error(f"Error cleaning up orphaned data: {e}", exc_info=True)

    def _is_message_recent(self, msg: dict, now_ts: float) -> bool:
        """
        Check if a message is recent (within 1 hour).

        Args:
            msg: Message dictionary
            now_ts: Current timestamp as float

        Returns:
            bool: True if message is recent, False otherwise
        """
        try:
            timestamp = msg.get("timestamp", 0)
            if isinstance(timestamp, str):
                # Try to parse ISO timestamp string
                try:
                    from datetime import datetime

                    dt = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
                    msg_ts = dt.timestamp()
                except (ValueError, AttributeError):
                    # If parsing fails, assume it's old
                    return False
            elif isinstance(timestamp, (int, float)):
                msg_ts = float(timestamp)
            else:
                # Unknown timestamp format, assume it's old
                return False

            return now_ts - msg_ts < 3600  # 1 hour
        except Exception:
            # If any error occurs, assume the message is old
            return False

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
        canonical_id = self._canonical_room_id(room_id) or room_id
        if canonical_id not in self.room_subscriptions:
            self.room_subscriptions[canonical_id] = set()
        self.room_subscriptions[canonical_id].add(player_id)
        logger.debug(f"Player {player_id} subscribed to room {canonical_id}")

        # Redis has been removed - no subscription needed
        logger.debug(f"Redis removed - no subscription needed for room {canonical_id}")

    async def unsubscribe_from_room(self, player_id: str, room_id: str):
        """
        Unsubscribe a player from a room.

        Args:
            player_id: The player's ID
            room_id: The room's ID
        """
        canonical_id = self._canonical_room_id(room_id) or room_id
        if canonical_id in self.room_subscriptions:
            self.room_subscriptions[canonical_id].discard(player_id)
            if not self.room_subscriptions[canonical_id]:
                del self.room_subscriptions[canonical_id]

                # Redis has been removed - no unsubscription needed
        logger.debug(f"Redis removed - no unsubscription needed for room {canonical_id}")

        logger.debug(f"Player {player_id} unsubscribed from room {canonical_id}")

    def _get_next_sequence(self) -> int:
        """
        Get the next sequence number for events.

        Returns:
            int: The next sequence number
        """
        self.sequence_counter += 1
        return self.sequence_counter

    def _canonical_room_id(self, room_id: str | None) -> str | None:
        """Resolve a room id to the canonical Room.id value, when possible."""
        try:
            if not room_id:
                return room_id
            if self.persistence is not None:
                room = self.persistence.get_room(room_id)
                if room is not None and getattr(room, "id", None):
                    return room.id
        except Exception as e:
            logger.error(f"Error resolving canonical room id for {room_id}: {e}")
        return room_id

    def _convert_uuids_to_strings(self, obj):
        """
        Recursively convert UUID objects to strings for JSON serialization.

        Args:
            obj: Object to convert

        Returns:
            Object with UUIDs converted to strings
        """
        if isinstance(obj, dict):
            return {k: self._convert_uuids_to_strings(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [self._convert_uuids_to_strings(item) for item in obj]
        elif hasattr(obj, "__class__") and "UUID" in obj.__class__.__name__:
            return str(obj)
        else:
            return obj

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
            # Convert UUIDs to strings for JSON serialization
            serializable_event = self._convert_uuids_to_strings(event)

            # Try WebSocket first
            if player_id in self.player_websockets:
                connection_id = self.player_websockets[player_id]
                if connection_id in self.active_websockets:
                    websocket = self.active_websockets[connection_id]
                    await websocket.send_json(serializable_event)
                    return True

            # Fallback to pending messages
            if player_id not in self.pending_messages:
                self.pending_messages[player_id] = []
            self.pending_messages[player_id].append(serializable_event)
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
        canonical_id = self._canonical_room_id(room_id) or room_id
        targets: set[str] = set()
        if canonical_id in self.room_subscriptions:
            targets.update(self.room_subscriptions[canonical_id])
        if room_id != canonical_id and room_id in self.room_subscriptions:
            targets.update(self.room_subscriptions[room_id])
        for pid in targets:
            if pid != exclude_player:
                await self.send_personal_message(pid, event)

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
            self.mark_player_seen(player_id)

            # Update room occupants using canonical room id
            room_id = getattr(player, "current_room_id", None)
            if self.persistence and room_id:
                room = self.persistence.get_room(room_id)
                if room and getattr(room, "id", None):
                    room_id = room.id
            if room_id:
                if room_id not in self.room_occupants:
                    self.room_occupants[room_id] = set()
                self.room_occupants[room_id].add(player_id)

                # Prune any stale occupant ids not currently online
                self._reconcile_room_presence(room_id)

                # Add player to the Room object's _players set for movement service
                if self.persistence:
                    # Create MovementService with the same persistence layer
                    event_bus = getattr(self, "_event_bus", None)
                    movement_service = MovementService(event_bus)
                    # Override the persistence layer to use the same instance
                    movement_service._persistence = self.persistence
                    success = movement_service.add_player_to_room(player_id, room_id)
                    if success:
                        logger.info(f"Player {player_id} added to room {room_id} for movement service")
                    else:
                        logger.warning(f"Failed to add player {player_id} to room {room_id} for movement service")

                # Send initial game_state event to the player
                await self._send_initial_game_state(player_id, player, room_id)

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
            # Resolve player using flexible lookup (ID or name)
            pl = self._get_player(player_id)
            room_id: str | None = getattr(pl, "current_room_id", None) if pl else None
            player_name: str | None = getattr(pl, "name", None) if pl else None

            # Remove from online and room presence
            # Remove possible variants (provided id, canonical id, and name)
            keys_to_remove = {player_id}
            if pl is not None:
                canonical_id = getattr(pl, "player_id", None) or getattr(pl, "user_id", None)
                if canonical_id:
                    keys_to_remove.add(str(canonical_id))
                if player_name:
                    keys_to_remove.add(player_name)

            for key in list(keys_to_remove):
                if key in self.online_players:
                    del self.online_players[key]
                self._prune_player_from_all_rooms(key)

            # Clean up any remaining references
            if player_id in self.online_players:
                del self.online_players[player_id]
            if player_id in self.last_seen:
                del self.last_seen[player_id]
            if player_id in self.connection_attempts:
                del self.connection_attempts[player_id]
            if player_id in self.pending_messages:
                del self.pending_messages[player_id]

            # Notify current room that player left the game and refresh occupants
            if room_id:
                # 1) left-game notification
                from .envelope import build_event

                left_event = build_event(
                    "player_left_game",
                    {"player_id": player_id, "player_name": player_name or player_id},
                    room_id=room_id,
                )
                await self.broadcast_to_room(room_id, left_event)

                # 2) occupants update (names only)
                occ_infos = self.get_room_occupants(room_id)
                names: list[str] = []
                for occ in occ_infos:
                    name = occ.get("player_name") if isinstance(occ, dict) else None
                    if name:
                        names.append(name)
                occ_event = build_event(
                    "room_occupants",
                    {"occupants": names, "count": len(names)},
                    room_id=room_id,
                )
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

        # Resolve to canonical id and check set presence
        room_id = self._canonical_room_id(room_id) or room_id
        if room_id not in self.room_occupants:
            return occupants

        # Only include online players currently tracked in this room
        for player_id in self.room_occupants[room_id]:
            if player_id in self.online_players:
                occupants.append(self.online_players[player_id])

        return occupants

    async def _send_initial_game_state(self, player_id: str, player: Player, room_id: str):
        """
        Send initial game_state event to a newly connected player.

        Args:
            player_id: The player's ID
            player: The player object
            room_id: The player's current room ID
        """
        try:
            from .envelope import build_event

            # Get room information
            room_data = None
            if self.persistence and room_id:
                room = self.persistence.get_room(room_id)
                if room:
                    room_data = room.to_dict()

            # Get room occupants
            occupants = []
            if room_id and room_id in self.room_occupants:
                for occ_player_id in self.room_occupants[room_id]:
                    if occ_player_id != player_id:  # Exclude the player themselves
                        occ_player = self._get_player(occ_player_id)
                        if occ_player:
                            occupants.append(getattr(occ_player, "name", occ_player_id))

            # Create game_state event
            game_state_data = {
                "player": {
                    "player_id": str(getattr(player, "player_id", player_id)),
                    "name": getattr(player, "name", player_id),
                    "level": getattr(player, "level", 1),
                    "current_room_id": room_id,
                },
                "room": room_data,
                "occupants": occupants,
            }

            game_state_event = build_event("game_state", game_state_data, player_id=player_id, room_id=room_id)

            # Send the event to the player
            await self.send_personal_message(player_id, game_state_event)
            logger.info(f"Sent initial game_state to player {player_id}")

        except Exception as e:
            logger.error(f"Error sending initial game_state to player {player_id}: {e}", exc_info=True)

    def _reconcile_room_presence(self, room_id: str):
        """Ensure room_occupants only contains currently online players."""
        try:
            if room_id in self.room_occupants:
                current = self.room_occupants[room_id]
                pruned = {pid for pid in current if pid in self.online_players}
                self.room_occupants[room_id] = pruned
        except Exception as e:
            logger.error(f"Error reconciling room presence for {room_id}: {e}")

    async def _check_and_cleanup(self):
        """
        Periodically check for cleanup conditions and perform cleanup if needed.
        """
        if self.memory_monitor.should_cleanup():
            logger.info("MemoryMonitor triggered cleanup.")
            self.cleanup_stats["memory_cleanups"] += 1
            self.cleanup_stats["last_cleanup"] = time.time()
            await self.cleanup_orphaned_data()
            self.prune_stale_players()
            gc.collect()
            logger.info("Cleanup complete.")

    def get_memory_stats(self) -> dict:
        """Get comprehensive memory and connection statistics."""
        try:
            memory_stats = self.memory_monitor.get_memory_stats()

            return {
                "memory": memory_stats,
                "connections": {
                    "active_websockets": len(self.active_websockets),
                    "active_sse": len(self.active_sse_connections),
                    "total_connections": len(self.active_websockets) + len(self.active_sse_connections),
                    "player_websockets": len(self.player_websockets),
                    "connection_timestamps": len(self.connection_timestamps),
                },
                "data_structures": {
                    "online_players": len(self.online_players),
                    "room_occupants": len(self.room_occupants),
                    "room_subscriptions": len(self.room_subscriptions),
                    "last_seen": len(self.last_seen),
                    "connection_attempts": len(self.connection_attempts),
                    "pending_messages": len(self.pending_messages),
                },
                "cleanup_stats": self.cleanup_stats,
                "memory_monitor": {
                    "last_cleanup": self.memory_monitor.last_cleanup_time,
                    "cleanup_interval": self.memory_monitor.cleanup_interval,
                    "memory_threshold": self.memory_monitor.memory_threshold,
                    "max_connection_age": self.memory_monitor.max_connection_age,
                    "max_pending_messages": self.memory_monitor.max_pending_messages,
                    "max_rate_limit_entries": self.memory_monitor.max_rate_limit_entries,
                },
            }
        except Exception as e:
            logger.error(f"Error getting memory stats: {e}", exc_info=True)
            return {}

    def get_memory_alerts(self) -> list[str]:
        """Get memory-related alerts."""
        alerts = []

        try:
            memory_usage = self.memory_monitor.get_memory_usage()

            if memory_usage > 0.9:  # 90%
                alerts.append(f"CRITICAL: Memory usage at {memory_usage:.1%}")
            elif memory_usage > 0.8:  # 80%
                alerts.append(f"WARNING: Memory usage at {memory_usage:.1%}")
            elif memory_usage > 0.7:  # 70%
                alerts.append(f"INFO: Memory usage at {memory_usage:.1%}")

            # Check for large data structures
            if len(self.connection_attempts) > 1000:
                alerts.append(f"WARNING: Large number of rate limit entries: {len(self.connection_attempts)}")

            if len(self.pending_messages) > 1000:
                alerts.append(f"WARNING: Large number of pending message queues: {len(self.pending_messages)}")

            # Check for stale connections
            now = time.time()
            stale_count = sum(
                1 for ts in self.connection_timestamps.values() if now - ts > self.memory_monitor.max_connection_age
            )
            if stale_count > 0:
                alerts.append(f"WARNING: {stale_count} stale connections detected")

        except Exception as e:
            logger.error(f"Error getting memory alerts: {e}", exc_info=True)
            alerts.append(f"ERROR: Failed to get memory alerts: {e}")

        return alerts

    async def force_cleanup(self):
        """Force immediate cleanup of all orphaned data."""
        try:
            logger.info("Forcing immediate cleanup")
            await self.cleanup_orphaned_data()
            self.prune_stale_players()
            gc.collect()
            self.cleanup_stats["cleanups_performed"] += 1
            self.memory_monitor.last_cleanup_time = time.time()
            logger.info("Force cleanup completed")
        except Exception as e:
            logger.error(f"Error during force cleanup: {e}", exc_info=True)


# Global connection manager instance
connection_manager = ConnectionManager()
