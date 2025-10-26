"""
Refactored Connection Manager for MythosMUD real-time communication.

This module provides a clean, modular connection management system that
separates concerns into dedicated components for better maintainability
and testability.
"""

import asyncio
import time
import uuid
from dataclasses import dataclass
from datetime import UTC
from typing import Any

from fastapi import WebSocket

from ..logging.enhanced_logging_config import get_logger
from ..models import Player
from .memory_monitor import MemoryMonitor
from .message_queue import MessageQueue
from .rate_limiter import RateLimiter
from .room_subscription_manager import RoomSubscriptionManager

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


@dataclass
class ConnectionMetadata:
    """
    Metadata for tracking connection details in the dual connection system.

    This dataclass stores information about each connection to enable
    proper management of multiple connections per player.
    """

    connection_id: str
    player_id: str
    connection_type: str  # "websocket" or "sse"
    established_at: float
    last_seen: float
    is_healthy: bool
    session_id: str | None = None  # For tracking new game client sessions


class ConnectionManager:
    """
    Manages real-time connections for the game.

    This refactored version uses modular components to separate concerns:
    - MemoryMonitor: Memory usage monitoring and cleanup scheduling
    - RateLimiter: Connection rate limiting
    - MessageQueue: Pending message management
    - RoomSubscriptionManager: Room subscriptions and occupant tracking
    """

    def __init__(self, event_publisher=None):
        """Initialize the connection manager with modular components."""
        # Active WebSocket connections
        self.active_websockets: dict[str, WebSocket] = {}
        # Player ID to WebSocket connection IDs mapping (supports multiple connections)
        self.player_websockets: dict[str, list[str]] = {}
        # Active SSE connections (player_id -> list of connection_ids)
        self.active_sse_connections: dict[str, list[str]] = {}
        # Connection metadata tracking
        self.connection_metadata: dict[str, ConnectionMetadata] = {}
        # Global event sequence counter
        self.sequence_counter = 0
        # Reference to persistence layer (set during app startup)
        self.persistence = None
        # EventPublisher for NATS integration
        self.event_publisher = event_publisher

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

        # Performance monitoring
        self.performance_stats = {
            "connection_establishment_times": [],  # List of (connection_type, duration_ms)
            "message_delivery_times": [],  # List of (message_type, duration_ms)
            "disconnection_times": [],  # List of (connection_type, duration_ms)
            "session_switch_times": [],  # List of (duration_ms)
            "health_check_times": [],  # List of (duration_ms)
            "total_connections_established": 0,
            "total_messages_delivered": 0,
            "total_disconnections": 0,
            "total_session_switches": 0,
            "total_health_checks": 0,
        }

        # Initialize modular components
        self.memory_monitor = MemoryMonitor()
        self.rate_limiter = RateLimiter()
        self.message_queue = MessageQueue(max_messages_per_player=self.memory_monitor.max_pending_messages)
        self.room_manager = RoomSubscriptionManager()

        # Session management
        self.player_sessions: dict[str, str] = {}  # player_id -> current_session_id
        self.session_connections: dict[str, list[str]] = {}  # session_id -> list of connection_ids

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

    # Compatibility methods for dual connection system
    def get_player_websocket_connection_id(self, player_id: str) -> str | None:
        """
        Get the first WebSocket connection ID for a player (backward compatibility).

        Args:
            player_id: The player's ID

        Returns:
            str: The first connection ID if any exist, None otherwise
        """
        if player_id in self.player_websockets and self.player_websockets[player_id]:
            return self.player_websockets[player_id][0]
        return None

    def get_player_sse_connection_id(self, player_id: str) -> str | None:
        """
        Get the first SSE connection ID for a player (backward compatibility).

        Args:
            player_id: The player's ID

        Returns:
            str: The first connection ID if any exist, None otherwise
        """
        if player_id in self.active_sse_connections and self.active_sse_connections[player_id]:
            return self.active_sse_connections[player_id][0]
        return None

    def has_websocket_connection(self, player_id: str) -> bool:
        """
        Check if a player has any WebSocket connections.

        Args:
            player_id: The player's ID

        Returns:
            bool: True if player has WebSocket connections, False otherwise
        """
        return player_id in self.player_websockets and len(self.player_websockets[player_id]) > 0

    def has_sse_connection(self, player_id: str) -> bool:
        """
        Check if a player has any SSE connections.

        Args:
            player_id: The player's ID

        Returns:
            bool: True if player has SSE connections, False otherwise
        """
        return player_id in self.active_sse_connections and len(self.active_sse_connections[player_id]) > 0

    def get_connection_count(self, player_id: str) -> dict[str, int]:
        """
        Get the number of connections for a player by type.

        Args:
            player_id: The player's ID

        Returns:
            dict: Connection counts by type
        """
        websocket_count = len(self.player_websockets.get(player_id, []))
        sse_count = len(self.active_sse_connections.get(player_id, []))
        return {"websocket": websocket_count, "sse": sse_count, "total": websocket_count + sse_count}

    # Add compatibility methods
    async def subscribe_to_room(self, player_id: str, room_id: str):
        """Subscribe a player to a room (compatibility method)."""
        # Resolve canonical room ID first
        canonical_id = self._canonical_room_id(room_id) or room_id
        return self.room_manager.subscribe_to_room(player_id, canonical_id)

    async def unsubscribe_from_room(self, player_id: str, room_id: str):
        """Unsubscribe a player from a room (compatibility method)."""
        # Resolve canonical room ID first (must match subscribe_to_room behavior)
        canonical_id = self._canonical_room_id(room_id) or room_id
        return self.room_manager.unsubscribe_from_room(player_id, canonical_id)

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
            logger.error("Error resolving canonical room id", room_id=room_id, error=str(e))
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

    async def connect_websocket(self, websocket: WebSocket, player_id: str, session_id: str | None = None) -> bool:
        """
        Connect a WebSocket for a player.

        Args:
            websocket: The WebSocket connection
            player_id: The player's ID
            session_id: Optional session ID for tracking new game client sessions

        Returns:
            bool: True if connection was successful, False otherwise
        """
        start_time = time.time()
        try:
            # CRITICAL FIX: Check for dead connections BEFORE acquiring lock to prevent hanging
            dead_connection_ids = []
            if player_id in self.player_websockets:
                # Check connections for health without holding the lock
                for connection_id in self.player_websockets[player_id]:
                    if connection_id in self.active_websockets:
                        existing_websocket = self.active_websockets[connection_id]
                        try:
                            # Check if the existing WebSocket is still open by checking its state
                            if existing_websocket.client_state.name != "CONNECTED":
                                raise Exception("WebSocket not connected")
                        except Exception as ping_error:
                            logger.warning(
                                f"Dead WebSocket connection {connection_id} for player {player_id}, will clean up: {ping_error}"
                            )
                            dead_connection_ids.append(connection_id)

            # CRITICAL FIX: Minimal lock scope - only for data structure updates
            async with self.disconnect_lock:
                # Clean up dead connections identified above
                if dead_connection_ids:
                    for connection_id in dead_connection_ids:
                        # Clean up the dead connection
                        if connection_id in self.active_websockets:
                            del self.active_websockets[connection_id]
                            if connection_id in self.connection_metadata:
                                del self.connection_metadata[connection_id]

                # Check if player already has active WebSocket connections
                # For dual connection system, we allow multiple connections
                if player_id in self.player_websockets:
                    # Update the player's connection list with only active connections
                    active_connection_ids = [
                        conn_id for conn_id in self.player_websockets[player_id] if conn_id in self.active_websockets
                    ]
                    if active_connection_ids:
                        self.player_websockets[player_id] = active_connection_ids
                    else:
                        # No active connections, remove the player entry
                        del self.player_websockets[player_id]

            # Accept the WebSocket connection
            await websocket.accept()
            connection_id = str(uuid.uuid4())
            self.active_websockets[connection_id] = websocket

            # Add the new connection to the player's connection list
            if player_id not in self.player_websockets:
                self.player_websockets[player_id] = []
            self.player_websockets[player_id].append(connection_id)

            # Create connection metadata
            current_time = time.time()
            self.connection_metadata[connection_id] = ConnectionMetadata(
                connection_id=connection_id,
                player_id=player_id,
                connection_type="websocket",
                established_at=current_time,
                last_seen=current_time,
                is_healthy=True,
                session_id=session_id,
            )

            # Track connection in session
            if session_id:
                if session_id not in self.session_connections:
                    self.session_connections[session_id] = []
                self.session_connections[session_id].append(connection_id)
                # Only update player session if they don't have one or if this is the same session
                if player_id not in self.player_sessions or self.player_sessions[player_id] == session_id:
                    self.player_sessions[player_id] = session_id

            # Enhanced dual connection logging
            existing_websocket_count = len(self.player_websockets[player_id]) - 1  # -1 because we just added one
            existing_sse_count = len(self.active_sse_connections.get(player_id, []))
            total_connections = existing_websocket_count + existing_sse_count + 1  # +1 for the new connection

            logger.info(
                f"WebSocket connected for player {player_id}",
                connection_id=connection_id,
                session_id=session_id,
                existing_websocket_connections=existing_websocket_count,
                existing_sse_connections=existing_sse_count,
                total_connections=total_connections,
                is_dual_connection=existing_sse_count > 0,
                connection_type="websocket",
            )

            # Get player and room information
            player = self._get_player(player_id)
            if not player:
                if self.persistence is None:
                    logger.warning("Persistence not available, connecting without player tracking", player_id=player_id)
                else:
                    logger.error("Player not found", player_id=player_id)
                    return False
            else:
                canonical_room_id = getattr(player, "current_room_id", None)
                if canonical_room_id:
                    self.room_manager.subscribe_to_room(player_id, canonical_room_id)

                # Track player presence - always call _track_player_connected for WebSocket connections
                # to ensure connection messages are broadcast to other players
                if player_id not in self.online_players:
                    await self._track_player_connected(player_id, player, "websocket")
                else:
                    logger.info(
                        f"Player {player_id} already tracked as online, but broadcasting connection message for WebSocket"
                    )
                    # Still broadcast connection message even if player is already tracked
                    await self._broadcast_connection_message(player_id, player)

        except Exception as e:
            logger.error("Error connecting WebSocket", player_id=player_id, error=str(e), exc_info=True)
            return False

        # Track performance metrics
        duration_ms = (time.time() - start_time) * 1000
        self.performance_stats["connection_establishment_times"].append(("websocket", duration_ms))
        self.performance_stats["total_connections_established"] += 1

        # Keep only last 1000 entries to prevent memory growth
        if len(self.performance_stats["connection_establishment_times"]) > 1000:
            self.performance_stats["connection_establishment_times"] = self.performance_stats[
                "connection_establishment_times"
            ][-1000:]

        return True

    async def disconnect_websocket(self, player_id: str, is_force_disconnect: bool = False):
        """
        Disconnect all WebSocket connections for a player.

        Args:
            player_id: The player's ID
            is_force_disconnect: If True, don't broadcast player_left_game
        """
        try:
            logger.info(
                f"🔍 DEBUG: Starting WebSocket disconnect for player {player_id}, force_disconnect={is_force_disconnect}"
            )

            if player_id in self.player_websockets:
                connection_ids = self.player_websockets[player_id].copy()  # Copy to avoid modification during iteration
                logger.info(
                    f"🔍 DEBUG: Found {len(connection_ids)} WebSocket connections for player {player_id}: {connection_ids}"
                )

                # Disconnect all WebSocket connections for this player
                for connection_id in connection_ids:
                    if connection_id in self.active_websockets:
                        websocket = self.active_websockets[connection_id]
                        logger.info("DEBUG: Closing WebSocket", connection_id=connection_id, player_id=player_id)
                        # Properly close the WebSocket connection
                        try:
                            await asyncio.wait_for(websocket.close(code=1000, reason="Connection closed"), timeout=2.0)
                            logger.info(
                                f"🔍 DEBUG: Successfully closed WebSocket {connection_id} for player {player_id}"
                            )
                        except (TimeoutError, Exception) as e:
                            logger.warning(
                                "Error closing WebSocket",
                                connection_id=connection_id,
                                player_id=player_id,
                                error=str(e),
                            )
                        del self.active_websockets[connection_id]

                    # Clean up connection metadata
                    if connection_id in self.connection_metadata:
                        del self.connection_metadata[connection_id]

                # Remove player from websocket tracking
                del self.player_websockets[player_id]

                # Check if we need to track disconnection (outside of disconnect_lock to avoid deadlock)
                should_track_disconnect = False
                if not is_force_disconnect and not self.has_sse_connection(player_id):
                    # Check if disconnect needs to be processed without holding the disconnect_lock
                    async with self.processed_disconnect_lock:
                        if player_id not in self.processed_disconnects:
                            self.processed_disconnects.add(player_id)
                            should_track_disconnect = True
                        else:
                            logger.debug("Disconnect already processed, skipping", player_id=player_id)

                    # Track disconnect outside of disconnect_lock to avoid deadlock
                    if should_track_disconnect:
                        await self._track_player_disconnected(player_id)

                # Unsubscribe from all rooms only if it's not a force disconnect and no other connections
                # During reconnections, we want to preserve room membership
                if not is_force_disconnect and not self.has_sse_connection(player_id):
                    self.room_manager.remove_player_from_all_rooms(player_id)
                else:
                    logger.debug(
                        f"🔍 DEBUG: Preserving room membership for player {player_id} during force disconnect (reconnection)"
                    )

                # Clean up rate limiting data only if no other connections
                if not self.has_sse_connection(player_id):
                    self.rate_limiter.remove_player_data(player_id)
                    # Clean up pending messages
                    self.message_queue.remove_player_messages(player_id)
                    # Clean up last seen data
                    if player_id in self.last_seen:
                        del self.last_seen[player_id]

                logger.info("WebSocket disconnected", player_id=player_id)

        except Exception as e:
            logger.error("Error during WebSocket disconnect", player_id=player_id, error=str(e), exc_info=True)

    async def force_disconnect_player(self, player_id: str):
        """
        Force disconnect a player from all connections (WebSocket and SSE).

        Args:
            player_id: The player's ID
        """
        try:
            logger.info("Force disconnecting player from all connections", player_id=player_id)

            # Disconnect WebSocket if active (without broadcasting player_left_game)
            if player_id in self.player_websockets:
                await self.disconnect_websocket(player_id, is_force_disconnect=True)

            # Disconnect SSE if active
            if player_id in self.active_sse_connections:
                self.disconnect_sse(player_id, is_force_disconnect=True)

            logger.info("Player force disconnected from all connections", player_id=player_id)
        except Exception as e:
            logger.error("Error force disconnecting player", player_id=player_id, error=str(e), exc_info=True)

    async def disconnect_connection_by_id(self, connection_id: str) -> bool:
        """
        Disconnect a specific connection by its ID.

        Args:
            connection_id: The connection ID to disconnect

        Returns:
            bool: True if connection was found and disconnected, False otherwise
        """
        try:
            if connection_id not in self.connection_metadata:
                logger.warning("Connection not found in metadata", connection_id=connection_id)
                return False

            metadata = self.connection_metadata[connection_id]
            player_id = metadata.player_id
            connection_type = metadata.connection_type

            logger.info(
                "Disconnecting connection",
                connection_type=connection_type,
                connection_id=connection_id,
                player_id=player_id,
            )

            if connection_type == "websocket":
                # Disconnect WebSocket connection
                if connection_id in self.active_websockets:
                    websocket = self.active_websockets[connection_id]
                    logger.info("DEBUG: Closing WebSocket by connection ID", connection_id=connection_id)
                    try:
                        await websocket.close(code=1000, reason="Connection closed")
                        logger.info(
                            "DEBUG: Successfully closed WebSocket by connection ID", connection_id=connection_id
                        )
                    except Exception as e:
                        logger.warning("Error closing WebSocket", connection_id=connection_id, error=str(e))
                    del self.active_websockets[connection_id]

                # Remove from player's connection list
                if player_id in self.player_websockets and connection_id in self.player_websockets[player_id]:
                    self.player_websockets[player_id].remove(connection_id)
                    # If no more connections, remove the player entry
                    if not self.player_websockets[player_id]:
                        del self.player_websockets[player_id]

            elif connection_type == "sse":
                # Disconnect SSE connection
                if player_id in self.active_sse_connections and connection_id in self.active_sse_connections[player_id]:
                    self.active_sse_connections[player_id].remove(connection_id)
                    # If no more connections, remove the player entry
                    if not self.active_sse_connections[player_id]:
                        del self.active_sse_connections[player_id]

            # Clean up connection metadata
            del self.connection_metadata[connection_id]

            # Check if player has any remaining connections
            has_websocket = self.has_websocket_connection(player_id)
            has_sse = self.has_sse_connection(player_id)

            # If no connections remain, clean up player data
            if not has_websocket and not has_sse:
                self.rate_limiter.remove_player_data(player_id)
                self.message_queue.remove_player_messages(player_id)
                if player_id in self.last_seen:
                    del self.last_seen[player_id]
                # Remove from room subscriptions
                self.room_manager.remove_player_from_all_rooms(player_id)
                logger.info("Player has no remaining connections, cleaned up player data", player_id=player_id)

            logger.info(
                "Successfully disconnected connection", connection_type=connection_type, connection_id=connection_id
            )
            return True

        except Exception as e:
            logger.error("Error disconnecting connection", connection_id=connection_id, error=str(e), exc_info=True)
            return False

    async def disconnect_websocket_connection(self, player_id: str, connection_id: str) -> bool:
        """
        Disconnect a specific WebSocket connection for a player.

        Args:
            player_id: The player's ID
            connection_id: The WebSocket connection ID to disconnect

        Returns:
            bool: True if connection was found and disconnected, False otherwise
        """
        try:
            # Verify the connection belongs to this player
            if connection_id not in self.connection_metadata:
                logger.warning("Connection not found in metadata", connection_id=connection_id)
                return False

            metadata = self.connection_metadata[connection_id]
            if metadata.player_id != player_id or metadata.connection_type != "websocket":
                logger.warning(
                    f"Connection {connection_id} does not belong to player {player_id} or is not a WebSocket"
                )
                return False

            return await self.disconnect_connection_by_id(connection_id)

        except Exception as e:
            logger.error(
                f"Error disconnecting WebSocket connection {connection_id} for player {player_id}: {e}", exc_info=True
            )
            return False

    def disconnect_sse_connection(self, player_id: str, connection_id: str) -> bool:
        """
        Disconnect a specific SSE connection for a player.

        Args:
            player_id: The player's ID
            connection_id: The SSE connection ID to disconnect

        Returns:
            bool: True if connection was found and disconnected, False otherwise
        """
        try:
            # Verify the connection belongs to this player
            if connection_id not in self.connection_metadata:
                logger.warning("Connection not found in metadata", connection_id=connection_id)
                return False

            metadata = self.connection_metadata[connection_id]
            if metadata.player_id != player_id or metadata.connection_type != "sse":
                logger.warning(
                    f"Connection {connection_id} does not belong to player {player_id} or is not an SSE connection"
                )
                return False

            # Disconnect SSE connection
            if player_id in self.active_sse_connections and connection_id in self.active_sse_connections[player_id]:
                self.active_sse_connections[player_id].remove(connection_id)
                # If no more connections, remove the player entry
                if not self.active_sse_connections[player_id]:
                    del self.active_sse_connections[player_id]

            # Clean up connection metadata
            del self.connection_metadata[connection_id]

            # Check if player has any remaining connections
            has_websocket = self.has_websocket_connection(player_id)
            has_sse = self.has_sse_connection(player_id)

            # If no connections remain, clean up player data
            if not has_websocket and not has_sse:
                self.rate_limiter.remove_player_data(player_id)
                self.message_queue.remove_player_messages(player_id)
                if player_id in self.last_seen:
                    del self.last_seen[player_id]
                # Remove from room subscriptions
                self.room_manager.remove_player_from_all_rooms(player_id)
                logger.info("Player has no remaining connections, cleaned up player data", player_id=player_id)

            logger.info("Successfully disconnected SSE connection", connection_id=connection_id)
            return True

        except Exception as e:
            logger.error(
                f"Error disconnecting SSE connection {connection_id} for player {player_id}: {e}", exc_info=True
            )
            return False

    async def connect_sse(self, player_id: str, session_id: str | None = None) -> str:
        """
        Connect an SSE connection for a player.

        Args:
            player_id: The player's ID
            session_id: Optional session ID for tracking new game client sessions

        Returns:
            str: The connection ID
        """
        start_time = time.time()
        # For dual connection system, we allow multiple SSE connections
        # No need to terminate existing connections

        connection_id = str(uuid.uuid4())

        # Add the new connection to the player's SSE connection list
        if player_id not in self.active_sse_connections:
            self.active_sse_connections[player_id] = []
        self.active_sse_connections[player_id].append(connection_id)

        # Create connection metadata
        current_time = time.time()
        self.connection_metadata[connection_id] = ConnectionMetadata(
            connection_id=connection_id,
            player_id=player_id,
            connection_type="sse",
            established_at=current_time,
            last_seen=current_time,
            is_healthy=True,
            session_id=session_id,
        )

        # Track connection in session
        if session_id:
            if session_id not in self.session_connections:
                self.session_connections[session_id] = []
            self.session_connections[session_id].append(connection_id)
            # Only update player session if they don't have one or if this is the same session
            if player_id not in self.player_sessions or self.player_sessions[player_id] == session_id:
                self.player_sessions[player_id] = session_id

        # Enhanced dual connection logging
        existing_sse_count = len(self.active_sse_connections[player_id]) - 1  # -1 because we just added one
        existing_websocket_count = len(self.player_websockets.get(player_id, []))
        total_connections = existing_websocket_count + existing_sse_count + 1  # +1 for the new connection

        logger.info(
            f"SSE connected for player {player_id}",
            connection_id=connection_id,
            session_id=session_id,
            existing_websocket_connections=existing_websocket_count,
            existing_sse_connections=existing_sse_count,
            total_connections=total_connections,
            is_dual_connection=existing_websocket_count > 0,
            connection_type="sse",
        )

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
                    await self._track_player_connected(player_id, player, "sse")
                else:
                    logger.info(
                        "Player already tracked as online, skipping _track_player_connected", player_id=player_id
                    )
            elif self.persistence is None:
                logger.warning("Persistence not available, SSE connecting without player tracking", player_id=player_id)

        except Exception as e:
            logger.error("Error tracking SSE presence", player_id=player_id, error=str(e), exc_info=True)

        # Track performance metrics
        duration_ms = (time.time() - start_time) * 1000
        self.performance_stats["connection_establishment_times"].append(("sse", duration_ms))
        self.performance_stats["total_connections_established"] += 1

        # Keep only last 1000 entries to prevent memory growth
        if len(self.performance_stats["connection_establishment_times"]) > 1000:
            self.performance_stats["connection_establishment_times"] = self.performance_stats[
                "connection_establishment_times"
            ][-1000:]

        return connection_id

    async def handle_new_game_session(self, player_id: str, new_session_id: str) -> dict[str, Any]:
        """
        Handle a new game session by disconnecting existing connections.

        This method implements the requirement that when a user logs in through
        a new game client session, existing connections should be disconnected.

        Args:
            player_id: The player's ID
            new_session_id: The new session ID

        Returns:
            dict: Session handling results with detailed information
        """
        session_results = {
            "player_id": player_id,
            "new_session_id": new_session_id,
            "previous_session_id": None,
            "connections_disconnected": 0,
            "websocket_connections": 0,
            "sse_connections": 0,
            "success": False,
            "errors": [],
        }

        try:
            # Enhanced session logging
            existing_websocket_count = len(self.player_websockets.get(player_id, []))
            existing_sse_count = len(self.active_sse_connections.get(player_id, []))
            total_existing_connections = existing_websocket_count + existing_sse_count

            logger.info(
                f"Handling new game session {new_session_id} for player {player_id}",
                new_session_id=new_session_id,
                existing_websocket_connections=existing_websocket_count,
                existing_sse_connections=existing_sse_count,
                total_existing_connections=total_existing_connections,
                will_disconnect_all=True,
            )

            # Check if player has an existing session
            if player_id in self.player_sessions:
                session_results["previous_session_id"] = self.player_sessions[player_id]
                logger.info(
                    "Player had existing session",
                    player_id=player_id,
                    previous_session_id=session_results["previous_session_id"],
                )

            # Disconnect all existing WebSocket connections
            if player_id in self.player_websockets:
                connection_ids = self.player_websockets[player_id].copy()
                session_results["websocket_connections"] = len(connection_ids)

                for connection_id in connection_ids:
                    if connection_id in self.active_websockets:
                        websocket = self.active_websockets[connection_id]
                        try:
                            # Only try to close if WebSocket is actually connected
                            try:
                                is_connected = websocket.client_state.name == "CONNECTED"
                            except (AttributeError, Exception):
                                # If we can't check state, assume it's not connected
                                is_connected = False
                                logger.debug(
                                    f"Could not check state for WebSocket {connection_id}, assuming disconnected"
                                )

                            if is_connected:
                                logger.info(
                                    f"🔍 DEBUG: Closing WebSocket {connection_id} due to new game session for player {player_id}"
                                )
                                await websocket.close(code=1000, reason="New game session established")
                                logger.info(
                                    f"🔍 DEBUG: Successfully closed WebSocket {connection_id} due to new game session"
                                )
                                session_results["connections_disconnected"] += 1
                            else:
                                logger.debug(
                                    "Skipping close for WebSocket (not connected)", connection_id=connection_id
                                )
                                session_results["connections_disconnected"] += 1  # Count as disconnected
                        except Exception as e:
                            # Don't let close errors propagate - log and continue
                            logger.debug(
                                "Non-critical error closing WebSocket", connection_id=connection_id, error=str(e)
                            )
                            session_results["connections_disconnected"] += 1  # Still count as disconnected
                        # Clean up from active websockets regardless of close success
                        try:
                            del self.active_websockets[connection_id]
                        except KeyError:
                            pass  # Already removed, that's fine

                    # Clean up connection metadata
                    if connection_id in self.connection_metadata:
                        del self.connection_metadata[connection_id]

                # Remove player from websocket tracking
                try:
                    del self.player_websockets[player_id]
                except KeyError:
                    pass  # Already removed

            # Disconnect all existing SSE connections
            if player_id in self.active_sse_connections:
                connection_ids = self.active_sse_connections[player_id].copy()
                session_results["sse_connections"] = len(connection_ids)

                for connection_id in connection_ids:
                    # Clean up connection metadata
                    if connection_id in self.connection_metadata:
                        del self.connection_metadata[connection_id]
                    session_results["connections_disconnected"] += 1

                # Remove player from SSE tracking
                try:
                    del self.active_sse_connections[player_id]
                except KeyError:
                    pass  # Already removed

            # Clean up old session tracking
            if player_id in self.player_sessions:
                old_session_id = self.player_sessions[player_id]
                if old_session_id in self.session_connections:
                    try:
                        del self.session_connections[old_session_id]
                    except KeyError:
                        pass  # Already removed

            # Update session tracking
            self.player_sessions[player_id] = new_session_id
            self.session_connections[new_session_id] = []

            # Clean up player data
            self.rate_limiter.remove_player_data(player_id)
            self.message_queue.remove_player_messages(player_id)
            if player_id in self.last_seen:
                del self.last_seen[player_id]

            # Remove from room subscriptions
            self.room_manager.remove_player_from_all_rooms(player_id)

            session_results["success"] = True
            logger.info(
                f"Disconnected {session_results['connections_disconnected']} connections for new game session {new_session_id} of player {player_id}"
            )

        except Exception as e:
            error_msg = f"Error handling new game session for player {player_id}: {e}"
            logger.error(error_msg, exc_info=True)
            session_results["errors"].append(error_msg)
            session_results["success"] = False

        return session_results

    def get_player_session(self, player_id: str) -> str | None:
        """
        Get the current session ID for a player.

        Args:
            player_id: The player's ID

        Returns:
            str | None: The current session ID, or None if no session
        """
        return self.player_sessions.get(player_id)

    def get_session_connections(self, session_id: str) -> list[str]:
        """
        Get all connection IDs for a session.

        Args:
            session_id: The session ID

        Returns:
            list[str]: List of connection IDs for the session
        """
        return self.session_connections.get(session_id, [])

    def validate_session(self, player_id: str, session_id: str) -> bool:
        """
        Validate that a session ID matches the player's current session.

        Args:
            player_id: The player's ID
            session_id: The session ID to validate

        Returns:
            bool: True if the session is valid, False otherwise
        """
        current_session = self.player_sessions.get(player_id)
        return current_session == session_id

    def get_session_stats(self) -> dict[str, Any]:
        """
        Get session management statistics.

        Returns:
            dict: Session statistics
        """
        return {
            "total_sessions": len(self.session_connections),
            "total_players_with_sessions": len(self.player_sessions),
            "sessions_with_connections": len([s for s in self.session_connections.values() if s]),
            "average_connections_per_session": (
                sum(len(conns) for conns in self.session_connections.values()) / len(self.session_connections)
                if self.session_connections
                else 0
            ),
        }

    def disconnect_sse(self, player_id: str, is_force_disconnect: bool = False):
        """
        Disconnect all SSE connections for a player.

        Args:
            player_id: The player's ID
            is_force_disconnect: If True, don't broadcast player_left_game
        """
        try:
            if player_id in self.active_sse_connections:
                connection_ids = self.active_sse_connections[
                    player_id
                ].copy()  # Copy to avoid modification during iteration

                # Clean up connection metadata for all SSE connections
                for connection_id in connection_ids:
                    if connection_id in self.connection_metadata:
                        del self.connection_metadata[connection_id]

                # Remove player from SSE tracking
                del self.active_sse_connections[player_id]

            # Only clean up player data if no other connections exist
            if not self.has_websocket_connection(player_id):
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

            logger.info("SSE disconnected", player_id=player_id)
        except Exception as e:
            logger.error("Error during SSE disconnect", player_id=player_id, error=str(e), exc_info=True)

    def mark_player_seen(self, player_id: str):
        """Update last-seen timestamp for a player."""
        try:
            self.last_seen[player_id] = time.time()
        except Exception as e:
            logger.error("Error marking player seen", player_id=player_id, error=str(e))

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
                logger.info("Pruned stale players", stale_ids=stale_ids)
        except Exception as e:
            logger.error("Error pruning stale players", error=str(e))

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
                connection_age = now_ts - timestamp
                if connection_age > self.memory_monitor.max_connection_age:
                    logger.info(
                        f"🔍 DEBUG: Connection {connection_id} is stale (age: {connection_age:.1f}s, max: {self.memory_monitor.max_connection_age}s)"
                    )
                    stale_connections.append(connection_id)

            for connection_id in stale_connections:
                if connection_id in self.active_websockets:
                    try:
                        websocket = self.active_websockets[connection_id]
                        logger.info("DEBUG: Closing stale WebSocket due to timeout", connection_id=connection_id)
                        await websocket.close(code=1000, reason="Connection timeout")
                        logger.info("Successfully closed stale WebSocket", connection_id=connection_id)
                    except Exception as e:
                        logger.warning("Error closing stale connection", connection_id=connection_id, error=str(e))
                    del self.active_websockets[connection_id]
                del self.connection_timestamps[connection_id]
                cleanup_stats["stale_connections"] += 1

            # Update cleanup stats
            self.cleanup_stats["cleanups_performed"] += 1
            self.memory_monitor.update_cleanup_time()

            if any(cleanup_stats.values()):
                logger.info("Memory cleanup completed", stale_connections=cleanup_stats["stale_connections"])

        except Exception as e:
            logger.error("Error cleaning up orphaned data", error=str(e), exc_info=True)

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

    async def send_personal_message(self, player_id: str, event: dict[str, Any]) -> dict[str, Any]:
        """
        Send a personal message to a player across all active connections.

        Args:
            player_id: The player's ID
            event: The event data to send

        Returns:
            dict: Delivery status with detailed information:
                {
                    "success": bool,
                    "websocket_delivered": int,
                    "websocket_failed": int,
                    "sse_delivered": bool,
                    "total_connections": int,
                    "active_connections": int
                }
        """
        delivery_status = {
            "success": False,
            "websocket_delivered": 0,
            "websocket_failed": 0,
            "sse_delivered": False,
            "total_connections": 0,
            "active_connections": 0,
        }

        try:
            # Convert UUIDs to strings for JSON serialization
            serializable_event = self._convert_uuids_to_strings(event)

            # Debug logging to see what's being sent
            if event.get("event_type") == "game_state":
                logger.info("Sending game_state event", player_id=player_id, event_data=serializable_event)

            # Count total connections
            websocket_count = len(self.player_websockets.get(player_id, []))
            sse_count = len(self.active_sse_connections.get(player_id, []))
            delivery_status["total_connections"] = websocket_count + sse_count

            # Try WebSocket connections first
            if player_id in self.player_websockets:
                connection_ids = self.player_websockets[player_id].copy()  # Copy to avoid modification during iteration
                for connection_id in connection_ids:
                    if connection_id in self.active_websockets:
                        websocket = self.active_websockets[connection_id]
                        try:
                            # Check if WebSocket is still open by attempting to send
                            await websocket.send_json(serializable_event)
                            delivery_status["websocket_delivered"] += 1
                            delivery_status["active_connections"] += 1
                        except Exception as ws_error:
                            # WebSocket is closed or in an invalid state
                            logger.warning(
                                f"WebSocket send failed for player {player_id} connection {connection_id}: {ws_error}"
                            )
                            delivery_status["websocket_failed"] += 1
                            # Clean up the dead WebSocket connection
                            await self._cleanup_dead_websocket(player_id, connection_id)
                            # Continue to other connections

            # Add to pending messages for SSE connections
            if self.has_sse_connection(player_id):
                if player_id not in self.message_queue.pending_messages:
                    self.message_queue.pending_messages[player_id] = []
                self.message_queue.pending_messages[player_id].append(serializable_event)
                delivery_status["sse_delivered"] = True
                delivery_status["active_connections"] += len(self.active_sse_connections.get(player_id, []))

            # If no active connections, queue the message for later delivery
            if delivery_status["active_connections"] == 0:
                if player_id not in self.message_queue.pending_messages:
                    self.message_queue.pending_messages[player_id] = []
                self.message_queue.pending_messages[player_id].append(serializable_event)
                delivery_status["sse_delivered"] = True  # Mark as queued for later delivery

            # Determine overall success - true if message was delivered to active connections
            # OR if message was queued for later delivery (but not if WebSocket failed)
            delivery_status["success"] = (
                delivery_status["websocket_delivered"] > 0
                or (delivery_status["sse_delivered"] and delivery_status["active_connections"] > 0)
                or (
                    delivery_status["active_connections"] == 0
                    and delivery_status["sse_delivered"]
                    and delivery_status["websocket_failed"] == 0
                )
            )

            logger.debug("Message delivery status", player_id=player_id, delivery_status=delivery_status)
            return delivery_status

        except Exception as e:
            logger.error("Failed to send personal message", player_id=player_id, error=str(e))
            delivery_status["success"] = False
            return delivery_status

    def get_message_delivery_stats(self, player_id: str) -> dict[str, Any]:
        """
        Get message delivery statistics for a player.

        Args:
            player_id: The player's ID

        Returns:
            dict: Message delivery statistics
        """
        stats = {
            "player_id": player_id,
            "websocket_connections": len(self.player_websockets.get(player_id, [])),
            "sse_connections": len(self.active_sse_connections.get(player_id, [])),
            "total_connections": 0,
            "pending_messages": len(self.message_queue.pending_messages.get(player_id, [])),
            "has_active_connections": False,
        }

        stats["total_connections"] = stats["websocket_connections"] + stats["sse_connections"]
        stats["has_active_connections"] = stats["total_connections"] > 0

        return stats

    async def check_connection_health(self, player_id: str) -> dict[str, Any]:
        """
        Check the health of all connections for a player.

        Args:
            player_id: The player's ID

        Returns:
            dict: Connection health information
        """
        health_status = {
            "player_id": player_id,
            "websocket_healthy": 0,
            "websocket_unhealthy": 0,
            "sse_healthy": 0,
            "overall_health": "unknown",
        }

        try:
            # Check WebSocket connections
            if player_id in self.player_websockets:
                connection_ids = self.player_websockets[player_id].copy()
                for connection_id in connection_ids:
                    if connection_id in self.active_websockets:
                        websocket = self.active_websockets[connection_id]
                        try:
                            # Check WebSocket health by checking its state
                            if websocket.client_state.name == "CONNECTED":
                                health_status["websocket_healthy"] += 1
                            else:
                                raise Exception("WebSocket not connected")
                        except Exception:
                            health_status["websocket_unhealthy"] += 1
                            # Clean up unhealthy connection
                            await self._cleanup_dead_websocket(player_id, connection_id)

            # Check SSE connections (assume healthy if they exist)
            health_status["sse_healthy"] = len(self.active_sse_connections.get(player_id, []))

            # Determine overall health
            total_healthy = health_status["websocket_healthy"] + health_status["sse_healthy"]
            total_connections = total_healthy + health_status["websocket_unhealthy"]

            if total_connections == 0:
                health_status["overall_health"] = "no_connections"
            elif health_status["websocket_unhealthy"] == 0:
                health_status["overall_health"] = "healthy"
            elif total_healthy > 0:
                health_status["overall_health"] = "degraded"
            else:
                health_status["overall_health"] = "unhealthy"

            return health_status

        except Exception as e:
            logger.error("Error checking connection health", player_id=player_id, error=str(e))
            health_status["overall_health"] = "error"
            return health_status

    async def cleanup_dead_connections(self, player_id: str | None = None) -> dict[str, Any]:
        """
        Clean up dead connections for a specific player or all players.

        Args:
            player_id: Optional player ID to clean up. If None, cleans up all players.

        Returns:
            dict: Cleanup results
        """
        cleanup_results = {"players_checked": 0, "connections_cleaned": 0, "errors": []}

        try:
            if player_id:
                # Clean up specific player
                players_to_check = [player_id]
            else:
                # Clean up all players
                players_to_check = list(
                    set(list(self.player_websockets.keys()) + list(self.active_sse_connections.keys()))
                )

            cleanup_results["players_checked"] = len(players_to_check)

            for pid in players_to_check:
                try:
                    # Check WebSocket connections
                    if pid in self.player_websockets:
                        connection_ids = self.player_websockets[pid].copy()
                        for connection_id in connection_ids:
                            if connection_id in self.active_websockets:
                                websocket = self.active_websockets[connection_id]
                                try:
                                    # Check WebSocket health by checking its state
                                    if websocket.client_state.name != "CONNECTED":
                                        raise Exception("WebSocket not connected")
                                except Exception:
                                    # Connection is dead, clean it up
                                    await self._cleanup_dead_websocket(pid, connection_id)
                                    cleanup_results["connections_cleaned"] += 1
                except Exception as e:
                    cleanup_results["errors"].append(f"Error cleaning player {pid}: {e}")

            logger.info("Connection cleanup completed", cleanup_results=cleanup_results)
            return cleanup_results

        except Exception as e:
            logger.error("Error during connection cleanup", error=str(e))
            cleanup_results["errors"].append(str(e))
            return cleanup_results

    async def _cleanup_dead_websocket(self, player_id: str, connection_id: str):
        """
        Clean up a dead WebSocket connection.

        Args:
            player_id: The player's ID
            connection_id: The connection ID to clean up
        """
        try:
            # Close the WebSocket if it's still in active_websockets
            if connection_id in self.active_websockets:
                websocket = self.active_websockets[connection_id]
                logger.info("Closing dead WebSocket", connection_id=connection_id, player_id=player_id)
                try:
                    await asyncio.wait_for(websocket.close(code=1000, reason="Connection cleaned up"), timeout=2.0)
                    logger.info("Successfully closed dead WebSocket", connection_id=connection_id, player_id=player_id)
                except (TimeoutError, Exception) as e:
                    logger.warning(
                        "Error closing dead WebSocket", connection_id=connection_id, player_id=player_id, error=str(e)
                    )
                del self.active_websockets[connection_id]

            # Remove from player's connection list
            if player_id in self.player_websockets and connection_id in self.player_websockets[player_id]:
                self.player_websockets[player_id].remove(connection_id)
                # If no more connections, remove the player entry
                if not self.player_websockets[player_id]:
                    del self.player_websockets[player_id]

            # Remove connection metadata
            if connection_id in self.connection_metadata:
                del self.connection_metadata[connection_id]

            logger.info("Cleaned up dead WebSocket connection", connection_id=connection_id, player_id=player_id)
        except Exception as e:
            logger.error(
                "Error cleaning up dead WebSocket", connection_id=connection_id, player_id=player_id, error=str(e)
            )

    async def broadcast_to_room(
        self, room_id: str, event: dict[str, Any], exclude_player: str | None = None
    ) -> dict[str, Any]:
        """
        Broadcast a message to all players in a room.

        Args:
            room_id: The room's ID
            event: The event data to send
            exclude_player: Player ID to exclude from broadcast

        Returns:
            dict: Broadcast delivery statistics
        """
        targets = self.room_manager.get_room_subscribers(room_id)

        broadcast_stats = {
            "room_id": room_id,
            "total_targets": len(targets),
            "excluded_players": 0,
            "successful_deliveries": 0,
            "failed_deliveries": 0,
            "delivery_details": {},
        }

        # Debug logging for self-message exclusion
        logger.debug("broadcast_to_room", room_id=room_id, exclude_player=exclude_player)
        logger.debug("broadcast_to_room targets", targets=targets)

        for pid in targets:
            if pid != exclude_player:
                logger.debug("broadcast_to_room sending to player", player_id=pid)
                delivery_status = await self.send_personal_message(pid, event)

                # Track delivery statistics
                broadcast_stats["delivery_details"][pid] = delivery_status
                if delivery_status["success"]:
                    broadcast_stats["successful_deliveries"] += 1
                else:
                    broadcast_stats["failed_deliveries"] += 1
            else:
                logger.debug("broadcast_to_room: excluding player (self-message exclusion)", player_id=pid)
                broadcast_stats["excluded_players"] += 1

        logger.debug("broadcast_to_room: delivery stats for room", room_id=room_id, stats=broadcast_stats)
        return broadcast_stats

    async def broadcast_global(self, event: dict[str, Any], exclude_player: str | None = None) -> dict[str, Any]:
        """
        Broadcast a message to all connected players.

        Args:
            event: The event data to send
            exclude_player: Player ID to exclude from broadcast

        Returns:
            dict: Global broadcast delivery statistics
        """
        # Get all players with any type of connection (WebSocket or SSE)
        all_players = set(list(self.player_websockets.keys()) + list(self.active_sse_connections.keys()))

        global_stats = {
            "total_players": len(all_players),
            "excluded_players": 0,
            "successful_deliveries": 0,
            "failed_deliveries": 0,
            "delivery_details": {},
        }

        for player_id in all_players:
            if player_id != exclude_player:
                delivery_status = await self.send_personal_message(player_id, event)

                # Track delivery statistics
                global_stats["delivery_details"][player_id] = delivery_status
                if delivery_status["success"]:
                    global_stats["successful_deliveries"] += 1
                else:
                    global_stats["failed_deliveries"] += 1
            else:
                global_stats["excluded_players"] += 1

        logger.debug("broadcast_global: delivery stats", stats=global_stats)
        return global_stats

    async def broadcast_room_event(self, event_type: str, room_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """
        Broadcast a room-specific event to all players in the room.

        Args:
            event_type: Type of event (e.g., 'player_entered', 'player_left')
            room_id: Room ID to broadcast to
            data: Event data

        Returns:
            dict: Broadcast delivery statistics
        """
        try:
            # Import here to avoid circular imports
            from .envelope import build_event

            # Create event message
            event = build_event(event_type, data)

            # Broadcast to room
            return await self.broadcast_to_room(room_id, event)

        except Exception as e:
            logger.error("Error broadcasting room event", error=str(e), event_type=event_type, room_id=room_id)
            return {
                "room_id": room_id,
                "total_targets": 0,
                "excluded_players": 0,
                "successful_deliveries": 0,
                "failed_deliveries": 0,
                "delivery_details": {},
                "error": str(e),
            }

    async def broadcast_global_event(self, event_type: str, data: dict[str, Any]) -> dict[str, Any]:
        """
        Broadcast a global event to all connected players.

        Args:
            event_type: Type of event (e.g., 'game_tick')
            data: Event data

        Returns:
            dict: Broadcast delivery statistics
        """
        try:
            # Import here to avoid circular imports
            from .envelope import build_event

            # Create event message
            event = build_event(event_type, data)

            # Broadcast globally
            return await self.broadcast_global(event)

        except Exception as e:
            logger.error("Error broadcasting global event", error=str(e), event_type=event_type)
            return {
                "total_players": 0,
                "excluded_players": 0,
                "successful_deliveries": 0,
                "failed_deliveries": 0,
                "delivery_details": {},
                "error": str(e),
            }

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
            logger.warning("Persistence layer not initialized for player lookup", player_id=player_id)
            return None

        player = self.persistence.get_player(player_id)
        if player is None:
            # Fallback to get_player_by_name
            logger.info("Player not found by ID, trying by name", player_id=player_id)
            player = self.persistence.get_player_by_name(player_id)
            if player:
                logger.info("Player found by name", player_id=player_id)
            else:
                logger.warning("Player not found by name", player_id=player_id)
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

    async def _track_player_connected(self, player_id: str, player: Player, connection_type: str = "unknown"):
        """
        Track when a player connects.

        Args:
            player_id: The player's ID
            player: The player object
            connection_type: Type of connection ("websocket", "sse", "unknown")
        """
        try:
            # Check if player is already tracked as online
            is_new_connection = player_id not in self.online_players

            player_info = {
                "player_id": player_id,
                "player_name": getattr(player, "name", player_id),
                "level": getattr(player, "level", 1),
                "current_room_id": getattr(player, "current_room_id", None),
                "connected_at": time.time(),
                "connection_types": set(),
                "total_connections": 0,
            }

            # If player is already online, update existing info
            if not is_new_connection:
                existing_info = self.online_players[player_id]
                player_info["connected_at"] = existing_info.get("connected_at", time.time())
                player_info["connection_types"] = existing_info.get("connection_types", set())

            # Add the new connection type
            player_info["connection_types"].add(connection_type)
            player_info["total_connections"] = len(self.player_websockets.get(player_id, [])) + len(
                self.active_sse_connections.get(player_id, [])
            )

            self.online_players[player_id] = player_info
            self.mark_player_seen(player_id)

            # Only perform these actions for new connections (not additional connections)
            if is_new_connection:
                # Update last_active timestamp in database when player connects
                if self.persistence:
                    try:
                        from datetime import UTC, datetime

                        player.last_active = datetime.now(UTC)
                        self.persistence.save_player(player)
                        logger.debug("Updated last_active for player on connection", player_id=player_id)
                    except Exception as e:
                        logger.warning("Failed to update last_active for player", player_id=player_id, error=str(e))

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
                            logger.info(
                                "Player entered room via player_entered()", player_id=player_id, room_id=room_id
                            )
                        else:
                            logger.warning(
                                "Room not found when trying to add player", room_id=room_id, player_id=player_id
                            )

                    # Send initial game_state event to the player
                    await self._send_initial_game_state(player_id, player, room_id)

                    # Note: Removed duplicate player_entered_game event generation
                    # The room.player_entered() call above already triggers PlayerEnteredRoom events
                    # which are handled by the RealTimeEventHandler to create "enters the room" messages
                    # This eliminates duplicate "has entered the game" messages

                logger.info("Player presence tracked as connected (new connection)", player_id=player_id)
            else:
                logger.info(
                    "Player additional connection tracked", player_id=player_id, connection_type=connection_type
                )

        except Exception as e:
            logger.error("Error tracking player connection", error=str(e), exc_info=True)

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
                # Note: Removed duplicate player_entered_game event generation
                # The room.player_entered() call during connection setup already triggers
                # PlayerEnteredRoom events which are handled by the RealTimeEventHandler
                # This eliminates duplicate "has entered the game" messages for players
                # who are already tracked as online but connecting via additional channels
                logger.debug(
                    "Player already tracked as online, skipping duplicate connection message", player_id=player_id
                )

        except Exception as e:
            logger.error("Error broadcasting connection message", player_id=player_id, error=str(e), exc_info=True)

    async def _track_player_disconnected(self, player_id: str, connection_type: str | None = None):
        """
        Track when a player disconnects.

        Args:
            player_id: The player's ID
            connection_type: Type of connection being disconnected ("websocket", "sse", None for all)
        """
        try:
            # Check if player has any remaining connections
            has_websocket = self.has_websocket_connection(player_id)
            has_sse = self.has_sse_connection(player_id)
            has_any_connections = has_websocket or has_sse

            # If player still has connections, don't fully disconnect them
            if has_any_connections and connection_type:
                logger.info(
                    f"Player {player_id} still has connections, not fully disconnecting (disconnected {connection_type})"
                )
                return

            # Prevent duplicate disconnect events for the same player using async lock
            async with self.disconnect_lock:
                if player_id in self.disconnecting_players:
                    logger.debug(
                        "🔍 DEBUG: Player already being disconnected, skipping duplicate event", player_id=player_id
                    )
                    return

                # Mark player as being disconnected
                self.disconnecting_players.add(player_id)
                logger.debug("🔍 DEBUG: Marked player as disconnecting", player_id=player_id)

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
                        logger.debug("🔍 DEBUG: Removing ghost player from room", ghost_player=key, room_id=room_id)
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
                logger.info("🔍 DEBUG: Broadcasting player_left_game", player_id=player_id, room_id=room_id)
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

            logger.info("Player presence tracked as disconnected", player_id=player_id)

        except Exception as e:
            logger.error("Error tracking player disconnection", error=str(e), exc_info=True)
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
                    logger.debug("🔍 DEBUG: Found ghost players in room", room_id=room.id, ghost_players=ghost_players)
                    for ghost_player_id in ghost_players:
                        room._players.discard(ghost_player_id)
                        logger.debug(
                            "🔍 DEBUG: Removed ghost player from room", ghost_player_id=ghost_player_id, room_id=room.id
                        )

        except Exception as e:
            logger.error("Error cleaning up ghost players", error=str(e), exc_info=True)

    async def detect_and_handle_error_state(
        self, player_id: str, error_type: str, error_details: str, connection_id: str | None = None
    ) -> dict[str, Any]:
        """
        Detect when a client is in an error state and handle it appropriately.

        Args:
            player_id: The player's ID
            error_type: Type of error detected
            error_details: Detailed error information
            connection_id: Optional specific connection ID that caused the error

        Returns:
            dict: Error handling results with detailed information
        """
        error_results = {
            "player_id": player_id,
            "error_type": error_type,
            "error_details": error_details,
            "connection_id": connection_id,
            "connections_terminated": 0,
            "connections_kept": 0,
            "fatal_error": False,
            "success": False,
            "errors": [],
        }

        try:
            import json
            from datetime import datetime

            logger.error(
                "ERROR STATE DETECTED for player",
                player_id=player_id,
                error_type=error_type,
                error_details=error_details,
            )

            # Get detailed connection information
            websocket_connections = len(self.player_websockets.get(player_id, []))
            sse_connections = len(self.active_sse_connections.get(player_id, []))
            total_connections = websocket_connections + sse_connections

            # Get session information
            current_session = self.get_player_session(player_id)
            session_connections = self.get_session_connections(current_session) if current_session else []

            # Log the error state to a dedicated error log file
            error_log_entry = {
                "timestamp": datetime.now().isoformat(),
                "player_id": player_id,
                "error_type": error_type,
                "error_details": error_details,
                "connection_id": connection_id,
                "connections": {
                    "websocket_count": websocket_connections,
                    "sse_count": sse_connections,
                    "total_connections": total_connections,
                    "online": player_id in self.online_players,
                    "current_session": current_session,
                    "session_connections": len(session_connections),
                },
            }

            # Write to error log file using proper logging configuration
            from ..config import get_config
            from ..logging.enhanced_logging_config import _resolve_log_base

            config = get_config()
            log_base = config.logging.log_base
            environment = config.logging.environment

            resolved_log_base = _resolve_log_base(log_base)
            error_log_path = resolved_log_base / environment / "connection_errors.log"
            error_log_path.parent.mkdir(parents=True, exist_ok=True)

            with open(error_log_path, "a") as f:
                f.write(json.dumps(error_log_entry) + "\n")

            # Determine if this is a fatal error
            fatal_errors = [
                "CRITICAL_WEBSOCKET_ERROR",
                "CRITICAL_SSE_ERROR",
                "AUTHENTICATION_FAILURE",
                "SECURITY_VIOLATION",
                "MALFORMED_DATA",
                "PROTOCOL_VIOLATION",
            ]

            error_results["fatal_error"] = error_type in fatal_errors

            if error_results["fatal_error"]:
                logger.error("FATAL ERROR: Terminating all connections for player", player_id=player_id)

                # Terminate all connections for the player
                await self.force_disconnect_player(player_id)
                error_results["connections_terminated"] = total_connections
                error_results["connections_kept"] = 0

            elif connection_id:
                # Handle connection-specific error (non-fatal)
                logger.warning(
                    f"Connection-specific error: Terminating connection {connection_id} for player {player_id}"
                )

                # Try to disconnect the specific connection
                if await self.disconnect_connection_by_id(connection_id):
                    error_results["connections_terminated"] = 1
                    error_results["connections_kept"] = total_connections - 1
                else:
                    error_results["errors"].append(f"Failed to disconnect connection {connection_id}")
                    error_results["connections_kept"] = total_connections

            else:
                # Non-fatal error, keep all connections alive
                logger.warning("Non-critical error: Keeping all connections alive for player", player_id=player_id)
                error_results["connections_terminated"] = 0
                error_results["connections_kept"] = total_connections

            error_results["success"] = True
            logger.info("Error handling completed for player", player_id=player_id, error_results=error_results)

        except Exception as e:
            error_msg = f"Error in detect_and_handle_error_state for {player_id}: {e}"
            logger.error(error_msg, exc_info=True)
            error_results["errors"].append(error_msg)
            error_results["success"] = False

        return error_results

    async def handle_websocket_error(
        self, player_id: str, connection_id: str, error_type: str, error_details: str
    ) -> dict[str, Any]:
        """
        Handle WebSocket-specific errors.

        Args:
            player_id: The player's ID
            connection_id: The WebSocket connection ID
            error_type: Type of WebSocket error
            error_details: Detailed error information

        Returns:
            dict: Error handling results
        """
        logger.warning(
            f"WebSocket error for player {player_id}, connection {connection_id}: {error_type} - {error_details}"
        )

        # Check if this is a critical WebSocket error
        critical_websocket_errors = [
            "CONNECTION_CLOSED_UNEXPECTEDLY",
            "INVALID_FRAME_FORMAT",
            "PROTOCOL_ERROR",
            "MESSAGE_TOO_LARGE",
        ]

        if error_type in critical_websocket_errors:
            return await self.detect_and_handle_error_state(
                player_id, "CRITICAL_WEBSOCKET_ERROR", f"{error_type}: {error_details}", connection_id
            )
        else:
            # Non-critical WebSocket error, just disconnect the specific connection
            return await self.detect_and_handle_error_state(
                player_id, "WEBSOCKET_ERROR", f"{error_type}: {error_details}", connection_id
            )

    async def handle_sse_error(
        self, player_id: str, connection_id: str, error_type: str, error_details: str
    ) -> dict[str, Any]:
        """
        Handle SSE-specific errors.

        Args:
            player_id: The player's ID
            connection_id: The SSE connection ID
            error_type: Type of SSE error
            error_details: Detailed error information

        Returns:
            dict: Error handling results
        """
        logger.warning(
            "SSE error for player",
            player_id=player_id,
            connection_id=connection_id,
            error_type=error_type,
            error_details=error_details,
        )

        # Check if this is a critical SSE error
        critical_sse_errors = ["STREAM_INTERRUPTED", "INVALID_EVENT_FORMAT", "CONNECTION_TIMEOUT", "BUFFER_OVERFLOW"]

        if error_type in critical_sse_errors:
            return await self.detect_and_handle_error_state(
                player_id, "CRITICAL_SSE_ERROR", f"{error_type}: {error_details}", connection_id
            )
        else:
            # Non-critical SSE error, just disconnect the specific connection
            return await self.detect_and_handle_error_state(
                player_id, "SSE_ERROR", f"{error_type}: {error_details}", connection_id
            )

    async def handle_authentication_error(self, player_id: str, error_type: str, error_details: str) -> dict[str, Any]:
        """
        Handle authentication-related errors.

        Args:
            player_id: The player's ID
            error_type: Type of authentication error
            error_details: Detailed error information

        Returns:
            dict: Error handling results
        """
        logger.error(
            "Authentication error for player", player_id=player_id, error_type=error_type, error_details=error_details
        )

        return await self.detect_and_handle_error_state(
            player_id, "AUTHENTICATION_FAILURE", f"{error_type}: {error_details}"
        )

    async def handle_security_violation(
        self, player_id: str, violation_type: str, violation_details: str
    ) -> dict[str, Any]:
        """
        Handle security violations.

        Args:
            player_id: The player's ID
            violation_type: Type of security violation
            violation_details: Detailed violation information

        Returns:
            dict: Error handling results
        """
        logger.error(
            "Security violation for player",
            player_id=player_id,
            violation_type=violation_type,
            violation_details=violation_details,
        )

        return await self.detect_and_handle_error_state(
            player_id, "SECURITY_VIOLATION", f"{violation_type}: {violation_details}"
        )

    async def recover_from_error(self, player_id: str, recovery_type: str = "FULL") -> dict[str, Any]:
        """
        Attempt to recover from an error state for a player.

        Args:
            player_id: The player's ID
            recovery_type: Type of recovery to attempt ("FULL", "CONNECTIONS_ONLY", "SESSION_ONLY")

        Returns:
            dict: Recovery results
        """
        recovery_results = {
            "player_id": player_id,
            "recovery_type": recovery_type,
            "success": False,
            "connections_restored": 0,
            "sessions_cleared": 0,
            "errors": [],
        }

        try:
            logger.info("Attempting recovery for player", recovery_type=recovery_type, player_id=player_id)

            if recovery_type in ["FULL", "CONNECTIONS_ONLY"]:
                # Clean up any dead connections
                cleanup_results = await self.cleanup_dead_connections(player_id)
                recovery_results["connections_restored"] = cleanup_results.get("connections_cleaned", 0)

            if recovery_type in ["FULL", "SESSION_ONLY"]:
                # Clear session data if needed
                if player_id in self.player_sessions:
                    old_session = self.player_sessions[player_id]
                    if old_session in self.session_connections:
                        del self.session_connections[old_session]
                    del self.player_sessions[player_id]
                    recovery_results["sessions_cleared"] = 1

            recovery_results["success"] = True
            logger.info("Recovery completed for player", player_id=player_id, recovery_results=recovery_results)

        except Exception as e:
            error_msg = f"Error during recovery for player {player_id}: {e}"
            logger.error(error_msg, exc_info=True)
            recovery_results["errors"].append(error_msg)
            recovery_results["success"] = False

        return recovery_results

    def get_player_presence_info(self, player_id: str) -> dict[str, Any]:
        """
        Get detailed presence information for a player.

        Args:
            player_id: The player's ID

        Returns:
            dict: Detailed presence information
        """
        if player_id not in self.online_players:
            return {
                "player_id": player_id,
                "is_online": False,
                "connection_types": [],
                "total_connections": 0,
                "websocket_connections": 0,
                "sse_connections": 0,
                "connected_at": None,
                "last_seen": None,
            }

        player_info = self.online_players[player_id]
        websocket_count = len(self.player_websockets.get(player_id, []))
        sse_count = len(self.active_sse_connections.get(player_id, []))

        return {
            "player_id": player_id,
            "is_online": True,
            "connection_types": list(player_info.get("connection_types", set())),
            "total_connections": player_info.get("total_connections", 0),
            "websocket_connections": websocket_count,
            "sse_connections": sse_count,
            "connected_at": player_info.get("connected_at"),
            "last_seen": self.last_seen.get(player_id),
            "player_name": player_info.get("player_name"),
            "current_room_id": player_info.get("current_room_id"),
            "level": player_info.get("level"),
        }

    def validate_player_presence(self, player_id: str) -> dict[str, Any]:
        """
        Validate player presence and clean up any inconsistencies.

        Args:
            player_id: The player's ID

        Returns:
            dict: Validation results
        """
        validation_results = {"player_id": player_id, "is_consistent": True, "issues_found": [], "actions_taken": []}

        try:
            # Check if player is in online_players but has no actual connections
            is_in_online = player_id in self.online_players
            has_websocket = self.has_websocket_connection(player_id)
            has_sse = self.has_sse_connection(player_id)
            has_any_connections = has_websocket or has_sse

            if is_in_online and not has_any_connections:
                validation_results["is_consistent"] = False
                validation_results["issues_found"].append("Player marked as online but has no connections")
                # Remove from online players
                del self.online_players[player_id]
                validation_results["actions_taken"].append("Removed from online_players")

            elif not is_in_online and has_any_connections:
                validation_results["is_consistent"] = False
                validation_results["issues_found"].append("Player has connections but not marked as online")
                # This should be handled by the connection methods, but log it
                validation_results["actions_taken"].append(
                    "Logged inconsistency - should be handled by connection methods"
                )

            # Check connection count consistency
            if is_in_online:
                player_info = self.online_players[player_id]
                recorded_count = player_info.get("total_connections", 0)
                actual_count = len(self.player_websockets.get(player_id, [])) + len(
                    self.active_sse_connections.get(player_id, [])
                )

                if recorded_count != actual_count:
                    validation_results["is_consistent"] = False
                    validation_results["issues_found"].append(
                        f"Connection count mismatch: recorded={recorded_count}, actual={actual_count}"
                    )
                    # Update the count
                    player_info["total_connections"] = actual_count
                    validation_results["actions_taken"].append("Updated connection count")

        except Exception as e:
            validation_results["is_consistent"] = False
            validation_results["issues_found"].append(f"Error during validation: {e}")

        return validation_results

    def get_presence_statistics(self) -> dict[str, Any]:
        """
        Get presence tracking statistics.

        Returns:
            dict: Presence statistics
        """
        total_online = len(self.online_players)
        total_websockets = sum(len(conns) for conns in self.player_websockets.values())
        total_sse = sum(len(conns) for conns in self.active_sse_connections.values())
        total_connections = total_websockets + total_sse

        # Count players by connection type
        websocket_only = 0
        sse_only = 0
        dual_connection = 0

        for player_id in self.online_players:
            has_ws = self.has_websocket_connection(player_id)
            has_sse = self.has_sse_connection(player_id)

            if has_ws and has_sse:
                dual_connection += 1
            elif has_ws:
                websocket_only += 1
            elif has_sse:
                sse_only += 1

        return {
            "total_online_players": total_online,
            "total_connections": total_connections,
            "websocket_connections": total_websockets,
            "sse_connections": total_sse,
            "connection_distribution": {
                "websocket_only": websocket_only,
                "sse_only": sse_only,
                "dual_connection": dual_connection,
            },
            "average_connections_per_player": total_connections / total_online if total_online > 0 else 0,
        }

    def get_error_statistics(self) -> dict[str, Any]:
        """
        Get error handling statistics.

        Returns:
            dict: Error statistics
        """
        # Get the proper error log path using logging configuration
        from ..config import get_config
        from ..logging.enhanced_logging_config import _resolve_log_base

        config = get_config()
        log_base = config.logging.log_base
        environment = config.logging.environment

        resolved_log_base = _resolve_log_base(log_base)
        error_log_path = resolved_log_base / environment / "connection_errors.log"

        return {
            "total_players": len(self.online_players),
            "total_connections": (
                sum(len(conns) for conns in self.player_websockets.values())
                + sum(len(conns) for conns in self.active_sse_connections.values())
            ),
            "active_sessions": len(self.session_connections),
            "players_with_sessions": len(self.player_sessions),
            "error_log_path": str(error_log_path),
        }

    async def handle_new_login(self, player_id: str):
        """
        Handle a new login by terminating all existing connections for the player.
        This ensures that only one session per player is active at a time.

        Args:
            player_id: The player's ID
        """
        try:
            logger.info("NEW LOGIN detected for player, terminating existing connections", player_id=player_id)

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
            logger.error("Error handling new login", player_id=player_id, error=str(e), exc_info=True)

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
                logger.debug("Disconnect already processed for player, skipping", player_id=player_id)

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
                logger.debug("Found online player", display_name=display_name, player_id=player_id)
                return player_info

        logger.debug("Online player not found", display_name=display_name)
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
                    logger.info(
                        f"DEBUG: Room data for {room_id}: npcs={room_data.get('npcs', [])}, occupant_count={room_data.get('occupant_count', 0)}"
                    )

            # Get room occupants (players and NPCs)
            occupants = []
            if room_id:
                # Get player occupants
                occ_infos = self.room_manager.get_room_occupants(room_id, self.online_players)
                for occ_player_info in occ_infos:
                    if isinstance(occ_player_info, dict) and occ_player_info.get("player_id") != player_id:
                        occupants.append(occ_player_info.get("player_name", "Unknown"))

                # Get NPC occupants
                if self.persistence:
                    room = self.persistence.get_room(room_id)
                    if room:
                        npc_ids = room.get_npcs()
                        logger.info("DEBUG: Room has NPCs", room_id=room_id, npc_ids=npc_ids)
                        logger.info(
                            "DEBUG: Room occupant_count", room_id=room_id, occupant_count=room.get_occupant_count()
                        )
                        for npc_id in npc_ids:
                            # Get NPC name from the actual NPC instance, preserving original case from database
                            npc_name = _get_npc_name_from_instance(npc_id)
                            if npc_name:
                                logger.info("DEBUG: Got NPC name from database", npc_name=npc_name, npc_id=npc_id)
                                occupants.append(npc_name)
                            else:
                                # Log warning if NPC instance not found - this should not happen in normal operation
                                logger.warning(
                                    "NPC instance not found for ID - skipping from room display", npc_id=npc_id
                                )

            # Create game_state event
            game_state_data = {
                "player": {
                    "player_id": str(getattr(player, "player_id", player_id)),
                    "name": getattr(player, "name", player_id),
                    "level": getattr(player, "level", 1),
                    "xp": getattr(player, "experience_points", 0),
                    "current_room_id": room_id,
                },
                "room": room_data,
                "occupants": occupants,
            }

            logger.info("DEBUG: Sending initial game state with occupants", occupants=occupants)

            game_state_event = build_event("game_state", game_state_data, player_id=player_id, room_id=room_id)

            # Send the event to the player
            await self.send_personal_message(player_id, game_state_event)
            logger.info("Sent initial game_state to player", player_id=player_id)

        except Exception as e:
            logger.error("Error sending initial game_state to player", player_id=player_id, error=str(e), exc_info=True)

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

            # Calculate dual connection metrics
            total_websocket_connections = sum(len(conn_ids) for conn_ids in self.player_websockets.values())
            total_sse_connections = sum(len(conn_ids) for conn_ids in self.active_sse_connections.values())
            players_with_multiple_connections = sum(
                1 for conn_ids in self.player_websockets.values() if len(conn_ids) > 1
            )
            players_with_dual_connections = sum(
                1
                for player_id in self.player_websockets.keys()
                if player_id in self.active_sse_connections
                and len(self.player_websockets[player_id]) > 0
                and len(self.active_sse_connections[player_id]) > 0
            )

            # Session metrics
            total_sessions = len(self.player_sessions)
            total_session_connections = sum(len(conn_ids) for conn_ids in self.session_connections.values())

            return {
                "memory": memory_stats,
                "connections": {
                    "active_websockets": len(self.active_websockets),
                    "active_sse": len(self.active_sse_connections),
                    "total_connections": len(self.active_websockets) + len(self.active_sse_connections),
                    "player_websockets": len(self.player_websockets),
                    "connection_timestamps": len(self.connection_timestamps),
                    # Dual connection metrics
                    "total_websocket_connections": total_websocket_connections,
                    "total_sse_connections": total_sse_connections,
                    "players_with_multiple_connections": players_with_multiple_connections,
                    "players_with_dual_connections": players_with_dual_connections,
                    "dual_connection_rate": (players_with_dual_connections / len(self.player_websockets) * 100)
                    if self.player_websockets
                    else 0,
                    "avg_connections_per_player": (total_websocket_connections + total_sse_connections)
                    / len(self.player_websockets)
                    if self.player_websockets
                    else 0,
                },
                "sessions": {
                    "total_sessions": total_sessions,
                    "total_session_connections": total_session_connections,
                    "avg_connections_per_session": total_session_connections / total_sessions
                    if total_sessions > 0
                    else 0,
                    "session_connection_ratio": total_session_connections
                    / (total_websocket_connections + total_sse_connections)
                    if (total_websocket_connections + total_sse_connections) > 0
                    else 0,
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
            logger.error("Error getting memory stats", error=str(e), exc_info=True)
            return {}

    def get_dual_connection_stats(self) -> dict[str, Any]:
        """
        Get comprehensive dual connection statistics.

        Returns:
            dict: Dual connection statistics including metrics, health, and performance data
        """
        try:
            now = time.time()

            # Calculate connection type distribution
            websocket_only_players = 0
            sse_only_players = 0
            dual_connection_players = 0
            total_players = len(self.player_websockets)

            for player_id in self.player_websockets.keys():
                has_websocket = len(self.player_websockets[player_id]) > 0
                has_sse = player_id in self.active_sse_connections and len(self.active_sse_connections[player_id]) > 0

                if has_websocket and has_sse:
                    dual_connection_players += 1
                elif has_websocket:
                    websocket_only_players += 1
                elif has_sse:
                    sse_only_players += 1

            # Calculate connection health metrics
            healthy_connections = 0
            unhealthy_connections = 0
            total_connection_metadata = len(self.connection_metadata)

            for metadata in self.connection_metadata.values():
                if metadata.is_healthy:
                    healthy_connections += 1
                else:
                    unhealthy_connections += 1

            # Calculate session distribution
            session_connection_counts = {}
            for _session_id, conn_ids in self.session_connections.items():
                count = len(conn_ids)
                session_connection_counts[count] = session_connection_counts.get(count, 0) + 1

            # Calculate connection age distribution
            connection_ages = []
            for metadata in self.connection_metadata.values():
                age = now - metadata.established_at
                connection_ages.append(age)

            avg_connection_age = sum(connection_ages) / len(connection_ages) if connection_ages else 0
            max_connection_age = max(connection_ages) if connection_ages else 0
            min_connection_age = min(connection_ages) if connection_ages else 0

            return {
                "connection_distribution": {
                    "total_players": total_players,
                    "websocket_only_players": websocket_only_players,
                    "sse_only_players": sse_only_players,
                    "dual_connection_players": dual_connection_players,
                    "dual_connection_percentage": (dual_connection_players / total_players * 100)
                    if total_players > 0
                    else 0,
                },
                "connection_health": {
                    "total_connections": total_connection_metadata,
                    "healthy_connections": healthy_connections,
                    "unhealthy_connections": unhealthy_connections,
                    "health_percentage": (healthy_connections / total_connection_metadata * 100)
                    if total_connection_metadata > 0
                    else 0,
                },
                "session_metrics": {
                    "total_sessions": len(self.player_sessions),
                    "total_session_connections": sum(len(conn_ids) for conn_ids in self.session_connections.values()),
                    "session_connection_distribution": session_connection_counts,
                    "avg_connections_per_session": sum(len(conn_ids) for conn_ids in self.session_connections.values())
                    / len(self.session_connections)
                    if self.session_connections
                    else 0,
                },
                "connection_lifecycle": {
                    "avg_connection_age_seconds": avg_connection_age,
                    "max_connection_age_seconds": max_connection_age,
                    "min_connection_age_seconds": min_connection_age,
                    "connections_older_than_1h": sum(1 for age in connection_ages if age > 3600),
                    "connections_older_than_24h": sum(1 for age in connection_ages if age > 86400),
                },
                "performance_metrics": {
                    "total_websocket_connections": sum(len(conn_ids) for conn_ids in self.player_websockets.values()),
                    "total_sse_connections": sum(len(conn_ids) for conn_ids in self.active_sse_connections.values()),
                    "avg_connections_per_player": (
                        sum(len(conn_ids) for conn_ids in self.player_websockets.values())
                        + sum(len(conn_ids) for conn_ids in self.active_sse_connections.values())
                    )
                    / total_players
                    if total_players > 0
                    else 0,
                },
                "timestamp": now,
            }
        except Exception as e:
            logger.error("Error getting dual connection stats", error=str(e), exc_info=True)
            return {"error": f"Failed to get dual connection stats: {e}", "timestamp": time.time()}

    def get_performance_stats(self) -> dict[str, Any]:
        """
        Get connection performance statistics.

        Returns:
            dict: Performance statistics including timing data and averages
        """
        try:
            # Calculate averages for connection establishment times
            websocket_times = [
                duration
                for conn_type, duration in self.performance_stats["connection_establishment_times"]
                if conn_type == "websocket"
            ]
            sse_times = [
                duration
                for conn_type, duration in self.performance_stats["connection_establishment_times"]
                if conn_type == "sse"
            ]

            # Calculate averages for message delivery times
            message_times = [duration for msg_type, duration in self.performance_stats["message_delivery_times"]]

            # Calculate averages for disconnection times
            disconnection_times = [duration for conn_type, duration in self.performance_stats["disconnection_times"]]

            # Calculate averages for session switch times
            session_switch_times = self.performance_stats["session_switch_times"]

            # Calculate averages for health check times
            health_check_times = self.performance_stats["health_check_times"]

            return {
                "connection_establishment": {
                    "total_connections": self.performance_stats["total_connections_established"],
                    "websocket_connections": len(websocket_times),
                    "sse_connections": len(sse_times),
                    "avg_websocket_establishment_ms": sum(websocket_times) / len(websocket_times)
                    if websocket_times
                    else 0,
                    "avg_sse_establishment_ms": sum(sse_times) / len(sse_times) if sse_times else 0,
                    "max_websocket_establishment_ms": max(websocket_times) if websocket_times else 0,
                    "max_sse_establishment_ms": max(sse_times) if sse_times else 0,
                    "min_websocket_establishment_ms": min(websocket_times) if websocket_times else 0,
                    "min_sse_establishment_ms": min(sse_times) if sse_times else 0,
                },
                "message_delivery": {
                    "total_messages": self.performance_stats["total_messages_delivered"],
                    "avg_delivery_time_ms": sum(message_times) / len(message_times) if message_times else 0,
                    "max_delivery_time_ms": max(message_times) if message_times else 0,
                    "min_delivery_time_ms": min(message_times) if message_times else 0,
                },
                "disconnections": {
                    "total_disconnections": self.performance_stats["total_disconnections"],
                    "avg_disconnection_time_ms": sum(disconnection_times) / len(disconnection_times)
                    if disconnection_times
                    else 0,
                    "max_disconnection_time_ms": max(disconnection_times) if disconnection_times else 0,
                    "min_disconnection_time_ms": min(disconnection_times) if disconnection_times else 0,
                },
                "session_management": {
                    "total_session_switches": self.performance_stats["total_session_switches"],
                    "avg_session_switch_time_ms": sum(session_switch_times) / len(session_switch_times)
                    if session_switch_times
                    else 0,
                    "max_session_switch_time_ms": max(session_switch_times) if session_switch_times else 0,
                    "min_session_switch_time_ms": min(session_switch_times) if session_switch_times else 0,
                },
                "health_monitoring": {
                    "total_health_checks": self.performance_stats["total_health_checks"],
                    "avg_health_check_time_ms": sum(health_check_times) / len(health_check_times)
                    if health_check_times
                    else 0,
                    "max_health_check_time_ms": max(health_check_times) if health_check_times else 0,
                    "min_health_check_time_ms": min(health_check_times) if health_check_times else 0,
                },
                "timestamp": time.time(),
            }
        except Exception as e:
            logger.error("Error getting performance stats", error=str(e), exc_info=True)
            return {"error": f"Failed to get performance stats: {e}", "timestamp": time.time()}

    def get_connection_health_stats(self) -> dict[str, Any]:
        """
        Get comprehensive connection health statistics.

        Returns:
            dict: Connection health statistics including health distribution and trends
        """
        try:
            now = time.time()

            # Analyze connection health distribution
            healthy_connections = 0
            unhealthy_connections = 0

            # Analyze connection types
            websocket_connections = 0
            sse_connections = 0

            # Analyze connection ages
            connection_ages = []
            stale_connections = 0

            # Analyze session health
            session_health = {}

            for _connection_id, metadata in self.connection_metadata.items():
                # Health analysis
                if metadata.is_healthy:
                    healthy_connections += 1
                else:
                    unhealthy_connections += 1

                # Type analysis
                if metadata.connection_type == "websocket":
                    websocket_connections += 1
                elif metadata.connection_type == "sse":
                    sse_connections += 1

                # Age analysis
                age = now - metadata.established_at
                connection_ages.append(age)
                if age > 3600:  # 1 hour
                    stale_connections += 1

                # Session health analysis
                if metadata.session_id:
                    if metadata.session_id not in session_health:
                        session_health[metadata.session_id] = {"healthy": 0, "unhealthy": 0, "total": 0}
                    session_health[metadata.session_id]["total"] += 1
                    if metadata.is_healthy:
                        session_health[metadata.session_id]["healthy"] += 1
                    else:
                        session_health[metadata.session_id]["unhealthy"] += 1

            # Calculate session health percentages
            healthy_sessions = 0
            unhealthy_sessions = 0
            for _session_id, health in session_health.items():
                if health["total"] > 0:
                    health_percentage = health["healthy"] / health["total"] * 100
                    if health_percentage >= 80:  # 80% threshold for healthy session
                        healthy_sessions += 1
                    else:
                        unhealthy_sessions += 1

            total_connections = len(self.connection_metadata)
            total_sessions = len(session_health)

            return {
                "overall_health": {
                    "total_connections": total_connections,
                    "healthy_connections": healthy_connections,
                    "unhealthy_connections": unhealthy_connections,
                    "health_percentage": (healthy_connections / total_connections * 100)
                    if total_connections > 0
                    else 0,
                },
                "connection_type_health": {
                    "websocket_connections": websocket_connections,
                    "sse_connections": sse_connections,
                    "websocket_health_percentage": 0,  # Would need separate tracking
                    "sse_health_percentage": 0,  # Would need separate tracking
                },
                "connection_lifecycle": {
                    "avg_connection_age_seconds": sum(connection_ages) / len(connection_ages) if connection_ages else 0,
                    "max_connection_age_seconds": max(connection_ages) if connection_ages else 0,
                    "min_connection_age_seconds": min(connection_ages) if connection_ages else 0,
                    "stale_connections": stale_connections,
                    "stale_connection_percentage": (stale_connections / total_connections * 100)
                    if total_connections > 0
                    else 0,
                },
                "session_health": {
                    "total_sessions": total_sessions,
                    "healthy_sessions": healthy_sessions,
                    "unhealthy_sessions": unhealthy_sessions,
                    "session_health_percentage": (healthy_sessions / total_sessions * 100) if total_sessions > 0 else 0,
                    "avg_connections_per_session": total_connections / total_sessions if total_sessions > 0 else 0,
                },
                "health_trends": {
                    "connections_older_than_1h": sum(1 for age in connection_ages if age > 3600),
                    "connections_older_than_24h": sum(1 for age in connection_ages if age > 86400),
                    "connections_older_than_7d": sum(1 for age in connection_ages if age > 604800),
                },
                "timestamp": now,
            }
        except Exception as e:
            logger.error("Error getting connection health stats", error=str(e), exc_info=True)
            return {"error": f"Failed to get connection health stats: {e}", "timestamp": time.time()}

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
            logger.error("Error getting memory alerts", error=str(e), exc_info=True)
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
                    logger.error("Error cancelling cleanup task", error=str(e))

            await self.cleanup_orphaned_data()
            self.prune_stale_players()
            self.memory_monitor.force_garbage_collection()
            self.cleanup_stats["cleanups_performed"] += 1
            self.memory_monitor.update_cleanup_time()
            logger.info("Force cleanup completed")
        except Exception as e:
            logger.error("Error during force cleanup", error=str(e), exc_info=True)

    # --- Event Subscription Methods ---

    def _get_event_bus(self):
        """Get the event bus from the persistence layer."""
        from ..persistence import get_persistence

        persistence = get_persistence()
        return getattr(persistence, "_event_bus", None)

    async def subscribe_to_room_events(self):
        """Subscribe to room movement events for occupant broadcasting."""
        event_bus = self._get_event_bus()
        if not event_bus:
            logger.warning("No event bus available for room event subscription")
            return

        try:
            from ..events.event_types import PlayerEnteredRoom, PlayerLeftRoom

            event_bus.subscribe(PlayerEnteredRoom, self._handle_player_entered_room)
            event_bus.subscribe(PlayerLeftRoom, self._handle_player_left_room)
            logger.info("Successfully subscribed to room movement events")
        except Exception as e:
            logger.error("Error subscribing to room events", error=str(e), exc_info=True)

    async def unsubscribe_from_room_events(self):
        """Unsubscribe from room movement events."""
        event_bus = self._get_event_bus()
        if not event_bus:
            return

        try:
            from ..events.event_types import PlayerEnteredRoom, PlayerLeftRoom

            event_bus.unsubscribe(PlayerEnteredRoom, self._handle_player_entered_room)
            event_bus.unsubscribe(PlayerLeftRoom, self._handle_player_left_room)
            logger.info("Successfully unsubscribed from room movement events")
        except Exception as e:
            logger.error("Error unsubscribing from room events", error=str(e), exc_info=True)

    async def _handle_player_entered_room(self, event_data):
        """Handle PlayerEnteredRoom events by broadcasting updated occupant count."""
        try:
            room_id = event_data.get("room_id")
            player_id = event_data.get("player_id")

            if not room_id:
                logger.warning("PlayerEnteredRoom event missing room_id")
                return

            # Publish NATS event if event_publisher is available
            if self.event_publisher and player_id:
                try:
                    from datetime import datetime

                    timestamp = datetime.now(UTC).isoformat()
                    await self.event_publisher.publish_player_entered_event(
                        player_id=player_id, room_id=room_id, timestamp=timestamp
                    )
                except Exception as e:
                    logger.error("Failed to publish player_entered NATS event", error=str(e))

            # Get current room occupants
            occ_infos = self.room_manager.get_room_occupants(room_id, self.online_players)
            names: list[str] = []
            for occ in occ_infos:
                name = occ.get("player_name") if isinstance(occ, dict) else None
                if name:
                    names.append(name)

            # Build and broadcast room_occupants event
            from .envelope import build_event

            occ_event = build_event(
                "room_occupants",
                {"occupants": names, "count": len(names)},
                room_id=room_id,
            )
            await self.broadcast_to_room(room_id, occ_event)

            logger.debug("Broadcasted room_occupants event for room", room_id=room_id, occupant_count=len(names))

        except Exception as e:
            logger.error("Error handling PlayerEnteredRoom event", error=str(e), exc_info=True)

    async def _handle_player_left_room(self, event_data):
        """Handle PlayerLeftRoom events by broadcasting updated occupant count."""
        try:
            room_id = event_data.get("room_id")
            player_id = event_data.get("player_id")

            if not room_id:
                logger.warning("PlayerLeftRoom event missing room_id")
                return

            # Publish NATS event if event_publisher is available
            if self.event_publisher and player_id:
                try:
                    from datetime import datetime

                    timestamp = datetime.now(UTC).isoformat()
                    await self.event_publisher.publish_player_left_event(
                        player_id=player_id, room_id=room_id, timestamp=timestamp
                    )
                except Exception as e:
                    logger.error("Failed to publish player_left NATS event", error=str(e))

            # Get current room occupants
            occ_infos = self.room_manager.get_room_occupants(room_id, self.online_players)
            names: list[str] = []
            for occ in occ_infos:
                name = occ.get("player_name") if isinstance(occ, dict) else None
                if name:
                    names.append(name)

            # Build and broadcast room_occupants event
            from .envelope import build_event

            occ_event = build_event(
                "room_occupants",
                {"occupants": names, "count": len(names)},
                room_id=room_id,
            )
            await self.broadcast_to_room(room_id, occ_event)

            logger.debug("Broadcasted room_occupants event for room", room_id=room_id, occupant_count=len(names))

        except Exception as e:
            logger.error("Error handling PlayerLeftRoom event", error=str(e), exc_info=True)


# Global connection manager instance
connection_manager = ConnectionManager()
