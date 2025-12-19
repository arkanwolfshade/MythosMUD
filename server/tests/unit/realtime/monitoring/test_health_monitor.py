"""
Tests for health monitoring for connection management.

This module tests the HealthMonitor class which provides comprehensive
connection health checking including WebSocket state verification,
token validation, and proactive cleanup of stale connections.
"""

import asyncio
import time
from typing import Any, cast
from unittest.mock import AsyncMock, MagicMock, PropertyMock, patch
from uuid import uuid4

import pytest

from server.realtime.monitoring.health_monitor import HealthMonitor


class TestHealthMonitorInit:
    """Test HealthMonitor initialization."""

    def test_init(self) -> None:
        """Test HealthMonitor initialization."""
        mock_is_websocket_open = MagicMock(return_value=True)
        mock_validate_token = AsyncMock(return_value=True)
        mock_cleanup_dead_websocket = AsyncMock()
        mock_performance_tracker = MagicMock()

        monitor = HealthMonitor(
            mock_is_websocket_open,
            mock_validate_token,
            mock_cleanup_dead_websocket,
            mock_performance_tracker,
            health_check_interval=30.0,
            connection_timeout=300.0,
            token_revalidation_interval=300.0,
        )

        assert monitor.is_websocket_open == mock_is_websocket_open
        assert monitor.validate_token == mock_validate_token
        assert monitor.cleanup_dead_websocket == mock_cleanup_dead_websocket
        assert monitor.performance_tracker == mock_performance_tracker
        assert monitor.health_check_interval == 30.0
        assert monitor.connection_timeout == 300.0
        assert monitor.token_revalidation_interval == 300.0
        assert monitor._health_check_task is None


