# Any

> 37 nodes

## Key Concepts

- **Any** (10 connections)
- **._handle_event_async()** (8 connections) — `server/events/event_bus.py`
- **._create_async_subscriber_tasks()** (6 connections) — `server/events/event_bus.py`
- **._ensure_async_processing()** (6 connections) — `server/events/event_bus.py`
- **._process_sync_subscribers()** (5 connections) — `server/events/event_bus.py`
- **._separate_subscribers()** (5 connections) — `server/events/event_bus.py`
- **.unsubscribe()** (5 connections) — `server/events/event_bus.py`
- **._wait_for_async_subscribers()** (5 connections) — `server/events/event_bus.py`
- **.get_subscriber_stats()** (4 connections) — `server/events/event_bus.py`
- **._handle_task_result_async()** (4 connections) — `server/events/event_bus.py`
- **.inject()** (4 connections) — `server/events/event_bus.py`
- **._process_events_async()** (4 connections) — `server/events/event_bus.py`
- **.publish()** (4 connections) — `server/events/event_bus.py`
- **.subscribe()** (4 connections) — `server/events/event_bus.py`
- **._ensure_processing_started()** (3 connections) — `server/events/event_bus.py`
- **.get_active_task_details()** (3 connections) — `server/events/event_bus.py`
- **.get_all_subscriber_counts()** (3 connections) — `server/events/event_bus.py`
- **.get_subscriber_lifecycle_metrics()** (3 connections) — `server/events/event_bus.py`
- **Task** (3 connections)
- **T** (2 connections)
- **Legacy wrapper for API compatibility during transition.** (1 connections) — `server/events/event_bus.py`
- **Pure async event processing loop replacing the dangerous threading pattern.** (1 connections) — `server/events/event_bus.py`
- **Separate async and sync subscribers for appropriate execution. Uses…** (1 connections) — `server/events/event_bus.py`
- **Execute sync subscribers sequentially with error isolation. Sync subscribers…** (1 connections) — `server/events/event_bus.py`
- **Create asyncio tasks for async event subscribers and track their lifecycle.…** (1 connections) — `server/events/event_bus.py`
- *... and 12 more nodes in this community*

## Relationships

- [ApplicationContainer](ApplicationContainer.md) (18 shared connections)
- [event_types.py](event_types.py.md) (6 shared connections)

## Source Files

- `server/events/event_bus.py`

## Audit Trail

- EXTRACTED: 66 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*