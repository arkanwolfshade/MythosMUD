"""
Unit tests for health models.

Tests the health monitoring Pydantic models.
"""

import pytest
from pydantic import ValidationError

from server.models.health import (
    ConnectionsComponent,
    DatabaseComponent,
    HealthComponents,
    HealthErrorResponse,
    HealthResponse,
    HealthStatus,
    ServerComponent,
)

# --- Tests for HealthStatus enum ---


def test_health_status_enum_values():
    """Test HealthStatus enum contains expected values."""
    assert HealthStatus.HEALTHY.value == "healthy"
    assert HealthStatus.DEGRADED.value == "degraded"
    assert HealthStatus.UNHEALTHY.value == "unhealthy"


def test_health_status_enum_all_statuses():
    """Test HealthStatus enum contains all expected statuses."""
    expected_statuses = {"healthy", "degraded", "unhealthy"}
    actual_statuses = {s.value for s in HealthStatus}
    assert actual_statuses == expected_statuses


# --- Tests for ServerComponent model ---


def test_server_component_creation():
    """Test ServerComponent can be created with required fields."""
    component = ServerComponent(
        status=HealthStatus.HEALTHY,
        uptime_seconds=12345.67,
        memory_usage_mb=256.5,
        cpu_usage_percent=15.2,
    )

    assert component.status == HealthStatus.HEALTHY
    assert component.uptime_seconds == 12345.67
    assert component.memory_usage_mb == 256.5
    assert component.cpu_usage_percent == 15.2


def test_server_component_rejects_extra_fields():
    """Test ServerComponent rejects unknown fields (extra='forbid')."""
    with pytest.raises(ValidationError) as exc_info:
        # Reason: Intentionally testing Pydantic validation with extra='forbid' - extra fields should be rejected
        ServerComponent(  # type: ignore[call-arg]
            status=HealthStatus.HEALTHY,
            uptime_seconds=100.0,
            memory_usage_mb=100.0,
            cpu_usage_percent=10.0,
            unknown_field="value",
        )

    error_str = str(exc_info.value).lower()
    assert "extra" in error_str and ("not permitted" in error_str or "forbidden" in error_str)


def test_server_component_frozen():
    """Test ServerComponent is frozen (immutable)."""
    component = ServerComponent(
        status=HealthStatus.HEALTHY,
        uptime_seconds=100.0,
        memory_usage_mb=100.0,
        cpu_usage_percent=10.0,
    )

    with pytest.raises(ValidationError):
        # Reason: Testing frozen Pydantic model - assignment to read-only property raises ValidationError at runtime
        component.status = HealthStatus.DEGRADED  # type: ignore[misc]


# --- Tests for DatabaseComponent model ---


def test_database_component_creation():
    """Test DatabaseComponent can be created with required fields."""
    component = DatabaseComponent(
        status=HealthStatus.HEALTHY,
        connection_count=5,
        last_query_time_ms=12.5,
    )

    assert component.status == HealthStatus.HEALTHY
    assert component.connection_count == 5
    assert component.last_query_time_ms == 12.5


def test_database_component_without_last_query_time():
    """Test DatabaseComponent can have None for last_query_time_ms."""
    component = DatabaseComponent(
        status=HealthStatus.HEALTHY,
        connection_count=0,
        last_query_time_ms=None,
    )

    assert component.last_query_time_ms is None


def test_database_component_rejects_extra_fields():
    """Test DatabaseComponent rejects unknown fields."""
    with pytest.raises(ValidationError):
        # Reason: Intentionally testing Pydantic validation with extra='forbid' - extra fields should be rejected
        DatabaseComponent(  # type: ignore[call-arg]
            status=HealthStatus.HEALTHY,
            connection_count=5,
            last_query_time_ms=10.0,
            unknown_field="value",
        )


# --- Tests for ConnectionsComponent model ---


def test_connections_component_creation():
    """Test ConnectionsComponent can be created with required fields."""
    component = ConnectionsComponent(
        status=HealthStatus.HEALTHY,
        active_connections=3,
        max_connections=100,
        connection_rate_per_minute=45.2,
    )

    assert component.status == HealthStatus.HEALTHY
    assert component.active_connections == 3
    assert component.max_connections == 100
    assert component.connection_rate_per_minute == 45.2


def test_connections_component_rejects_extra_fields():
    """Test ConnectionsComponent rejects unknown fields."""
    with pytest.raises(ValidationError):
        # Reason: Intentionally testing Pydantic validation with extra='forbid' - extra fields should be rejected
        ConnectionsComponent(  # type: ignore[call-arg]
            status=HealthStatus.HEALTHY,
            active_connections=3,
            max_connections=100,
            connection_rate_per_minute=45.2,
            unknown_field="value",
        )


# --- Tests for HealthComponents model ---


def test_health_components_creation():
    """Test HealthComponents can be created with required fields."""
    server = ServerComponent(
        status=HealthStatus.HEALTHY,
        uptime_seconds=100.0,
        memory_usage_mb=100.0,
        cpu_usage_percent=10.0,
    )
    database = DatabaseComponent(
        status=HealthStatus.HEALTHY,
        connection_count=5,
        last_query_time_ms=10.0,
    )
    connections = ConnectionsComponent(
        status=HealthStatus.HEALTHY,
        active_connections=3,
        max_connections=100,
        connection_rate_per_minute=45.2,
    )

    components = HealthComponents(server=server, database=database, connections=connections)

    assert components.server == server
    assert components.database == database
    assert components.connections == connections


