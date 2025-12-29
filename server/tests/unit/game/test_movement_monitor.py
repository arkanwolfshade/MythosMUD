"""
Unit tests for movement monitor.

Tests the MovementMonitor class for monitoring and validating movement operations.
"""

import uuid
from unittest.mock import MagicMock

import pytest

from server.game.movement_monitor import MovementMonitor, get_movement_monitor, reset_movement_monitor


@pytest.fixture
def movement_monitor():
    """Create a MovementMonitor instance."""
    return MovementMonitor()


@pytest.fixture
def sample_player_id():
    """Create a sample player ID."""
    return uuid.uuid4()


def test_movement_monitor_init(movement_monitor):
    """Test MovementMonitor initialization."""
    assert movement_monitor._movement_count == 0
    assert movement_monitor._failed_movements == 0
    assert movement_monitor._concurrent_movements == 0
    assert movement_monitor._max_concurrent_movements == 0
    assert movement_monitor._integrity_checks == 0
    assert movement_monitor._integrity_violations == 0


def test_record_movement_attempt_success(movement_monitor, sample_player_id):
    """Test record_movement_attempt() records successful movement."""
    movement_monitor.record_movement_attempt(sample_player_id, "room_001", "room_002", success=True, duration_ms=50.0)
    assert movement_monitor._movement_count == 1
    assert movement_monitor._failed_movements == 0
    assert len(movement_monitor._movement_times) == 1
    assert movement_monitor._movement_times[0] == 50.0
    # Room occupancy uses max(0, ...) so it can't go below 0
    assert movement_monitor._room_occupancy["room_001"] == 0  # max(0, 0-1) = 0
    assert movement_monitor._room_occupancy["room_002"] == 1


def test_record_movement_attempt_failure(movement_monitor, sample_player_id):
    """Test record_movement_attempt() records failed movement."""
    movement_monitor.record_movement_attempt(sample_player_id, "room_001", "room_002", success=False, duration_ms=30.0)
    assert movement_monitor._movement_count == 1
    assert movement_monitor._failed_movements == 1
    assert len(movement_monitor._movement_times) == 1
    # Failed movements don't update room occupancy
    assert movement_monitor._room_occupancy["room_001"] == 0
    assert movement_monitor._room_occupancy["room_002"] == 0


def test_record_movement_attempt_string_player_id(movement_monitor):
    """Test record_movement_attempt() handles string player_id."""
    player_id_str = str(uuid.uuid4())
    movement_monitor.record_movement_attempt(player_id_str, "room_001", "room_002", success=True, duration_ms=40.0)
    assert movement_monitor._movement_count == 1
    assert player_id_str in movement_monitor._player_movements


def test_record_movement_attempt_uuid_player_id(movement_monitor, sample_player_id):
    """Test record_movement_attempt() handles UUID player_id."""
    movement_monitor.record_movement_attempt(sample_player_id, "room_001", "room_002", success=True, duration_ms=40.0)
    assert movement_monitor._movement_count == 1
    assert str(sample_player_id) in movement_monitor._player_movements


def test_record_movement_attempt_multiple_players(movement_monitor):
    """Test record_movement_attempt() tracks multiple players."""
    player1 = uuid.uuid4()
    player2 = uuid.uuid4()
    movement_monitor.record_movement_attempt(player1, "room_001", "room_002", success=True, duration_ms=50.0)
    movement_monitor.record_movement_attempt(player2, "room_002", "room_003", success=True, duration_ms=60.0)
    assert movement_monitor._player_movements[str(player1)] == 1
    assert movement_monitor._player_movements[str(player2)] == 1


def test_record_concurrent_movement(movement_monitor):
    """Test record_concurrent_movement() updates concurrent count."""
    movement_monitor.record_concurrent_movement(5)
    assert movement_monitor._concurrent_movements == 5
    assert movement_monitor._max_concurrent_movements == 5


def test_record_concurrent_movement_updates_max(movement_monitor):
    """Test record_concurrent_movement() updates max concurrent."""
    movement_monitor.record_concurrent_movement(5)
    movement_monitor.record_concurrent_movement(3)
    assert movement_monitor._concurrent_movements == 3
    assert movement_monitor._max_concurrent_movements == 5  # Max should remain


