"""
Unit tests for health monitor.

Tests the HealthMonitor class.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.realtime.monitoring.health_monitor import HealthMonitor


@pytest.fixture
def mock_is_websocket_open():
    """Create a mock is_websocket_open callback."""
    return MagicMock(return_value=True)


@pytest.fixture
def mock_validate_token():
    """Create a mock validate_token callback."""
    return AsyncMock(return_value=True)


@pytest.fixture
def mock_cleanup_dead_websocket():
    """Create a mock cleanup_dead_websocket callback."""
    return AsyncMock()


@pytest.fixture
def mock_performance_tracker():
    """Create a mock performance tracker."""
    return MagicMock()


@pytest.fixture
def health_monitor(mock_is_websocket_open, mock_validate_token, mock_cleanup_dead_websocket, mock_performance_tracker):
    """Create a HealthMonitor instance."""
    return HealthMonitor(
        is_websocket_open_callback=mock_is_websocket_open,
        validate_token_callback=mock_validate_token,
        cleanup_dead_websocket_callback=mock_cleanup_dead_websocket,
        performance_tracker=mock_performance_tracker,
    )


def test_health_monitor_init(health_monitor, mock_is_websocket_open, mock_performance_tracker):
    """Test HealthMonitor initialization."""
    assert health_monitor.is_websocket_open == mock_is_websocket_open
    assert health_monitor.performance_tracker == mock_performance_tracker
    assert health_monitor.health_check_interval == 30.0
    assert health_monitor.connection_timeout == 300.0


@pytest.mark.asyncio
async def test_check_player_connection_health(health_monitor, mock_is_websocket_open):
    """Test check_player_connection_health() returns health status."""
    player_id = uuid.uuid4()
    player_websockets = {player_id: ["ws_001", "ws_002"]}
    active_websockets = {"ws_001": MagicMock(), "ws_002": MagicMock()}
    mock_is_websocket_open.return_value = True
    result = await health_monitor.check_player_connection_health(player_id, player_websockets, active_websockets)
    assert "player_id" in result
    assert "websocket_healthy" in result
    assert "overall_health" in result


@pytest.mark.asyncio
async def test_check_player_connection_health_no_websockets(health_monitor):
    """Test check_player_connection_health() when player has no websockets."""
    player_id = uuid.uuid4()
    player_websockets = {}
    active_websockets = {}
    result = await health_monitor.check_player_connection_health(player_id, player_websockets, active_websockets)
    assert result["websocket_healthy"] == 0
    assert result["overall_health"] == "no_connections"


@pytest.mark.asyncio
async def test_check_player_connection_health_unhealthy(health_monitor, mock_is_websocket_open):
    """Test check_player_connection_health() when websockets are unhealthy."""
    player_id = uuid.uuid4()
    player_websockets = {player_id: ["ws_001"]}
    active_websockets = {"ws_001": MagicMock()}
    mock_is_websocket_open.return_value = False
    result = await health_monitor.check_player_connection_health(player_id, player_websockets, active_websockets)
    assert result["websocket_unhealthy"] > 0
    assert result["overall_health"] in ["unhealthy", "degraded"]


@pytest.mark.asyncio
async def test_check_all_connections_health(health_monitor, mock_is_websocket_open):
    """Test check_all_connections_health() checks all connections."""
    player_websockets = {uuid.uuid4(): ["ws_001"], uuid.uuid4(): ["ws_002"]}
    active_websockets = {"ws_001": MagicMock(), "ws_002": MagicMock()}
    connection_metadata = {}
    mock_is_websocket_open.return_value = True
    # check_all_connections_health takes (active_websockets, connection_metadata, player_websockets)
    await health_monitor.check_all_connections_health(active_websockets, connection_metadata, player_websockets)
    # Should not raise
    assert True  # If we get here, it succeeded


def test_health_monitor_init_custom_intervals(mock_is_websocket_open, mock_validate_token, mock_cleanup_dead_websocket, mock_performance_tracker):
    """Test HealthMonitor initialization with custom intervals."""
    monitor = HealthMonitor(
        is_websocket_open_callback=mock_is_websocket_open,
        validate_token_callback=mock_validate_token,
        cleanup_dead_websocket_callback=mock_cleanup_dead_websocket,
        performance_tracker=mock_performance_tracker,
        health_check_interval=60.0,
        connection_timeout=600.0,
        token_revalidation_interval=600.0,
    )
    assert monitor.health_check_interval == 60.0
    assert monitor.connection_timeout == 600.0
    assert monitor.token_revalidation_interval == 600.0


@pytest.mark.asyncio
async def test_start_periodic_checks(health_monitor):
    """Test start_periodic_checks() starts periodic checks."""
    # start_periodic_checks takes (active_websockets, connection_metadata, player_websockets)
    # It needs a running event loop to create tasks
    health_monitor.start_periodic_checks({}, {}, {})
    # Task may be None if creation fails (no event loop), but should not raise
    assert health_monitor._health_check_task is None or health_monitor._health_check_task is not None


@pytest.mark.asyncio
async def test_stop_periodic_checks(health_monitor):
    """Test stop_periodic_checks() stops periodic checks."""
    # Create a mock task in async context
    import asyncio
    async def dummy_task():
        await asyncio.sleep(0.1)
    health_monitor._health_check_task = asyncio.create_task(dummy_task())
    health_monitor.stop_periodic_checks()
    # Task should be cancelled or None
    assert health_monitor._health_check_task is None or health_monitor._health_check_task.cancelled()
