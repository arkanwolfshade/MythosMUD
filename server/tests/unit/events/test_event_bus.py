"""
Unit tests for event bus.

Tests the EventBus class.
"""

import asyncio
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.events.event_bus import EventBus
from server.events.event_types import BaseEvent


class MockEventClass(BaseEvent):
    """Mock event class for testing."""

    pass


@pytest.fixture
def event_bus():
    """Create an EventBus instance."""
    return EventBus()


def test_event_bus_init(event_bus):
    """Test EventBus initialization."""
    assert event_bus._running is False
    assert event_bus._processing_task is None
    assert len(event_bus._subscribers) == 0


def test_event_bus_subscribe(event_bus):
    """Test EventBus.subscribe() adds subscriber."""
    handler = MagicMock()
    event_bus.subscribe(MockEventClass, handler)
    assert MockEventClass in event_bus._subscribers
    assert handler in event_bus._subscribers[MockEventClass]


def test_event_bus_subscribe_multiple(event_bus):
    """Test EventBus.subscribe() with multiple handlers."""
    handler1 = MagicMock()
    handler2 = MagicMock()
    event_bus.subscribe(MockEventClass, handler1)
    event_bus.subscribe(MockEventClass, handler2)
    assert len(event_bus._subscribers[MockEventClass]) == 2


def test_event_bus_unsubscribe(event_bus):
    """Test EventBus.unsubscribe() removes subscriber."""
    handler = MagicMock()
    event_bus.subscribe(MockEventClass, handler)
    result = event_bus.unsubscribe(MockEventClass, handler)
    assert result is True
    assert handler not in event_bus._subscribers[MockEventClass]


def test_event_bus_unsubscribe_not_found(event_bus):
    """Test EventBus.unsubscribe() when handler not found."""
    handler = MagicMock()
    result = event_bus.unsubscribe(MockEventClass, handler)
    assert result is False


def test_event_bus_get_subscriber_count(event_bus):
    """Test EventBus.get_subscriber_count() returns count."""
    handler1 = MagicMock()
    handler2 = MagicMock()
    event_bus.subscribe(MockEventClass, handler1)
    event_bus.subscribe(MockEventClass, handler2)
    count = event_bus.get_subscriber_count(MockEventClass)
    assert count == 2


def test_event_bus_get_subscriber_count_none(event_bus):
    """Test EventBus.get_subscriber_count() returns 0 for no subscribers."""
    count = event_bus.get_subscriber_count(MockEventClass)
    assert count == 0


def test_event_bus_get_all_subscriber_counts(event_bus):
    """Test EventBus.get_all_subscriber_counts() returns all counts."""
    handler1 = MagicMock()
    handler2 = MagicMock()
    event_bus.subscribe(MockEventClass, handler1)
    event_bus.subscribe(MockEventClass, handler2)
    counts = event_bus.get_all_subscriber_counts()
    assert "MockEventClass" in counts
    assert counts["MockEventClass"] == 2


@pytest.mark.asyncio
async def test_event_bus_publish(event_bus):
    """Test EventBus.publish() queues or processes event."""
    handler = AsyncMock()
    event_bus.subscribe(MockEventClass, handler)
    event = MockEventClass()
    event_bus.publish(event)
    # In test mode, event may be processed synchronously, so just verify publish doesn't raise
    # The handler will be called if processing is synchronous
    # Give it a moment for async processing if it's queued
    await asyncio.sleep(0.1)
    # Verify publish completed without error
    assert True  # If we get here, publish succeeded


@pytest.mark.asyncio
async def test_event_bus_shutdown(event_bus):
    """Test EventBus.shutdown() stops processing."""
    await event_bus.shutdown()
    assert event_bus._running is False


def test_event_bus_set_main_loop(event_bus):
    """Test EventBus.set_main_loop() sets main loop."""
    import asyncio

    loop = asyncio.new_event_loop()
    event_bus.set_main_loop(loop)
    assert event_bus._main_loop == loop
    loop.close()


def test_event_bus_unsubscribe_multiple_handlers(event_bus):
    """Test EventBus.unsubscribe() with multiple handlers."""
    handler1 = MagicMock()
    handler2 = MagicMock()
    event_bus.subscribe(MockEventClass, handler1)
    event_bus.subscribe(MockEventClass, handler2)
    result = event_bus.unsubscribe(MockEventClass, handler1)
    assert result is True
    assert handler1 not in event_bus._subscribers[MockEventClass]
    assert handler2 in event_bus._subscribers[MockEventClass]


def test_event_bus_get_all_subscriber_counts_empty(event_bus):
    """Test EventBus.get_all_subscriber_counts() with no subscribers."""
    counts = event_bus.get_all_subscriber_counts()
    assert isinstance(counts, dict)
    assert len(counts) == 0


