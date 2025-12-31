"""
Unit tests for connection initialization.

Tests the connection_initialization module functions.
"""

from unittest.mock import MagicMock, patch

from server.realtime.connection_initialization import (
    initialize_connection_cleaner,
    initialize_error_handler,
    initialize_game_state_provider,
    initialize_health_monitor,
    initialize_messaging,
    initialize_room_event_handler,
)


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
