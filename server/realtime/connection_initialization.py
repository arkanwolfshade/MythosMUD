"""
Initialization helpers for connection manager.

This module provides helper functions for initializing the connection manager
and its various components.
"""

from typing import Any

from .errors.error_handler import ConnectionErrorHandler
from .integration.game_state_provider import GameStateProvider
from .integration.room_event_handler import RoomEventHandler
from .maintenance.connection_cleaner import ConnectionCleaner
from .messaging.message_broadcaster import MessageBroadcaster
from .messaging.personal_message_sender import PersonalMessageSender
from .monitoring.health_monitor import HealthMonitor


def initialize_health_monitor(manager: Any) -> None:
    """Initialize the health monitor with required callbacks."""
    # Accessing protected members is necessary for initialization
    # pylint: disable=protected-access
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
    # pylint: disable=protected-access
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
    # pylint: disable=protected-access
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
    # pylint: disable=protected-access
    manager.room_event_handler = RoomEventHandler(
        room_manager=manager.room_manager,
        get_event_bus=lambda: manager._event_bus,
        get_event_publisher=lambda: manager.event_publisher,
        broadcast_to_room_callback=manager.broadcast_to_room,
        get_online_players=lambda: manager.online_players,
    )
