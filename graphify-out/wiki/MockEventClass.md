# MockEventClass

> 16 nodes

## Key Concepts

- **MockEventClass** (18 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_inject_dispatches_to_subscribers()** (4 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_publish()** (4 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_publish_multiple_subscribers()** (4 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_task_result_async_no_error()** (4 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_inject_queue_full_and_invalid()** (4 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_async_subscriber_error_isolation()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_publish_isolates_sync_subscriber_errors()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_publish_queue_full_raises()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_stop_processing_and_publish_when_running()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_inject_and_get_all_counts()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.publish() queues or processes event.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.inject() delivers event to subscribers (used by distributed…** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.publish() with multiple subscribers.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Mock event class for testing.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test _handle_task_result_async() with successful task.** (1 connections) — `server/tests/unit/events/test_event_bus.py`

## Relationships

- [test_event_bus.py](test_event_bus.py.md) (11 shared connections)
- [asyncio](asyncio.md) (9 shared connections)
- [test_event_bus_publish_no_subscribers](test_event_bus_publish_no_subscribers.md) (1 shared connections)
- [test_handle_event_async_async_subscriber_error](test_handle_event_async_async_subscriber_error.md) (1 shared connections)
- [test_handle_event_async_no_subscribers](test_handle_event_async_no_subscribers.md) (1 shared connections)
- [test_handle_event_async_sync_subscriber_error](test_handle_event_async_sync_subscriber_error.md) (1 shared connections)
- [test_handle_task_result_async_with_error](test_handle_task_result_async_with_error.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (1 shared connections)

## Source Files

- `server/tests/unit/events/test_event_bus.py`

## Audit Trail

- EXTRACTED: 40 (95%)
- INFERRED: 2 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*