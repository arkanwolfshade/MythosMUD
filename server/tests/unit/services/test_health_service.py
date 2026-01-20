"""
Unit tests for health service.

Tests the health monitoring service for system health checks.
"""

import time
from unittest.mock import MagicMock, patch

import pytest

from server.models.health import HealthStatus
from server.services.health_service import HealthService, get_health_service


@pytest.fixture
def mock_connection_manager():
    """Create a mock connection manager."""
    manager = MagicMock()
    manager.get_memory_stats.return_value = {
        "connections": {
            "active_connections": 5,
            "max_connections": 100,
            "connection_rate_per_minute": 2.5,
        }
    }
    return manager


@pytest.fixture
def health_service(mock_connection_manager):
    """Create a HealthService instance."""
    return HealthService(connection_manager=mock_connection_manager)


def test_health_service_initialization(health_service):
    """Test HealthService initialization."""
    assert health_service.start_time > 0
    assert health_service.last_health_check is None
    assert health_service.health_check_count == 0
    assert health_service.memory_threshold_mb == 1024
    assert health_service.cpu_threshold_percent == 80.0


def test_get_server_uptime(health_service):
    """Test get_server_uptime returns positive value."""
    uptime = health_service.get_server_uptime()
    assert uptime >= 0
    # Wait a bit and verify uptime increases
    time.sleep(0.1)
    new_uptime = health_service.get_server_uptime()
    assert new_uptime > uptime


@patch("server.services.health_service.psutil.Process")
def test_get_memory_usage_success(mock_process, health_service):
    """Test get_memory_usage returns memory usage."""
    mock_memory_info = MagicMock()
    mock_memory_info.rss = 512 * 1024 * 1024  # 512 MB
    mock_process_instance = MagicMock()
    mock_process_instance.memory_info.return_value = mock_memory_info
    mock_process.return_value = mock_process_instance

    memory_usage = health_service.get_memory_usage()
    assert memory_usage == 512.0


@patch("server.services.health_service.psutil.Process")
def test_get_memory_usage_error(mock_process, health_service):
    """Test get_memory_usage handles errors gracefully."""
    mock_process.side_effect = Exception("Process error")
    memory_usage = health_service.get_memory_usage()
    assert memory_usage == 0.0


@patch("server.services.health_service.psutil.cpu_percent")
def test_get_cpu_usage_success(mock_cpu_percent, health_service):
    """Test get_cpu_usage returns CPU usage."""
    mock_cpu_percent.return_value = 45.5
    cpu_usage = health_service.get_cpu_usage()
    assert cpu_usage == 45.5


@patch("server.services.health_service.psutil.cpu_percent")
def test_get_cpu_usage_error(mock_cpu_percent, health_service):
    """Test get_cpu_usage handles errors gracefully."""
    mock_cpu_percent.side_effect = Exception("CPU error")
    cpu_usage = health_service.get_cpu_usage()
    assert cpu_usage == 0.0


@patch("server.container.ApplicationContainer")
def test_check_database_health_healthy(mock_container_class, health_service):
    """Test check_database_health returns healthy status."""
    mock_container = MagicMock()
    # Mock async_persistence with a pool that has size > 0
    mock_pool = MagicMock()
    mock_pool._size = 5  # Pool size > 0
    mock_async_persistence = MagicMock()
    mock_async_persistence._pool = mock_pool
    mock_container.async_persistence = mock_async_persistence
    mock_container_class.get_instance.return_value = mock_container

    with patch("time.time", side_effect=[0, 0.05]):  # 50ms query time (< 100ms = healthy)
        result = health_service.check_database_health()
        assert result["status"] == HealthStatus.HEALTHY
        assert result["connection_count"] == 5
        assert result["last_query_time_ms"] == 50.0


@patch("server.container.ApplicationContainer")
def test_check_database_health_degraded(mock_container_class, health_service):
    """Test check_database_health returns degraded status."""
    mock_container = MagicMock()
    # Mock async_persistence with a pool that has size > 0
    mock_pool = MagicMock()
    mock_pool._size = 3  # Pool size > 0
    mock_async_persistence = MagicMock()
    mock_async_persistence._pool = mock_pool
    mock_container.async_persistence = mock_async_persistence
    mock_container_class.get_instance.return_value = mock_container

    with patch("time.time", side_effect=[0, 0.5]):  # 500ms query time (between 100ms and timeout = degraded)
        result = health_service.check_database_health()
        assert result["status"] == HealthStatus.DEGRADED
        assert result["connection_count"] == 3
        assert result["last_query_time_ms"] == 500.0