class TestCheckPlayerConnectionHealth:
    """Test check_player_connection_health method."""

    @pytest.mark.asyncio
    async def test_check_player_connection_health_healthy(self) -> None:
        """Test checking health when all connections are healthy."""
        mock_is_websocket_open = MagicMock(return_value=True)
        mock_validate_token = AsyncMock(return_value=True)
        mock_cleanup_dead_websocket = AsyncMock()
        mock_performance_tracker = MagicMock()

        monitor = HealthMonitor(
            mock_is_websocket_open,
            mock_validate_token,
            mock_cleanup_dead_websocket,
            mock_performance_tracker,
        )

        player_id = uuid4()
        connection_id1 = "conn-1"
        connection_id2 = "conn-2"

        mock_websocket1 = MagicMock()
        mock_websocket1.client_state.name = "CONNECTED"

        mock_websocket2 = MagicMock()
        mock_websocket2.client_state.name = "CONNECTED"

        player_websockets = {player_id: [connection_id1, connection_id2]}
        active_websockets = {connection_id1: mock_websocket1, connection_id2: mock_websocket2}

        with patch("server.realtime.monitoring.health_monitor.logger"):
            result = await monitor.check_player_connection_health(
                player_id, cast(Any, player_websockets), cast(Any, active_websockets)
            )

            assert result["player_id"] == player_id
            assert result["websocket_healthy"] == 2
            assert result["websocket_unhealthy"] == 0
            assert result["overall_health"] == "healthy"

    @pytest.mark.asyncio
    async def test_check_player_connection_health_unhealthy(self) -> None:
        """Test checking health when connections are unhealthy."""
        mock_is_websocket_open = MagicMock(return_value=True)
        mock_validate_token = AsyncMock(return_value=True)
        mock_cleanup_dead_websocket = AsyncMock()
        mock_performance_tracker = MagicMock()

        monitor = HealthMonitor(
            mock_is_websocket_open,
            mock_validate_token,
            mock_cleanup_dead_websocket,
            mock_performance_tracker,
        )

        player_id = uuid4()
        connection_id = "conn-1"

        # Make accessing client_state.name raise RuntimeError (which is caught)
        mock_websocket = MagicMock()
        type(mock_websocket).client_state = PropertyMock(side_effect=RuntimeError("Connection error"))

        player_websockets = {player_id: [connection_id]}
        active_websockets = {connection_id: mock_websocket}

        with patch("server.realtime.monitoring.health_monitor.logger"):
            result = await monitor.check_player_connection_health(
                player_id, cast(Any, player_websockets), cast(Any, active_websockets)
            )

            assert result["websocket_healthy"] == 0
            assert result["websocket_unhealthy"] == 1
            assert result["overall_health"] == "unhealthy"
            mock_cleanup_dead_websocket.assert_called_once_with(player_id, connection_id)

    @pytest.mark.asyncio
    async def test_check_player_connection_health_degraded(self) -> None:
        """Test checking health when some connections are unhealthy."""
        mock_is_websocket_open = MagicMock(return_value=True)
        mock_validate_token = AsyncMock(return_value=True)
        mock_cleanup_dead_websocket = AsyncMock()
        mock_performance_tracker = MagicMock()

        monitor = HealthMonitor(
            mock_is_websocket_open,
            mock_validate_token,
            mock_cleanup_dead_websocket,
            mock_performance_tracker,
        )

        player_id = uuid4()
        connection_id1 = "conn-1"
        connection_id2 = "conn-2"

        mock_websocket1 = MagicMock()
        mock_websocket1.client_state.name = "CONNECTED"

        # Make the second websocket raise RuntimeError when accessing client_state (which is caught)
        mock_websocket2 = MagicMock()
        type(mock_websocket2).client_state = PropertyMock(side_effect=RuntimeError("Connection error"))

        player_websockets = {player_id: [connection_id1, connection_id2]}
        active_websockets = {connection_id1: mock_websocket1, connection_id2: mock_websocket2}

        with patch("server.realtime.monitoring.health_monitor.logger"):
            result = await monitor.check_player_connection_health(
                player_id, cast(Any, player_websockets), cast(Any, active_websockets)
            )

            assert result["websocket_healthy"] == 1
            assert result["websocket_unhealthy"] == 1
            assert result["overall_health"] == "degraded"

    @pytest.mark.asyncio
    async def test_check_player_connection_health_no_connections(self) -> None:
        """Test checking health when player has no connections."""
        mock_is_websocket_open = MagicMock(return_value=True)
        mock_validate_token = AsyncMock(return_value=True)
        mock_cleanup_dead_websocket = AsyncMock()
        mock_performance_tracker = MagicMock()

        monitor = HealthMonitor(
            mock_is_websocket_open,
            mock_validate_token,
            mock_cleanup_dead_websocket,
            mock_performance_tracker,
        )

        player_id = uuid4()
        player_websockets: dict[str, Any] = {}
        active_websockets: dict[str, Any] = {}

        with patch("server.realtime.monitoring.health_monitor.logger"):
            result = await monitor.check_player_connection_health(
                player_id, cast(Any, player_websockets), cast(Any, active_websockets)
            )

            assert result["websocket_healthy"] == 0
            assert result["websocket_unhealthy"] == 0
            assert result["overall_health"] == "no_connections"

    @pytest.mark.asyncio
    async def test_check_player_connection_health_error(self) -> None:
        """Test checking health when an error occurs."""
        mock_is_websocket_open = MagicMock(return_value=True)
        mock_validate_token = AsyncMock(return_value=True)
        mock_cleanup_dead_websocket = AsyncMock()
        mock_performance_tracker = MagicMock()

        monitor = HealthMonitor(
            mock_is_websocket_open,
            mock_validate_token,
            mock_cleanup_dead_websocket,
            mock_performance_tracker,
        )

        player_id = uuid4()
        # Cause an error by passing invalid data
        player_websockets = {player_id: ["conn-1"]}
        active_websockets = None

        with patch("server.realtime.monitoring.health_monitor.logger"):
            result = await monitor.check_player_connection_health(
                player_id, cast(Any, player_websockets), cast(Any, active_websockets)
            )

            assert result["overall_health"] == "error"


