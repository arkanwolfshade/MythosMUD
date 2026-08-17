"""NATS health-check, batch flush, and subscription-lifecycle tests."""

# pylint: disable=redefined-outer-name  # Reason: pytest fixtures injected as parameters
# pylint: disable=protected-access  # Reason: tests inspect NATSService internals
# pylint: disable=duplicate-code  # Reason: sibling of test_nats_service; shared fixture/mock setup is intentional
# pyright: reportPrivateUsage=false

from __future__ import annotations

import asyncio
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.config.models import NATSConfig
from server.services.nats_service import JsonMap, NATSService


@pytest.fixture
def nats_config() -> NATSConfig:
    """Create a NATSConfig instance."""
    return NATSConfig(
        url="nats://localhost:4222",
        max_reconnect_attempts=5,
        reconnect_time_wait=2,
        ping_interval=20,
        max_outstanding_pings=2,
    )


@pytest.fixture
def nats_service(nats_config: NATSConfig) -> NATSService:
    """Create a NATSService instance."""
    return NATSService(nats_config)


@pytest.mark.asyncio
async def test_perform_health_check_success(nats_service: NATSService) -> None:
    """Test _perform_health_check() returns True when healthy."""
    mock_client = MagicMock()
    flush: AsyncMock = AsyncMock()
    mock_client.flush = flush
    nats_service.nc = mock_client
    result = await nats_service._perform_health_check()
    assert result is True
    flush.assert_awaited_once()


@pytest.mark.asyncio
async def test_perform_health_check_no_client(nats_service: NATSService) -> None:
    """Test _perform_health_check() returns False when no client."""
    nats_service.nc = None
    result = await nats_service._perform_health_check()
    assert result is False


@pytest.mark.asyncio
async def test_perform_health_check_timeout(nats_service: NATSService) -> None:
    """Test _perform_health_check() returns False on timeout."""
    mock_client = MagicMock()
    mock_client.flush = AsyncMock(side_effect=TimeoutError())
    nats_service.nc = mock_client
    result = await nats_service._perform_health_check()
    assert result is False


@pytest.mark.asyncio
async def test_perform_health_check_error(nats_service: NATSService) -> None:
    """Test _perform_health_check() returns False on error."""
    mock_client = MagicMock()
    mock_client.flush = AsyncMock(side_effect=Exception("Flush error"))
    nats_service.nc = mock_client
    result = await nats_service._perform_health_check()
    assert result is False


@pytest.mark.asyncio
async def test_cancel_background_tasks(nats_service: NATSService) -> None:
    """Test _cancel_background_tasks() cancels all tasks."""
    task1 = asyncio.create_task(asyncio.sleep(10))
    task2 = asyncio.create_task(asyncio.sleep(10))
    nats_service._background_tasks = {task1, task2}
    await nats_service._cancel_background_tasks()
    assert task1.cancelled()
    assert task2.cancelled()
    assert len(nats_service._background_tasks) == 0


@pytest.mark.asyncio
async def test_cancel_background_tasks_empty(nats_service: NATSService) -> None:
    """Test _cancel_background_tasks() handles empty task set."""
    nats_service._background_tasks = set()
    # Should not raise
    await nats_service._cancel_background_tasks()


@pytest.mark.asyncio
async def test_stop_health_monitoring(nats_service: NATSService) -> None:
    """Test _stop_health_monitoring() stops health check task."""

    # Create a real task that can be cancelled
    async def dummy_task():
        await asyncio.sleep(10)

    task = asyncio.create_task(dummy_task())
    nats_service._health_check_task = task
    await nats_service._stop_health_monitoring()
    assert task.cancelled()
    assert nats_service._health_check_task is None


@pytest.mark.asyncio
async def test_stop_health_monitoring_no_task(nats_service: NATSService) -> None:
    """Test _stop_health_monitoring() handles no task."""
    nats_service._health_check_task = None
    # Should not raise
    await nats_service._stop_health_monitoring()


@pytest.mark.asyncio
async def test_publish_batch_adds_to_batch(nats_service: NATSService) -> None:
    """Test publish_batch() adds message to batch."""
    # Disable subject validation for this test
    nats_service.config.enable_subject_validation = False
    nats_service.message_batch = []
    result = await nats_service.publish_batch("test.subject", {"key": "value"})
    assert result is True
    assert len(nats_service.message_batch) == 1
    assert nats_service.message_batch[0] == ("test.subject", {"key": "value"})


@pytest.mark.asyncio
async def test_publish_batch_flushes_when_full(nats_service: NATSService) -> None:
    """Test publish_batch() flushes when batch is full."""
    nats_service.config.enable_subject_validation = False
    nats_service.batch_size = 2
    nats_service.message_batch = [("sub1", {}), ("sub2", {})]
    with patch.object(nats_service, "_flush_batch", new_callable=AsyncMock) as mock_flush:
        _ = await nats_service.publish_batch("test.subject", {"key": "value"})
        mock_flush.assert_awaited_once()