@patch("server.container.ApplicationContainer")
def test_check_database_health_unhealthy(mock_container_class, health_service):
    """Test check_database_health returns unhealthy status."""
    mock_container = MagicMock()
    # Mock async_persistence with a pool that has size = 0 (unhealthy)
    mock_pool = MagicMock()
    mock_pool._size = 0  # Pool size = 0 = unhealthy
    mock_async_persistence = MagicMock()
    mock_async_persistence._pool = mock_pool
    mock_container.async_persistence = mock_async_persistence
    mock_container_class.get_instance.return_value = mock_container

    with patch("time.time", side_effect=[0, 1.5]):  # 1500ms query time
        result = health_service.check_database_health()
        assert result["status"] == HealthStatus.UNHEALTHY
        assert result["connection_count"] == 0
        assert result["last_query_time_ms"] == 1500.0


@patch("server.container.ApplicationContainer")
def test_check_database_health_error(mock_container_class, health_service):
    """Test check_database_health handles errors gracefully."""
    mock_container_class.get_instance.side_effect = Exception("Container error")
    result = health_service.check_database_health()
    assert result["status"] == HealthStatus.UNHEALTHY
    assert result["connection_count"] == 0
    assert result["last_query_time_ms"] is None


def test_check_connections_health_healthy(health_service, mock_connection_manager):
    """Test check_connections_health returns healthy status."""
    mock_connection_manager.get_memory_stats.return_value = {
        "connections": {
            "active_connections": 30,
            "max_connections": 100,
            "connection_rate_per_minute": 5.0,
        }
    }
    result = health_service.check_connections_health()
    assert result["status"] == HealthStatus.HEALTHY
    assert result["active_connections"] == 30
    assert result["max_connections"] == 100


def test_check_connections_health_degraded(health_service, mock_connection_manager):
    """Test check_connections_health returns degraded status."""
    mock_connection_manager.get_memory_stats.return_value = {
        "connections": {
            "active_connections": 60,
            "max_connections": 100,
            "connection_rate_per_minute": 10.0,
        }
    }
    result = health_service.check_connections_health()
    assert result["status"] == HealthStatus.DEGRADED
    assert result["active_connections"] == 60


def test_check_connections_health_unhealthy(health_service, mock_connection_manager):
    """Test check_connections_health returns unhealthy status."""
    mock_connection_manager.get_memory_stats.return_value = {
        "connections": {
            "active_connections": 85,
            "max_connections": 100,
            "connection_rate_per_minute": 15.0,
        }
    }
    result = health_service.check_connections_health()
    assert result["status"] == HealthStatus.UNHEALTHY
    assert result["active_connections"] == 85


def test_check_connections_health_no_manager(health_service):
    """Test check_connections_health when connection manager is not available."""
    health_service.connection_manager = None
    with patch("server.services.health_service.resolve_connection_manager", return_value=None):
        result = health_service.check_connections_health()
        assert result["status"] == HealthStatus.UNHEALTHY
        assert result["active_connections"] == 0


def test_check_connections_health_error(health_service, mock_connection_manager):
    """Test check_connections_health handles errors gracefully."""
    mock_connection_manager.get_memory_stats.side_effect = Exception("Connection error")
    result = health_service.check_connections_health()
    assert result["status"] == HealthStatus.UNHEALTHY
    assert result["active_connections"] == 0


@patch("server.services.health_service.psutil.Process")
@patch("server.services.health_service.psutil.cpu_percent")
def test_get_server_component_health_healthy(mock_cpu, mock_process, health_service):
    """Test get_server_component_health returns healthy status."""
    mock_memory_info = MagicMock()
    mock_memory_info.rss = 512 * 1024 * 1024  # 512 MB
    mock_process_instance = MagicMock()
    mock_process_instance.memory_info.return_value = mock_memory_info
    mock_process.return_value = mock_process_instance
    mock_cpu.return_value = 50.0

    component = health_service.get_server_component_health()
    assert component.status == HealthStatus.HEALTHY
    assert component.memory_usage_mb == 512.0
    assert component.cpu_usage_percent == 50.0


@patch("server.services.health_service.psutil.Process")
@patch("server.services.health_service.psutil.cpu_percent")
def test_get_server_component_health_degraded(mock_cpu, mock_process, health_service):
    """Test get_server_component_health returns degraded status."""
    mock_memory_info = MagicMock()
    mock_memory_info.rss = 1400 * 1024 * 1024  # 1400 MB
    mock_process_instance = MagicMock()
    mock_process_instance.memory_info.return_value = mock_memory_info
    mock_process.return_value = mock_process_instance
    mock_cpu.return_value = 85.0

    component = health_service.get_server_component_health()
    assert component.status == HealthStatus.DEGRADED


