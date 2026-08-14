# asyncio

> 30 nodes

## Key Concepts

- **asyncio** (27 connections)
- **MockEventClass** (19 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_inject_dispatches_to_subscribers()** (4 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_publish()** (4 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_publish_multiple_subscribers()** (4 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_publish_no_subscribers()** (4 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_event_async_async_subscriber_error()** (4 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_event_async_no_subscribers()** (4 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_event_async_sync_subscriber_error()** (4 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_task_result_async_no_error()** (4 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_inject_queue_full_and_invalid()** (4 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_async_subscriber_error_isolation()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_publish_isolates_sync_subscriber_errors()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_publish_queue_full_raises()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_stop_processing_and_publish_when_running()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_active_task_details_and_lifecycle_metrics()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_active_task_details_includes_exception()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_ensure_async_processing_no_loop_logs()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_inject_and_get_all_counts()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_set_main_loop_and_ensure_processing()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_signal_shutdown_and_cancel_helpers()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.publish() queues or processes event.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.publish() with no subscribers.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.inject() delivers event to subscribers (used by distributed…** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.publish() with multiple subscribers.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- *... and 5 more nodes in this community*

## Relationships

- [test_event_bus.py](test_event_bus.py.md) (21 shared connections)
- [test_handle_task_result_async_with_error](test_handle_task_result_async_with_error.md) (2 shared connections)
- [EventBus](EventBus.md) (1 shared connections)
- [event_types.py](event_types.py.md) (1 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (1 shared connections)
- [test_event_bus_shutdown](test_event_bus_shutdown.md) (1 shared connections)
- [test_event_bus_shutdown_idempotent](test_event_bus_shutdown_idempotent.md) (1 shared connections)
- [test_multiple_services_subscribe_same_events_integration](test_multiple_services_subscribe_same_events_integration.md) (1 shared connections)
- [test_multiple_services_subscribe_to_same_event](test_multiple_services_subscribe_to_same_event.md) (1 shared connections)
- [test_service_shutdown_removes_subscribers](test_service_shutdown_removes_subscribers.md) (1 shared connections)
- [test_shutdown_cleans_up_service_subscriptions](test_shutdown_cleans_up_service_subscriptions.md) (1 shared connections)
- [test_stop_processing_not_running](test_stop_processing_not_running.md) (1 shared connections)

## Source Files

- `server/tests/unit/events/test_event_bus.py`

## Audit Trail

- EXTRACTED: 71 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*