class TestCheckAllConnectionsHealth:
    """Test check_all_connections_health method."""

    @pytest.mark.asyncio
    async def test_check_all_connections_health_healthy(self) -> None:
        """Test checking all connections when they are healthy."""
        mock_is_websocket_open = MagicMock(return_value=True)
        mock_validate_token = AsyncMock(return_value=True)
        mock_cleanup_dead_websocket = AsyncMock()
        mock_performance_tracker = MagicMock()
        mock_performance_tracker.record_health_check = MagicMock()

        monitor = HealthMonitor(
            mock_is_websocket_open,
            mock_validate_token,
            mock_cleanup_dead_websocket,
            mock_performance_tracker,
        )

        player_id = uuid4()
        connection_id = "conn-1"

        # Create mock metadata
        class MockMetadata:
            def __init__(self):
                self.player_id = player_id
                self.last_seen = time.time()
                self.token = None
                self.last_token_validation = None
                self.is_healthy = True

        mock_metadata = MockMetadata()
        mock_websocket = MagicMock()

        active_websockets = {connection_id: mock_websocket}
        connection_metadata = {connection_id: mock_metadata}
        player_websockets = {player_id: [connection_id]}

        with patch("server.realtime.monitoring.health_monitor.logger"):
            await monitor.check_all_connections_health(
                cast(Any, active_websockets), cast(Any, connection_metadata), cast(Any, player_websockets)
            )

            assert mock_metadata.is_healthy is True
            mock_performance_tracker.record_health_check.assert_called_once()

    @pytest.mark.asyncio
    async def test_check_all_connections_health_stale(self) -> None:
        """Test checking all connections when some are stale."""
        mock_is_websocket_open = MagicMock(return_value=True)
        mock_validate_token = AsyncMock(return_value=True)
        mock_cleanup_dead_websocket = AsyncMock()
        mock_performance_tracker = MagicMock()
        mock_performance_tracker.record_health_check = MagicMock()

        monitor = HealthMonitor(
            mock_is_websocket_open,
            mock_validate_token,
            mock_cleanup_dead_websocket,
            mock_performance_tracker,
            connection_timeout=300.0,
        )

        player_id = uuid4()
        connection_id = "conn-1"

        # Create mock metadata with stale connection
        class MockMetadata:
            def __init__(self):
                self.player_id = player_id
                self.last_seen = time.time() - 400.0  # Stale (older than 300s timeout)
                self.token = None
                self.last_token_validation = None
                self.is_healthy = True

        mock_metadata = MockMetadata()
        mock_websocket = MagicMock()

        active_websockets = {connection_id: mock_websocket}
        connection_metadata = {connection_id: mock_metadata}
        player_websockets = {player_id: [connection_id]}

        with patch("server.realtime.monitoring.health_monitor.logger"):
            await monitor.check_all_connections_health(
                cast(Any, active_websockets), cast(Any, connection_metadata), cast(Any, player_websockets)
            )

            assert mock_metadata.is_healthy is False
            mock_cleanup_dead_websocket.assert_called_once_with(player_id, connection_id)

    @pytest.mark.asyncio
    async def test_check_all_connections_health_token_revalidation(self) -> None:
        """Test checking all connections with token revalidation."""
        mock_is_websocket_open = MagicMock(return_value=True)
        mock_validate_token = AsyncMock(return_value=True)
        mock_cleanup_dead_websocket = AsyncMock()
        mock_performance_tracker = MagicMock()
        mock_performance_tracker.record_health_check = MagicMock()

        monitor = HealthMonitor(
            mock_is_websocket_open,
            mock_validate_token,
            mock_cleanup_dead_websocket,
            mock_performance_tracker,
            token_revalidation_interval=300.0,
        )

        player_id = uuid4()
        connection_id = "conn-1"

        # Create mock metadata with token that needs revalidation
        class MockMetadata:
            def __init__(self):
                self.player_id = player_id
                self.last_seen = time.time()
                self.token = "test-token"
                self.last_token_validation = time.time() - 400.0  # Needs revalidation
                self.is_healthy = True

        mock_metadata = MockMetadata()
        mock_websocket = MagicMock()

        active_websockets = {connection_id: mock_websocket}
        connection_metadata = {connection_id: mock_metadata}
        player_websockets = {player_id: [connection_id]}

        with patch("server.realtime.monitoring.health_monitor.logger"):
            await monitor.check_all_connections_health(
                cast(Any, active_websockets), cast(Any, connection_metadata), cast(Any, player_websockets)
            )

            mock_validate_token.assert_called_once_with("test-token", player_id)
            assert mock_metadata.is_healthy is True
            assert mock_metadata.last_token_validation > time.time() - 1.0  # Updated recently

    @pytest.mark.asyncio
    async def test_check_all_connections_health_token_validation_failed(self) -> None:
        """Test checking all connections when token validation fails."""
        mock_is_websocket_open = MagicMock(return_value=True)
        mock_validate_token = AsyncMock(return_value=False)  # Token invalid
        mock_cleanup_dead_websocket = AsyncMock()
        mock_performance_tracker = MagicMock()
        mock_performance_tracker.record_health_check = MagicMock()

        monitor = HealthMonitor(
            mock_is_websocket_open,
            mock_validate_token,
            mock_cleanup_dead_websocket,
            mock_performance_tracker,
            token_revalidation_interval=300.0,
        )

        player_id = uuid4()
        connection_id = "conn-1"

        # Create mock metadata with token that needs revalidation
        class MockMetadata:
            def __init__(self):
                self.player_id = player_id
                self.last_seen = time.time()
                self.token = "test-token"
                self.last_token_validation = time.time() - 400.0  # Needs revalidation
                self.is_healthy = True

        mock_metadata = MockMetadata()
        mock_websocket = MagicMock()

        active_websockets = {connection_id: mock_websocket}
        connection_metadata = {connection_id: mock_metadata}
        player_websockets = {player_id: [connection_id]}

        with patch("server.realtime.monitoring.health_monitor.logger"):
            await monitor.check_all_connections_health(
                cast(Any, active_websockets), cast(Any, connection_metadata), cast(Any, player_websockets)
            )

            assert mock_metadata.is_healthy is False
            mock_cleanup_dead_websocket.assert_called_once_with(player_id, connection_id)

    @pytest.mark.asyncio
    async def test_check_all_connections_health_missing_metadata(self) -> None:
        """Test checking all connections when metadata is missing."""
        mock_is_websocket_open = MagicMock(return_value=True)
        mock_validate_token = AsyncMock(return_value=True)
        mock_cleanup_dead_websocket = AsyncMock()
        mock_performance_tracker = MagicMock()
        mock_performance_tracker.record_health_check = MagicMock()

        monitor = HealthMonitor(
            mock_is_websocket_open,
            mock_validate_token,
            mock_cleanup_dead_websocket,
            mock_performance_tracker,
        )

        player_id = uuid4()
        connection_id = "conn-1"

        mock_websocket = MagicMock()

        active_websockets = {connection_id: mock_websocket}
        connection_metadata: dict[str, Any] = {}  # Missing metadata
        player_websockets = {player_id: [connection_id]}

        with patch("server.realtime.monitoring.health_monitor.logger"):
            await monitor.check_all_connections_health(
                cast(Any, active_websockets), cast(Any, connection_metadata), cast(Any, player_websockets)
            )

            # Should attempt cleanup for missing metadata
            mock_cleanup_dead_websocket.assert_called_once_with(player_id, connection_id)

    @pytest.mark.asyncio
    async def test_check_all_connections_health_websocket_not_open(self) -> None:
        """Test checking all connections when WebSocket is not open."""
        mock_is_websocket_open = MagicMock(return_value=False)  # Not open
        mock_validate_token = AsyncMock(return_value=True)
        mock_cleanup_dead_websocket = AsyncMock()
        mock_performance_tracker = MagicMock()
        mock_performance_tracker.record_health_check = MagicMock()

        monitor = HealthMonitor(
            mock_is_websocket_open,
            mock_validate_token,
            mock_cleanup_dead_websocket,
            mock_performance_tracker,
        )

        player_id = uuid4()
        connection_id = "conn-1"

        # Create mock metadata
        class MockMetadata:
            def __init__(self):
                self.player_id = player_id
                self.last_seen = time.time()
                self.token = None
                self.last_token_validation = None
                self.is_healthy = True

        mock_metadata = MockMetadata()
        mock_websocket = MagicMock()

        active_websockets = {connection_id: mock_websocket}
        connection_metadata = {connection_id: mock_metadata}
        player_websockets = {player_id: [connection_id]}

        with patch("server.realtime.monitoring.health_monitor.logger"):
            await monitor.check_all_connections_health(
                cast(Any, active_websockets), cast(Any, connection_metadata), cast(Any, player_websockets)
            )

            assert mock_metadata.is_healthy is False
            mock_cleanup_dead_websocket.assert_called_once_with(player_id, connection_id)


