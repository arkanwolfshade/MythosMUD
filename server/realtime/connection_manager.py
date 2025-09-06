"""
Refactored Connection Manager for MythosMUD real-time communication.

This module provides a clean, modular connection management system that
separates concerns into dedicated components for better maintainability
and testability.
"""

import asyncio
import time
import uuid
from typing import Any

from fastapi import WebSocket

from ..logging_config import get_logger
from ..models import Player
from .memory_monitor import MemoryMonitor
from .message_queue import MessageQueue
from .rate_limiter import RateLimiter
from .room_subscription_manager import RoomSubscriptionManager

logger = get_logger(__name__)


class ConnectionManager:
    """
    Manages real-time connections for the game.

    This refactored version uses modular components to separate concerns:
    - MemoryMonitor: Memory usage monitoring and cleanup scheduling
    - RateLimiter: Connection rate limiting
    - MessageQueue: Pending message management
    - RoomSubscriptionManager: Room subscriptions and occupant tracking
    """

    def __init__(self):
        """Initialize the connection manager with modular components."""
        # Active WebSocket connections
        self.active_websockets: dict[str, WebSocket] = {}
        # Player ID to WebSocket mapping
        self.player_websockets: dict[str, str] = {}
        # Active SSE connections (player_id -> connection_id)
        self.active_sse_connections: dict[str, str] = {}
        # Global event sequence counter
        self.sequence_counter = 0
        # Reference to persistence layer (set during app startup)
        self.persistence = None

        # Player presence tracking
        # player_id -> player_info
        self.online_players: dict[str, dict[str, Any]] = {}
        # player_id -> last seen unix timestamp
        self.last_seen: dict[str, float] = {}
        # Track players currently being disconnected to prevent duplicate events
        self.disconnecting_players: set[str] = set()
        self.disconnect_lock = asyncio.Lock()
        # Track players whose disconnect has already been processed
        self.processed_disconnects: set[str] = set()
        self.processed_disconnect_lock = asyncio.Lock()

        # Connection tracking with timestamps
        self.connection_timestamps: dict[str, float] = {}

        # Cleanup counters
        self.cleanup_stats = {
            "last_cleanup": time.time(),
            "cleanups_performed": 0,
            "memory_cleanups": 0,
            "time_cleanups": 0,
        }

        # Initialize modular components
        self.memory_monitor = MemoryMonitor()
        self.rate_limiter = RateLimiter()
        self.message_queue = MessageQueue(max_messages_per_player=self.memory_monitor.max_pending_messages)
        self.room_manager = RoomSubscriptionManager()

    # Compatibility properties for existing tests and code
    # These provide access to the internal data structures for backward compatibility
    @property
    def room_subscriptions(self):
        return self.room_manager.room_subscriptions

    @room_subscriptions.setter
    def room_subscriptions(self, value):
        self.room_manager.room_subscriptions = value

    @room_subscriptions.deleter
    def room_subscriptions(self):
        self.room_manager.room_subscriptions.clear()

    @property
    def room_occupants(self):
        return self.room_manager.room_occupants

    @room_occupants.setter
    def room_occupants(self, value):
        self.room_manager.room_occupants = value

    @room_occupants.deleter
    def room_occupants(self):
        self.room_manager.room_occupants.clear()

    @property
    def connection_attempts(self):
        return self.rate_limiter.connection_attempts

    @connection_attempts.setter
    def connection_attempts(self, value):
        self.rate_limiter.connection_attempts = value

    @connection_attempts.deleter
    def connection_attempts(self):
        self.rate_limiter.connection_attempts.clear()

    @property
    def pending_messages(self):
        return self.message_queue.pending_messages

    @pending_messages.setter
    def pending_messages(self, value):
        self.message_queue.pending_messages = value

    @pending_messages.deleter
    def pending_messages(self):
        self.message_queue.pending_messages.clear()

    # Add missing attributes that tests expect
    @property
    def max_connection_attempts(self):
        return self.rate_limiter.max_connection_attempts

    @property
    def connection_window(self):
        return self.rate_limiter.connection_window

    # Add compatibility methods
    async def subscribe_to_room(self, player_id: str, room_id: str):
        """Subscribe a player to a room (compatibility method)."""
        # Resolve canonical room ID first
        canonical_id = self._canonical_room_id(room_id) or room_id
        return self.room_manager.subscribe_to_room(player_id, canonical_id)

    async def unsubscribe_from_room(self, player_id: str, room_id: str):
        """Unsubscribe a player from a room (compatibility method)."""
        return self.room_manager.unsubscribe_from_room(player_id, room_id)

    def _canonical_room_id(self, room_id: str | None) -> str | None:
        """Resolve a room id to the canonical Room.id value (compatibility method)."""
        # First try the room manager's persistence
        result = self.room_manager._canonical_room_id(room_id)
        if result != room_id:  # If room manager resolved it, return that
            return result

        # Fallback to main persistence layer for compatibility
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

    def _reconcile_room_presence(self, room_id: str):
        """Ensure room_occupants only contains currently online players (compatibility method)."""
        return self.room_manager.reconcile_room_presence(room_id, self.online_players)

    def _prune_player_from_all_rooms(self, player_id: str):
        """Remove a player from all room subscriptions and occupant lists (compatibility method)."""
        return self.room_manager.remove_player_from_all_rooms(player_id)

    def set_persistence(self, persistence):
        """Set the persistence layer reference for all components."""
        self.persistence = persistence
        self.room_manager.set_persistence(persistence)

    async def connect_websocket(self, websocket: WebSocket, player_id: str) -> bool:
        """
        Connect a WebSocket for a player.

        Args:
            websocket: The WebSocket connection
            player_id: The player's ID

        Returns:
            bool: True if connection was successful, False otherwise
        """
        try:
            # CRITICAL FIX: Add connection lock to prevent race conditions
            async with self.disconnect_lock:
                # Check if player already has an active WebSocket connection
                # Only terminate if this is a genuine reconnection (not simultaneous connection)
                if player_id in self.player_websockets:
                    existing_connection_id = self.player_websockets[player_id]
                    if existing_connection_id in self.active_websockets:
                        existing_websocket = self.active_websockets[existing_connection_id]
                        # Check if the existing WebSocket is still open
                        try:
                            # CRITICAL FIX: Add timeout to ping operation to prevent hanging
                            await asyncio.wait_for(existing_websocket.ping(), timeout=2.0)
                            logger.info(
                                f"Player {player_id} has existing active WebSocket connection, terminating it for reconnection"
                            )
                            # Clear pending messages BEFORE force disconnect to prevent stale messages
                            self.message_queue.remove_player_messages(player_id)
                            # Only disconnect the WebSocket, not all connections
                            await self.disconnect_websocket(player_id, is_force_disconnect=True)
                        except TimeoutError:
                            logger.warning(f"Existing WebSocket for player {player_id} ping timeout, cleaning up")
                            # Clean up the dead connection
                            await self.disconnect_websocket(player_id, is_force_disconnect=True)
                        except Exception as ping_error:
                            logger.warning(
                                f"Existing WebSocket for player {player_id} is not responding, cleaning up: {ping_error}"
                            )
                            # Clean up the dead connection
                            await self.disconnect_websocket(player_id, is_force_disconnect=True)
                    else:
                        logger.warning(f"Player {player_id} has stale WebSocket reference, cleaning up")
                        # Clean up stale reference
                        del self.player_websockets[player_id]

            await websocket.accept()
            connection_id = str(uuid.uuid4())
            self.active_websockets[connection_id] = websocket
            self.player_websockets[player_id] = connection_id
            logger.info(f"WebSocket connected for player {player_id}")

            # Get player and room information
            player = self._get_player(player_id)
            if not player:
                if self.persistence is None:
                    logger.warning(f"Persistence not available, connecting without player tracking for {player_id}")
                else:
                    logger.error(f"Player {player_id} not found")
                    return False
            else:
                canonical_room_id = getattr(player, "current_room_id", None)
                if canonical_room_id:
                    self.room_manager.subscribe_to_room(player_id, canonical_room_id)

                # Track player presence - always call _track_player_connected for WebSocket connections
                # to ensure connection messages are broadcast to other players
                if player_id not in self.online_players:
                    await self._track_player_connected(player_id, player)
                else:
                    logger.info(
                        f"Player {player_id} already tracked as online, but broadcasting connection message for WebSocket"
                    )
                    # Still broadcast connection message even if player is already tracked
                    await self._broadcast_connection_message(player_id, player)

        except Exception as e:
            logger.error(f"Error connecting WebSocket for {player_id}: {e}", exc_info=True)
            return False

        return True

    async def disconnect_websocket(self, player_id: str, is_force_disconnect: bool = False):
        """
        Disconnect a WebSocket for a player.

        Args:
            player_id: The player's ID
            is_force_disconnect: If True, don't broadcast player_left_game
        """
        try:
            if player_id in self.player_websockets:
                connection_id = self.player_websockets[player_id]
                if connection_id in self.active_websockets:
                    websocket = self.active_websockets[connection_id]
                    # Only track disconnection if it's not a force disconnect
                    if not is_force_disconnect:
                        async with self.processed_disconnect_lock:
                            if player_id not in self.processed_disconnects:
                                self.processed_disconnects.add(player_id)
                                await self._track_player_disconnected(player_id)
                            else:
                                logger.debug(f"Disconnect already processed for player {player_id}, skipping")

                    # Properly close the WebSocket connection
                    try:
                        await websocket.close(code=1000, reason="New connection established")
                    except Exception as e:
                        logger.warning(f"Error closing WebSocket for {player_id}: {e}")
                    del self.active_websockets[connection_id]
                del self.player_websockets[player_id]

                # Unsubscribe from all rooms only if it's not a force disconnect (reconnection)
                # During reconnections, we want to preserve room membership
                if not is_force_disconnect:
                    self.room_manager.remove_player_from_all_rooms(player_id)
                else:
                    logger.debug(
                        f"🔍 DEBUG: Preserving room membership for player {player_id} during force disconnect (reconnection)"
                    )

                # Clean up rate limiting data
                self.rate_limiter.remove_player_data(player_id)

                # Clean up pending messages
                self.message_queue.remove_player_messages(player_id)

                # Clean up last seen data
                if player_id in self.last_seen:
                    del self.last_seen[player_id]

                logger.info(f"WebSocket disconnected for player {player_id}")
        except Exception as e:
            logger.error(f"Error during WebSocket disconnect for {player_id}: {e}", exc_info=True)

    async def force_disconnect_player(self, player_id: str):
        """
        Force disconnect a player from all connections (WebSocket and SSE).

        Args:
            player_id: The player's ID
        """
        try:
            logger.info(f"Force disconnecting player {player_id} from all connections")

            # Disconnect WebSocket if active (without broadcasting player_left_game)
            if player_id in self.player_websockets:
                await self.disconnect_websocket(player_id, is_force_disconnect=True)

            # Disconnect SSE if active
            if player_id in self.active_sse_connections:
                self.disconnect_sse(player_id, is_force_disconnect=True)

            logger.info(f"Player {player_id} force disconnected from all connections")
        except Exception as e:
            logger.error(f"Error force disconnecting player {player_id}: {e}", exc_info=True)

    async def connect_sse(self, player_id: str) -> str:
        """
        Connect an SSE connection for a player.

        Args:
            player_id: The player's ID

        Returns:
            str: The connection ID
        """
        try:
            # Check if player already has an active SSE connection
            # Only terminate if this is a genuine reconnection (not simultaneous connection)
            if player_id in self.active_sse_connections:
                logger.info(f"Player {player_id} has existing SSE connection, terminating it for reconnection")
                # Only disconnect the SSE connection, not all connections
                self.disconnect_sse(player_id, is_force_disconnect=True)

        except Exception as e:
            logger.error(f"Error force disconnecting player {player_id}: {e}", exc_info=True)

        connection_id = str(uuid.uuid4())
        self.active_sse_connections[player_id] = connection_id
        logger.info(f"SSE connected for player {player_id}")

        # Clear pending messages to prevent stale messages from previous connections
        self.message_queue.remove_player_messages(player_id)

        # Track presence on SSE as well so occupants reflect players who have only SSE connected
        try:
            player = self._get_player(player_id)
            if player:
                canonical_room_id = None
                if self.persistence:
                    room = self.persistence.get_room(player.current_room_id)
                    if room:
                        canonical_room_id = getattr(room, "id", None) or player.current_room_id
                await self.subscribe_to_room(player_id, canonical_room_id or player.current_room_id)

                # Track player presence - only call _track_player_connected if this is the first connection
                if player_id not in self.online_players:
                    await self._track_player_connected(player_id, player)
                else:
                    logger.info(f"Player {player_id} already tracked as online, skipping _track_player_connected")
            elif self.persistence is None:
                logger.warning(f"Persistence not available, SSE connecting without player tracking for {player_id}")

        except Exception as e:
            logger.error(f"Error tracking SSE presence for {player_id}: {e}", exc_info=True)

        return connection_id

    def disconnect_sse(self, player_id: str, is_force_disconnect: bool = False):
        """
        Disconnect an SSE connection for a player.

        Args:
            player_id: The player's ID
            is_force_disconnect: If True, don't broadcast player_left_game
        """
        try:
            if player_id in self.active_sse_connections:
                del self.active_sse_connections[player_id]

            # Clean up rate limiting data
            self.rate_limiter.remove_player_data(player_id)

            # Clean up pending messages
            self.message_queue.remove_player_messages(player_id)

            # Clean up last seen data
            if player_id in self.last_seen:
                del self.last_seen[player_id]

            # Only track disconnection if it's not a force disconnect
            if not is_force_disconnect:
                try:
                    loop = asyncio.get_running_loop()
                    loop.create_task(self._check_and_process_disconnect(player_id))
                except RuntimeError:
                    # No running loop in this thread; execute synchronously
                    asyncio.run(self._check_and_process_disconnect(player_id))

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
        """
        Remove players whose presence is stale beyond the threshold.

        Args:
            max_age_seconds: Maximum age in seconds before considering a player stale
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
                self.room_manager.remove_player_from_all_rooms(pid)
                # forget last_seen entry
                if pid in self.last_seen:
                    del self.last_seen[pid]
                # Clean up other references
                self.rate_limiter.remove_player_data(pid)
                self.message_queue.remove_player_messages(pid)
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

            # Clean up rate limiting data
            self.rate_limiter.cleanup_old_attempts()
            self.rate_limiter.cleanup_large_structures(self.memory_monitor.max_rate_limit_entries)

            # Clean up message queue data
            self.message_queue.cleanup_old_messages()
            self.message_queue.cleanup_large_structures(self.memory_monitor.max_pending_messages)

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
            self.memory_monitor.update_cleanup_time()

            if any(cleanup_stats.values()):
                logger.info(f"Memory cleanup completed: {cleanup_stats['stale_connections']} stale connections")

        except Exception as e:
            logger.error(f"Error cleaning up orphaned data: {e}", exc_info=True)

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
        return self.rate_limiter.check_rate_limit(player_id)

    def get_rate_limit_info(self, player_id: str) -> dict[str, Any]:
        """
        Get rate limit information for a player.

        Args:
            player_id: The player's ID

        Returns:
            Dict[str, Any]: Rate limit information
        """
        return self.rate_limiter.get_rate_limit_info(player_id)

    async def send_personal_message(self, player_id: str, event: dict[str, Any]) -> bool:
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
                    # CRITICAL FIX: Check WebSocket state before sending
                    try:
                        # Check if WebSocket is still open by attempting to send
                        await websocket.send_json(serializable_event)
                        return True
                    except Exception as ws_error:
                        # WebSocket is closed or in an invalid state
                        logger.warning(f"WebSocket send failed for player {player_id}: {ws_error}")
                        # Clean up the dead WebSocket connection
                        await self._cleanup_dead_websocket(player_id, connection_id)
                        # Continue to fallback to pending messages

            # Fallback to pending messages - add message without timestamp for compatibility
            if player_id not in self.message_queue.pending_messages:
                self.message_queue.pending_messages[player_id] = []
            self.message_queue.pending_messages[player_id].append(serializable_event)
            return True

        except Exception as e:
            logger.error(f"Failed to send personal message to {player_id}: {e}")
            return False

    async def broadcast_to_room(self, room_id: str, event: dict[str, Any], exclude_player: str | None = None):
        """
        Broadcast a message to all players in a room.

        Args:
            room_id: The room's ID
            event: The event data to send
            exclude_player: Player ID to exclude from broadcast
        """
        targets = self.room_manager.get_room_subscribers(room_id)

        # Debug logging for self-message exclusion
        logger.debug(f"broadcast_to_room: room_id={room_id}, exclude_player={exclude_player}")
        logger.debug(f"broadcast_to_room: targets={targets}")

        for pid in targets:
            if pid != exclude_player:
                logger.debug(f"broadcast_to_room: sending to player {pid}")
                await self.send_personal_message(pid, event)
            else:
                logger.debug(f"broadcast_to_room: excluding player {pid} (self-message exclusion)")

    async def broadcast_global(self, event: dict[str, Any], exclude_player: str | None = None):
        """
        Broadcast a message to all connected players.

        Args:
            event: The event data to send
            exclude_player: Player ID to exclude from broadcast
        """
        for player_id in list(self.player_websockets.keys()):
            if player_id != exclude_player:
                await self.send_personal_message(player_id, event)

    def get_pending_messages(self, player_id: str) -> list[dict[str, Any]]:
        """
        Get pending messages for a player.

        Args:
            player_id: The player's ID

        Returns:
            List[Dict[str, Any]]: List of pending messages
        """
        return self.message_queue.get_messages(player_id)

    def _get_player(self, player_id: str) -> Player | None:
        """
        Get a player from the persistence layer.

        Args:
            player_id: The player's ID

        Returns:
            Optional[Player]: The player object or None if not found
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

    def _get_next_sequence(self) -> int:
        """
        Get the next sequence number for events.

        Returns:
            int: The next sequence number
        """
        self.sequence_counter += 1
        return self.sequence_counter

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

            # Update last_active timestamp in database when player connects
            if self.persistence:
                try:
                    from datetime import UTC, datetime

                    player.last_active = datetime.now(UTC)
                    self.persistence.save_player(player)
                    logger.debug(f"Updated last_active for player {player_id} on connection")
                except Exception as e:
                    logger.warning(f"Failed to update last_active for player {player_id}: {e}")

            # Clear any pending messages to ensure fresh game state
            self.message_queue.remove_player_messages(player_id)

            # Clear processed disconnect flag to allow future disconnect processing
            async with self.processed_disconnect_lock:
                self.processed_disconnects.discard(player_id)

            # Update room occupants using canonical room id
            room_id = getattr(player, "current_room_id", None)
            if self.persistence and room_id:
                room = self.persistence.get_room(room_id)
                if room and getattr(room, "id", None):
                    room_id = room.id
            if room_id:
                self.room_manager.add_room_occupant(player_id, room_id)

                # Prune any stale occupant ids not currently online
                self.room_manager.reconcile_room_presence(room_id, self.online_players)

                # Add player to the Room object and trigger player_entered event
                if self.persistence:
                    room = self.persistence.get_room(room_id)
                    if room:
                        # Call room.player_entered() to ensure proper event publishing
                        room.player_entered(player_id)
                        logger.info(f"Player {player_id} entered room {room_id} via player_entered()")
                    else:
                        logger.warning(f"Room {room_id} not found when trying to add player {player_id}")

                # Send initial game_state event to the player
                await self._send_initial_game_state(player_id, player, room_id)

                # Notify current room that player entered the game
                from .envelope import build_event

                entered_event = build_event(
                    "player_entered_game",
                    {"player_id": player_id, "player_name": player_info["player_name"]},
                    room_id=room_id,
                )
                logger.info(f"🔍 DEBUG: Broadcasting player_entered_game for {player_id} in room {room_id}")
                await self.broadcast_to_room(room_id, entered_event, exclude_player=player_id)

            logger.info(f"Player {player_id} presence tracked as connected")

        except Exception as e:
            logger.error(f"Error tracking player connection: {e}", exc_info=True)

    async def _broadcast_connection_message(self, player_id: str, player: Player):
        """
        Broadcast a connection message for a player who is already tracked as online.
        This is used when a player connects via WebSocket but is already in the online_players list.

        Args:
            player_id: The player's ID
            player: The player object
        """
        try:
            room_id = getattr(player, "current_room_id", None)
            if self.persistence and room_id:
                room = self.persistence.get_room(room_id)
                if room and getattr(room, "id", None):
                    room_id = room.id

            if room_id:
                # Debug: Check room subscriptions before broadcasting
                subscribers = self.room_manager.get_room_subscribers(room_id)
                logger.debug(f"🔍 DEBUG: Room {room_id} has subscribers: {subscribers}")
                logger.debug(f"🔍 DEBUG: Room subscriptions dict: {self.room_manager.room_subscriptions}")

                # Broadcast connection message to other players in the room
                from .envelope import build_event

                player_name = getattr(player, "name", player_id)
                entered_event = build_event(
                    "player_entered_game",
                    {"player_id": player_id, "player_name": player_name},
                    room_id=room_id,
                )
                logger.info(
                    f"🔍 DEBUG: Broadcasting player_entered_game for {player_id} in room {room_id} (already tracked)"
                )
                await self.broadcast_to_room(room_id, entered_event, exclude_player=player_id)

        except Exception as e:
            logger.error(f"Error broadcasting connection message for {player_id}: {e}", exc_info=True)

    async def _track_player_disconnected(self, player_id: str):
        """
        Track when a player disconnects.

        Args:
            player_id: The player's ID
        """
        try:
            # Prevent duplicate disconnect events for the same player using async lock
            async with self.disconnect_lock:
                if player_id in self.disconnecting_players:
                    logger.debug(f"🔍 DEBUG: Player {player_id} already being disconnected, skipping duplicate event")
                    return

                # Mark player as being disconnected
                self.disconnecting_players.add(player_id)
                logger.debug(f"🔍 DEBUG: Marked player {player_id} as disconnecting")

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
                self.room_manager.remove_player_from_all_rooms(key)

                # CRITICAL FIX: Also remove player from room's internal _players set
                if room_id and self.persistence:
                    room = self.persistence.get_room(room_id)
                    if room and room.has_player(key):
                        logger.debug(f"🔍 DEBUG: Removing ghost player {key} from room {room_id}")
                        room.player_left(key)

                # CRITICAL FIX: Clean up all ghost players from all rooms
                self._cleanup_ghost_players()

            # Clean up any remaining references
            if player_id in self.online_players:
                del self.online_players[player_id]
            if player_id in self.last_seen:
                del self.last_seen[player_id]
            self.rate_limiter.remove_player_data(player_id)
            self.message_queue.remove_player_messages(player_id)

            # Notify current room that player left the game and refresh occupants
            if room_id:
                # 1) left-game notification
                from .envelope import build_event

                left_event = build_event(
                    "player_left_game",
                    {"player_id": player_id, "player_name": player_name or player_id},
                    room_id=room_id,
                )
                # Exclude the disconnecting player from their own "left game" message
                logger.info(f"🔍 DEBUG: Broadcasting player_left_game for {player_id} in room {room_id}")
                await self.broadcast_to_room(room_id, left_event, exclude_player=player_id)

                # 2) occupants update (names only)
                occ_infos = self.room_manager.get_room_occupants(room_id, self.online_players)
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
        finally:
            # Always remove player from disconnecting set, even on error
            async with self.disconnect_lock:
                self.disconnecting_players.discard(player_id)

    def _cleanup_ghost_players(self):
        """
        Clean up ghost players from all rooms.

        This method removes players from room's internal _players set
        if they are no longer in the online_players set.
        """
        try:
            if not self.persistence or not hasattr(self.persistence, "_room_cache"):
                return

            # Get all online player IDs
            online_player_ids = set(self.online_players.keys())

            # Get all rooms from the room cache
            for _room_id, room in self.persistence._room_cache.items():
                if not hasattr(room, "_players"):
                    continue

                # Get players in this room
                room_player_ids = set(room._players)

                # Find ghost players (players in room but not online)
                ghost_players = room_player_ids - online_player_ids

                if ghost_players:
                    logger.debug(f"🔍 DEBUG: Found ghost players in room {room.id}: {ghost_players}")
                    for ghost_player_id in ghost_players:
                        room._players.discard(ghost_player_id)
                        logger.debug(f"🔍 DEBUG: Removed ghost player {ghost_player_id} from room {room.id}")

        except Exception as e:
            logger.error(f"Error cleaning up ghost players: {e}", exc_info=True)

    async def detect_and_handle_error_state(self, player_id: str, error_type: str, error_details: str):
        """
        Detect when a client is in an error state and handle it appropriately.

        Args:
            player_id: The player's ID
            error_type: Type of error detected
            error_details: Detailed error information
        """
        try:
            import json
            import os
            from datetime import datetime

            logger.error(f"ERROR STATE DETECTED for player {player_id}: {error_type} - {error_details}")

            # Log the error state to a dedicated error log file
            error_log_entry = {
                "timestamp": datetime.now().isoformat(),
                "player_id": player_id,
                "error_type": error_type,
                "error_details": error_details,
                "connections": {
                    "websocket": player_id in self.player_websockets,
                    "sse": player_id in self.active_sse_connections,
                    "online": player_id in self.online_players,
                },
            }

            # Write to error log file
            error_log_path = "logs/development/connection_errors.log"
            os.makedirs(os.path.dirname(error_log_path), exist_ok=True)
            with open(error_log_path, "a") as f:
                f.write(json.dumps(error_log_entry) + "\n")

            # Only terminate connections if this is a critical error
            if error_type in ["CRITICAL_WEBSOCKET_ERROR", "CRITICAL_SSE_ERROR", "AUTHENTICATION_FAILURE"]:
                logger.error(f"CRITICAL ERROR: Terminating all connections for player {player_id}")
                await self.force_disconnect_player(player_id)
            else:
                logger.warning(f"Non-critical error: Keeping connections alive for player {player_id}")

        except Exception as e:
            logger.error(f"Error in detect_and_handle_error_state for {player_id}: {e}", exc_info=True)

    async def handle_new_login(self, player_id: str):
        """
        Handle a new login by terminating all existing connections for the player.
        This ensures that only one session per player is active at a time.

        Args:
            player_id: The player's ID
        """
        try:
            logger.info(f"NEW LOGIN detected for player {player_id}, terminating existing connections")

            # Log the new login event
            import json
            import os
            from datetime import datetime

            login_log_entry = {
                "timestamp": datetime.now().isoformat(),
                "player_id": player_id,
                "event_type": "NEW_LOGIN",
                "connections_before": {
                    "websocket": player_id in self.player_websockets,
                    "sse": player_id in self.active_sse_connections,
                    "online": player_id in self.online_players,
                },
            }

            # Write to login log file
            login_log_path = "logs/development/new_logins.log"
            os.makedirs(os.path.dirname(login_log_path), exist_ok=True)
            with open(login_log_path, "a") as f:
                f.write(json.dumps(login_log_entry) + "\n")

            # Terminate all existing connections
            await self.force_disconnect_player(player_id)

        except Exception as e:
            logger.error(f"Error handling new login for {player_id}: {e}", exc_info=True)

    async def _check_and_process_disconnect(self, player_id: str):
        """
        Check if disconnect has already been processed for a player and process it if not.

        Args:
            player_id: The player's ID
        """
        async with self.processed_disconnect_lock:
            if player_id not in self.processed_disconnects:
                self.processed_disconnects.add(player_id)
                await self._track_player_disconnected(player_id)
            else:
                logger.debug(f"Disconnect already processed for player {player_id}, skipping")

    def get_online_players(self) -> list[dict[str, Any]]:
        """
        Get list of online players.

        Returns:
            List[Dict[str, Any]]: List of online player information
        """
        return list(self.online_players.values())

    def get_online_player_by_display_name(self, display_name: str) -> dict[str, Any] | None:
        """
        Get online player information by display name.

        Args:
            display_name: Display name to search for (case-insensitive)

        Returns:
            dict: Player information if found, None otherwise
        """
        # Case-insensitive search
        display_name_lower = display_name.lower()

        for player_id, player_info in self.online_players.items():
            if player_info.get("player_name", "").lower() == display_name_lower:
                logger.debug(f"Found online player {display_name} with ID {player_id}")
                return player_info

        logger.debug(f"Online player {display_name} not found")
        return None

    def get_room_occupants(self, room_id: str) -> list[dict[str, Any]]:
        """
        Get list of occupants in a room.

        Args:
            room_id: The room ID

        Returns:
            List[Dict[str, Any]]: List of occupant information
        """
        return self.room_manager.get_room_occupants(room_id, self.online_players)

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
            if room_id:
                occ_infos = self.room_manager.get_room_occupants(room_id, self.online_players)
                for occ_player_info in occ_infos:
                    if isinstance(occ_player_info, dict) and occ_player_info.get("player_id") != player_id:
                        occupants.append(occ_player_info.get("player_name", "Unknown"))

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

    async def _check_and_cleanup(self):
        """Periodically check for cleanup conditions and perform cleanup if needed."""
        if self.memory_monitor.should_cleanup():
            logger.info("MemoryMonitor triggered cleanup.")
            self.cleanup_stats["memory_cleanups"] += 1
            self.cleanup_stats["last_cleanup"] = time.time()
            await self.cleanup_orphaned_data()
            self.prune_stale_players()
            self.memory_monitor.force_garbage_collection()
            logger.info("Cleanup complete.")

    def get_memory_stats(self) -> dict[str, Any]:
        """Get comprehensive memory and connection statistics."""
        try:
            memory_stats = self.memory_monitor.get_memory_stats()
            rate_limiter_stats = self.rate_limiter.get_stats()
            message_queue_stats = self.message_queue.get_stats()
            room_stats = self.room_manager.get_stats()

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
                    "last_seen": len(self.last_seen),
                    "room_occupants": len(self.room_manager.room_occupants),
                    "connection_attempts": len(self.rate_limiter.connection_attempts),
                    "pending_messages": len(self.message_queue.pending_messages),
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
                "rate_limiter": rate_limiter_stats,
                "message_queue": message_queue_stats,
                "room_manager": room_stats,
            }
        except Exception as e:
            logger.error(f"Error getting memory stats: {e}", exc_info=True)
            return {}

    def get_memory_alerts(self) -> list[str]:
        """Get memory-related alerts."""
        try:
            # Calculate stale connections
            now_ts = time.time()
            stale_connections = 0
            for timestamp in self.connection_timestamps.values():
                if now_ts - timestamp > self.memory_monitor.max_connection_age:
                    stale_connections += 1

            connection_stats = {
                "connection_attempts": len(self.rate_limiter.connection_attempts),
                "pending_messages": len(self.message_queue.pending_messages),
                "stale_connections": stale_connections,
            }
            return self.memory_monitor.get_memory_alerts(connection_stats)
        except Exception as e:
            logger.error(f"Error getting memory alerts: {e}", exc_info=True)
            return [f"ERROR: Failed to get memory alerts: {e}"]

    async def force_cleanup(self):
        """Force immediate cleanup of all orphaned data."""
        try:
            logger.info("Forcing immediate cleanup")

            # Cancel any running cleanup tasks
            if hasattr(self, "_cleanup_task") and self._cleanup_task and not self._cleanup_task.done():
                logger.info("Cancelling existing cleanup task")
                self._cleanup_task.cancel()
                try:
                    await self._cleanup_task
                except asyncio.CancelledError:
                    pass
                except Exception as e:
                    logger.error(f"Error cancelling cleanup task: {e}")

            await self.cleanup_orphaned_data()
            self.prune_stale_players()
            self.memory_monitor.force_garbage_collection()
            self.cleanup_stats["cleanups_performed"] += 1
            self.memory_monitor.update_cleanup_time()
            logger.info("Force cleanup completed")
        except Exception as e:
            logger.error(f"Error during force cleanup: {e}", exc_info=True)

    async def check_connection_health(self, player_id: str) -> bool:
        """
        Check if a player's connections are healthy.

        Args:
            player_id: The player's ID

        Returns:
            bool: True if connections are healthy, False otherwise
        """
        try:
            health_status = {"websocket_healthy": False, "sse_healthy": False, "overall_healthy": False}

            # Check WebSocket health
            if player_id in self.player_websockets:
                connection_id = self.player_websockets[player_id]
                if connection_id in self.active_websockets:
                    websocket = self.active_websockets[connection_id]
                    try:
                        # Try to send a ping to check if connection is alive
                        await websocket.ping()
                        health_status["websocket_healthy"] = True
                        logger.debug(f"WebSocket health check passed for player {player_id}")
                    except Exception as e:
                        logger.warning(f"WebSocket health check failed for player {player_id}: {e}")
                        # Mark WebSocket as unhealthy and remove it
                        await self.disconnect_websocket(player_id, is_force_disconnect=True)

            # Check SSE health
            if player_id in self.active_sse_connections:
                try:
                    # For SSE, we can't easily ping, so we assume it's healthy if it exists
                    # and hasn't been explicitly disconnected
                    health_status["sse_healthy"] = True
                    logger.debug(f"SSE health check passed for player {player_id}")
                except Exception as e:
                    logger.warning(f"SSE health check failed for player {player_id}: {e}")
                    self.disconnect_sse(player_id, is_force_disconnect=True)

            # Overall health is good if at least one connection is healthy
            health_status["overall_healthy"] = health_status["websocket_healthy"] or health_status["sse_healthy"]

            if not health_status["overall_healthy"]:
                logger.warning(f"All connections unhealthy for player {player_id}")
                await self.detect_and_handle_error_state(
                    player_id, "CONNECTION_HEALTH_FAILURE", f"All connections failed health check: {health_status}"
                )

            return health_status["overall_healthy"]

        except Exception as e:
            logger.error(f"Error checking connection health for player {player_id}: {e}", exc_info=True)
            return False


# Global connection manager instance
connection_manager = ConnectionManager()
