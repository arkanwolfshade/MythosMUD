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
