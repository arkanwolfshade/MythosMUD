# holiday service services

> 83 nodes

## Key Concepts

- **HolidayCollection** (41 connections) — `server/schemas/calendar/calendar.py`
- **HolidayEntry** (31 connections) — `server/schemas/calendar/calendar.py`
- **test_calendar_schemas.py** (21 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **validate_calendar.py** (17 connections) — `scripts/validate_calendar.py`
- **ScheduleCollection** (12 connections) — `server/schemas/calendar/calendar.py`
- **__init__.py** (10 connections) — `server/schemas/calendar/__init__.py`
- **run_validation()** (9 connections) — `scripts/validate_calendar.py`
- **calendar.py** (9 connections) — `server/schemas/calendar/calendar.py`
- **load_schedule_directory()** (8 connections) — `server/schemas/calendar/calendar.py`
- **extract_observance_ids()** (8 connections) — `server/schemas/calendar/calendar.py`
- **_get_calendar_paths()** (7 connections) — `scripts/validate_calendar.py`
- **Path** (6 connections)
- **_load_and_validate_holidays()** (6 connections) — `scripts/validate_calendar.py`
- **_check_holiday_coverage()** (6 connections) — `scripts/validate_calendar.py`
- **_validate_schedule_files()** (6 connections) — `scripts/validate_calendar.py`
- **slugify_observance()** (6 connections) — `server/schemas/calendar/calendar.py`
- **_print_success_message()** (5 connections) — `scripts/validate_calendar.py`
- **.load_file()** (5 connections) — `server/schemas/calendar/calendar.py`
- **.load_file()** (5 connections) — `server/schemas/calendar/calendar.py`
- **.test_init_loads_from_database()** (5 connections) — `server/tests/unit/services/test_holiday_service.py`
- **parse_args()** (4 connections) — `scripts/validate_calendar.py`
- **load_document_ids()** (4 connections) — `scripts/validate_calendar.py`
- **BaseModel** (4 connections)
- **test_holiday_entry_validation_tradition()** (4 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_holiday_entry_validation_season()** (4 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- *... and 58 more nodes in this community*

## Relationships

- [auth users rationale](auth_users_rationale.md) (30 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (12 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (9 shared connections)
- [inventory schemas schema](inventory_schemas_schema.md) (4 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (4 shared connections)
- [player requests schemas](player_requests_schemas.md) (2 shared connections)
- [game rationale schemas](game_rationale_schemas.md) (2 shared connections)

## Source Files

- `scripts/validate_calendar.py`
- `server/schemas/calendar/__init__.py`
- `server/schemas/calendar/calendar.py`
- `server/tests/unit/schemas/test_calendar_schemas.py`
- `server/tests/unit/services/test_holiday_service.py`

## Audit Trail

- EXTRACTED: 339 (98%)
- INFERRED: 6 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*