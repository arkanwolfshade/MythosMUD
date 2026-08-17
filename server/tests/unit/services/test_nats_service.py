"""
Unit tests for NATS service.

Tests the NATSService class and NATSMetrics.
"""
# pylint: disable=redefined-outer-name  # Reason: Pytest fixtures are injected as function parameters
# pylint: disable=protected-access  # Reason: Tests need to access protected members to verify internal state and behavior
# pyright: reportPrivateUsage=false

import asyncio
import json
import time
from collections import deque
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.config.models import NATSConfig
from server.realtime.connection_state_machine import NATSConnectionStateMachine
from server.services.nats_exceptions import NATSPublishError, NATSSubscribeError
from server.services.nats_metrics import NATSMetrics
from server.services.nats_service import NATSService
from server.services.nats_subject_manager import NATSSubjectManager


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


def test_nats_metrics_init():
    """Test NATSMetrics initialization."""
    metrics = NATSMetrics()
    assert metrics.publish_count == 0
    assert metrics.publish_errors == 0
    assert metrics.subscribe_count == 0
    assert metrics.subscribe_errors == 0
    assert isinstance(metrics.message_processing_times, deque)
    assert metrics.connection_health_score == 100.0
    assert metrics.batch_flush_count == 0
    assert metrics.batch_flush_errors == 0
    assert metrics.pool_utilization == 0.0


def test_nats_metrics_record_publish_success():
    """Test NATSMetrics.record_publish() records successful publish."""
    metrics = NATSMetrics()
    metrics.record_publish(success=True, processing_time=0.1)
    assert metrics.publish_count == 1
    assert metrics.publish_errors == 0
    assert len(metrics.message_processing_times) == 1
    assert metrics.message_processing_times[0] == 0.1


def test_nats_metrics_record_publish_error():
    """Test NATSMetrics.record_publish() records failed publish."""
    metrics = NATSMetrics()
    metrics.record_publish(success=False, processing_time=0.1)
    assert metrics.publish_count == 1
    assert metrics.publish_errors == 1
    assert len(metrics.message_processing_times) == 1


def test_nats_metrics_record_subscribe_success():
    """Test NATSMetrics.record_subscribe() records successful subscribe."""
    metrics = NATSMetrics()
    metrics.record_subscribe(success=True)
    assert metrics.subscribe_count == 1
    assert metrics.subscribe_errors == 0


def test_nats_metrics_record_subscribe_error():
    """Test NATSMetrics.record_subscribe() records failed subscribe."""
    metrics = NATSMetrics()
    metrics.record_subscribe(success=False)
    assert metrics.subscribe_count == 1
    assert metrics.subscribe_errors == 1


def test_nats_metrics_record_batch_flush_success():
    """Test NATSMetrics.record_batch_flush() records successful flush."""
    metrics = NATSMetrics()
    metrics.record_batch_flush(success=True, _message_count=10)
    assert metrics.batch_flush_count == 1
    assert metrics.batch_flush_errors == 0


def test_nats_metrics_record_batch_flush_error():
    """Test NATSMetrics.record_batch_flush() records failed flush."""
    metrics = NATSMetrics()
    metrics.record_batch_flush(success=False, _message_count=10)
    assert metrics.batch_flush_count == 1
    assert metrics.batch_flush_errors == 1


def test_nats_metrics_update_connection_health():
    """Test NATSMetrics.update_connection_health() updates health score."""
    metrics = NATSMetrics()
    metrics.update_connection_health(75.5)
    assert metrics.connection_health_score == 75.5


def test_nats_metrics_update_connection_health_clamped():
    """Test NATSMetrics.update_connection_health() clamps values."""
    metrics = NATSMetrics()
    metrics.update_connection_health(150.0)
    assert metrics.connection_health_score == 100.0
    metrics.update_connection_health(-10.0)
    assert metrics.connection_health_score == 0.0


def test_nats_metrics_update_pool_utilization():
    """Test NATSMetrics.update_pool_utilization() updates utilization."""
    metrics = NATSMetrics()
    metrics.update_pool_utilization(0.75)
    assert metrics.pool_utilization == 0.75