class TestPeriodicHealthCheckTask:
    """Test periodic_health_check_task method."""

    @pytest.mark.asyncio
    async def test_periodic_health_check_task_runs(self) -> None:
        """Test that periodic health check task runs."""
        mock_is_websocket_open = MagicMock(return_value=True)
        mock_validate_token = AsyncMock(return_value=True)
        mock_cleanup_dead_websocket = AsyncMock()
        mock_performance_tracker = MagicMock()

        monitor = HealthMonitor(
            mock_is_websocket_open,
            mock_validate_token,
            mock_cleanup_dead_websocket,
            mock_performance_tracker,
            health_check_interval=0.1,  # Short interval for testing
        )

        active_websockets: dict[str, Any] = {}
        connection_metadata: dict[str, Any] = {}
        player_websockets: dict[str, Any] = {}

        with patch("server.realtime.monitoring.health_monitor.logger"):
            # Start the task
            task = asyncio.create_task(
                monitor.periodic_health_check_task(
                    cast(Any, active_websockets), cast(Any, connection_metadata), cast(Any, player_websockets)
                )
            )

            # Wait a bit for it to run
            await asyncio.sleep(0.15)

            # Cancel the task
            task.cancel()

            # Wait for cancellation
            try:
                await task
            except asyncio.CancelledError:
                pass


