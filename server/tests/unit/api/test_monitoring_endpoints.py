"""
Tests for monitoring API endpoints with dual connection support.

This module tests the new monitoring API endpoints that provide dual connection
statistics, performance metrics, and connection health information.
"""

from unittest.mock import AsyncMock, MagicMock, Mock, patch

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from server.api.monitoring import monitoring_router
from server.app.factory import create_app
from server.game.movement_monitor import reset_movement_monitor


class TestMonitoringAPIEndpoints:
    """Test monitoring API endpoints."""

    @pytest.fixture
    def app(self):
        """Create a FastAPI app with monitoring router."""
        app = FastAPI()
        app.include_router(monitoring_router)
        return app

    @pytest.fixture
    def client(self, app):
        """Create a test client."""
        return TestClient(app)

    @pytest.fixture
    def mock_connection_manager(self):
        """Create a mock connection manager."""
        manager = Mock()

        # Mock dual connection stats
        manager.get_dual_connection_stats.return_value = {
            "connection_distribution": {
                "total_players": 10,
                "websocket_only_players": 5,
                "sse_only_players": 2,
                "dual_connection_players": 3,
                "dual_connection_percentage": 30.0,
            },
            "connection_health": {
                "total_connections": 15,
                "healthy_connections": 14,
                "unhealthy_connections": 1,
                "health_percentage": 93.3,
            },
            "session_metrics": {
                "total_sessions": 8,
                "total_session_connections": 15,
                "avg_connections_per_session": 1.875,
            },
            "connection_lifecycle": {
                "avg_connection_age_seconds": 1800,
                "max_connection_age_seconds": 7200,
                "min_connection_age_seconds": 60,
                "connections_older_than_1h": 8,
                "connections_older_than_24h": 2,
            },
            "performance_metrics": {
                "total_websocket_connections": 8,
                "total_sse_connections": 7,
                "avg_connections_per_player": 1.5,
            },
            "timestamp": 1234567890.0,
        }

        # Mock performance stats
        manager.get_performance_stats.return_value = {
            "connection_establishment": {
                "total_connections": 15,
                "websocket_connections": 8,
                "sse_connections": 7,
                "avg_websocket_establishment_ms": 25.5,
                "avg_sse_establishment_ms": 18.2,
                "max_websocket_establishment_ms": 100.0,
                "max_sse_establishment_ms": 75.0,
                "min_websocket_establishment_ms": 10.0,
                "min_sse_establishment_ms": 5.0,
            },
            "message_delivery": {
                "total_messages": 1500,
                "avg_delivery_time_ms": 5.2,
                "max_delivery_time_ms": 50.0,
                "min_delivery_time_ms": 1.0,
            },
            "disconnections": {
                "total_disconnections": 5,
                "avg_disconnection_time_ms": 12.3,
                "max_disconnection_time_ms": 30.0,
                "min_disconnection_time_ms": 5.0,
            },
            "session_management": {
                "total_session_switches": 3,
                "avg_session_switch_time_ms": 200.0,
                "max_session_switch_time_ms": 500.0,
                "min_session_switch_time_ms": 100.0,
            },
            "health_monitoring": {
                "total_health_checks": 100,
                "avg_health_check_time_ms": 2.5,
                "max_health_check_time_ms": 10.0,
                "min_health_check_time_ms": 1.0,
            },
            "timestamp": 1234567890.0,
        }

        # Mock connection health stats
        manager.get_connection_health_stats.return_value = {
            "overall_health": {
                "total_connections": 15,
                "healthy_connections": 14,
                "unhealthy_connections": 1,
                "health_percentage": 93.3,
            },
            "connection_type_health": {
                "websocket_connections": 8,
                "sse_connections": 7,
                "websocket_health_percentage": 0,
                "sse_health_percentage": 0,
            },
            "connection_lifecycle": {
                "avg_connection_age_seconds": 1800,
                "max_connection_age_seconds": 7200,
                "min_connection_age_seconds": 60,
                "stale_connections": 8,
                "stale_connection_percentage": 53.3,
            },
            "session_health": {
                "total_sessions": 8,
                "healthy_sessions": 7,
                "unhealthy_sessions": 1,
                "session_health_percentage": 87.5,
                "avg_connections_per_session": 1.875,
            },
            "health_trends": {
                "connections_older_than_1h": 8,
                "connections_older_than_24h": 2,
                "connections_older_than_7d": 0,
            },
            "timestamp": 1234567890.0,
        }

        return manager

    @pytest.fixture
    def mock_conn_manager(self, mock_connection_manager):
        """Legacy alias for mock_connection_manager fixture."""
        return mock_connection_manager

    def test_get_dual_connection_stats_success(self, client, mock_connection_manager):
        """Test successful retrieval of dual connection statistics."""
        container = MagicMock()
        container.connection_manager = mock_connection_manager
        client.app.state.container = container
        mock_connection_manager.get_dual_connection_stats.return_value = (
            mock_connection_manager.get_dual_connection_stats()
        )

        response = client.get("/monitoring/dual-connections")

        assert response.status_code == 200
        data = response.json()

        # Check response structure
        assert "connection_distribution" in data
        assert "connection_health" in data
        assert "session_metrics" in data
        assert "connection_lifecycle" in data
        assert "performance_metrics" in data
        assert "timestamp" in data

        # Check specific values
        assert data["connection_distribution"]["total_players"] == 10
        assert data["connection_distribution"]["dual_connection_players"] == 3
        assert data["connection_distribution"]["dual_connection_percentage"] == 30.0
        assert data["connection_health"]["total_connections"] == 15
        assert data["connection_health"]["health_percentage"] == 93.3

    def test_get_dual_connection_stats_error(self, client):
        """Test error handling in dual connection statistics endpoint."""
        mock_conn_manager = MagicMock()
        mock_conn_manager.get_dual_connection_stats.side_effect = Exception("Database error")
        container = MagicMock()
        container.connection_manager = mock_conn_manager
        client.app.state.container = container

        response = client.get("/monitoring/dual-connections")

        assert response.status_code == 500
        data = response.json()
        assert "Error retrieving dual connection stats" in data["detail"]

    def test_get_performance_stats_success(self, client, mock_connection_manager):
        """Test successful retrieval of performance statistics."""
        container = MagicMock()
        container.connection_manager = mock_connection_manager
        client.app.state.container = container
        mock_connection_manager.get_performance_stats.return_value = mock_connection_manager.get_performance_stats()

        response = client.get("/monitoring/performance")

        assert response.status_code == 200
        data = response.json()

        # Check response structure
        assert "connection_establishment" in data
        assert "message_delivery" in data
        assert "disconnections" in data
        assert "session_management" in data
        assert "health_monitoring" in data
        assert "timestamp" in data

        # Check specific values
        assert data["connection_establishment"]["total_connections"] == 15
        assert data["connection_establishment"]["avg_websocket_establishment_ms"] == 25.5
        assert data["connection_establishment"]["avg_sse_establishment_ms"] == 18.2
        assert data["message_delivery"]["total_messages"] == 1500
        assert data["message_delivery"]["avg_delivery_time_ms"] == 5.2

    def test_get_performance_stats_error(self, client):
        """Test error handling in performance statistics endpoint."""
        mock_conn_manager = MagicMock()
        mock_conn_manager.get_performance_stats.side_effect = Exception("Performance data unavailable")
        container = MagicMock()
        container.connection_manager = mock_conn_manager
        client.app.state.container = container

        response = client.get("/monitoring/performance")

        assert response.status_code == 500
        data = response.json()
        assert "Error retrieving performance stats" in data["detail"]

    def test_get_connection_health_stats_success(self, client, mock_connection_manager):
        """Test successful retrieval of connection health statistics."""
        container = MagicMock()
        container.connection_manager = mock_connection_manager
        client.app.state.container = container
        mock_connection_manager.get_connection_health_stats.return_value = (
            mock_connection_manager.get_connection_health_stats()
        )

        response = client.get("/monitoring/connection-health")

        assert response.status_code == 200
        data = response.json()

        # Check response structure
        assert "overall_health" in data
        assert "connection_type_health" in data
        assert "connection_lifecycle" in data
        assert "session_health" in data
        assert "health_trends" in data
        assert "timestamp" in data

        # Check specific values
        assert data["overall_health"]["total_connections"] == 15
        assert data["overall_health"]["healthy_connections"] == 14
        assert data["overall_health"]["unhealthy_connections"] == 1
        assert data["overall_health"]["health_percentage"] == 93.3
        assert data["connection_lifecycle"]["stale_connections"] == 8
        assert data["session_health"]["session_health_percentage"] == 87.5

    def test_get_connection_health_stats_error(self, client):
        """Test error handling in connection health statistics endpoint."""
        mock_conn_manager = MagicMock()
        mock_conn_manager.get_connection_health_stats.side_effect = Exception("Health check failed")
        container = MagicMock()
        container.connection_manager = mock_conn_manager
        client.app.state.container = container

        response = client.get("/monitoring/connection-health")

        assert response.status_code == 500
        data = response.json()
        assert "Error retrieving connection health stats" in data["detail"]

    def test_monitoring_endpoints_content_type(self, client, mock_connection_manager):
        """Test that monitoring endpoints return proper content type."""
        container = MagicMock()
        container.connection_manager = mock_connection_manager
        client.app.state.container = container
        mock_connection_manager.get_dual_connection_stats.return_value = (
            mock_connection_manager.get_dual_connection_stats()
        )
        mock_connection_manager.get_performance_stats.return_value = mock_connection_manager.get_performance_stats()
        mock_connection_manager.get_connection_health_stats.return_value = (
            mock_connection_manager.get_connection_health_stats()
        )

        # Test all new endpoints
        endpoints = ["/monitoring/dual-connections", "/monitoring/performance", "/monitoring/connection-health"]

        for endpoint in endpoints:
            response = client.get(endpoint)
            assert response.status_code == 200
            assert response.headers["content-type"] == "application/json"

    def test_monitoring_endpoints_response_validation(self, client, mock_connection_manager):
        """Test that monitoring endpoints return valid response models."""
        container = MagicMock()
        container.connection_manager = mock_connection_manager
        client.app.state.container = container
        mock_connection_manager.get_dual_connection_stats.return_value = (
            mock_connection_manager.get_dual_connection_stats()
        )
        mock_connection_manager.get_performance_stats.return_value = mock_connection_manager.get_performance_stats()
        mock_connection_manager.get_connection_health_stats.return_value = (
            mock_connection_manager.get_connection_health_stats()
        )

        # Test dual connections endpoint
        response = client.get("/monitoring/dual-connections")
        assert response.status_code == 200
        data = response.json()

        # Validate required fields are present and have correct types
        assert isinstance(data["connection_distribution"], dict)
        assert isinstance(data["connection_health"], dict)
        assert isinstance(data["session_metrics"], dict)
        assert isinstance(data["connection_lifecycle"], dict)
        assert isinstance(data["performance_metrics"], dict)
        assert isinstance(data["timestamp"], int | float)

        # Test performance endpoint
        response = client.get("/monitoring/performance")
        assert response.status_code == 200
        data = response.json()

        assert isinstance(data["connection_establishment"], dict)
        assert isinstance(data["message_delivery"], dict)
        assert isinstance(data["disconnections"], dict)
        assert isinstance(data["session_management"], dict)
        assert isinstance(data["health_monitoring"], dict)
        assert isinstance(data["timestamp"], int | float)

        # Test connection health endpoint
        response = client.get("/monitoring/connection-health")
        assert response.status_code == 200
        data = response.json()

        assert isinstance(data["overall_health"], dict)
        assert isinstance(data["connection_type_health"], dict)
        assert isinstance(data["connection_lifecycle"], dict)
        assert isinstance(data["session_health"], dict)
        assert isinstance(data["health_trends"], dict)
        assert isinstance(data["timestamp"], int | float)

    def test_monitoring_endpoints_with_empty_data(self, mock_conn_manager, client):
        """Test monitoring endpoints with empty data."""
        # Mock empty responses
        mock_conn_manager.get_dual_connection_stats.return_value = {
            "connection_distribution": {
                "total_players": 0,
                "dual_connection_players": 0,
                "websocket_only_players": 0,
                "sse_only_players": 0,
                "dual_connection_percentage": 0,
            },
            "connection_health": {
                "total_connections": 0,
                "healthy_connections": 0,
                "unhealthy_connections": 0,
                "health_percentage": 0,
            },
            "session_metrics": {"total_sessions": 0, "total_session_connections": 0, "avg_connections_per_session": 0},
            "connection_lifecycle": {
                "avg_connection_age_seconds": 0,
                "max_connection_age_seconds": 0,
                "min_connection_age_seconds": 0,
                "connections_older_than_1h": 0,
                "connections_older_than_24h": 0,
            },
            "performance_metrics": {
                "total_websocket_connections": 0,
                "total_sse_connections": 0,
                "avg_connections_per_player": 0,
            },
            "timestamp": 0.0,
        }

        mock_conn_manager.get_performance_stats.return_value = {
            "connection_establishment": {
                "total_connections": 0,
                "websocket_connections": 0,
                "sse_connections": 0,
                "avg_websocket_establishment_ms": 0,
                "avg_sse_establishment_ms": 0,
                "max_websocket_establishment_ms": 0,
                "max_sse_establishment_ms": 0,
                "min_websocket_establishment_ms": 0,
                "min_sse_establishment_ms": 0,
            },
            "message_delivery": {
                "total_messages": 0,
                "avg_delivery_time_ms": 0,
                "max_delivery_time_ms": 0,
                "min_delivery_time_ms": 0,
            },
            "disconnections": {
                "total_disconnections": 0,
                "avg_disconnection_time_ms": 0,
                "max_disconnection_time_ms": 0,
                "min_disconnection_time_ms": 0,
            },
            "session_management": {
                "total_session_switches": 0,
                "avg_session_switch_time_ms": 0,
                "max_session_switch_time_ms": 0,
                "min_session_switch_time_ms": 0,
            },
            "health_monitoring": {
                "total_health_checks": 0,
                "avg_health_check_time_ms": 0,
                "max_health_check_time_ms": 0,
                "min_health_check_time_ms": 0,
            },
            "timestamp": 0.0,
        }

        mock_conn_manager.get_connection_health_stats.return_value = {
            "overall_health": {
                "total_connections": 0,
                "healthy_connections": 0,
                "unhealthy_connections": 0,
                "health_percentage": 0,
            },
            "connection_type_health": {
                "websocket_connections": 0,
                "sse_connections": 0,
                "websocket_health_percentage": 0,
                "sse_health_percentage": 0,
            },
            "connection_lifecycle": {
                "avg_connection_age_seconds": 0,
                "max_connection_age_seconds": 0,
                "min_connection_age_seconds": 0,
                "stale_connections": 0,
                "stale_connection_percentage": 0,
            },
            "session_health": {
                "total_sessions": 0,
                "healthy_sessions": 0,
                "unhealthy_sessions": 0,
                "session_health_percentage": 0,
                "avg_connections_per_session": 0,
            },
            "health_trends": {
                "connections_older_than_1h": 0,
                "connections_older_than_24h": 0,
                "connections_older_than_7d": 0,
            },
            "timestamp": 0.0,
        }

        container = MagicMock()
        container.connection_manager = mock_conn_manager
        client.app.state.container = container

        # Test all endpoints with empty data
        endpoints = ["/monitoring/dual-connections", "/monitoring/performance", "/monitoring/connection-health"]

        for endpoint in endpoints:
            response = client.get(endpoint)
            assert response.status_code == 200
            data = response.json()
            assert data is not None
            assert "timestamp" in data