def test_health_components_rejects_extra_fields():
    """Test HealthComponents rejects unknown fields."""
    server = ServerComponent(
        status=HealthStatus.HEALTHY,
        uptime_seconds=100.0,
        memory_usage_mb=100.0,
        cpu_usage_percent=10.0,
    )
    database = DatabaseComponent(
        status=HealthStatus.HEALTHY,
        connection_count=5,
        last_query_time_ms=10.0,
    )
    connections = ConnectionsComponent(
        status=HealthStatus.HEALTHY,
        active_connections=3,
        max_connections=100,
        connection_rate_per_minute=45.2,
    )

    with pytest.raises(ValidationError):
        # Reason: Intentionally testing Pydantic validation with extra='forbid' - extra fields should be rejected
        HealthComponents(server=server, database=database, connections=connections, unknown_field="value")  # type: ignore[call-arg]


# --- Tests for HealthResponse model ---


def test_health_response_creation():
    """Test HealthResponse can be created with required fields."""
    server = ServerComponent(
        status=HealthStatus.HEALTHY,
        uptime_seconds=100.0,
        memory_usage_mb=100.0,
        cpu_usage_percent=10.0,
    )
    database = DatabaseComponent(
        status=HealthStatus.HEALTHY,
        connection_count=5,
        last_query_time_ms=10.0,
    )
    connections = ConnectionsComponent(
        status=HealthStatus.HEALTHY,
        active_connections=3,
        max_connections=100,
        connection_rate_per_minute=45.2,
    )
    components = HealthComponents(server=server, database=database, connections=connections)

    response = HealthResponse(
        status=HealthStatus.HEALTHY,
        timestamp="2025-08-27T15:30:45.123456Z",
        uptime_seconds=12345.67,
        version="0.1.0",
        components=components,
        alerts=[],
    )

    assert response.status == HealthStatus.HEALTHY
    assert response.timestamp == "2025-08-27T15:30:45.123456Z"
    assert response.uptime_seconds == 12345.67
    assert response.version == "0.1.0"
    assert response.components == components
    assert response.alerts == []


def test_health_response_with_alerts():
    """Test HealthResponse can have alerts."""
    server = ServerComponent(
        status=HealthStatus.HEALTHY,
        uptime_seconds=100.0,
        memory_usage_mb=100.0,
        cpu_usage_percent=10.0,
    )
    database = DatabaseComponent(
        status=HealthStatus.HEALTHY,
        connection_count=5,
        last_query_time_ms=10.0,
    )
    connections = ConnectionsComponent(
        status=HealthStatus.HEALTHY,
        active_connections=3,
        max_connections=100,
        connection_rate_per_minute=45.2,
    )
    components = HealthComponents(server=server, database=database, connections=connections)

    response = HealthResponse(
        status=HealthStatus.DEGRADED,
        timestamp="2025-08-27T15:30:45.123456Z",
        uptime_seconds=12345.67,
        version="0.1.0",
        components=components,
        alerts=["High memory usage", "Slow database queries"],
    )

    assert len(response.alerts) == 2
    assert "High memory usage" in response.alerts
    assert "Slow database queries" in response.alerts


def test_health_response_default_alerts():
    """Test HealthResponse defaults alerts to empty list."""
    server = ServerComponent(
        status=HealthStatus.HEALTHY,
        uptime_seconds=100.0,
        memory_usage_mb=100.0,
        cpu_usage_percent=10.0,
    )
    database = DatabaseComponent(
        status=HealthStatus.HEALTHY,
        connection_count=5,
        last_query_time_ms=10.0,
    )
    connections = ConnectionsComponent(
        status=HealthStatus.HEALTHY,
        active_connections=3,
        max_connections=100,
        connection_rate_per_minute=45.2,
    )
    components = HealthComponents(server=server, database=database, connections=connections)

    response = HealthResponse(
        status=HealthStatus.HEALTHY,
        timestamp="2025-08-27T15:30:45.123456Z",
        uptime_seconds=12345.67,
        version="0.1.0",
        components=components,
    )

    assert response.alerts == []


# --- Tests for HealthErrorResponse model ---


def test_health_error_response_creation():
    """Test HealthErrorResponse can be created with required fields."""
    response = HealthErrorResponse(
        error="Database connection failed",
        detail="Unable to connect to PostgreSQL database",
        timestamp="2025-08-27T15:30:45.123456Z",
    )

    assert response.error == "Database connection failed"
    assert response.detail == "Unable to connect to PostgreSQL database"
    assert response.timestamp == "2025-08-27T15:30:45.123456Z"


def test_health_error_response_rejects_extra_fields():
    """Test HealthErrorResponse rejects unknown fields."""
    with pytest.raises(ValidationError):
        # Reason: Intentionally testing Pydantic validation with extra='forbid' - extra fields should be rejected
        HealthErrorResponse(  # type: ignore[call-arg]
            error="Test error",
            detail="Test detail",
            timestamp="2025-08-27T15:30:45.123456Z",
            unknown_field="value",
        )


def test_health_error_response_frozen():
    """Test HealthErrorResponse is frozen (immutable)."""
    response = HealthErrorResponse(
        error="Test error",
        detail="Test detail",
        timestamp="2025-08-27T15:30:45.123456Z",
    )

    with pytest.raises(ValidationError):
        # Reason: Testing frozen Pydantic model - assignment to read-only property raises ValidationError at runtime
        response.error = "Modified error"  # type: ignore[misc]
