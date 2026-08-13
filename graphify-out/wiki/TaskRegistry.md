# TaskRegistry

> 142 nodes

## Key Concepts

- **TaskRegistry** (33 connections) — `server/app/task_registry.py`
- **MythosChronicle** (27 connections) — `server/time/time_service.py`
- **EventPublisher** (20 connections) — `server/realtime/event_publisher.py`
- **get_global_tracked_manager()** (17 connections) — `server/app/tracked_task_manager.py`
- **datetime** (15 connections)
- **TrackedTaskManager** (14 connections) — `server/app/tracked_task_manager.py`
- **tracked_task_manager.py** (14 connections) — `server/app/tracked_task_manager.py`
- **_ensure_utc()** (11 connections) — `server/time/time_service.py`
- **MemoryThresholdMonitor** (10 connections) — `server/app/memory_cleanup_service.py`
- **.get_calendar_components()** (10 connections) — `server/time/time_service.py`
- **memory_cleanup_service.py** (10 connections) — `server/app/memory_cleanup_service.py`
- **memory_lifespan_coordinator.py** (10 connections) — `server/app/memory_lifespan_coordinator.py`
- **ChronicleState** (9 connections) — `server/time/time_service.py`
- **.get_current_mythos_datetime()** (9 connections) — `server/time/time_service.py`
- **event_publisher.py** (9 connections) — `server/realtime/event_publisher.py`
- **game_tick_service.py** (9 connections) — `server/services/game_tick_service.py`
- **.get_daypart()** (8 connections) — `server/time/time_service.py`
- **._load_state()** (8 connections) — `server/time/time_service.py`
- **._persist_state()** (8 connections) — `server/time/time_service.py`
- **get_registry()** (7 connections) — `server/app/task_registry.py`
- **.shutdown_all()** (7 connections) — `server/app/task_registry.py`
- **._create_event_message()** (7 connections) — `server/realtime/event_publisher.py`
- **.__init__()** (7 connections) — `server/time/tick_scheduler.py`
- **.is_daytime()** (7 connections) — `server/time/time_service.py`
- **.is_witching_hour()** (7 connections) — `server/time/time_service.py`
- *... and 117 more nodes in this community*

## Relationships

- [ApplicationContainer](ApplicationContainer.md) (24 shared connections)
- [get_logger](get_logger.md) (16 shared connections)
- [Any](Any.md) (14 shared connections)
- [DatabaseError](DatabaseError.md) (7 shared connections)
- [PeriodicOrphanAuditor](PeriodicOrphanAuditor.md) (6 shared connections)
- [test_event_publisher.py](test_event_publisher.py.md) (5 shared connections)
- [test_event_publisher_helpers.py](test_event_publisher_helpers.py.md) (3 shared connections)
- [GameTickService](GameTickService.md) (3 shared connections)
- [.create_supervised_task](create_supervised_task.md) (2 shared connections)
- [api/monitoring.py](api-monitoring.py.md) (2 shared connections)
- [NPCEventHandler](NPCEventHandler.md) (2 shared connections)
- [event_types.py](event_types.py.md) (2 shared connections)

## Source Files

- `server/app/memory_cleanup_service.py`
- `server/app/memory_lifespan_coordinator.py`
- `server/app/task_registry.py`
- `server/app/tracked_task_manager.py`
- `server/realtime/event_publisher.py`
- `server/services/game_tick_service.py`
- `server/time/tick_scheduler.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 302 (97%)
- INFERRED: 10 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*