# ============================================================================
# Tests merged from test_monitoring_api_legacy.py
# ============================================================================


"""
Tests for the monitoring API endpoints.

This module tests the monitoring API endpoints to ensure they
provide accurate metrics, validation, and alerting data.

As noted in the Pnakotic Manuscripts, comprehensive testing of
monitoring APIs is essential for maintaining oversight of our
eldritch systems.
"""


class TestMonitoringAPI:
    """Test the monitoring API endpoints."""

    def __init__(self) -> None:
        """Initialize test class attributes."""
        self.app: FastAPI | None = None
        self.client: TestClient | None = None

    def setup_method(self) -> None:
        """Set up test environment."""
        self.app = create_app()
        self.client = TestClient(self.app)
        reset_movement_monitor()

    def test_get_movement_metrics(self) -> None:
        """Test getting movement metrics."""
        assert self.client is not None
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

    def test_validate_room_integrity(self) -> None:
        """Test room integrity validation."""
        assert self.app is not None
        assert self.client is not None
        # Ensure persistence is set up for this test
        if not hasattr(self.app.state, "persistence") or self.app.state.persistence is None:
            mock_persistence = AsyncMock()
            mock_persistence.list_rooms = AsyncMock(return_value=[])
            self.app.state.persistence = mock_persistence

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

    def test_get_system_alerts(self) -> None:
        """Test getting system alerts."""
        assert self.client is not None
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

    def test_reset_metrics(self) -> None:
        """Test resetting metrics."""
        assert self.client is not None
        response = self.client.post("/monitoring/reset")

        assert response.status_code == 200
        data = response.json()

        assert "message" in data
        assert data["message"] == "Metrics reset successfully"

    def test_get_performance_summary(self) -> None:
        """Test getting performance summary."""
        assert self.client is not None
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

    def test_metrics_with_movements(self) -> None:
        """Test metrics after recording some movements."""
        assert self.client is not None
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

    def test_alerts_with_high_failure_rate(self) -> None:
        """Test alerts when failure rate is high."""
        assert self.client is not None
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

    def test_integrity_with_duplicate_player(self) -> None:
        """Test integrity validation with duplicate player."""
        assert self.app is not None
        assert self.client is not None
        from server.models.room import Room

        # Create rooms with duplicate player
        room1 = Room({"id": "room1", "name": "Room 1", "description": "First room", "exits": {}})
        room2 = Room({"id": "room2", "name": "Room 2", "description": "Second room", "exits": {}})

        # Add same player to both rooms (violation)
        room1.player_entered("player1")
        room2.player_entered("player1")

        # Mock persistence to return our test rooms
        # Set up persistence in app.state (replaces get_persistence)
        mock_persistence = AsyncMock()
        mock_persistence.list_rooms = AsyncMock(return_value=[room1, room2])
        self.app.state.persistence = mock_persistence

        response = self.client.get("/monitoring/integrity")

        assert response.status_code == 200
        data = response.json()

        assert data["valid"] is False
        assert len(data["violations"]) == 1
        assert "Player player1 found in multiple rooms" in data["violations"][0]

    def test_error_handling(self) -> None:
        """Test error handling in monitoring endpoints."""
        assert self.client is not None
        # Test with mocked error
        with patch("server.api.monitoring.get_movement_monitor") as mock_get_monitor:
            mock_get_monitor.side_effect = Exception("Test error")

            response = self.client.get("/monitoring/metrics")

            assert response.status_code == 500
            data = response.json()
            assert "error" in data
            assert "Error retrieving metrics" in data["error"]["message"]

    def test_performance_summary_formatting(self) -> None:
        """Test that performance summary formats values correctly."""
        assert self.client is not None
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

    def test_api_endpoints_consistency(self) -> None:
        """Test that all monitoring endpoints return consistent data."""
        assert self.client is not None
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