def test_nats_metrics_update_pool_utilization_clamped():
    """Test NATSMetrics.update_pool_utilization() clamps values."""
    metrics = NATSMetrics()
    metrics.update_pool_utilization(1.5)
    assert metrics.pool_utilization == 1.0
    metrics.update_pool_utilization(-0.1)
    assert metrics.pool_utilization == 0.0


def test_nats_metrics_get_metrics():
    """Test NATSMetrics.get_metrics() returns comprehensive metrics."""
    metrics = NATSMetrics()
    metrics.record_publish(success=True, processing_time=0.1)
    metrics.record_publish(success=False, processing_time=0.2)
    metrics.record_subscribe(success=True)
    metrics.record_batch_flush(success=True, _message_count=5)
    metrics.update_connection_health(80.0)
    metrics.update_pool_utilization(0.6)
    result = metrics.get_metrics()
    assert result["publish_count"] == 2
    assert result["publish_error_rate"] == 0.5
    assert result["subscribe_count"] == 1
    assert result["subscribe_error_rate"] == 0.0
    assert result["connection_health"] == 80.0
    assert result["pool_utilization"] == 0.6
    assert result["batch_flush_count"] == 1
    assert "avg_processing_time_ms" in result
    assert "processing_time_samples" in result


def test_nats_metrics_get_metrics_empty_processing_times():
    """Test NATSMetrics.get_metrics() handles empty processing times."""
    metrics = NATSMetrics()
    result = metrics.get_metrics()
    assert result["avg_processing_time_ms"] == 0
    assert result["processing_time_samples"] == 0


def test_nats_metrics_message_processing_times_maxlen():
    """Test NATSMetrics message_processing_times deque has maxlen."""
    metrics = NATSMetrics()
    # Fill beyond maxlen (1000)
    for _i in range(1500):
        metrics.record_publish(success=True, processing_time=0.1)
    # Should only keep last 1000
    assert len(metrics.message_processing_times) == 1000


def test_nats_service_init_with_config(nats_config: NATSConfig) -> None:
    """Test NATSService initialization with NATSConfig."""
    service = NATSService(nats_config)
    assert service.config == nats_config
    assert service.nc is None
    assert not service.subscriptions
    assert service._running is False
    assert isinstance(service.metrics, NATSMetrics)
    assert isinstance(service.state_machine, NATSConnectionStateMachine)


def test_nats_service_init_with_dict():
    """Test NATSService initialization with dict config."""
    config_dict = {
        "url": "nats://localhost:4222",
        "max_reconnect_attempts": 3,
        "tls_enabled": False,
    }
    service = NATSService(config_dict)
    assert isinstance(service.config, NATSConfig)
    assert service.config.url == "nats://localhost:4222"
    assert service.config.max_reconnect_attempts == 3


def test_nats_service_init_with_none():
    """Test NATSService initialization with None config."""
    service = NATSService(None)
    assert isinstance(service.config, NATSConfig)


def test_nats_service_init_with_subject_manager(nats_config: NATSConfig) -> None:
    """Test NATSService initialization with subject manager."""
    subject_manager = NATSSubjectManager()
    service = NATSService(nats_config, subject_manager=subject_manager)
    assert service.subject_manager == subject_manager


def test_nats_service_init_connection_pool(nats_config: NATSConfig) -> None:
    """Test NATSService initializes connection pool structures."""
    service = NATSService(nats_config)
    assert not service.connection_pool
    assert service.pool_size == 5  # Default
    assert isinstance(service.available_connections, asyncio.Queue)
    assert service._pool_initialized is False


def test_nats_service_init_message_batch(nats_config: NATSConfig) -> None:
    """Test NATSService initializes message batching structures."""
    service = NATSService(nats_config)
    assert not service.message_batch
    assert service.batch_size == 100  # Default
    assert service.batch_timeout == 0.1  # Default 100ms


