# schemas player rationale

> 39 nodes

## Key Concepts

- **TrackedTaskManager** (22 connections) — `server/app/tracked_task_manager.py`
- **get_global_tracked_manager()** (20 connections) — `server/app/tracked_task_manager.py`
- **test_tracked_task_manager.py** (18 connections) — `server/tests/unit/app/test_tracked_task_manager.py`
- **tracked_task_manager.py** (15 connections) — `server/app/tracked_task_manager.py`
- **memory_cleanup_service.py** (11 connections) — `server/app/memory_cleanup_service.py`
- **game_tick_service.py** (9 connections) — `server/services/game_tick_service.py`
- **memory_leak_prevention_channel_start_session()** (5 connections) — `server/app/tracked_task_manager.py`
- **reset_global_tracked_manager()** (4 connections) — `server/app/tracked_task_manager.py`
- **patch_asyncio_create_task_with_tracking()** (4 connections) — `server/app/tracked_task_manager.py`
- **.__init__()** (3 connections) — `server/app/tracked_task_manager.py`
- **.set_task_registry()** (3 connections) — `server/app/tracked_task_manager.py`
- **.audit_orphans()** (2 connections) — `server/app/tracked_task_manager.py`
- **.cleanup_orphaned_tasks()** (2 connections) — `server/app/tracked_task_manager.py`
- **.actively_tracked_task_count()** (2 connections) — `server/app/tracked_task_manager.py`
- **reset_global()** (2 connections) — `server/tests/unit/app/test_tracked_task_manager.py`
- **test_create_tracked_task_runs_coro()** (2 connections) — `server/tests/unit/app/test_tracked_task_manager.py`
- **test_create_tracked_task_with_registry()** (2 connections) — `server/tests/unit/app/test_tracked_task_manager.py`
- **test_create_tracked_task_registry_failure_falls_back()** (2 connections) — `server/tests/unit/app/test_tracked_task_manager.py`
- **test_create_supervised_task_completes()** (2 connections) — `server/tests/unit/app/test_tracked_task_manager.py`
- **test_audit_orphans_counts_untracked()** (2 connections) — `server/tests/unit/app/test_tracked_task_manager.py`
- **test_cleanup_orphaned_tasks_cancels_running()** (2 connections) — `server/tests/unit/app/test_tracked_task_manager.py`
- **test_global_manager_singleton()** (2 connections) — `server/tests/unit/app/test_tracked_task_manager.py`
- **test_set_task_registry()** (2 connections) — `server/tests/unit/app/test_tracked_task_manager.py`
- **test_memory_leak_prevention_session_start()** (2 connections) — `server/tests/unit/app/test_tracked_task_manager.py`
- **test_patch_asyncio_create_task_with_tracking()** (2 connections) — `server/tests/unit/app/test_tracked_task_manager.py`
- *... and 14 more nodes in this community*

## Relationships

- [Loot Generation](Loot_Generation.md) (6 shared connections)
- [dialogue definitions admin](dialogue_definitions_admin.md) (6 shared connections)
- [combat attack handler](combat_attack_handler.md) (5 shared connections)
- [follow service game](follow_service_game.md) (5 shared connections)
- [realtime monitoring performance](realtime_monitoring_performance.md) (3 shared connections)
- [tick service services](tick_service_services.md) (3 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (2 shared connections)
- [startup services npc](startup_services_npc.md) (2 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (2 shared connections)
- [event publisher realtime](event_publisher_realtime.md) (2 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)
- [nats services service](nats_services_service.md) (1 shared connections)

## Source Files

- `server/app/memory_cleanup_service.py`
- `server/app/tracked_task_manager.py`
- `server/services/game_tick_service.py`
- `server/tests/unit/app/test_tracked_task_manager.py`

## Audit Trail

- EXTRACTED: 152 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*