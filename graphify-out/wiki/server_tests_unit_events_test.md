# server tests unit events test

> 94 nodes

## Key Concepts

- **test_event_bus.py** (59 connections) — `server/tests/unit/events/test_event_bus.py`
- **asyncio** (27 connections)
- **MockEventClass** (18 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_multiple_services_subscribe_same_events_integration()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_service_shutdown_removes_subscribers()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
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
- **test_inject_queue_full_and_invalid()** (4 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_shutdown_cleans_up_service_subscriptions()** (4 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_async_subscriber_error_isolation()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_get_all_subscriber_counts_multiple_types()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_shutdown()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_shutdown_idempotent()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_get_subscriber_stats()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_multiple_services_subscribe_to_same_event()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_publish_isolates_sync_subscriber_errors()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_publish_queue_full_raises()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- *... and 69 more nodes in this community*

## Relationships

- [moduletype](moduletype.md) (8 shared connections)
- [server events event bus eventbus](server_events_event_bus_eventbus.md) (5 shared connections)
- [server events event bus](server_events_event_bus.md) (2 shared connections)
- [object](object.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/tests/unit/events/test_event_bus.py`

## Audit Trail

- EXTRACTED: 141 (93%)
- INFERRED: 11 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*