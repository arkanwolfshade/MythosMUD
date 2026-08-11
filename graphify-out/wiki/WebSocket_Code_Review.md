# WebSocket Code Review

> 172 nodes

## Key Concepts

- **game.py** (42 connections) — `server/container/bundles/game.py`
- **main.py** (33 connections) — `server/container/main.py`
- **ScheduleService** (28 connections) — `server/services/schedule_service.py`
- **schedule_service.py** (25 connections) — `server/services/schedule_service.py`
- **CombatBundle** (21 connections) — `server/container/bundles/combat.py`
- **__init__.py** (19 connections) — `server/container/bundles/__init__.py`
- **core.py** (18 connections) — `server/container/bundles/core.py`
- **validate_calendar.py** (17 connections) — `scripts/validate_calendar.py`
- **RealtimeBundle** (17 connections) — `server/container/bundles/realtime.py`
- **normalize_environment()** (15 connections) — `server/utils/project_paths.py`
- **TrackedTaskManager** (14 connections) — `server/app/tracked_task_manager.py`
- **CoreBundle** (14 connections) — `server/container/bundles/core.py`
- **TestScheduleService** (14 connections) — `server/tests/unit/services/test_schedule_service.py`
- **get_calendar_paths_for_environment()** (14 connections) — `server/utils/project_paths.py`
- **combat.py** (13 connections) — `server/container/bundles/combat.py`
- **MonitoringBundle** (13 connections) — `server/container/bundles/monitoring.py`
- **.initialize()** (12 connections) — `server/container/bundles/core.py`
- **realtime.py** (12 connections) — `server/container/bundles/realtime.py`
- **DistributedEventBus** (12 connections) — `server/events/distributed_event_bus.py`
- **project_paths.py** (12 connections) — `server/utils/project_paths.py`
- **monitoring.py** (11 connections) — `server/container/bundles/monitoring.py`
- **._initialize_primary_bundles()** (10 connections) — `server/container/main.py`
- **test_project_paths.py** (10 connections) — `server/tests/unit/utils/test_project_paths.py`
- **get_project_root()** (10 connections) — `server/utils/project_paths.py`
- **get_environment_data_dir()** (10 connections) — `server/utils/project_paths.py`
- *... and 147 more nodes in this community*

## Relationships

- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (43 shared connections)
- [Spell Effects Tests](Spell_Effects_Tests.md) (35 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (20 shared connections)
- [Command Factory Tests](Command_Factory_Tests.md) (14 shared connections)
- [Client Security Utilities](Client_Security_Utilities.md) (11 shared connections)
- [Player Respawn Events](Player_Respawn_Events.md) (6 shared connections)
- [Spell Registry Costs](Spell_Registry_Costs.md) (6 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (6 shared connections)
- [NPC Spawn Validator](NPC_Spawn_Validator.md) (6 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (5 shared connections)
- [Client Event Store](Client_Event_Store.md) (5 shared connections)
- [Realtime Service Bundle](Realtime_Service_Bundle.md) (5 shared connections)

## Source Files

- `scripts/validate_calendar.py`
- `server/app/tracked_task_manager.py`
- `server/container/__init__.py`
- `server/container/bundles/__init__.py`
- `server/container/bundles/chat.py`
- `server/container/bundles/combat.py`
- `server/container/bundles/core.py`
- `server/container/bundles/game.py`
- `server/container/bundles/monitoring.py`
- `server/container/bundles/realtime.py`
- `server/container/bundles/time.py`
- `server/container/main.py`
- `server/container/utils.py`
- `server/events/distributed_event_bus.py`
- `server/services/schedule_service.py`
- `server/tests/unit/services/test_schedule_service.py`
- `server/tests/unit/utils/test_project_paths.py`
- `server/utils/project_paths.py`

## Audit Trail

- EXTRACTED: 749 (94%)
- INFERRED: 50 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*