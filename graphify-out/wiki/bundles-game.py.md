# bundles/game.py

> 47 nodes

## Key Concepts

- **bundles/game.py** (41 connections) — `server/container/bundles/game.py`
- **schedule_service.py** (25 connections) — `server/services/schedule_service.py`
- **normalize_environment()** (17 connections) — `server/utils/project_paths.py`
- **project_paths.py** (15 connections) — `server/utils/project_paths.py`
- **get_calendar_paths_for_environment()** (14 connections) — `server/utils/project_paths.py`
- **get_project_root()** (14 connections) — `server/utils/project_paths.py`
- **test_schedule_service.py** (12 connections) — `server/tests/unit/services/test_schedule_service.py`
- **_schedule_entry_from_row()** (10 connections) — `server/services/schedule_service.py`
- **get_environment_data_dir()** (10 connections) — `server/utils/project_paths.py`
- **test_project_paths.py** (10 connections) — `server/tests/unit/utils/test_project_paths.py`
- **._async_load_from_database()** (7 connections) — `server/services/schedule_service.py`
- **.__init__()** (7 connections) — `server/services/schedule_service.py`
- **_fetch_schedule_entries()** (6 connections) — `server/services/schedule_service.py`
- **_lower_string_list_from_row()** (6 connections) — `server/services/schedule_service.py`
- **_resolve_asyncpg_database_url()** (6 connections) — `server/services/schedule_service.py`
- **_string_list_from_row()** (6 connections) — `server/services/schedule_service.py`
- **normalize_weekday_names()** (5 connections) — `server/services/schedule_service.py`
- **_DatabaseLoadResult** (4 connections) — `server/services/schedule_service.py`
- **test_get_calendar_paths_for_environment()** (3 connections) — `server/tests/unit/utils/test_project_paths.py`
- **test_get_environment_data_dir()** (3 connections) — `server/tests/unit/utils/test_project_paths.py`
- **test_get_project_root()** (3 connections) — `server/tests/unit/utils/test_project_paths.py`
- **test_normalize_environment()** (3 connections) — `server/tests/unit/utils/test_project_paths.py`
- **Path** (3 connections)
- **Connection** (1 connections)
- **Path** (1 connections)
- *... and 22 more nodes in this community*

## Relationships

- [ScheduleEntry](ScheduleEntry.md) (14 shared connections)
- [HolidayService](HolidayService.md) (12 shared connections)
- [HolidayCollection](HolidayCollection.md) (10 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (10 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [world](world.md) (3 shared connections)
- [test_dml_room_graph.py](test_dml_room_graph.py.md) (3 shared connections)
- [get_asyncpg_server_settings_for_database_url](get_asyncpg_server_settings_for_database_url.md) (2 shared connections)
- [Player](Player.md) (2 shared connections)
- [item_catalog_repository.py](item_catalog_repository.py.md) (2 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [DatabaseManager](DatabaseManager.md) (2 shared connections)

## Source Files

- `server/container/bundles/game.py`
- `server/services/schedule_service.py`
- `server/tests/unit/services/test_schedule_service.py`
- `server/tests/unit/utils/test_project_paths.py`
- `server/utils/project_paths.py`

## Audit Trail

- EXTRACTED: 177 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*