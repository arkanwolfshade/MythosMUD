"""
Initialization helpers for connection manager.

This module provides helper functions for initializing the connection manager
and its various components.
"""

import time
from collections import deque
from typing import Any

from anyio import Lock

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


def initialize_connection_maps(manager: Any, event_publisher: Any | None) -> None:
    """Initialize connection maps, presence tracking, and service references."""
    # pylint: disable=protected-access  # Reason: init helper owns private ConnectionManager attrs
    manager.active_websockets = {}  # dict[str, WebSocket]
    manager.player_websockets = {}  # dict[uuid.UUID, list[str]]
    manager.connection_metadata = {}  # dict[str, ConnectionMetadata]
    manager.sequence_counter = 0
    # ARCHITECTURAL FIX: Use async_persistence instead of sync persistence
    manager.async_persistence = None
    manager.event_publisher = event_publisher
    manager._event_bus = None
    manager.app = None
    manager._player_combat_service = None

    manager.online_players = {}  # dict[uuid.UUID, dict[str, Any]]
    manager.last_seen = {}  # dict[uuid.UUID, float]
    manager.last_active_update_interval = 60.0
    manager.last_active_update_times = {}  # dict[uuid.UUID, float]
    manager.disconnecting_players = set()  # set[uuid.UUID]
    manager.disconnect_lock = Lock()
    manager.processed_disconnects = set()  # set[uuid.UUID]
    manager.processed_disconnect_lock = Lock()
    manager.grace_period_players = {}  # dict[uuid.UUID, asyncio.Task[Any]]
    manager.login_grace_period_players = {}  # dict[uuid.UUID, asyncio.Task[Any]]
    manager.login_grace_period_start_times = {}  # dict[uuid.UUID, float]
    manager.resting_players = {}  # dict[uuid.UUID, asyncio.Task[Any]]
    manager.intentional_disconnects = set()  # set[uuid.UUID]
    manager.connection_timestamps = {}  # dict[str, float]


def initialize_core_components(manager: Any) -> None:
    """Initialize cleanup stats, modular services, and specialized placeholders."""
    manager.cleanup_stats = {
        "last_cleanup": time.time(),
        "cleanups_performed": 0,
        "memory_cleanups": 0,
        "time_cleanups": 0,
        "cleanup_operation_counts": {
            "dead_connections": 0,
            "orphaned_data": 0,
            "ghost_players": 0,
            "force_cleanup": 0,
            "check_and_cleanup": 0,
        },
        "cleanup_operation_timestamps": [],
    }

    manager.memory_monitor = MemoryMonitor()
    manager.rate_limiter = RateLimiter()
    manager.message_queue = MessageQueue(max_messages_per_player=manager.memory_monitor.max_pending_messages)
    manager.room_manager = RoomSubscriptionManager()
    manager.performance_tracker = PerformanceTracker(max_samples=1000)
    manager.statistics_aggregator = StatisticsAggregator(
        memory_monitor=manager.memory_monitor,
        rate_limiter=manager.rate_limiter,
        message_queue=manager.message_queue,
        room_manager=manager.room_manager,
        performance_tracker=manager.performance_tracker,
    )
    manager.health_monitor = None
    manager.error_handler = None
    manager.connection_cleaner = None
    manager.game_state_provider = None
    manager.room_event_handler = None
    manager.personal_message_sender = None
    manager.message_broadcaster = None


def initialize_session_and_health_config(manager: Any) -> None:
    """Initialize session maps, closed-socket tracking, and health-check config."""
    # pylint: disable=protected-access  # Reason: init helper owns private ConnectionManager attrs
    manager.player_sessions = {}  # dict[uuid.UUID, str]
    manager.session_connections = {}  # dict[str, list[str]]
    # Disconnected sessions age off after 5 min; reconnects purge old sessions immediately
    manager.session_disconnect_times = {}  # dict[str, float]
    # Use deque with maxlen to prevent unbounded growth (maxlen=1000)
    manager._closed_websockets = deque(maxlen=1000)
    manager._disconnect_executor = None
    manager._health_check_interval = 30.0
    manager._health_check_task = None
    # 5 minutes idle = stale connection (aligned with MemoryMonitor.max_connection_age)
    manager._connection_timeout = 300.0
    manager._token_revalidation_interval = 300.0


def initialize_specialized_components(manager: Any) -> None:
    """Wire specialized components that need manager callbacks."""
    initialize_health_monitor(manager)
    initialize_error_handler(manager)
    initialize_connection_cleaner(manager)
    initialize_game_state_provider(manager)
    initialize_messaging(manager)
    initialize_room_event_handler(manager)


