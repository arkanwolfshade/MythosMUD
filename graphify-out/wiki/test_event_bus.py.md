# test_event_bus.py

> 84 nodes

## Key Concepts

- **test_event_bus.py** (46 connections) — `server/tests/unit/events/test_event_bus.py`
- **asyncio** (17 connections)
- **MockEventClass** (13 connections) — `server/tests/unit/events/test_event_bus.py`
- **event_bus()** (4 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_inject_dispatches_to_subscribers()** (4 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_publish()** (4 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_publish_multiple_subscribers()** (4 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_publish_no_subscribers()** (4 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_event_async_async_subscriber_error()** (4 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_event_async_no_subscribers()** (4 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_event_async_sync_subscriber_error()** (4 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_task_result_async_no_error()** (4 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_task_result_async_with_error()** (4 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_shutdown()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_shutdown_idempotent()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_multiple_services_subscribe_same_events_integration()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_multiple_services_subscribe_to_same_event()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_service_shutdown_removes_subscribers()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_shutdown_cleans_up_service_subscriptions()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_stop_processing_not_running()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_ensure_processing_started()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_get_all_subscriber_counts()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_get_all_subscriber_counts_empty()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_get_all_subscriber_counts_multiple_types()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_get_subscriber_count()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- *... and 59 more nodes in this community*

## Relationships

- [EventBus](EventBus.md) (4 shared connections)
- [BaseEvent](BaseEvent.md) (2 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (1 shared connections)

## Source Files

- `server/tests/unit/events/test_event_bus.py`

## Audit Trail

- EXTRACTED: 221 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*