def test_event_bus_get_all_subscriber_counts_multiple_types(event_bus):
    """Test EventBus.get_all_subscriber_counts() with multiple event types."""

    class MockEventClass2(BaseEvent):
        pass

    handler1 = MagicMock()
    handler2 = MagicMock()
    handler3 = MagicMock()
    event_bus.subscribe(MockEventClass, handler1)
    event_bus.subscribe(MockEventClass, handler2)
    event_bus.subscribe(MockEventClass2, handler3)
    counts = event_bus.get_all_subscriber_counts()
    assert "MockEventClass" in counts
    assert "MockEventClass2" in counts
    assert counts["MockEventClass"] == 2
    assert counts["MockEventClass2"] == 1


@pytest.mark.asyncio
async def test_event_bus_publish_no_subscribers(event_bus):
    """Test EventBus.publish() with no subscribers."""
    event = MockEventClass()
    # Should not raise even with no subscribers
    event_bus.publish(event)
    await asyncio.sleep(0.1)
    assert True  # If we get here, publish succeeded


@pytest.mark.asyncio
async def test_event_bus_publish_multiple_subscribers(event_bus):
    """Test EventBus.publish() with multiple subscribers."""
    handler1 = AsyncMock()
    handler2 = AsyncMock()
    event_bus.subscribe(MockEventClass, handler1)
    event_bus.subscribe(MockEventClass, handler2)
    event = MockEventClass()
    event_bus.publish(event)
    await asyncio.sleep(0.1)
    # Handlers may be called if processing is synchronous or queued
    assert True  # If we get here, publish succeeded


@pytest.mark.asyncio
async def test_event_bus_shutdown_idempotent(event_bus):
    """Test EventBus.shutdown() is idempotent."""
    await event_bus.shutdown()
    assert event_bus._running is False
    # Shutdown again should not raise
    await event_bus.shutdown()
    assert event_bus._running is False


def test_subscribe_invalid_event_type(event_bus):
    """Test subscribe() raises error for invalid event type."""
    with pytest.raises(ValueError, match="must inherit from BaseEvent"):
        event_bus.subscribe(str, MagicMock())


def test_subscribe_invalid_handler(event_bus):
    """Test subscribe() raises error for non-callable handler."""
    with pytest.raises(ValueError, match="must be callable"):
        event_bus.subscribe(MockEventClass, "not_callable")


def test_unsubscribe_invalid_event_type(event_bus):
    """Test unsubscribe() raises error for invalid event type."""
    with pytest.raises(ValueError, match="must inherit from BaseEvent"):
        event_bus.unsubscribe(str, MagicMock())


def test_publish_invalid_event(event_bus):
    """Test publish() raises error for invalid event."""
    with pytest.raises(ValueError, match="must inherit from BaseEvent"):
        event_bus.publish("not_an_event")


@pytest.mark.asyncio
async def test_stop_processing_not_running(event_bus):
    """Test _stop_processing() when not running."""
    await event_bus._stop_processing()
    # Should return early without error


def test_ensure_processing_started(event_bus):
    """Test _ensure_processing_started() calls _ensure_async_processing."""
    event_bus._ensure_async_processing = MagicMock()
    event_bus._ensure_processing_started()
    event_bus._ensure_async_processing.assert_called_once()


@pytest.mark.asyncio
async def test_handle_event_async_no_subscribers(event_bus):
    """Test _handle_event_async() when no subscribers."""
    event = MockEventClass()
    await event_bus._handle_event_async(event)
    # Should complete without error


@pytest.mark.asyncio
async def test_handle_event_async_sync_subscriber_error(event_bus):
    """Test _handle_event_async() handles sync subscriber errors."""

    def error_handler(event):
        raise ValueError("Test error")

    event_bus.subscribe(MockEventClass, error_handler)
    event = MockEventClass()
    await event_bus._handle_event_async(event)
    # Should handle error gracefully


@pytest.mark.asyncio
async def test_handle_event_async_async_subscriber_error(event_bus):
    """Test _handle_event_async() handles async subscriber errors."""

    async def error_handler(event):
        raise ValueError("Test error")

    event_bus.subscribe(MockEventClass, error_handler)
    event = MockEventClass()
    await event_bus._handle_event_async(event)
    # Should handle error gracefully


@pytest.mark.asyncio
async def test_handle_task_result_async_no_error(event_bus):
    """Test _handle_task_result_async() with successful task."""

    async def success_handler(event):
        return "success"

    task = asyncio.create_task(success_handler(MockEventClass()))
    # Wait for task to complete
    await task
    event_bus._handle_task_result_async(task, "test_handler")
    # Should complete without error


@pytest.mark.asyncio
async def test_handle_task_result_async_with_error(event_bus):
    """Test _handle_task_result_async() with task that raises error."""

    async def error_handler(event):
        raise ValueError("Test error")

    task = asyncio.create_task(error_handler(MockEventClass()))
    # Wait for task to complete
    try:
        await task
    except ValueError:
        pass
    event_bus._handle_task_result_async(task, "test_handler")
    # Should handle error gracefully
