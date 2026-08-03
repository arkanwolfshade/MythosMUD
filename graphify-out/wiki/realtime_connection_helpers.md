# realtime connection helpers

> 10 nodes

## Key Concepts

- **._stop_processing()** (7 connections) — `server/events/event_bus.py`
- **._signal_shutdown()** (3 connections) — `server/events/event_bus.py`
- **._cancel_processing_task()** (3 connections) — `server/events/event_bus.py`
- **._cancel_and_wait_for_active_tasks()** (3 connections) — `server/events/event_bus.py`
- **._finalize_shutdown()** (3 connections) — `server/events/event_bus.py`
- **Signal shutdown to async processing loop.** (1 connections) — `server/events/event_bus.py`
- **Cancel the main processing task if it exists.** (1 connections) — `server/events/event_bus.py`
- **Cancel all active tasks and wait for graceful shutdown.** (1 connections) — `server/events/event_bus.py`
- **Finalize shutdown by clearing tasks and logging.** (1 connections) — `server/events/event_bus.py`
- **Stop pure async event processing gracefully.** (1 connections) — `server/events/event_bus.py`

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (6 shared connections)

## Source Files

- `server/events/event_bus.py`

## Audit Trail

- EXTRACTED: 24 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*