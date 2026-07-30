# hash password()

> 30 nodes

## Key Concepts

- **validate_calendar.py** (17 connections) — `scripts/validate_calendar.py`
- **run_validation()** (9 connections) — `scripts/validate_calendar.py`
- **load_schedule_directory()** (8 connections) — `server/schemas/calendar/calendar.py`
- **_get_calendar_paths()** (7 connections) — `scripts/validate_calendar.py`
- **Path** (6 connections)
- **_load_and_validate_holidays()** (6 connections) — `scripts/validate_calendar.py`
- **_check_holiday_coverage()** (6 connections) — `scripts/validate_calendar.py`
- **_validate_schedule_files()** (6 connections) — `scripts/validate_calendar.py`
- **_print_success_message()** (5 connections) — `scripts/validate_calendar.py`
- **.load_file()** (5 connections) — `server/schemas/calendar/calendar.py`
- **.load_file()** (5 connections) — `server/schemas/calendar/calendar.py`
- **parse_args()** (4 connections) — `scripts/validate_calendar.py`
- **load_document_ids()** (4 connections) — `scripts/validate_calendar.py`
- **Namespace** (3 connections)
- **_print_errors()** (3 connections) — `scripts/validate_calendar.py`
- **main()** (3 connections) — `scripts/validate_calendar.py`
- **Path** (3 connections)
- **test_holiday_collection_load_file()** (3 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_schedule_collection_load_file()** (3 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **Get holidays and schedules paths.** (1 connections) — `scripts/validate_calendar.py`
- **Load and validate holidays.** (1 connections) — `scripts/validate_calendar.py`
- **Check if holidays cover documentation references.** (1 connections) — `scripts/validate_calendar.py`
- **Load and validate schedule files.** (1 connections) — `scripts/validate_calendar.py`
- **Print validation errors.** (1 connections) — `scripts/validate_calendar.py`
- **Print success message if not quiet.** (1 connections) — `scripts/validate_calendar.py`
- *... and 5 more nodes in this community*

## Relationships

- [HolidayCollection](HolidayCollection.md) (14 shared connections)
- [test command parser](test_command_parser.md) (7 shared connections)

## Source Files

- `scripts/validate_calendar.py`
- `server/schemas/calendar/calendar.py`
- `server/tests/unit/schemas/test_calendar_schemas.py`

## Audit Trail

- EXTRACTED: 117 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*