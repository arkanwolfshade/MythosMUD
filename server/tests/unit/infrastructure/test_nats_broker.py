"""
Tests for NATS MessageBroker implementation.

This module tests the concrete NATS implementation of the MessageBroker protocol,
ensuring proper integration with the NATS messaging system while maintaining
independence from actual NATS infrastructure during testing.

AI Agent: Tests for NATSMessageBroker covering initialization, connection management,
         error handling, and basic protocol operations with mocked NATS client.
"""

# pylint: disable=redefined-outer-name,protected-access
# Justification: pytest fixtures redefine names, protected access needed for testing internals

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.config.models import NATSConfig
from server.infrastructure.message_broker import (
    ConnectionError as BrokerConnectionError,
)
from server.infrastructure.message_broker import (
    PublishError,
    RequestError,
    SubscribeError,
)
from server.infrastructure.nats_broker import NATSMessageBroker


@pytest.fixture
def nats_config():
    """Provide NATS configuration for testing."""
    return NATSConfig(
        url="nats://localhost:4222",
        max_reconnect_attempts=3,
        reconnect_time_wait=1,
        ping_interval=30,
        max_outstanding_pings=5,
    )


@pytest.fixture
def nats_broker(nats_config):  # pylint: disable=redefined-outer-name
    """Provide NATSMessageBroker instance for testing."""
    return NATSMessageBroker(nats_config)


class TestNATSMessageBrokerInit:
    """Test NATSMessageBroker initialization."""

    def test_initialization(self, nats_config):
        """Test broker initializes with correct configuration."""
        broker = NATSMessageBroker(nats_config)

        assert broker.config == nats_config
        assert broker._client is None
        assert not broker._subscriptions
        assert broker._logger is not None

    def test_config_attributes_accessible(self, nats_broker):
        """Test configuration attributes are accessible."""
        assert nats_broker.config.url == "nats://localhost:4222"
        assert nats_broker.config.max_reconnect_attempts == 3
        assert nats_broker.config.reconnect_time_wait == 1


class TestNATSMessageBrokerConnection:
    """Test NATS connection management."""

    @pytest.mark.asyncio
    async def test_is_connected_when_not_connected(self, nats_broker):
        """Test is_connected returns False when client is None."""
        assert not nats_broker.is_connected()

    @pytest.mark.asyncio
    async def test_is_connected_when_client_exists_but_disconnected(self, nats_broker):
        """Test is_connected returns False when client exists but not connected."""
        mock_client = MagicMock()
        mock_client.is_connected = False
        nats_broker._client = mock_client

        assert not nats_broker.is_connected()

    @pytest.mark.asyncio
    async def test_is_connected_when_connected(self, nats_broker):
        """Test is_connected returns True when client is connected."""
        mock_client = MagicMock()
        mock_client.is_connected = True
        nats_broker._client = mock_client

        assert nats_broker.is_connected()

    @pytest.mark.asyncio
    @patch("server.infrastructure.nats_broker.nats.connect")
    async def test_connect_success(self, mock_nats_connect, nats_broker):
        """Test successful connection to NATS."""
        mock_client = AsyncMock()
        mock_client.is_connected = True
        mock_nats_connect.return_value = mock_client

        result = await nats_broker.connect()

        assert result is True
        assert nats_broker._client is not None
        mock_nats_connect.assert_called_once()

    @pytest.mark.asyncio
    @patch("server.infrastructure.nats_broker.nats.connect")
    async def test_connect_already_connected(self, mock_nats_connect, nats_broker):
        """Test connect returns True when already connected."""
        mock_client = AsyncMock()
        mock_client.is_connected = True
        nats_broker._client = mock_client

        result = await nats_broker.connect()

        assert result is True
        mock_nats_connect.assert_not_called()

    @pytest.mark.asyncio
    @patch("server.infrastructure.nats_broker.nats.connect")
    async def test_connect_failure_raises_connection_error(self, mock_nats_connect, nats_broker):
        """Test connection failure raises ConnectionError."""
        mock_nats_connect.side_effect = Exception("Connection failed")

        with pytest.raises(BrokerConnectionError) as exc_info:
            await nats_broker.connect()

        assert "Failed to connect to NATS" in str(exc_info.value)
        assert "Connection failed" in str(exc_info.value)

    @pytest.mark.asyncio
    async def test_disconnect_when_not_connected(self, nats_broker):
        """Test disconnect does nothing when client is None."""
        # Should not raise exception
        await nats_broker.disconnect()
        assert nats_broker._client is None

    @pytest.mark.asyncio
    async def test_disconnect_success(self, nats_broker):
        """Test successful disconnection from NATS."""
        mock_client = AsyncMock()
        mock_client.is_connected = True
        nats_broker._client = mock_client

        await nats_broker.disconnect()

        mock_client.close.assert_called_once()


