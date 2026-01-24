# Event Subscription Cleanup Patterns

This document describes the recommended patterns for managing event subscriptions in MythosMUD services to prevent
memory leaks and ensure proper resource cleanup.

## Overview

The EventBus provides automatic cleanup of service subscriptions during application shutdown, but services should also
implement proper cleanup patterns to ensure subscriptions are removed in the correct order and prevent memory leaks
during service lifecycle changes.

## Core Principles

1. **Service Identification**: All services should provide a unique `service_id` when subscribing to events
2. **Explicit Cleanup**: Services should explicitly unsubscribe during their own shutdown
3. **Automatic Fallback**: EventBus automatically cleans up all subscriptions during application shutdown
4. **Order Matters**: Service-level cleanup should happen before application-level cleanup

## Recommended Pattern

### Basic Service Pattern

```python
from server.events.event_bus import EventBus
from server.events.event_types import BaseEvent

class MyService:
    def __init__(self, event_bus: EventBus):
        self.event_bus = event_bus
        self.service_id = "my_service"  # Unique identifier for this service

        # Subscribe to events with service_id for tracking

        self.event_bus.subscribe(
            MyEventType,
            self.handle_event,
            service_id=self.service_id
        )
        self.event_bus.subscribe(
            AnotherEventType,
            self.handle_another_event,
            service_id=self.service_id
        )

    async def handle_event(self, event: MyEventType) -> None:
        """Handle MyEventType events."""
        # Process event

        pass

    async def handle_another_event(self, event: AnotherEventType) -> None:
        """Handle AnotherEventType events."""
        # Process event

        pass

    async def shutdown(self) -> None:
        """
        Shutdown the service and clean up all event subscriptions.

        This should be called during service shutdown to ensure proper
        cleanup order. The EventBus will also clean up subscriptions
        during application shutdown, but explicit cleanup here ensures
        proper order and prevents issues during service restarts.
        """
        # Cleanup all subscriptions for this service

        removed_count = self.event_bus.unsubscribe_all_for_service(self.service_id)
        self.logger.info(
            "Service shutdown complete",
            service_id=self.service_id,
            subscriptions_removed=removed_count
        )
```

### Context Manager Pattern (Optional)

For services that need automatic cleanup when exiting a context:

```python
from contextlib import asynccontextmanager
from server.events.event_bus import EventBus

class EventSubscriptionContext:
    """Context manager for automatic event subscription cleanup."""

    def __init__(self, event_bus: EventBus, service_id: str):
        self.event_bus = event_bus
        self.service_id = service_id
        self._subscribed_events: list[tuple[type[BaseEvent], Callable]] = []

    def subscribe(self, event_type: type[BaseEvent], handler: Callable) -> None:
        """Subscribe to an event and track it for cleanup."""
        self.event_bus.subscribe(event_type, handler, service_id=self.service_id)
        self._subscribed_events.append((event_type, handler))

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Cleanup all subscriptions when exiting context."""
        self.event_bus.unsubscribe_all_for_service(self.service_id)

# Usage

async def my_function(event_bus: EventBus):
    async with EventSubscriptionContext(event_bus, "temporary_service") as ctx:
        ctx.subscribe(MyEventType, my_handler)
        # Do work - subscriptions automatically cleaned up on exit

        pass
```

## Service ID Naming Conventions

Service IDs should follow these conventions:

**Format**: `{module_name}_{service_name}` or `{service_name}` for top-level services

**Examples**:

- `connection_manager` - Connection manager service
- `nats_message_handler` - NATS message handler service
- `combat_service` - Combat service
- `player_service` - Player service
- **Uniqueness**: Service IDs must be unique within the application
- **Persistence**: Service IDs should remain constant across service restarts

## Cleanup Order

The recommended cleanup order is:

1. **Service-Level Cleanup**: Services call `unsubscribe_all_for_service()` during their own shutdown

2. **Application-Level Cleanup**: EventBus automatically cleans up all remaining subscriptions during

   `EventBus.shutdown()`

This two-phase approach ensures:

- Services can clean up in the correct order
- No subscriptions are missed if a service fails to clean up
- Proper logging of cleanup operations

