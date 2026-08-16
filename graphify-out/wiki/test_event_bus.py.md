# test_event_bus.py

> 26 nodes

## Key Concepts

- **test_event_bus.py** (59 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_get_subscriber_stats()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_unsubscribe_all_for_service()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_get_all_subscriber_counts()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_get_subscriber_count()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_init()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_set_main_loop()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_subscribe()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_subscribe_multiple()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_unsubscribe_multiple_handlers()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_publish_invalid_event()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_subscribe_invalid_handler()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_unsubscribe_all_for_service_nonexistent()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **Unit tests for event bus. Tests the EventBus class.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.set_main_loop() sets main loop.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.unsubscribe() with multiple handlers.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test subscribe() raises error for non-callable handler.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test publish() raises error for invalid event.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus initialization.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.unsubscribe_all_for_service() removes all handlers for a service.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.unsubscribe_all_for_service() with nonexistent service_id.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.subscribe() adds subscriber.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.get_subscriber_stats() returns subscriber statistics.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.subscribe() with multiple handlers.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.get_subscriber_count() returns count.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- *... and 1 more nodes in this community*

## Relationships

- [asyncio](asyncio.md) (13 shared connections)
- [MockEventClass](MockEventClass.md) (11 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [test_event_bus_get_all_subscriber_counts_empty](test_event_bus_get_all_subscriber_counts_empty.md) (1 shared connections)
- [test_event_bus_get_all_subscriber_counts_multiple_types](test_event_bus_get_all_subscriber_counts_multiple_types.md) (1 shared connections)
- [test_event_bus_publish_no_subscribers](test_event_bus_publish_no_subscribers.md) (1 shared connections)
- [test_subscribe_invalid_event_type](test_subscribe_invalid_event_type.md) (1 shared connections)
- [test_unsubscribe_invalid_event_type](test_unsubscribe_invalid_event_type.md) (1 shared connections)
- [event_bus](event_bus.md) (1 shared connections)
- [test_ensure_processing_started](test_ensure_processing_started.md) (1 shared connections)
- [test_handle_event_async_no_subscribers](test_handle_event_async_no_subscribers.md) (1 shared connections)

## Source Files

- `server/tests/unit/events/test_event_bus.py`

## Audit Trail

- EXTRACTED: 71 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*