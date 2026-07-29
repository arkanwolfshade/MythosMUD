# . create async subscriber tasks()

> 41 nodes

## Key Concepts

- **Any** (10 connections)
- **._handle_event_async()** (8 connections) — `server/events/event_bus.py`
- **._ensure_async_processing()** (6 connections) — `server/events/event_bus.py`
- **._create_async_subscriber_tasks()** (6 connections) — `server/events/event_bus.py`
- **.unsubscribe()** (6 connections) — `server/events/event_bus.py`
- **._separate_subscribers()** (5 connections) — `server/events/event_bus.py`
- **._process_sync_subscribers()** (5 connections) — `server/events/event_bus.py`
- **._wait_for_async_subscribers()** (5 connections) — `server/events/event_bus.py`
- **.subscribe()** (5 connections) — `server/events/event_bus.py`
- **._process_events_async()** (4 connections) — `server/events/event_bus.py`
- **._handle_task_result_async()** (4 connections) — `server/events/event_bus.py`
- **.publish()** (4 connections) — `server/events/event_bus.py`
- **.inject()** (4 connections) — `server/events/event_bus.py`
- **.unsubscribe_all_for_service()** (4 connections) — `server/events/event_bus.py`
- **.get_subscriber_stats()** (4 connections) — `server/events/event_bus.py`
- **.shutdown()** (4 connections) — `server/events/event_bus.py`
- **._ensure_processing_started()** (3 connections) — `server/events/event_bus.py`
- **Task** (3 connections)
- **.get_all_subscriber_counts()** (3 connections) — `server/events/event_bus.py`
- **.get_active_task_details()** (3 connections) — `server/events/event_bus.py`
- **.get_subscriber_lifecycle_metrics()** (3 connections) — `server/events/event_bus.py`
- **T** (2 connections)
- **Ensure async processing is started only when needed and within an event loop.** (1 connections) — `server/events/event_bus.py`
- **Legacy wrapper for API compatibility during transition.** (1 connections) — `server/events/event_bus.py`
- **Pure async event processing loop replacing the dangerous threading pattern.** (1 connections) — `server/events/event_bus.py`
- *... and 16 more nodes in this community*

## Relationships

- [.initialize()](initialize%28%29.md) (20 shared connections)
- [Any](Any.md) (8 shared connections)

## Source Files

- `server/events/event_bus.py`

## Audit Trail

- EXTRACTED: 118 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*