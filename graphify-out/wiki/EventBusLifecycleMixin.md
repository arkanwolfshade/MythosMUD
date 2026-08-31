# EventBusLifecycleMixin

> 30 nodes

## Key Concepts

- **EventBusLifecycleMixin** (18 connections) — `server/events/event_bus_lifecycle.py`
- **._cancel_task_quietly()** (7 connections) — `server/events/event_bus_lifecycle.py`
- **._stop_processing()** (7 connections) — `server/events/event_bus_lifecycle.py`
- **.shutdown()** (6 connections) — `server/events/event_bus_lifecycle.py`
- **._abandon_pending_tasks()** (5 connections) — `server/events/event_bus_lifecycle.py`
- **._cancel_and_wait_for_active_tasks()** (5 connections) — `server/events/event_bus_lifecycle.py`
- **._cancel_active_tasks_best_effort()** (4 connections) — `server/events/event_bus_lifecycle.py`
- **._warn_shutdown_error()** (4 connections) — `server/events/event_bus_lifecycle.py`
- **._cancel_processing_task()** (3 connections) — `server/events/event_bus_lifecycle.py`
- **._cleanup_tracked_subscriptions()** (3 connections) — `server/events/event_bus_lifecycle.py`
- **.__del__()** (3 connections) — `server/events/event_bus_lifecycle.py`
- **._finalize_shutdown()** (3 connections) — `server/events/event_bus_lifecycle.py`
- **._signal_shutdown()** (3 connections) — `server/events/event_bus_lifecycle.py`
- **._ensure_async_processing()** (2 connections) — `server/events/event_bus_lifecycle.py`
- **Task** (2 connections)
- **Exception** (1 connections)
- **Cancel leftover tasks after the grace wait, then give them a short drain.** (1 connections) — `server/events/event_bus_lifecycle.py`
- **Cancel all active tasks and wait for graceful shutdown.** (1 connections) — `server/events/event_bus_lifecycle.py`
- **Finalize shutdown by clearing tasks and logging.** (1 connections) — `server/events/event_bus_lifecycle.py`
- **Stop pure async event processing gracefully.** (1 connections) — `server/events/event_bus_lifecycle.py`
- **Unsubscribe every tracked service. No-op when none are registered.** (1 connections) — `server/events/event_bus_lifecycle.py`
- **Log a non-fatal shutdown error without letting logging fail the process.** (1 connections) — `server/events/event_bus_lifecycle.py`
- **Shutdown the pure asyncio event bus with proper grace period coordination. This…** (1 connections) — `server/events/event_bus_lifecycle.py`
- **Mixin: on-demand processing start, graceful stop, and destruction.** (1 connections) — `server/events/event_bus_lifecycle.py`
- **Cancel subscriber tasks if a loop is still running; always clear the set.** (1 connections) — `server/events/event_bus_lifecycle.py`
- *... and 5 more nodes in this community*

## Relationships

- [NPCLifecycleManager](NPCLifecycleManager.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [EventBus](EventBus.md) (1 shared connections)

## Source Files

- `server/events/event_bus_lifecycle.py`

## Audit Trail

- EXTRACTED: 47 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*