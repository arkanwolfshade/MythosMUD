"""
Tests for the NATS service module.

This module tests the NATSService class which handles all NATS pub/sub operations
and real-time messaging for the chat system.
"""

import asyncio
import json
from unittest.mock import AsyncMock, Mock, patch

import pytest

from server.services.nats_service import NATSService, nats_service


class TestNATSService:
    """Test cases for NATSService class."""

    def setup_method(self):
        """Set up test fixtures."""
        # Create a mock NATS client
        self.mock_nats_client = Mock()
        self.mock_nats_client.publish = AsyncMock()
        self.mock_nats_client.subscribe = AsyncMock()
        self.mock_nats_client.request = AsyncMock()
        self.mock_nats_client.close = AsyncMock()
        self.mock_nats_client.add_error_listener = Mock()
        self.mock_nats_client.add_disconnect_listener = Mock()
        self.mock_nats_client.add_reconnect_listener = Mock()

        # Create the service instance with test configuration
        self.nats_service = NATSService(
            {
                "url": "nats://localhost:4222",
                "max_reconnect_attempts": 3,
                "connect_timeout": 5,
            }
        )

        # Test data - using standardized subject format
        self.test_subject = "chat.say.room.room_001"  # Updated to match standardized pattern
        self.test_data = {
            "message_id": "test_message_123",
            "sender_id": "test_sender",
            "sender_name": "TestPlayer",
            "channel": "say",
            "content": "Hello, world!",
            "timestamp": "2024-01-01T12:00:00Z",
            "room_id": "room_001",
        }

    def test_nats_service_initialization(self):
        """Test NATSService initialization."""
        assert self.nats_service.nc is None
        assert self.nats_service.subscriptions == {}
        assert self.nats_service._running is False
        assert self.nats_service._connection_retries == 0
        assert self.nats_service._max_retries == 3
        # Verify background tasks tracking is initialized
        assert hasattr(self.nats_service, "_background_tasks")
        assert isinstance(self.nats_service._background_tasks, set)

    def test_nats_service_initialization_with_config(self):
        """Test NATSService initialization with custom config."""
        config = {
            "url": "nats://test-server:4222",
            "max_reconnect_attempts": 10,
            "connect_timeout": 10,
        }

        service = NATSService(config)

        # Config is converted to NATSConfig Pydantic model
        assert service.config.url == "nats://test-server:4222"
        assert service.config.max_reconnect_attempts == 10
        assert service.config.connect_timeout == 10
        assert service._max_retries == 10

    @pytest.mark.asyncio
    async def test_connect_success(self):
        """Test successful NATS connection."""
        # Mock nats.connect to return our mock client
        with patch("nats.connect", new_callable=AsyncMock) as mock_connect:
            mock_connect.return_value = self.mock_nats_client

            # Execute
            result = await self.nats_service.connect()

            # Verify
            assert result is True
            assert self.nats_service.nc == self.mock_nats_client
            assert self.nats_service._running is True
            assert self.nats_service._connection_retries == 0

            # Verify connection was called (may be called multiple times due to state machine)
            assert mock_connect.call_count >= 1
            # Check that at least one call was made with the correct URL
            call_args_list = mock_connect.call_args_list
            url_calls = [call for call in call_args_list if call[0][0] == "nats://localhost:4222"]
            assert len(url_calls) >= 1

    @pytest.mark.asyncio
    async def test_connect_with_custom_url(self):
        """Test NATS connection with custom URL."""
        config = {"url": "nats://custom-server:4222"}
        service = NATSService(config)

        with patch("nats.connect", new_callable=AsyncMock) as mock_connect:
            mock_connect.return_value = self.mock_nats_client

            # Execute
            result = await service.connect()

            # Verify
            assert result is True
            assert mock_connect.call_count >= 1
            # Check that at least one call was made with the correct URL
            call_args_list = mock_connect.call_args_list
            url_calls = [call for call in call_args_list if call[0][0] == "nats://custom-server:4222"]
            assert len(url_calls) >= 1

    @pytest.mark.asyncio
    async def test_connect_with_custom_options(self):
        """Test NATS connection with custom options."""
        config = {
            "reconnect_time_wait": 2,
            "max_reconnect_attempts": 10,
            "connect_timeout": 10,
            "ping_interval": 60,
            "max_outstanding_pings": 10,
        }
        service = NATSService(config)

        with patch("nats.connect", new_callable=AsyncMock) as mock_connect:
            mock_connect.return_value = self.mock_nats_client

            # Execute
            result = await service.connect()

            # Verify
            assert result is True
            assert mock_connect.call_count >= 1
            # Check that at least one call was made with the correct options
            call_args_list = mock_connect.call_args_list
            for call in call_args_list:
                if len(call[1]) > 0:  # Check keyword arguments
                    call_kwargs = call[1]
                    if "reconnect_time_wait" in call_kwargs:
                        assert call_kwargs["reconnect_time_wait"] == 2
                        assert call_kwargs["max_reconnect_attempts"] == 10
                        assert call_kwargs["connect_timeout"] == 10
                        assert call_kwargs["ping_interval"] == 60
                        assert call_kwargs["max_outstanding_pings"] == 10
                        break

    @pytest.mark.asyncio
    async def test_connect_failure(self):
        """Test NATS connection failure."""
        with patch("nats.connect", new_callable=AsyncMock) as mock_connect:
            mock_connect.side_effect = Exception("Connection failed")

            # Execute
            result = await self.nats_service.connect()

            # Verify
            assert result is False
            assert self.nats_service._connection_retries == 1
            assert self.nats_service._running is False

    @pytest.mark.asyncio
    async def test_connect_with_event_listeners(self):
        """Test NATS connection with event listeners."""
        with patch("nats.connect", new_callable=AsyncMock) as mock_connect:
            mock_connect.return_value = self.mock_nats_client

            # Execute
            result = await self.nats_service.connect()

            # Verify
            assert result is True
            self.mock_nats_client.add_error_listener.assert_called_once()
            self.mock_nats_client.add_disconnect_listener.assert_called_once()
            self.mock_nats_client.add_reconnect_listener.assert_called_once()

    @pytest.mark.asyncio
    async def test_connect_with_event_listeners_not_available(self):
        """Test NATS connection when event listeners are not available."""
        # Mock NATS client without event listener methods
        mock_client_no_listeners = Mock()
        mock_client_no_listeners.publish = AsyncMock()
        mock_client_no_listeners.subscribe = AsyncMock()
        mock_client_no_listeners.request = AsyncMock()
        mock_client_no_listeners.close = AsyncMock()
        # Don't add the event listener methods

        with patch("nats.connect", new_callable=AsyncMock) as mock_connect:
            mock_connect.return_value = mock_client_no_listeners

            # Execute - should not raise exception
            result = await self.nats_service.connect()

            # Verify
            assert result is True

    @pytest.mark.asyncio
    async def test_disconnect_success(self):
        """Test successful NATS disconnection."""
        # Setup connected state
        self.nats_service.nc = self.mock_nats_client
        self.nats_service._running = True
        self.nats_service.subscriptions = {"test_subject": Mock()}

        # Execute
        await self.nats_service.disconnect()

        # Verify
        self.mock_nats_client.close.assert_called_once()
        assert self.nats_service.nc is None
        assert self.nats_service.subscriptions == {}
        assert self.nats_service._running is False

    @pytest.mark.asyncio
    async def test_disconnect_not_connected(self):
        """Test disconnection when not connected."""
        # Execute - should not raise exception
        await self.nats_service.disconnect()

        # Verify no calls were made
        self.mock_nats_client.close.assert_not_called()

    @pytest.mark.asyncio
    async def test_disconnect_with_subscription_errors(self):
        """Test disconnection with subscription unsubscribe errors."""
        # Setup connected state with subscription that raises error
        mock_subscription = Mock()
        mock_subscription.unsubscribe = AsyncMock(side_effect=Exception("Unsubscribe failed"))

        self.nats_service.nc = self.mock_nats_client
        self.nats_service._running = True
        self.nats_service.subscriptions = {"test_subject": mock_subscription}

        # Execute - should not raise exception
        await self.nats_service.disconnect()

        # Verify
        self.mock_nats_client.close.assert_called_once()
        assert self.nats_service.nc is None
        assert self.nats_service.subscriptions == {}
        assert self.nats_service._running is False

    @pytest.mark.asyncio
    async def test_publish_success(self):
        """Test successful message publishing."""
        # Setup connected state and connection pool
        self.nats_service.nc = self.mock_nats_client
        self.nats_service._running = True
        self.nats_service._pool_initialized = True
        # Add mock connection to pool queue
        await self.nats_service.available_connections.put(self.mock_nats_client)
        self.nats_service.connection_pool.append(self.mock_nats_client)

        # Execute
        await self.nats_service.publish(self.test_subject, self.test_data)

        # Verify
        self.mock_nats_client.publish.assert_called_once()

        # Verify the published data
        call_args = self.mock_nats_client.publish.call_args
        assert call_args[0][0] == self.test_subject
        published_data = json.loads(call_args[0][1].decode("utf-8"))
        assert published_data == self.test_data

    @pytest.mark.asyncio
    async def test_publish_not_connected(self):
        """Test publishing when not connected."""
        # Execute - should raise NATSPublishError when pool not initialized
        from server.services.nats_exceptions import NATSPublishError

        with pytest.raises(NATSPublishError, match="Connection pool not initialized"):
            await self.nats_service.publish(self.test_subject, self.test_data)

        # Verify
        self.mock_nats_client.publish.assert_not_called()

    @pytest.mark.asyncio
    async def test_publish_exception(self):
        """Test publishing when an exception occurs."""
        # Setup connected state and connection pool
        self.nats_service.nc = self.mock_nats_client
        self.nats_service._running = True
        self.nats_service._pool_initialized = True
        # Add mock connection to pool queue
        await self.nats_service.available_connections.put(self.mock_nats_client)
        self.nats_service.connection_pool.append(self.mock_nats_client)
        self.mock_nats_client.publish.side_effect = Exception("Publish failed")

        # Execute - should raise NATSPublishError when exception occurs
        from server.services.nats_exceptions import NATSPublishError

        with pytest.raises(NATSPublishError):
            await self.nats_service.publish(self.test_subject, self.test_data)

    @pytest.mark.asyncio
    async def test_subscribe_success(self):
        """Test successful subscription."""
        # Setup connected state
        self.nats_service.nc = self.mock_nats_client
        self.nats_service._running = True

        mock_subscription = Mock()
        self.mock_nats_client.subscribe.return_value = mock_subscription

        # Test callback
        callback_called = False

        def test_callback(data):
            nonlocal callback_called
            callback_called = True
            assert data == self.test_data

        # Execute - subscribe now returns None, not True
        await self.nats_service.subscribe(self.test_subject, test_callback)

        # Verify
        assert self.test_subject in self.nats_service.subscriptions
        assert self.nats_service.subscriptions[self.test_subject] == mock_subscription

    @pytest.mark.asyncio
    async def test_subscribe_not_connected(self):
        """Test subscription when not connected."""
        from server.services.nats_exceptions import NATSSubscribeError

        def test_callback(data):
            pass

        # Execute - should raise NATSSubscribeError when not connected
        with pytest.raises(NATSSubscribeError, match="NATS client not connected"):
            await self.nats_service.subscribe(self.test_subject, test_callback)

        # Verify
        assert self.test_subject not in self.nats_service.subscriptions

    @pytest.mark.asyncio
    async def test_subscribe_exception(self):
        """Test subscription when an exception occurs."""
        from server.services.nats_exceptions import NATSSubscribeError

        # Setup connected state
        self.nats_service.nc = self.mock_nats_client
        self.nats_service._running = True
        self.mock_nats_client.subscribe.side_effect = Exception("Subscribe failed")

        def test_callback(data):
            pass

        # Execute - should raise NATSSubscribeError when exception occurs
        with pytest.raises(NATSSubscribeError, match="Failed to subscribe to NATS subject"):
            await self.nats_service.subscribe(self.test_subject, test_callback)

    @pytest.mark.asyncio
    async def test_subscribe_with_async_callback(self):
        """Test subscription with async callback."""
        # Setup connected state
        self.nats_service.nc = self.mock_nats_client
        self.nats_service._running = True

        mock_subscription = Mock()
        self.mock_nats_client.subscribe.return_value = mock_subscription

        # Test async callback
        callback_called = False

        async def test_async_callback(data):
            nonlocal callback_called
            callback_called = True
            assert data == self.test_data

        # Execute - subscribe now returns None, not True
        await self.nats_service.subscribe(self.test_subject, test_async_callback)

        # Verify
        assert self.test_subject in self.nats_service.subscriptions

    @pytest.mark.asyncio
    async def test_subscribe_message_handler_json_decode_error(self):
        """Test subscription message handler with JSON decode error."""
        # Setup connected state
        self.nats_service.nc = self.mock_nats_client
        self.nats_service._running = True

        mock_subscription = Mock()
        self.mock_nats_client.subscribe.return_value = mock_subscription

        def test_callback(data):
            pass

        # Execute - subscribe now returns None, not True
        await self.nats_service.subscribe(self.test_subject, test_callback)

        # Verify subscription was created
        assert self.test_subject in self.nats_service.subscriptions

        # Get the message handler that was registered
        message_handler = self.mock_nats_client.subscribe.call_args[1]["cb"]

        # Create a mock message with invalid JSON
        mock_msg = Mock()
        mock_msg.data = b"invalid json"

        # Execute message handler - should not raise exception
        await message_handler(mock_msg)

    @pytest.mark.asyncio
    async def test_subscribe_message_handler_callback_exception(self):
        """Test subscription message handler when callback raises exception."""
        # Setup connected state
        self.nats_service.nc = self.mock_nats_client
        self.nats_service._running = True

        mock_subscription = Mock()
        self.mock_nats_client.subscribe.return_value = mock_subscription

        def test_callback(data):
            raise Exception("Callback error")

        # Execute - subscribe returns None, but should not raise exception
        result = await self.nats_service.subscribe(self.test_subject, test_callback)

        # Verify subscription was registered
        assert result is None
        assert self.mock_nats_client.subscribe.called

        # Get the message handler that was registered
        message_handler = self.mock_nats_client.subscribe.call_args[1]["cb"]

        # Create a mock message
        mock_msg = Mock()
        mock_msg.data = json.dumps(self.test_data).encode("utf-8")

        # Execute message handler - should not raise exception
        await message_handler(mock_msg)

    @pytest.mark.asyncio
    async def test_unsubscribe_success(self):
        """Test successful unsubscription."""
        # Setup connected state with subscription
        mock_subscription = Mock()
        mock_subscription.unsubscribe = AsyncMock()

        self.nats_service.nc = self.mock_nats_client
        self.nats_service._running = True
        self.nats_service.subscriptions[self.test_subject] = mock_subscription

        # Execute
        result = await self.nats_service.unsubscribe(self.test_subject)

        # Verify
        assert result is True
        mock_subscription.unsubscribe.assert_called_once()
        assert self.test_subject not in self.nats_service.subscriptions

    @pytest.mark.asyncio
    async def test_unsubscribe_not_subscribed(self):
        """Test unsubscription when not subscribed."""
        # Execute
        result = await self.nats_service.unsubscribe(self.test_subject)

        # Verify
        assert result is False

    @pytest.mark.asyncio
    async def test_unsubscribe_exception(self):
        """Test unsubscription when an exception occurs."""
        # Setup connected state with subscription
        mock_subscription = Mock()
        mock_subscription.unsubscribe = AsyncMock(side_effect=Exception("Unsubscribe failed"))

        self.nats_service.nc = self.mock_nats_client
        self.nats_service._running = True
        self.nats_service.subscriptions[self.test_subject] = mock_subscription

        # Execute
        result = await self.nats_service.unsubscribe(self.test_subject)

        # Verify
        assert result is False

    @pytest.mark.asyncio
    async def test_request_success(self):
        """Test successful request/response."""
        # Setup connected state
        self.nats_service.nc = self.mock_nats_client
        self.nats_service._running = True

        # Mock response
        mock_response = Mock()
        mock_response.data = json.dumps({"response": "success"}).encode("utf-8")
        self.mock_nats_client.request.return_value = mock_response

        # Execute
        result = await self.nats_service.request(self.test_subject, self.test_data, timeout=5.0)

        # Verify
        assert result == {"response": "success"}
        self.mock_nats_client.request.assert_called_once()

        # Verify the request data
        call_args = self.mock_nats_client.request.call_args
        assert call_args[0][0] == self.test_subject
        request_data = json.loads(call_args[0][1].decode("utf-8"))
        assert request_data == self.test_data
        assert call_args[1]["timeout"] == 5.0

    @pytest.mark.asyncio
    async def test_request_not_connected(self):
        """Test request when not connected."""
        # Execute
        result = await self.nats_service.request(self.test_subject, self.test_data)

        # Verify
        assert result is None
        self.mock_nats_client.request.assert_not_called()

    @pytest.mark.asyncio
    async def test_request_timeout(self):
        """Test request with timeout."""
        # Setup connected state
        self.nats_service.nc = self.mock_nats_client
        self.nats_service._running = True
        self.mock_nats_client.request.side_effect = TimeoutError("Request timeout")

        # Execute
        result = await self.nats_service.request(self.test_subject, self.test_data, timeout=1.0)

        # Verify
        assert result is None

    @pytest.mark.asyncio
    async def test_request_exception(self):
        """Test request when an exception occurs."""
        # Setup connected state
        self.nats_service.nc = self.mock_nats_client
        self.nats_service._running = True
        self.mock_nats_client.request.side_effect = Exception("Request failed")

        # Execute
        result = await self.nats_service.request(self.test_subject, self.test_data)

        # Verify
        assert result is None

    @pytest.mark.asyncio
    async def test_request_json_decode_error(self):
        """Test request with JSON decode error in response."""
        # Setup connected state
        self.nats_service.nc = self.mock_nats_client
        self.nats_service._running = True

        # Mock response with invalid JSON
        mock_response = Mock()
        mock_response.data = b"invalid json"
        self.mock_nats_client.request.return_value = mock_response

        # Execute
        result = await self.nats_service.request(self.test_subject, self.test_data)

        # Verify
        assert result is None

    def test_is_connected_true(self):
        """Test is_connected when connected."""
        # Setup connected state
        self.nats_service.nc = self.mock_nats_client
        self.nats_service._running = True

        # Execute
        result = self.nats_service.is_connected()

        # Verify
        assert result is True

    def test_is_connected_false_no_client(self):
        """Test is_connected when no client."""
        # Execute
        result = self.nats_service.is_connected()

        # Verify
        assert result is False

    def test_is_connected_false_not_running(self):
        """Test is_connected when not running."""
        # Setup client but not running
        self.nats_service.nc = self.mock_nats_client
        self.nats_service._running = False

        # Execute
        result = self.nats_service.is_connected()

        # Verify
        assert result is False

    def test_get_subscription_count(self):
        """Test getting subscription count."""
        # Setup subscriptions
        self.nats_service.subscriptions = {
            "subject1": Mock(),
            "subject2": Mock(),
            "subject3": Mock(),
        }

        # Execute
        result = self.nats_service.get_subscription_count()

        # Verify
        assert result == 3

    def test_get_subscription_count_empty(self):
        """Test getting subscription count when empty."""
        # Execute
        result = self.nats_service.get_subscription_count()

        # Verify
        assert result == 0

    def test_on_error(self):
        """Test error event handler."""
        # Execute - should not raise exception
        self.nats_service._on_error("Test error")

    def test_on_disconnect(self):
        """Test disconnect event handler."""
        # Setup running state
        self.nats_service._running = True

        # Execute
        self.nats_service._on_disconnect()

        # Verify
        assert self.nats_service._running is False

    def test_on_reconnect(self):
        """Test reconnect event handler."""
        # Setup state
        self.nats_service._running = False
        self.nats_service._connection_retries = 5

        # Execute
        self.nats_service._on_reconnect()

        # Verify
        assert self.nats_service._running is True
        assert self.nats_service._connection_retries == 0

    @pytest.mark.asyncio
    async def test_background_task_cleanup_on_disconnect(self):
        """
        Test that NATS service properly cleans up background tasks on disconnect.

        AnyIO Pattern: All tracked background tasks should be cancelled and cleaned up
        during service shutdown.
        """
        service = NATSService(
            {
                "url": "nats://localhost:4222",
                "max_reconnect_attempts": 3,
                "connect_timeout": 5,
            }
        )

        # Create some background tasks manually to test cleanup
        async def background_task():
            await asyncio.sleep(10)  # Long-running task

        # Create tracked tasks
        task1 = service._create_tracked_task(background_task(), task_name="test_task_1")
        task2 = service._create_tracked_task(background_task(), task_name="test_task_2")

        # Verify tasks are tracked
        assert len(service._background_tasks) == 2
        assert task1 in service._background_tasks
        assert task2 in service._background_tasks

        # Disconnect should cancel all background tasks
        await service.disconnect()

        # Wait a bit for cancellation to complete
        await asyncio.sleep(0.1)

        # Background tasks should be cancelled and cleaned up
        assert len(service._background_tasks) == 0
        assert task1.done()
        assert task2.done()


class TestGlobalNATSService:
    """Test cases for the global NATS service instance."""

    def test_global_nats_service_instance(self):
        """Test that the global NATS service instance exists."""
        assert isinstance(nats_service, NATSService)
        assert nats_service.nc is None
        assert nats_service.subscriptions == {}
        assert nats_service._running is False
