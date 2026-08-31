# ScheduleCollection

> 26 nodes

## Key Concepts

- **ScheduleCollection** (12 connections) — `server/schemas/calendar/calendar.py`
- **calendar/__init__.py** (11 connections) — `server/schemas/calendar/__init__.py`
- **calendar/calendar.py** (10 connections) — `server/schemas/calendar/calendar.py`
- **extract_observance_ids()** (8 connections) — `server/schemas/calendar/calendar.py`
- **load_schedule_directory()** (8 connections) — `server/schemas/calendar/calendar.py`
- **slugify_observance()** (6 connections) — `server/schemas/calendar/calendar.py`
- **.load_file()** (5 connections) — `server/schemas/calendar/calendar.py`
- **.load_file()** (5 connections) — `server/schemas/calendar/calendar.py`
- **BaseModel** (4 connections)
- **test_extract_observance_ids()** (3 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_holiday_collection_load_file()** (3 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_schedule_collection_load_file()** (3 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_slugify_observance()** (3 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **Path** (3 connections)
- **Calendar ingestion schemas for MythosMUD. These models provide a typed wrapper…** (1 connections) — `server/schemas/calendar/calendar.py`
- **Load holiday collection from JSON file.** (1 connections) — `server/schemas/calendar/calendar.py`
- **Wrapper around an array of schedule entries.** (1 connections) — `server/schemas/calendar/calendar.py`
- **Load schedule collection from a JSON file. Args: path: Path to the JSON file…** (1 connections) — `server/schemas/calendar/calendar.py`
- **Utility for loading every schedule file within a directory.** (1 connections) — `server/schemas/calendar/calendar.py`
- **Normalize document observance names into snake_case ids.** (1 connections) — `server/schemas/calendar/calendar.py`
- **Parse table rows from MYTHOS_HOLIDAY_CANDIDATES.md into slug ids.** (1 connections) — `server/schemas/calendar/calendar.py`
- **Calendar domain schemas: holidays, schedules, and Mythos calendar.** (1 connections) — `server/schemas/calendar/__init__.py`
- **Test HolidayCollection.load_file() loads from JSON.** (1 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **Test ScheduleCollection.load_file() loads from JSON.** (1 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **Test slugify_observance() converts name to slug.** (1 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- *... and 1 more nodes in this community*

## Relationships

- [HolidayEntry](HolidayEntry.md) (10 shared connections)
- [validate_calendar.py](validate_calendar.py.md) (5 shared connections)
- [ScheduleEntry](ScheduleEntry.md) (4 shared connections)
- [HolidayService](HolidayService.md) (4 shared connections)
- [server/services/__init__.py](server-services-__init__.py.md) (3 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (2 shared connections)
- [BaseCommand](BaseCommand.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/schemas/calendar/__init__.py`
- `server/schemas/calendar/calendar.py`
- `server/tests/unit/schemas/test_calendar_schemas.py`

## Audit Trail

- EXTRACTED: 63 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*