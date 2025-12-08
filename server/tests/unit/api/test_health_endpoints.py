"""
Tests for the health endpoint.

This module tests the health endpoint functionality to ensure
it returns proper health status and handles errors correctly.

As noted in the Pnakotic Manuscripts, proper testing of our monitoring
systems is essential for maintaining oversight of our eldritch infrastructure.
"""

from unittest.mock import Mock, patch

import pytest
from fastapi.testclient import TestClient

from server.app.factory import create_app
from server.models.health import (
    ConnectionsComponent,
    DatabaseComponent,
    HealthComponents,
    HealthResponse,
    HealthStatus,
    ServerComponent,
)


@pytest.fixture
def client():
    """Create a test client for the FastAPI application."""

    app = create_app()

    # Ensure container and connection_manager are set up for health endpoint
    if not hasattr(app.state, "container") or app.state.container is None:
        from server.container import ApplicationContainer

        app.state.container = ApplicationContainer.get_instance()

    # Ensure connection_manager exists
    if hasattr(app.state.container, "connection_manager") and app.state.container.connection_manager is None:
        from server.realtime.connection_manager import ConnectionManager

        app.state.container.connection_manager = ConnectionManager()
    elif not hasattr(app.state.container, "connection_manager"):
        from server.realtime.connection_manager import ConnectionManager

        app.state.container.connection_manager = ConnectionManager()

    return TestClient(app)


@pytest.fixture
def mock_health_response():
    """Create a mock health response for testing."""
    return HealthResponse(
        status=HealthStatus.HEALTHY,
        timestamp="2025-01-27T12:00:00.000000Z",
        uptime_seconds=3600.0,
        version="0.1.0",
        components=HealthComponents(
            server=ServerComponent(
                status=HealthStatus.HEALTHY, uptime_seconds=3600.0, memory_usage_mb=256.5, cpu_usage_percent=15.2
            ),
            database=DatabaseComponent(status=HealthStatus.HEALTHY, connection_count=5, last_query_time_ms=12.5),
            connections=ConnectionsComponent(
                status=HealthStatus.HEALTHY, active_connections=3, max_connections=100, connection_rate_per_minute=45.2
            ),
        ),
        alerts=[],
    )


