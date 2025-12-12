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
from typing import Any

from fastapi import WebSocket

from ..logging.enhanced_logging_config import get_logger
from ..models import Player
from .connection_compatibility import attach_compatibility_properties
from .connection_delegates import cleanup_dead_websocket_impl, validate_token_impl
from .connection_disconnection import (
    cleanup_websocket_disconnect,
    disconnect_connection_by_id_impl,
)
from .connection_establishment import establish_websocket_connection
from .connection_helpers import (
    handle_new_login_impl,
    mark_player_seen_impl,
    send_personal_message_old_impl,
)
from .connection_initialization import (
    initialize_connection_cleaner,
    initialize_error_handler,
    initialize_game_state_provider,
    initialize_health_monitor,
    initialize_messaging,
    initialize_room_event_handler,
)
from .connection_manager_methods import (
    broadcast_global_event_impl,
    broadcast_global_impl,
    broadcast_room_event_impl,
    broadcast_to_room_impl,
    canonical_room_id_public_impl,
    check_and_cleanup_impl,
    check_connection_health_impl,
    cleanup_dead_connections_impl,
    cleanup_ghost_players_impl,
    cleanup_orphaned_data_impl,
    convert_room_players_uuids_to_names_impl,
    convert_uuids_to_strings_impl,
    detect_and_handle_error_state_impl,
    disconnect_websocket_connection_impl,
    force_cleanup_impl,
    force_disconnect_player_impl,
    get_active_connection_count_impl,
    get_connection_count_impl,
    get_connection_health_stats_impl,
    get_connection_id_from_websocket_impl,
    get_dual_connection_stats_impl,
    get_error_statistics_impl,
    get_memory_alerts_impl,
    get_memory_stats_impl,
    get_message_delivery_stats_impl,
    get_next_sequence_impl,
    get_npcs_batch_impl,
    get_online_player_by_display_name_method,
    get_online_players_impl,
    get_pending_messages_impl,
    get_performance_stats_impl,
    get_player_impl,
    get_player_presence_info_method,
    get_player_session_impl,
    get_player_websocket_connection_id_impl,
    get_players_batch_impl,
    get_rate_limit_info_impl,
    get_room_occupants_impl,
    get_session_connections_impl,
    handle_authentication_error_impl,
    handle_player_entered_room_impl,
    handle_player_left_room_impl,
    handle_security_violation_impl,
    handle_websocket_error_impl,
    has_websocket_connection_impl,
    is_websocket_open_impl,
    prune_stale_players_impl,
    recover_from_error_impl,
    safe_close_websocket_impl,
    send_initial_game_state_impl,
    send_personal_message_impl,
    start_health_checks_impl,
    stop_health_checks_impl,
    subscribe_to_room_events_impl,
    subscribe_to_room_impl,
    unsubscribe_from_room_events_impl,
    unsubscribe_from_room_impl,
    validate_player_presence_method,
    validate_session_impl,
)
from .connection_models import ConnectionMetadata
from .connection_room_utils import (
    canonical_room_id_impl,
    prune_player_from_all_rooms_impl,
    reconcile_room_presence_impl,
)
from .connection_session_management import handle_new_game_session_impl
from .connection_statistics import get_presence_statistics_impl, get_session_stats_impl
from .connection_utils import get_npc_name_from_instance
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
from .player_presence_tracker import (
    broadcast_connection_message_impl,
    track_player_connected_impl,
    track_player_disconnected_impl,
)
from .rate_limiter import RateLimiter
from .room_subscription_manager import RoomSubscriptionManager

logger = get_logger(__name__)

