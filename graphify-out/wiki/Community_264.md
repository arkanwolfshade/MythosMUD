# Community 264

> 61 nodes

## Key Concepts

- **schedule_service.py** (25 connections) — `server/services/schedule_service.py`
- **holiday_service.py** (24 connections) — `server/services/holiday_service.py`
- **normalize_environment()** (15 connections) — `server/utils/project_paths.py`
- **project_paths.py** (15 connections) — `server/utils/project_paths.py`
- **get_calendar_paths_for_environment()** (14 connections) — `server/utils/project_paths.py`
- **get_project_root()** (12 connections) — `server/utils/project_paths.py`
- **test_schedule_service.py** (12 connections) — `server/tests/unit/services/test_schedule_service.py`
- **._init_temporal_services()** (10 connections) — `server/container/bundles/time.py`
- **_schedule_entry_from_row()** (10 connections) — `server/services/schedule_service.py`
- **test_project_paths.py** (10 connections) — `server/tests/unit/utils/test_project_paths.py`
- **get_environment_data_dir()** (8 connections) — `server/utils/project_paths.py`
- **._async_load_from_database()** (7 connections) — `server/services/schedule_service.py`
- **.__init__()** (7 connections) — `server/services/schedule_service.py`
- **_fetch_schedule_entries()** (6 connections) — `server/services/schedule_service.py`
- **_lower_string_list_from_row()** (6 connections) — `server/services/schedule_service.py`
- **_resolve_asyncpg_database_url()** (6 connections) — `server/services/schedule_service.py`
- **_string_list_from_row()** (6 connections) — `server/services/schedule_service.py`
- **normalize_weekday_names()** (5 connections) — `server/services/schedule_service.py`
- **.test_async_load_from_database_passes_search_path_for_mythos_e2e()** (5 connections) — `server/tests/unit/services/test_schedule_service.py`
- **_DatabaseLoadResult** (4 connections) — `server/services/schedule_service.py`
- **.test_resolve_asyncpg_database_url()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_resolve_asyncpg_database_url_missing()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_lower_string_list_from_row()** (3 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_string_list_from_row()** (3 connections) — `server/tests/unit/services/test_schedule_service.py`
- **test_get_calendar_paths_for_environment()** (3 connections) — `server/tests/unit/utils/test_project_paths.py`
- *... and 36 more nodes in this community*

## Relationships

- [Community 247](Community_247.md) (17 shared connections)
- [Community 114](Community_114.md) (17 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (17 shared connections)
- [Community 162](Community_162.md) (7 shared connections)
- [Core Bundle & DB Init](Core_Bundle_&_DB_Init.md) (6 shared connections)
- [Community 92](Community_92.md) (3 shared connections)
- [Community 457](Community_457.md) (3 shared connections)
- [Community 886](Community_886.md) (3 shared connections)
- [Community 906](Community_906.md) (3 shared connections)
- [Community 588](Community_588.md) (2 shared connections)
- [Community 274](Community_274.md) (2 shared connections)
- [Magic Service Lifespan](Magic_Service_Lifespan.md) (1 shared connections)

## Source Files

- `server/container/bundles/time.py`
- `server/services/holiday_service.py`
- `server/services/schedule_service.py`
- `server/tests/unit/services/test_schedule_service.py`
- `server/tests/unit/utils/test_project_paths.py`
- `server/utils/project_paths.py`

## Audit Trail

- EXTRACTED: 176 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*