class TestNATSMessageBrokerPublish:
    """Test NATS message publishing."""

    @pytest.mark.asyncio
    async def test_publish_when_not_connected_raises_error(self, nats_broker):
        """Test publish raises PublishError when not connected."""
        with pytest.raises(PublishError) as exc_info:
            await nats_broker.publish("test.subject", {"data": "test"})

        assert "Not connected to NATS" in str(exc_info.value)

    @pytest.mark.asyncio
    async def test_publish_success(self, nats_broker):
        """Test successful message publishing."""
        mock_client = AsyncMock()
        mock_client.is_connected = True
        nats_broker._client = mock_client

        await nats_broker.publish("test.subject", {"data": "test"})

        mock_client.publish.assert_called_once()
        call_args = mock_client.publish.call_args
        assert call_args[0][0] == "test.subject"
        assert b"test" in call_args[0][1]


class TestNATSMessageBrokerSubscribe:
    """Test NATS subscription management."""

    @pytest.mark.asyncio
    async def test_subscribe_when_not_connected_raises_error(self, nats_broker):
        """Test subscribe raises SubscribeError when not connected."""
        handler = AsyncMock()

        with pytest.raises(SubscribeError) as exc_info:
            await nats_broker.subscribe("test.subject", handler)

        assert "Not connected to NATS" in str(exc_info.value)


class TestNATSMessageBrokerUnsubscribe:
    """Test NATS unsubscription."""

    @pytest.mark.asyncio
    async def test_unsubscribe_nonexistent_subscription_logs_warning(self, nats_broker):
        """Test unsubscribe with nonexistent subscription logs warning but doesn't raise."""
        # Should not raise exception
        await nats_broker.unsubscribe("nonexistent-id")

        # Verify no subscriptions were affected
        assert len(nats_broker._subscriptions) == 0


class TestNATSMessageBrokerRequest:
    """Test NATS request-reply pattern."""

    @pytest.mark.asyncio
    async def test_request_when_not_connected_raises_error(self, nats_broker):
        """Test request raises RequestError when not connected."""
        with pytest.raises(RequestError) as exc_info:
            await nats_broker.request("test.subject", {"query": "test"})

        assert "Not connected to NATS" in str(exc_info.value)


class TestNATSMessageBrokerCallbacks:
    """Test NATS event callbacks."""

    @pytest.mark.asyncio
    async def test_error_callback(self, nats_broker):
        """Test error callback logs error."""
        error = Exception("Test error")

        # Should not raise exception
        await nats_broker._error_callback(error)

    @pytest.mark.asyncio
    async def test_disconnected_callback(self, nats_broker):
        """Test disconnected callback logs warning."""
        # Should not raise exception
        await nats_broker._disconnected_callback()

    @pytest.mark.asyncio
    async def test_reconnected_callback(self, nats_broker):
        """Test reconnected callback logs info."""
        # Should not raise exception
        await nats_broker._reconnected_callback()
