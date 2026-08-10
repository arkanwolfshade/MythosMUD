# UI Player Event Handlers

> 51 nodes

## Key Concepts

- **Any** (10 connections)
- **._handle_event_async()** (8 connections) — `server/events/event_bus.py`
- **._stop_processing()** (7 connections) — `server/events/event_bus.py`
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
- **._signal_shutdown()** (3 connections) — `server/events/event_bus.py`
- **._cancel_processing_task()** (3 connections) — `server/events/event_bus.py`
- **._cancel_and_wait_for_active_tasks()** (3 connections) — `server/events/event_bus.py`
- **._finalize_shutdown()** (3 connections) — `server/events/event_bus.py`
- **Task** (3 connections)
- **.get_all_subscriber_counts()** (3 connections) — `server/events/event_bus.py`
- **.get_active_task_details()** (3 connections) — `server/events/event_bus.py`
- *... and 26 more nodes in this community*

## Relationships

- [Level and XP Curve](Level_and_XP_Curve.md) (24 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (8 shared connections)

## Source Files

- `server/events/event_bus.py`

## Audit Trail

- EXTRACTED: 142 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*