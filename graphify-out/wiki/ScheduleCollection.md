# ScheduleCollection

> 17 nodes

## Key Concepts

- **ScheduleCollection** (12 connections) — `server/schemas/calendar/calendar.py`
- **calendar/__init__.py** (10 connections) — `server/schemas/calendar/__init__.py`
- **calendar/calendar.py** (9 connections) — `server/schemas/calendar/calendar.py`
- **extract_observance_ids()** (8 connections) — `server/schemas/calendar/calendar.py`
- **slugify_observance()** (6 connections) — `server/schemas/calendar/calendar.py`
- **test_schedule_collection()** (4 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **BaseModel** (4 connections)
- **test_extract_observance_ids()** (3 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_slugify_observance()** (3 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **Calendar ingestion schemas for MythosMUD. These models provide a typed wrapper…** (1 connections) — `server/schemas/calendar/calendar.py`
- **Wrapper around an array of schedule entries.** (1 connections) — `server/schemas/calendar/calendar.py`
- **Normalize document observance names into snake_case ids.** (1 connections) — `server/schemas/calendar/calendar.py`
- **Parse table rows from MYTHOS_HOLIDAY_CANDIDATES.md into slug ids.** (1 connections) — `server/schemas/calendar/calendar.py`
- **Calendar domain schemas: holidays, schedules, and Mythos calendar.** (1 connections) — `server/schemas/calendar/__init__.py`
- **Test ScheduleCollection can be instantiated.** (1 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **Test slugify_observance() converts name to slug.** (1 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **Test extract_observance_ids() extracts IDs from markdown table lines.** (1 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`

## Relationships

- [DatabaseError](DatabaseError.md) (7 shared connections)
- [test_calendar_schemas.py](test_calendar_schemas.py.md) (6 shared connections)
- [validate_calendar.py](validate_calendar.py.md) (5 shared connections)
- [HolidayService](HolidayService.md) (3 shared connections)
- [HolidayCollection](HolidayCollection.md) (3 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (2 shared connections)
- [.load_file](load_file.md) (1 shared connections)

## Source Files

- `server/schemas/calendar/__init__.py`
- `server/schemas/calendar/calendar.py`
- `server/tests/unit/schemas/test_calendar_schemas.py`

## Audit Trail

- EXTRACTED: 47 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*