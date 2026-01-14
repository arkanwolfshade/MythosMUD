"""
Unit tests for NATS message broker.

Tests the NATSMessageBroker class.
"""

import json
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.config.models import NATSConfig
from server.infrastructure.message_broker import (
    MessageBrokerConnectionError,
    MessageBrokerError,
    PublishError,
    RequestError,
    SubscribeError,
    UnsubscribeError,
)
from server.infrastructure.nats_broker import NATSMessageBroker


@pytest.fixture
def nats_config():
    """Create a NATSConfig instance."""
    return NATSConfig(
        url="nats://localhost:4222",
        max_reconnect_attempts=5,
        reconnect_time_wait=2.0,
        ping_interval=20,
        max_outstanding_pings=2,
        enable_subject_validation=False,  # Disable for unit tests to allow test subjects
    )


@pytest.fixture
def nats_broker(nats_config):
    """Create a NATSMessageBroker instance."""
    # Disable message validation for unit tests to allow simple test messages
    return NATSMessageBroker(nats_config, enable_message_validation=False)


def test_nats_message_broker_init(nats_broker, nats_config):
    """Test NATSMessageBroker initialization."""
    assert nats_broker.config == nats_config
    assert nats_broker._client is None
    assert nats_broker._subscriptions == {}


@pytest.mark.asyncio
async def test_connect_success(nats_broker):
    """Test connect() successfully connects to NATS."""
    mock_client = MagicMock()
    mock_client.is_connected = True
    with patch("server.infrastructure.nats_broker.nats.connect", new_callable=AsyncMock, return_value=mock_client):
        # Mock health monitoring to prevent it from starting during test
        with patch.object(nats_broker, "_start_health_monitoring", new_callable=AsyncMock):
            result = await nats_broker.connect()
            assert result is True
            assert nats_broker._client == mock_client


@pytest.mark.asyncio
async def test_connect_already_connected(nats_broker):
    """Test connect() returns True when already connected."""
    mock_client = MagicMock()
    mock_client.is_connected = True
    nats_broker._client = mock_client
    result = await nats_broker.connect()
    assert result is True


@pytest.mark.asyncio
async def test_connect_failure(nats_broker):
    """Test connect() raises ConnectionError on failure."""
    with patch(
        "server.infrastructure.nats_broker.nats.connect",
        new_callable=AsyncMock,
        side_effect=Exception("Connection failed"),
    ):
        with pytest.raises(MessageBrokerConnectionError, match="Failed to connect to NATS"):
            await nats_broker.connect()


@pytest.mark.asyncio
async def test_connect_sets_callbacks(nats_broker):
    """Test connect() sets error, disconnect, and reconnect callbacks."""
    mock_client = MagicMock()
    mock_client.is_connected = True
    with patch(
        "server.infrastructure.nats_broker.nats.connect", new_callable=AsyncMock, return_value=mock_client
    ) as mock_connect:
        # Mock health monitoring to prevent it from starting during test
        with patch.object(nats_broker, "_start_health_monitoring", new_callable=AsyncMock):
            await nats_broker.connect()
            call_kwargs = mock_connect.call_args[1]
            assert "error_cb" in call_kwargs
            assert "disconnected_cb" in call_kwargs
            assert "reconnected_cb" in call_kwargs


@pytest.mark.asyncio
async def test_disconnect_no_client(nats_broker):
    """Test disconnect() does nothing when no client."""
    await nats_broker.disconnect()  # Should not raise


@pytest.mark.asyncio
async def test_disconnect_success(nats_broker):
    """Test disconnect() successfully disconnects."""
    mock_client = MagicMock()
    mock_client.is_connected = True
    mock_client.close = AsyncMock()
    nats_broker._client = mock_client
    await nats_broker.disconnect()
    mock_client.close.assert_awaited_once()


@pytest.mark.asyncio
async def test_disconnect_unsubscribes_all(nats_broker):
    """Test disconnect() unsubscribes from all subscriptions."""
    mock_client = MagicMock()
    mock_client.is_connected = True
    mock_client.close = AsyncMock()
    nats_broker._client = mock_client
    mock_sub1 = MagicMock()
    mock_sub1.unsubscribe = AsyncMock()
    mock_sub2 = MagicMock()
    mock_sub2.unsubscribe = AsyncMock()
    nats_broker._subscriptions = {"sub1": mock_sub1, "sub2": mock_sub2}
    await nats_broker.disconnect()
    mock_sub1.unsubscribe.assert_awaited_once()
    mock_sub2.unsubscribe.assert_awaited_once()
    assert len(nats_broker._subscriptions) == 0