class TestStartPeriodicChecks:
    """Test start_periodic_checks method."""

    def test_start_periodic_checks_success(self) -> None:
        """Test successfully starting periodic checks."""
        mock_is_websocket_open = MagicMock(return_value=True)
        mock_validate_token = AsyncMock(return_value=True)
        mock_cleanup_dead_websocket = AsyncMock()
        mock_performance_tracker = MagicMock()

        monitor = HealthMonitor(
            mock_is_websocket_open,
            mock_validate_token,
            mock_cleanup_dead_websocket,
            mock_performance_tracker,
        )

        mock_tracked_manager = MagicMock()
        mock_task = MagicMock()
        mock_tracked_manager.create_tracked_task.return_value = mock_task

        active_websockets: dict[str, Any] = {}
        connection_metadata: dict[str, Any] = {}
        player_websockets: dict[str, Any] = {}

        with patch("server.app.tracked_task_manager.get_global_tracked_manager", return_value=mock_tracked_manager):
            with patch("server.realtime.monitoring.health_monitor.logger"):
                monitor.start_periodic_checks(
                    cast(Any, active_websockets), cast(Any, connection_metadata), cast(Any, player_websockets)
                )

                assert monitor._health_check_task == mock_task
                mock_tracked_manager.create_tracked_task.assert_called_once()

    def test_start_periodic_checks_already_running(self) -> None:
        """Test starting periodic checks when already running."""
        mock_is_websocket_open = MagicMock(return_value=True)
        mock_validate_token = AsyncMock(return_value=True)
        mock_cleanup_dead_websocket = AsyncMock()
        mock_performance_tracker = MagicMock()

        monitor = HealthMonitor(
            mock_is_websocket_open,
            mock_validate_token,
            mock_cleanup_dead_websocket,
            mock_performance_tracker,
        )

        mock_task = MagicMock()
        mock_task.done.return_value = False
        monitor._health_check_task = mock_task

        with patch("server.realtime.monitoring.health_monitor.logger"):
            monitor.start_periodic_checks({}, {}, {})

            # Should not create a new task
            assert monitor._health_check_task == mock_task


