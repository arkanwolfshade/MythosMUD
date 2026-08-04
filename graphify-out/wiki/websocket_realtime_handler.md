# websocket realtime handler

> 43 nodes

## Key Concepts

- **game.py** (43 connections) — `server/container/bundles/game.py`
- **holiday_service.py** (24 connections) — `server/services/holiday_service.py`
- **normalize_environment()** (15 connections) — `server/utils/project_paths.py`
- **get_calendar_paths_for_environment()** (14 connections) — `server/utils/project_paths.py`
- **ChronicleLike** (13 connections) — `server/time/time_service.py`
- **project_paths.py** (12 connections) — `server/utils/project_paths.py`
- **test_project_paths.py** (10 connections) — `server/tests/unit/utils/test_project_paths.py`
- **get_project_root()** (10 connections) — `server/utils/project_paths.py`
- **get_environment_data_dir()** (10 connections) — `server/utils/project_paths.py`
- **.__init__()** (8 connections) — `server/services/holiday_service.py`
- **.__init__()** (7 connections) — `server/services/schedule_service.py`
- **_HolidayLoadResult** (5 connections) — `server/services/holiday_service.py`
- **._load_from_database()** (4 connections) — `server/services/holiday_service.py`
- **._resolve_hourly_holidays()** (3 connections) — `server/container/bundles/game.py`
- **test_get_project_root()** (3 connections) — `server/tests/unit/utils/test_project_paths.py`
- **test_normalize_environment()** (3 connections) — `server/tests/unit/utils/test_project_paths.py`
- **test_get_environment_data_dir()** (3 connections) — `server/tests/unit/utils/test_project_paths.py`
- **test_get_calendar_paths_for_environment()** (3 connections) — `server/tests/unit/utils/test_project_paths.py`
- **.get_current_mythos_datetime()** (3 connections) — `server/time/time_service.py`
- **.format_clock()** (3 connections) — `server/time/time_service.py`
- **Path** (3 connections)
- **datetime** (2 connections)
- **Path** (2 connections)
- **Path** (2 connections)
- **Game bundle: player, room, movement, exploration, user_manager, container_servic** (1 connections) — `server/container/bundles/game.py`
- *... and 18 more nodes in this community*

## Relationships

- [persistence rationale players](persistence_rationale_players.md) (16 shared connections)
- [holiday service services](holiday_service_services.md) (12 shared connections)
- [auth users rationale](auth_users_rationale.md) (11 shared connections)
- [time service rationale](time_service_rationale.md) (10 shared connections)
- [Loot Generation](Loot_Generation.md) (6 shared connections)
- [Database Config](Database_Config.md) (6 shared connections)
- [nats services service](nats_services_service.md) (4 shared connections)
- [Error Conversion](Error_Conversion.md) (4 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (4 shared connections)
- [startup npc service](startup_npc_service.md) (1 shared connections)
- [services lucidity repository](services_lucidity_repository.md) (1 shared connections)
- [dead letter realtime](dead_letter_realtime.md) (1 shared connections)

## Source Files

- `server/container/bundles/game.py`
- `server/services/holiday_service.py`
- `server/services/schedule_service.py`
- `server/tests/unit/utils/test_project_paths.py`
- `server/time/time_service.py`
- `server/utils/project_paths.py`

## Audit Trail

- EXTRACTED: 217 (97%)
- INFERRED: 7 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*