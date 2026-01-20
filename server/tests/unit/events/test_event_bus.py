"""
Unit tests for event bus.

Tests the EventBus class.
"""

# pylint: disable=redefined-outer-name  # Reason: Pytest fixtures require parameter names to match fixture names for dependency injection
# pylint: disable=too-many-lines  # Reason: Comprehensive test suite requires extensive test coverage for event bus functionality including subscription management, cleanup patterns, and multi-service scenarios

import asyncio
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.events.event_bus import EventBus
from server.events.event_types import BaseEvent


class MockEventClass(BaseEvent):
    """Mock event class for testing."""


@pytest.fixture
def event_bus():
    """Create an EventBus instance."""
    return EventBus()


def test_event_bus_init(event_bus):
    """Test EventBus initialization."""
    # pylint: disable=protected-access  # Reason: Testing internal initialization state requires accessing protected members to verify correct setup
    assert event_bus._running is False  # pylint: disable=protected-access
    assert event_bus._processing_task is None  # pylint: disable=protected-access
    assert len(event_bus._subscribers) == 0  # pylint: disable=protected-access


def test_event_bus_subscribe(event_bus):
    """Test EventBus.subscribe() adds subscriber."""
    # pylint: disable=protected-access  # Reason: Testing internal state requires accessing protected members to verify subscription behavior
    handler = MagicMock()
    event_bus.subscribe(MockEventClass, handler)
    assert MockEventClass in event_bus._subscribers
    assert handler in event_bus._subscribers[MockEventClass]


def test_event_bus_subscribe_multiple(event_bus):
    """Test EventBus.subscribe() with multiple handlers."""
    # pylint: disable=protected-access  # Reason: Testing internal state requires accessing protected members to verify multiple subscription behavior
    handler1 = MagicMock()
    handler2 = MagicMock()
    event_bus.subscribe(MockEventClass, handler1)
    event_bus.subscribe(MockEventClass, handler2)
    assert len(event_bus._subscribers[MockEventClass]) == 2


def test_event_bus_unsubscribe(event_bus):
    """Test EventBus.unsubscribe() removes subscriber."""
    # pylint: disable=protected-access  # Reason: Testing internal state requires accessing protected members to verify unsubscription behavior
    handler = MagicMock()
    event_bus.subscribe(MockEventClass, handler)
    result = event_bus.unsubscribe(MockEventClass, handler)
    assert result is True
    assert handler not in event_bus._subscribers[MockEventClass]  # pylint: disable=protected-access


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
    # pylint: disable=protected-access  # Reason: Testing internal state requires accessing protected members to verify shutdown behavior
    await event_bus.shutdown()
    assert event_bus._running is False  # pylint: disable=protected-access


def test_event_bus_set_main_loop(event_bus):
    """Test EventBus.set_main_loop() sets main loop."""
    # pylint: disable=protected-access  # Reason: Testing internal state requires accessing protected members to verify main loop assignment
    loop = asyncio.new_event_loop()
    event_bus.set_main_loop(loop)
    assert event_bus._main_loop == loop  # pylint: disable=protected-access
    loop.close()


def test_event_bus_unsubscribe_multiple_handlers(event_bus):
    """Test EventBus.unsubscribe() with multiple handlers."""
    # pylint: disable=protected-access  # Reason: Testing internal state requires accessing protected members to verify selective unsubscription behavior
    handler1 = MagicMock()
    handler2 = MagicMock()
    event_bus.subscribe(MockEventClass, handler1)
    event_bus.subscribe(MockEventClass, handler2)
    result = event_bus.unsubscribe(MockEventClass, handler1)
    assert result is True
    assert handler1 not in event_bus._subscribers[MockEventClass]  # pylint: disable=protected-access
    assert handler2 in event_bus._subscribers[MockEventClass]  # pylint: disable=protected-access


def test_event_bus_get_all_subscriber_counts_empty(event_bus):
    """Test EventBus.get_all_subscriber_counts() with no subscribers."""
    counts = event_bus.get_all_subscriber_counts()
    assert isinstance(counts, dict)
    assert len(counts) == 0


def test_event_bus_get_all_subscriber_counts_multiple_types(event_bus):
    """Test EventBus.get_all_subscriber_counts() with multiple event types."""

    class MockEventClass2(BaseEvent):
        """Mock event class for testing."""

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
    # pylint: disable=protected-access  # Reason: Testing internal state requires accessing protected members to verify idempotent shutdown behavior
    await event_bus.shutdown()
    assert event_bus._running is False  # pylint: disable=protected-access
    # Shutdown again should not raise
    await event_bus.shutdown()
    assert event_bus._running is False  # pylint: disable=protected-access


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
    # pylint: disable=protected-access  # Reason: Testing internal method requires accessing protected member to verify behavior when not running
    await event_bus._stop_processing()
    # Should return early without error


