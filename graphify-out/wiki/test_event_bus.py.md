# test_event_bus.py

> 44 nodes

## Key Concepts

- **test_event_bus.py** (59 connections) — `server/tests/unit/events/test_event_bus.py`
- **asyncio** (27 connections)
- **MockEventClass** (18 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_multiple_services_subscribe_same_events_integration()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_service_shutdown_removes_subscribers()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_inject_dispatches_to_subscribers()** (4 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_publish()** (4 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_publish_multiple_subscribers()** (4 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_publish_no_subscribers()** (4 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_event_async_async_subscriber_error()** (4 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_event_async_no_subscribers()** (4 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_event_async_sync_subscriber_error()** (4 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_task_result_async_no_error()** (4 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_task_result_async_with_error()** (4 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_inject_queue_full_and_invalid()** (4 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_shutdown_cleans_up_service_subscriptions()** (4 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_async_subscriber_error_isolation()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_multiple_services_subscribe_to_same_event()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_publish_isolates_sync_subscriber_errors()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_publish_queue_full_raises()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_stop_processing_and_publish_when_running()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_stop_processing_not_running()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_active_task_details_and_lifecycle_metrics()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_active_task_details_includes_exception()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_ensure_async_processing_no_loop_logs()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- *... and 19 more nodes in this community*

## Relationships

- [BaseEvent](BaseEvent.md) (5 shared connections)
- [EventBus](EventBus.md) (4 shared connections)
- [test_get_subscriber_stats](test_get_subscriber_stats.md) (4 shared connections)
- [NPCDefinition](NPCDefinition.md) (2 shared connections)
- [test_event_bus_shutdown](test_event_bus_shutdown.md) (2 shared connections)
- [test_event_bus_shutdown_idempotent](test_event_bus_shutdown_idempotent.md) (2 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [test_event_bus_set_main_loop](test_event_bus_set_main_loop.md) (1 shared connections)
- [test_event_bus_unsubscribe_multiple_handlers](test_event_bus_unsubscribe_multiple_handlers.md) (1 shared connections)
- [test_event_bus_get_all_subscriber_counts_empty](test_event_bus_get_all_subscriber_counts_empty.md) (1 shared connections)
- [test_event_bus_get_all_subscriber_counts_multiple_types](test_event_bus_get_all_subscriber_counts_multiple_types.md) (1 shared connections)

## Source Files

- `server/tests/unit/events/test_event_bus.py`

## Audit Trail

- EXTRACTED: 115 (94%)
- INFERRED: 7 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*