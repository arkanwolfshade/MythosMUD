"""
Tests for the monitoring API endpoints.

This module tests the monitoring API endpoints to ensure they
provide accurate metrics, validation, and alerting data.

As noted in the Pnakotic Manuscripts, comprehensive testing of
monitoring APIs is essential for maintaining oversight of our
eldritch systems.
"""

from unittest.mock import Mock, patch

from fastapi.testclient import TestClient

from server.app.factory import create_app
from server.game.movement_monitor import reset_movement_monitor


class TestMonitoringAPI:
    """Test the monitoring API endpoints."""

    def setup_method(self):
        """Set up test environment."""
        self.app = create_app()
        self.client = TestClient(self.app)
        reset_movement_monitor()

    def test_get_movement_metrics(self):
        """Test getting movement metrics."""
        response = self.client.get("/monitoring/metrics")

        assert response.status_code == 200
        data = response.json()

        # Check required fields
        assert "total_movements" in data
        assert "successful_movements" in data
        assert "failed_movements" in data
        assert "success_rate" in data
        assert "failure_rate" in data
        assert "avg_movement_time_ms" in data
        assert "timestamp" in data

        # Check initial values
        assert data["total_movements"] == 0
        assert data["successful_movements"] == 0
        assert data["failed_movements"] == 0
        assert data["success_rate"] == 1.0  # Default when no movements
        assert data["failure_rate"] == 0.0

    def test_validate_room_integrity(self):
        """Test room integrity validation."""
        response = self.client.get("/monitoring/integrity")

        assert response.status_code == 200
        data = response.json()

        # Check required fields
        assert "valid" in data
        assert "violations" in data
        assert "total_rooms" in data
        assert "total_players" in data
        assert "avg_occupancy" in data
        assert "max_occupancy" in data
        assert "timestamp" in data

        # Check data types
        assert isinstance(data["valid"], bool)
        assert isinstance(data["violations"], list)
        assert isinstance(data["total_rooms"], int)
        assert isinstance(data["total_players"], int)
        assert isinstance(data["avg_occupancy"], float)
        assert isinstance(data["max_occupancy"], int)

    def test_get_system_alerts(self):
        """Test getting system alerts."""
        response = self.client.get("/monitoring/alerts")

        assert response.status_code == 200
        data = response.json()

        # Check required fields
        assert "alerts" in data
        assert "alert_count" in data
        assert "timestamp" in data

        # Check data types
        assert isinstance(data["alerts"], list)
        assert isinstance(data["alert_count"], int)
        assert isinstance(data["timestamp"], str)

        # Initially should have no alerts
        assert data["alert_count"] == 0
        assert len(data["alerts"]) == 0

    def test_reset_metrics(self):
        """Test resetting metrics."""
        response = self.client.post("/monitoring/reset")

        assert response.status_code == 200
        data = response.json()

        assert "message" in data
        assert data["message"] == "Metrics reset successfully"

    def test_get_performance_summary(self):
        """Test getting performance summary."""
        response = self.client.get("/monitoring/performance-summary")

        assert response.status_code == 200
        data = response.json()

        # Check required fields
        assert "summary" in data
        assert "alerts" in data
        assert "timestamp" in data

        summary = data["summary"]
        assert "total_movements" in summary
        assert "success_rate" in summary
        assert "avg_movement_time" in summary
        assert "current_concurrent" in summary
        assert "max_concurrent" in summary
        assert "integrity_rate" in summary
        assert "uptime" in summary
        assert "alert_count" in summary

        # Check data types
        assert isinstance(summary["total_movements"], int)
        assert isinstance(summary["success_rate"], str)
        assert isinstance(summary["avg_movement_time"], str)
        assert isinstance(summary["current_concurrent"], int)
        assert isinstance(summary["max_concurrent"], int)
        assert isinstance(summary["integrity_rate"], str)
        assert isinstance(summary["uptime"], str)
        assert isinstance(summary["alert_count"], int)
        assert isinstance(data["alerts"], list)
        assert isinstance(data["timestamp"], str)

    def test_metrics_with_movements(self):
        """Test metrics after recording some movements."""
        from server.game.movement_monitor import get_movement_monitor

        # Record some movements
        monitor = get_movement_monitor()
        monitor.record_movement_attempt("player1", "room1", "room2", True, 50.0)
        monitor.record_movement_attempt("player2", "room2", "room3", False, 75.0)
        monitor.record_movement_attempt("player3", "room3", "room1", True, 100.0)

        response = self.client.get("/monitoring/metrics")

        assert response.status_code == 200
        data = response.json()

        assert data["total_movements"] == 3
        assert data["successful_movements"] == 2
        assert data["failed_movements"] == 1
        assert data["success_rate"] == 2 / 3
        assert data["failure_rate"] == 1 / 3
        assert data["avg_movement_time_ms"] == 75.0

    def test_alerts_with_high_failure_rate(self):
        """Test alerts when failure rate is high."""
        from server.game.movement_monitor import get_movement_monitor

        # Record mostly failed movements to trigger alert
        monitor = get_movement_monitor()
        for i in range(10):
            monitor.record_movement_attempt(f"player{i}", "room1", "room2", False, 50.0)

        # Record one successful movement
        monitor.record_movement_attempt("player10", "room1", "room2", True, 50.0)

        response = self.client.get("/monitoring/alerts")

        assert response.status_code == 200
        data = response.json()

        assert data["alert_count"] > 0
        assert any("High failure rate" in alert for alert in data["alerts"])

    def test_integrity_with_duplicate_player(self):
        """Test integrity validation with duplicate player."""
        from server.models.room import Room

        # Create rooms with duplicate player
        room1 = Room({"id": "room1", "name": "Room 1", "description": "First room", "exits": {}})
        room2 = Room({"id": "room2", "name": "Room 2", "description": "Second room", "exits": {}})

        # Add same player to both rooms (violation)
        room1.player_entered("player1")
        room2.player_entered("player1")

        # Mock persistence to return our test rooms
        with patch("server.api.monitoring.get_persistence") as mock_get_persistence:
            mock_persistence = Mock()
            mock_persistence.list_rooms.return_value = [room1, room2]
            mock_get_persistence.return_value = mock_persistence

            response = self.client.get("/monitoring/integrity")

            assert response.status_code == 200
            data = response.json()

            assert data["valid"] is False
            assert len(data["violations"]) == 1
            assert "Player player1 found in multiple rooms" in data["violations"][0]

    def test_error_handling(self):
        """Test error handling in monitoring endpoints."""
        # Test with mocked error
        with patch("server.api.monitoring.get_movement_monitor") as mock_get_monitor:
            mock_get_monitor.side_effect = Exception("Test error")

            response = self.client.get("/monitoring/metrics")

            assert response.status_code == 500
            data = response.json()
            assert "error" in data
            assert "Error retrieving metrics" in data["error"]["message"]

    def test_performance_summary_formatting(self):
        """Test that performance summary formats values correctly."""
        from server.game.movement_monitor import get_movement_monitor

        # Record some movements
        monitor = get_movement_monitor()
        monitor.record_movement_attempt("player1", "room1", "room2", True, 50.0)
        monitor.record_movement_attempt("player2", "room2", "room3", False, 75.0)

        response = self.client.get("/monitoring/performance-summary")

        assert response.status_code == 200
        data = response.json()

        summary = data["summary"]

        # Check that percentages are formatted correctly
        assert "%" in summary["success_rate"]
        assert "%" in summary["integrity_rate"]

        # Check that time values are formatted correctly
        assert "ms" in summary["avg_movement_time"]
        assert "s" in summary["uptime"]

    def test_api_endpoints_consistency(self):
        """Test that all monitoring endpoints return consistent data."""
        # Get metrics
        metrics_response = self.client.get("/monitoring/metrics")
        assert metrics_response.status_code == 200
        metrics_data = metrics_response.json()

        # Get performance summary
        summary_response = self.client.get("/monitoring/performance-summary")
        assert summary_response.status_code == 200
        summary_data = summary_response.json()

        # Check that summary data matches metrics data
        assert summary_data["summary"]["total_movements"] == metrics_data["total_movements"]
        assert summary_data["summary"]["alert_count"] == metrics_data.get("alert_count", 0)

        # Get alerts
        alerts_response = self.client.get("/monitoring/alerts")
        assert alerts_response.status_code == 200
        alerts_data = alerts_response.json()

        # Check that alert count is consistent
        assert summary_data["summary"]["alert_count"] == alerts_data["alert_count"]
