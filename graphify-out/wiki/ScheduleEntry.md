# ScheduleEntry

> 107 nodes · cohesion 0.03

## Key Concepts

- **ScheduleEntry** (28 connections) — `server/schemas/calendar/calendar.py`
- **ScheduleService** (28 connections) — `server/services/schedule_service.py`
- **schedule_service.py** (25 connections) — `server/services/schedule_service.py`
- **validate_calendar.py** (17 connections) — `scripts/validate_calendar.py`
- **normalize_environment()** (15 connections) — `server/utils/project_paths.py`
- **TestScheduleService** (14 connections) — `server/tests/unit/services/test_schedule_service.py`
- **get_calendar_paths_for_environment()** (14 connections) — `server/utils/project_paths.py`
- **project_paths.py** (12 connections) — `server/utils/project_paths.py`
- **test_project_paths.py** (10 connections) — `server/tests/unit/utils/test_project_paths.py`
- **get_environment_data_dir()** (10 connections) — `server/utils/project_paths.py`
- **get_project_root()** (10 connections) — `server/utils/project_paths.py`
- **run_validation()** (9 connections) — `scripts/validate_calendar.py`
- **_schedule_entry_from_row()** (8 connections) — `server/services/schedule_service.py`
- **test_schedule_service.py** (8 connections) — `server/tests/unit/services/test_schedule_service.py`
- **_get_calendar_paths()** (7 connections) — `scripts/validate_calendar.py`
- **._async_load_from_database()** (7 connections) — `server/services/schedule_service.py`
- **.__init__()** (7 connections) — `server/services/schedule_service.py`
- **_check_holiday_coverage()** (6 connections) — `scripts/validate_calendar.py`
- **Path** (6 connections)
- **_fetch_schedule_entries()** (6 connections) — `server/services/schedule_service.py`
- **_print_success_message()** (5 connections) — `scripts/validate_calendar.py`
- **_DatabaseLoadResult** (5 connections) — `server/services/schedule_service.py`
- **normalize_weekday_names()** (5 connections) — `server/services/schedule_service.py`
- **.test_async_load_from_database_passes_search_path_for_mythos_e2e()** (5 connections) — `server/tests/unit/services/test_schedule_service.py`
- **load_document_ids()** (4 connections) — `scripts/validate_calendar.py`
- *... and 82 more nodes in this community*

## Relationships

- [HolidayService](HolidayService.md) (27 shared connections)
- [__init__.py](__init__.py.md) (13 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (8 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (6 shared connections)
- [get_asyncpg_server_settings_for_database_url](get_asyncpg_server_settings_for_database_url.md) (2 shared connections)
- [dependencies.py](dependencies.py.md) (2 shared connections)
- [.get_instance](get_instance.md) (1 shared connections)

## Source Files

- `scripts/validate_calendar.py`
- `server/npc/lifecycle_manager.py`
- `server/schemas/calendar/calendar.py`
- `server/services/schedule_service.py`
- `server/tests/unit/services/test_schedule_service.py`
- `server/tests/unit/utils/test_project_paths.py`
- `server/utils/project_paths.py`

## Audit Trail

- EXTRACTED: 413 (97%)
- INFERRED: 14 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*