@pytest.mark.asyncio
async def test_disconnect_handles_unsubscribe_error(nats_broker):
    """Test disconnect() handles unsubscribe errors gracefully."""
    mock_client = MagicMock()
    mock_client.is_connected = True
    mock_client.close = AsyncMock()
    nats_broker._client = mock_client
    mock_sub = MagicMock()
    mock_sub.unsubscribe = AsyncMock(side_effect=Exception("Unsubscribe error"))
    nats_broker._subscriptions = {"sub1": mock_sub}
    # Should not raise, just log warning
    await nats_broker.disconnect()


@pytest.mark.asyncio
async def test_disconnect_error_handling(nats_broker):
    """Test disconnect() raises MessageBrokerError on disconnect failure."""
    mock_client = MagicMock()
    mock_client.is_connected = True
    mock_client.close = AsyncMock(side_effect=Exception("Close error"))
    nats_broker._client = mock_client
    with pytest.raises(MessageBrokerError, match="Error disconnecting from NATS"):
        await nats_broker.disconnect()


def test_is_connected_true(nats_broker):
    """Test is_connected() returns True when connected."""
    mock_client = MagicMock()
    mock_client.is_connected = True
    nats_broker._client = mock_client
    nats_broker._running = True
    nats_broker._last_health_check = 0  # Initialize health check timestamp
    assert nats_broker.is_connected() is True


def test_is_connected_false_no_client(nats_broker):
    """Test is_connected() returns False when no client."""
    assert nats_broker.is_connected() is False


def test_is_connected_false_not_connected(nats_broker):
    """Test is_connected() returns False when client not connected."""
    mock_client = MagicMock()
    mock_client.is_connected = False
    nats_broker._client = mock_client
    assert nats_broker.is_connected() is False


@pytest.mark.asyncio
async def test_publish_success(nats_broker):
    """Test publish() successfully publishes message."""
    mock_client = MagicMock()
    mock_client.is_connected = True
    mock_client.publish = AsyncMock()
    nats_broker._client = mock_client
    nats_broker._running = True
    nats_broker._last_health_check = 0  # Initialize health check timestamp
    message = {"key": "value"}
    await nats_broker.publish("test.subject", message)
    mock_client.publish.assert_awaited_once()
    call_args = mock_client.publish.call_args
    assert call_args[0][0] == "test.subject"
    assert json.loads(call_args[0][1].decode("utf-8")) == message


@pytest.mark.asyncio
async def test_publish_not_connected(nats_broker):
    """Test publish() raises PublishError when not connected."""
    with pytest.raises(PublishError, match="Not connected to NATS"):
        await nats_broker.publish("test.subject", {"key": "value"})


@pytest.mark.asyncio
async def test_publish_failure(nats_broker):
    """Test publish() raises PublishError on failure."""
    mock_client = MagicMock()
    mock_client.is_connected = True
    mock_client.publish = AsyncMock(side_effect=Exception("Publish failed"))
    nats_broker._client = mock_client
    nats_broker._running = True
    nats_broker._last_health_check = 0  # Initialize health check timestamp
    with pytest.raises(PublishError, match="Failed to publish to test.subject"):
        await nats_broker.publish("test.subject", {"key": "value"})


@pytest.mark.asyncio
async def test_publish_json_serialization(nats_broker):
    """Test publish() handles JSON serialization."""
    mock_client = MagicMock()
    mock_client.is_connected = True
    mock_client.publish = AsyncMock()
    nats_broker._client = mock_client
    nats_broker._running = True
    nats_broker._last_health_check = 0  # Initialize health check timestamp
    message = {"nested": {"key": "value"}, "list": [1, 2, 3]}
    await nats_broker.publish("test.subject", message)
    call_args = mock_client.publish.call_args
    decoded = json.loads(call_args[0][1].decode("utf-8"))
    assert decoded == message


@pytest.mark.asyncio
async def test_subscribe_success(nats_broker):
    """Test subscribe() successfully subscribes."""
    mock_client = MagicMock()
    mock_client.is_connected = True
    mock_subscription = MagicMock()
    mock_client.subscribe = AsyncMock(return_value=mock_subscription)
    nats_broker._client = mock_client
    nats_broker._running = True
    nats_broker._last_health_check = 0  # Initialize health check timestamp
    handler = AsyncMock()
    subscription_id = await nats_broker.subscribe("test.subject", handler)
    assert subscription_id in nats_broker._subscriptions
    assert nats_broker._subscriptions[subscription_id] == mock_subscription
    mock_client.subscribe.assert_awaited_once()


@pytest.mark.asyncio
async def test_subscribe_with_queue_group(nats_broker):
    """Test subscribe() subscribes with queue group."""
    mock_client = MagicMock()
    mock_client.is_connected = True
    mock_subscription = MagicMock()
    mock_client.subscribe = AsyncMock(return_value=mock_subscription)
    nats_broker._client = mock_client
    nats_broker._running = True
    nats_broker._last_health_check = 0  # Initialize health check timestamp
    handler = AsyncMock()
    await nats_broker.subscribe("test.subject", handler, queue_group="workers")
    call_args = mock_client.subscribe.call_args
    assert call_args[1]["queue"] == "workers"


