"""
Tests for health models.

This module tests the health model functionality to ensure
proper serialization, deserialization, and configuration behavior.
"""

import pytest
from pydantic import ValidationError

from ..models.health import (
    ConnectionsComponent,
    DatabaseComponent,
    HealthComponents,
    HealthResponse,
    HealthStatus,
    ServerComponent,
)


class TestHealthModels:
    """Test cases for health models."""

    def test_health_response_model_creation(self):
        """Test that HealthResponse model can be created with valid data."""
        # Create component data
        server_component = ServerComponent(
            status=HealthStatus.HEALTHY,
            uptime_seconds=12345.67,
            memory_usage_mb=256.5,
            cpu_usage_percent=15.2,
        )

        database_component = DatabaseComponent(
            status=HealthStatus.HEALTHY,
            connection_count=5,
            last_query_time_ms=12.5,
        )

        connections_component = ConnectionsComponent(
            status=HealthStatus.HEALTHY,
            active_connections=3,
            max_connections=100,
            connection_rate_per_minute=45.2,
        )

        components = HealthComponents(
            server=server_component,
            database=database_component,
            connections=connections_component,
        )

        # Create health response
        health_response = HealthResponse(
            status=HealthStatus.HEALTHY,
            timestamp="2025-08-27T15:30:45.123456Z",
            uptime_seconds=12345.67,
            version="0.1.0",
            components=components,
            alerts=[],
        )

        assert health_response.status == HealthStatus.HEALTHY
        assert health_response.timestamp == "2025-08-27T15:30:45.123456Z"
        assert health_response.uptime_seconds == 12345.67
        assert health_response.version == "0.1.0"
        assert health_response.alerts == []

    def test_health_response_model_serialization(self):
        """Test that HealthResponse model serializes correctly."""
        # Create minimal valid health response
        server_component = ServerComponent(
            status=HealthStatus.HEALTHY,
            uptime_seconds=100.0,
            memory_usage_mb=128.0,
            cpu_usage_percent=10.0,
        )

        database_component = DatabaseComponent(
            status=HealthStatus.HEALTHY,
            connection_count=1,
            last_query_time_ms=None,
        )

        connections_component = ConnectionsComponent(
            status=HealthStatus.HEALTHY,
            active_connections=0,
            max_connections=50,
            connection_rate_per_minute=0.0,
        )

        components = HealthComponents(
            server=server_component,
            database=database_component,
            connections=connections_component,
        )

        health_response = HealthResponse(
            status=HealthStatus.HEALTHY,
            timestamp="2025-08-27T15:30:45.123456Z",
            uptime_seconds=100.0,
            version="0.1.0",
            components=components,
        )

        # Serialize to dict
        data = health_response.model_dump()

        # Verify all required fields are present
        assert "status" in data
        assert "timestamp" in data
        assert "uptime_seconds" in data
        assert "version" in data
        assert "components" in data
        assert "alerts" in data

        # Verify data types
        assert data["status"] == "healthy"
        assert data["timestamp"] == "2025-08-27T15:30:45.123456Z"
        assert data["uptime_seconds"] == 100.0
        assert data["version"] == "0.1.0"
        assert data["alerts"] == []

    def test_health_response_model_json_schema(self):
        """Test that HealthResponse model has proper JSON schema configuration."""
        # Verify that the model has json_schema_extra configuration
        schema = HealthResponse.model_json_schema()

        # Check that the example is present in the schema
        assert "example" in schema

        # Verify example structure matches expected format
        example = schema["example"]
        assert "status" in example
        assert "timestamp" in example
        assert "uptime_seconds" in example
        assert "version" in example
        assert "components" in example
        assert "alerts" in example

        # Verify example data types
        assert example["status"] == "healthy"
        assert example["timestamp"] == "2025-08-27T15:30:45.123456Z"
        assert example["uptime_seconds"] == 12345.67
        assert example["version"] == "0.1.0"
        assert example["alerts"] == []

    def test_health_response_model_validation(self):
        """Test that HealthResponse model validates input correctly."""
        # Test with invalid status
        with pytest.raises(ValidationError):
            HealthResponse(
                status="invalid_status",  # Invalid status
                timestamp="2025-08-27T15:30:45.123456Z",
                uptime_seconds=100.0,
                version="0.1.0",
                components=HealthComponents(
                    server=ServerComponent(
                        status=HealthStatus.HEALTHY,
                        uptime_seconds=100.0,
                        memory_usage_mb=128.0,
                        cpu_usage_percent=10.0,
                    ),
                    database=DatabaseComponent(
                        status=HealthStatus.HEALTHY,
                        connection_count=1,
                        last_query_time_ms=None,
                    ),
                    connections=ConnectionsComponent(
                        status=HealthStatus.HEALTHY,
                        active_connections=0,
                        max_connections=50,
                        connection_rate_per_minute=0.0,
                    ),
                ),
            )

    def test_health_response_model_default_alerts(self):
        """Test that HealthResponse model has default empty alerts list."""
        # Create health response without specifying alerts
        server_component = ServerComponent(
            status=HealthStatus.HEALTHY,
            uptime_seconds=100.0,
            memory_usage_mb=128.0,
            cpu_usage_percent=10.0,
        )

        database_component = DatabaseComponent(
            status=HealthStatus.HEALTHY,
            connection_count=1,
            last_query_time_ms=None,
        )

        connections_component = ConnectionsComponent(
            status=HealthStatus.HEALTHY,
            active_connections=0,
            max_connections=50,
            connection_rate_per_minute=0.0,
        )

        components = HealthComponents(
            server=server_component,
            database=database_component,
            connections=connections_component,
        )

        health_response = HealthResponse(
            status=HealthStatus.HEALTHY,
            timestamp="2025-08-27T15:30:45.123456Z",
            uptime_seconds=100.0,
            version="0.1.0",
            components=components,
            # alerts not specified, should default to empty list
        )

        assert health_response.alerts == []