@patch("server.services.health_service.psutil.Process")
@patch("server.services.health_service.psutil.cpu_percent")
def test_get_server_component_health_unhealthy(mock_cpu, mock_process, health_service):
    """Test get_server_component_health returns unhealthy status."""
    mock_memory_info = MagicMock()
    mock_memory_info.rss = 2000 * 1024 * 1024  # 2000 MB
    mock_process_instance = MagicMock()
    mock_process_instance.memory_info.return_value = mock_memory_info
    mock_process.return_value = mock_process_instance
    mock_cpu.return_value = 95.0

    component = health_service.get_server_component_health()
    assert component.status == HealthStatus.UNHEALTHY


@patch("server.container.ApplicationContainer")
def test_get_database_component_health(mock_container_class, health_service):
    """Test get_database_component_health returns database component."""
    mock_container = MagicMock()
    # Mock async_persistence with a pool that has size > 0
    mock_pool = MagicMock()
    mock_pool._size = 5  # Pool size > 0
    mock_async_persistence = MagicMock()
    mock_async_persistence._pool = mock_pool
    mock_container.async_persistence = mock_async_persistence
    mock_container_class.get_instance.return_value = mock_container

    with patch("time.time", side_effect=[0, 0.05]):  # 50ms query time (< 100ms = healthy)
        component = health_service.get_database_component_health()
        assert component.status == HealthStatus.HEALTHY
        assert component.connection_count == 5
        assert component.last_query_time_ms == 50.0


def test_get_connections_component_health(health_service, mock_connection_manager):
    """Test get_connections_component_health returns connections component."""
    component = health_service.get_connections_component_health()
    assert component.status == HealthStatus.HEALTHY
    assert component.active_connections == 5
    assert component.max_connections == 100


def test_generate_alerts_no_alerts(health_service):
    """Test generate_alerts returns empty list when all healthy."""
    from server.models.health import ConnectionsComponent, DatabaseComponent, HealthComponents, ServerComponent

    components = HealthComponents(
        server=ServerComponent(
            status=HealthStatus.HEALTHY, uptime_seconds=100, memory_usage_mb=500, cpu_usage_percent=50
        ),
        database=DatabaseComponent(status=HealthStatus.HEALTHY, connection_count=5, last_query_time_ms=50),
        connections=ConnectionsComponent(
            status=HealthStatus.HEALTHY, active_connections=10, max_connections=100, connection_rate_per_minute=2.0
        ),
    )
    alerts = health_service.generate_alerts(components)
    assert len(alerts) == 0


def test_generate_alerts_with_alerts(health_service):
    """Test generate_alerts returns alerts when components are unhealthy."""
    from server.models.health import ConnectionsComponent, DatabaseComponent, HealthComponents, ServerComponent

    components = HealthComponents(
        server=ServerComponent(
            status=HealthStatus.UNHEALTHY, uptime_seconds=100, memory_usage_mb=1500, cpu_usage_percent=90
        ),
        database=DatabaseComponent(status=HealthStatus.DEGRADED, connection_count=5, last_query_time_ms=500),
        connections=ConnectionsComponent(
            status=HealthStatus.UNHEALTHY, active_connections=85, max_connections=100, connection_rate_per_minute=20.0
        ),
    )
    alerts = health_service.generate_alerts(components)
    assert len(alerts) > 0
    assert any("Server performance critical" in alert for alert in alerts)
    assert any("High memory usage" in alert for alert in alerts)
    assert any("High CPU usage" in alert for alert in alerts)


def test_determine_overall_status_healthy(health_service):
    """Test determine_overall_status returns healthy when all components healthy."""
    from server.models.health import ConnectionsComponent, DatabaseComponent, HealthComponents, ServerComponent

    components = HealthComponents(
        server=ServerComponent(
            status=HealthStatus.HEALTHY, uptime_seconds=100, memory_usage_mb=500, cpu_usage_percent=50
        ),
        database=DatabaseComponent(status=HealthStatus.HEALTHY, connection_count=5, last_query_time_ms=50),
        connections=ConnectionsComponent(
            status=HealthStatus.HEALTHY, active_connections=10, max_connections=100, connection_rate_per_minute=2.0
        ),
    )
    status = health_service.determine_overall_status(components)
    assert status == HealthStatus.HEALTHY


def test_determine_overall_status_degraded(health_service):
    """Test determine_overall_status returns degraded when any component degraded."""
    from server.models.health import ConnectionsComponent, DatabaseComponent, HealthComponents, ServerComponent

    components = HealthComponents(
        server=ServerComponent(
            status=HealthStatus.HEALTHY, uptime_seconds=100, memory_usage_mb=500, cpu_usage_percent=50
        ),
        database=DatabaseComponent(status=HealthStatus.DEGRADED, connection_count=5, last_query_time_ms=500),
        connections=ConnectionsComponent(
            status=HealthStatus.HEALTHY, active_connections=10, max_connections=100, connection_rate_per_minute=2.0
        ),
    )
    status = health_service.determine_overall_status(components)
    assert status == HealthStatus.DEGRADED