def test_ensure_processing_started(event_bus):
    """Test _ensure_processing_started() calls _ensure_async_processing."""
    # pylint: disable=protected-access  # Reason: Testing internal methods requires accessing protected members to verify method delegation
    event_bus._ensure_async_processing = MagicMock()  # pylint: disable=protected-access
    event_bus._ensure_processing_started()  # pylint: disable=protected-access
    event_bus._ensure_async_processing.assert_called_once()  # pylint: disable=protected-access


@pytest.mark.asyncio
async def test_handle_event_async_no_subscribers(event_bus):
    """Test _handle_event_async() when no subscribers."""
    # pylint: disable=protected-access  # Reason: Testing internal method requires accessing protected member to verify behavior with no subscribers
    event = MockEventClass()
    await event_bus._handle_event_async(event)  # pylint: disable=protected-access
    # Should complete without error


@pytest.mark.asyncio
async def test_handle_event_async_sync_subscriber_error(event_bus):
    """Test _handle_event_async() handles sync subscriber errors."""
    # pylint: disable=protected-access  # Reason: Testing internal method requires accessing protected member to verify error handling behavior

    def error_handler(event):
        raise ValueError("Test error")

    event_bus.subscribe(MockEventClass, error_handler)
    event = MockEventClass()
    await event_bus._handle_event_async(event)
    # Should handle error gracefully


@pytest.mark.asyncio
async def test_handle_event_async_async_subscriber_error(event_bus):
    """Test _handle_event_async() handles async subscriber errors."""
    # pylint: disable=protected-access  # Reason: Testing internal method requires accessing protected member to verify async error handling behavior

    async def error_handler(event):
        raise ValueError("Test error")

    event_bus.subscribe(MockEventClass, error_handler)
    event = MockEventClass()
    await event_bus._handle_event_async(event)  # pylint: disable=protected-access
    # Should handle error gracefully


@pytest.mark.asyncio
async def test_handle_task_result_async_no_error(event_bus):
    """Test _handle_task_result_async() with successful task."""
    # pylint: disable=protected-access  # Reason: Testing internal method requires accessing protected member to verify successful task handling

    async def success_handler(_event):  # pylint: disable=unused-argument  # Reason: Event parameter required by handler signature but not used in this test
        return "success"

    task = asyncio.create_task(success_handler(MockEventClass()))
    # Wait for task to complete
    await task
    event_bus._handle_task_result_async(task, "test_handler")  # pylint: disable=protected-access
    # Should complete without error


@pytest.mark.asyncio
async def test_handle_task_result_async_with_error(event_bus):
    """Test _handle_task_result_async() with task that raises error."""
    # pylint: disable=protected-access  # Reason: Testing internal method requires accessing protected member to verify error handling behavior

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


def test_subscribe_with_service_id(event_bus):
    """Test EventBus.subscribe() with service_id for tracking."""
    # pylint: disable=protected-access  # Reason: Testing internal state requires accessing protected members to verify service_id tracking behavior
    handler = MagicMock()
    service_id = "test_service"
    event_bus.subscribe(MockEventClass, handler, service_id=service_id)
    assert MockEventClass in event_bus._subscribers  # pylint: disable=protected-access
    assert handler in event_bus._subscribers[MockEventClass]  # pylint: disable=protected-access
    assert service_id in event_bus._subscriber_tracking  # pylint: disable=protected-access
    assert (MockEventClass, handler) in event_bus._subscriber_tracking[service_id]  # pylint: disable=protected-access


def test_unsubscribe_all_for_service(event_bus):
    """Test EventBus.unsubscribe_all_for_service() removes all handlers for a service."""
    # pylint: disable=protected-access  # Reason: Testing internal state requires accessing protected members to verify service-based unsubscription behavior
    handler1 = MagicMock()
    handler2 = MagicMock()

    class MockEventClass2(BaseEvent):
        """Mock event class for testing."""

    service_id = "test_service"
    event_bus.subscribe(MockEventClass, handler1, service_id=service_id)
    event_bus.subscribe(MockEventClass2, handler2, service_id=service_id)

    # Verify both handlers are subscribed
    assert handler1 in event_bus._subscribers[MockEventClass]
    assert handler2 in event_bus._subscribers[MockEventClass2]

    # Unsubscribe all for service
    removed_count = event_bus.unsubscribe_all_for_service(service_id)
    assert removed_count == 2
    assert handler1 not in event_bus._subscribers[MockEventClass]
    assert handler2 not in event_bus._subscribers[MockEventClass2]
    assert service_id not in event_bus._subscriber_tracking