class TestHealthEndpoint:
    """Test cases for the health endpoint."""

    @patch("server.api.monitoring.get_health_service")
    def test_health_endpoint_healthy_status_returns_200(self, mock_get_health_service, client, mock_health_response):
        """Test that health endpoint returns 200 when system is healthy."""
        # Mock the health service to return healthy status
        mock_health_service = Mock()
        mock_health_service.get_health_status.return_value = mock_health_response
        mock_get_health_service.return_value = mock_health_service

        response = client.get("/monitoring/health")

        assert response.status_code == 200
        data = response.json()

        # Verify response structure matches HealthResponse model
        assert data["status"] == "healthy"
        assert data["timestamp"] == "2025-01-27T12:00:00.000000Z"
        assert data["uptime_seconds"] == 3600.0
        assert data["version"] == "0.1.0"
        assert data["alerts"] == []

        # Verify components structure
        components = data["components"]
        assert "server" in components
        assert "database" in components
        assert "connections" in components

        # Verify server component
        server = components["server"]
        assert server["status"] == "healthy"
        assert server["uptime_seconds"] == 3600.0
        assert server["memory_usage_mb"] == 256.5
        assert server["cpu_usage_percent"] == 15.2

        # Verify database component
        database = components["database"]
        assert database["status"] == "healthy"
        assert database["connection_count"] == 5
        assert database["last_query_time_ms"] == 12.5

        # Verify connections component
        connections = components["connections"]
        assert connections["status"] == "healthy"
        assert connections["active_connections"] == 3
        assert connections["max_connections"] == 100
        assert connections["connection_rate_per_minute"] == 45.2

    @patch("server.api.monitoring.get_health_service")
    def test_health_endpoint_degraded_status_returns_200(self, mock_get_health_service, client):
        """Test that health endpoint returns 200 when system is degraded."""
        # Create degraded health response
        degraded_response = HealthResponse(
            status=HealthStatus.DEGRADED,
            timestamp="2025-01-27T12:00:00.000000Z",
            uptime_seconds=3600.0,
            version="0.1.0",
            components=HealthComponents(
                server=ServerComponent(
                    status=HealthStatus.DEGRADED,
                    uptime_seconds=3600.0,
                    memory_usage_mb=900.0,  # High memory usage
                    cpu_usage_percent=15.2,
                ),
                database=DatabaseComponent(status=HealthStatus.HEALTHY, connection_count=5, last_query_time_ms=12.5),
                connections=ConnectionsComponent(
                    status=HealthStatus.HEALTHY,
                    active_connections=3,
                    max_connections=100,
                    connection_rate_per_minute=45.2,
                ),
            ),
            alerts=["High memory usage detected"],
        )

        # Mock the health service to return degraded status
        mock_health_service = Mock()
        mock_health_service.get_health_status.return_value = degraded_response
        mock_get_health_service.return_value = mock_health_service

        response = client.get("/monitoring/health")

        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "degraded"
        assert "High memory usage detected" in data["alerts"]

    @patch("server.api.monitoring.get_health_service")
    def test_health_endpoint_unhealthy_status_returns_503(self, mock_get_health_service, client):
        """Test that health endpoint returns 503 when system is unhealthy."""
        # Create unhealthy health response
        unhealthy_response = HealthResponse(
            status=HealthStatus.UNHEALTHY,
            timestamp="2025-01-27T12:00:00.000000Z",
            uptime_seconds=3600.0,
            version="0.1.0",
            components=HealthComponents(
                server=ServerComponent(
                    status=HealthStatus.UNHEALTHY,
                    uptime_seconds=3600.0,
                    memory_usage_mb=1500.0,  # Critical memory usage
                    cpu_usage_percent=95.0,  # Critical CPU usage
                ),
                database=DatabaseComponent(status=HealthStatus.UNHEALTHY, connection_count=0, last_query_time_ms=None),
                connections=ConnectionsComponent(
                    status=HealthStatus.HEALTHY,
                    active_connections=3,
                    max_connections=100,
                    connection_rate_per_minute=45.2,
                ),
            ),
            alerts=["Critical memory usage", "Database connection failed"],
        )

        # Mock the health service to return unhealthy status
        mock_health_service = Mock()
        mock_health_service.get_health_status.return_value = unhealthy_response
        mock_get_health_service.return_value = mock_health_service

        response = client.get("/monitoring/health")

        assert response.status_code == 503
        data = response.json()
        assert data["status"] == "unhealthy"
        assert "Critical memory usage" in data["alerts"]
        assert "Database connection failed" in data["alerts"]

    @patch("server.api.monitoring.get_health_service")
    def test_health_endpoint_service_exception_returns_500(self, mock_get_health_service, client):
        """Test that health endpoint returns 500 when health service fails."""
        # Mock the health service to raise an exception
        mock_health_service = Mock()
        mock_health_service.get_health_status.side_effect = Exception("Health check failed")
        mock_get_health_service.return_value = mock_health_service

        response = client.get("/monitoring/health")

        assert response.status_code == 500
        data = response.json()

        # Check the standardized error response format
        assert "error" in data
        error = data["error"]
        assert error["type"] == "internal_error"
        assert "Health check failed" in error["message"]
        assert "timestamp" in error
        assert "severity" in error

    def test_health_endpoint_content_type(self, client):
        """Test that health endpoint returns correct content type."""
        with patch("server.api.monitoring.get_health_service") as mock_get_health_service:
            # Mock a healthy response
            mock_health_service = Mock()
            mock_health_service.get_health_status.return_value = HealthResponse(
                status=HealthStatus.HEALTHY,
                timestamp="2025-01-27T12:00:00.000000Z",
                uptime_seconds=3600.0,
                version="0.1.0",
                components=HealthComponents(
                    server=ServerComponent(
                        status=HealthStatus.HEALTHY,
                        uptime_seconds=3600.0,
                        memory_usage_mb=256.5,
                        cpu_usage_percent=15.2,
                    ),
                    database=DatabaseComponent(
                        status=HealthStatus.HEALTHY, connection_count=5, last_query_time_ms=12.5
                    ),
                    connections=ConnectionsComponent(
                        status=HealthStatus.HEALTHY,
                        active_connections=3,
                        max_connections=100,
                        connection_rate_per_minute=45.2,
                    ),
                ),
                alerts=[],
            )
            mock_get_health_service.return_value = mock_health_service

            response = client.get("/monitoring/health")

            assert response.status_code == 200
            assert response.headers["content-type"] == "application/json"

    @patch("server.api.monitoring.get_health_service")
    def test_health_endpoint_health_status_values(self, mock_get_health_service, client, mock_health_response):
        """Test that health status values are valid."""
        mock_health_service = Mock()
        mock_health_service.get_health_status.return_value = mock_health_response
        mock_get_health_service.return_value = mock_health_service

        response = client.get("/monitoring/health")

        assert response.status_code == 200
        data = response.json()

        # Check that status is one of the valid values
        assert data["status"] in ["healthy", "degraded", "unhealthy"]

        # Check component statuses
        components = data["components"]
        for _component_name, component in components.items():
            assert component["status"] in ["healthy", "degraded", "unhealthy"]

    @patch("server.api.monitoring.get_health_service")
    def test_health_endpoint_numeric_values(self, mock_get_health_service, client, mock_health_response):
        """Test that numeric values in response are valid."""
        mock_health_service = Mock()
        mock_health_service.get_health_status.return_value = mock_health_response
        mock_get_health_service.return_value = mock_health_service

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

    @patch("server.api.monitoring.get_health_service")
    def test_health_endpoint_timestamp_format(self, mock_get_health_service, client, mock_health_response):
        """Test that timestamp is in ISO format."""
        mock_health_service = Mock()
        mock_health_service.get_health_status.return_value = mock_health_response
        mock_get_health_service.return_value = mock_health_service

        response = client.get("/monitoring/health")

        assert response.status_code == 200
        data = response.json()

        # Check timestamp format (should be ISO 8601)
        timestamp = data["timestamp"]
        assert "T" in timestamp  # ISO format separator
        assert "+" in timestamp or "Z" in timestamp  # Timezone indicator

    @patch("server.api.monitoring.get_health_service")
    def test_health_endpoint_version_present(self, mock_get_health_service, client, mock_health_response):
        """Test that version field is present and not empty."""
        mock_health_service = Mock()
        mock_health_service.get_health_status.return_value = mock_health_response
        mock_get_health_service.return_value = mock_health_service

        response = client.get("/monitoring/health")

        assert response.status_code == 200
        data = response.json()

        assert "version" in data
        assert data["version"] != ""
        assert data["version"] is not None

    @patch("server.api.monitoring.get_health_service")
    def test_health_endpoint_alerts_is_list(self, mock_get_health_service, client, mock_health_response):
        """Test that alerts field is a list."""
        mock_health_service = Mock()
        mock_health_service.get_health_status.return_value = mock_health_response
        mock_get_health_service.return_value = mock_health_service

        response = client.get("/monitoring/health")

        assert response.status_code == 200
        data = response.json()

        assert isinstance(data["alerts"], list)
