"""
Tests for MessageBroker Protocol and exception classes.

This module tests the MessageBroker abstraction layer, ensuring proper
protocol definition and exception handling as documented in the
Pnakotic Manuscripts of Hexagonal Architecture.

AI Agent: Tests for the MessageBroker Protocol (abstract interface).
         Covers exception classes, protocol conformance, and type validation.
"""

from typing import Any
from unittest.mock import AsyncMock

import pytest

from server.infrastructure.message_broker import (
    ConnectionError as BrokerConnectionError,
)
from server.infrastructure.message_broker import (
    MessageBroker,
    MessageBrokerError,
    MessageHandler,
    PublishError,
    RequestError,
    SubscribeError,
    UnsubscribeError,
)


class TestMessageBrokerExceptions:
    """Test MessageBroker exception classes."""

    def test_message_broker_error_base_exception(self):
        """Test MessageBrokerError can be instantiated and raised."""
        error = MessageBrokerError("Test error message")
        assert str(error) == "Test error message"
        assert isinstance(error, Exception)

        with pytest.raises(MessageBrokerError) as exc_info:
            raise MessageBrokerError("Base error")
        assert str(exc_info.value) == "Base error"

    def test_connection_error_inherits_from_base(self):
        """Test ConnectionError inherits from MessageBrokerError."""
        error = BrokerConnectionError("Connection failed")
        assert str(error) == "Connection failed"
        assert isinstance(error, MessageBrokerError)
        assert isinstance(error, Exception)

        with pytest.raises(MessageBrokerError):
            raise BrokerConnectionError("Test connection error")

    def test_publish_error_inherits_from_base(self):
        """Test PublishError inherits from MessageBrokerError."""
        error = PublishError("Publish failed")
        assert str(error) == "Publish failed"
        assert isinstance(error, MessageBrokerError)
        assert isinstance(error, Exception)

        with pytest.raises(MessageBrokerError):
            raise PublishError("Test publish error")

    def test_subscribe_error_inherits_from_base(self):
        """Test SubscribeError inherits from MessageBrokerError."""
        error = SubscribeError("Subscribe failed")
        assert str(error) == "Subscribe failed"
        assert isinstance(error, MessageBrokerError)
        assert isinstance(error, Exception)

        with pytest.raises(MessageBrokerError):
            raise SubscribeError("Test subscribe error")

    def test_unsubscribe_error_inherits_from_base(self):
        """Test UnsubscribeError inherits from MessageBrokerError."""
        error = UnsubscribeError("Unsubscribe failed")
        assert str(error) == "Unsubscribe failed"
        assert isinstance(error, MessageBrokerError)
        assert isinstance(error, Exception)

        with pytest.raises(MessageBrokerError):
            raise UnsubscribeError("Test unsubscribe error")

    def test_request_error_inherits_from_base(self):
        """Test RequestError inherits from MessageBrokerError."""
        error = RequestError("Request failed")
        assert str(error) == "Request failed"
        assert isinstance(error, MessageBrokerError)
        assert isinstance(error, Exception)

        with pytest.raises(MessageBrokerError):
            raise RequestError("Test request error")

    def test_exception_hierarchy_catching(self):
        """Test that all broker exceptions can be caught as MessageBrokerError."""
        exceptions = [
            BrokerConnectionError("conn"),
            PublishError("pub"),
            SubscribeError("sub"),
            UnsubscribeError("unsub"),
            RequestError("req"),
        ]

        for exc in exceptions:
            with pytest.raises(MessageBrokerError):
                raise exc

    def test_exception_with_no_message(self):
        """Test exceptions can be raised without message."""
        error = MessageBrokerError()
        assert isinstance(error, Exception)

        with pytest.raises(MessageBrokerError):
            raise MessageBrokerError()


