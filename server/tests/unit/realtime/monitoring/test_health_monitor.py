"""
Unit tests for health monitor.

Tests the HealthMonitor class.
"""

import uuid
from typing import Any
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.realtime.monitoring.health_monitor import HealthMonitor

# pylint: disable=redefined-outer-name  # Reason: Test fixtures need to be redefined for each test
# pylint: disable=protected-access  # Reason: Test code needs to access protected members


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
    player_websockets: dict[uuid.UUID, list[str]] = {}
    active_websockets: dict[str, Any] = {}
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
    connection_metadata: dict[str, Any] = {}
    mock_is_websocket_open.return_value = True
    # check_all_connections_health takes (active_websockets, connection_metadata, player_websockets)
    await health_monitor.check_all_connections_health(active_websockets, connection_metadata, player_websockets)
    # Should not raise
    assert True  # If we get here, it succeeded


def test_health_monitor_init_custom_intervals(
    mock_is_websocket_open, mock_validate_token, mock_cleanup_dead_websocket, mock_performance_tracker
):
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
    # Mock the tracked_task_manager import to prevent import errors
    # Patch at the source module since the import happens inside the method
    with patch("server.app.tracked_task_manager.get_global_tracked_manager") as mock_get_manager:
        mock_manager = MagicMock()
        mock_task = MagicMock()
        mock_task.done.return_value = False
        mock_manager.create_tracked_task.return_value = mock_task
        mock_get_manager.return_value = mock_manager

        health_monitor.start_periodic_checks({}, {}, {})
        # Task should be set if manager is available
        assert health_monitor._health_check_task is not None


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


def test_find_player_id_for_cleanup(health_monitor):
    player_id = uuid.uuid4()
    assert health_monitor._find_player_id_for_cleanup("ws_missing", {}) is None
    assert health_monitor._find_player_id_for_cleanup("ws_001", {player_id: ["ws_001"]}) == player_id


def test_check_connection_stale(health_monitor):
    metadata = MagicMock()
    metadata.last_seen = 0.0
    metadata.player_id = uuid.uuid4()
    assert health_monitor._check_connection_stale(metadata, now=1000.0, connection_id="ws_1") is True
    metadata.last_seen = 999.0
    assert health_monitor._check_connection_stale(metadata, now=1000.0, connection_id="ws_1") is False


def test_check_websocket_open(health_monitor, mock_is_websocket_open):
    metadata = MagicMock()
    metadata.player_id = uuid.uuid4()
    mock_is_websocket_open.return_value = True
    assert health_monitor._check_websocket_open(MagicMock(), "ws_1", metadata) is True
    mock_is_websocket_open.return_value = False
    assert health_monitor._check_websocket_open(MagicMock(), "ws_1", metadata) is False


@pytest.mark.asyncio
async def test_validate_and_update_token(health_monitor, mock_validate_token):
    metadata = MagicMock()
    metadata.token = "tok"
    metadata.player_id = uuid.uuid4()
    # last_token_validation must be truthy; 0.0 skips revalidation
    metadata.last_token_validation = 1.0
    mock_validate_token.return_value = False
    assert await health_monitor._validate_and_update_token(metadata, now=1000.0, connection_id="ws_1") is False
    mock_validate_token.return_value = True
    metadata.last_token_validation = 1.0
    assert await health_monitor._validate_and_update_token(metadata, now=1000.0, connection_id="ws_1") is True
    assert metadata.last_token_validation == 1000.0


@pytest.mark.asyncio
async def test_process_single_connection_paths(health_monitor, mock_is_websocket_open, mock_validate_token):
    player_id = uuid.uuid4()
    stale: list[tuple[uuid.UUID, str]] = []
    await health_monitor._process_single_connection(
        "ws_orphan", MagicMock(), {}, {player_id: ["ws_orphan"]}, 1000.0, stale
    )
    assert stale == [(player_id, "ws_orphan")]

    stale.clear()
    metadata = MagicMock()
    metadata.player_id = player_id
    metadata.last_seen = 999.0
    metadata.token = "tok"
    metadata.last_token_validation = 999.0
    mock_is_websocket_open.return_value = True
    mock_validate_token.return_value = True
    await health_monitor._process_single_connection(
        "ws_ok", MagicMock(), {"ws_ok": metadata}, {player_id: ["ws_ok"]}, 1000.0, stale
    )
    assert stale == []
    assert metadata.is_healthy is True

    stale.clear()
    metadata.last_seen = 0.0
    await health_monitor._process_single_connection(
        "ws_stale", MagicMock(), {"ws_stale": metadata}, {player_id: ["ws_stale"]}, 1000.0, stale
    )
    assert stale == [(player_id, "ws_stale")]


@pytest.mark.asyncio
async def test_cleanup_stale_connections(health_monitor, mock_cleanup_dead_websocket):
    player_id = uuid.uuid4()
    mock_cleanup_dead_websocket.side_effect = [None, RuntimeError("cleanup fail")]
    await health_monitor._cleanup_stale_connections([(player_id, "ws_1"), (player_id, "ws_2")])
    assert mock_cleanup_dead_websocket.await_count == 2


@pytest.mark.asyncio
async def test_check_all_connections_health_with_metadata(
    health_monitor, mock_is_websocket_open, mock_validate_token, mock_cleanup_dead_websocket
):
    player_id = uuid.uuid4()
    metadata = MagicMock()
    metadata.player_id = player_id
    metadata.last_seen = 999999.0
    metadata.token = None
    metadata.last_token_validation = None
    mock_is_websocket_open.return_value = False
    await health_monitor.check_all_connections_health(
        {"ws_1": MagicMock()},
        {"ws_1": metadata},
        {player_id: ["ws_1"]},
    )
    mock_cleanup_dead_websocket.assert_awaited()


@pytest.mark.asyncio
async def test_periodic_health_check_task_cancel(health_monitor):
    import asyncio

    health_monitor.health_check_interval = 0.01
    task = asyncio.create_task(health_monitor.periodic_health_check_task({}, {}, {}))
    await asyncio.sleep(0.02)
    task.cancel()
    with pytest.raises(asyncio.CancelledError):
        await task


@pytest.mark.asyncio
async def test_wait_for_task_cancellation(health_monitor):
    import asyncio

    async def long_task():
        await asyncio.sleep(10)

    task = asyncio.create_task(long_task())
    task.cancel()
    await health_monitor._wait_for_task_cancellation(task)


def test_start_periodic_checks_already_running(health_monitor):
    health_monitor._health_check_task = MagicMock()
    health_monitor._health_check_task.done.return_value = False
    health_monitor.start_periodic_checks({}, {}, {})
