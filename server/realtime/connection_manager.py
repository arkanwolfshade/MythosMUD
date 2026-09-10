"""
Refactored Connection Manager for MythosMUD real-time communication.

This module provides a clean, modular connection management system that
separates concerns into dedicated components for better maintainability
and testability.
"""

# pylint: disable=too-many-instance-attributes,too-many-lines,too-many-public-methods,too-many-statements  # Reason: Connection manager requires many state tracking and service attributes. Connection manager requires extensive connection management logic for comprehensive real-time communication. Connection manager legitimately requires many public methods and statements for comprehensive connection management.

import uuid
from collections import deque
from typing import cast

from anyio import Lock
from fastapi import WebSocket

from ..events.event_bus import EventBus
from ..models import Player
from ..services.player_combat_service import PlayerCombatService
from ..structured_logging.enhanced_logging_config import get_logger
from . import connection_manager_methods as _cmm
from .connection_cleanup_methods import (
    check_and_cleanup_impl,
    cleanup_dead_connections_impl,
    cleanup_ghost_players_impl,
    cleanup_orphaned_data_impl,
    force_cleanup_impl,
    prune_stale_players_impl,
)
from .connection_compatibility import attach_compatibility_properties
from .connection_delegates import cleanup_dead_websocket_impl, validate_token_impl
from .connection_disconnection import (
    cleanup_websocket_disconnect,
    disconnect_connection_by_id_impl,
    force_disconnect_player_impl,
)
from .connection_error_methods import (
    detect_and_handle_error_state_impl,
    handle_authentication_error_impl,
    handle_security_violation_impl,
    handle_websocket_error_impl,
    recover_from_error_impl,
)
from .connection_establishment import establish_websocket_connection
from .connection_helpers import (
    handle_new_login_impl,
    mark_player_seen_impl,
    send_personal_message_old_impl,
)
from .connection_initialization import (
    initialize_connection_cleaner,
    initialize_connection_state,
    initialize_core_components,
    initialize_error_handler,
    initialize_game_state_provider,
    initialize_health_monitor,
    initialize_messaging,
    initialize_room_event_handler,
)
from .connection_manager_utils import resolve_connection_manager as _resolve_connection_manager_uncast
from .connection_models import ConnectionMetadata
from .connection_room_utils import (
    canonical_room_id_impl,
    prune_player_from_all_rooms_impl,
    reconcile_room_presence_impl,
)
from .connection_session_management import NewGameSessionResult, handle_new_game_session_impl
from .connection_statistics import get_presence_statistics_impl, get_session_stats_impl
from .connection_utils import get_npc_name_from_instance
from .connection_websocket_close import is_websocket_open_impl, safe_close_websocket_impl
from .errors.error_handler import ConnectionErrorHandler
from .event_publisher import EventPublisher
from .memory_monitor import MemoryMonitor
from .message_queue import MessageQueue
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

    def __init__(self, event_publisher: EventPublisher | None = None) -> None:
        """Initialize the connection manager with modular components."""
        # Declared here so basedpyright sees the attr; init helper also sets it
        self._closed_websockets: deque[int] = deque(maxlen=1000)
        # Set later via set_async_persistence; object | None matches _TokenValidateManager Protocol
        self.async_persistence: object | None = None
        # Set later via set_event_bus / set_player_combat_service
        self._event_bus: EventBus | None = None
        self._player_combat_service: PlayerCombatService | None = None
        # Declared for basedpyright / Protocol conformance; init helpers assign real values
        self.active_websockets: dict[str, WebSocket]
        self.connection_metadata: dict[str, ConnectionMetadata]
        self.player_websockets: dict[uuid.UUID, list[str]]
        self.rate_limiter: RateLimiter
        self.message_queue: MessageQueue
        self.room_manager: RoomSubscriptionManager
        self.processed_disconnects: set[uuid.UUID]
        self.last_seen: dict[uuid.UUID, float]
        self.last_active_update_times: dict[uuid.UUID, float]
        self.intentional_disconnects: set[uuid.UUID]
        self.disconnect_lock: Lock
        self.processed_disconnect_lock: Lock
        self.performance_tracker: PerformanceTracker
        # Set in initialize_connection_state / core components (needed for mypy + _SupportsEventSequence)
        self.sequence_counter: int
        self.online_players: dict[uuid.UUID, dict[str, object]]
        self.player_sessions: dict[uuid.UUID, str]
        self.session_connections: dict[str, list[str]]
        self.session_disconnect_times: dict[str, float]
        self.connection_timestamps: dict[str, float]
        self.cleanup_stats: dict[str, object]
        self.statistics_aggregator: StatisticsAggregator
        self.memory_monitor: MemoryMonitor
        self.error_handler: ConnectionErrorHandler | None
        self.health_monitor: HealthMonitor | None
        self.personal_message_sender: object | None
        self.message_broadcaster: object | None
        self.game_state_provider: object | None
        self.room_event_handler: object | None
        self.app: object | None
        initialize_connection_state(self, event_publisher)
        initialize_core_components(self)
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
        # Use append() instead of add() for deque
        # Note: deque automatically evicts oldest entries when maxlen is reached
        self._closed_websockets.append(ws_id)

    def get_closed_websockets_count(self) -> int:
        """Get the count of closed WebSocket IDs being tracked."""
        return len(self._closed_websockets)

    async def _safe_close_websocket(
        self, websocket: WebSocket, code: int = 1000, reason: str = "Connection closed"
    ) -> None:
        """Safely close a WebSocket connection."""
        await safe_close_websocket_impl(self, websocket, code, reason)

    # Compatibility properties attached by attach_compatibility_properties below

    # Compatibility methods for WebSocket connection system
    def get_player_websocket_connection_id(self, player_id: uuid.UUID) -> str | None:
        """Get the first WebSocket connection ID for a player (backward compatibility)."""
        return _cmm.get_player_websocket_connection_id_impl(self, player_id)

    def has_websocket_connection(self, player_id: uuid.UUID) -> bool:
        """Check if a player has any WebSocket connections."""
        return _cmm.has_websocket_connection_impl(self, player_id)

    def get_connection_count(self, player_id: uuid.UUID) -> dict[str, int]:
        """Get the number of connections for a player by type."""
        return _cmm.get_connection_count_impl(self, player_id)

    # Add compatibility methods
    async def subscribe_to_room(self, player_id: uuid.UUID, room_id: str) -> None:
        """Subscribe a player to a room (compatibility method)."""
        return await _cmm.subscribe_to_room_impl(self, player_id, room_id)

    async def unsubscribe_from_room(self, player_id: uuid.UUID, room_id: str) -> None:
        """Unsubscribe a player from a room (compatibility method)."""
        return await _cmm.unsubscribe_from_room_impl(self, player_id, room_id)

    def update_player_room_cache(self, player_id: uuid.UUID, room_id: str) -> None:
        """Sync online_players[...]['current_room_id'] with an actual room move (#297/#610)."""
        _cmm.update_player_room_cache_impl(self, player_id, room_id)

    def canonical_room_id(self, room_id: str | None) -> str | None:
        """Resolve a room id to the canonical Room.id value (public method)."""
        return _cmm.canonical_room_id_public_impl(self, room_id)

    def _canonical_room_id(self, room_id: str | None) -> str | None:
        """Resolve a room id to the canonical Room.id value (compatibility method)."""
        return canonical_room_id_impl(room_id, self)

    def _reconcile_room_presence(self, room_id: str) -> None:
        """Ensure room_occupants only contains currently online players (compatibility method)."""
        reconcile_room_presence_impl(room_id, self)

    def _prune_player_from_all_rooms(self, player_id: uuid.UUID) -> None:
        """Remove a player from all room subscriptions and occupant lists (compatibility method)."""
        prune_player_from_all_rooms_impl(player_id, self)

    def set_async_persistence(self, async_persistence: object) -> None:
        """Set the async persistence layer reference for all components."""
        self.async_persistence = async_persistence
        self.room_manager.set_async_persistence(async_persistence)

    async def connect_websocket(
        self, websocket: WebSocket, player_id: uuid.UUID, session_id: str | None = None, token: str | None = None
    ) -> bool:
        """Connect a WebSocket for a player."""
        success, _connection_id = await establish_websocket_connection(websocket, player_id, self, session_id, token)
        return success

    async def disconnect_websocket(self, player_id: uuid.UUID, is_force_disconnect: bool = False) -> None:
        """Disconnect all WebSocket connections for a player."""
        should_track_disconnect = await cleanup_websocket_disconnect(player_id, self, is_force_disconnect)
        if should_track_disconnect:
            await self._track_player_disconnected(player_id)

    async def force_disconnect_player(self, player_id: uuid.UUID) -> None:
        """Force disconnect a player from all connections (WebSocket only)."""
        await force_disconnect_player_impl(self, player_id)

    async def disconnect_connection_by_id(self, connection_id: str) -> bool:
        """Disconnect a specific connection by its ID."""
        return await disconnect_connection_by_id_impl(connection_id, self)

    async def disconnect_websocket_connection(self, player_id: uuid.UUID, connection_id: str) -> bool:
        """Disconnect a specific WebSocket connection for a player."""
        return await _cmm.disconnect_websocket_connection_impl(self, player_id, connection_id)

    async def handle_new_game_session(self, player_id: uuid.UUID, new_session_id: str) -> NewGameSessionResult:
        """Handle a new game session by disconnecting existing connections."""
        return await handle_new_game_session_impl(player_id, new_session_id, self)

    def get_player_session(self, player_id: uuid.UUID) -> str | None:
        """Get the current session ID for a player."""
        return _cmm.get_player_session_impl(self, player_id)

    def get_session_connections(self, session_id: str) -> list[str]:
        """Get all connection IDs for a session."""
        return _cmm.get_session_connections_impl(self, session_id)

    def validate_session(self, player_id: uuid.UUID, session_id: str) -> bool:
        """Validate that a session ID matches the player's current session."""
        return _cmm.validate_session_impl(self, player_id, session_id)

    def get_session_stats(self) -> dict[str, object]:
        """Get session management statistics."""
        return get_session_stats_impl(self)

    def mark_player_seen(self, player_id: uuid.UUID) -> None:
        """Update last-seen timestamp for a player and all their connections."""
        mark_player_seen_impl(player_id, self)

    def prune_stale_players(self, max_age_seconds: int = 90) -> None:
        """Remove players whose presence is stale beyond the threshold."""
        prune_stale_players_impl(self, max_age_seconds)

    async def cleanup_orphaned_data(self) -> None:
        """Clean up orphaned data that might accumulate over time."""
        await cleanup_orphaned_data_impl(self)

    def get_active_connection_count(self) -> int:
        """Get the total number of active connections."""
        return _cmm.get_active_connection_count_impl(self)

    def check_rate_limit(self, player_id: uuid.UUID) -> bool:
        """Check if a player has exceeded rate limits."""
        return self.rate_limiter.check_rate_limit(str(player_id))

    def get_rate_limit_info(self, player_id: uuid.UUID) -> dict[str, object]:
        """Get rate limit information for a player."""
        return _cmm.get_rate_limit_info_impl(self, player_id)

    async def send_personal_message(self, player_id: uuid.UUID, event: dict[str, object]) -> dict[str, object]:
        """Send a personal message to a player via WebSocket."""
        return await _cmm.send_personal_message_impl(self, player_id, event)

    # Deprecated: Use send_personal_message instead
    async def send_personal_message_old(self, player_id: uuid.UUID, event: dict[str, object]) -> dict[str, object]:
        """Send a personal message to a player via WebSocket (deprecated)."""
        return await send_personal_message_old_impl(player_id, event, self)

    def get_message_delivery_stats(self, player_id: uuid.UUID) -> dict[str, object]:
        """Get message delivery statistics for a player."""
        return _cmm.get_message_delivery_stats_impl(self, player_id)

    async def check_connection_health(self, player_id: uuid.UUID) -> dict[str, object]:
        """Check the health of all connections for a player."""
        return await _cmm.check_connection_health_impl(self, player_id)

    async def cleanup_dead_connections(self, player_id: uuid.UUID | None = None) -> dict[str, object]:
        """Clean up dead connections for a specific player or all players."""
        return await cleanup_dead_connections_impl(self, player_id)

    async def _cleanup_dead_websocket(self, player_id: uuid.UUID, connection_id: str) -> None:
        """Clean up a dead WebSocket connection."""
        await cleanup_dead_websocket_impl(player_id, connection_id, self)

    async def _check_connection_health(self) -> None:
        """Check health of all connections and clean up stale/dead ones."""
        await _cmm.check_all_connections_health_impl(self)

    async def _periodic_health_check(self) -> None:
        """Periodic health check task that runs continuously."""
        await _cmm.periodic_health_check_impl(self)

    def start_health_checks(self) -> None:
        """Start the periodic health check task."""
        _cmm.start_health_checks_impl(self)

    def stop_health_checks(self) -> None:
        """Stop the periodic health check task."""
        _cmm.stop_health_checks_impl(self)

    async def _validate_token(self, token: str, player_id: uuid.UUID) -> bool:
        """Validate a JWT token for a connection."""
        return await validate_token_impl(token, player_id, self)

    def get_connection_id_from_websocket(self, websocket: WebSocket) -> str | None:
        """Get connection ID from a WebSocket instance."""
        return _cmm.get_connection_id_from_websocket_impl(self, websocket)

    async def broadcast_to_room(
        self,
        room_id: str,
        event: dict[str, object],
        exclude_player: uuid.UUID | str | None = None,
    ) -> dict[str, object]:
        """Broadcast a message to all players in a room."""
        return await _cmm.broadcast_to_room_impl(self, room_id, event, exclude_player)

    async def broadcast_global(self, event: dict[str, object], exclude_player: str | None = None) -> dict[str, object]:
        """Broadcast a message to all connected players."""
        return await _cmm.broadcast_global_impl(self, event, exclude_player)

    async def broadcast_room_event(self, event_type: str, room_id: str, data: dict[str, object]) -> dict[str, object]:
        """Broadcast a room-specific event to all players in the room."""
        return await _cmm.broadcast_room_event_impl(self, event_type, room_id, data)

    async def broadcast_global_event(self, event_type: str, data: dict[str, object]) -> dict[str, object]:
        """Broadcast a global event to all connected players."""
        return await _cmm.broadcast_global_event_impl(self, event_type, data)

    def get_pending_messages(self, player_id: uuid.UUID) -> list[dict[str, object]]:
        """Get pending messages for a player."""
        return _cmm.get_pending_messages_impl(self, player_id)

    async def _get_player(self, player_id: uuid.UUID) -> Player | None:
        """Get a player from the persistence layer (async version)."""
        return await _cmm.get_player_impl(self, player_id)

    async def get_player(self, player_id: uuid.UUID) -> Player | None:
        """Get a player from the persistence layer (public API)."""
        return await self._get_player(player_id)

    async def _get_players_batch(self, player_ids: list[uuid.UUID]) -> dict[uuid.UUID, Player]:
        """Get multiple players from the persistence layer in a single batch operation."""
        return await _cmm.get_players_batch_impl(self, player_ids)

    async def convert_room_players_uuids_to_names(self, room_data: dict[str, object]) -> dict[str, object]:
        """Convert player UUIDs and NPC IDs in room_data to names."""
        return await _cmm.convert_room_players_uuids_to_names_impl(self, room_data)

    def _get_npcs_batch(self, npc_ids: list[str]) -> dict[str, str]:
        """Get NPC names for multiple NPCs in a batch operation."""
        return _cmm.get_npcs_batch_impl(self, npc_ids)

    def _convert_uuids_to_strings(self, obj: object) -> object:
        """Recursively convert UUID objects to strings for JSON serialization."""
        return _cmm.convert_uuids_to_strings_impl(self, obj)

    def _get_next_sequence(self) -> int:
        """
        Get the next sequence number for events.

        Returns:
            int: The next sequence number
        """
        return _cmm.get_next_sequence_impl(self)

    async def track_player_connected(
        self, player_id: uuid.UUID, player: Player, connection_type: str = "unknown"
    ) -> None:
        """Track when a player connects."""
        await track_player_connected_impl(player_id, player, connection_type, self)

    async def broadcast_connection_message(self, player_id: uuid.UUID, player: Player) -> None:
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

    async def track_player_disconnected(self, player_id: uuid.UUID, connection_type: str | None = None) -> None:
        """Public wrapper for intentional-logout leave tracking from facade impls."""
        await self._track_player_disconnected(player_id, connection_type)

    def _cleanup_ghost_players(self) -> None:
        """Clean up ghost players from all rooms."""
        cleanup_ghost_players_impl(self)

    async def detect_and_handle_error_state(
        self, player_id: uuid.UUID, error_type: str, error_details: str, connection_id: str | None = None
    ) -> dict[str, object]:
        """Detect when a client is in an error state and handle it appropriately."""
        return await detect_and_handle_error_state_impl(self, player_id, error_type, error_details, connection_id)

    async def handle_websocket_error(
        self, player_id: uuid.UUID, connection_id: str, error_type: str, error_details: str
    ) -> dict[str, object]:
        """Handle WebSocket-specific errors."""
        return await handle_websocket_error_impl(self, player_id, connection_id, error_type, error_details)

    async def handle_authentication_error(
        self, player_id: uuid.UUID, error_type: str, error_details: str
    ) -> dict[str, object]:
        """Handle authentication-related errors."""
        return await handle_authentication_error_impl(self, player_id, error_type, error_details)

    async def handle_security_violation(
        self, player_id: uuid.UUID, violation_type: str, violation_details: str
    ) -> dict[str, object]:
        """Handle security violations."""
        return await handle_security_violation_impl(self, player_id, violation_type, violation_details)

    async def recover_from_error(self, player_id: uuid.UUID, recovery_type: str = "FULL") -> dict[str, object]:
        """Attempt to recover from an error state for a player."""
        return await recover_from_error_impl(self, player_id, recovery_type)

    def get_player_presence_info(self, player_id: uuid.UUID) -> dict[str, object]:
        """Get detailed presence information for a player."""
        return _cmm.get_player_presence_info_method(self, player_id)

    def validate_player_presence(self, player_id: uuid.UUID) -> dict[str, object]:
        """Validate player presence and clean up any inconsistencies."""
        return _cmm.validate_player_presence_method(self, player_id)

    def get_presence_statistics(self) -> dict[str, object]:
        """Get presence tracking statistics."""
        return get_presence_statistics_impl(self)

    def get_error_statistics(self) -> dict[str, object]:
        """Get error handling statistics."""
        return _cmm.get_error_statistics_impl(self)

    async def handle_new_login(self, player_id: uuid.UUID) -> None:
        """Handle a new login by terminating all existing connections for the player."""
        await handle_new_login_impl(player_id, self)

    async def _check_and_process_disconnect(self, player_id: uuid.UUID) -> None:
        """Check if disconnect has already been processed for a player and process it if not."""
        async with self.processed_disconnect_lock:
            if player_id not in self.processed_disconnects:
                self.processed_disconnects.add(player_id)
                await self._track_player_disconnected(player_id)
            else:
                logger.debug("Disconnect already processed for player, skipping", player_id=player_id)

    def get_online_players(self) -> list[dict[str, object]]:
        """Get list of online players."""
        return _cmm.get_online_players_impl(self)

    def get_online_player_by_display_name(self, display_name: str) -> dict[str, object] | None:
        """Get online player information by display name."""
        return _cmm.get_online_player_by_display_name_method(self, display_name)

    async def get_room_occupants(self, room_id: str) -> list[dict[str, object]]:
        """Get list of occupants in a room."""
        return await _cmm.get_room_occupants_impl(self, room_id)

    async def _send_initial_game_state(self, player_id: uuid.UUID, player: Player, room_id: str) -> None:
        """Send initial game_state event to a newly connected player."""
        await _cmm.send_initial_game_state_impl(self, player_id, player, room_id)

    async def _check_and_cleanup(self) -> None:
        """Periodically check for cleanup conditions and perform cleanup if needed."""
        await check_and_cleanup_impl(self)

    def get_memory_stats(self) -> dict[str, object]:
        """Get comprehensive memory and connection statistics."""
        return _cmm.get_memory_stats_impl(self)

    def get_dual_connection_stats(self) -> dict[str, object]:
        """Get comprehensive connection statistics."""
        return _cmm.get_dual_connection_stats_impl(self)

    def get_performance_stats(self) -> dict[str, object]:
        """Get connection performance statistics."""
        return _cmm.get_performance_stats_impl(self)

    def get_connection_health_stats(self) -> dict[str, object]:
        """Get comprehensive connection health statistics."""
        return _cmm.get_connection_health_stats_impl(self)

    def get_memory_alerts(self) -> list[str]:
        """Get memory-related alerts."""
        return _cmm.get_memory_alerts_impl(self)

    async def force_cleanup(self) -> None:
        """Force immediate cleanup of all orphaned data."""
        await force_cleanup_impl(self)

    # --- Event Subscription Methods ---

    def set_event_bus(self, event_bus: EventBus) -> None:
        """Set the event bus for the connection manager."""
        self._event_bus = event_bus

    def set_player_combat_service(self, player_combat_service: PlayerCombatService) -> None:
        """Set the player combat service for the connection manager."""
        self._player_combat_service = player_combat_service

    @property
    def event_bus(self) -> EventBus | None:
        """Get the event bus from connection manager."""
        return self._event_bus

    def _get_event_bus(self) -> EventBus | None:
        """Get the event bus from connection manager."""
        # Event bus is already available on connection_manager
        return self._event_bus

    async def subscribe_to_room_events(self) -> None:
        """Subscribe to room movement events for occupant broadcasting."""
        await _cmm.subscribe_to_room_events_impl(self)

    async def unsubscribe_from_room_events(self) -> None:
        """Unsubscribe from room movement events."""
        await _cmm.unsubscribe_from_room_events_impl(self)

    async def _handle_player_entered_room(self, event_data: dict[str, object]) -> None:
        """Handle PlayerEnteredRoom events by broadcasting updated occupant count."""
        await _cmm.handle_player_entered_room_impl(self, event_data)

    async def _handle_player_left_room(self, event_data: dict[str, object]) -> None:
        """Handle PlayerLeftRoom events by broadcasting updated occupant count."""
        await _cmm.handle_player_left_room_impl(self, event_data)


# Attach compatibility properties after class definition
attach_compatibility_properties(ConnectionManager)


def resolve_connection_manager(candidate: ConnectionManager | None = None) -> ConnectionManager | None:
    """Typed wrapper; utils stays free of ConnectionManager imports (import cycles)."""
    return cast(ConnectionManager | None, _resolve_connection_manager_uncast(candidate))


__all__ = ["ConnectionManager", "ConnectionMetadata", "resolve_connection_manager"]


def __getattr__(name: str) -> object:
    from .connection_manager_lazy import resolve_lazy_attr

    return resolve_lazy_attr(name, __name__)
