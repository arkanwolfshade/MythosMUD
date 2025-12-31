"""
Unit tests for connection state machine.

Tests the NATSConnectionStateMachine class and ConnectionEvent enum.
"""

from datetime import UTC, datetime
from unittest.mock import patch

import pytest

from server.realtime.connection_state_machine import ConnectionEvent, NATSConnectionStateMachine


def test_connection_event_enum():
    """Test ConnectionEvent enum values."""
    assert ConnectionEvent.CONNECT_REQUESTED.value == "connect_requested"
    assert ConnectionEvent.CONNECTED.value == "connected"
    assert ConnectionEvent.CONNECTION_FAILED.value == "connection_failed"
    assert ConnectionEvent.DISCONNECTED.value == "disconnected"
    assert ConnectionEvent.RECONNECT_REQUESTED.value == "reconnect_requested"
    assert ConnectionEvent.CIRCUIT_OPENED.value == "circuit_opened"
    assert ConnectionEvent.CIRCUIT_CLOSED.value == "circuit_closed"
    assert ConnectionEvent.HEALTH_CHECK_FAILED.value == "health_check_failed"
    assert ConnectionEvent.HEALTH_CHECK_PASSED.value == "health_check_passed"


def test_nats_connection_state_machine_init():
    """Test NATSConnectionStateMachine initialization."""
    fsm = NATSConnectionStateMachine(connection_id="test-connection", max_reconnect_attempts=5)
    assert fsm.connection_id == "test-connection"
    assert fsm.max_reconnect_attempts == 5
    assert fsm.reconnect_attempts == 0
    assert fsm.last_connected_time is None
    assert fsm.last_error is None
    assert fsm.total_connections == 0
    assert fsm.total_disconnections == 0
    assert fsm.current_state.id == "disconnected"


def test_nats_connection_state_machine_init_defaults():
    """Test NATSConnectionStateMachine initialization with defaults."""
    fsm = NATSConnectionStateMachine(connection_id="test-connection")
    assert fsm.max_reconnect_attempts == 5  # Default


def test_connect_transition():
    """Test connect() transition from disconnected to connecting."""
    fsm = NATSConnectionStateMachine(connection_id="test-connection")
    assert fsm.current_state.id == "disconnected"
    fsm.connect()
    assert fsm.current_state.id == "connecting"
    assert fsm.reconnect_attempts == 0


def test_connected_successfully_from_connecting():
    """Test connected_successfully() transition from connecting to connected."""
    fsm = NATSConnectionStateMachine(connection_id="test-connection")
    fsm.connect()
    assert fsm.current_state.id == "connecting"
    fsm.connected_successfully()
    assert fsm.current_state.id == "connected"
    assert fsm.total_connections == 1
    assert fsm.last_connected_time is not None


def test_connected_successfully_from_reconnecting():
    """Test connected_successfully() transition from reconnecting to connected."""
    fsm = NATSConnectionStateMachine(connection_id="test-connection")
    fsm.connect()
    fsm.connection_failed()
    fsm.start_reconnect()
    assert fsm.current_state.id == "reconnecting"
    fsm.connected_successfully()
    assert fsm.current_state.id == "connected"
    assert fsm.reconnect_attempts == 0  # Reset on successful connection


def test_connection_failed_from_connecting():
    """Test connection_failed() transition from connecting to disconnected."""
    fsm = NATSConnectionStateMachine(connection_id="test-connection")
    fsm.connect()
    error = Exception("Connection failed")
    fsm.connection_failed(error)
    assert fsm.current_state.id == "disconnected"
    assert fsm.last_error == error
    assert fsm.reconnect_attempts == 1


def test_connection_failed_from_reconnecting():
    """Test connection_failed() transition from reconnecting to disconnected."""
    fsm = NATSConnectionStateMachine(connection_id="test-connection")
    fsm.connect()
    fsm.connection_failed()
    fsm.start_reconnect()
    assert fsm.current_state.id == "reconnecting"
    error = Exception("Reconnection failed")
    fsm.connection_failed(error)
    assert fsm.current_state.id == "disconnected"
    assert fsm.reconnect_attempts == 2


def test_disconnect_from_connected():
    """Test disconnect() transition from connected to disconnected."""
    fsm = NATSConnectionStateMachine(connection_id="test-connection")
    fsm.connect()
    fsm.connected_successfully()
    assert fsm.current_state.id == "connected"
    fsm.disconnect()
    assert fsm.current_state.id == "disconnected"
    assert fsm.total_disconnections == 1


