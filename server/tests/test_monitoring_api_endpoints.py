"""
Tests for monitoring API endpoints with dual connection support.

This module tests the new monitoring API endpoints that provide dual connection
statistics, performance metrics, and connection health information.
"""

from unittest.mock import Mock, patch

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from server.api.monitoring import router


class TestMonitoringAPIEndpoints:
    """Test monitoring API endpoints."""

    @pytest.fixture
    def app(self):
        """Create a FastAPI app with monitoring router."""
        app = FastAPI()
        app.include_router(router)
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

    @patch("server.api.monitoring.connection_manager")
    def test_get_dual_connection_stats_success(self, mock_conn_manager, client, mock_connection_manager):
        """Test successful retrieval of dual connection statistics."""
        mock_conn_manager.get_dual_connection_stats.return_value = mock_connection_manager.get_dual_connection_stats()

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

    @patch("server.api.monitoring.connection_manager")
    def test_get_dual_connection_stats_error(self, mock_conn_manager, client):
        """Test error handling in dual connection statistics endpoint."""
        mock_conn_manager.get_dual_connection_stats.side_effect = Exception("Database error")

        response = client.get("/monitoring/dual-connections")

        assert response.status_code == 500
        data = response.json()
        assert "Error retrieving dual connection stats" in data["detail"]

    @patch("server.api.monitoring.connection_manager")
    def test_get_performance_stats_success(self, mock_conn_manager, client, mock_connection_manager):
        """Test successful retrieval of performance statistics."""
        mock_conn_manager.get_performance_stats.return_value = mock_connection_manager.get_performance_stats()

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

    @patch("server.api.monitoring.connection_manager")
    def test_get_performance_stats_error(self, mock_conn_manager, client):
        """Test error handling in performance statistics endpoint."""
        mock_conn_manager.get_performance_stats.side_effect = Exception("Performance data unavailable")

        response = client.get("/monitoring/performance")

        assert response.status_code == 500
        data = response.json()
        assert "Error retrieving performance stats" in data["detail"]

    @patch("server.api.monitoring.connection_manager")
    def test_get_connection_health_stats_success(self, mock_conn_manager, client, mock_connection_manager):
        """Test successful retrieval of connection health statistics."""
        mock_conn_manager.get_connection_health_stats.return_value = (
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

    @patch("server.api.monitoring.connection_manager")
    def test_get_connection_health_stats_error(self, mock_conn_manager, client):
        """Test error handling in connection health statistics endpoint."""
        mock_conn_manager.get_connection_health_stats.side_effect = Exception("Health check failed")

        response = client.get("/monitoring/connection-health")

        assert response.status_code == 500
        data = response.json()
        assert "Error retrieving connection health stats" in data["detail"]

    @patch("server.api.monitoring.connection_manager")
    def test_monitoring_endpoints_content_type(self, mock_conn_manager, client, mock_connection_manager):
        """Test that monitoring endpoints return proper content type."""
        mock_conn_manager.get_dual_connection_stats.return_value = mock_connection_manager.get_dual_connection_stats()
        mock_conn_manager.get_performance_stats.return_value = mock_connection_manager.get_performance_stats()
        mock_conn_manager.get_connection_health_stats.return_value = (
            mock_connection_manager.get_connection_health_stats()
        )

        # Test all new endpoints
        endpoints = ["/monitoring/dual-connections", "/monitoring/performance", "/monitoring/connection-health"]

        for endpoint in endpoints:
            response = client.get(endpoint)
            assert response.status_code == 200
            assert response.headers["content-type"] == "application/json"

    @patch("server.api.monitoring.connection_manager")
    def test_monitoring_endpoints_response_validation(self, mock_conn_manager, client, mock_connection_manager):
        """Test that monitoring endpoints return valid response models."""
        mock_conn_manager.get_dual_connection_stats.return_value = mock_connection_manager.get_dual_connection_stats()
        mock_conn_manager.get_performance_stats.return_value = mock_connection_manager.get_performance_stats()
        mock_conn_manager.get_connection_health_stats.return_value = (
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
        assert isinstance(data["timestamp"], (int, float))

        # Test performance endpoint
        response = client.get("/monitoring/performance")
        assert response.status_code == 200
        data = response.json()

        assert isinstance(data["connection_establishment"], dict)
        assert isinstance(data["message_delivery"], dict)
        assert isinstance(data["disconnections"], dict)
        assert isinstance(data["session_management"], dict)
        assert isinstance(data["health_monitoring"], dict)
        assert isinstance(data["timestamp"], (int, float))

        # Test connection health endpoint
        response = client.get("/monitoring/connection-health")
        assert response.status_code == 200
        data = response.json()

        assert isinstance(data["overall_health"], dict)
        assert isinstance(data["connection_type_health"], dict)
        assert isinstance(data["connection_lifecycle"], dict)
        assert isinstance(data["session_health"], dict)
        assert isinstance(data["health_trends"], dict)
        assert isinstance(data["timestamp"], (int, float))

    @patch("server.api.monitoring.connection_manager")
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

        # Test all endpoints with empty data
        endpoints = ["/monitoring/dual-connections", "/monitoring/performance", "/monitoring/connection-health"]

        for endpoint in endpoints:
            response = client.get(endpoint)
            assert response.status_code == 200
            data = response.json()
            assert data is not None
            assert "timestamp" in data