## Monitoring

The EventBus provides monitoring methods to track subscription health:

```python
# Get subscriber statistics

stats = event_bus.get_subscriber_stats()
print(f"Total subscribers: {stats['total_subscribers']}")
print(f"Services tracked: {stats['services_tracked']}")
print(f"Service subscriber counts: {stats['service_subscriber_counts']}")

# Get subscriber counts per event type

counts = event_bus.get_all_subscriber_counts()
for event_type, count in counts.items():
    print(f"{event_type}: {count} subscribers")
```

## Common Pitfalls

### ❌ Don't: Subscribe without service_id

```python
# BAD: No service_id means subscription won't be tracked for cleanup

event_bus.subscribe(MyEventType, handler)
```

### ✅ Do: Always provide service_id

```python
# GOOD: Service_id enables automatic cleanup tracking

event_bus.subscribe(MyEventType, handler, service_id="my_service")
```

### ❌ Don't: Forget to cleanup during service shutdown

```python
# BAD: Subscriptions remain after service shutdown

async def shutdown(self):
    # Missing: event_bus.unsubscribe_all_for_service(self.service_id)

    pass
```

### ✅ Do: Explicitly cleanup during shutdown

```python
# GOOD: Explicit cleanup ensures proper order

async def shutdown(self):
    self.event_bus.unsubscribe_all_for_service(self.service_id)
```

### ❌ Don't: Use the same service_id for multiple service instances

```python
# BAD: Multiple instances with same service_id causes tracking conflicts

service1 = MyService(event_bus)  # service_id="my_service"
service2 = MyService(event_bus)  # service_id="my_service" - CONFLICT!
```

### ✅ Do: Use unique service_ids or instance-specific IDs

```python
# GOOD: Unique service_id per instance

service1 = MyService(event_bus, instance_id="1")  # service_id="my_service_1"
service2 = MyService(event_bus, instance_id="2")  # service_id="my_service_2"
```

## Testing

When testing services with event subscriptions:

1. **Verify Cleanup**: Test that `unsubscribe_all_for_service()` removes all subscriptions
2. **Test Shutdown**: Verify subscriptions are cleaned up during service shutdown
3. **Test Restart**: Verify service restart doesn't create duplicate subscriptions
4. **Monitor Stats**: Use `get_subscriber_stats()` to verify subscription counts

Example test:

```python
async def test_service_cleanup_subscriptions(event_bus: EventBus):
    service = MyService(event_bus)

    # Verify subscriptions exist

    stats = event_bus.get_subscriber_stats()
    assert stats['services_tracked'] == 1
    assert stats['service_subscriber_counts']['my_service'] == 2

    # Shutdown service

    await service.shutdown()

    # Verify subscriptions removed

    stats = event_bus.get_subscriber_stats()
    assert stats['services_tracked'] == 0
    assert 'my_service' not in stats['service_subscriber_counts']
```

## Integration with Application Shutdown

The EventBus is automatically cleaned up during application shutdown in `server/app/lifespan_shutdown.py`:

```python
async def _shutdown_event_bus(container: ApplicationContainer) -> None:
    """Shutdown event bus and clean up all service subscriptions."""
    if not container.event_bus:
        return

    # Get stats before shutdown for logging

    stats = container.event_bus.get_subscriber_stats()
    logger.info(
        "EventBus subscriber stats before shutdown",
        total_subscribers=stats.get("total_subscribers", 0),
        services_tracked=stats.get("services_tracked", 0),
    )

    # Shutdown will automatically clean up all service subscriptions

    await container.event_bus.shutdown()
```

This ensures that even if services fail to clean up their subscriptions, the EventBus will clean them up during
application shutdown.

## Summary

Always provide a unique `service_id` when subscribing to events

- Explicitly call `unsubscribe_all_for_service()` during service shutdown
- Use consistent service_id naming conventions
- Monitor subscription counts using `get_subscriber_stats()`
- Test cleanup behavior in your service tests

Following these patterns ensures proper resource cleanup and prevents memory leaks from orphaned event subscriptions.