def test_record_integrity_check_no_violation(movement_monitor):
    """Test record_integrity_check() records check without violation."""
    movement_monitor.record_integrity_check(violation_found=False)
    assert movement_monitor._integrity_checks == 1
    assert movement_monitor._integrity_violations == 0
    assert movement_monitor._last_validation_time is not None


def test_record_integrity_check_with_violation(movement_monitor):
    """Test record_integrity_check() records check with violation."""
    movement_monitor.record_integrity_check(violation_found=True)
    assert movement_monitor._integrity_checks == 1
    assert movement_monitor._integrity_violations == 1
    assert movement_monitor._last_validation_time is not None


def test_validate_room_integrity_valid(movement_monitor):
    """Test validate_room_integrity() with valid room data."""
    mock_room1 = MagicMock()
    mock_room1.get_players = MagicMock(return_value=["player1", "player2"])
    mock_room2 = MagicMock()
    mock_room2.get_players = MagicMock(return_value=["player3"])
    rooms = {"room_001": mock_room1, "room_002": mock_room2}

    result = movement_monitor.validate_room_integrity(rooms)
    assert result["valid"] is True
    assert len(result["violations"]) == 0
    assert result["total_rooms"] == 2
    assert result["total_players"] == 3


def test_validate_room_integrity_duplicate_players(movement_monitor):
    """Test validate_room_integrity() detects duplicate players."""
    mock_room1 = MagicMock()
    mock_room1.get_players = MagicMock(return_value=["player1"])
    mock_room2 = MagicMock()
    mock_room2.get_players = MagicMock(return_value=["player1"])  # Same player in both rooms
    rooms = {"room_001": mock_room1, "room_002": mock_room2}

    result = movement_monitor.validate_room_integrity(rooms)
    assert result["valid"] is False
    assert len(result["violations"]) > 0
    assert "player1" in result["violations"][0]


def test_validate_room_integrity_empty_rooms(movement_monitor):
    """Test validate_room_integrity() handles empty rooms dict."""
    result = movement_monitor.validate_room_integrity({})
    assert result["valid"] is True
    assert result["total_rooms"] == 0
    assert result["total_players"] == 0


def test_validate_room_integrity_room_without_get_players(movement_monitor):
    """Test validate_room_integrity() handles rooms without get_players method."""
    mock_room = MagicMock()
    del mock_room.get_players  # Remove get_players method
    rooms = {"room_001": mock_room}

    result = movement_monitor.validate_room_integrity(rooms)
    # Should not crash, should handle gracefully
    assert result["total_rooms"] == 1


def test_get_metrics_empty(movement_monitor):
    """Test get_metrics() returns metrics for empty monitor."""
    metrics = movement_monitor.get_metrics()
    assert metrics["total_movements"] == 0
    assert metrics["successful_movements"] == 0
    assert metrics["failed_movements"] == 0
    assert metrics["success_rate"] == 1.0
    assert metrics["failure_rate"] == 0.0
    assert metrics["integrity_checks"] == 0
    assert "timestamp" in metrics


def test_get_metrics_with_data(movement_monitor, sample_player_id):
    """Test get_metrics() returns metrics with movement data."""
    movement_monitor.record_movement_attempt(sample_player_id, "room_001", "room_002", success=True, duration_ms=50.0)
    movement_monitor.record_movement_attempt(sample_player_id, "room_002", "room_003", success=False, duration_ms=30.0)
    movement_monitor.record_integrity_check(violation_found=False)

    metrics = movement_monitor.get_metrics()
    assert metrics["total_movements"] == 2
    assert metrics["successful_movements"] == 1
    assert metrics["failed_movements"] == 1
    assert metrics["success_rate"] == 0.5
    assert metrics["failure_rate"] == 0.5
    assert metrics["integrity_checks"] == 1
    assert metrics["avg_movement_time_ms"] == 40.0


def test_get_metrics_integrity_rate(movement_monitor):
    """Test get_metrics() calculates integrity rate correctly."""
    movement_monitor.record_integrity_check(violation_found=False)
    movement_monitor.record_integrity_check(violation_found=False)
    movement_monitor.record_integrity_check(violation_found=True)

    metrics = movement_monitor.get_metrics()
    assert metrics["integrity_checks"] == 3
    assert metrics["integrity_violations"] == 1
    assert metrics["integrity_rate"] == pytest.approx(2.0 / 3.0)