@pytest.mark.asyncio
async def test_connect_success(nats_service: NATSService) -> None:
    """Test connect() successfully connects to NATS."""
    mock_client = MagicMock()
    mock_client.is_connected = True
    mock_client.add_error_listener = MagicMock()
    mock_client.add_disconnect_listener = MagicMock()
    mock_client.add_reconnect_listener = MagicMock()
    mock_client.flush = AsyncMock()
    with patch("server.services.nats_service_connect.nats.connect", new_callable=AsyncMock, return_value=mock_client):
        with patch.object(nats_service, "_initialize_connection_pool", new_callable=AsyncMock):
            with patch.object(nats_service, "_start_health_monitoring", new_callable=AsyncMock):
                result = await nats_service.connect()
                assert result is True
                assert nats_service.nc == mock_client
                assert nats_service._running is True


@pytest.mark.asyncio
async def test_connect_state_machine_blocked(nats_service: NATSService) -> None:
    """Test connect() returns False when state machine blocks connection."""
    # Force state machine to block connection by opening circuit first
    nats_service.state_machine.max_reconnect_attempts = 1
    # Trigger a connection failure to get into reconnecting state
    with patch(
        "server.services.nats_service_connect.nats.connect",
        new_callable=AsyncMock,
        side_effect=Exception("Connection failed"),
    ):
        _ = await nats_service.connect()  # This will open circuit
    # Now try to connect again - should be blocked
    result = await nats_service.connect()
    assert result is False


@pytest.mark.asyncio
async def test_connect_failure(nats_service: NATSService) -> None:
    """Test connect() handles connection failure."""
    with patch(
        "server.services.nats_service_connect.nats.connect",
        new_callable=AsyncMock,
        side_effect=Exception("Connection failed"),
    ):
        result = await nats_service.connect()
        assert result is False
        assert nats_service._connection_retries == 1


@pytest.mark.asyncio
async def test_connect_circuit_breaker_opens(nats_service: NATSService) -> None:
    """Test connect() opens circuit breaker after max retries."""
    nats_service._max_retries = 1
    nats_service.state_machine.max_reconnect_attempts = 1
    with patch(
        "server.services.nats_service_connect.nats.connect",
        new_callable=AsyncMock,
        side_effect=Exception("Connection failed"),
    ):
        # First failure - should open circuit
        result = await nats_service.connect()
        assert result is False
        # Circuit should be open after exceeding max attempts
        assert nats_service.state_machine.state.id == "circuit_open"


@pytest.mark.asyncio
async def test_disconnect_success(nats_service: NATSService) -> None:
    """Test disconnect() successfully disconnects."""
    mock_client = MagicMock()
    mock_subscription = MagicMock()
    drain: AsyncMock = AsyncMock()
    unsub: AsyncMock = AsyncMock()
    close: AsyncMock = AsyncMock()
    mock_subscription.drain = drain
    mock_subscription.unsubscribe = unsub
    mock_client.close = close
    nats_service.nc = mock_client
    nats_service.subscriptions = {"test.subject": mock_subscription}
    nats_service._running = True
    nats_service._background_tasks = set()
    with patch.object(nats_service, "_cancel_background_tasks", new_callable=AsyncMock):
        with patch.object(nats_service, "_cleanup_connection_pool", new_callable=AsyncMock):
            with patch.object(nats_service, "_stop_health_monitoring", new_callable=AsyncMock):
                await nats_service.disconnect()
                drain.assert_awaited_once()
                unsub.assert_awaited_once()
                close.assert_awaited_once()
                assert nats_service.nc is None
                assert nats_service._running is False


@pytest.mark.asyncio
async def test_disconnect_flushes_batch(nats_service: NATSService) -> None:
    """Test disconnect() flushes pending batch."""
    nats_service.message_batch = [("test.subject", {"key": "value"})]
    nats_service.nc = None
    with patch.object(nats_service, "_flush_batch", new_callable=AsyncMock) as mock_flush:
        with patch.object(nats_service, "_cancel_background_tasks", new_callable=AsyncMock):
            await nats_service.disconnect()
            mock_flush.assert_awaited_once()


