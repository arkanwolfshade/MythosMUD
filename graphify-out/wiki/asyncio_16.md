# asyncio

> 15 nodes

## Key Concepts

- **asyncio** (17 connections)
- **test_event_bus_shutdown()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_shutdown_idempotent()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_multiple_services_subscribe_same_events_integration()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_multiple_services_subscribe_to_same_event()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_service_shutdown_removes_subscribers()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_shutdown_cleans_up_service_subscriptions()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_stop_processing_not_running()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.shutdown() stops processing.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.shutdown() is idempotent.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test _stop_processing() when not running.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.shutdown() automatically cleans up all service subscriptions.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test multiple services subscribing to the same event type.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test that service shutdown removes all subscribers for that service. This test…** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Integration test: Multiple services subscribing to same events and cleanup.…** (1 connections) — `server/tests/unit/events/test_event_bus.py`

## Relationships

- [test_event_bus.py](test_event_bus.py.md) (8 shared connections)
- [MockEventClass](MockEventClass.md) (7 shared connections)
- [test_event_bus_publish_no_subscribers](test_event_bus_publish_no_subscribers.md) (1 shared connections)
- [test_handle_task_result_async_with_error](test_handle_task_result_async_with_error.md) (1 shared connections)

## Source Files

- `server/tests/unit/events/test_event_bus.py`

## Audit Trail

- EXTRACTED: 31 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*