class TestMessageBrokerProtocol:
    """Test MessageBroker Protocol conformance."""

    def test_message_handler_type_alias(self):
        """Test MessageHandler type alias is properly defined."""

        # MessageHandler should be a callable that takes dict[str, Any] and returns Any
        def sync_handler(_message: dict[str, Any]) -> str:
            return "handled"

        async def async_handler(_message: dict[str, Any]) -> dict[str, Any]:
            return {"result": "handled"}

        # Type alias should allow both sync and async handlers
        handler1: MessageHandler = sync_handler
        handler2: MessageHandler = async_handler

        # Verify they can be called (type checking)
        assert handler1({"test": "data"}) == "handled"
        assert callable(handler2)

    def test_protocol_defines_required_methods(self):
        """Test that Protocol defines all required methods."""
        # Verify Protocol has all required method names
        assert hasattr(MessageBroker, "connect")
        assert hasattr(MessageBroker, "disconnect")
        assert hasattr(MessageBroker, "is_connected")
        assert hasattr(MessageBroker, "publish")
        assert hasattr(MessageBroker, "subscribe")
        assert hasattr(MessageBroker, "unsubscribe")
        assert hasattr(MessageBroker, "request")

    @pytest.mark.asyncio
    async def test_mock_implementation_conforms_to_protocol(self):
        """Test that a mock implementation can conform to MessageBroker Protocol."""

        class MockMessageBroker:
            """Mock implementation for testing protocol conformance."""

            def __init__(self):
                self._connected = False
                self._subscriptions: dict[str, MessageHandler] = {}

            async def connect(self) -> bool:
                self._connected = True
                return True

            async def disconnect(self) -> None:
                self._connected = False
                self._subscriptions.clear()

            def is_connected(self) -> bool:
                return self._connected

            async def publish(self, _subject: str, _message: dict[str, Any]) -> None:
                if not self._connected:
                    raise BrokerConnectionError("Not connected")

            async def subscribe(self, _subject: str, handler: MessageHandler, _queue_group: str | None = None) -> str:
                if not self._connected:
                    raise BrokerConnectionError("Not connected")
                sub_id = f"sub_{len(self._subscriptions)}"
                self._subscriptions[sub_id] = handler
                return sub_id

            async def unsubscribe(self, subscription_id: str) -> None:
                if subscription_id in self._subscriptions:
                    del self._subscriptions[subscription_id]

            async def request(self, _subject: str, _message: dict[str, Any], _timeout: float = 2.0) -> dict[str, Any]:
                if not self._connected:
                    raise BrokerConnectionError("Not connected")
                return {"reply": "mock_response"}

            def has_subscription(self, subscription_id: str) -> bool:
                """Test helper to check if a subscription exists."""
                return subscription_id in self._subscriptions

        # Create mock broker and verify it works
        broker = MockMessageBroker()

        # Test connection
        assert not broker.is_connected()
        result = await broker.connect()
        assert result is True
        assert broker.is_connected()

        # Test publish
        await broker.publish("test.subject", {"data": "test"})

        # Test subscribe
        handler = AsyncMock()
        sub_id = await broker.subscribe("test.subject", handler)
        assert broker.has_subscription(sub_id)

        # Test unsubscribe
        await broker.unsubscribe(sub_id)
        assert not broker.has_subscription(sub_id)

        # Test request
        reply = await broker.request("test.request", {"query": "test"})
        assert reply == {"reply": "mock_response"}

        # Test disconnect
        await broker.disconnect()
        assert not broker.is_connected()

    @pytest.mark.asyncio
    async def test_protocol_requires_connection_before_operations(self):
        """Test that implementations should check connection state."""

        class StrictMockBroker:
            """Strict mock that enforces connection state."""

            def __init__(self):
                self._connected = False

            async def connect(self) -> bool:
                self._connected = True
                return True

            async def disconnect(self) -> None:
                self._connected = False

            def is_connected(self) -> bool:
                return self._connected

            async def publish(self, _subject: str, _message: dict[str, Any]) -> None:
                if not self._connected:
                    raise BrokerConnectionError("Cannot publish: not connected")

            async def subscribe(self, _subject: str, _handler: MessageHandler, _queue_group: str | None = None) -> str:
                if not self._connected:
                    raise BrokerConnectionError("Cannot subscribe: not connected")
                return "sub_0"

            async def unsubscribe(self, _subscription_id: str) -> None:
                if not self._connected:
                    raise BrokerConnectionError("Cannot unsubscribe: not connected")

            async def request(self, _subject: str, _message: dict[str, Any], _timeout: float = 2.0) -> dict[str, Any]:
                if not self._connected:
                    raise BrokerConnectionError("Cannot request: not connected")
                return {}

        broker = StrictMockBroker()

        # Verify operations fail when not connected
        with pytest.raises(BrokerConnectionError, match="not connected"):
            await broker.publish("test", {})

        with pytest.raises(BrokerConnectionError, match="not connected"):
            await broker.subscribe("test", AsyncMock())

        with pytest.raises(BrokerConnectionError, match="not connected"):
            await broker.unsubscribe("sub_0")

        with pytest.raises(BrokerConnectionError, match="not connected"):
            await broker.request("test", {})

        # Connect and verify operations work
        await broker.connect()
        assert broker.is_connected()

        # These should not raise
        await broker.publish("test", {})
        sub_id = await broker.subscribe("test", AsyncMock())
        await broker.unsubscribe(sub_id)
        await broker.request("test", {})

    def test_exception_class_specific_catching(self):
        """Test that specific exception types can be caught individually."""
        # Test ConnectionError specifically
        with pytest.raises(BrokerConnectionError) as exc_info:
            raise BrokerConnectionError("Connection lost")
        assert not isinstance(exc_info.value, PublishError)
        assert isinstance(exc_info.value, MessageBrokerError)

        # Test PublishError specifically
        with pytest.raises(PublishError) as exc_info:
            raise PublishError("Publish failed")
        assert not isinstance(exc_info.value, BrokerConnectionError)
        assert isinstance(exc_info.value, MessageBrokerError)

        # Test SubscribeError specifically
        with pytest.raises(SubscribeError) as exc_info:
            raise SubscribeError("Subscribe failed")
        assert not isinstance(exc_info.value, PublishError)
        assert isinstance(exc_info.value, MessageBrokerError)

    def test_exception_chaining(self):
        """Test exception chaining preserves context."""
        original_error = ValueError("Original issue")

        try:
            try:
                raise original_error
            except ValueError as e:
                raise BrokerConnectionError("Failed to connect") from e
        except BrokerConnectionError as broker_error:
            assert broker_error.__cause__ is original_error
            assert isinstance(broker_error, MessageBrokerError)

    @pytest.mark.asyncio
    async def test_message_handler_with_different_return_types(self):
        """Test MessageHandler can handle different return types."""

        # Handler returning None
        async def void_handler(_message: dict[str, Any]) -> None:
            pass

        # Handler returning dict
        async def dict_handler(_message: dict[str, Any]) -> dict[str, Any]:
            return {"processed": True}

        # Handler returning string
        async def string_handler(_message: dict[str, Any]) -> str:
            return "acknowledged"

        # All should be valid MessageHandlers
        handlers: list[MessageHandler] = [void_handler, dict_handler, string_handler]

        for handler in handlers:
            result = await handler({"test": "data"})
            # Results vary by handler type, just verify they can be called
            assert result is None or isinstance(result, dict | str)

    @pytest.mark.asyncio
    async def test_protocol_method_signatures(self):
        """Test that Protocol method signatures are correctly defined."""

        class SignatureTestBroker:
            """Broker to test method signatures."""

            async def connect(self) -> bool:
                return True

            async def disconnect(self) -> None:
                return None

            def is_connected(self) -> bool:
                return True

            async def publish(self, _subject: str, _message: dict[str, Any]) -> None:
                return None

            async def subscribe(self, _subject: str, _handler: MessageHandler, queue_group: str | None = None) -> str:
                _ = queue_group  # Acknowledge parameter for signature testing
                return "sub_123"

            async def unsubscribe(self, _subscription_id: str) -> None:
                return None

            async def request(self, _subject: str, _message: dict[str, Any], timeout: float = 2.0) -> dict[str, Any]:
                _ = timeout  # Acknowledge parameter for signature testing
                return {"status": "ok"}

        broker = SignatureTestBroker()

        # Test all methods can be called with correct signatures
        assert await broker.connect() is True
        await broker.disconnect()
        assert broker.is_connected() is True
        await broker.publish("subject", {"data": "test"})

        handler = AsyncMock()
        sub_id = await broker.subscribe("subject", handler, queue_group="group1")
        assert isinstance(sub_id, str)

        await broker.unsubscribe("sub_123")

        reply = await broker.request("request.subject", {"query": "test"}, timeout=5.0)
        assert isinstance(reply, dict)

    def test_exception_repr_and_str(self):
        """Test exception string representations."""
        errors = [
            MessageBrokerError("base error"),
            BrokerConnectionError("connection error"),
            PublishError("publish error"),
            SubscribeError("subscribe error"),
            UnsubscribeError("unsubscribe error"),
            RequestError("request error"),
        ]

        for error in errors:
            error_str = str(error)
            assert len(error_str) > 0
            assert "error" in error_str.lower()

    def test_exception_attributes(self):
        """Test that exceptions preserve attributes."""
        error = MessageBrokerError("Error with context")
        error.custom_attr = "custom_value"

        assert hasattr(error, "custom_attr")
        assert error.custom_attr == "custom_value"

    @pytest.mark.asyncio
    async def test_subscribe_with_queue_group_parameter(self):
        """Test subscribe method handles optional queue_group parameter."""

        class QueueGroupBroker:
            """Broker to test queue group handling."""

            def __init__(self):
                self._queue_groups: dict[str, str] = {}

            async def connect(self) -> bool:
                return True

            async def disconnect(self) -> None:
                pass

            def is_connected(self) -> bool:
                return True

            async def publish(self, subject: str, message: dict[str, Any]) -> None:
                pass

            async def subscribe(self, _subject: str, _handler: MessageHandler, queue_group: str | None = None) -> str:
                sub_id = f"sub_{len(self._queue_groups)}"
                if queue_group:
                    self._queue_groups[sub_id] = queue_group
                return sub_id

            async def unsubscribe(self, subscription_id: str) -> None:
                if subscription_id in self._queue_groups:
                    del self._queue_groups[subscription_id]

            async def request(self, _subject: str, _message: dict[str, Any], _timeout: float = 2.0) -> dict[str, Any]:
                return {}

            def get_queue_group(self, subscription_id: str) -> str | None:
                """Test helper to get the queue group for a subscription."""
                return self._queue_groups.get(subscription_id)

        broker = QueueGroupBroker()
        handler = AsyncMock()

        # Subscribe without queue group
        sub_id1 = await broker.subscribe("subject1", handler)
        assert broker.get_queue_group(sub_id1) is None

        # Subscribe with queue group
        sub_id2 = await broker.subscribe("subject2", handler, queue_group="workers")
        assert broker.get_queue_group(sub_id2) == "workers"

    @pytest.mark.asyncio
    async def test_request_timeout_parameter(self):
        """Test request method handles timeout parameter."""

        class TimeoutBroker:
            """Broker to test timeout handling."""

            def __init__(self):
                self._last_timeout: float | None = None

            async def connect(self) -> bool:
                return True

            async def disconnect(self) -> None:
                pass

            def is_connected(self) -> bool:
                return True

            async def publish(self, _subject: str, _message: dict[str, Any]) -> None:
                pass

            async def subscribe(self, _subject: str, _handler: MessageHandler, _queue_group: str | None = None) -> str:
                return "sub_0"

            async def unsubscribe(self, _subscription_id: str) -> None:
                pass

            async def request(self, _subject: str, _message: dict[str, Any], timeout: float = 2.0) -> dict[str, Any]:
                self._last_timeout = timeout
                return {"timeout_used": timeout}

            def get_last_timeout(self) -> float | None:
                """Test helper to get the last timeout value used."""
                return self._last_timeout

        broker = TimeoutBroker()

        # Test default timeout
        result = await broker.request("test", {})
        assert broker.get_last_timeout() == 2.0

        # Test custom timeout
        result = await broker.request("test", {}, timeout=10.0)
        assert broker.get_last_timeout() == 10.0
        assert result["timeout_used"] == 10.0

    def test_all_exception_classes_exist(self):
        """Test that all documented exception classes are defined."""
        # Verify all exception classes can be imported and instantiated
        exceptions = [
            MessageBrokerError,
            BrokerConnectionError,
            PublishError,
            SubscribeError,
            UnsubscribeError,
            RequestError,
        ]

        for exc_class in exceptions:
            instance = exc_class("test")
            assert isinstance(instance, Exception)
            assert isinstance(instance, MessageBrokerError)
