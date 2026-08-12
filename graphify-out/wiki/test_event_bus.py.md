# test_event_bus.py

> 22 nodes

## Key Concepts

- **test_event_bus.py** (46 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_ensure_processing_started()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_get_all_subscriber_counts()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_get_all_subscriber_counts_empty()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_subscribe()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_subscribe_multiple()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_unsubscribe()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_unsubscribe_not_found()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_get_subscriber_stats()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_subscribe_with_service_id()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_unsubscribe_all_for_service_partial_cleanup()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **Unit tests for event bus. Tests the EventBus class.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.get_all_subscriber_counts() with no subscribers.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test _ensure_processing_started() calls _ensure_async_processing.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.subscribe() with service_id for tracking.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.unsubscribe_all_for_service() only removes tracked handlers.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.subscribe() adds subscriber.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.get_subscriber_stats() returns subscriber statistics.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.subscribe() with multiple handlers.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.unsubscribe() removes subscriber.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.unsubscribe() when handler not found.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.get_all_subscriber_counts() returns all counts.** (1 connections) — `server/tests/unit/events/test_event_bus.py`

## Relationships

- [asyncio](asyncio.md) (8 shared connections)
- [MockEventClass](MockEventClass.md) (8 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [test_event_bus_set_main_loop](test_event_bus_set_main_loop.md) (1 shared connections)
- [test_event_bus_unsubscribe_multiple_handlers](test_event_bus_unsubscribe_multiple_handlers.md) (1 shared connections)
- [test_event_bus_get_all_subscriber_counts_multiple_types](test_event_bus_get_all_subscriber_counts_multiple_types.md) (1 shared connections)
- [test_event_bus_inject_dispatches_to_subscribers](test_event_bus_inject_dispatches_to_subscribers.md) (1 shared connections)
- [test_subscribe_invalid_event_type](test_subscribe_invalid_event_type.md) (1 shared connections)
- [test_subscribe_invalid_handler](test_subscribe_invalid_handler.md) (1 shared connections)
- [test_unsubscribe_invalid_event_type](test_unsubscribe_invalid_event_type.md) (1 shared connections)
- [test_publish_invalid_event](test_publish_invalid_event.md) (1 shared connections)
- [event_bus](event_bus.md) (1 shared connections)

## Source Files

- `server/tests/unit/events/test_event_bus.py`

## Audit Trail

- EXTRACTED: 77 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*