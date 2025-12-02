"""
Refactored Connection Manager for MythosMUD real-time communication.

This module provides a clean, modular connection management system that
separates concerns into dedicated components for better maintainability
and testability.
"""

import asyncio
import inspect
import time
import uuid
from dataclasses import dataclass
from datetime import UTC
from typing import Any, TypedDict
from unittest.mock import AsyncMock, Mock

from fastapi import WebSocket
from starlette.websockets import WebSocketState

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
        # Get the NPC instance from the lifecycle manager (single source of truth)
        from ..services.npc_instance_service import get_npc_instance_service

        npc_instance_service = get_npc_instance_service()
        if hasattr(npc_instance_service, "lifecycle_manager"):
            lifecycle_manager = npc_instance_service.lifecycle_manager
            if lifecycle_manager and npc_id in lifecycle_manager.active_npcs:
                npc_instance = lifecycle_manager.active_npcs[npc_id]
                name = getattr(npc_instance, "name", None)
                if name:
                    return name

        return None
    except Exception as e:
        logger.debug("Error getting NPC name from instance", npc_id=npc_id, error=str(e))
        return None


class PerformanceStats(TypedDict):
    """Type definition for performance statistics tracking."""

    connection_establishment_times: list[tuple[str, float]]
    message_delivery_times: list[tuple[str, float]]
    disconnection_times: list[tuple[str, float]]
    session_switch_times: list[float]
    health_check_times: list[float]
    total_connections_established: int
    total_messages_delivered: int
    total_disconnections: int
    total_session_switches: int
    total_health_checks: int


@dataclass
class ConnectionMetadata:
    """
    Metadata for tracking connection details in the WebSocket-only system.

    This dataclass stores information about each connection to enable
    proper management of multiple connections per player.
    """

    connection_id: str
    player_id: uuid.UUID
    connection_type: str  # "websocket"
    established_at: float
    last_seen: float
    is_healthy: bool
    session_id: str | None = None  # For tracking new game client sessions
    token: str | None = None  # JWT token for periodic revalidation
    last_token_validation: float | None = None  # Timestamp of last token validation