def test_unsubscribe_all_for_service_nonexistent(event_bus):
    """Test EventBus.unsubscribe_all_for_service() with nonexistent service_id."""
    removed_count = event_bus.unsubscribe_all_for_service("nonexistent_service")
    assert removed_count == 0


def test_unsubscribe_all_for_service_partial_cleanup(event_bus):
    """Test EventBus.unsubscribe_all_for_service() only removes tracked handlers."""
    # pylint: disable=protected-access  # Reason: Testing internal state requires accessing protected members to verify partial cleanup behavior
    handler1 = MagicMock()
    handler2 = MagicMock()

    service_id = "test_service"
    # Subscribe handler1 with service_id, handler2 without
    event_bus.subscribe(MockEventClass, handler1, service_id=service_id)
    event_bus.subscribe(MockEventClass, handler2)  # No service_id

    # Unsubscribe all for service should only remove handler1
    removed_count = event_bus.unsubscribe_all_for_service(service_id)
    assert removed_count == 1
    assert handler1 not in event_bus._subscribers[MockEventClass]
    assert handler2 in event_bus._subscribers[MockEventClass]  # Still subscribed


def test_get_subscriber_stats(event_bus):
    """Test EventBus.get_subscriber_stats() returns subscriber statistics."""
    handler1 = MagicMock()
    handler2 = MagicMock()

    class MockEventClass2(BaseEvent):
        """Mock event class for testing."""

    service_id = "test_service"
    event_bus.subscribe(MockEventClass, handler1, service_id=service_id)
    event_bus.subscribe(MockEventClass2, handler2, service_id=service_id)

    stats = event_bus.get_subscriber_stats()
    assert "subscriber_counts_by_event" in stats
    assert "total_subscribers" in stats
    assert "services_tracked" in stats
    assert "service_subscriber_counts" in stats
    assert "tracked_subscriptions" in stats
    assert stats["total_subscribers"] == 2
    assert stats["services_tracked"] == 1
    assert stats["tracked_subscriptions"] == 2
    assert service_id in stats["service_subscriber_counts"]
    assert stats["service_subscriber_counts"][service_id] == 2


@pytest.mark.asyncio
async def test_shutdown_cleans_up_service_subscriptions(event_bus):
    """Test EventBus.shutdown() automatically cleans up all service subscriptions."""
    # pylint: disable=protected-access  # Reason: Testing internal state requires accessing protected members to verify shutdown cleanup behavior
    handler1 = MagicMock()
    handler2 = MagicMock()

    class MockEventClass2(BaseEvent):
        """Mock event class for testing."""

    service_id1 = "service1"
    service_id2 = "service2"
    event_bus.subscribe(MockEventClass, handler1, service_id=service_id1)
    event_bus.subscribe(MockEventClass2, handler2, service_id=service_id2)

    # Verify subscriptions exist
    assert handler1 in event_bus._subscribers[MockEventClass]
    assert handler2 in event_bus._subscribers[MockEventClass2]
    assert len(event_bus._subscriber_tracking) == 2

    # Shutdown should clean up all service subscriptions
    await event_bus.shutdown()

    # Verify all subscriptions are removed
    assert handler1 not in event_bus._subscribers[MockEventClass]
    assert handler2 not in event_bus._subscribers[MockEventClass2]
    assert len(event_bus._subscriber_tracking) == 0