@pytest.mark.asyncio
async def test_disconnect_handles_drain_error(nats_service: NATSService) -> None:
    """Test disconnect() handles drain errors gracefully."""
    mock_client = MagicMock()
    mock_subscription = MagicMock()
    mock_subscription.drain = AsyncMock(side_effect=Exception("Drain error"))
    mock_subscription.unsubscribe = AsyncMock()
    mock_client.close = AsyncMock()
    nats_service.nc = mock_client
    nats_service.subscriptions = {"test.subject": mock_subscription}
    nats_service._background_tasks = set()
    with patch.object(nats_service, "_cancel_background_tasks", new_callable=AsyncMock):
        with patch.object(nats_service, "_cleanup_connection_pool", new_callable=AsyncMock):
            with patch.object(nats_service, "_stop_health_monitoring", new_callable=AsyncMock):
                # Should not raise
                await nats_service.disconnect()


@pytest.mark.asyncio
async def test_publish_not_initialized(nats_service: NATSService) -> None:
    """Test publish() raises error when pool not initialized."""
    with pytest.raises(NATSPublishError, match="Connection pool not initialized"):
        await nats_service.publish("test.subject", {"key": "value"})


@pytest.mark.asyncio
async def test_publish_no_available_connections(nats_service: NATSService) -> None:
    """Test publish() raises error when no connections available after waiting for pool_wait_timeout."""
    nats_service._pool_initialized = True
    nats_service.config.pool_wait_timeout = 0.01  # Short timeout so test does not block
    # available_connections is empty; no other task will return a connection
    with pytest.raises(NATSPublishError, match="No available connections in pool"):
        await nats_service.publish("test.subject", {"key": "value"})


@pytest.mark.asyncio
async def test_publish_success(nats_service: NATSService) -> None:
    """Test publish() successfully publishes using pool."""
    nats_service._pool_initialized = True
    mock_connection = MagicMock()
    mock_connection.publish = AsyncMock()
    nats_service.available_connections.put_nowait(mock_connection)
    with patch.object(nats_service, "publish_with_pool", new_callable=AsyncMock) as mock_publish:
        await nats_service.publish("test.subject", {"key": "value"})
        mock_publish.assert_awaited_once_with("test.subject", {"key": "value"})


@pytest.mark.asyncio
async def test_subscribe_not_connected(nats_service: NATSService) -> None:
    """Test subscribe() raises error when not connected."""
    nats_service.nc = None
    callback = AsyncMock()
    with pytest.raises(NATSSubscribeError, match="NATS client not connected"):
        await nats_service.subscribe("test.subject", callback)


@pytest.mark.asyncio
async def test_subscribe_not_running(nats_service: NATSService) -> None:
    """Test subscribe() raises error when not running."""
    mock_client = MagicMock()
    nats_service.nc = mock_client
    nats_service._running = False
    callback = AsyncMock()
    with pytest.raises(NATSSubscribeError, match="NATS client not connected"):
        await nats_service.subscribe("test.subject", callback)


@pytest.mark.asyncio
async def test_subscribe_success(nats_service: NATSService) -> None:
    """Test subscribe() successfully subscribes."""
    mock_client = MagicMock()
    mock_subscription = MagicMock()
    client_subscribe: AsyncMock = AsyncMock(return_value=mock_subscription)
    mock_client.subscribe = client_subscribe
    nats_service.nc = mock_client
    nats_service._running = True
    callback = AsyncMock()
    await nats_service.subscribe("test.subject", callback)
    assert "test.subject" in nats_service.subscriptions
    client_subscribe.assert_awaited_once()


@pytest.mark.asyncio
async def test_subscribe_with_manual_ack(nats_service: NATSService) -> None:
    """Test subscribe() handles manual acknowledgment."""
    mock_client = MagicMock()
    mock_subscription = MagicMock()
    mock_client.subscribe = AsyncMock(return_value=mock_subscription)
    nats_service.nc = mock_client
    nats_service._running = True
    nats_service.config.manual_ack = True
    callback = AsyncMock()
    await nats_service.subscribe("test.subject", callback)
    # Verify subscription was created
    assert "test.subject" in nats_service.subscriptions


@pytest.mark.asyncio
async def test_unsubscribe_success(nats_service: NATSService) -> None:
    """Test unsubscribe() successfully unsubscribes."""

    mock_subscription = MagicMock()
    unsub: AsyncMock = AsyncMock()
    mock_subscription.unsubscribe = unsub
    nats_service.subscriptions = {"test.subject": mock_subscription}
    await nats_service.unsubscribe("test.subject")
    assert "test.subject" not in nats_service.subscriptions
    unsub.assert_awaited_once()


