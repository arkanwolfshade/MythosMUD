# Async Task Registry

> 58 nodes · cohesion 0.06

## Key Concepts

- **TaskRegistry** (39 connections) — `server/app/task_registry.py`
- **MythosChronicle** (31 connections) — `server/time/time_service.py`
- **MythosHourTickEvent** (22 connections) — `server/events/event_types.py`
- **MythosTickScheduler** (22 connections) — `server/time/tick_scheduler.py`
- **tick_scheduler.py** (10 connections) — `server/time/tick_scheduler.py`
- **__init__.py** (8 connections) — `server/time/__init__.py`
- **.shutdown_all()** (7 connections) — `server/app/task_registry.py`
- **datetime** (7 connections) — `server/time/tick_scheduler.py`
- **.__init__()** (7 connections) — `server/time/tick_scheduler.py`
- **.get_task_lifecycle_metrics()** (5 connections) — `server/app/task_registry.py`
- **HolidayResolver** (5 connections) — `server/time/tick_scheduler.py`
- **MythosChronicle** (5 connections) — `server/time/tick_scheduler.py`
- **EventBus** (5 connections) — `server/time/tick_scheduler.py`
- **TaskRegistry** (5 connections) — `server/time/tick_scheduler.py`
- **._emit_pending_ticks()** (5 connections) — `server/time/tick_scheduler.py`
- **._publish_tick()** (5 connections) — `server/time/tick_scheduler.py`
- **._run()** (5 connections) — `server/time/tick_scheduler.py`
- **._cleanup_registry_collections()** (4 connections) — `server/app/task_registry.py`
- **._truncate_to_hour()** (4 connections) — `server/time/tick_scheduler.py`
- **._cancel_lifecycle_tasks()** (3 connections) — `server/app/task_registry.py`
- **._cancel_remaining_tasks()** (3 connections) — `server/app/task_registry.py`
- **._forcible_cleanup_on_timeout()** (3 connections) — `server/app/task_registry.py`
- **.get_active_task_count()** (3 connections) — `server/app/task_registry.py`
- **.get_task_stats_by_type()** (3 connections) — `server/app/task_registry.py`
- **._wait_for_task_completion()** (3 connections) — `server/app/task_registry.py`
- *... and 33 more nodes in this community*

## Relationships

- [[NPC Admin API]] (13 shared connections)
- [[Async Task Registry]] (12 shared connections)
- [[Time Event Consumer]] (10 shared connections)
- [[Mythos Calendar Time Service]] (10 shared connections)
- [[Distributed Event Bus]] (9 shared connections)
- [[Time Service]] (8 shared connections)
- [[Game Service Bundle]] (7 shared connections)
- [[App Tracked Task]] (3 shared connections)
- [[Game Tick Processing]] (3 shared connections)
- [[Monitoring API Endpoints]] (1 shared connections)
- [[NPC Combat Events]] (1 shared connections)
- [[Inventory Service Helpers]] (1 shared connections)

## Source Files

- `server/app/task_registry.py`
- `server/events/event_types.py`
- `server/time/__init__.py`
- `server/time/tick_scheduler.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 199 (76%)
- INFERRED: 63 (24%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