class TestStopPeriodicChecks:
    """Test stop_periodic_checks method."""

    def test_stop_periodic_checks_success(self) -> None:
        """Test successfully stopping periodic checks."""
        mock_is_websocket_open = MagicMock(return_value=True)
        mock_validate_token = AsyncMock(return_value=True)
        mock_cleanup_dead_websocket = AsyncMock()
        mock_performance_tracker = MagicMock()

        monitor = HealthMonitor(
            mock_is_websocket_open,
            mock_validate_token,
            mock_cleanup_dead_websocket,
            mock_performance_tracker,
        )

        mock_task = MagicMock()
        mock_task.done.return_value = False
        mock_task.cancel = MagicMock()
        monitor._health_check_task = mock_task

        with patch("server.realtime.monitoring.health_monitor.logger"):
            with patch("asyncio.get_running_loop", return_value=MagicMock()):
                with patch("asyncio.create_task"):
                    monitor.stop_periodic_checks()

                    mock_task.cancel.assert_called_once()
                    assert monitor._health_check_task is None

    def test_stop_periodic_checks_no_task(self) -> None:
        """Test stopping periodic checks when no task exists."""
        mock_is_websocket_open = MagicMock(return_value=True)
        mock_validate_token = AsyncMock(return_value=True)
        mock_cleanup_dead_websocket = AsyncMock()
        mock_performance_tracker = MagicMock()

        monitor = HealthMonitor(
            mock_is_websocket_open,
            mock_validate_token,
            mock_cleanup_dead_websocket,
            mock_performance_tracker,
        )

        monitor._health_check_task = None

        with patch("server.realtime.monitoring.health_monitor.logger"):
            monitor.stop_periodic_checks()

            # Should not raise error

    def test_stop_periodic_checks_task_done(self) -> None:
        """Test stopping periodic checks when task is already done."""
        mock_is_websocket_open = MagicMock(return_value=True)
        mock_validate_token = AsyncMock(return_value=True)
        mock_cleanup_dead_websocket = AsyncMock()
        mock_performance_tracker = MagicMock()

        monitor = HealthMonitor(
            mock_is_websocket_open,
            mock_validate_token,
            mock_cleanup_dead_websocket,
            mock_performance_tracker,
        )

        mock_task = MagicMock()
        mock_task.done.return_value = True
        monitor._health_check_task = mock_task

        with patch("server.realtime.monitoring.health_monitor.logger"):
            monitor.stop_periodic_checks()

            # Should not cancel if already done
            mock_task.cancel.assert_not_called()


class TestWaitForTaskCancellation:
    """Test _wait_for_task_cancellation method."""

    @pytest.mark.asyncio
    async def test_wait_for_task_cancellation_success(self) -> None:
        """Test successfully waiting for task cancellation."""
        mock_is_websocket_open = MagicMock(return_value=True)
        mock_validate_token = AsyncMock(return_value=True)
        mock_cleanup_dead_websocket = AsyncMock()
        mock_performance_tracker = MagicMock()

        monitor = HealthMonitor(
            mock_is_websocket_open,
            mock_validate_token,
            mock_cleanup_dead_websocket,
            mock_performance_tracker,
        )

        mock_task = AsyncMock()
        mock_task.__await__ = lambda self: iter([])  # Completed task

        with patch("server.realtime.monitoring.health_monitor.logger"):
            await monitor._wait_for_task_cancellation(mock_task)

            # Should complete without error

    @pytest.mark.asyncio
    async def test_wait_for_task_cancellation_timeout(self) -> None:
        """Test waiting for task cancellation with timeout."""
        mock_is_websocket_open = MagicMock(return_value=True)
        mock_validate_token = AsyncMock(return_value=True)
        mock_cleanup_dead_websocket = AsyncMock()
        mock_performance_tracker = MagicMock()

        monitor = HealthMonitor(
            mock_is_websocket_open,
            mock_validate_token,
            mock_cleanup_dead_websocket,
            mock_performance_tracker,
        )

        # Create a task that never completes
        async def never_complete():
            while True:
                await asyncio.sleep(1)

        task = asyncio.create_task(never_complete())

        with patch("server.realtime.monitoring.health_monitor.logger"):
            await monitor._wait_for_task_cancellation(task)

            # Should handle timeout gracefully
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                pass