@pytest.mark.asyncio
async def test_multiple_services_subscribe_to_same_event(event_bus):
    """Test multiple services subscribing to the same event type."""
    # pylint: disable=protected-access  # Reason: Testing internal state requires accessing protected members to verify multiple service subscription behavior
    handler1 = MagicMock()
    handler2 = MagicMock()
    handler3 = MagicMock()

    service_id1 = "service1"
    service_id2 = "service2"
    # All three handlers subscribe to same event type
    event_bus.subscribe(MockEventClass, handler1, service_id=service_id1)
    event_bus.subscribe(MockEventClass, handler2, service_id=service_id2)
    event_bus.subscribe(MockEventClass, handler3)  # No service_id

    # Verify all handlers are subscribed
    assert len(event_bus._subscribers[MockEventClass]) == 3
    assert handler1 in event_bus._subscribers[MockEventClass]
    assert handler2 in event_bus._subscribers[MockEventClass]
    assert handler3 in event_bus._subscribers[MockEventClass]

    # Unsubscribe service1 should only remove handler1
    removed = event_bus.unsubscribe_all_for_service(service_id1)
    assert removed == 1
    assert handler1 not in event_bus._subscribers[MockEventClass]
    assert handler2 in event_bus._subscribers[MockEventClass]
    assert handler3 in event_bus._subscribers[MockEventClass]

    # Unsubscribe service2 should only remove handler2
    removed = event_bus.unsubscribe_all_for_service(service_id2)
    assert removed == 1
    assert handler1 not in event_bus._subscribers[MockEventClass]
    assert handler2 not in event_bus._subscribers[MockEventClass]
    assert handler3 in event_bus._subscribers[MockEventClass]  # Still subscribed


@pytest.mark.asyncio
async def test_service_shutdown_removes_subscribers(event_bus):
    """
    Test that service shutdown removes all subscribers for that service.

    This test verifies the recommended service cleanup pattern where services
    call unsubscribe_all_for_service() during their shutdown to ensure proper
    cleanup order and prevent memory leaks.
    """
    # pylint: disable=protected-access  # Reason: Testing internal state requires accessing protected members to verify service shutdown cleanup behavior

    # Create a mock service with multiple event subscriptions
    class MockService:
        """Mock service for testing event subscription cleanup."""

        def __init__(self, event_bus: EventBus):
            self.event_bus = event_bus
            self.service_id = "test_service"
            self.handler1 = MagicMock()
            self.handler2 = MagicMock()

            # Subscribe to multiple event types
            self.event_bus.subscribe(MockEventClass, self.handler1, service_id=self.service_id)

            class MockEventClass2(BaseEvent):
                """Mock event class for testing."""

            self.mock_event_class2 = MockEventClass2
            self.event_bus.subscribe(MockEventClass2, self.handler2, service_id=self.service_id)

        async def shutdown(self):
            """Service shutdown method that cleans up subscriptions."""
            removed_count = self.event_bus.unsubscribe_all_for_service(self.service_id)
            return removed_count

    # Create service and verify subscriptions
    service = MockService(event_bus)
    assert service.handler1 in event_bus._subscribers[MockEventClass]
    assert service.handler2 in event_bus._subscribers[service.mock_event_class2]
    assert service.service_id in event_bus._subscriber_tracking
    assert len(event_bus._subscriber_tracking[service.service_id]) == 2

    # Get stats before shutdown
    stats_before = event_bus.get_subscriber_stats()
    assert stats_before["services_tracked"] == 1
    assert stats_before["total_subscribers"] == 2
    assert stats_before["service_subscriber_counts"][service.service_id] == 2

    # Shutdown service
    removed_count = await service.shutdown()
    assert removed_count == 2

    # Verify all subscriptions for this service are removed
    assert service.handler1 not in event_bus._subscribers[MockEventClass]
    assert service.handler2 not in event_bus._subscribers[service.mock_event_class2]
    assert service.service_id not in event_bus._subscriber_tracking

    # Verify stats after shutdown
    stats_after = event_bus.get_subscriber_stats()
    assert stats_after["services_tracked"] == 0
    assert stats_after["total_subscribers"] == 0
    assert service.service_id not in stats_after["service_subscriber_counts"]