@pytest.mark.asyncio
async def test_flush_batch_success(nats_service: NATSService) -> None:
    """Test _flush_batch() successfully flushes batch."""
    nats_service.message_batch = [("sub1", {"msg1": "data1"}), ("sub2", {"msg2": "data2"})]
    nats_service._pool_initialized = True
    mock_connection = MagicMock()
    mock_connection.publish = AsyncMock()
    nats_service.available_connections.put_nowait(mock_connection)
    with patch.object(nats_service, "publish_with_pool", new_callable=AsyncMock) as mock_publish:
        await nats_service._flush_batch()
        assert mock_publish.await_count == 2
        assert len(nats_service.message_batch) == 0


@pytest.mark.asyncio
async def test_flush_batch_empty(nats_service: NATSService) -> None:
    """Test _flush_batch() handles empty batch."""
    nats_service.message_batch = []
    # Should not raise
    await nats_service._flush_batch()


def test_get_connection_stats(nats_service: NATSService) -> None:
    """Test get_connection_stats() returns connection statistics."""
    nats_service.subscriptions = {"sub1": MagicMock(), "sub2": MagicMock()}
    nats_service._connection_retries = 3
    nats_service._running = True
    nats_service._pool_initialized = True
    stats = nats_service.get_connection_stats()
    # Check that stats contains expected keys
    assert "nats_connected" in stats
    assert "pool_initialized" in stats
    assert "pool_size" in stats
    assert "available_connections" in stats
    assert "health_check_enabled" in stats
    assert "consecutive_health_failures" in stats
    # Metrics from state machine and metrics objects
    assert "publish_count" in stats  # From metrics
    assert "connection_health" in stats  # From metrics


@pytest.mark.asyncio
async def test_disconnect_removes_all_subscriptions(nats_service: NATSService) -> None:
    """
    Test that disconnect() removes all subscriptions on service shutdown.

    Task 4-10: Verify all subscriptions are removed on service shutdown.
    """
    mock_client = MagicMock()
    mock_client.close = AsyncMock()
    mock_sub1 = MagicMock()
    mock_sub1.drain = AsyncMock()
    unsub1: AsyncMock = AsyncMock()
    mock_sub1.unsubscribe = unsub1
    mock_sub2 = MagicMock()
    mock_sub2.drain = AsyncMock()
    unsub2: AsyncMock = AsyncMock()
    mock_sub2.unsubscribe = unsub2

    nats_service.nc = mock_client
    nats_service.subscriptions = {
        "test.subject1": mock_sub1,
        "test.subject2": mock_sub2,
    }
    nats_service._running = True
    nats_service._background_tasks = set()

    # Track subscriptions before cleanup
    subscriptions_before = list(nats_service.subscriptions.keys())
    assert len(subscriptions_before) == 2

    with patch.object(nats_service, "_cancel_background_tasks", new_callable=AsyncMock):
        with patch.object(nats_service, "_cleanup_connection_pool", new_callable=AsyncMock):
            with patch.object(nats_service, "_stop_health_monitoring", new_callable=AsyncMock):
                await nats_service.disconnect()

    # Verify all subscriptions were unsubscribed
    assert unsub1.await_count == 1
    assert unsub2.await_count == 1

    # Verify subscriptions dict is cleared
    assert len(nats_service.subscriptions) == 0
    assert nats_service.get_active_subscriptions() == []


@pytest.mark.asyncio
async def test_service_restart_no_duplicate_subscriptions(nats_service: NATSService) -> None:
    """
    Test that service restart does not create duplicate subscriptions.

    Task 4-11: Verify service restart doesn't create duplicate subscriptions.
    """
    mock_client = MagicMock()
    mock_client.close = AsyncMock()

    # Create a function that returns a new mock subscription each time
    def create_mock_subscription(*_args: object, **_kwargs: object) -> MagicMock:
        return MagicMock()

    mock_client.subscribe = AsyncMock(side_effect=create_mock_subscription)

    nats_service.nc = mock_client
    nats_service._running = True
    nats_service.subscriptions = {}

    # First subscription
    async def callback1(message_data: JsonMap) -> None:
        _ = message_data

    await nats_service.subscribe("test.subject", callback1)
    assert len(nats_service.subscriptions) == 1
    assert "test.subject" in nats_service.subscriptions
    first_subscription = nats_service.subscriptions["test.subject"]

    # Disconnect (simulate shutdown)
    nats_service.subscriptions["test.subject"].drain = AsyncMock()
    nats_service.subscriptions["test.subject"].unsubscribe = AsyncMock()
    nats_service._background_tasks = set()
    with patch.object(nats_service, "_cancel_background_tasks", new_callable=AsyncMock):
        with patch.object(nats_service, "_cleanup_connection_pool", new_callable=AsyncMock):
            with patch.object(nats_service, "_stop_health_monitoring", new_callable=AsyncMock):
                await nats_service.disconnect()

    # Verify subscriptions cleared
    assert len(nats_service.subscriptions) == 0

    # Reconnect (simulate restart)
    nats_service.nc = mock_client
    nats_service._running = True

    # Subscribe again to same subject
    async def callback2(message_data: JsonMap) -> None:
        _ = message_data

    await nats_service.subscribe("test.subject", callback2)

    # Verify only one subscription exists (no duplicates)
    assert len(nats_service.subscriptions) == 1
    assert "test.subject" in nats_service.subscriptions
    # Verify it's a new subscription object (not the old one)
    assert nats_service.subscriptions["test.subject"] is not first_subscription
