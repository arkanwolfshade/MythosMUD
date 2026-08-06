# room realtime occupant

> 175 nodes

## Key Concepts

- **game.py** (43 connections) — `server/container/bundles/game.py`
- **.initialize()** (35 connections) — `server/container/bundles/game.py`
- **ScheduleService** (30 connections) — `server/services/schedule_service.py`
- **ScheduleEntry** (29 connections) — `server/schemas/calendar/calendar.py`
- **schedule_service.py** (25 connections) — `server/services/schedule_service.py`
- **TestScheduleService** (21 connections) — `server/tests/unit/services/test_schedule_service.py`
- **InstanceManager** (19 connections) — `server/game/instance_manager.py`
- **test_instance_manager.py** (15 connections) — `server/tests/unit/game/test_instance_manager.py`
- **normalize_environment()** (15 connections) — `server/utils/project_paths.py`
- **get_calendar_paths_for_environment()** (14 connections) — `server/utils/project_paths.py`
- **LevelService** (13 connections) — `server/game/level_service.py`
- **test_schedule_service.py** (12 connections) — `server/tests/unit/services/test_schedule_service.py`
- **project_paths.py** (12 connections) — `server/utils/project_paths.py`
- **_schedule_entry_from_row()** (10 connections) — `server/services/schedule_service.py`
- **test_project_paths.py** (10 connections) — `server/tests/unit/utils/test_project_paths.py`
- **get_project_root()** (10 connections) — `server/utils/project_paths.py`
- **get_environment_data_dir()** (10 connections) — `server/utils/project_paths.py`
- **.create_instance()** (7 connections) — `server/game/instance_manager.py`
- **.__init__()** (7 connections) — `server/services/schedule_service.py`
- **._async_load_from_database()** (7 connections) — `server/services/schedule_service.py`
- **._build_instance_rooms()** (6 connections) — `server/game/instance_manager.py`
- **_string_list_from_row()** (6 connections) — `server/services/schedule_service.py`
- **_lower_string_list_from_row()** (6 connections) — `server/services/schedule_service.py`
- **_resolve_asyncpg_database_url()** (6 connections) — `server/services/schedule_service.py`
- **_fetch_schedule_entries()** (6 connections) — `server/services/schedule_service.py`
- *... and 150 more nodes in this community*

## Relationships

- [player event handlers](player_event_handlers.md) (32 shared connections)
- [Error Conversion](Error_Conversion.md) (21 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (15 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (9 shared connections)
- [nats services service](nats_services_service.md) (6 shared connections)
- [commands rescue rationale](commands_rescue_rationale.md) (5 shared connections)
- [services lucidity repository](services_lucidity_repository.md) (2 shared connections)
- [game magic regeneration](game_magic_regeneration.md) (2 shared connections)
- [party service game](party_service_game.md) (2 shared connections)
- [skill game service](skill_game_service.md) (2 shared connections)
- [persistence core infrastructure](persistence_core_infrastructure.md) (2 shared connections)
- [quest game service](quest_game_service.md) (2 shared connections)

## Source Files

- `server/container/bundles/game.py`
- `server/game/instance_manager.py`
- `server/game/level_service.py`
- `server/npc/lifecycle_manager.py`
- `server/schemas/calendar/calendar.py`
- `server/services/schedule_service.py`
- `server/tests/unit/game/test_instance_manager.py`
- `server/tests/unit/schemas/test_calendar_schemas.py`
- `server/tests/unit/services/test_schedule_service.py`
- `server/tests/unit/utils/test_project_paths.py`
- `server/utils/project_paths.py`

## Audit Trail

- EXTRACTED: 646 (96%)
- INFERRED: 24 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*