# Backward compatibility: Export old private function name
_get_npc_name_from_instance = get_npc_name_from_instance


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
        initialize_health_monitor(self)
        initialize_error_handler(self)
        initialize_connection_cleaner(self)
        initialize_game_state_provider(self)
        initialize_messaging(self)
        initialize_room_event_handler(self)

    def _is_websocket_open(self, websocket: WebSocket) -> bool:
        """Check if a WebSocket is open."""
        return is_websocket_open_impl(self, websocket)

    def is_websocket_closed(self, ws_id: int) -> bool:
        """Check if a WebSocket ID is in the closed set."""
        return ws_id in self._closed_websockets

    def mark_websocket_closed(self, ws_id: int) -> None:
        """Mark a WebSocket ID as closed."""
        self._closed_websockets.add(ws_id)

    async def _safe_close_websocket(
        self, websocket: WebSocket, code: int = 1000, reason: str = "Connection closed"
    ) -> None:
        """Safely close a WebSocket connection."""
        await safe_close_websocket_impl(self, websocket, code, reason)

    # Compatibility properties attached by attach_compatibility_properties below

    # Compatibility methods for WebSocket connection system
    def get_player_websocket_connection_id(self, player_id: uuid.UUID) -> str | None:
        """Get the first WebSocket connection ID for a player (backward compatibility)."""
        return get_player_websocket_connection_id_impl(self, player_id)

    def has_websocket_connection(self, player_id: uuid.UUID) -> bool:
        """Check if a player has any WebSocket connections."""
        return has_websocket_connection_impl(self, player_id)

    def get_connection_count(self, player_id: uuid.UUID) -> dict[str, int]:
        """Get the number of connections for a player by type."""
        return get_connection_count_impl(self, player_id)

    # Add compatibility methods
    async def subscribe_to_room(self, player_id: uuid.UUID, room_id: str):
        """Subscribe a player to a room (compatibility method)."""
        return await subscribe_to_room_impl(self, player_id, room_id)

    async def unsubscribe_from_room(self, player_id: uuid.UUID, room_id: str):
        """Unsubscribe a player from a room (compatibility method)."""
        return await unsubscribe_from_room_impl(self, player_id, room_id)

    def canonical_room_id(self, room_id: str | None) -> str | None:
        """Resolve a room id to the canonical Room.id value (public method)."""
        return canonical_room_id_public_impl(self, room_id)

    def _canonical_room_id(self, room_id: str | None) -> str | None:
        """Resolve a room id to the canonical Room.id value (compatibility method)."""
        return canonical_room_id_impl(room_id, self)

    def _reconcile_room_presence(self, room_id: str):
        """Ensure room_occupants only contains currently online players (compatibility method)."""
        reconcile_room_presence_impl(room_id, self)

    def _prune_player_from_all_rooms(self, player_id: uuid.UUID):
        """Remove a player from all room subscriptions and occupant lists (compatibility method)."""
        prune_player_from_all_rooms_impl(player_id, self)

    def set_async_persistence(self, async_persistence):
        """Set the async persistence layer reference for all components."""
        self.async_persistence = async_persistence
        self.room_manager.set_async_persistence(async_persistence)

    async def connect_websocket(
        self, websocket: WebSocket, player_id: uuid.UUID, session_id: str | None = None, token: str | None = None
    ) -> bool:
        """Connect a WebSocket for a player."""
        success, _connection_id = await establish_websocket_connection(websocket, player_id, self, session_id, token)
        return success

    async def disconnect_websocket(self, player_id: uuid.UUID, is_force_disconnect: bool = False):
        """Disconnect all WebSocket connections for a player."""
        should_track_disconnect = await cleanup_websocket_disconnect(player_id, self, is_force_disconnect)
        if should_track_disconnect:
            await self._track_player_disconnected(player_id)

    async def force_disconnect_player(self, player_id: uuid.UUID):
        """Force disconnect a player from all connections (WebSocket only)."""
        await force_disconnect_player_impl(self, player_id)

    async def disconnect_connection_by_id(self, connection_id: str) -> bool:
        """Disconnect a specific connection by its ID."""
        return await disconnect_connection_by_id_impl(connection_id, self)

    async def disconnect_websocket_connection(self, player_id: uuid.UUID, connection_id: str) -> bool:
        """Disconnect a specific WebSocket connection for a player."""
        return await disconnect_websocket_connection_impl(self, player_id, connection_id)

    async def handle_new_game_session(self, player_id: uuid.UUID, new_session_id: str) -> dict[str, Any]:
        """Handle a new game session by disconnecting existing connections."""
        return await handle_new_game_session_impl(player_id, new_session_id, self)

    def get_player_session(self, player_id: uuid.UUID) -> str | None:
        """Get the current session ID for a player."""
        return get_player_session_impl(self, player_id)

    def get_session_connections(self, session_id: str) -> list[str]:
        """Get all connection IDs for a session."""
        return get_session_connections_impl(self, session_id)

    def validate_session(self, player_id: uuid.UUID, session_id: str) -> bool:
        """Validate that a session ID matches the player's current session."""
        return validate_session_impl(self, player_id, session_id)

    def get_session_stats(self) -> dict[str, Any]:
        """Get session management statistics."""
        return get_session_stats_impl(self)

    def mark_player_seen(self, player_id: uuid.UUID):
        """Update last-seen timestamp for a player and all their connections."""
        mark_player_seen_impl(player_id, self)

    def prune_stale_players(self, max_age_seconds: int = 90):
        """Remove players whose presence is stale beyond the threshold."""
        prune_stale_players_impl(self, max_age_seconds)

    async def cleanup_orphaned_data(self):
        """Clean up orphaned data that might accumulate over time."""
        await cleanup_orphaned_data_impl(self)

    def get_active_connection_count(self) -> int:
        """Get the total number of active connections."""
        return get_active_connection_count_impl(self)

    def check_rate_limit(self, player_id: uuid.UUID) -> bool:
        """Check if a player has exceeded rate limits."""
        return self.rate_limiter.check_rate_limit(str(player_id))

    def get_rate_limit_info(self, player_id: uuid.UUID) -> dict[str, Any]:
        """Get rate limit information for a player."""
        return get_rate_limit_info_impl(self, player_id)

    async def send_personal_message(self, player_id: uuid.UUID, event: dict[str, Any]) -> dict[str, Any]:
        """Send a personal message to a player via WebSocket."""
        return await send_personal_message_impl(self, player_id, event)

    # Deprecated: Use send_personal_message instead
    async def send_personal_message_old(self, player_id: uuid.UUID, event: dict[str, Any]) -> dict[str, Any]:
        """Send a personal message to a player via WebSocket (deprecated)."""
        return await send_personal_message_old_impl(player_id, event, self)

    def get_message_delivery_stats(self, player_id: uuid.UUID) -> dict[str, Any]:
        """Get message delivery statistics for a player."""
        return get_message_delivery_stats_impl(self, player_id)

    async def check_connection_health(self, player_id: uuid.UUID) -> dict[str, Any]:
        """Check the health of all connections for a player."""
        return await check_connection_health_impl(self, player_id)

    async def cleanup_dead_connections(self, player_id: uuid.UUID | None = None) -> dict[str, Any]:
        """Clean up dead connections for a specific player or all players."""
        return await cleanup_dead_connections_impl(self, player_id)

    async def _cleanup_dead_websocket(self, player_id: uuid.UUID, connection_id: str):
        """Clean up a dead WebSocket connection."""
        await cleanup_dead_websocket_impl(player_id, connection_id, self)

    async def _check_connection_health(self) -> None:
        """Check health of all connections and clean up stale/dead ones."""
        from .connection_manager_methods import _check_connection_health_impl

        await _check_connection_health_impl(self)

    async def _periodic_health_check(self) -> None:
        """Periodic health check task that runs continuously."""
        from .connection_manager_methods import _periodic_health_check_impl

        await _periodic_health_check_impl(self)

    def start_health_checks(self) -> None:
        """Start the periodic health check task."""
        start_health_checks_impl(self)

    def stop_health_checks(self) -> None:
        """Stop the periodic health check task."""
        stop_health_checks_impl(self)

    async def _validate_token(self, token: str, player_id: uuid.UUID) -> bool:
        """Validate a JWT token for a connection."""
        return await validate_token_impl(token, player_id, self)

    def get_connection_id_from_websocket(self, websocket: WebSocket) -> str | None:
        """Get connection ID from a WebSocket instance."""
        return get_connection_id_from_websocket_impl(self, websocket)

    async def broadcast_to_room(
        self,
        room_id: str,
        event: dict[str, Any],
        exclude_player: uuid.UUID | str | None = None,
    ) -> dict[str, Any]:
        """Broadcast a message to all players in a room."""
        return await broadcast_to_room_impl(self, room_id, event, exclude_player)

    async def broadcast_global(self, event: dict[str, Any], exclude_player: str | None = None) -> dict[str, Any]:
        """Broadcast a message to all connected players."""
        return await broadcast_global_impl(self, event, exclude_player)

    async def broadcast_room_event(self, event_type: str, room_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Broadcast a room-specific event to all players in the room."""
        return await broadcast_room_event_impl(self, event_type, room_id, data)

    async def broadcast_global_event(self, event_type: str, data: dict[str, Any]) -> dict[str, Any]:
        """Broadcast a global event to all connected players."""
        return await broadcast_global_event_impl(self, event_type, data)

    def get_pending_messages(self, player_id: uuid.UUID) -> list[dict[str, Any]]:
        """Get pending messages for a player."""
        return get_pending_messages_impl(self, player_id)

    async def _get_player(self, player_id: uuid.UUID) -> Player | None:
        """Get a player from the persistence layer (async version)."""
        return await get_player_impl(self, player_id)

    async def get_player(self, player_id: uuid.UUID) -> Player | None:
        """Get a player from the persistence layer (public API)."""
        return await self._get_player(player_id)

    async def _get_players_batch(self, player_ids: list[uuid.UUID]) -> dict[uuid.UUID, Player]:
        """Get multiple players from the persistence layer in a single batch operation."""
        return await get_players_batch_impl(self, player_ids)

    async def convert_room_players_uuids_to_names(self, room_data: dict[str, Any]) -> dict[str, Any]:
        """Convert player UUIDs and NPC IDs in room_data to names."""
        return await convert_room_players_uuids_to_names_impl(self, room_data)

    def _get_npcs_batch(self, npc_ids: list[str]) -> dict[str, str]:
        """Get NPC names for multiple NPCs in a batch operation."""
        return get_npcs_batch_impl(self, npc_ids)

    def _convert_uuids_to_strings(self, obj):
        """Recursively convert UUID objects to strings for JSON serialization."""
        return convert_uuids_to_strings_impl(self, obj)

    def _get_next_sequence(self) -> int:
        """
        Get the next sequence number for events.

        Returns:
            int: The next sequence number
        """
        return get_next_sequence_impl(self)

    async def _track_player_connected(self, player_id: uuid.UUID, player: Player, connection_type: str = "unknown"):
        """Track when a player connects."""
        await track_player_connected_impl(player_id, player, connection_type, self)

    async def _broadcast_connection_message(self, player_id: uuid.UUID, player: Player) -> None:
        """Broadcast a connection message for a player who is already tracked as online."""
        await broadcast_connection_message_impl(player_id, player, self)

    async def _track_player_disconnected(self, player_id: uuid.UUID, connection_type: str | None = None) -> None:
        """
        Track when a player disconnects.

        Args:
            player_id: The player's ID
            connection_type: Type of connection being disconnected ("websocket", None for all)
        """
        await track_player_disconnected_impl(player_id, self, connection_type)

    def _cleanup_ghost_players(self) -> None:
        """Clean up ghost players from all rooms."""
        cleanup_ghost_players_impl(self)

    async def detect_and_handle_error_state(
        self, player_id: uuid.UUID, error_type: str, error_details: str, connection_id: str | None = None
    ) -> dict[str, Any]:
        """Detect when a client is in an error state and handle it appropriately."""
        return await detect_and_handle_error_state_impl(self, player_id, error_type, error_details, connection_id)

    async def handle_websocket_error(
        self, player_id: uuid.UUID, connection_id: str, error_type: str, error_details: str
    ) -> dict[str, Any]:
        """Handle WebSocket-specific errors."""
        return await handle_websocket_error_impl(self, player_id, connection_id, error_type, error_details)

    async def handle_authentication_error(
        self, player_id: uuid.UUID, error_type: str, error_details: str
    ) -> dict[str, Any]:
        """Handle authentication-related errors."""
        return await handle_authentication_error_impl(self, player_id, error_type, error_details)

    async def handle_security_violation(
        self, player_id: uuid.UUID, violation_type: str, violation_details: str
    ) -> dict[str, Any]:
        """Handle security violations."""
        return await handle_security_violation_impl(self, player_id, violation_type, violation_details)

    async def recover_from_error(self, player_id: uuid.UUID, recovery_type: str = "FULL") -> dict[str, Any]:
        """Attempt to recover from an error state for a player."""
        return await recover_from_error_impl(self, player_id, recovery_type)

    def get_player_presence_info(self, player_id: uuid.UUID) -> dict[str, Any]:
        """Get detailed presence information for a player."""
        return get_player_presence_info_method(self, player_id)

    def validate_player_presence(self, player_id: uuid.UUID) -> dict[str, Any]:
        """Validate player presence and clean up any inconsistencies."""
        return validate_player_presence_method(self, player_id)

    def get_presence_statistics(self) -> dict[str, Any]:
        """Get presence tracking statistics."""
        return get_presence_statistics_impl(self)

    def get_error_statistics(self) -> dict[str, Any]:
        """Get error handling statistics."""
        return get_error_statistics_impl(self)

    async def handle_new_login(self, player_id: uuid.UUID):
        """Handle a new login by terminating all existing connections for the player."""
        await handle_new_login_impl(player_id, self)

    async def _check_and_process_disconnect(self, player_id: uuid.UUID):
        """Check if disconnect has already been processed for a player and process it if not."""
        async with self.processed_disconnect_lock:
            if player_id not in self.processed_disconnects:
                self.processed_disconnects.add(player_id)
                await self._track_player_disconnected(player_id)
            else:
                logger.debug("Disconnect already processed for player, skipping", player_id=player_id)

    def get_online_players(self) -> list[dict[str, Any]]:
        """Get list of online players."""
        return get_online_players_impl(self)

    def get_online_player_by_display_name(self, display_name: str) -> dict[str, Any] | None:
        """Get online player information by display name."""
        return get_online_player_by_display_name_method(self, display_name)

    async def get_room_occupants(self, room_id: str) -> list[dict[str, Any]]:
        """Get list of occupants in a room."""
        return await get_room_occupants_impl(self, room_id)

    async def _send_initial_game_state(self, player_id: uuid.UUID, player: Player, room_id: str):
        """Send initial game_state event to a newly connected player."""
        await send_initial_game_state_impl(self, player_id, player, room_id)

    async def _check_and_cleanup(self):
        """Periodically check for cleanup conditions and perform cleanup if needed."""
        await check_and_cleanup_impl(self)

    def get_memory_stats(self) -> dict[str, Any]:
        """Get comprehensive memory and connection statistics."""
        return get_memory_stats_impl(self)

    def get_dual_connection_stats(self) -> dict[str, Any]:
        """Get comprehensive connection statistics."""
        return get_dual_connection_stats_impl(self)

    def get_performance_stats(self) -> dict[str, Any]:
        """Get connection performance statistics."""
        return get_performance_stats_impl(self)

    def get_connection_health_stats(self) -> dict[str, Any]:
        """Get comprehensive connection health statistics."""
        return get_connection_health_stats_impl(self)

    def get_memory_alerts(self) -> list[str]:
        """Get memory-related alerts."""
        return get_memory_alerts_impl(self)

    async def force_cleanup(self):
        """Force immediate cleanup of all orphaned data."""
        await force_cleanup_impl(self)

    # --- Event Subscription Methods ---

    def set_event_bus(self, event_bus: Any) -> None:
        """Set the event bus for the connection manager."""
        self._event_bus = event_bus

    def set_player_combat_service(self, player_combat_service: Any) -> None:
        """Set the player combat service for the connection manager."""
        self._player_combat_service = player_combat_service

    @property
    def event_bus(self) -> Any:
        """Get the event bus from connection manager."""
        return self._event_bus

    def _get_event_bus(self):
        """Get the event bus from connection manager."""
        # Event bus is already available on connection_manager
        return self._event_bus

    async def subscribe_to_room_events(self):
        """Subscribe to room movement events for occupant broadcasting."""
        await subscribe_to_room_events_impl(self)

    async def unsubscribe_from_room_events(self):
        """Unsubscribe from room movement events."""
        await unsubscribe_from_room_events_impl(self)

    async def _handle_player_entered_room(self, event_data: dict[str, Any]):
        """Handle PlayerEnteredRoom events by broadcasting updated occupant count."""
        await handle_player_entered_room_impl(self, event_data)

    async def _handle_player_left_room(self, event_data: dict[str, Any]):
        """Handle PlayerLeftRoom events by broadcasting updated occupant count."""
        await handle_player_left_room_impl(self, event_data)


# Attach compatibility properties after class definition
attach_compatibility_properties(ConnectionManager)

# Constants for async compatibility
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


def _ensure_async_compat(manager: "Any | None") -> "Any | None":
    """
    Ensure connection manager methods are awaitable.

    Wraps synchronous callables in async wrappers to ensure production code
    can await methods that might be synchronous (e.g., in test scenarios).
    Uses duck typing to detect mock-like objects without importing test utilities.
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

        # Wrap any callable (including mock-like objects) in an async wrapper
        # This works for both real methods and test mocks without importing Mock types
        if callable(attr):

            async def _async_wrapper(*args, _attr=attr, **kwargs):
                result = _attr(*args, **kwargs)
                if inspect.isawaitable(result):
                    return await result
                return result

            setattr(manager, method_name, _async_wrapper)

    return manager


def resolve_connection_manager(candidate: "Any | None" = None) -> "Any | None":
    """
    Resolve a connection manager instance.

    Prefers explicitly supplied candidate, then tries to resolve from:
    1. FastAPI app state container (if available in context)
    2. ApplicationContainer.get_instance() (for background tasks)

    Args:
        candidate: Explicit connection manager to prefer.

    Returns:
        Optional[ConnectionManager]: The resolved connection manager instance (if any)
    """
    if candidate is not None:
        return _ensure_async_compat(candidate)

    # Try to get from app state (for API routes)
    # This requires accessing the current request context, which is not always available
    # For now, try ApplicationContainer.get_instance() as fallback
    try:
        from ..container import ApplicationContainer

        container = ApplicationContainer.get_instance()
        if container is not None:
            manager = getattr(container, "connection_manager", None)
            if manager is not None:
                return _ensure_async_compat(manager)
    except (AttributeError, RuntimeError, ImportError):
        # Container not available or not initialized
        pass

    return None


# Re-export for backward compatibility
__all__ = [
    "ConnectionManager",
    "ConnectionMetadata",
    "resolve_connection_manager",
]


def __getattr__(name: str) -> Any:
    """Lazy import for API utility functions to avoid circular dependencies."""
    from collections.abc import Callable
    from typing import cast

    if name == "broadcast_game_event":
        from .connection_manager_api import broadcast_game_event

        return cast(Callable[..., Any], broadcast_game_event)
    elif name == "send_game_event":
        from .connection_manager_api import send_game_event

        return cast(Callable[..., Any], send_game_event)
    elif name == "send_player_status_update":
        from .connection_manager_api import send_player_status_update

        return cast(Callable[..., Any], send_player_status_update)
    elif name == "send_room_description":
        from .connection_manager_api import send_room_description

        return cast(Callable[..., Any], send_room_description)
    elif name == "send_room_event":
        from .connection_manager_api import send_room_event

        return cast(Callable[..., Any], send_room_event)
    elif name == "send_system_notification":
        from .connection_manager_api import send_system_notification

        return cast(Callable[..., Any], send_system_notification)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