def test_determine_overall_status_unhealthy(health_service):
    """Test determine_overall_status returns unhealthy when any component unhealthy."""
    from server.models.health import ConnectionsComponent, DatabaseComponent, HealthComponents, ServerComponent

    components = HealthComponents(
        server=ServerComponent(
            status=HealthStatus.UNHEALTHY, uptime_seconds=100, memory_usage_mb=1500, cpu_usage_percent=90
        ),
        database=DatabaseComponent(status=HealthStatus.HEALTHY, connection_count=5, last_query_time_ms=50),
        connections=ConnectionsComponent(
            status=HealthStatus.HEALTHY, active_connections=10, max_connections=100, connection_rate_per_minute=2.0
        ),
    )
    status = health_service.determine_overall_status(components)
    assert status == HealthStatus.UNHEALTHY


@patch("importlib.metadata.version")
@patch("server.services.health_service.psutil.Process")
@patch("server.services.health_service.psutil.cpu_percent")
@patch("server.container.ApplicationContainer")
def test_get_health_status_success(
    mock_container, mock_cpu, mock_process, mock_version, health_service, mock_connection_manager
):
    """Test get_health_status returns comprehensive health response."""
    mock_version.return_value = "1.0.0"
    mock_memory_info = MagicMock()
    mock_memory_info.rss = 512 * 1024 * 1024
    mock_process_instance = MagicMock()
    mock_process_instance.memory_info.return_value = mock_memory_info
    mock_process.return_value = mock_process_instance
    mock_cpu.return_value = 50.0

    mock_container_instance = MagicMock()
    # Mock async_persistence with a pool that has size > 0
    mock_pool = MagicMock()
    mock_pool._size = 5  # Pool size > 0
    mock_async_persistence = MagicMock()
    mock_async_persistence._pool = mock_pool
    mock_container_instance.async_persistence = mock_async_persistence
    mock_container_instance.room_service = MagicMock()
    mock_container.get_instance.return_value = mock_container_instance

    # Mock time.time to return consistent values
    # First call is in get_server_component_health -> get_server_uptime
    # Second call is in get_health_status -> get_server_uptime
    # We need to account for all calls
    current_time = 1000.0
    with patch("time.time", return_value=current_time):
        # Also need to patch the start_time to ensure positive uptime
        health_service.start_time = current_time - 100.0
        response = health_service.get_health_status()
        assert response.status == HealthStatus.HEALTHY
        assert response.version == "1.0.0"
        assert response.uptime_seconds >= 0
        assert response.components is not None
        assert response.alerts is not None
        assert health_service.health_check_count == 1
        assert health_service.last_health_check is not None


@patch("importlib.metadata.version")
def test_get_health_status_version_fallback(mock_version, health_service):
    """Test get_health_status handles version lookup failure."""
    from importlib.metadata import PackageNotFoundError

    mock_version.side_effect = PackageNotFoundError("Package not found")
    with patch.object(health_service, "get_server_component_health") as mock_server:
        from server.models.health import ConnectionsComponent, DatabaseComponent, ServerComponent

        mock_server.return_value = ServerComponent(
            status=HealthStatus.HEALTHY, uptime_seconds=100, memory_usage_mb=500, cpu_usage_percent=50
        )
        with patch.object(health_service, "get_database_component_health") as mock_db:
            mock_db.return_value = DatabaseComponent(
                status=HealthStatus.HEALTHY, connection_count=5, last_query_time_ms=50
            )
            with patch.object(health_service, "get_connections_component_health") as mock_conn:
                mock_conn.return_value = ConnectionsComponent(
                    status=HealthStatus.HEALTHY,
                    active_connections=10,
                    max_connections=100,
                    connection_rate_per_minute=2.0,
                )
                response = health_service.get_health_status()
                assert response.version == "0.1.0"  # Fallback version


def test_get_health_service_creates_instance():
    """Test get_health_service creates singleton instance."""
    # Reset global state
    import server.services.health_service as health_service_module

    health_service_module._health_service = None
    service = get_health_service()
    assert service is not None
    assert isinstance(service, HealthService)


def test_get_health_service_returns_singleton():
    """Test get_health_service returns same instance."""
    import server.services.health_service as health_service_module

    health_service_module._health_service = None
    service1 = get_health_service()
    service2 = get_health_service()
    assert service1 is service2


def test_get_health_service_updates_connection_manager():
    """Test get_health_service updates connection manager when provided."""
    import server.services.health_service as health_service_module

    health_service_module._health_service = None
    mock_manager = MagicMock()
    service = get_health_service(connection_manager=mock_manager)
    assert service.connection_manager is mock_manager

    # Update with new manager
    new_manager = MagicMock()
    service2 = get_health_service(connection_manager=new_manager)
    assert service2 is service
    assert service2.connection_manager is new_manager
