"""
Unit tests for the movement monitoring system.

This module tests the MovementMonitor class and its integration
with the movement system to ensure proper metrics tracking,
validation, and alerting.

As noted in the Pnakotic Manuscripts, comprehensive testing of
monitoring systems is essential for maintaining the integrity
of our eldritch architecture.
"""

from server.game.movement_monitor import MovementMonitor, get_movement_monitor, reset_movement_monitor
from server.models.room import Room


class TestMovementMonitor:
    """Test the MovementMonitor class."""

    def setup_method(self) -> None:
        """Reset the monitor before each test."""
        reset_movement_monitor()

    def test_monitor_creation(self) -> None:
        """Test that the monitor can be created."""
        monitor = MovementMonitor()
        assert monitor is not None
        metrics = monitor.get_metrics()
        assert metrics["total_movements"] == 0
        assert metrics["failed_movements"] == 0

    def test_record_movement_attempt_success(self) -> None:
        """Test recording a successful movement attempt."""
        monitor = MovementMonitor()

        monitor.record_movement_attempt("player1", "room1", "room2", True, 50.0)

        metrics = monitor.get_metrics()
        assert metrics["total_movements"] == 1
        assert metrics["successful_movements"] == 1
        assert metrics["failed_movements"] == 0
        assert metrics["success_rate"] == 1.0
        assert metrics["avg_movement_time_ms"] == 50.0

    def test_record_movement_attempt_failure(self) -> None:
        """Test recording a failed movement attempt."""
        monitor = MovementMonitor()

        monitor.record_movement_attempt("player1", "room1", "room2", False, 25.0)

        metrics = monitor.get_metrics()
        assert metrics["total_movements"] == 1
        assert metrics["successful_movements"] == 0
        assert metrics["failed_movements"] == 1
        assert metrics["success_rate"] == 0.0
        assert metrics["failure_rate"] == 1.0

    def test_record_multiple_movements(self) -> None:
        """Test recording multiple movement attempts."""
        monitor = MovementMonitor()

        # Record multiple movements
        monitor.record_movement_attempt("player1", "room1", "room2", True, 50.0)
        monitor.record_movement_attempt("player2", "room2", "room3", True, 75.0)
        monitor.record_movement_attempt("player3", "room3", "room1", False, 100.0)

        metrics = monitor.get_metrics()
        assert metrics["total_movements"] == 3
        assert metrics["successful_movements"] == 2
        assert metrics["failed_movements"] == 1
        assert metrics["success_rate"] == 2 / 3
        assert metrics["failure_rate"] == 1 / 3
        assert metrics["avg_movement_time_ms"] == 75.0

    def test_record_concurrent_movement(self) -> None:
        """Test recording concurrent movement count."""
        monitor = MovementMonitor()

        monitor.record_concurrent_movement(5)
        monitor.record_concurrent_movement(10)
        monitor.record_concurrent_movement(3)

        metrics = monitor.get_metrics()
        assert metrics["current_concurrent_movements"] == 3
        assert metrics["max_concurrent_movements"] == 10

    def test_record_integrity_check(self) -> None:
        """Test recording integrity check results."""
        monitor = MovementMonitor()

        monitor.record_integrity_check(False)  # No violation
        monitor.record_integrity_check(True)  # Violation found
        monitor.record_integrity_check(False)  # No violation

        metrics = monitor.get_metrics()
        assert metrics["integrity_checks"] == 3
        assert metrics["integrity_violations"] == 1
        assert metrics["integrity_rate"] == 2 / 3

    def test_validate_room_integrity_valid(self) -> None:
        """Test room integrity validation with valid data."""
        monitor = MovementMonitor()

        # Create valid rooms
        room1 = Room({"id": "room1", "name": "Room 1", "description": "First room", "exits": {}})
        room2 = Room({"id": "room2", "name": "Room 2", "description": "Second room", "exits": {}})

        # Add players to rooms
        room1.player_entered("player1")
        room2.player_entered("player2")

        rooms = {"room1": room1, "room2": room2}

        result = monitor.validate_room_integrity(rooms)

        assert result["valid"] is True
        assert len(result["violations"]) == 0
        assert result["total_rooms"] == 2
        assert result["total_players"] == 2
        assert result["avg_occupancy"] == 1.0
        assert result["max_occupancy"] == 1

    def test_validate_room_integrity_duplicate_player(self) -> None:
        """Test room integrity validation with duplicate player."""
        monitor = MovementMonitor()

        # Create rooms with duplicate player
        room1 = Room({"id": "room1", "name": "Room 1", "description": "First room", "exits": {}})
        room2 = Room({"id": "room2", "name": "Room 2", "description": "Second room", "exits": {}})

        # Add same player to both rooms (violation)
        room1.player_entered("player1")
        room2.player_entered("player1")

        rooms = {"room1": room1, "room2": room2}

        result = monitor.validate_room_integrity(rooms)

        assert result["valid"] is False
        assert len(result["violations"]) == 1
        assert "Player player1 found in multiple rooms" in result["violations"][0]
        assert result["total_rooms"] == 2
        assert result["total_players"] == 2

    def test_validate_room_integrity_empty_rooms(self) -> None:
        """Test room integrity validation with empty rooms."""
        monitor = MovementMonitor()

        room1 = Room({"id": "room1", "name": "Room 1", "description": "First room", "exits": {}})
        room2 = Room({"id": "room2", "name": "Room 2", "description": "Second room", "exits": {}})

        rooms = {"room1": room1, "room2": room2}

        result = monitor.validate_room_integrity(rooms)

        assert result["valid"] is True
        assert len(result["violations"]) == 0
        assert result["total_rooms"] == 2
        assert result["total_players"] == 0
        assert result["avg_occupancy"] == 0.0
        assert result["max_occupancy"] == 0

    def test_get_alerts_no_alerts(self) -> None:
        """Test getting alerts when no thresholds are exceeded."""
        monitor = MovementMonitor()

        # Record some normal movements
        monitor.record_movement_attempt("player1", "room1", "room2", True, 50.0)
        monitor.record_movement_attempt("player2", "room2", "room3", True, 75.0)

        alerts = monitor.get_alerts()
        assert len(alerts) == 0

    def test_get_alerts_high_failure_rate(self) -> None:
        """Test getting alerts when failure rate is high."""
        monitor = MovementMonitor()

        # Record mostly failed movements
        for i in range(10):
            monitor.record_movement_attempt(f"player{i}", "room1", "room2", False, 50.0)

        # Record one successful movement
        monitor.record_movement_attempt("player10", "room1", "room2", True, 50.0)

        alerts = monitor.get_alerts()
        assert len(alerts) > 0
        assert any("High failure rate" in alert for alert in alerts)

    def test_get_alerts_high_concurrent_movements(self) -> None:
        """Test getting alerts when concurrent movements are high."""
        monitor = MovementMonitor()

        # Record high concurrent movements
        monitor.record_concurrent_movement(60)  # Above threshold of 50

        alerts = monitor.get_alerts()
        assert len(alerts) > 0
        assert any("High concurrent movements" in alert for alert in alerts)

    def test_reset_metrics(self) -> None:
        """Test resetting all metrics."""
        monitor = MovementMonitor()

        # Record some movements
        monitor.record_movement_attempt("player1", "room1", "room2", True, 50.0)
        monitor.record_movement_attempt("player2", "room2", "room3", False, 75.0)
        monitor.record_concurrent_movement(10)
        monitor.record_integrity_check(True)

        # Reset metrics
        monitor.reset_metrics()

        metrics = monitor.get_metrics()
        assert metrics["total_movements"] == 0
        assert metrics["failed_movements"] == 0
        assert metrics["current_concurrent_movements"] == 0
        assert metrics["max_concurrent_movements"] == 0
        assert metrics["integrity_checks"] == 0
        assert metrics["integrity_violations"] == 0

    def test_log_performance_summary(self) -> None:
        """Test logging performance summary."""
        monitor = MovementMonitor()

        # Record some movements
        monitor.record_movement_attempt("player1", "room1", "room2", True, 50.0)
        monitor.record_movement_attempt("player2", "room2", "room3", False, 75.0)
        monitor.record_concurrent_movement(5)
        monitor.record_integrity_check(False)

        # This should not raise an exception
        monitor.log_performance_summary()

    def test_global_monitor_singleton(self) -> None:
        """Test that get_movement_monitor returns the same instance."""
        monitor1 = get_movement_monitor()
        monitor2 = get_movement_monitor()

        assert monitor1 is monitor2

    def test_reset_global_monitor(self) -> None:
        """Test resetting the global monitor."""
        monitor1 = get_movement_monitor()
        monitor1.record_movement_attempt("player1", "room1", "room2", True, 50.0)

        # Reset should clear metrics
        reset_movement_monitor()
        monitor2 = get_movement_monitor()

        metrics = monitor2.get_metrics()
        assert metrics["total_movements"] == 0

    def test_metrics_calculation_edge_cases(self) -> None:
        """Test metrics calculation with edge cases."""
        monitor = MovementMonitor()

        # Test with no movements
        metrics = monitor.get_metrics()
        assert metrics["success_rate"] == 1.0  # Default when no movements
        assert metrics["failure_rate"] == 0.0
        assert metrics["avg_movement_time_ms"] == 0
        assert metrics["movements_per_second"] == 0
        assert metrics["integrity_rate"] == 1.0  # Default when no checks

    def test_room_occupancy_tracking(self) -> None:
        """Test that room occupancy is tracked correctly."""
        monitor = MovementMonitor()

        # Record successful movements
        monitor.record_movement_attempt("player1", "room1", "room2", True, 50.0)
        monitor.record_movement_attempt("player2", "room2", "room3", True, 75.0)
        monitor.record_movement_attempt("player3", "room3", "room1", True, 100.0)

        metrics = monitor.get_metrics()
        room_occupancy = metrics["room_occupancy"]

        # Check that room occupancy is tracked
        assert "room1" in room_occupancy
        assert "room2" in room_occupancy
        assert "room3" in room_occupancy

    def test_player_movement_counts(self) -> None:
        """Test that player movement counts are tracked."""
        monitor = MovementMonitor()

        # Record movements for same player
        monitor.record_movement_attempt("player1", "room1", "room2", True, 50.0)
        monitor.record_movement_attempt("player1", "room2", "room3", True, 75.0)
        monitor.record_movement_attempt("player2", "room3", "room1", True, 100.0)

        metrics = monitor.get_metrics()
        player_movements = metrics["player_movement_counts"]

        assert player_movements["player1"] == 2
        assert player_movements["player2"] == 1

    def test_movement_time_tracking(self) -> None:
        """Test that movement times are tracked correctly."""
        monitor = MovementMonitor()

        # Record movements with different times
        monitor.record_movement_attempt("player1", "room1", "room2", True, 50.0)
        monitor.record_movement_attempt("player2", "room2", "room3", True, 150.0)
        monitor.record_movement_attempt("player3", "room3", "room1", True, 25.0)

        metrics = monitor.get_metrics()
        assert metrics["avg_movement_time_ms"] == 75.0
        assert metrics["max_movement_time_ms"] == 150.0
        assert metrics["min_movement_time_ms"] == 25.0

    def test_get_alerts_high_integrity_violation_rate(self) -> None:
        """Test alert when integrity violation rate is high.

        AI: Tests line 219 in movement_monitor.py where high integrity violation
        rate triggers an alert. Covers the alert generation for data integrity issues.
        """
        monitor = MovementMonitor()

        # Record many integrity checks with violations
        for _ in range(20):
            monitor.record_integrity_check(violation_found=True)

        # Record only a few movements to make violation rate high
        monitor.record_movement_attempt("player1", "room1", "room2", True, 50.0)

        alerts = monitor.get_alerts()
        # Should have an alert about high integrity violation rate
        assert len(alerts) > 0
        # One of the alerts should be about integrity violations
        assert any("integrity" in alert.lower() for alert in alerts)

    def test_get_alerts_slow_average_movement_time(self) -> None:
        """Test alert when average movement time exceeds threshold.

        AI: Tests line 222 in movement_monitor.py where slow average movement
        times trigger an alert. Covers the performance monitoring alert path.
        """
        monitor = MovementMonitor()

        # Record movements with very slow times (threshold is 1000ms)
        for i in range(10):
            monitor.record_movement_attempt(f"player{i}", "room1", "room2", True, 2000.0)

        alerts = monitor.get_alerts()
        assert len(alerts) > 0
        assert any("Slow average movement time" in alert for alert in alerts)

    def test_reset_movement_monitor_creates_new_monitor(self) -> None:
        """Test reset_movement_monitor when no monitor exists.

        AI: Tests line 295 in movement_monitor.py where a new MovementMonitor
        is created if none exists. Covers the initialization path in reset function.
        """
        # This test uses the module-level reset function
        # reset_movement_monitor is already imported at the top of the file

        # Call reset which should ensure a monitor exists
        reset_movement_monitor()

        # Get the monitor and verify it's initialized
        monitor = get_movement_monitor()
        assert monitor is not None
        metrics = monitor.get_metrics()
        assert metrics["total_movements"] == 0
