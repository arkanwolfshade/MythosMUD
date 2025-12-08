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
from typing import Any
from unittest.mock import AsyncMock, Mock

from fastapi import WebSocket
from starlette.websockets import WebSocketState

from ..logging.enhanced_logging_config import get_logger
from ..models import Player
from .errors.error_handler import ConnectionErrorHandler
from .integration.game_state_provider import GameStateProvider
from .integration.room_event_handler import RoomEventHandler
from .maintenance.connection_cleaner import ConnectionCleaner
from .memory_monitor import MemoryMonitor
from .message_queue import MessageQueue
from .messaging.message_broadcaster import MessageBroadcaster
from .messaging.personal_message_sender import PersonalMessageSender
from .monitoring.health_monitor import HealthMonitor
from .monitoring.performance_tracker import PerformanceTracker
from .monitoring.statistics_aggregator import StatisticsAggregator
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


# AI Agent: PerformanceStats moved to monitoring/performance_tracker.py


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
        self.async_persistence: Any | None = (
            None  # ARCHITECTURAL FIX: Use async_persistence instead of sync persistence
        )
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

        # Initialize modular components
        self.memory_monitor = MemoryMonitor()
        self.rate_limiter = RateLimiter()
        self.message_queue = MessageQueue(max_messages_per_player=self.memory_monitor.max_pending_messages)
        self.room_manager = RoomSubscriptionManager()
        self.performance_tracker = PerformanceTracker(max_samples=1000)
        self.statistics_aggregator = StatisticsAggregator(
            memory_monitor=self.memory_monitor,
            rate_limiter=self.rate_limiter,
            message_queue=self.message_queue,
            room_manager=self.room_manager,
            performance_tracker=self.performance_tracker,
        )
        # Initialize specialized components (require callbacks, set after other components)
        self.health_monitor: HealthMonitor | None = None
        self.error_handler: ConnectionErrorHandler | None = None
        self.connection_cleaner: ConnectionCleaner | None = None
        self.game_state_provider: GameStateProvider | None = None
        self.room_event_handler: RoomEventHandler | None = None
        self.personal_message_sender: PersonalMessageSender | None = None
        self.message_broadcaster: MessageBroadcaster | None = None

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

        # Initialize specialized components with callbacks
        self._initialize_health_monitor()
        self._initialize_error_handler()
        self._initialize_connection_cleaner()
        self._initialize_game_state_provider()
        self._initialize_messaging()
        self._initialize_room_event_handler()

    def _initialize_health_monitor(self) -> None:
        """Initialize the health monitor with required callbacks."""
        self.health_monitor = HealthMonitor(
            is_websocket_open_callback=self._is_websocket_open,
            validate_token_callback=self._validate_token,
            cleanup_dead_websocket_callback=self._cleanup_dead_websocket,
            performance_tracker=self.performance_tracker,
            health_check_interval=self._health_check_interval,
            connection_timeout=self._connection_timeout,
            token_revalidation_interval=self._token_revalidation_interval,
        )

    def _initialize_error_handler(self) -> None:
        """Initialize the error handler with required callbacks."""
        self.error_handler = ConnectionErrorHandler(
            force_disconnect_callback=self.force_disconnect_player,
            disconnect_connection_callback=self.disconnect_connection_by_id,
            cleanup_dead_connections_callback=self.cleanup_dead_connections,
            get_player_session_callback=self.get_player_session,
            get_session_connections_callback=self.get_session_connections,
            get_player_websockets=lambda pid: self.player_websockets.get(pid, []),
            get_online_players=lambda: self.online_players,
            get_session_connections=lambda: self.session_connections,
            get_player_sessions=lambda: self.player_sessions,
        )

    def _initialize_connection_cleaner(self) -> None:
        """Initialize the connection cleaner with required callbacks."""
        self.connection_cleaner = ConnectionCleaner(
            memory_monitor=self.memory_monitor,
            rate_limiter=self.rate_limiter,
            message_queue=self.message_queue,
            room_manager=self.room_manager,
            cleanup_dead_websocket_callback=self._cleanup_dead_websocket,
            has_websocket_connection_callback=self.has_websocket_connection,
            get_async_persistence=lambda: self.async_persistence,
        )

    def _initialize_game_state_provider(self) -> None:
        """Initialize the game state provider with required callbacks."""
        self.game_state_provider = GameStateProvider(
            room_manager=self.room_manager,
            get_async_persistence=lambda: self.async_persistence,
            send_personal_message_callback=self.send_personal_message,
            get_app=lambda: self.app,
        )

    def _initialize_messaging(self) -> None:
        """Initialize messaging components with required callbacks."""
        self.personal_message_sender = PersonalMessageSender(
            message_queue=self.message_queue,
            cleanup_dead_websocket_callback=self._cleanup_dead_websocket,
            convert_uuids_to_strings=self._convert_uuids_to_strings,
        )
        self.message_broadcaster = MessageBroadcaster(
            room_manager=self.room_manager,
            send_personal_message_callback=self.send_personal_message,
        )

    def _initialize_room_event_handler(self) -> None:
        """Initialize the room event handler with required callbacks."""
        self.room_event_handler = RoomEventHandler(
            room_manager=self.room_manager,
            get_event_bus=lambda: self._event_bus,
            get_event_publisher=lambda: self.event_publisher,
            broadcast_to_room_callback=self.broadcast_to_room,
            get_online_players=lambda: self.online_players,
        )

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

    def canonical_room_id(self, room_id: str | None) -> str | None:
        """
        Resolve a room id to the canonical Room.id value (public method).

        Args:
            room_id: The room ID to resolve

        Returns:
            Optional[str]: The canonical room ID or the original ID if resolution fails
        """
        return self._canonical_room_id(room_id)

    def _canonical_room_id(self, room_id: str | None) -> str | None:
        """Resolve a room id to the canonical Room.id value (compatibility method)."""
        # Use room manager's persistence if available, otherwise use main persistence layer
        # Both use the same async_persistence instance, so we can use either
        try:
            if not room_id:
                return room_id

            # Try room manager's persistence first (public attribute access)
            if self.room_manager.async_persistence is not None:
                room = self.room_manager.async_persistence.get_room_by_id(room_id)  # Sync method, uses cache
                if room is not None and getattr(room, "id", None):
                    return room.id

            # Fallback to main persistence layer for compatibility
            if self.async_persistence is not None:
                room = self.async_persistence.get_room_by_id(room_id)  # Sync method, uses cache
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

    def set_async_persistence(self, async_persistence):
        """Set the async persistence layer reference for all components."""
        self.async_persistence = async_persistence
        self.room_manager.set_async_persistence(async_persistence)

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
                                raise ConnectionError("WebSocket not connected")
                        except ConnectionError as ping_error:
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

            # Accept the WebSocket connection without subprotocol
            # CRITICAL FIX: Token is now passed via query parameter, not subprotocol
            # No subprotocol negotiation needed
            await websocket.accept()
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
            player = await self._get_player(player_id)
            if not player:
                if self.async_persistence is None:
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
        self.performance_tracker.record_connection_establishment("websocket", duration_ms)

        return True

    async def disconnect_websocket(self, player_id: uuid.UUID, is_force_disconnect: bool = False):
        """
        Disconnect all WebSocket connections for a player.

        Args:
            player_id: The player's ID (UUID)
            is_force_disconnect: If True, don't broadcast player_left_game
        """
        # Use disconnect_lock to prevent concurrent disconnects for the same player
        # Initialize should_track_disconnect before the try block to ensure it's always defined
        should_track_disconnect = False
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

            if self.async_persistence:
                last_update = self.last_active_update_times.get(player_id, 0.0)
                if now_ts - last_update >= self.last_active_update_interval:
                    try:
                        # Fire-and-forget async call - not critical for event loop blocking
                        # Update timestamp immediately to prevent rapid retries
                        self.last_active_update_times[player_id] = now_ts
                        # Try to create task if event loop is running, otherwise skip (non-critical)
                        try:
                            loop = asyncio.get_running_loop()
                            loop.create_task(self.async_persistence.update_player_last_active(player_id))
                        except RuntimeError:
                            # No running loop - skip update (non-critical)
                            pass
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
        if self.connection_cleaner is None:
            logger.error("Connection cleaner not initialized")
            return
        self.connection_cleaner.prune_stale_players(
            last_seen=self.last_seen,
            online_players=self.online_players,
            player_websockets=self.player_websockets,
            active_websockets=self.active_websockets,
            last_active_update_times=self.last_active_update_times,
            max_age_seconds=max_age_seconds,
        )

    async def cleanup_orphaned_data(self):
        """Clean up orphaned data that might accumulate over time."""
        if self.connection_cleaner is None:
            logger.error("Connection cleaner not initialized")
            return
        await self.connection_cleaner.cleanup_orphaned_data(
            connection_timestamps=self.connection_timestamps,
            active_websockets=self.active_websockets,
            cleanup_stats=self.cleanup_stats,
        )

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
        """Send a personal message to a player via WebSocket."""
        if self.personal_message_sender is None:
            logger.error("Personal message sender not initialized")
            return {"success": False}
        return await self.personal_message_sender.send_message(
            player_id=player_id,
            event=event,
            player_websockets=self.player_websockets,
            active_websockets=self.active_websockets,
        )

    async def send_personal_message_old(self, player_id: uuid.UUID, event: dict[str, Any]) -> dict[str, Any]:
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
        """Get message delivery statistics for a player."""
        if self.personal_message_sender is None:
            logger.error("Personal message sender not initialized")
            return {"player_id": player_id}
        return self.personal_message_sender.get_delivery_stats(
            player_id=player_id, player_websockets=self.player_websockets
        )

    async def check_connection_health(self, player_id: uuid.UUID) -> dict[str, Any]:
        """
        Check the health of all connections for a player.

        Args:
            player_id: The player's ID

        Returns:
            dict: Connection health information
        """
        if self.health_monitor is None:
            logger.error("Health monitor not initialized")
            return {"player_id": player_id, "overall_health": "error"}
        return await self.health_monitor.check_player_connection_health(
            player_id=player_id, player_websockets=self.player_websockets, active_websockets=self.active_websockets
        )

    async def cleanup_dead_connections(self, player_id: uuid.UUID | None = None) -> dict[str, Any]:
        """
        Clean up dead connections for a specific player or all players.

        Args:
            player_id: Optional player ID to clean up. If None, cleans up all players.

        Returns:
            dict: Cleanup results
        """
        if self.connection_cleaner is None:
            logger.error("Connection cleaner not initialized")
            return {"players_checked": 0, "connections_cleaned": 0, "errors": ["Connection cleaner not initialized"]}
        return await self.connection_cleaner.cleanup_dead_connections(
            player_websockets=self.player_websockets, active_websockets=self.active_websockets, player_id=player_id
        )

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

        AI: Delegates to HealthMonitor for modular health checking.
        """
        if self.health_monitor is None:
            logger.error("Health monitor not initialized")
            return
        await self.health_monitor.check_all_connections_health(
            active_websockets=self.active_websockets,
            connection_metadata=self.connection_metadata,
            player_websockets=self.player_websockets,
        )

    async def _periodic_health_check(self) -> None:
        """
        Periodic health check task that runs continuously.

        AI: Delegates to HealthMonitor for periodic health checking.
        """
        if self.health_monitor is None:
            logger.error("Health monitor not initialized")
            return
        await self.health_monitor.periodic_health_check_task(
            active_websockets=self.active_websockets,
            connection_metadata=self.connection_metadata,
            player_websockets=self.player_websockets,
        )

    def start_health_checks(self) -> None:
        """
        Start the periodic health check task.

        This should be called during application startup to begin
        proactive connection health monitoring.

        AI: Delegates to HealthMonitor for task management.
        """
        if self.health_monitor is None:
            logger.error("Health monitor not initialized")
            return
        self.health_monitor.start_periodic_checks(
            active_websockets=self.active_websockets,
            connection_metadata=self.connection_metadata,
            player_websockets=self.player_websockets,
        )

    def stop_health_checks(self) -> None:
        """
        Stop the periodic health check task.

        This should be called during application shutdown.

        AI: Delegates to HealthMonitor for task management.
        """
        if self.health_monitor is None:
            logger.error("Health monitor not initialized")
            return
        self.health_monitor.stop_periodic_checks()

    async def _validate_token(self, token: str, player_id: uuid.UUID) -> bool:
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
            if not self.async_persistence:
                logger.warning("Cannot validate token: persistence not available", player_id=player_id)
                return False

            player = await self.async_persistence.get_player_by_user_id(user_id)
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
        # Search active_websockets to find the connection ID
        # This avoids accessing protected members on the WebSocket object
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
        """Broadcast a message to all players in a room."""
        if self.message_broadcaster is None:
            logger.error("Message broadcaster not initialized")
            return {"room_id": room_id, "total_targets": 0}
        return await self.message_broadcaster.broadcast_to_room(
            room_id=room_id, event=event, exclude_player=exclude_player, player_websockets=self.player_websockets
        )

    async def broadcast_global(self, event: dict[str, Any], exclude_player: str | None = None) -> dict[str, Any]:
        """Broadcast a message to all connected players."""
        if self.message_broadcaster is None:
            logger.error("Message broadcaster not initialized")
            return {"total_players": 0}
        return await self.message_broadcaster.broadcast_global(
            event=event, exclude_player=exclude_player, player_websockets=self.player_websockets
        )

    async def broadcast_room_event(self, event_type: str, room_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Broadcast a room-specific event to all players in the room."""
        try:
            from .envelope import build_event

            event = build_event(event_type, data)
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
        """Broadcast a global event to all connected players."""
        try:
            from .envelope import build_event

            event = build_event(event_type, data)
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

    async def _get_player(self, player_id: uuid.UUID) -> Player | None:
        """Get a player from the persistence layer (async version)."""
        if self.game_state_provider is None:
            logger.error("Game state provider not initialized")
            return None
        return await self.game_state_provider.get_player(player_id)

    async def _get_players_batch(self, player_ids: list[uuid.UUID]) -> dict[uuid.UUID, Player]:
        """Get multiple players from the persistence layer in a single batch operation."""
        if self.game_state_provider is None:
            logger.error("Game state provider not initialized")
            return {}
        return await self.game_state_provider.get_players_batch(player_ids)

    async def _convert_room_players_uuids_to_names(self, room_data: dict[str, Any]) -> dict[str, Any]:
        """Convert player UUIDs and NPC IDs in room_data to names."""
        if self.game_state_provider is None:
            logger.error("Game state provider not initialized")
            return room_data
        return await self.game_state_provider.convert_room_uuids_to_names(room_data)

    def _get_npcs_batch(self, npc_ids: list[str]) -> dict[str, str]:
        """Get NPC names for multiple NPCs in a batch operation."""
        if self.game_state_provider is None:
            logger.error("Game state provider not initialized")
            return {}
        return self.game_state_provider.get_npcs_batch(npc_ids)

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
                if self.async_persistence:
                    try:
                        await self.async_persistence.update_player_last_active(player_id)
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
                if self.async_persistence and room_id:
                    room = self.async_persistence.get_room_by_id(room_id)  # Sync method, uses cache
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
                    if self.async_persistence:
                        room = self.async_persistence.get_room_by_id(room_id)  # Sync method, uses cache
                        if room:
                            # Add player to room's internal set without triggering event (initial connection)
                            if not room.has_player(player_id):
                                room.add_player_silently(player_id)
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

                        if event_handler and hasattr(event_handler, "send_room_occupants_update"):
                            logger.debug(
                                "Sending room_occupants update after player_entered_game",
                                player_id=player_id,
                                room_id=room_id,
                            )
                            await event_handler.send_room_occupants_update(room_id, exclude_player=str(player_id))
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
            if self.async_persistence and room_id:
                room = self.async_persistence.get_room_by_id(room_id)  # Sync method, uses cache
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
            pl = await self._get_player(player_id)
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
            if room_id and self.async_persistence:
                room = self.async_persistence.get_room_by_id(room_id)  # Sync method, uses cache
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
        if self.connection_cleaner is None:
            logger.error("Connection cleaner not initialized")
            return
        self.connection_cleaner.cleanup_ghost_players(online_players=self.online_players)

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
        if self.error_handler is None:
            logger.error("Error handler not initialized")
            return {
                "player_id": player_id,
                "error_type": error_type,
                "success": False,
                "errors": ["Error handler not initialized"],
            }
        return await self.error_handler.detect_and_handle_error_state(
            player_id, error_type, error_details, connection_id
        )

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
        if self.error_handler is None:
            logger.error("Error handler not initialized")
            return {"player_id": player_id, "success": False, "errors": ["Error handler not initialized"]}
        return await self.error_handler.handle_websocket_error(player_id, connection_id, error_type, error_details)

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
        if self.error_handler is None:
            logger.error("Error handler not initialized")
            return {"player_id": player_id, "success": False, "errors": ["Error handler not initialized"]}
        return await self.error_handler.handle_authentication_error(player_id, error_type, error_details)

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
        if self.error_handler is None:
            logger.error("Error handler not initialized")
            return {"player_id": player_id, "success": False, "errors": ["Error handler not initialized"]}
        return await self.error_handler.handle_security_violation(player_id, violation_type, violation_details)

    async def recover_from_error(self, player_id: uuid.UUID, recovery_type: str = "FULL") -> dict[str, Any]:
        """
        Attempt to recover from an error state for a player.

        Args:
            player_id: The player's ID
            recovery_type: Type of recovery to attempt ("FULL", "CONNECTIONS_ONLY", "SESSION_ONLY")

        Returns:
            dict: Recovery results
        """
        if self.error_handler is None:
            logger.error("Error handler not initialized")
            return {"player_id": player_id, "success": False, "errors": ["Error handler not initialized"]}
        return await self.error_handler.recover_from_error(player_id, recovery_type)

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
        if self.error_handler is None:
            logger.error("Error handler not initialized")
            return {}
        return self.error_handler.get_error_statistics(
            online_players=self.online_players, player_websockets=self.player_websockets
        )

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
            with open(login_log_path, "a", encoding="utf-8") as f:
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

    async def get_room_occupants(self, room_id: str) -> list[dict[str, Any]]:
        """Get list of occupants in a room."""
        if self.game_state_provider is None:
            logger.error("Game state provider not initialized")
            return []
        return await self.game_state_provider.get_room_occupants(room_id=room_id, online_players=self.online_players)

    async def _send_initial_game_state(self, player_id: uuid.UUID, player: Player, room_id: str):
        """Send initial game_state event to a newly connected player."""
        if self.game_state_provider is None:
            logger.error("Game state provider not initialized")
            return
        await self.game_state_provider.send_initial_game_state(
            player_id=player_id, player=player, room_id=room_id, online_players=self.online_players
        )

    async def _check_and_cleanup(self):
        """Periodically check for cleanup conditions and perform cleanup if needed."""
        if self.connection_cleaner is None:
            logger.error("Connection cleaner not initialized")
            return
        await self.connection_cleaner.check_and_cleanup(
            online_players=self.online_players,
            last_seen=self.last_seen,
            player_websockets=self.player_websockets,
            active_websockets=self.active_websockets,
            connection_timestamps=self.connection_timestamps,
            cleanup_stats=self.cleanup_stats,
            last_active_update_times=self.last_active_update_times,
        )

    def get_memory_stats(self) -> dict[str, Any]:
        """Get comprehensive memory and connection statistics."""
        return self.statistics_aggregator.get_memory_stats(
            active_websockets=self.active_websockets,
            player_websockets=self.player_websockets,
            connection_timestamps=self.connection_timestamps,
            cleanup_stats=self.cleanup_stats,
            player_sessions=self.player_sessions,
            session_connections=self.session_connections,
            online_players=self.online_players,
            last_seen=self.last_seen,
        )

    def get_dual_connection_stats(self) -> dict[str, Any]:
        """
        Get comprehensive connection statistics.

        Returns:
            dict: Connection statistics including metrics, health, and performance data
        """
        return self.statistics_aggregator.get_connection_stats(
            player_websockets=self.player_websockets,
            connection_metadata=self.connection_metadata,
            session_connections=self.session_connections,
            player_sessions=self.player_sessions,
        )

    def get_performance_stats(self) -> dict[str, Any]:
        """
        Get connection performance statistics.

        Returns:
            dict: Performance statistics including timing data and averages
        """
        return self.performance_tracker.get_stats()

    def get_connection_health_stats(self) -> dict[str, Any]:
        """
        Get comprehensive connection health statistics.

        Returns:
            dict: Connection health statistics including health distribution and trends
        """
        return self.statistics_aggregator.get_connection_health_stats(connection_metadata=self.connection_metadata)

    def get_memory_alerts(self) -> list[str]:
        """Get memory-related alerts."""
        return self.statistics_aggregator.get_memory_alerts(
            connection_timestamps=self.connection_timestamps, max_connection_age=self.memory_monitor.max_connection_age
        )

    async def force_cleanup(self):
        """Force immediate cleanup of all orphaned data."""
        if self.connection_cleaner is None:
            logger.error("Connection cleaner not initialized")
            return
        await self.connection_cleaner.force_cleanup(
            online_players=self.online_players,
            last_seen=self.last_seen,
            player_websockets=self.player_websockets,
            active_websockets=self.active_websockets,
            connection_timestamps=self.connection_timestamps,
            cleanup_stats=self.cleanup_stats,
            last_active_update_times=self.last_active_update_times,
            cleanup_orphaned_data_callback=self.cleanup_orphaned_data,
            prune_stale_players_callback=self.prune_stale_players,
        )

    # --- Event Subscription Methods ---

    def set_event_bus(self, event_bus: Any) -> None:
        """
        Set the event bus for the connection manager.

        This public method allows external code to set the event bus
        without accessing the protected _event_bus member.

        Args:
            event_bus: The EventBus instance to set
        """
        self._event_bus = event_bus

    def _get_event_bus(self):
        """Get the event bus from connection manager."""
        # Event bus is already available on connection_manager
        return self._event_bus

    async def subscribe_to_room_events(self):
        """Subscribe to room movement events for occupant broadcasting."""
        event_bus = self._get_event_bus()
        if not event_bus:
            logger.warning("No event bus available for room event subscription")
            return

        try:
            from ..events.event_types import PlayerEnteredRoom, PlayerLeftRoom

            # Subscribe using ConnectionManager methods (which delegate to room_event_handler)
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

    async def _handle_player_entered_room(self, event_data: dict[str, Any]):
        """Handle PlayerEnteredRoom events by broadcasting updated occupant count."""
        if self.room_event_handler is None:
            logger.error("Room event handler not initialized")
            return
        await self.room_event_handler.handle_player_entered_room(event_data)

    async def _handle_player_left_room(self, event_data: dict[str, Any]):
        """Handle PlayerLeftRoom events by broadcasting updated occupant count."""
        if self.room_event_handler is None:
            logger.error("Room event handler not initialized")
            return
        await self.room_event_handler.handle_player_left_room(event_data)


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

        manager = resolve_connection_manager()
        if manager is None:
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
        await manager.send_personal_message(player_id_uuid, build_event(event_type, data, player_id=player_id_uuid))

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

        manager = resolve_connection_manager()
        if manager is None:
            raise RuntimeError("Connection manager not available")
        await manager.broadcast_global(build_event(event_type, data), exclude_player)

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

        manager = resolve_connection_manager()
        if manager is None:
            raise RuntimeError("Connection manager not available")
        await manager.broadcast_to_room(
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
