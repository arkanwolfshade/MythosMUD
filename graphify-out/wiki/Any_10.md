# Any

> 33 nodes

## Key Concepts

- **Any** (10 connections)
- **._stop_processing()** (7 connections) — `server/events/event_bus.py`
- **.unsubscribe()** (5 connections) — `server/events/event_bus.py`
- **._wait_for_async_subscribers()** (5 connections) — `server/events/event_bus.py`
- **.get_subscriber_stats()** (4 connections) — `server/events/event_bus.py`
- **._handle_task_result_async()** (4 connections) — `server/events/event_bus.py`
- **.shutdown()** (4 connections) — `server/events/event_bus.py`
- **.subscribe()** (4 connections) — `server/events/event_bus.py`
- **.unsubscribe_all_for_service()** (4 connections) — `server/events/event_bus.py`
- **._cancel_and_wait_for_active_tasks()** (3 connections) — `server/events/event_bus.py`
- **._cancel_processing_task()** (3 connections) — `server/events/event_bus.py`
- **._finalize_shutdown()** (3 connections) — `server/events/event_bus.py`
- **.get_active_task_details()** (3 connections) — `server/events/event_bus.py`
- **.get_all_subscriber_counts()** (3 connections) — `server/events/event_bus.py`
- **.get_subscriber_lifecycle_metrics()** (3 connections) — `server/events/event_bus.py`
- **._signal_shutdown()** (3 connections) — `server/events/event_bus.py`
- **Task** (3 connections)
- **T** (2 connections)
- **Signal shutdown to async processing loop.** (1 connections) — `server/events/event_bus.py`
- **Cancel the main processing task if it exists.** (1 connections) — `server/events/event_bus.py`
- **Cancel all active tasks and wait for graceful shutdown.** (1 connections) — `server/events/event_bus.py`
- **Finalize shutdown by clearing tasks and logging.** (1 connections) — `server/events/event_bus.py`
- **Stop pure async event processing gracefully.** (1 connections) — `server/events/event_bus.py`
- **Wait for all async subscriber tasks to complete and handle their results. Uses…** (1 connections) — `server/events/event_bus.py`
- **Handle async task completion with proper exception extraction.** (1 connections) — `server/events/event_bus.py`
- *... and 8 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (20 shared connections)

## Source Files

- `server/events/event_bus.py`

## Audit Trail

- EXTRACTED: 54 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*