@pytest.mark.asyncio
async def test_subscribe_without_queue_group(nats_broker):
    """Test subscribe() uses empty string when queue_group is None."""
    mock_client = MagicMock()
    mock_client.is_connected = True
    mock_subscription = MagicMock()
    mock_client.subscribe = AsyncMock(return_value=mock_subscription)
    nats_broker._client = mock_client
    nats_broker._running = True
    nats_broker._last_health_check = 0  # Initialize health check timestamp
    handler = AsyncMock()
    await nats_broker.subscribe("test.subject", handler, queue_group=None)
    call_args = mock_client.subscribe.call_args
    assert call_args[1]["queue"] == ""


@pytest.mark.asyncio
async def test_subscribe_not_connected(nats_broker):
    """Test subscribe() raises SubscribeError when not connected."""
    handler = AsyncMock()
    with pytest.raises(SubscribeError, match="Not connected to NATS"):
        await nats_broker.subscribe("test.subject", handler)


@pytest.mark.asyncio
async def test_subscribe_failure(nats_broker):
    """Test subscribe() raises SubscribeError on failure."""
    mock_client = MagicMock()
    mock_client.is_connected = True
    mock_client.subscribe = AsyncMock(side_effect=Exception("Subscribe failed"))
    nats_broker._client = mock_client
    nats_broker._running = True
    nats_broker._last_health_check = 0  # Initialize health check timestamp
    handler = AsyncMock()
    with pytest.raises(SubscribeError, match="Failed to subscribe to test.subject"):
        await nats_broker.subscribe("test.subject", handler)


@pytest.mark.asyncio
async def test_subscribe_message_wrapper_calls_handler(nats_broker):
    """Test subscribe() message wrapper calls handler with decoded message."""
    mock_client = MagicMock()
    mock_client.is_connected = True
    mock_subscription = MagicMock()
    mock_client.subscribe = AsyncMock(return_value=mock_subscription)
    nats_broker._client = mock_client
    nats_broker._running = True
    nats_broker._last_health_check = 0  # Initialize health check timestamp
    handler = AsyncMock()
    await nats_broker.subscribe("test.subject", handler)
    # Get the wrapper function
    call_args = mock_client.subscribe.call_args
    wrapper = call_args[1]["cb"]
    # Create mock NATS message
    mock_msg = MagicMock()
    mock_msg.subject = "test.subject"
    mock_msg.data = json.dumps({"key": "value"}).encode("utf-8")
    await wrapper(mock_msg)
    handler.assert_awaited_once_with({"key": "value"})


@pytest.mark.asyncio
async def test_subscribe_message_wrapper_handles_error(nats_broker):
    """Test subscribe() message wrapper handles handler errors."""
    mock_client = MagicMock()
    mock_client.is_connected = True
    mock_subscription = MagicMock()
    mock_client.subscribe = AsyncMock(return_value=mock_subscription)
    nats_broker._client = mock_client
    nats_broker._running = True
    nats_broker._last_health_check = 0  # Initialize health check timestamp
    handler = AsyncMock(side_effect=ValueError("Handler error"))
    await nats_broker.subscribe("test.subject", handler)
    # Get the wrapper function
    call_args = mock_client.subscribe.call_args
    wrapper = call_args[1]["cb"]
    # Create mock NATS message
    mock_msg = MagicMock()
    mock_msg.subject = "test.subject"
    mock_msg.data = json.dumps({"key": "value"}).encode("utf-8")
    # Should not raise, just log error
    await wrapper(mock_msg)


@pytest.mark.asyncio
async def test_unsubscribe_success(nats_broker):
    """Test unsubscribe() successfully unsubscribes."""
    mock_subscription = MagicMock()
    mock_subscription.unsubscribe = AsyncMock()
    nats_broker._subscriptions = {"sub1": mock_subscription}
    await nats_broker.unsubscribe("sub1")
    mock_subscription.unsubscribe.assert_awaited_once()
    assert "sub1" not in nats_broker._subscriptions


@pytest.mark.asyncio
async def test_unsubscribe_not_found(nats_broker):
    """Test unsubscribe() handles subscription not found."""
    nats_broker._subscriptions = {}
    # Should not raise, just log warning
    await nats_broker.unsubscribe("nonexistent")


