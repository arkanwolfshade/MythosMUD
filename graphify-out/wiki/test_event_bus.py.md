# test_event_bus.py

> 28 nodes

## Key Concepts

- **test_event_bus.py** (58 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_get_all_subscriber_counts_multiple_types()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_get_all_subscriber_counts()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_get_all_subscriber_counts_empty()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_get_subscriber_count_none()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_subscribe()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_subscribe_multiple()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_unsubscribe()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_unsubscribe_multiple_handlers()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_unsubscribe_not_found()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_publish_invalid_event()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_subscribe_invalid_handler()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_subscribe_with_service_id()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_unsubscribe_invalid_event_type()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **Unit tests for event bus. Tests the EventBus class.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.unsubscribe() with multiple handlers.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.get_all_subscriber_counts() with no subscribers.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.get_all_subscriber_counts() with multiple event types.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test subscribe() raises error for non-callable handler.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test unsubscribe() raises error for invalid event type.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test publish() raises error for invalid event.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.subscribe() with service_id for tracking.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.subscribe() adds subscriber.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.subscribe() with multiple handlers.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.unsubscribe() removes subscriber.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- *... and 3 more nodes in this community*

## Relationships

- [asyncio](asyncio.md) (14 shared connections)
- [MockEventClass](MockEventClass.md) (13 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [test_event_bus_set_main_loop](test_event_bus_set_main_loop.md) (1 shared connections)
- [test_event_bus_publish_no_subscribers](test_event_bus_publish_no_subscribers.md) (1 shared connections)
- [test_event_bus_publish_multiple_subscribers](test_event_bus_publish_multiple_subscribers.md) (1 shared connections)
- [test_subscribe_invalid_event_type](test_subscribe_invalid_event_type.md) (1 shared connections)
- [event_bus](event_bus.md) (1 shared connections)
- [test_ensure_processing_started](test_ensure_processing_started.md) (1 shared connections)
- [test_event_bus_init](test_event_bus_init.md) (1 shared connections)
- [test_unsubscribe_all_for_service](test_unsubscribe_all_for_service.md) (1 shared connections)
- [test_unsubscribe_all_for_service_nonexistent](test_unsubscribe_all_for_service_nonexistent.md) (1 shared connections)

## Source Files

- `server/tests/unit/events/test_event_bus.py`

## Audit Trail

- EXTRACTED: 71 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*