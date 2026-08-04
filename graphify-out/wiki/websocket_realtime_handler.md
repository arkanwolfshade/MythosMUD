# websocket realtime handler

> 111 nodes

## Key Concepts

- **GameBundle** (50 connections) — `server/container/bundles/game.py`
- **HolidayService** (45 connections) — `server/services/holiday_service.py`
- **game.py** (43 connections) — `server/container/bundles/game.py`
- **.initialize()** (35 connections) — `server/container/bundles/game.py`
- **HolidayEntry** (31 connections) — `server/schemas/calendar/calendar.py`
- **holiday_service.py** (24 connections) — `server/services/holiday_service.py`
- **InstanceManager** (19 connections) — `server/game/instance_manager.py`
- **normalize_environment()** (15 connections) — `server/utils/project_paths.py`
- **get_calendar_paths_for_environment()** (14 connections) — `server/utils/project_paths.py`
- **LevelService** (13 connections) — `server/game/level_service.py`
- **ChronicleLike** (13 connections) — `server/time/time_service.py`
- **project_paths.py** (12 connections) — `server/utils/project_paths.py`
- **._initialize_item_services()** (10 connections) — `server/container/bundles/game.py`
- **test_project_paths.py** (10 connections) — `server/tests/unit/utils/test_project_paths.py`
- **get_project_root()** (10 connections) — `server/utils/project_paths.py`
- **get_environment_data_dir()** (10 connections) — `server/utils/project_paths.py`
- **test_holiday_service.py** (9 connections) — `server/tests/unit/services/test_holiday_service.py`
- **_holiday_entry_from_row()** (8 connections) — `server/services/holiday_service.py`
- **.__init__()** (8 connections) — `server/services/holiday_service.py`
- **.get_upcoming_holidays()** (8 connections) — `server/services/holiday_service.py`
- **datetime** (7 connections)
- **._async_load_from_database()** (7 connections) — `server/services/holiday_service.py`
- **.refresh_active()** (7 connections) — `server/services/holiday_service.py`
- **.__init__()** (7 connections) — `server/services/schedule_service.py`
- **._initialize_caching_services()** (6 connections) — `server/container/bundles/game.py`
- *... and 86 more nodes in this community*

## Relationships

- [holiday service services](holiday_service_services.md) (53 shared connections)
- [nats services service](nats_services_service.md) (30 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (18 shared connections)
- [NPC Combat](NPC_Combat.md) (15 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (9 shared connections)
- [time service rationale](time_service_rationale.md) (8 shared connections)
- [endpoints auth rationale](endpoints_auth_rationale.md) (6 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (6 shared connections)
- [Database Config](Database_Config.md) (6 shared connections)
- [Exception Containers](Exception_Containers.md) (5 shared connections)
- [commands rescue rationale](commands_rescue_rationale.md) (5 shared connections)
- [command service commands](command_service_commands.md) (4 shared connections)

## Source Files

- `server/container/bundles/game.py`
- `server/game/instance_manager.py`
- `server/game/level_service.py`
- `server/schemas/calendar/calendar.py`
- `server/services/holiday_service.py`
- `server/services/schedule_service.py`
- `server/tests/unit/container/test_container_bundles.py`
- `server/tests/unit/services/test_holiday_service.py`
- `server/tests/unit/utils/test_project_paths.py`
- `server/time/time_service.py`
- `server/utils/project_paths.py`

## Audit Trail

- EXTRACTED: 538 (92%)
- INFERRED: 49 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*