class ConnectionManager:
    """
    Manages real-time connections for the game.

    This refactored version uses modular components to separate concerns:
    - MemoryMonitor: Memory usage monitoring and cleanup scheduling
    - RateLimiter: Connection rate limiting
    - MessageQueue: Pending message management
    - RoomSubscriptionManager: Room subscriptions and occupant tracking
    """

    def __init__(self, event_publisher: Any = None) -> None:
        """Initialize the connection manager with modular components."""
        # Active WebSocket connections
        self.active_websockets: dict[str, WebSocket] = {}
        # Player ID to WebSocket connection IDs mapping (supports multiple connections)
        self.player_websockets: dict[uuid.UUID, list[str]] = {}
        # Connection metadata tracking
        self.connection_metadata: dict[str, ConnectionMetadata] = {}
        # Global event sequence counter
        self.sequence_counter = 0
        # Reference to persistence layer (set during app startup)
        self.persistence: Any | None = None
        # EventPublisher for NATS integration
        self.event_publisher = event_publisher
        # Event bus reference (set during app startup)
        self._event_bus: Any = None
        # FastAPI app reference (set during app startup)
        self.app: Any = None
        # Player combat service reference (set during app startup)
        self._player_combat_service: Any = None

        # Player presence tracking
        # player_id -> player_info
        self.online_players: dict[uuid.UUID, dict[str, Any]] = {}
        # player_id -> last seen unix timestamp
        self.last_seen: dict[uuid.UUID, float] = {}
        # Throttled persistence updates for last_active timestamps
        self.last_active_update_interval: float = 60.0
        self.last_active_update_times: dict[uuid.UUID, float] = {}
        # Track players currently being disconnected to prevent duplicate events
        self.disconnecting_players: set[uuid.UUID] = set()
        self.disconnect_lock = asyncio.Lock()
        # Track players whose disconnect has already been processed
        self.processed_disconnects: set[uuid.UUID] = set()
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
        self.performance_stats: PerformanceStats = {
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
        self.player_sessions: dict[uuid.UUID, str] = {}  # player_id -> current_session_id
        self.session_connections: dict[str, list[str]] = {}  # session_id -> list of connection_ids

        # Track safely closed websocket objects to avoid duplicate closes
        self._closed_websockets: set[int] = set()

        # Background executor for disconnect processing when no event loop is available
        self._disconnect_executor: Any | None = None

        # Connection health check configuration
        self._health_check_interval: float = 30.0  # Check every 30 seconds
        self._health_check_task: Any | None = None
        # 5 minutes idle = stale connection (aligned with MemoryMonitor.max_connection_age)
        self._connection_timeout: float = 300.0
        self._token_revalidation_interval: float = 300.0  # Revalidate tokens every 5 minutes

    def _is_websocket_open(self, websocket: WebSocket) -> bool:
        try:
            state = getattr(websocket, "application_state", None)
            # WebSocketState only has: CONNECTED, CONNECTING, DISCONNECTED, RESPONSE
            # AI Agent: Fixed mypy error - CLOSING and CLOSED don't exist in Starlette's WebSocketState
            return state != WebSocketState.DISCONNECTED
        except Exception:
            # If we cannot determine, assume open and let close handle exceptions
            return True

    async def _safe_close_websocket(
        self, websocket: WebSocket, code: int = 1000, reason: str = "Connection closed"
    ) -> None:
        ws_id = id(websocket)
        if ws_id in self._closed_websockets:
            return
        if not self._is_websocket_open(websocket):
            self._closed_websockets.add(ws_id)
            return
        try:
            await asyncio.wait_for(websocket.close(code=code, reason=reason), timeout=2.0)
        except Exception:
            # Ignore close errors; treat as closed
            pass
        finally:
            self._closed_websockets.add(ws_id)

    # Compatibility properties for existing tests and code
    # These provide access to the internal data structures for backward compatibility
    @property
    def room_subscriptions(self) -> Any:
        return self.room_manager.room_subscriptions

    @room_subscriptions.setter
    def room_subscriptions(self, value: Any) -> None:
        self.room_manager.room_subscriptions = value

    @room_subscriptions.deleter
    def room_subscriptions(self) -> None:
        self.room_manager.room_subscriptions.clear()

    @property
    def room_occupants(self) -> Any:
        return self.room_manager.room_occupants

    @room_occupants.setter
    def room_occupants(self, value: Any) -> None:
        self.room_manager.room_occupants = value

    @room_occupants.deleter
    def room_occupants(self) -> None:
        self.room_manager.room_occupants.clear()

    @property
    def connection_attempts(self) -> Any:
        return self.rate_limiter.connection_attempts

    @connection_attempts.setter
    def connection_attempts(self, value: Any) -> None:
        self.rate_limiter.connection_attempts = value

    @connection_attempts.deleter
    def connection_attempts(self) -> None:
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

    # Compatibility methods for WebSocket connection system
    def get_player_websocket_connection_id(self, player_id: uuid.UUID) -> str | None:
        """
        Get the first WebSocket connection ID for a player (backward compatibility).

        Args:
            player_id: The player's ID (UUID)

        Returns:
            str: The first connection ID if any exist, None otherwise
        """
        if player_id in self.player_websockets and self.player_websockets[player_id]:
            return self.player_websockets[player_id][0]
        return None

    def has_websocket_connection(self, player_id: uuid.UUID) -> bool:
        """
        Check if a player has any WebSocket connections.

        Args:
            player_id: The player's ID (UUID)

        Returns:
            bool: True if player has WebSocket connections, False otherwise
        """
        return player_id in self.player_websockets and len(self.player_websockets[player_id]) > 0

    def get_connection_count(self, player_id: uuid.UUID) -> dict[str, int]:
        """
        Get the number of connections for a player by type.

        Args:
            player_id: The player's ID (UUID)

        Returns:
            dict: Connection counts by type
        """
        websocket_count = len(self.player_websockets.get(player_id, []))
        return {"websocket": websocket_count, "total": websocket_count}

    # Add compatibility methods
    async def subscribe_to_room(self, player_id: uuid.UUID, room_id: str):
        """Subscribe a player to a room (compatibility method)."""
        # Resolve canonical room ID first
        canonical_id = self._canonical_room_id(room_id) or room_id
        return self.room_manager.subscribe_to_room(str(player_id), canonical_id)

    async def unsubscribe_from_room(self, player_id: uuid.UUID, room_id: str):
        """Unsubscribe a player from a room (compatibility method)."""
        # Resolve canonical room ID first (must match subscribe_to_room behavior)
        canonical_id = self._canonical_room_id(room_id) or room_id
        return self.room_manager.unsubscribe_from_room(str(player_id), canonical_id)

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
        # Convert UUID keys to strings for room manager
        online_players_str = {str(k): v for k, v in self.online_players.items()}
        return self.room_manager.reconcile_room_presence(room_id, online_players_str)

    def _prune_player_from_all_rooms(self, player_id: uuid.UUID):
        """Remove a player from all room subscriptions and occupant lists (compatibility method)."""
        return self.room_manager.remove_player_from_all_rooms(str(player_id))

    def set_persistence(self, persistence):
        """Set the persistence layer reference for all components."""
        self.persistence = persistence
        self.room_manager.set_persistence(persistence)

    async def connect_websocket(
        self, websocket: WebSocket, player_id: uuid.UUID, session_id: str | None = None, token: str | None = None
    ) -> bool:
        """
        Connect a WebSocket for a player.

        Args:
            websocket: The WebSocket connection
            player_id: The player's ID (UUID)
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
                                "Dead WebSocket connection, will clean up",
                                connection_id=connection_id,
                                player_id=player_id,
                                ping_error=str(ping_error),
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
                # We allow multiple WebSocket connections per player
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

            # Accept the WebSocket connection with subprotocol negotiation
            # CRITICAL FIX: Client sends ['bearer', <token>] as subprotocols
            # Server must select 'bearer' to complete the handshake
            await websocket.accept(subprotocol="bearer")
            connection_id = str(uuid.uuid4())
            self.active_websockets[connection_id] = websocket

            # Store connection_id in websocket state for easy retrieval
            # Note: websocket.state is read-only in Starlette, so we use a workaround
            # by storing connection_id in a custom attribute
            websocket._mythos_connection_id = connection_id  # type: ignore[attr-defined]

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
                token=token,
                last_token_validation=current_time if token else None,
            )

            # Track connection in session
            if session_id:
                if session_id not in self.session_connections:
                    self.session_connections[session_id] = []
                self.session_connections[session_id].append(connection_id)
                # Only update player session if they don't have one or if this is the same session
                if player_id not in self.player_sessions or self.player_sessions[player_id] == session_id:
                    self.player_sessions[player_id] = session_id

            # Enhanced connection logging
            existing_websocket_count = len(self.player_websockets[player_id]) - 1  # -1 because we just added one
            total_connections = existing_websocket_count + 1  # +1 for the new connection

            logger.info(
                "WebSocket connected for player",
                player_id=player_id,
                connection_id=connection_id,
                session_id=session_id,
                existing_websocket_connections=existing_websocket_count,
                total_connections=total_connections,
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
                    self.room_manager.subscribe_to_room(str(player_id), canonical_room_id)

                # Track player presence - always call _track_player_connected for WebSocket connections
                # to ensure connection messages are broadcast to other players
                if player_id not in self.online_players:
                    await self._track_player_connected(player_id, player, "websocket")
                else:
                    logger.info(
                        "Player already tracked as online, but broadcasting connection message for WebSocket",
                        player_id=player_id,
                    )
                    # Still broadcast connection message even if player is already tracked
                    await self._broadcast_connection_message(player_id, player)

        except Exception as e:
            # Enhanced error context for connection failures
            logger.error(
                "Error connecting WebSocket",
                player_id=player_id,
                session_id=session_id,
                has_token=bool(token),
                error=str(e),
                error_type=type(e).__name__,
                exc_info=True,
            )
            # Attempt cleanup on connection failure
            try:
                if "connection_id" in locals():
                    # Connection was partially established, clean it up
                    if connection_id in self.active_websockets:
                        del self.active_websockets[connection_id]
                    if connection_id in self.connection_metadata:
                        del self.connection_metadata[connection_id]
            except Exception as cleanup_error:
                logger.warning(
                    "Error during connection failure cleanup",
                    player_id=player_id,
                    cleanup_error=str(cleanup_error),
                )
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

    async def disconnect_websocket(self, player_id: uuid.UUID, is_force_disconnect: bool = False):
        """
        Disconnect all WebSocket connections for a player.

        Args:
            player_id: The player's ID (UUID)
            is_force_disconnect: If True, don't broadcast player_left_game
        """
        # Use disconnect_lock to prevent concurrent disconnects for the same player
        async with self.disconnect_lock:
            try:
                logger.info(
                    "Starting WebSocket disconnect",
                    player_id=player_id,
                    force_disconnect=bool(is_force_disconnect),
                )

                if player_id in self.player_websockets:
                    connection_ids = self.player_websockets[
                        player_id
                    ].copy()  # Copy to avoid modification during iteration
                    logger.info(
                        "Found WebSocket connections",
                        player_id=player_id,
                        connection_count=len(connection_ids),
                        connection_ids=connection_ids,
                    )

                    # Disconnect all WebSocket connections for this player
                    for connection_id in connection_ids:
                        if connection_id in self.active_websockets:
                            websocket = self.active_websockets[connection_id]
                            logger.info("DEBUG: Closing WebSocket", connection_id=connection_id, player_id=player_id)
                            # Properly close the WebSocket connection
                            await self._safe_close_websocket(websocket, code=1000, reason="Connection closed")
                            logger.info(
                                "Successfully closed WebSocket",
                                connection_id=connection_id,
                                player_id=player_id,
                            )
                            del self.active_websockets[connection_id]

                        # Clean up connection metadata
                        if connection_id in self.connection_metadata:
                            del self.connection_metadata[connection_id]

                        # Clean up message rate limit data for this connection
                        self.rate_limiter.remove_connection_message_data(connection_id)

                    # Remove player from websocket tracking
                    del self.player_websockets[player_id]

                    # Check if we need to track disconnection (outside of disconnect_lock to avoid deadlock)
                    should_track_disconnect = False
                    if not is_force_disconnect and not self.has_websocket_connection(player_id):
                        # Check if disconnect needs to be processed without holding the disconnect_lock
                        async with self.processed_disconnect_lock:
                            if player_id not in self.processed_disconnects:
                                self.processed_disconnects.add(player_id)
                                should_track_disconnect = True
                            else:
                                logger.debug("Disconnect already processed, skipping", player_id=player_id)

                    # Unsubscribe from all rooms only if it's not a force disconnect and no other connections
                    # During reconnections, we want to preserve room membership
                    if not is_force_disconnect and not self.has_websocket_connection(player_id):
                        self.room_manager.remove_player_from_all_rooms(str(player_id))
                    else:
                        logger.debug(
                            "Preserving room membership during force disconnect (reconnection)",
                            player_id=player_id,
                        )

                    # Clean up rate limiting data only if no other connections
                    if not self.has_websocket_connection(player_id):
                        self.rate_limiter.remove_player_data(str(player_id))
                        # Clean up pending messages
                        self.message_queue.remove_player_messages(str(player_id))
                        # Clean up last seen data
                        if player_id in self.last_seen:
                            del self.last_seen[player_id]
                        self.last_active_update_times.pop(player_id, None)

                    logger.info("WebSocket disconnected", player_id=player_id)

            except Exception as e:
                logger.error("Error during WebSocket disconnect", player_id=player_id, error=str(e), exc_info=True)

        # CRITICAL FIX: Track disconnect OUTSIDE of disconnect_lock to avoid deadlock
        # This must be after the disconnect_lock context manager exits
        if should_track_disconnect:
            await self._track_player_disconnected(player_id)

    async def force_disconnect_player(self, player_id: uuid.UUID):
        """
        Force disconnect a player from all connections (WebSocket only).

        Args:
            player_id: The player's ID (UUID)
        """
        try:
            logger.info("Force disconnecting player from all connections", player_id=player_id)

            # Disconnect WebSocket if active (without broadcasting player_left_game)
            if player_id in self.player_websockets:
                await self.disconnect_websocket(player_id, is_force_disconnect=True)

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
                    await self._safe_close_websocket(websocket, code=1000, reason="Connection closed")
                    logger.info("DEBUG: Successfully closed WebSocket by connection ID", connection_id=connection_id)
                    del self.active_websockets[connection_id]

                # Remove from player's connection list
                if player_id in self.player_websockets and connection_id in self.player_websockets[player_id]:
                    self.player_websockets[player_id].remove(connection_id)
                    # If no more connections, remove the player entry
                    if not self.player_websockets[player_id]:
                        del self.player_websockets[player_id]

            # Clean up connection metadata
            del self.connection_metadata[connection_id]

            # Check if player has any remaining connections
            has_websocket = self.has_websocket_connection(player_id)

            # If no connections remain, clean up player data
            if not has_websocket:
                self.rate_limiter.remove_player_data(str(player_id))
                self.message_queue.remove_player_messages(str(player_id))
                if player_id in self.last_seen:
                    del self.last_seen[player_id]
                self.last_active_update_times.pop(player_id, None)
                # Remove from room subscriptions
                self.room_manager.remove_player_from_all_rooms(str(player_id))
                logger.info("Player has no remaining connections, cleaned up player data", player_id=player_id)

            logger.info(
                "Successfully disconnected connection", connection_type=connection_type, connection_id=connection_id
            )
            return True

        except Exception as e:
            logger.error("Error disconnecting connection", connection_id=connection_id, error=str(e), exc_info=True)
            return False

    async def disconnect_websocket_connection(self, player_id: uuid.UUID, connection_id: str) -> bool:
        """
        Disconnect a specific WebSocket connection for a player.

        Args:
            player_id: The player's ID (UUID)
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
                    "Connection does not belong to player or is not a WebSocket",
                    connection_id=connection_id,
                    player_id=player_id,
                )
                return False

            return await self.disconnect_connection_by_id(connection_id)

        except Exception as e:
            logger.error(
                "Error disconnecting WebSocket connection",
                connection_id=connection_id,
                player_id=player_id,
                error=str(e),
                exc_info=True,
            )
            return False

    async def handle_new_game_session(self, player_id: uuid.UUID, new_session_id: str) -> dict[str, Any]:
        """
        Handle a new game session by disconnecting existing connections.

        This method implements the requirement that when a user logs in through
        a new game client session, existing connections should be disconnected.

        Args:
            player_id: The player's ID (UUID)
            new_session_id: The new session ID

        Returns:
            dict: Session handling results with detailed information
        """
        session_results: dict[str, Any] = {
            # FastAPI automatically serializes UUIDs to strings in JSON responses
            "player_id": player_id,
            "new_session_id": new_session_id,
            "previous_session_id": None,
            "connections_disconnected": 0,
            "websocket_connections": 0,
            "success": False,
            "errors": [],
        }

        try:
            # Enhanced session logging
            existing_websocket_count = len(self.player_websockets.get(player_id, []))
            total_existing_connections = existing_websocket_count

            logger.info(
                "Handling new game session for player",
                new_session_id=new_session_id,
                player_id=player_id,
                existing_websocket_connections=existing_websocket_count,
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
                                    "Could not check WebSocket state, assuming disconnected",
                                    connection_id=connection_id,
                                )

                            if is_connected:
                                logger.info(
                                    "Closing WebSocket due to new game session",
                                    connection_id=connection_id,
                                    player_id=player_id,
                                )
                                await websocket.close(code=1000, reason="New game session established")
                                logger.info(
                                    "Successfully closed WebSocket due to new game session",
                                    connection_id=connection_id,
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
            self.rate_limiter.remove_player_data(str(player_id))
            self.message_queue.remove_player_messages(str(player_id))
            if player_id in self.last_seen:
                del self.last_seen[player_id]
            self.last_active_update_times.pop(player_id, None)

            # Remove from room subscriptions
            self.room_manager.remove_player_from_all_rooms(str(player_id))

            session_results["success"] = True
            logger.info(
                "Disconnected connections for new game session",
                connections_disconnected=session_results["connections_disconnected"],
                new_session_id=new_session_id,
                player_id=player_id,
            )

        except Exception as e:
            error_msg = f"Error handling new game session for player {player_id}: {e}"
            logger.error(error_msg, exc_info=True)
            session_results["errors"].append(error_msg)
            session_results["success"] = False

        return session_results

    def get_player_session(self, player_id: uuid.UUID) -> str | None:
        """
        Get the current session ID for a player.

        Args:
            player_id: The player's ID (UUID)

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

    def validate_session(self, player_id: uuid.UUID, session_id: str) -> bool:
        """
        Validate that a session ID matches the player's current session.

        Args:
            player_id: The player's ID (UUID)
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

    def mark_player_seen(self, player_id: uuid.UUID):
        """Update last-seen timestamp for a player and all their connections."""
        try:
            now_ts = time.time()
            self.last_seen[player_id] = now_ts

            # CRITICAL FIX: Update last_seen for all connection metadata for this player
            # This ensures health checks see ping messages as activity
            if player_id in self.player_websockets:
                for connection_id in self.player_websockets[player_id]:
                    if connection_id in self.connection_metadata:
                        self.connection_metadata[connection_id].last_seen = now_ts

            if self.persistence:
                last_update = self.last_active_update_times.get(player_id, 0.0)
                if now_ts - last_update >= self.last_active_update_interval:
                    from datetime import UTC, datetime

                    try:
                        self.persistence.update_player_last_active(player_id, datetime.now(UTC))
                        self.last_active_update_times[player_id] = now_ts
                    except Exception as update_error:
                        logger.warning(
                            "Failed to persist last_active update",
                            player_id=player_id,
                            error=str(update_error),
                        )
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
            stale_ids: list[uuid.UUID] = []
            for pid, last in list(self.last_seen.items()):
                if now_ts - last > max_age_seconds:
                    stale_ids.append(pid)

            for pid in stale_ids:
                if pid in self.online_players:
                    del self.online_players[pid]
                if pid in self.player_websockets:
                    # forget websocket mapping; socket likely already dead
                    conn_ids = self.player_websockets.pop(pid, None)
                    if conn_ids:
                        for conn_id in conn_ids:
                            if conn_id in self.active_websockets:
                                del self.active_websockets[conn_id]
                # remove from rooms
                self.room_manager.remove_player_from_all_rooms(str(pid))
                # forget last_seen entry
                if pid in self.last_seen:
                    del self.last_seen[pid]
                self.last_active_update_times.pop(pid, None)
                # Clean up other references
                self.rate_limiter.remove_player_data(str(pid))
                self.message_queue.remove_player_messages(str(pid))
            if stale_ids:
                logger.info("Pruned stale players", stale_ids=[str(pid) for pid in stale_ids])
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
                        "DEBUG: Connection is stale",
                        connection_id=connection_id,
                        connection_age=connection_age,
                        max_connection_age=self.memory_monitor.max_connection_age,
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
        return len(self.active_websockets)

    def check_rate_limit(self, player_id: uuid.UUID) -> bool:
        """
        Check if a player has exceeded rate limits.

        Args:
            player_id: The player's ID (UUID)

        Returns:
            bool: True if rate limit not exceeded, False if exceeded
        """
        return self.rate_limiter.check_rate_limit(str(player_id))

    def get_rate_limit_info(self, player_id: uuid.UUID) -> dict[str, Any]:
        """
        Get rate limit information for a player.

        Args:
            player_id: The player's ID (UUID)

        Returns:
            Dict[str, Any]: Rate limit information
        """
        return self.rate_limiter.get_rate_limit_info(str(player_id))

    async def send_personal_message(self, player_id: uuid.UUID, event: dict[str, Any]) -> dict[str, Any]:
        """
        Send a personal message to a player via WebSocket.

        Args:
            player_id: The player's ID (UUID)
            event: The event data to send

        Returns:
            dict: Delivery status with detailed information:
                {
                    "success": bool,
                    "websocket_delivered": int,
                    "websocket_failed": int,
                    "total_connections": int,
                    "active_connections": int
                }
        """
        delivery_status = {
            "success": False,
            "websocket_delivered": 0,
            "websocket_failed": 0,
            "total_connections": 0,
            "active_connections": 0,
        }

        try:
            # Convert UUIDs to strings for JSON serialization
            serializable_event = self._convert_uuids_to_strings(event)

            # OPTIMIZATION: Optimize payload size (compression, size limits)
            try:
                from .payload_optimizer import get_payload_optimizer

                optimizer = get_payload_optimizer()
                serializable_event = optimizer.optimize_payload(serializable_event)
            except ValueError as size_error:
                # Payload too large - log error and send truncated/error message
                logger.error(
                    "Payload too large to send",
                    player_id=player_id,
                    error=str(size_error),
                    event_type=event.get("event_type"),
                )
                # Send error message instead
                serializable_event = {
                    "type": "error",
                    "error_type": "payload_too_large",
                    "message": "Message payload too large to transmit",
                    "details": {"max_size": optimizer.max_payload_size},
                }
            except Exception as opt_error:
                # Optimization failed, but continue with original payload
                logger.warning(
                    "Payload optimization failed, using original",
                    player_id=player_id,
                    error=str(opt_error),
                )

            # Debug logging to see what's being sent
            if event.get("event_type") == "game_state":
                logger.info("Sending game_state event", player_id=player_id, event_data=serializable_event)

            # Count total connections
            websocket_count = len(self.player_websockets.get(player_id, []))
            delivery_status["total_connections"] = websocket_count

            # Track if we had any connection attempts (for failure detection)
            had_connection_attempts = False

            # Try WebSocket connections
            if player_id in self.player_websockets:
                connection_ids = self.player_websockets[player_id].copy()  # Copy to avoid modification during iteration
                for connection_id in connection_ids:
                    if connection_id in self.active_websockets:
                        had_connection_attempts = True
                        websocket = self.active_websockets[connection_id]
                        try:
                            # Check if WebSocket is still open by attempting to send
                            await websocket.send_json(serializable_event)
                            delivery_status["websocket_delivered"] += 1
                            delivery_status["active_connections"] += 1
                        except Exception as ws_error:
                            # WebSocket is closed or in an invalid state
                            logger.warning(
                                "WebSocket send failed",
                                player_id=player_id,
                                connection_id=connection_id,
                                error=str(ws_error),
                            )
                            delivery_status["websocket_failed"] += 1
                            # Clean up the dead WebSocket connection
                            await self._cleanup_dead_websocket(player_id, connection_id)
                            # Continue to other connections
            # If no active connections, queue the message for later delivery
            if delivery_status["active_connections"] == 0:
                player_id_str = str(player_id)
                if player_id_str not in self.message_queue.pending_messages:
                    self.message_queue.pending_messages[player_id_str] = []
                self.message_queue.pending_messages[player_id_str].append(serializable_event)
                logger.debug(
                    "No active connections, queued message for later delivery",
                    player_id=player_id,
                    event_type=event.get("event_type"),
                )
                # Mark as successful if message was queued (will be delivered on reconnect)
                # BUT: if we had connection attempts that failed, this is still a failure
                if had_connection_attempts and delivery_status["websocket_failed"] > 0:
                    delivery_status["success"] = False
                else:
                    delivery_status["success"] = True
            else:
                # Mark as successful if any delivery succeeded
                delivery_status["success"] = delivery_status["websocket_delivered"] > 0

            logger.debug("Message delivery status", player_id=player_id, delivery_status=delivery_status)
            return delivery_status

        except Exception as e:
            logger.error("Failed to send personal message", player_id=player_id, error=str(e))
            delivery_status["success"] = False
            return delivery_status

    def get_message_delivery_stats(self, player_id: uuid.UUID) -> dict[str, Any]:
        """
        Get message delivery statistics for a player.

        Args:
            player_id: The player's ID

        Returns:
            dict: Message delivery statistics
        """
        # pending_messages uses str keys, so convert UUID to str
        player_id_str = str(player_id)
        stats: dict[str, Any] = {
            "player_id": player_id,
            "websocket_connections": len(self.player_websockets.get(player_id, [])),
            "total_connections": 0,
            "pending_messages": len(self.message_queue.pending_messages.get(player_id_str, [])),
            "has_active_connections": False,
        }

        stats["total_connections"] = stats["websocket_connections"]
        stats["has_active_connections"] = stats["total_connections"] > 0

        return stats

    async def check_connection_health(self, player_id: uuid.UUID) -> dict[str, Any]:
        """
        Check the health of all connections for a player.

        Args:
            player_id: The player's ID

        Returns:
            dict: Connection health information
        """
        health_status: dict[str, Any] = {
            "player_id": player_id,
            "websocket_healthy": 0,
            "websocket_unhealthy": 0,
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
                        except (RuntimeError, ConnectionError, AttributeError) as e:
                            logger.error(
                                "WebSocket health check failed",
                                player_id=player_id,
                                connection_id=connection_id,
                                error=str(e),
                                error_type=type(e).__name__,
                            )
                            health_status["websocket_unhealthy"] += 1
                            # Clean up unhealthy connection
                            await self._cleanup_dead_websocket(player_id, connection_id)

            # Determine overall health
            total_healthy = health_status["websocket_healthy"]
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

    async def cleanup_dead_connections(self, player_id: uuid.UUID | None = None) -> dict[str, Any]:
        """
        Clean up dead connections for a specific player or all players.

        Args:
            player_id: Optional player ID to clean up. If None, cleans up all players.

        Returns:
            dict: Cleanup results
        """
        cleanup_results: dict[str, Any] = {"players_checked": 0, "connections_cleaned": 0, "errors": []}

        try:
            if player_id:
                # Clean up specific player
                players_to_check = [player_id]
            else:
                # Clean up all players
                players_to_check = list(self.player_websockets.keys())

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
                                except (RuntimeError, ConnectionError, AttributeError) as e:
                                    logger.debug(
                                        "WebSocket cleanup check failed",
                                        player_id=pid,
                                        connection_id=connection_id,
                                        error=str(e),
                                        error_type=type(e).__name__,
                                    )
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

    async def _cleanup_dead_websocket(self, player_id: uuid.UUID, connection_id: str):
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

            # Clean up rate limit data for this connection
            self.rate_limiter.remove_connection_message_data(connection_id)

            logger.info("Cleaned up dead WebSocket connection", connection_id=connection_id, player_id=player_id)
        except Exception as e:
            logger.error(
                "Error cleaning up dead WebSocket", connection_id=connection_id, player_id=player_id, error=str(e)
            )

    async def _check_connection_health(self) -> None:
        """
        Check health of all connections and clean up stale/dead ones.

        This method:
        - Verifies WebSocket state for all active connections
        - Detects stale connections based on last_seen timestamps
        - Cleans up dead connections proactively
        - Updates connection metadata health status

        AI: Periodic health checks prevent memory leaks from dead connections.
        """
        start_time = time.time()
        try:
            now = time.time()
            stale_connections: list[tuple[uuid.UUID, str]] = []  # (player_id, connection_id)

            # Check WebSocket connections
            for connection_id, websocket in list(self.active_websockets.items()):
                try:
                    # Get connection metadata
                    metadata = self.connection_metadata.get(connection_id)
                    if not metadata:
                        # Missing metadata - mark for cleanup
                        # Try to find player_id from player_websockets mapping
                        player_id_for_cleanup: uuid.UUID | None = None
                        for pid, conn_ids in self.player_websockets.items():
                            if connection_id in conn_ids:
                                player_id_for_cleanup = pid
                                break
                        if player_id_for_cleanup is not None:
                            stale_connections.append((player_id_for_cleanup, connection_id))
                        continue

                    # Check if connection is stale (no activity for timeout period)
                    time_since_last_seen = now - metadata.last_seen
                    if time_since_last_seen > self._connection_timeout:
                        logger.debug(
                            "Connection marked as stale",
                            connection_id=connection_id,
                            player_id=metadata.player_id,
                            seconds_idle=time_since_last_seen,
                        )
                        stale_connections.append((metadata.player_id, connection_id))
                        metadata.is_healthy = False
                        continue

                    # Verify WebSocket is actually open
                    if not self._is_websocket_open(websocket):
                        logger.debug(
                            "WebSocket not open, marking for cleanup",
                            connection_id=connection_id,
                            player_id=metadata.player_id,
                        )
                        stale_connections.append((metadata.player_id, connection_id))
                        metadata.is_healthy = False
                        continue

                    # Check token validity if token exists and revalidation interval has passed
                    if metadata.token and metadata.last_token_validation:
                        time_since_validation = now - metadata.last_token_validation
                        if time_since_validation >= self._token_revalidation_interval:
                            if not self._validate_token(metadata.token, metadata.player_id):
                                logger.warning(
                                    "Token validation failed during health check",
                                    connection_id=connection_id,
                                    player_id=metadata.player_id,
                                )
                                stale_connections.append((metadata.player_id, connection_id))
                                metadata.is_healthy = False
                                continue
                            else:
                                # Update last validation time
                                metadata.last_token_validation = now
                                logger.debug(
                                    "Token revalidated successfully",
                                    connection_id=connection_id,
                                    player_id=metadata.player_id,
                                )

                    # Connection is healthy
                    metadata.is_healthy = True

                except Exception as e:
                    logger.warning(
                        "Error checking connection health",
                        connection_id=connection_id,
                        error=str(e),
                    )
                    # Mark for cleanup on error
                    metadata = self.connection_metadata.get(connection_id)
                    if metadata:
                        stale_connections.append((metadata.player_id, connection_id))
                        metadata.is_healthy = False

            # Clean up stale connections
            if stale_connections:
                logger.info(
                    "Cleaning up stale connections from health check",
                    stale_count=len(stale_connections),
                )
                for player_id, connection_id in stale_connections:
                    try:
                        await self._cleanup_dead_websocket(player_id, connection_id)
                    except Exception as e:
                        logger.error(
                            "Error cleaning up stale connection",
                            player_id=player_id,
                            connection_id=connection_id,
                            error=str(e),
                        )

            # Update performance stats
            duration_ms = (time.time() - start_time) * 1000
            self.performance_stats["health_check_times"].append(duration_ms)
            self.performance_stats["total_health_checks"] += 1

            # Keep only recent health check times (last 100)
            if len(self.performance_stats["health_check_times"]) > 100:
                self.performance_stats["health_check_times"] = self.performance_stats["health_check_times"][-100:]

            logger.debug(
                "Connection health check completed",
                duration_ms=duration_ms,
                stale_connections_cleaned=len(stale_connections),
            )

        except Exception as e:
            logger.error("Error in connection health check", error=str(e), exc_info=True)

    async def _periodic_health_check(self) -> None:
        """
        Periodic health check task that runs continuously.

        This task:
        - Runs health checks at configured intervals
        - Handles cancellation gracefully
        - Logs health check statistics

        AI: Background task for proactive connection health monitoring.
        """
        logger.info(
            "Starting periodic connection health checks",
            interval_seconds=self._health_check_interval,
            connection_timeout_seconds=self._connection_timeout,
        )

        try:
            while True:
                await asyncio.sleep(self._health_check_interval)
                await self._check_connection_health()
        except asyncio.CancelledError:
            logger.info("Periodic health check task cancelled")
            raise
        except Exception as e:
            logger.error("Error in periodic health check task", error=str(e), exc_info=True)
            raise

    def start_health_checks(self) -> None:
        """
        Start the periodic health check task.

        This should be called during application startup to begin
        proactive connection health monitoring.

        AI: Creates and tracks the health check task to prevent memory leaks.
        """
        if self._health_check_task is not None and not self._health_check_task.done():
            logger.warning("Health check task already running")
            return

        try:
            from ..app.tracked_task_manager import get_global_tracked_manager

            tracked_manager = get_global_tracked_manager()
            self._health_check_task = tracked_manager.create_tracked_task(
                self._periodic_health_check(),
                task_name="connection_manager/periodic_health_check",
                task_type="connection_manager",
            )
            logger.info("Periodic health check task started")
        except Exception as e:
            logger.error("Error starting health check task", error=str(e), exc_info=True)

    def stop_health_checks(self) -> None:
        """
        Stop the periodic health check task.

        This should be called during application shutdown.
        """
        if self._health_check_task is not None and not self._health_check_task.done():
            logger.info("Stopping periodic health check task")
            self._health_check_task.cancel()
            try:
                # Wait briefly for task to cancel
                try:
                    _ = asyncio.get_running_loop()  # Verify loop exists
                    # Schedule wait in background with proper tracking
                    # AnyIO Pattern: Track background tasks for proper cleanup
                    # Note: This is a short-lived task that completes quickly
                    asyncio.create_task(self._wait_for_task_cancellation(self._health_check_task))
                    # Don't track this specific task as it's very short-lived and self-cleaning
                    # The health check task itself is already tracked separately
                except RuntimeError:
                    # No running loop - task will be cleaned up on next event loop
                    logger.debug("No running loop for health check task cancellation")
            except Exception as e:
                logger.warning("Error waiting for health check task cancellation", error=str(e))
            self._health_check_task = None

    async def _wait_for_task_cancellation(self, task: Any) -> None:
        """Wait for a task to be cancelled, with timeout."""
        try:
            await asyncio.wait_for(task, timeout=5.0)
        except (TimeoutError, asyncio.CancelledError):
            pass
        except Exception as e:
            logger.debug("Task cancellation wait completed", error=str(e))

    def _validate_token(self, token: str, player_id: uuid.UUID) -> bool:
        """
        Validate a JWT token for a connection.

        Args:
            token: JWT token to validate
            player_id: Player ID to verify token matches

        Returns:
            bool: True if token is valid, False otherwise

        AI: Token revalidation ensures connections with expired or revoked tokens are disconnected.
        """
        try:
            from ..auth_utils import decode_access_token

            payload = decode_access_token(token)
            if not payload or "sub" not in payload:
                logger.debug("Token validation failed: invalid payload", player_id=player_id)
                return False

            # Verify player matches token
            user_id = str(payload["sub"]).strip()
            if not self.persistence:
                logger.warning("Cannot validate token: persistence not available", player_id=player_id)
                return False

            player = self.persistence.get_player_by_user_id(user_id)
            # CRITICAL FIX: Compare both as strings - player_id is UUID, player.player_id is also UUID
            if not player or str(player.player_id) != str(player_id):
                logger.warning(
                    "Token validation failed: player mismatch",
                    player_id=player_id,
                    token_user_id=user_id,
                )
                return False

            return True
        except Exception as e:
            logger.error("Error validating token", player_id=player_id, error=str(e), exc_info=True)
            return False

    def get_connection_id_from_websocket(self, websocket: WebSocket) -> str | None:
        """
        Get connection ID from a WebSocket instance.

        Args:
            websocket: The WebSocket connection

        Returns:
            str: Connection ID if found, None otherwise
        """
        # Try to get from websocket custom attribute first
        if hasattr(websocket, "_mythos_connection_id"):
            connection_id = websocket._mythos_connection_id
            if connection_id:
                return connection_id

        # Fallback: search active_websockets
        for conn_id, ws in self.active_websockets.items():
            if ws is websocket:
                return conn_id

        return None

    async def broadcast_to_room(
        self,
        room_id: str,
        event: dict[str, Any],
        exclude_player: uuid.UUID | str | None = None,
    ) -> dict[str, Any]:
        """
        Broadcast a message to all players in a room.

        Args:
            room_id: The room's ID
            event: The event data to send
            exclude_player: Player ID to exclude from broadcast (UUID or string)

        Returns:
            dict: Broadcast delivery statistics
        """
        targets = self.room_manager.get_room_subscribers(room_id)

        broadcast_stats: dict[str, Any] = {
            "room_id": room_id,
            "total_targets": len(targets),
            "excluded_players": 0,
            "successful_deliveries": 0,
            "failed_deliveries": 0,
            "delivery_details": {},
        }

        # Convert exclude_player to string for comparison with targets (room_manager uses strings)
        exclude_player_str = str(exclude_player) if exclude_player else None

        # Debug logging for self-message exclusion
        logger.debug("broadcast_to_room", room_id=room_id, exclude_player=exclude_player_str)
        logger.debug("broadcast_to_room targets", targets=targets)

        # OPTIMIZATION: Batch send messages concurrently to all recipients
        # This significantly improves performance when broadcasting to multiple players
        # Compare with string since targets are strings (room_manager uses strings internally)
        target_list = [pid for pid in targets if pid != exclude_player_str]
        excluded_count = len(targets) - len(target_list)

        if excluded_count > 0:
            broadcast_stats["excluded_players"] = excluded_count

        if target_list:
            # Convert string player IDs to UUIDs for send_personal_message (room_manager uses strings, but send_personal_message expects UUIDs)
            # Keep mapping of string ID to UUID for proper result tracking
            target_mapping: list[tuple[str, uuid.UUID]] = []
            for pid_str in target_list:
                try:
                    pid_uuid = uuid.UUID(pid_str)
                    target_mapping.append((pid_str, pid_uuid))
                except (ValueError, TypeError, AttributeError):
                    logger.warning("Invalid player ID format in room subscribers", player_id=pid_str, room_id=room_id)
                    broadcast_stats["delivery_details"][pid_str] = {
                        "success": False,
                        "error": "Invalid player ID format",
                    }
                    broadcast_stats["failed_deliveries"] += 1
                    continue

            # Send to all targets concurrently using asyncio.gather
            # ARCHITECTURE: Room broadcasts are server-initiated events
            try:
                delivery_results = await asyncio.gather(
                    *[self.send_personal_message(pid_uuid, event) for _pid_str, pid_uuid in target_mapping],
                    return_exceptions=True,
                )

                # Process results (use original string IDs for stats dictionary keys)
                for i, (pid_str, _pid_uuid) in enumerate(target_mapping):
                    if i >= len(delivery_results):
                        continue
                    result = delivery_results[i]
                    if isinstance(result, Exception):
                        logger.error(
                            "Error sending message in batch broadcast",
                            player_id=pid_str,
                            room_id=room_id,
                            error=str(result),
                        )
                        broadcast_stats["delivery_details"][pid_str] = {"success": False, "error": str(result)}
                        broadcast_stats["failed_deliveries"] += 1
                    else:
                        # Type narrowing: result is dict[str, Any] when not an exception
                        delivery_status: dict[str, Any] = result  # type: ignore[assignment]
                        broadcast_stats["delivery_details"][pid_str] = delivery_status
                        if delivery_status["success"]:
                            broadcast_stats["successful_deliveries"] += 1
                        else:
                            broadcast_stats["failed_deliveries"] += 1
            except Exception as e:
                logger.error(
                    "Error in batch broadcast",
                    room_id=room_id,
                    target_count=len(target_list),
                    error=str(e),
                    exc_info=True,
                )
                # Fallback: send individually if batch fails
                for pid_str, pid_uuid in target_mapping:
                    try:
                        delivery_status = await self.send_personal_message(pid_uuid, event)
                        broadcast_stats["delivery_details"][pid_str] = delivery_status
                        if delivery_status["success"]:
                            broadcast_stats["successful_deliveries"] += 1
                        else:
                            broadcast_stats["failed_deliveries"] += 1
                    except Exception as individual_error:
                        logger.error(
                            "Error sending individual message in fallback",
                            player_id=pid_str,
                            error=str(individual_error),
                        )
                        broadcast_stats["failed_deliveries"] += 1

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
        # Get all players with WebSocket connections
        all_players = set(self.player_websockets.keys())

        global_stats: dict[str, Any] = {
            "total_players": len(all_players),
            "excluded_players": 0,
            "successful_deliveries": 0,
            "failed_deliveries": 0,
            "delivery_details": {},
        }

        # OPTIMIZATION: Batch send messages concurrently to all recipients
        target_list = [pid for pid in all_players if pid != exclude_player]
        excluded_count = len(all_players) - len(target_list)

        if excluded_count > 0:
            global_stats["excluded_players"] = excluded_count

        if target_list:
            # Send to all targets concurrently using asyncio.gather
            try:
                delivery_results = await asyncio.gather(
                    *[self.send_personal_message(pid, event) for pid in target_list],
                    return_exceptions=True,
                )

                # Process results
                for i, player_id in enumerate(target_list):
                    result = delivery_results[i]
                    if isinstance(result, Exception):
                        logger.error(
                            "Error sending message in batch global broadcast",
                            player_id=player_id,
                            error=str(result),
                        )
                        global_stats["delivery_details"][player_id] = {"success": False, "error": str(result)}
                        global_stats["failed_deliveries"] += 1
                    else:
                        # Type narrowing: result is dict[str, Any] when not an exception
                        delivery_status: dict[str, Any] = result  # type: ignore[assignment]
                        global_stats["delivery_details"][player_id] = delivery_status
                        if delivery_status["success"]:
                            global_stats["successful_deliveries"] += 1
                        else:
                            global_stats["failed_deliveries"] += 1
            except Exception as e:
                logger.error(
                    "Error in batch global broadcast",
                    target_count=len(target_list),
                    error=str(e),
                    exc_info=True,
                )
                # Fallback: send individually if batch fails
                for player_id in target_list:
                    try:
                        delivery_status = await self.send_personal_message(player_id, event)
                        global_stats["delivery_details"][player_id] = delivery_status
                        if delivery_status["success"]:
                            global_stats["successful_deliveries"] += 1
                        else:
                            global_stats["failed_deliveries"] += 1
                    except Exception as individual_error:
                        logger.error(
                            "Error sending individual message in fallback",
                            player_id=player_id,
                            error=str(individual_error),
                        )
                        global_stats["failed_deliveries"] += 1

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
            result = await self.broadcast_to_room(room_id, event)
            return result

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

    def get_pending_messages(self, player_id: uuid.UUID) -> list[dict[str, Any]]:
        """
        Get pending messages for a player.

        Args:
            player_id: The player's ID

        Returns:
            List[Dict[str, Any]]: List of pending messages
        """
        return self.message_queue.get_messages(str(player_id))

    def _get_player(self, player_id: uuid.UUID) -> Player | None:
        """
        Get a player from the persistence layer.

        Args:
            player_id: The player's ID (UUID)

        Returns:
            Optional[Player]: The player object or None if not found
        """
        if self.persistence is None:
            # Structlog handles UUID objects automatically, no need to convert to string
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

    def _get_players_batch(self, player_ids: list[uuid.UUID]) -> dict[uuid.UUID, Player]:
        """
        Get multiple players from the persistence layer in a single batch operation.

        This method optimizes room occupant lookups by reducing N+1 queries to a single
        batch operation.

        Args:
            player_ids: List of player IDs to retrieve (UUIDs)

        Returns:
            dict: Mapping of player_id to Player object (only includes found players)

        AI: Batch loading eliminates N+1 queries when getting room occupants.
        """
        if self.persistence is None:
            logger.warning("Persistence layer not initialized for batch player lookup", player_count=len(player_ids))
            return {}

        players: dict[uuid.UUID, Player] = {}
        if not player_ids:
            return players

        # Load players in batch - iterate through IDs and get each one
        # Note: If persistence layer supports batch operations in the future, this can be optimized further
        for player_id in player_ids:
            try:
                player = self.persistence.get_player(player_id)
                if player:
                    players[player_id] = player
            except Exception as e:
                # Structlog handles UUID objects automatically, no need to convert to string
                logger.debug("Error loading player in batch", player_id=player_id, error=str(e))

        logger.debug(
            "Batch loaded players",
            requested_count=len(player_ids),
            loaded_count=len(players),
        )
        return players

    def _convert_room_players_uuids_to_names(self, room_data: dict[str, Any]) -> dict[str, Any]:
        """
        Convert player UUIDs and NPC IDs in room_data to names.

        CRITICAL: NEVER send UUIDs or NPC IDs to the client - this is a security issue.
        room.to_dict() returns UUIDs in "players" field and NPC IDs in "npcs" field,
        we must convert both to names.

        Args:
            room_data: Room data dictionary from room.to_dict()

        Returns:
            Modified room_data with players and NPCs as names instead of UUIDs/IDs
        """
        if "players" in room_data and isinstance(room_data["players"], list):
            player_uuids = room_data["players"]
            player_names: list[str] = []
            for player_id_str in player_uuids:
                try:
                    player_id_uuid = uuid.UUID(player_id_str) if isinstance(player_id_str, str) else player_id_str
                    # Get player from batch or individual lookup
                    player_obj = self._get_player(player_id_uuid)
                    if player_obj:
                        # Extract player name - NEVER use UUID as fallback
                        player_name = getattr(player_obj, "name", None)
                        if not player_name or not isinstance(player_name, str) or not player_name.strip():
                            # Try to get name from related User object
                            if hasattr(player_obj, "user"):
                                try:
                                    user = getattr(player_obj, "user", None)
                                    if user:
                                        player_name = getattr(user, "username", None) or getattr(
                                            user, "display_name", None
                                        )
                                except Exception:
                                    pass

                        # Validate name is not UUID
                        if player_name and isinstance(player_name, str) and player_name.strip():
                            is_uuid_string = (
                                len(player_name) == 36
                                and player_name.count("-") == 4
                                and all(c in "0123456789abcdefABCDEF-" for c in player_name)
                            )
                            if not is_uuid_string:
                                player_names.append(player_name)
                except (ValueError, AttributeError):
                    # Skip invalid UUIDs
                    pass
            # Replace UUIDs with names
            room_data["players"] = player_names

        # CRITICAL FIX: Convert NPC IDs to names in room_data
        # room.to_dict() returns NPC IDs in "npcs" field, we must convert to names
        # As documented in "Resurrection and NPC Display Synchronization" - Dr. Armitage, 1930
        # NPC IDs must be resolved to display names before sending to client
        if "npcs" in room_data and isinstance(room_data["npcs"], list):
            npc_ids = room_data["npcs"]
            # Batch load NPC names for efficiency
            npc_names_dict = self._get_npcs_batch(npc_ids)
            npc_names: list[str] = []
            for npc_id in npc_ids:
                npc_name = npc_names_dict.get(npc_id)
                if npc_name and isinstance(npc_name, str) and npc_name.strip():
                    # Validate name is not an ID (check if it looks like an ID with underscores)
                    # NPC IDs typically have format like "npc_type_location_timestamp_instance"
                    # If the "name" is the same as the ID, skip it
                    if npc_name != npc_id:
                        npc_names.append(npc_name)
                    else:
                        # Fallback: Generate name from ID if name resolution failed
                        # This should rarely happen, but provides a safety net
                        fallback_name = npc_id.split("_")[0].replace("_", " ").title()
                        if fallback_name and fallback_name != npc_id:
                            npc_names.append(fallback_name)
            # Replace NPC IDs with names
            room_data["npcs"] = npc_names

        return room_data

    def _get_npcs_batch(self, npc_ids: list[str]) -> dict[str, str]:
        """
        Get NPC names for multiple NPCs in a batch operation.

        Args:
            npc_ids: List of NPC IDs to retrieve names for

        Returns:
            dict: Mapping of npc_id to npc_name (only includes found NPCs)

        AI: Batch loading eliminates N+1 queries when getting NPC names for room occupants.
        """
        npc_names: dict[str, str] = {}
        if not npc_ids:
            return npc_names

        try:
            # Get NPC instance service for batch lookup
            from ..services.npc_instance_service import get_npc_instance_service

            npc_instance_service = get_npc_instance_service()
            if hasattr(npc_instance_service, "lifecycle_manager"):
                lifecycle_manager = npc_instance_service.lifecycle_manager
                if lifecycle_manager:
                    for npc_id in npc_ids:
                        if npc_id in lifecycle_manager.active_npcs:
                            npc_instance = lifecycle_manager.active_npcs[npc_id]
                            name = getattr(npc_instance, "name", None)
                            if name:
                                npc_names[npc_id] = name
                            else:
                                # Fallback: Extract NPC name from the NPC ID
                                npc_names[npc_id] = npc_id.split("_")[0].replace("_", " ").title()
                        else:
                            # Fallback: Extract NPC name from the NPC ID
                            npc_names[npc_id] = npc_id.split("_")[0].replace("_", " ").title()
        except Exception as e:
            logger.debug("Error batch loading NPC names", npc_count=len(npc_ids), error=str(e))
            # Fallback: Generate names from IDs
            for npc_id in npc_ids:
                npc_names[npc_id] = npc_id.split("_")[0].replace("_", " ").title()

        logger.debug(
            "Batch loaded NPC names",
            requested_count=len(npc_ids),
            loaded_count=len(npc_names),
        )
        return npc_names

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

    async def _track_player_connected(self, player_id: uuid.UUID, player: Player, connection_type: str = "unknown"):
        """
        Track when a player connects.

        Args:
            player_id: The player's ID
            player: The player object
            connection_type: Type of connection ("websocket", "unknown")
        """
        try:
            # Check if player is already tracked as online
            is_new_connection = player_id not in self.online_players

            # Determine current player position from stats (defaults to standing)
            position = "standing"
            if hasattr(player, "get_stats"):
                try:
                    stats = player.get_stats()
                    if isinstance(stats, dict):
                        position = stats.get("position", "standing")
                except Exception as exc:
                    logger.warning(
                        "Failed to load player stats during connection",
                        player_id=player_id,
                        error=str(exc),
                    )

            # Type annotation for player_info to help mypy
            connection_types_set: set[str] = set()

            # CRITICAL: Extract player name - NEVER use player_id as fallback
            # Player model has a 'name' column that should always exist (nullable=False)
            player_name = getattr(player, "name", None)
            if not player_name or not isinstance(player_name, str) or not player_name.strip():
                # Try to get name from related User object if player.name is not available
                if hasattr(player, "user"):
                    try:
                        user = getattr(player, "user", None)
                        if user:
                            player_name = getattr(user, "username", None) or getattr(user, "display_name", None)
                    except Exception as e:
                        logger.debug("Error accessing user relationship for player name", error=str(e))

                # If still no name, log warning and use placeholder (NEVER use UUID)
                if not player_name or not isinstance(player_name, str) or not player_name.strip():
                    logger.warning(
                        "Player name not found, using placeholder",
                        player_id=player_id,
                        has_name_attr=hasattr(player, "name"),
                        name_value=getattr(player, "name", "NOT_FOUND"),
                    )
                    player_name = "Unknown Player"

            # CRITICAL: Final validation - ensure player_name is NEVER a UUID
            # This is a defensive check in case player.name somehow contains a UUID
            if isinstance(player_name, str):
                is_uuid_string = (
                    len(player_name) == 36
                    and player_name.count("-") == 4
                    and all(c in "0123456789abcdefABCDEF-" for c in player_name)
                )
                if is_uuid_string:
                    logger.error(
                        "CRITICAL: Player name is a UUID string, this should never happen",
                        player_id=player_id,
                        player_name=player_name,
                        player_name_from_db=getattr(player, "name", "NOT_FOUND"),
                    )
                    # Use placeholder instead of UUID
                    player_name = "Unknown Player"

            player_info: dict[str, Any] = {
                "player_id": player_id,
                "player_name": player_name,
                "level": getattr(player, "level", 1),
                "current_room_id": getattr(player, "current_room_id", None),
                "connected_at": time.time(),
                "connection_types": connection_types_set,
                "total_connections": 0,
                "position": position,
            }

            # If player is already online, update existing info
            if not is_new_connection:
                existing_info = self.online_players[player_id]
                player_info["connected_at"] = existing_info.get("connected_at", time.time())
                existing_types = existing_info.get("connection_types", set())
                player_info["connection_types"] = existing_types if isinstance(existing_types, set) else set()
                player_info["position"] = existing_info.get("position", player_info["position"])

            # Add the new connection type
            connection_types_for_player = player_info["connection_types"]
            if isinstance(connection_types_for_player, set):
                connection_types_for_player.add(connection_type)
            player_info["total_connections"] = len(self.player_websockets.get(player_id, []))

            self.online_players[player_id] = player_info
            self.mark_player_seen(player_id)

            # Only perform these actions for new connections (not additional connections)
            if is_new_connection:
                # Update last_active timestamp in database when player connects
                # Use update_player_last_active instead of save_player to avoid overwriting inventory
                if self.persistence:
                    try:
                        from datetime import UTC, datetime

                        self.persistence.update_player_last_active(player_id, datetime.now(UTC))
                        logger.debug("Updated last_active for player on connection", player_id=player_id)
                    except Exception as e:
                        logger.warning("Failed to update last_active for player", player_id=player_id, error=str(e))

                # Clear any pending messages to ensure fresh game state
                self.message_queue.remove_player_messages(str(player_id))

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
                    self.room_manager.add_room_occupant(str(player_id), room_id)

                    # Prune any stale occupant ids not currently online
                    online_players_str = {str(k): v for k, v in self.online_players.items()}
                    self.room_manager.reconcile_room_presence(room_id, online_players_str)

                    # Add player to the Room object WITHOUT triggering player_entered event
                    # On initial connection, we only send player_entered_game, not player_entered
                    # player_entered events will be triggered when players move between rooms
                    if self.persistence:
                        room = self.persistence.get_room(room_id)
                        if room:
                            # Add player to room's internal set without triggering event (initial connection)
                            player_id_str = str(player_id)
                            if player_id_str not in room._players:
                                room._players.add(player_id_str)
                                logger.info(
                                    "Player added to room on initial connection (no player_entered event)",
                                    player_id=player_id,
                                    room_id=room_id,
                                )
                        else:
                            logger.warning(
                                "Room not found when trying to add player", room_id=room_id, player_id=player_id
                            )

                    # Send initial game_state event to the player
                    await self._send_initial_game_state(player_id, player, room_id)

                    # Broadcast a structured entry event to other occupants (excluding the newcomer)
                    try:
                        from .envelope import build_event

                        # CRITICAL: Extract player name - NEVER use UUID as fallback
                        player_name = getattr(player, "name", None)
                        if not player_name or not isinstance(player_name, str) or not player_name.strip():
                            # Try to get name from related User object if player.name is not available
                            if hasattr(player, "user"):
                                try:
                                    user = getattr(player, "user", None)
                                    if user:
                                        player_name = getattr(user, "username", None) or getattr(
                                            user, "display_name", None
                                        )
                                except Exception as e:
                                    logger.debug("Error accessing user relationship for player name", error=str(e))

                            # If still no name, use placeholder (NEVER use UUID)
                            if not player_name or not isinstance(player_name, str) or not player_name.strip():
                                logger.warning(
                                    "Player name not found, using placeholder",
                                    player_id=player_id,
                                    has_name_attr=hasattr(player, "name"),
                                    name_value=getattr(player, "name", "NOT_FOUND"),
                                )
                                player_name = "Unknown Player"

                        # CRITICAL: Final validation - ensure player_name is NEVER a UUID
                        if isinstance(player_name, str):
                            is_uuid_string = (
                                len(player_name) == 36
                                and player_name.count("-") == 4
                                and all(c in "0123456789abcdefABCDEF-" for c in player_name)
                            )
                            if is_uuid_string:
                                logger.error(
                                    "CRITICAL: Player name is a UUID string, this should never happen",
                                    player_id=player_id,
                                    player_name=player_name,
                                    player_name_from_db=getattr(player, "name", "NOT_FOUND"),
                                )
                                player_name = "Unknown Player"

                        entered_event = build_event(
                            "player_entered_game",
                            {
                                "player_id": player_id,
                                "player_name": player_name,
                            },
                            room_id=room_id,
                        )
                        logger.info(
                            "Broadcasting player_entered_game event",
                            player_id=player_id,
                            room_id=room_id,
                        )
                        await self.broadcast_to_room(room_id, entered_event, exclude_player=player_id)
                    except Exception as broadcast_error:  # pragma: no cover - defensive logging
                        logger.error(
                            "Failed to broadcast player_entered_game event",
                            player_id=player_id,
                            room_id=room_id,
                            error=str(broadcast_error),
                        )

                    # Send room_occupants update so other players see the new occupant in their list
                    # Use the event handler's method to ensure consistent structured format
                    try:
                        event_handler = None
                        if self.app and hasattr(self.app, "state"):
                            event_handler = getattr(self.app.state, "event_handler", None)

                        if event_handler and hasattr(event_handler, "_send_room_occupants_update"):
                            logger.debug(
                                "Sending room_occupants update after player_entered_game",
                                player_id=player_id,
                                room_id=room_id,
                            )
                            await event_handler._send_room_occupants_update(room_id, exclude_player=str(player_id))
                        else:
                            logger.warning(
                                "Event handler not available to send room_occupants update",
                                player_id=player_id,
                                room_id=room_id,
                                has_app=bool(self.app),
                            )
                    except Exception as occupants_error:
                        logger.error(
                            "Failed to send room_occupants update after player connection",
                            player_id=player_id,
                            room_id=room_id,
                            error=str(occupants_error),
                        )

                logger.info("Player presence tracked as connected (new connection)", player_id=player_id)
            else:
                logger.info(
                    "Player additional connection tracked", player_id=player_id, connection_type=connection_type
                )

        except Exception as e:
            logger.error("Error tracking player connection", error=str(e), exc_info=True)

    async def _broadcast_connection_message(self, player_id: uuid.UUID, player: Player) -> None:
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

    async def _track_player_disconnected(self, player_id: uuid.UUID, connection_type: str | None = None) -> None:
        """
        Track when a player disconnects.

        Args:
            player_id: The player's ID
            connection_type: Type of connection being disconnected ("websocket", None for all)
        """
        try:
            # Check if player has any remaining connections
            has_websocket = self.has_websocket_connection(player_id)
            has_any_connections = has_websocket

            # If player still has connections, don't fully disconnect them
            if has_any_connections and connection_type:
                logger.info(
                    "Player still has connections, not fully disconnecting",
                    player_id=player_id,
                    disconnected_connection_type=connection_type,
                )
                return

            # Prevent duplicate disconnect events for the same player
            # CRITICAL FIX: Check BEFORE acquiring lock to prevent race condition
            # BUGFIX: If player is in disconnecting_players but has no connections, force clear the flag
            # This handles the case where a previous disconnect attempt failed and left the player stuck
            if player_id in self.disconnecting_players:
                # Force clear the disconnecting flag since player has no active connections
                logger.warning(
                    "Player was stuck in disconnecting_players, force clearing to allow disconnect",
                    player_id=player_id,
                )
                async with self.disconnect_lock:
                    self.disconnecting_players.discard(player_id)

            # Acquire lock and double-check (to handle race condition between check and lock acquisition)
            async with self.disconnect_lock:
                if player_id in self.disconnecting_players:
                    logger.debug(
                        "DEBUG: Player already being disconnected (post-lock check), skipping duplicate event",
                        player_id=player_id,
                    )
                    return

                # Mark player as being disconnected
                self.disconnecting_players.add(player_id)
                logger.debug("DEBUG: Marked player as disconnecting", player_id=player_id)

            # Resolve player using flexible lookup (ID or name)
            pl = self._get_player(player_id)
            room_id: str | None = getattr(pl, "current_room_id", None) if pl else None
            # CRITICAL: Extract player name - NEVER use UUID as fallback
            player_name: str | None = None
            if pl:
                player_name = getattr(pl, "name", None)
                if not player_name or not isinstance(player_name, str) or not player_name.strip():
                    # Try to get name from related User object if player.name is not available
                    if hasattr(pl, "user"):
                        try:
                            user = getattr(pl, "user", None)
                            if user:
                                player_name = getattr(user, "username", None) or getattr(user, "display_name", None)
                        except Exception as e:
                            logger.debug("Error accessing user relationship for player name", error=str(e))

                    # If still no name, use placeholder (NEVER use UUID)
                    if not player_name or not isinstance(player_name, str) or not player_name.strip():
                        player_name = "Unknown Player"

                # CRITICAL: Final validation - ensure player_name is NEVER a UUID
                if isinstance(player_name, str):
                    is_uuid_string = (
                        len(player_name) == 36
                        and player_name.count("-") == 4
                        and all(c in "0123456789abcdefABCDEF-" for c in player_name)
                    )
                    if is_uuid_string:
                        logger.error(
                            "CRITICAL: Player name is a UUID string, this should never happen",
                            player_id=player_id,
                            player_name=player_name,
                            player_name_from_db=getattr(pl, "name", "NOT_FOUND"),
                        )
                        player_name = "Unknown Player"

            # Remove from online and room presence
            # Remove possible variants (provided id, canonical id, and name)
            keys_to_remove = {player_id}
            keys_to_remove_str: set[str] = set()
            if pl is not None:
                canonical_id = getattr(pl, "player_id", None) or getattr(pl, "user_id", None)
                if canonical_id:
                    if isinstance(canonical_id, uuid.UUID):
                        keys_to_remove.add(canonical_id)
                    else:
                        keys_to_remove_str.add(str(canonical_id))
                if player_name:
                    keys_to_remove_str.add(player_name)

            # CRITICAL: Call room.player_left() BEFORE removing from online_players
            # This ensures the PlayerLeftRoom event is published, which triggers
            # _handle_player_left() in event_handler, which sends structured room_occupants update
            if room_id and self.persistence:
                room = self.persistence.get_room(room_id)
                if room:
                    for key in list(keys_to_remove):
                        player_id_str = str(key)
                        has_player = room.has_player(player_id_str)
                        if has_player:
                            logger.debug(
                                "Calling room.player_left() before disconnect cleanup", player=key, room_id=room_id
                            )
                            room.player_left(player_id_str)
                            # CRITICAL FIX: Wait for PlayerLeftRoom event to be processed
                            # The event is published synchronously but handled asynchronously
                            # We need to yield control to allow the event handler to run
                            import asyncio

                            await asyncio.sleep(0)  # Yield to event loop
                        else:
                            logger.warning(
                                "Player not found in room when trying to call player_left()",
                                player_id=key,
                                room_id=room_id,
                                player_id_str=player_id_str,
                            )

            # Notify current room that player left the game
            # NOTE: Do this BEFORE removing from online_players so the room_occupants
            # update can still query the remaining online players correctly
            # NOTE: room_occupants update will be sent by _handle_player_left() in event_handler
            # when it receives the PlayerLeftRoom event from room.player_left()
            if room_id:
                # Send left-game notification
                from .envelope import build_event

                # CRITICAL: NEVER use UUID as fallback - use placeholder if name not found
                safe_player_name = player_name if player_name else "Unknown Player"
                left_event = build_event(
                    "player_left_game",
                    {"player_id": player_id, "player_name": safe_player_name},
                    room_id=room_id,
                )
                # Exclude the disconnecting player from their own "left game" message
                logger.info("Broadcasting player_left_game", player_id=player_id, room_id=room_id)
                await self.broadcast_to_room(room_id, left_event, exclude_player=player_id)

            # CRITICAL: Remove player from online_players AFTER broadcasting disconnect events
            # This ensures room_occupants updates can still query remaining players correctly
            # Remove UUID keys from online_players
            for key in list(keys_to_remove):
                if key in self.online_players:
                    del self.online_players[key]
                self.room_manager.remove_player_from_all_rooms(str(key))

            # Remove string keys (for backward compatibility with room_manager)
            for str_key in keys_to_remove_str:
                self.room_manager.remove_player_from_all_rooms(str_key)

            # CRITICAL FIX: Clean up all ghost players from all rooms
            self._cleanup_ghost_players()

            # Clean up any remaining references
            if player_id in self.online_players:
                del self.online_players[player_id]
            if player_id in self.last_seen:
                del self.last_seen[player_id]
            self.last_active_update_times.pop(player_id, None)
            self.rate_limiter.remove_player_data(str(player_id))
            self.message_queue.remove_player_messages(str(player_id))

            logger.info("Player presence tracked as disconnected", player_id=player_id)

        except Exception as e:
            logger.error("Error tracking player disconnection", error=str(e), exc_info=True)
        finally:
            # Always remove player from disconnecting set, even on error
            async with self.disconnect_lock:
                self.disconnecting_players.discard(player_id)

    def _cleanup_ghost_players(self) -> None:
        """
        Clean up ghost players from all rooms.

        This method removes players from room's internal _players set
        if they are no longer in the online_players set.
        """
        try:
            if not self.persistence or not hasattr(self.persistence, "_room_cache"):
                return

            # Get all online player IDs (convert to strings for comparison with room._players)
            # CRITICAL FIX: room._players uses string UUIDs, online_players.keys() uses UUID objects
            # We must convert to the same type for set comparison to work correctly
            online_player_ids = {str(pid) for pid in self.online_players.keys()}

            # Get all rooms from the room cache
            for _room_id, room in self.persistence._room_cache.items():
                if not hasattr(room, "_players"):
                    continue

                # Get players in this room (already strings)
                room_player_ids = set(room._players)

                # Find ghost players (players in room but not online)
                # Both sets are now strings, so comparison will work correctly
                potential_ghost_players = room_player_ids - online_player_ids

                if potential_ghost_players:
                    # CRITICAL FIX: Before removing players, verify they actually have NO connections
                    # A player might be in room._players but not in online_players during a race condition
                    # (e.g., during movement, or between connection setup steps)
                    # Only remove players who have ZERO WebSocket connections
                    actual_ghost_players = set()
                    for ghost_player_id_str in potential_ghost_players:
                        try:
                            ghost_player_uuid = uuid.UUID(ghost_player_id_str)
                            # Check if player has ANY WebSocket connections
                            has_connections = self.has_websocket_connection(ghost_player_uuid)
                            if not has_connections:
                                actual_ghost_players.add(ghost_player_id_str)
                            else:
                                logger.debug(
                                    "Player in room but not in online_players - keeping due to active connection",
                                    player_id=ghost_player_id_str,
                                    room_id=room.id,
                                    has_websocket=has_connections,
                                )
                        except (ValueError, AttributeError) as e:
                            # If we can't parse the UUID, it's definitely a ghost
                            logger.warning(
                                "Invalid player ID format in room - removing",
                                player_id=ghost_player_id_str,
                                room_id=room.id,
                                error=str(e),
                            )
                            actual_ghost_players.add(ghost_player_id_str)

                    if actual_ghost_players:
                        logger.debug(
                            "DEBUG: Found actual ghost players in room",
                            room_id=room.id,
                            ghost_players=actual_ghost_players,
                        )
                        for ghost_player_id in actual_ghost_players:
                            room._players.discard(ghost_player_id)
                            logger.debug(
                                "DEBUG: Removed actual ghost player from room",
                                ghost_player_id=ghost_player_id,
                                room_id=room.id,
                            )

        except Exception as e:
            logger.error("Error cleaning up ghost players", error=str(e), exc_info=True)

    async def detect_and_handle_error_state(
        self, player_id: uuid.UUID, error_type: str, error_details: str, connection_id: str | None = None
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
        error_results: dict[str, Any] = {
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
            total_connections = websocket_connections

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
                    "Connection-specific error: Terminating connection",
                    connection_id=connection_id,
                    player_id=player_id,
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
        self, player_id: uuid.UUID, connection_id: str, error_type: str, error_details: str
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
            "WebSocket error",
            player_id=player_id,
            connection_id=connection_id,
            error_type=error_type,
            error_details=error_details,
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

    async def handle_authentication_error(
        self, player_id: uuid.UUID, error_type: str, error_details: str
    ) -> dict[str, Any]:
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
        self, player_id: uuid.UUID, violation_type: str, violation_details: str
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

    async def recover_from_error(self, player_id: uuid.UUID, recovery_type: str = "FULL") -> dict[str, Any]:
        """
        Attempt to recover from an error state for a player.

        Args:
            player_id: The player's ID
            recovery_type: Type of recovery to attempt ("FULL", "CONNECTIONS_ONLY", "SESSION_ONLY")

        Returns:
            dict: Recovery results
        """
        recovery_results: dict[str, Any] = {
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

    def get_player_presence_info(self, player_id: uuid.UUID) -> dict[str, Any]:
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
                "connected_at": None,
                "last_seen": None,
            }

        player_info = self.online_players[player_id]
        websocket_count = len(self.player_websockets.get(player_id, []))

        return {
            "player_id": player_id,
            "is_online": True,
            "connection_types": list(player_info.get("connection_types", set())),
            "total_connections": player_info.get("total_connections", 0),
            "websocket_connections": websocket_count,
            "connected_at": player_info.get("connected_at"),
            "last_seen": self.last_seen.get(player_id),
            "player_name": player_info.get("player_name"),
            "current_room_id": player_info.get("current_room_id"),
            "level": player_info.get("level"),
        }

    def validate_player_presence(self, player_id: uuid.UUID) -> dict[str, Any]:
        """
        Validate player presence and clean up any inconsistencies.

        Args:
            player_id: The player's ID

        Returns:
            dict: Validation results
        """
        validation_results: dict[str, Any] = {
            "player_id": player_id,
            "is_consistent": True,
            "issues_found": [],
            "actions_taken": [],
        }

        try:
            # Check if player is in online_players but has no actual connections
            is_in_online = player_id in self.online_players
            has_websocket = self.has_websocket_connection(player_id)
            has_any_connections = has_websocket

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
                actual_count = len(self.player_websockets.get(player_id, []))

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
        total_connections = total_websockets

        # Count players by connection type
        websocket_only = 0

        for player_id in self.online_players:
            has_ws = self.has_websocket_connection(player_id)

            if has_ws:
                websocket_only += 1

        return {
            "total_online_players": total_online,
            "total_connections": total_connections,
            "websocket_connections": total_websockets,
            "connection_distribution": {
                "websocket_only": websocket_only,
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
            "total_connections": (sum(len(conns) for conns in self.player_websockets.values())),
            "active_sessions": len(self.session_connections),
            "players_with_sessions": len(self.player_sessions),
            "error_log_path": str(error_log_path),
        }

    async def handle_new_login(self, player_id: uuid.UUID):
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

    async def _check_and_process_disconnect(self, player_id: uuid.UUID):
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
        online_players_str = {str(k): v for k, v in self.online_players.items()}
        return self.room_manager.get_room_occupants(room_id, online_players_str)

    async def _send_initial_game_state(self, player_id: uuid.UUID, player: Player, room_id: str):
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
                    # CRITICAL: Convert player UUIDs to names - NEVER send UUIDs to client
                    room_data = self._convert_room_players_uuids_to_names(room_data)

                    logger.info(
                        "DEBUG: Room data",
                        room_id=room_id,
                        npcs=room_data.get("npcs", []),
                        occupant_count=room_data.get("occupant_count", 0),
                    )

            # Get room occupants (players and NPCs)
            occupants = []
            if room_id:
                # Get player occupants
                online_players_str = {str(k): v for k, v in self.online_players.items()}
                occ_infos = self.room_manager.get_room_occupants(room_id, online_players_str)
                for occ_player_info in occ_infos:
                    if isinstance(occ_player_info, dict) and occ_player_info.get("player_id") != player_id:
                        occupants.append(occ_player_info.get("player_name", "Unknown"))

                # CRITICAL FIX: Query NPCs from lifecycle manager instead of Room instance
                # Room instances are recreated from persistence and lose in-memory NPC tracking
                npc_ids: list[str] = []
                try:
                    from ..services.npc_instance_service import get_npc_instance_service

                    npc_instance_service = get_npc_instance_service()
                    if npc_instance_service and hasattr(npc_instance_service, "lifecycle_manager"):
                        lifecycle_manager = npc_instance_service.lifecycle_manager
                        if lifecycle_manager and hasattr(lifecycle_manager, "active_npcs"):
                            active_npcs_dict = lifecycle_manager.active_npcs
                            # Query all active NPCs to find those in this room
                            # BUGFIX: Filter out dead NPCs (is_alive=False) to prevent showing dead NPCs in occupants
                            # As documented in investigation: 2025-11-30_session-001_npc-combat-start-failure.md
                            for npc_id, npc_instance in active_npcs_dict.items():
                                # Skip dead NPCs
                                if not getattr(npc_instance, "is_alive", True):
                                    logger.debug(
                                        "Skipping dead NPC from occupants",
                                        npc_id=npc_id,
                                        npc_name=getattr(npc_instance, "name", "unknown"),
                                        room_id=room_id,
                                    )
                                    continue

                                # Check both current_room and current_room_id for compatibility
                                current_room = getattr(npc_instance, "current_room", None)
                                current_room_id = getattr(npc_instance, "current_room_id", None)
                                npc_room_id = current_room or current_room_id
                                if npc_room_id == room_id:
                                    npc_ids.append(npc_id)

                    logger.info("DEBUG: Room has NPCs from lifecycle manager", room_id=room_id, npc_ids=npc_ids)
                    for npc_id in npc_ids:
                        # Get NPC name from the actual NPC instance, preserving original case from database
                        npc_name = _get_npc_name_from_instance(npc_id)
                        if npc_name:
                            logger.info("DEBUG: Got NPC name from database", npc_name=npc_name, npc_id=npc_id)
                            occupants.append(npc_name)
                        else:
                            # Log warning if NPC instance not found - this should not happen in normal operation
                            logger.warning("NPC instance not found for ID - skipping from room display", npc_id=npc_id)
                except Exception as npc_query_error:
                    logger.warning(
                        "Error querying NPCs from lifecycle manager, falling back to room.get_npcs()",
                        room_id=room_id,
                        error=str(npc_query_error),
                    )
                    # Fallback to room.get_npcs() if lifecycle manager query fails
                    # BUGFIX: Filter fallback NPCs to only include alive NPCs from active_npcs
                    # As documented in investigation: 2025-11-30_session-001_npc-combat-start-failure.md
                    if self.persistence:
                        room = self.persistence.get_room(room_id)
                        if room:
                            room_npc_ids = room.get_npcs()
                            logger.info("DEBUG: Room has NPCs from fallback", room_id=room_id, npc_ids=room_npc_ids)

                            # Filter fallback NPCs: only include those in active_npcs and alive
                            filtered_npc_ids = []
                            try:
                                from ..services.npc_instance_service import get_npc_instance_service

                                npc_instance_service = get_npc_instance_service()
                                if npc_instance_service and hasattr(npc_instance_service, "lifecycle_manager"):
                                    lifecycle_manager = npc_instance_service.lifecycle_manager
                                    if lifecycle_manager and hasattr(lifecycle_manager, "active_npcs"):
                                        for npc_id in room_npc_ids:
                                            if npc_id in lifecycle_manager.active_npcs:
                                                npc_instance = lifecycle_manager.active_npcs[npc_id]
                                                # Only include alive NPCs
                                                if getattr(npc_instance, "is_alive", True):
                                                    filtered_npc_ids.append(npc_id)
                                                else:
                                                    logger.debug(
                                                        "Filtered dead NPC from fallback occupants",
                                                        npc_id=npc_id,
                                                        room_id=room_id,
                                                    )
                            except Exception as filter_error:
                                logger.warning(
                                    "Error filtering fallback NPCs, using all room NPCs",
                                    room_id=room_id,
                                    error=str(filter_error),
                                )
                                filtered_npc_ids = room_npc_ids

                            for npc_id in filtered_npc_ids:
                                npc_name = _get_npc_name_from_instance(npc_id)
                                if npc_name:
                                    occupants.append(npc_name)

            # CRITICAL: Extract player name - NEVER use UUID as fallback
            player_name = getattr(player, "name", None)
            if not player_name or not isinstance(player_name, str) or not player_name.strip():
                # Try to get name from related User object if player.name is not available
                if hasattr(player, "user"):
                    try:
                        user = getattr(player, "user", None)
                        if user:
                            player_name = getattr(user, "username", None) or getattr(user, "display_name", None)
                    except Exception as e:
                        logger.debug("Error accessing user relationship for player name", error=str(e))

                # If still no name, use placeholder (NEVER use UUID)
                if not player_name or not isinstance(player_name, str) or not player_name.strip():
                    player_name = "Unknown Player"

            # CRITICAL: Final validation - ensure player_name is NEVER a UUID
            if isinstance(player_name, str):
                is_uuid_string = (
                    len(player_name) == 36
                    and player_name.count("-") == 4
                    and all(c in "0123456789abcdefABCDEF-" for c in player_name)
                )
                if is_uuid_string:
                    logger.error(
                        "CRITICAL: Player name is a UUID string, this should never happen",
                        player_id=player_id,
                        player_name=player_name,
                        player_name_from_db=getattr(player, "name", "NOT_FOUND"),
                    )
                    player_name = "Unknown Player"

            # Create game_state event
            game_state_data = {
                "player": {
                    "player_id": str(getattr(player, "player_id", player_id)),
                    "name": player_name,
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

            # Calculate connection metrics
            total_websocket_connections = sum(len(conn_ids) for conn_ids in self.player_websockets.values())
            players_with_multiple_connections = sum(
                1 for conn_ids in self.player_websockets.values() if len(conn_ids) > 1
            )

            # Session metrics
            total_sessions = len(self.player_sessions)
            total_session_connections = sum(len(conn_ids) for conn_ids in self.session_connections.values())

            return {
                "memory": memory_stats,
                "connections": {
                    "active_websockets": len(self.active_websockets),
                    "total_connections": len(self.active_websockets),
                    "player_websockets": len(self.player_websockets),
                    "connection_timestamps": len(self.connection_timestamps),
                    # Connection metrics
                    "total_websocket_connections": total_websocket_connections,
                    "players_with_multiple_connections": players_with_multiple_connections,
                    "avg_connections_per_player": total_websocket_connections / len(self.player_websockets)
                    if self.player_websockets
                    else 0,
                },
                "sessions": {
                    "total_sessions": total_sessions,
                    "total_session_connections": total_session_connections,
                    "avg_connections_per_session": total_session_connections / total_sessions
                    if total_sessions > 0
                    else 0,
                    "session_connection_ratio": total_session_connections / total_websocket_connections
                    if total_websocket_connections > 0
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
        Get comprehensive connection statistics.

        Returns:
            dict: Connection statistics including metrics, health, and performance data
        """
        try:
            now = time.time()

            # Calculate connection type distribution
            websocket_only_players = 0
            total_players = len(self.player_websockets)

            for player_id in self.player_websockets.keys():
                has_websocket = len(self.player_websockets[player_id]) > 0

                if has_websocket:
                    websocket_only_players += 1

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
            session_connection_counts: dict[int, int] = {}
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
                    "avg_connections_per_player": (sum(len(conn_ids) for conn_ids in self.player_websockets.values()))
                    / total_players
                    if total_players > 0
                    else 0,
                },
                "timestamp": now,
            }
        except Exception as e:
            logger.error("Error getting connection stats", error=str(e), exc_info=True)
            return {"error": f"Failed to get connection stats: {e}", "timestamp": time.time()}

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
                    "avg_websocket_establishment_ms": sum(websocket_times) / len(websocket_times)
                    if websocket_times
                    else 0,
                    "max_websocket_establishment_ms": max(websocket_times) if websocket_times else 0,
                    "min_websocket_establishment_ms": min(websocket_times) if websocket_times else 0,
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
                    "websocket_health_percentage": 0,  # Would need separate tracking
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
            # CRITICAL: Convert UUID keys to strings for room_manager compatibility
            online_players_str = {str(k): v for k, v in self.online_players.items()}
            occ_infos = self.room_manager.get_room_occupants(room_id, online_players_str)
            names: list[str] = []
            for occ in occ_infos:
                name = occ.get("player_name") if isinstance(occ, dict) else None
                # CRITICAL: Validate name is not a UUID before adding
                if name and isinstance(name, str):
                    # Skip if it looks like a UUID (36 chars, 4 dashes, hex)
                    is_uuid = (
                        len(name) == 36 and name.count("-") == 4 and all(c in "0123456789abcdefABCDEF-" for c in name)
                    )
                    if not is_uuid:
                        names.append(name)
                    else:
                        logger.warning(
                            "Skipping UUID as player name in room_occupants event",
                            name=name,
                            room_id=room_id,
                        )

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
            # CRITICAL: Convert UUID keys to strings for room_manager compatibility
            online_players_str = {str(k): v for k, v in self.online_players.items()}
            occ_infos = self.room_manager.get_room_occupants(room_id, online_players_str)
            names: list[str] = []
            for occ in occ_infos:
                name = occ.get("player_name") if isinstance(occ, dict) else None
                # CRITICAL: Validate name is not a UUID before adding
                if name and isinstance(name, str):
                    # Skip if it looks like a UUID (36 chars, 4 dashes, hex)
                    is_uuid = (
                        len(name) == 36 and name.count("-") == 4 and all(c in "0123456789abcdefABCDEF-" for c in name)
                    )
                    if not is_uuid:
                        names.append(name)
                    else:
                        logger.warning(
                            "Skipping UUID as player name in room_occupants event",
                            name=name,
                            room_id=room_id,
                        )

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


# AI Agent: Global singleton removed - use ApplicationContainer.connection_manager instead
# Migration complete: All production code now uses dependency injection via container
#
# IMPORTANT: Tests must update fixtures to use container.connection_manager
# Importing `connection_manager` as a global will NO LONGER WORK
#
# If you see "NameError: name 'connection_manager' is not defined":
# - In production code: Get from request.app.state.container.connection_manager
# - In tests: Create container and use container.connection_manager
# - In services: Accept as constructor parameter


# --------------------------------------------------------------------------- #
# Legacy compatibility helpers
# --------------------------------------------------------------------------- #

# NOTE: Several existing tests (and some legacy modules) still patch the module-level
# `connection_manager` attribute for dependency injection. The refactored runtime now
# resolves the connection manager through the application container, but we preserve
# this attribute so those tests can continue to function without extensive rewrites.
connection_manager: "ConnectionManager | None" = None


_ASYNC_METHODS_REQUIRING_COMPAT: set[str] = {
    "handle_new_game_session",
    "force_cleanup",
    "check_connection_health",
    "cleanup_orphaned_data",
    "broadcast_room_event",
    "broadcast_global_event",
    "broadcast_global",
    "send_personal_message",
}


def _ensure_async_compat(manager: "ConnectionManager | Any | None") -> "ConnectionManager | Any | None":
    """
    Ensure mocked connection manager implementations expose awaitable methods.

    Many unit tests patch the module-level connection_manager with simple ``Mock``
    instances whose methods are synchronous. Production code awaits these methods,
    so this shim wraps them in AsyncMock/async functions when necessary.
    """
    if manager is None:
        return None

    for method_name in _ASYNC_METHODS_REQUIRING_COMPAT:
        if not hasattr(manager, method_name):
            continue

        attr = getattr(manager, method_name)

        # Already awaitable - nothing to do
        if inspect.iscoroutinefunction(attr) or inspect.isawaitable(attr):
            continue
        if isinstance(attr, AsyncMock):
            continue

        if isinstance(attr, Mock):
            async_mock = AsyncMock()
            # Preserve configured behaviour
            async_mock.side_effect = attr.side_effect
            async_mock.return_value = attr.return_value
            setattr(manager, method_name, async_mock)
            continue

        if callable(attr):

            async def _async_wrapper(*args, _attr=attr, **kwargs):
                result = _attr(*args, **kwargs)
                if inspect.isawaitable(result):
                    return await result
                return result

            setattr(manager, method_name, _async_wrapper)

    return manager


def set_global_connection_manager(manager: "ConnectionManager | None") -> None:
    """
    Update the legacy module-level connection_manager reference.

    Args:
        manager: ConnectionManager instance to expose (or None to clear)
    """
    global connection_manager
    connection_manager = _ensure_async_compat(manager)


def get_global_connection_manager() -> "ConnectionManager | None":
    """
    Retrieve the legacy module-level connection manager if one has been registered.

    Returns:
        Optional[ConnectionManager]: The module-level connection manager instance or None
    """
    return connection_manager


def resolve_connection_manager(candidate: "ConnectionManager | None" = None) -> "ConnectionManager | None":
    """
    Resolve a connection manager instance, preferring an explicitly supplied candidate
    and falling back to the legacy module-level reference.

    Args:
        candidate: Explicit connection manager to prefer.

    Returns:
        Optional[ConnectionManager]: The resolved connection manager instance (if any)
    """
    manager = candidate or connection_manager
    return _ensure_async_compat(manager)


# Utility functions for sending game events
async def send_game_event(player_id: uuid.UUID | str, event_type: str, data: dict) -> None:
    """
    Send a game event to a specific player via WebSocket.

    Args:
        player_id: The player's ID (UUID or string)
        event_type: The type of event
        data: The event data
    """
    try:
        from .envelope import build_event

        connection_manager = resolve_connection_manager()
        if connection_manager is None:
            raise RuntimeError("Connection manager not available")
        # Convert player_id to UUID if it's a string
        if isinstance(player_id, str):
            try:
                player_id_uuid = uuid.UUID(player_id)
            except (ValueError, AttributeError):
                logger.error("Invalid player_id format", player_id=player_id)
                return
        else:
            player_id_uuid = player_id
        # Pass UUID object directly to build_event (it accepts UUID | str)
        await connection_manager.send_personal_message(
            player_id_uuid, build_event(event_type, data, player_id=player_id_uuid)
        )

    except Exception as e:
        logger.error("Error sending game event", player_id=player_id, error=str(e))


async def broadcast_game_event(event_type: str, data: dict, exclude_player: str | None = None) -> None:
    """
    Broadcast a game event to all connected players.

    Args:
        event_type: The type of event
        data: The event data
        exclude_player: Player ID to exclude from broadcast
    """
    try:
        from .envelope import build_event

        connection_manager = resolve_connection_manager()
        if connection_manager is None:
            raise RuntimeError("Connection manager not available")
        await connection_manager.broadcast_global(build_event(event_type, data), exclude_player)

    except Exception as e:
        logger.error("Error broadcasting game event", error=str(e))


async def send_room_event(room_id: str, event_type: str, data: dict, exclude_player: str | None = None) -> None:
    """
    Send a room event to all players in a specific room.

    Args:
        room_id: The room's ID
        event_type: The type of event
        data: The event data
        exclude_player: Player ID to exclude from broadcast
    """
    try:
        from .envelope import build_event

        connection_manager = resolve_connection_manager()
        if connection_manager is None:
            raise RuntimeError("Connection manager not available")
        await connection_manager.broadcast_to_room(
            room_id,
            build_event(event_type, data, room_id=room_id),
            exclude_player,
        )

    except Exception as e:
        logger.error("Error sending room event", room_id=room_id, error=str(e))


async def send_system_notification(player_id: uuid.UUID | str, message: str, notification_type: str = "info") -> None:
    """
    Send a system notification to a player.

    Args:
        player_id: The player's ID
        message: The notification message
        notification_type: The type of notification (info, warning, error)
    """
    try:
        notification_data = {
            "message": message,
            "notification_type": notification_type,
        }

        await send_game_event(player_id, "system_notification", notification_data)

    except Exception as e:
        logger.error("Error sending system notification", player_id=player_id, error=str(e))


async def send_player_status_update(player_id: uuid.UUID | str, status_data: dict) -> None:
    """
    Send a player status update to a player.

    Args:
        player_id: The player's ID
        status_data: The status data to send
    """
    try:
        await send_game_event(player_id, "player_status", status_data)

    except Exception as e:
        logger.error("Error sending status update", player_id=player_id, error=str(e))


async def send_room_description(player_id: uuid.UUID | str, room_data: dict) -> None:
    """
    Send room description to a player.

    Args:
        player_id: The player's ID
        room_data: The room data to send
    """
    try:
        await send_game_event(player_id, "room_description", room_data)

    except Exception as e:
        logger.error("Error sending room description", player_id=player_id, error=str(e))