@pytest.mark.asyncio
async def test_unsubscribe_failure(nats_broker):
    """Test unsubscribe() raises UnsubscribeError on failure."""
    mock_subscription = MagicMock()
    mock_subscription.unsubscribe = AsyncMock(side_effect=Exception("Unsubscribe failed"))
    nats_broker._subscriptions = {"sub1": mock_subscription}
    with pytest.raises(UnsubscribeError, match="Failed to unsubscribe sub1"):
        await nats_broker.unsubscribe("sub1")


@pytest.mark.asyncio
async def test_request_success(nats_broker):
    """Test request() successfully sends request and receives reply."""
    mock_client = MagicMock()
    mock_client.is_connected = True
    mock_reply = MagicMock()
    mock_reply.data = json.dumps({"reply": "data"}).encode("utf-8")
    mock_client.request = AsyncMock(return_value=mock_reply)
    nats_broker._client = mock_client
    nats_broker._running = True
    nats_broker._last_health_check = 0  # Initialize health check timestamp
    request_message = {"request": "data"}
    reply = await nats_broker.request("test.subject", request_message, timeout=1.0)
    assert reply == {"reply": "data"}
    mock_client.request.assert_awaited_once()
    call_args = mock_client.request.call_args
    assert call_args[0][0] == "test.subject"
    assert json.loads(call_args[0][1].decode("utf-8")) == request_message


@pytest.mark.asyncio
async def test_request_not_connected(nats_broker):
    """Test request() raises RequestError when not connected."""
    with pytest.raises(RequestError, match="Not connected to NATS"):
        await nats_broker.request("test.subject", {"key": "value"})


@pytest.mark.asyncio
async def test_request_timeout(nats_broker):
    """Test request() raises TimeoutError on timeout."""
    mock_client = MagicMock()
    mock_client.is_connected = True
    mock_client.request = AsyncMock(side_effect=TimeoutError())
    nats_broker._client = mock_client
    nats_broker._running = True
    nats_broker._last_health_check = 0  # Initialize health check timestamp
    with pytest.raises(TimeoutError, match="Request to test.subject timed out"):
        await nats_broker.request("test.subject", {"key": "value"}, timeout=0.1)


@pytest.mark.asyncio
async def test_request_failure(nats_broker):
    """Test request() raises RequestError on failure."""
    mock_client = MagicMock()
    mock_client.is_connected = True
    mock_client.request = AsyncMock(side_effect=Exception("Request failed"))
    nats_broker._client = mock_client
    nats_broker._running = True
    nats_broker._last_health_check = 0  # Initialize health check timestamp
    with pytest.raises(RequestError, match="Request to test.subject failed"):
        await nats_broker.request("test.subject", {"key": "value"})


@pytest.mark.asyncio
async def test_error_callback(nats_broker):
    """Test _error_callback() logs error."""
    error = Exception("Test error")
    # _error_callback is a sync wrapper that creates an async task
    # Call the async handler directly instead
    with patch.object(nats_broker._logger, "error") as mock_log:
        await nats_broker._handle_error_async(error)
        mock_log.assert_called_once()


@pytest.mark.asyncio
async def test_disconnected_callback(nats_broker):
    """Test _disconnected_callback() logs warning."""
    # _disconnected_callback is a sync wrapper that creates an async task
    # Call the async handler directly instead
    with patch.object(nats_broker._logger, "warning") as mock_log:
        await nats_broker._handle_disconnect_async()
        mock_log.assert_called_once()


@pytest.mark.asyncio
async def test_reconnected_callback(nats_broker):
    """Test _reconnected_callback() logs info."""
    # _reconnected_callback is a sync wrapper that creates an async task
    # Call the async handler directly instead
    # Mock health monitoring to prevent it from starting and logging
    with patch.object(nats_broker, "_start_health_monitoring", new_callable=AsyncMock):
        with patch.object(nats_broker._logger, "info") as mock_log:
            await nats_broker._handle_reconnect_async()
            # Check that "Reconnected to NATS" was logged
            mock_log.assert_any_call("Reconnected to NATS")


@pytest.mark.asyncio
async def test_subscribe_message_wrapper_invalid_json(nats_broker):
    """Test subscribe() message wrapper handles invalid JSON."""
    mock_client = MagicMock()
    mock_client.is_connected = True
    mock_subscription = MagicMock()
    mock_client.subscribe = AsyncMock(return_value=mock_subscription)
    nats_broker._client = mock_client
    nats_broker._running = True
    nats_broker._last_health_check = 0  # Initialize health check timestamp
    handler = AsyncMock()
    await nats_broker.subscribe("test.subject", handler)
    # Get the wrapper function
    call_args = mock_client.subscribe.call_args
    wrapper = call_args[1]["cb"]
    # Create mock NATS message with invalid JSON
    mock_msg = MagicMock()
    mock_msg.subject = "test.subject"
    mock_msg.data = b"invalid json"
    # Should not raise, just log error
    await wrapper(mock_msg)
    handler.assert_not_awaited()
