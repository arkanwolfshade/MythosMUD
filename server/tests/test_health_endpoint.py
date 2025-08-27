"""
Tests for the health endpoint.

This module tests the health endpoint functionality to ensure
it returns proper health status and handles errors correctly.
"""

import pytest
from fastapi.testclient import TestClient

from ..app.factory import create_app


@pytest.fixture
def client():
    """Create a test client for the FastAPI application."""
    app = create_app()
    return TestClient(app)


class TestHealthEndpoint:
    """Test cases for the health endpoint."""

    def test_health_endpoint_returns_200_when_healthy(self, client):
        """Test that health endpoint returns 200 when system is healthy."""
        response = client.get("/monitoring/health")

        assert response.status_code == 200
        data = response.json()

        # Verify response structure
        assert "status" in data
        assert "timestamp" in data
        assert "uptime_seconds" in data
        assert "version" in data
        assert "components" in data
        assert "alerts" in data

        # Verify components structure
        components = data["components"]
        assert "server" in components
        assert "database" in components
        assert "connections" in components

        # Verify server component
        server = components["server"]
        assert "status" in server
        assert "uptime_seconds" in server
        assert "memory_usage_mb" in server
        assert "cpu_usage_percent" in server

        # Verify database component
        database = components["database"]
        assert "status" in database
        assert "connection_count" in database
        assert "last_query_time_ms" in database

        # Verify connections component
        connections = components["connections"]
        assert "status" in connections
        assert "active_connections" in connections
        assert "max_connections" in connections
        assert "connection_rate_per_minute" in connections

    def test_health_endpoint_content_type(self, client):
        """Test that health endpoint returns correct content type."""
        response = client.get("/monitoring/health")

        assert response.status_code == 200
        assert response.headers["content-type"] == "application/json"

    def test_health_endpoint_health_status_values(self, client):
        """Test that health status values are valid."""
        response = client.get("/monitoring/health")

        assert response.status_code == 200
        data = response.json()

        # Check that status is one of the valid values
        assert data["status"] in ["healthy", "degraded", "unhealthy"]

        # Check component statuses
        components = data["components"]
        for _component_name, component in components.items():
            assert component["status"] in ["healthy", "degraded", "unhealthy"]

    def test_health_endpoint_numeric_values(self, client):
        """Test that numeric values in response are valid."""
        response = client.get("/monitoring/health")

        assert response.status_code == 200
        data = response.json()

        # Check uptime is positive
        assert data["uptime_seconds"] >= 0

        # Check server component numeric values
        server = data["components"]["server"]
        assert server["uptime_seconds"] >= 0
        assert server["memory_usage_mb"] >= 0
        assert server["cpu_usage_percent"] >= 0

        # Check database component numeric values
        database = data["components"]["database"]
        assert database["connection_count"] >= 0
        assert database["last_query_time_ms"] is None or database["last_query_time_ms"] >= 0

        # Check connections component numeric values
        connections = data["components"]["connections"]
        assert connections["active_connections"] >= 0
        assert connections["max_connections"] > 0
        assert connections["connection_rate_per_minute"] >= 0

    def test_health_endpoint_timestamp_format(self, client):
        """Test that timestamp is in ISO format."""
        response = client.get("/monitoring/health")

        assert response.status_code == 200
        data = response.json()

        # Check timestamp format (should be ISO 8601)
        timestamp = data["timestamp"]
        assert "T" in timestamp  # ISO format separator
        assert "+" in timestamp or "Z" in timestamp  # Timezone indicator

    def test_health_endpoint_version_present(self, client):
        """Test that version field is present and not empty."""
        response = client.get("/monitoring/health")

        assert response.status_code == 200
        data = response.json()

        assert "version" in data
        assert data["version"] != ""
        assert data["version"] is not None

    def test_health_endpoint_alerts_is_list(self, client):
        """Test that alerts field is a list."""
        response = client.get("/monitoring/health")

        assert response.status_code == 200
        data = response.json()

        assert isinstance(data["alerts"], list)
