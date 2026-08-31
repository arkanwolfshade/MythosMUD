# schedule_service.py

> 48 nodes

## Key Concepts

- **schedule_service.py** (26 connections) — `server/services/schedule_service.py`
- **holiday_service.py** (25 connections) — `server/services/holiday_service.py`
- **validate_calendar.py** (18 connections) — `scripts/validate_calendar.py`
- **normalize_environment()** (17 connections) — `server/utils/project_paths.py`
- **get_calendar_paths_for_environment()** (14 connections) — `server/utils/project_paths.py`
- **project_paths.py** (13 connections) — `server/utils/project_paths.py`
- **._init_temporal_services()** (10 connections) — `server/container/bundles/time.py`
- **get_environment_data_dir()** (10 connections) — `server/utils/project_paths.py`
- **get_project_root()** (10 connections) — `server/utils/project_paths.py`
- **test_project_paths.py** (10 connections) — `server/tests/unit/utils/test_project_paths.py`
- **run_validation()** (9 connections) — `scripts/validate_calendar.py`
- **_get_calendar_paths()** (7 connections) — `scripts/validate_calendar.py`
- **.__init__()** (7 connections) — `server/services/schedule_service.py`
- **_check_holiday_coverage()** (6 connections) — `scripts/validate_calendar.py`
- **_load_and_validate_holidays()** (6 connections) — `scripts/validate_calendar.py`
- **_validate_schedule_files()** (6 connections) — `scripts/validate_calendar.py`
- **Path** (6 connections)
- **_print_success_message()** (5 connections) — `scripts/validate_calendar.py`
- **load_document_ids()** (4 connections) — `scripts/validate_calendar.py`
- **parse_args()** (4 connections) — `scripts/validate_calendar.py`
- **main()** (3 connections) — `scripts/validate_calendar.py`
- **_print_errors()** (3 connections) — `scripts/validate_calendar.py`
- **test_get_calendar_paths_for_environment()** (3 connections) — `server/tests/unit/utils/test_project_paths.py`
- **test_get_environment_data_dir()** (3 connections) — `server/tests/unit/utils/test_project_paths.py`
- **test_get_project_root()** (3 connections) — `server/tests/unit/utils/test_project_paths.py`
- *... and 23 more nodes in this community*

## Relationships

- [HolidayService](HolidayService.md) (14 shared connections)
- [ScheduleEntry](ScheduleEntry.md) (14 shared connections)
- [get_logger](get_logger.md) (12 shared connections)
- [HolidayEntry](HolidayEntry.md) (8 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (5 shared connections)
- [time_event_consumer.py](time_event_consumer.py.md) (3 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (3 shared connections)
- [connection_manager.py](connection_manager.py.md) (3 shared connections)
- [_holiday_entry_from_row](_holiday_entry_from_row.md) (3 shared connections)
- [MythosTickScheduler](MythosTickScheduler.md) (2 shared connections)
- [server/services/__init__.py](server-services-__init__.py.md) (2 shared connections)
- [asyncio.md](asyncio.md.md) (2 shared connections)

## Source Files

- `scripts/validate_calendar.py`
- `server/container/bundles/time.py`
- `server/services/holiday_service.py`
- `server/services/schedule_service.py`
- `server/tests/unit/utils/test_project_paths.py`
- `server/utils/project_paths.py`

## Audit Trail

- EXTRACTED: 169 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*