def test_disconnect_from_degraded():
    """Test disconnect() transition from degraded to disconnected."""
    fsm = NATSConnectionStateMachine(connection_id="test-connection")
    fsm.connect()
    fsm.connected_successfully()
    fsm.degrade()
    assert fsm.current_state.id == "degraded"
    fsm.disconnect()
    assert fsm.current_state.id == "disconnected"


def test_start_reconnect():
    """Test start_reconnect() transition from disconnected to reconnecting."""
    fsm = NATSConnectionStateMachine(connection_id="test-connection")
    assert fsm.current_state.id == "disconnected"
    fsm.start_reconnect()
    assert fsm.current_state.id == "reconnecting"


def test_degrade():
    """Test degrade() transition from connected to degraded."""
    fsm = NATSConnectionStateMachine(connection_id="test-connection")
    fsm.connect()
    fsm.connected_successfully()
    assert fsm.current_state.id == "connected"
    fsm.degrade()
    assert fsm.current_state.id == "degraded"


def test_recover():
    """Test recover() transition from degraded to connected."""
    fsm = NATSConnectionStateMachine(connection_id="test-connection")
    fsm.connect()
    fsm.connected_successfully()
    fsm.degrade()
    assert fsm.current_state.id == "degraded"
    fsm.recover()
    assert fsm.current_state.id == "connected"


def test_open_circuit():
    """Test open_circuit() transition from reconnecting to circuit_open."""
    fsm = NATSConnectionStateMachine(connection_id="test-connection")
    fsm.connect()
    fsm.connection_failed()
    fsm.start_reconnect()
    assert fsm.current_state.id == "reconnecting"
    fsm.open_circuit()
    assert fsm.current_state.id == "circuit_open"


def test_close_circuit():
    """Test close_circuit() transition from circuit_open to disconnected."""
    fsm = NATSConnectionStateMachine(connection_id="test-connection")
    fsm.connect()
    fsm.connection_failed()
    fsm.start_reconnect()
    fsm.open_circuit()
    assert fsm.current_state.id == "circuit_open"
    fsm.close_circuit()
    assert fsm.current_state.id == "disconnected"


def test_can_attempt_connection_disconnected():
    """Test can_attempt_connection() returns True when disconnected."""
    fsm = NATSConnectionStateMachine(connection_id="test-connection")
    assert fsm.current_state.id == "disconnected"
    assert fsm.can_attempt_connection() is True


def test_can_attempt_connection_connecting():
    """Test can_attempt_connection() returns True when connecting."""
    fsm = NATSConnectionStateMachine(connection_id="test-connection")
    fsm.connect()
    assert fsm.current_state.id == "connecting"
    # Connecting state allows connection attempts (it's already attempting)
    assert fsm.can_attempt_connection() is True


def test_can_attempt_connection_connected():
    """Test can_attempt_connection() returns False when connected."""
    fsm = NATSConnectionStateMachine(connection_id="test-connection")
    fsm.connect()
    fsm.connected_successfully()
    assert fsm.current_state.id == "connected"
    assert fsm.can_attempt_connection() is False


def test_can_attempt_connection_circuit_open():
    """Test can_attempt_connection() returns False when circuit is open."""
    fsm = NATSConnectionStateMachine(connection_id="test-connection")
    fsm.connect()
    fsm.connection_failed()
    fsm.start_reconnect()
    fsm.open_circuit()
    assert fsm.current_state.id == "circuit_open"
    assert fsm.can_attempt_connection() is False


def test_can_attempt_connection_reconnecting():
    """Test can_attempt_connection() returns True when reconnecting."""
    fsm = NATSConnectionStateMachine(connection_id="test-connection")
    fsm.connect()
    fsm.connection_failed()
    fsm.start_reconnect()
    assert fsm.current_state.id == "reconnecting"
    # Reconnecting state allows connection attempts
    assert fsm.can_attempt_connection() is True


def test_should_open_circuit_under_threshold():
    """Test should_open_circuit() returns False when under threshold."""
    fsm = NATSConnectionStateMachine(connection_id="test-connection", max_reconnect_attempts=5)
    fsm.reconnect_attempts = 3
    assert fsm.should_open_circuit() is False


def test_should_open_circuit_at_threshold():
    """Test should_open_circuit() returns True when at threshold."""
    fsm = NATSConnectionStateMachine(connection_id="test-connection", max_reconnect_attempts=5)
    fsm.reconnect_attempts = 5
    assert fsm.should_open_circuit() is True


def test_should_open_circuit_over_threshold():
    """Test should_open_circuit() returns True when over threshold."""
    fsm = NATSConnectionStateMachine(connection_id="test-connection", max_reconnect_attempts=5)
    fsm.reconnect_attempts = 6
    assert fsm.should_open_circuit() is True