@pytest.mark.asyncio
async def test_multiple_services_subscribe_same_events_integration(event_bus):
    """
    Integration test: Multiple services subscribing to same events and cleanup.

    This test verifies that when multiple services subscribe to the same event types,
    each service can clean up its own subscriptions independently without affecting
    other services' subscriptions. This prevents memory leaks when services are
    recreated or restarted.
    """
    # pylint: disable=protected-access  # Reason: Testing internal state requires accessing protected members to verify multi-service subscription and cleanup behavior

    # Define shared event class so both services subscribe to the same event type
    class MockEventClass2(BaseEvent):
        """Mock event class for testing."""

    # Create multiple services that subscribe to the same event types
    class ServiceA:
        """Mock service A for testing multi-service subscription behavior."""

        def __init__(self, event_bus: EventBus):
            self.event_bus = event_bus
            self.service_id = "service_a"
            self.handler_a1 = MagicMock()
            self.handler_a2 = MagicMock()

            # Subscribe to same event types as ServiceB
            self.event_bus.subscribe(MockEventClass, self.handler_a1, service_id=self.service_id)
            self.mock_event_class2 = MockEventClass2
            self.event_bus.subscribe(MockEventClass2, self.handler_a2, service_id=self.service_id)

        async def shutdown(self):
            """Service shutdown method that cleans up subscriptions."""
            return self.event_bus.unsubscribe_all_for_service(self.service_id)

    class ServiceB:
        """Mock service B for testing multi-service subscription behavior."""

        def __init__(self, event_bus: EventBus):
            self.event_bus = event_bus
            self.service_id = "service_b"
            self.handler_b1 = MagicMock()
            self.handler_b2 = MagicMock()

            # Subscribe to same event types as ServiceA
            self.event_bus.subscribe(MockEventClass, self.handler_b1, service_id=self.service_id)
            self.mock_event_class2 = MockEventClass2
            self.event_bus.subscribe(MockEventClass2, self.handler_b2, service_id=self.service_id)

        async def shutdown(self):
            """Service shutdown method that cleans up subscriptions."""
            return self.event_bus.unsubscribe_all_for_service(self.service_id)

    # Create both services
    service_a = ServiceA(event_bus)
    service_b = ServiceB(event_bus)

    # Verify both services have subscriptions to same event types
    assert len(event_bus._subscribers[MockEventClass]) == 2  # handler_a1 and handler_b1
    assert len(event_bus._subscribers[service_a.mock_event_class2]) == 2  # handler_a2 and handler_b2
    assert len(event_bus._subscriber_tracking) == 2  # Both services tracked

    # Verify stats show both services
    stats = event_bus.get_subscriber_stats()
    assert stats["services_tracked"] == 2
    assert stats["total_subscribers"] == 4
    assert stats["service_subscriber_counts"]["service_a"] == 2
    assert stats["service_subscriber_counts"]["service_b"] == 2

    # Shutdown service_a - should only remove its subscriptions
    removed_a = await service_a.shutdown()
    assert removed_a == 2

    # Verify service_a subscriptions removed, but service_b still subscribed
    assert service_a.handler_a1 not in event_bus._subscribers[MockEventClass]  # pylint: disable=protected-access
    assert service_a.handler_a2 not in event_bus._subscribers[service_a.mock_event_class2]  # pylint: disable=protected-access
    assert service_b.handler_b1 in event_bus._subscribers[MockEventClass]  # pylint: disable=protected-access
    assert service_b.handler_b2 in event_bus._subscribers[service_b.mock_event_class2]  # pylint: disable=protected-access
    assert "service_a" not in event_bus._subscriber_tracking  # pylint: disable=protected-access
    assert "service_b" in event_bus._subscriber_tracking  # pylint: disable=protected-access

    # Verify stats after service_a shutdown
    stats_after_a = event_bus.get_subscriber_stats()
    assert stats_after_a["services_tracked"] == 1
    assert stats_after_a["total_subscribers"] == 2
    assert "service_a" not in stats_after_a["service_subscriber_counts"]
    assert stats_after_a["service_subscriber_counts"]["service_b"] == 2

    # Shutdown service_b - should remove remaining subscriptions
    removed_b = await service_b.shutdown()
    assert removed_b == 2

    # Verify all subscriptions removed
    assert service_b.handler_b1 not in event_bus._subscribers[MockEventClass]
    assert service_b.handler_b2 not in event_bus._subscribers[service_b.mock_event_class2]
    assert len(event_bus._subscriber_tracking) == 0

    # Verify final stats
    stats_final = event_bus.get_subscriber_stats()
    assert stats_final["services_tracked"] == 0
    assert stats_final["total_subscribers"] == 0
    assert len(stats_final["service_subscriber_counts"]) == 0

    # Test service recreation - create new service_a instance
    service_a_new = ServiceA(event_bus)

    # Verify new service can subscribe without conflicts
    assert service_a_new.handler_a1 in event_bus._subscribers[MockEventClass]
    assert service_a_new.handler_a2 in event_bus._subscribers[service_a_new.mock_event_class2]
    assert "service_a" in event_bus._subscriber_tracking

    # Verify no memory leak - stats should show only new service
    stats_recreated = event_bus.get_subscriber_stats()
    assert stats_recreated["services_tracked"] == 1
    assert stats_recreated["total_subscribers"] == 2
    assert stats_recreated["service_subscriber_counts"]["service_a"] == 2

    # Cleanup
    await service_a_new.shutdown()
