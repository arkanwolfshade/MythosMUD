"""
Unit tests for connection initialization.

Tests the connection_initialization module functions.
"""

from unittest.mock import MagicMock, patch

from server.realtime.connection_initialization import (
    initialize_connection_cleaner,
    initialize_connection_state,
    initialize_core_components,
    initialize_error_handler,
    initialize_game_state_provider,
    initialize_health_monitor,
    initialize_messaging,
    initialize_room_event_handler,
)


def test_initialize_connection_state():
    """Test initialize_connection_state() sets core tracking attributes."""
    mock_manager = MagicMock()
    publisher = MagicMock()

    initialize_connection_state(mock_manager, publisher)

    assert mock_manager.event_publisher is publisher
    assert mock_manager.active_websockets == {}
    assert mock_manager.online_players == {}
    assert mock_manager._health_check_interval == 30.0
    assert mock_manager._closed_websockets.maxlen == 1000


def test_initialize_core_components():
    """Test initialize_core_components() builds modular components."""
    mock_manager = MagicMock()
    mock_memory = MagicMock()
    mock_memory.max_pending_messages = 50

    with (
        patch("server.realtime.connection_initialization.MemoryMonitor", return_value=mock_memory),
        patch("server.realtime.connection_initialization.RateLimiter") as mock_rate,
        patch("server.realtime.connection_initialization.MessageQueue") as mock_queue,
        patch("server.realtime.connection_initialization.RoomSubscriptionManager") as mock_room,
        patch("server.realtime.connection_initialization.PerformanceTracker") as mock_perf,
        patch("server.realtime.connection_initialization.StatisticsAggregator") as mock_stats,
    ):
        initialize_core_components(mock_manager)

        mock_rate.assert_called_once()
        mock_queue.assert_called_once_with(max_messages_per_player=50)
        mock_room.assert_called_once()
        mock_perf.assert_called_once_with(max_samples=1000)
        mock_stats.assert_called_once()
        assert mock_manager.health_monitor is None


def test_initialize_health_monitor():
    """Test initialize_health_monitor() initializes health monitor."""
    mock_manager = MagicMock()
    mock_manager._is_websocket_open = MagicMock()
    mock_manager._validate_token = MagicMock()
    mock_manager._cleanup_dead_websocket = MagicMock()
    mock_manager.performance_tracker = MagicMock()
    mock_manager._health_check_interval = 30
    mock_manager._connection_timeout = 60
    mock_manager._token_revalidation_interval = 300

    with patch("server.realtime.connection_initialization.HealthMonitor") as mock_health_monitor:
        initialize_health_monitor(mock_manager)

        mock_health_monitor.assert_called_once()
        assert hasattr(mock_manager, "health_monitor")


def test_initialize_error_handler():
    """Test initialize_error_handler() initializes error handler."""
    mock_manager = MagicMock()
    mock_manager.force_disconnect_player = MagicMock()
    mock_manager.disconnect_connection_by_id = MagicMock()
    mock_manager.cleanup_dead_connections = MagicMock()
    mock_manager.get_player_session = MagicMock()
    mock_manager.get_session_connections = MagicMock()
    mock_manager.player_websockets = {}
    mock_manager.online_players = {}
    mock_manager.session_connections = {}
    mock_manager.player_sessions = {}

    with patch("server.realtime.connection_initialization.ConnectionErrorHandler") as mock_error_handler:
        initialize_error_handler(mock_manager)

        mock_error_handler.assert_called_once()
        assert hasattr(mock_manager, "error_handler")


def test_initialize_connection_cleaner():
    """Test initialize_connection_cleaner() initializes connection cleaner."""
    mock_manager = MagicMock()
    mock_manager.memory_monitor = MagicMock()
    mock_manager.rate_limiter = MagicMock()
    mock_manager.message_queue = MagicMock()
    mock_manager.room_manager = MagicMock()
    mock_manager._cleanup_dead_websocket = MagicMock()
    mock_manager.has_websocket_connection = MagicMock()
    mock_manager.async_persistence = MagicMock()

    with patch("server.realtime.connection_initialization.ConnectionCleaner") as mock_cleaner:
        initialize_connection_cleaner(mock_manager)

        mock_cleaner.assert_called_once()
        assert hasattr(mock_manager, "connection_cleaner")


def test_initialize_game_state_provider():
    """Test initialize_game_state_provider() initializes game state provider."""
    mock_manager = MagicMock()
    mock_manager.room_manager = MagicMock()
    mock_manager.async_persistence = MagicMock()
    mock_manager.send_personal_message = MagicMock()
    mock_manager.app = MagicMock()

    with patch("server.realtime.connection_initialization.GameStateProvider") as mock_provider:
        initialize_game_state_provider(mock_manager)

        mock_provider.assert_called_once()
        assert hasattr(mock_manager, "game_state_provider")


def test_initialize_messaging():
    """Test initialize_messaging() initializes messaging components."""
    mock_manager = MagicMock()
    mock_manager.message_queue = MagicMock()
    mock_manager._cleanup_dead_websocket = MagicMock()
    mock_manager._convert_uuids_to_strings = MagicMock()
    mock_manager.room_manager = MagicMock()
    mock_manager.send_personal_message = MagicMock()

    with (
        patch("server.realtime.connection_initialization.PersonalMessageSender") as mock_sender,
        patch("server.realtime.connection_initialization.MessageBroadcaster") as mock_broadcaster,
    ):
        initialize_messaging(mock_manager)

        mock_sender.assert_called_once()
        mock_broadcaster.assert_called_once()
        assert hasattr(mock_manager, "personal_message_sender")
        assert hasattr(mock_manager, "message_broadcaster")


def test_initialize_room_event_handler():
    """Test initialize_room_event_handler() initializes room event handler."""
    mock_manager = MagicMock()
    mock_manager.room_manager = MagicMock()
    mock_manager._event_bus = MagicMock()
    mock_manager.event_publisher = MagicMock()
    mock_manager.broadcast_to_room = MagicMock()
    mock_manager.online_players = {}

    with patch("server.realtime.connection_initialization.RoomEventHandler") as mock_handler:
        initialize_room_event_handler(mock_manager)

        mock_handler.assert_called_once()
        assert hasattr(mock_manager, "room_event_handler")