def test_get_alerts_no_alerts(movement_monitor, sample_player_id):
    """Test get_alerts() returns no alerts when thresholds not exceeded."""
    movement_monitor.record_movement_attempt(sample_player_id, "room_001", "room_002", success=True, duration_ms=50.0)
    alerts = movement_monitor.get_alerts()
    assert len(alerts) == 0


def test_get_alerts_high_concurrent(movement_monitor):
    """Test get_alerts() alerts on high concurrent movements."""
    movement_monitor.record_concurrent_movement(60)  # Above threshold of 50
    alerts = movement_monitor.get_alerts()
    assert len(alerts) > 0
    assert any("concurrent" in alert.lower() for alert in alerts)


def test_get_alerts_high_failure_rate(movement_monitor, sample_player_id):
    """Test get_alerts() alerts on high failure rate."""
    # Record many failed movements to exceed 10% threshold
    for _ in range(10):
        movement_monitor.record_movement_attempt(
            sample_player_id, "room_001", "room_002", success=False, duration_ms=30.0
        )
    for _ in range(5):
        movement_monitor.record_movement_attempt(
            sample_player_id, "room_001", "room_002", success=True, duration_ms=30.0
        )
    # Failure rate: 10/15 = 0.67 > 0.1 threshold
    alerts = movement_monitor.get_alerts()
    assert len(alerts) > 0
    assert any("failure" in alert.lower() for alert in alerts)


def test_get_alerts_slow_movement_time(movement_monitor, sample_player_id):
    """Test get_alerts() alerts on slow movement time."""
    # Record slow movement (above 1000ms threshold)
    movement_monitor.record_movement_attempt(sample_player_id, "room_001", "room_002", success=True, duration_ms=1500.0)
    alerts = movement_monitor.get_alerts()
    assert len(alerts) > 0
    assert any("slow" in alert.lower() or "time" in alert.lower() for alert in alerts)


def test_reset_metrics(movement_monitor, sample_player_id):
    """Test reset_metrics() resets all metrics."""
    movement_monitor.record_movement_attempt(sample_player_id, "room_001", "room_002", success=True, duration_ms=50.0)
    movement_monitor.record_integrity_check(violation_found=True)
    movement_monitor.record_concurrent_movement(5)

    movement_monitor.reset_metrics()

    assert movement_monitor._movement_count == 0
    assert movement_monitor._failed_movements == 0
    assert movement_monitor._concurrent_movements == 0
    assert movement_monitor._max_concurrent_movements == 0
    assert len(movement_monitor._movement_times) == 0
    assert len(movement_monitor._room_occupancy) == 0
    assert len(movement_monitor._player_movements) == 0
    assert movement_monitor._integrity_checks == 0
    assert movement_monitor._integrity_violations == 0


def test_get_movement_monitor_returns_singleton():
    """Test get_movement_monitor() returns singleton instance."""
    monitor1 = get_movement_monitor()
    monitor2 = get_movement_monitor()
    assert monitor1 is monitor2


def test_reset_movement_monitor(movement_monitor):
    """Test reset_movement_monitor() resets global monitor."""
    # Use the global monitor
    monitor = get_movement_monitor()
    monitor.record_movement_attempt(uuid.uuid4(), "room_001", "room_002", success=True, duration_ms=50.0)

    reset_movement_monitor()

    # After reset, metrics should be cleared
    metrics = monitor.get_metrics()
    assert metrics["total_movements"] == 0


def test_log_performance_summary(movement_monitor, sample_player_id):
    """Test log_performance_summary() logs summary without error."""
    movement_monitor.record_movement_attempt(sample_player_id, "room_001", "room_002", success=True, duration_ms=50.0)
    # Should not raise
    movement_monitor.log_performance_summary()


def test_validate_room_integrity_calculates_occupancy(movement_monitor):
    """Test validate_room_integrity() calculates occupancy metrics."""
    mock_room1 = MagicMock()
    mock_room1.get_players = MagicMock(return_value=["player1", "player2", "player3"])
    mock_room2 = MagicMock()
    mock_room2.get_players = MagicMock(return_value=["player4"])
    rooms = {"room_001": mock_room1, "room_002": mock_room2}

    result = movement_monitor.validate_room_integrity(rooms)
    assert result["total_players"] == 4
    assert result["avg_occupancy"] == 2.0  # 4 players / 2 rooms
    assert result["max_occupancy"] == 3  # room_001 has 3 players
