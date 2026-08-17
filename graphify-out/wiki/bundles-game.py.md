# bundles/game.py

> 117 nodes

## Key Concepts

- **bundles/game.py** (44 connections) — `server/container/bundles/game.py`
- **ScheduleService** (28 connections) — `server/services/schedule_service.py`
- **schedule_service.py** (26 connections) — `server/services/schedule_service.py`
- **TestScheduleService** (21 connections) — `server/tests/unit/services/test_schedule_service.py`
- **get_container()** (19 connections) — `server/container/main.py`
- **container/__init__.py** (17 connections) — `server/container/__init__.py`
- **normalize_environment()** (15 connections) — `server/utils/project_paths.py`
- **get_calendar_paths_for_environment()** (14 connections) — `server/utils/project_paths.py`
- **project_paths.py** (12 connections) — `server/utils/project_paths.py`
- **_schedule_entry_from_row()** (10 connections) — `server/services/schedule_service.py`
- **get_environment_data_dir()** (10 connections) — `server/utils/project_paths.py`
- **get_project_root()** (10 connections) — `server/utils/project_paths.py`
- **test_project_paths.py** (10 connections) — `server/tests/unit/utils/test_project_paths.py`
- **utils.py** (8 connections) — `server/container/utils.py`
- **decode_json_column()** (7 connections) — `server/container/utils.py`
- **._async_load_from_database()** (7 connections) — `server/services/schedule_service.py`
- **.__init__()** (7 connections) — `server/services/schedule_service.py`
- **_fetch_schedule_entries()** (6 connections) — `server/services/schedule_service.py`
- **_lower_string_list_from_row()** (6 connections) — `server/services/schedule_service.py`
- **_resolve_asyncpg_database_url()** (6 connections) — `server/services/schedule_service.py`
- **_string_list_from_row()** (6 connections) — `server/services/schedule_service.py`
- **normalize_path_from_url_or_path()** (5 connections) — `server/container/utils.py`
- **normalize_weekday_names()** (5 connections) — `server/services/schedule_service.py`
- **._load_from_database()** (5 connections) — `server/services/schedule_service.py`
- **.test_async_load_from_database_passes_search_path_for_mythos_e2e()** (5 connections) — `server/tests/unit/services/test_schedule_service.py`
- *... and 92 more nodes in this community*

## Relationships

- [HolidayCollection](HolidayCollection.md) (32 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (23 shared connections)
- [HolidayService](HolidayService.md) (13 shared connections)
- [get_logger](get_logger.md) (11 shared connections)
- [.get_instance](get_instance.md) (8 shared connections)
- [pytest.md](pytest.md.md) (3 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (3 shared connections)
- [._init_player_quest_layer](_init_player_quest_layer.md) (3 shared connections)
- [database_config_helpers.py](database_config_helpers.py.md) (3 shared connections)
- [inventory_equip_command.py](inventory_equip_command.py.md) (2 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (2 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (2 shared connections)

## Source Files

- `server/container/__init__.py`
- `server/container/bundles/game.py`
- `server/container/main.py`
- `server/container/utils.py`
- `server/services/schedule_service.py`
- `server/tests/unit/services/test_schedule_service.py`
- `server/tests/unit/utils/test_project_paths.py`
- `server/utils/project_paths.py`

## Audit Trail

- EXTRACTED: 307 (99%)
- INFERRED: 4 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*