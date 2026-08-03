# time service rationale

> 272 nodes

## Key Concepts

- **time.py** (89 connections) — `server/container/bundles/time.py`
- **lifespan.py** (42 connections) — `server/app/lifespan.py`
- **TaskRegistry** (33 connections) — `server/app/task_registry.py`
- **MythosChronicle** (27 connections) — `server/time/time_service.py`
- **time_service.py** (25 connections) — `server/time/time_service.py`
- **time_event_consumer.py** (24 connections) — `server/time/time_event_consumer.py`
- **get_mythos_chronicle()** (24 connections) — `server/time/time_service.py`
- **MythosTimeEventConsumer** (21 connections) — `server/time/time_event_consumer.py`
- **get_global_tracked_manager()** (18 connections) — `server/app/tracked_task_manager.py`
- **MythosTickScheduler** (18 connections) — `server/time/tick_scheduler.py`
- **lifespan()** (15 connections) — `server/app/lifespan.py`
- **lifespan_shutdown.py** (15 connections) — `server/app/lifespan_shutdown.py`
- **datetime** (15 connections)
- **tracked_task_manager.py** (14 connections) — `server/app/tracked_task_manager.py`
- **TrackedTaskManager** (14 connections) — `server/app/tracked_task_manager.py`
- **tick_scheduler.py** (14 connections) — `server/time/tick_scheduler.py`
- **memory_leak_metrics.py** (13 connections) — `server/monitoring/memory_leak_metrics.py`
- **ChronicleLike** (13 connections) — `server/time/time_service.py`
- **shutdown_services()** (12 connections) — `server/app/lifespan_shutdown.py`
- **MythosHourTickEvent** (12 connections) — `server/events/event_types.py`
- **_ensure_utc()** (11 connections) — `server/time/time_service.py`
- **_shutdown_with_error_handling()** (10 connections) — `server/app/lifespan.py`
- **memory_cleanup_service.py** (10 connections) — `server/app/memory_cleanup_service.py`
- **MemoryThresholdMonitor** (10 connections) — `server/app/memory_cleanup_service.py`
- **memory_lifespan_coordinator.py** (10 connections) — `server/app/memory_lifespan_coordinator.py`
- *... and 247 more nodes in this community*

## Relationships

- [command inventory factories](command_inventory_factories.md) (44 shared connections)
- [Error Conversion](Error_Conversion.md) (32 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (20 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (14 shared connections)
- [Room Broadcast](Room_Broadcast.md) (11 shared connections)
- [holiday service services](holiday_service_services.md) (9 shared connections)
- [tick game processing](tick_game_processing.md) (8 shared connections)
- [command combat models](command_combat_models.md) (6 shared connections)
- [System Metrics](System_Metrics.md) (6 shared connections)
- [Database Config](Database_Config.md) (6 shared connections)
- [Player Name Validation](Player_Name_Validation.md) (5 shared connections)
- [item models rationale](item_models_rationale.md) (5 shared connections)

## Source Files

- `server/app/lifespan.py`
- `server/app/lifespan_shutdown.py`
- `server/app/memory_cleanup_service.py`
- `server/app/memory_lifespan_coordinator.py`
- `server/app/task_registry.py`
- `server/app/tracked_task_manager.py`
- `server/container/bundles/time.py`
- `server/events/event_types.py`
- `server/monitoring/memory_leak_metrics.py`
- `server/services/game_tick_service.py`
- `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- `server/tests/unit/test_main.py`
- `server/time/__init__.py`
- `server/time/tick_scheduler.py`
- `server/time/time_event_consumer.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 1116 (96%)
- INFERRED: 46 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*