def initialize_connection_manager(manager: Any, event_publisher: Any | None = None) -> None:
    """Fully initialize a ConnectionManager instance."""
    initialize_connection_maps(manager, event_publisher)
    initialize_core_components(manager)
    initialize_session_and_health_config(manager)
    initialize_specialized_components(manager)


def initialize_health_monitor(manager: Any) -> None:
    """Initialize the health monitor with required callbacks."""
    # Accessing protected members is necessary for initialization
    # pylint: disable=protected-access  # Reason: Initialization requires access to internal manager methods (_is_websocket_open, _validate_token, etc.) for callback setup, manager is guaranteed to have these methods
    manager.health_monitor = HealthMonitor(
        is_websocket_open_callback=manager._is_websocket_open,
        validate_token_callback=manager._validate_token,
        cleanup_dead_websocket_callback=manager._cleanup_dead_websocket,
        performance_tracker=manager.performance_tracker,
        health_check_interval=manager._health_check_interval,
        connection_timeout=manager._connection_timeout,
        token_revalidation_interval=manager._token_revalidation_interval,
    )


def initialize_error_handler(manager: Any) -> None:
    """Initialize the error handler with required callbacks."""
    manager.error_handler = ConnectionErrorHandler(
        force_disconnect_callback=manager.force_disconnect_player,
        disconnect_connection_callback=manager.disconnect_connection_by_id,
        cleanup_dead_connections_callback=manager.cleanup_dead_connections,
        get_player_session_callback=manager.get_player_session,
        get_session_connections_callback=manager.get_session_connections,
        get_player_websockets=lambda pid: manager.player_websockets.get(pid, []),
        get_online_players=lambda: manager.online_players,
        get_session_connections=lambda: manager.session_connections,
        get_player_sessions=lambda: manager.player_sessions,
    )


def initialize_connection_cleaner(manager: Any) -> None:
    """Initialize the connection cleaner with required callbacks."""
    # Accessing protected members is necessary for initialization
    # pylint: disable=protected-access  # Reason: Initialization requires access to internal manager method (_cleanup_dead_websocket) for callback setup, manager is guaranteed to have this method
    manager.connection_cleaner = ConnectionCleaner(
        memory_monitor=manager.memory_monitor,
        rate_limiter=manager.rate_limiter,
        message_queue=manager.message_queue,
        room_manager=manager.room_manager,
        cleanup_dead_websocket_callback=manager._cleanup_dead_websocket,
        has_websocket_connection_callback=manager.has_websocket_connection,
        get_async_persistence=lambda: manager.async_persistence,
    )


def initialize_game_state_provider(manager: Any) -> None:
    """Initialize the game state provider with required callbacks."""
    manager.game_state_provider = GameStateProvider(
        room_manager=manager.room_manager,
        get_async_persistence=lambda: manager.async_persistence,
        send_personal_message_callback=manager.send_personal_message,
        get_app=lambda: manager.app,
    )


def initialize_messaging(manager: Any) -> None:
    """Initialize messaging components with required callbacks."""
    # Accessing protected members is necessary for initialization
    # pylint: disable=protected-access  # Reason: Initialization requires access to internal manager methods (_cleanup_dead_websocket, _convert_uuids_to_strings) for callback setup, manager is guaranteed to have these methods
    manager.personal_message_sender = PersonalMessageSender(
        message_queue=manager.message_queue,
        cleanup_dead_websocket_callback=manager._cleanup_dead_websocket,
        convert_uuids_to_strings=manager._convert_uuids_to_strings,
    )
    manager.message_broadcaster = MessageBroadcaster(
        room_manager=manager.room_manager,
        send_personal_message_callback=manager.send_personal_message,
    )


def initialize_room_event_handler(manager: Any) -> None:
    """Initialize the room event handler with required callbacks."""
    # Accessing protected members is necessary for initialization
    # pylint: disable=protected-access  # Reason: Initialization requires access to internal manager method (_event_bus) for callback setup, manager is guaranteed to have this method
    manager.room_event_handler = RoomEventHandler(
        room_manager=manager.room_manager,
        get_event_bus=lambda: manager._event_bus,
        get_event_publisher=lambda: manager.event_publisher,
        broadcast_to_room_callback=manager.broadcast_to_room,
        get_online_players=lambda: manager.online_players,
    )
