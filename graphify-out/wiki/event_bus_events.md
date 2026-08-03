# event bus events

> 80 nodes

## Key Concepts

- **test_event_bus.py** (45 connections) — `server/tests/unit/events/test_event_bus.py`
- **MockEventClass** (29 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_subscribe()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_subscribe_multiple()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_unsubscribe()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_unsubscribe_not_found()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_get_subscriber_count()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_get_subscriber_count_none()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_get_all_subscriber_counts()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_publish()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_unsubscribe_multiple_handlers()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_get_all_subscriber_counts_multiple_types()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_publish_no_subscribers()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_inject_dispatches_to_subscribers()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_publish_multiple_subscribers()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_subscribe_invalid_handler()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_event_async_no_subscribers()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_event_async_sync_subscriber_error()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_event_async_async_subscriber_error()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_task_result_async_no_error()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_task_result_async_with_error()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_subscribe_with_service_id()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_unsubscribe_all_for_service()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_unsubscribe_all_for_service_partial_cleanup()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_get_subscriber_stats()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- *... and 55 more nodes in this community*

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (4 shared connections)
- [item models rationale](item_models_rationale.md) (3 shared connections)

## Source Files

- `server/tests/unit/events/test_event_bus.py`

## Audit Trail

- EXTRACTED: 171 (80%)
- INFERRED: 44 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*