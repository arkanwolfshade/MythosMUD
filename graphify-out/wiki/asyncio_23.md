# asyncio

> 22 nodes

## Key Concepts

- **asyncio** (27 connections)
- **test_multiple_services_subscribe_same_events_integration()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_service_shutdown_removes_subscribers()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_publish()** (4 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_shutdown_cleans_up_service_subscriptions()** (4 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_shutdown()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_shutdown_idempotent()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_multiple_services_subscribe_to_same_event()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_stop_processing_not_running()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_active_task_details_and_lifecycle_metrics()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_active_task_details_includes_exception()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_ensure_async_processing_no_loop_logs()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_set_main_loop_and_ensure_processing()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_signal_shutdown_and_cancel_helpers()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.publish() queues or processes event.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.shutdown() stops processing.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.shutdown() is idempotent.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test _stop_processing() when not running.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.shutdown() automatically cleans up all service subscriptions.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test multiple services subscribing to the same event type.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test that service shutdown removes all subscribers for that service. This test…** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Integration test: Multiple services subscribing to same events and cleanup.…** (1 connections) — `server/tests/unit/events/test_event_bus.py`

## Relationships

- [test_event_bus.py](test_event_bus.py.md) (14 shared connections)
- [MockEventClass](MockEventClass.md) (12 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [test_event_bus_publish_multiple_subscribers](test_event_bus_publish_multiple_subscribers.md) (1 shared connections)
- [test_event_bus_publish_no_subscribers](test_event_bus_publish_no_subscribers.md) (1 shared connections)

## Source Files

- `server/tests/unit/events/test_event_bus.py`

## Audit Trail

- EXTRACTED: 49 (91%)
- INFERRED: 5 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*