@pytest.mark.asyncio
async def test_unsubscribe_not_found(nats_service: NATSService) -> None:
    """Test unsubscribe() raises NATSUnsubscribeError when subscription not found."""
    from server.services.nats_exceptions import NATSUnsubscribeError

    nats_service.subscriptions = {}
    with pytest.raises(NATSUnsubscribeError):
        await nats_service.unsubscribe("test.subject")


@pytest.mark.asyncio
async def test_unsubscribe_error(nats_service: NATSService) -> None:
    """Test unsubscribe() raises NATSUnsubscribeError on unsubscribe errors."""
    from server.services.nats_exceptions import NATSUnsubscribeError

    mock_subscription = MagicMock()
    mock_subscription.unsubscribe = AsyncMock(side_effect=Exception("Unsubscribe error"))
    nats_service.subscriptions = {"test.subject": mock_subscription}
    with pytest.raises(NATSUnsubscribeError):
        await nats_service.unsubscribe("test.subject")


@pytest.mark.asyncio
async def test_request_success(nats_service: NATSService) -> None:
    """Test request() successfully sends request and receives reply."""
    mock_client = MagicMock()
    mock_client.is_connected = True
    mock_reply = MagicMock()
    mock_reply.data = json.dumps({"reply": "data"}).encode("utf-8")
    mock_client.request = AsyncMock(return_value=mock_reply)
    nats_service.nc = mock_client
    nats_service._running = True
    nats_service.config.health_check_interval = 0  # Disable health check for simpler test
    reply = await nats_service.request("test.subject", {"request": "data"}, timeout=1.0)
    assert reply == {"reply": "data"}


@pytest.mark.asyncio
async def test_request_not_connected(nats_service: NATSService) -> None:
    """Test request() raises NATSRequestError when not connected."""
    from server.services.nats_exceptions import NATSRequestError

    nats_service.nc = None
    with pytest.raises(NATSRequestError):
        _ = await nats_service.request("test.subject", {"request": "data"})


@pytest.mark.asyncio
async def test_request_timeout(nats_service: NATSService) -> None:
    """Test request() raises NATSRequestError on timeout."""
    from server.services.nats_exceptions import NATSRequestError

    mock_client = MagicMock()
    mock_client.is_connected = True
    mock_client.request = AsyncMock(side_effect=TimeoutError())
    nats_service.nc = mock_client
    nats_service._running = True
    nats_service.config.health_check_interval = 0  # Disable health check for simpler test
    with pytest.raises(NATSRequestError):
        _ = await nats_service.request("test.subject", {"request": "data"}, timeout=0.1)


@pytest.mark.asyncio
async def test_request_error(nats_service: NATSService) -> None:
    """Test request() raises NATSRequestError on errors."""
    from server.services.nats_exceptions import NATSRequestError

    mock_client = MagicMock()
    mock_client.is_connected = True
    mock_client.request = AsyncMock(side_effect=Exception("Request error"))
    nats_service.nc = mock_client
    nats_service._running = True
    nats_service.config.health_check_interval = 0  # Disable health check for simpler test
    with pytest.raises(NATSRequestError):
        _ = await nats_service.request("test.subject", {"request": "data"})


@pytest.mark.asyncio
async def test_is_connected_true(nats_service: NATSService) -> None:
    """Test is_connected() returns True when connected."""
    mock_client = MagicMock()
    mock_client.is_connected = True
    nats_service.nc = mock_client
    nats_service._running = True
    nats_service._last_health_check = time.monotonic()  # Recent health check (matches service)
    nats_service.config.health_check_interval = 0  # Disable health check for simpler test
    assert nats_service.is_connected() is True


def test_is_connected_false(nats_service: NATSService) -> None:
    """Test is_connected() returns False when not connected."""
    nats_service.nc = None
    assert nats_service.is_connected() is False


def test_get_subscription_count(nats_service: NATSService) -> None:
    """Test get_subscription_count() returns correct count."""
    nats_service.subscriptions = {"sub1": MagicMock(), "sub2": MagicMock(), "sub3": MagicMock()}
    assert nats_service.get_subscription_count() == 3
