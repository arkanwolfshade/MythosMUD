# Server Schemas (2)

> 74 nodes

## Key Concepts

- **ScheduleEntry** (28 connections) — `server/schemas/calendar/calendar.py`
- **test_calendar_schemas.py** (21 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **validate_calendar.py** (17 connections) — `scripts/validate_calendar.py`
- **ScheduleCollection** (12 connections) — `server/schemas/calendar/calendar.py`
- **__init__.py** (10 connections) — `server/schemas/calendar/__init__.py`
- **run_validation()** (9 connections) — `scripts/validate_calendar.py`
- **calendar.py** (9 connections) — `server/schemas/calendar/calendar.py`
- **load_schedule_directory()** (8 connections) — `server/schemas/calendar/calendar.py`
- **extract_observance_ids()** (8 connections) — `server/schemas/calendar/calendar.py`
- **test_schedule_service.py** (8 connections) — `server/tests/unit/services/test_schedule_service.py`
- **_get_calendar_paths()** (7 connections) — `scripts/validate_calendar.py`
- **Path** (6 connections)
- **_load_and_validate_holidays()** (6 connections) — `scripts/validate_calendar.py`
- **_check_holiday_coverage()** (6 connections) — `scripts/validate_calendar.py`
- **_validate_schedule_files()** (6 connections) — `scripts/validate_calendar.py`
- **slugify_observance()** (6 connections) — `server/schemas/calendar/calendar.py`
- **_print_success_message()** (5 connections) — `scripts/validate_calendar.py`
- **.load_file()** (5 connections) — `server/schemas/calendar/calendar.py`
- **.load_file()** (5 connections) — `server/schemas/calendar/calendar.py`
- **parse_args()** (4 connections) — `scripts/validate_calendar.py`
- **load_document_ids()** (4 connections) — `scripts/validate_calendar.py`
- **BaseModel** (4 connections)
- **test_holiday_entry_validation_tradition()** (4 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_holiday_entry_validation_season()** (4 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_holiday_entry_validation_bonus_tags()** (4 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- *... and 49 more nodes in this community*

## Relationships

- [Server Services (15)](Server_Services_%2815%29.md) (21 shared connections)
- [Server Utils (14)](Server_Utils_%2814%29.md) (15 shared connections)
- [Server Services (50)](Server_Services_%2850%29.md) (12 shared connections)
- [Server Utils](Server_Utils.md) (4 shared connections)
- [Server Admin](Server_Admin.md) (3 shared connections)
- [Server Npc (2)](Server_Npc_%282%29.md) (2 shared connections)

## Source Files

- `scripts/validate_calendar.py`
- `server/npc/lifecycle_manager.py`
- `server/schemas/calendar/__init__.py`
- `server/schemas/calendar/calendar.py`
- `server/tests/unit/schemas/test_calendar_schemas.py`
- `server/tests/unit/services/test_schedule_service.py`

## Audit Trail

- EXTRACTED: 283 (99%)
- INFERRED: 4 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*