# bundles/game.py

> 71 nodes

## Key Concepts

- **bundles/game.py** (42 connections) — `server/container/bundles/game.py`
- **schedule_service.py** (25 connections) — `server/services/schedule_service.py`
- **validate_calendar.py** (17 connections) — `scripts/validate_calendar.py`
- **normalize_environment()** (15 connections) — `server/utils/project_paths.py`
- **get_calendar_paths_for_environment()** (14 connections) — `server/utils/project_paths.py`
- **project_paths.py** (12 connections) — `server/utils/project_paths.py`
- **get_environment_data_dir()** (10 connections) — `server/utils/project_paths.py`
- **get_project_root()** (10 connections) — `server/utils/project_paths.py`
- **test_project_paths.py** (10 connections) — `server/tests/unit/utils/test_project_paths.py`
- **run_validation()** (9 connections) — `scripts/validate_calendar.py`
- **_schedule_entry_from_row()** (8 connections) — `server/services/schedule_service.py`
- **_get_calendar_paths()** (7 connections) — `scripts/validate_calendar.py`
- **._async_load_from_database()** (7 connections) — `server/services/schedule_service.py`
- **.__init__()** (7 connections) — `server/services/schedule_service.py`
- **_check_holiday_coverage()** (6 connections) — `scripts/validate_calendar.py`
- **_fetch_schedule_entries()** (6 connections) — `server/services/schedule_service.py`
- **Path** (6 connections)
- **_DatabaseLoadResult** (5 connections) — `server/services/schedule_service.py`
- **_print_success_message()** (5 connections) — `scripts/validate_calendar.py`
- **normalize_weekday_names()** (5 connections) — `server/services/schedule_service.py`
- **.test_async_load_from_database_passes_search_path_for_mythos_e2e()** (5 connections) — `server/tests/unit/services/test_schedule_service.py`
- **load_document_ids()** (4 connections) — `scripts/validate_calendar.py`
- **parse_args()** (4 connections) — `scripts/validate_calendar.py`
- **_lower_string_list_from_row()** (4 connections) — `server/services/schedule_service.py`
- **.get_active_entries()** (4 connections) — `server/services/schedule_service.py`
- *... and 46 more nodes in this community*

## Relationships

- [HolidayService](HolidayService.md) (28 shared connections)
- [ScheduleService](ScheduleService.md) (12 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (11 shared connections)
- [GameBundle](GameBundle.md) (7 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (5 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (3 shared connections)
- [ProfessionCacheService](ProfessionCacheService.md) (1 shared connections)
- [RoomCacheService](RoomCacheService.md) (1 shared connections)
- [MovementService](MovementService.md) (1 shared connections)
- [ExplorationService](ExplorationService.md) (1 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (1 shared connections)

## Source Files

- `scripts/validate_calendar.py`
- `server/container/bundles/game.py`
- `server/services/schedule_service.py`
- `server/tests/unit/services/test_schedule_service.py`
- `server/tests/unit/utils/test_project_paths.py`
- `server/utils/project_paths.py`

## Audit Trail

- EXTRACTED: 206 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*