def test_get_stats():
    """Test get_stats() returns comprehensive statistics."""
    fsm = NATSConnectionStateMachine(connection_id="test-connection", max_reconnect_attempts=5)
    fsm.reconnect_attempts = 3
    fsm.total_connections = 2
    fsm.total_disconnections = 1
    fsm.last_connected_time = datetime.now(UTC)
    stats = fsm.get_stats()
    assert stats["connection_id"] == "test-connection"
    assert stats["current_state"] == "disconnected"
    assert stats["reconnect_attempts"] == 3
    assert stats["max_reconnect_attempts"] == 5
    assert stats["total_connections"] == 2
    assert stats["total_disconnections"] == 1
    assert stats["last_connected_time"] is not None
    assert "last_error" in stats


def test_get_stats_with_error():
    """Test get_stats() includes error information when set."""
    fsm = NATSConnectionStateMachine(connection_id="test-connection")
    error = Exception("Test error")
    fsm.last_error = error
    stats = fsm.get_stats()
    assert stats["last_error"] == "Test error"


def test_get_stats_no_error():
    """Test get_stats() handles None error."""
    fsm = NATSConnectionStateMachine(connection_id="test-connection")
    fsm.last_error = None
    stats = fsm.get_stats()
    assert stats["last_error"] is None


def test_get_stats_no_connected_time():
    """Test get_stats() handles None connected time."""
    fsm = NATSConnectionStateMachine(connection_id="test-connection")
    fsm.last_connected_time = None
    stats = fsm.get_stats()
    assert stats["last_connected_time"] is None


def test_reconnect_attempts_increment():
    """Test reconnect_attempts increments on connection failures."""
    fsm = NATSConnectionStateMachine(connection_id="test-connection")
    assert fsm.reconnect_attempts == 0
    fsm.connect()
    fsm.connection_failed()
    assert fsm.reconnect_attempts == 1
    fsm.start_reconnect()
    fsm.connection_failed()
    assert fsm.reconnect_attempts == 2


def test_reconnect_attempts_reset_on_success():
    """Test reconnect_attempts resets on successful connection."""
    fsm = NATSConnectionStateMachine(connection_id="test-connection")
    fsm.connect()
    fsm.connection_failed()
    fsm.start_reconnect()
    assert fsm.reconnect_attempts == 1
    fsm.connected_successfully()
    assert fsm.reconnect_attempts == 0


def test_total_connections_increment():
    """Test total_connections increments on successful connection."""
    fsm = NATSConnectionStateMachine(connection_id="test-connection")
    assert fsm.total_connections == 0
    fsm.connect()
    fsm.connected_successfully()
    assert fsm.total_connections == 1
    fsm.disconnect()
    fsm.connect()
    fsm.connected_successfully()
    assert fsm.total_connections == 2


def test_total_disconnections_increment():
    """Test total_disconnections increments on disconnect."""
    fsm = NATSConnectionStateMachine(connection_id="test-connection")
    assert fsm.total_disconnections == 0
    fsm.connect()
    fsm.connected_successfully()
    fsm.disconnect()
    assert fsm.total_disconnections == 1
    fsm.connect()
    fsm.connected_successfully()
    fsm.disconnect()
    assert fsm.total_disconnections == 2


def test_last_connected_time_set():
    """Test last_connected_time is set on successful connection."""
    fsm = NATSConnectionStateMachine(connection_id="test-connection")
    assert fsm.last_connected_time is None
    fsm.connect()
    fsm.connected_successfully()
    assert fsm.last_connected_time is not None
    assert isinstance(fsm.last_connected_time, datetime)


def test_last_error_set():
    """Test last_error is set on connection failure."""
    fsm = NATSConnectionStateMachine(connection_id="test-connection")
    assert fsm.last_error is None
    fsm.connect()
    error = Exception("Connection failed")
    fsm.connection_failed(error)
    assert fsm.last_error == error


def test_on_enter_state_logs():
    """Test on_enter_state() logs state transitions."""
    fsm = NATSConnectionStateMachine(connection_id="test-connection")
    with patch("server.realtime.connection_state_machine.logger") as mock_logger:
        fsm.connect()
        # Should log state transition
        assert mock_logger.info.called


def test_invalid_transition_raises_error():
    """Test invalid state transitions raise errors."""
    from statemachine.exceptions import TransitionNotAllowed

    fsm = NATSConnectionStateMachine(connection_id="test-connection")
    # Cannot open circuit from disconnected state
    with pytest.raises(TransitionNotAllowed):  # StateMachine raises TransitionNotAllowed
        fsm.open_circuit()
