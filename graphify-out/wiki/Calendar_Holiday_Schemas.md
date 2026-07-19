# Calendar Holiday Schemas

> 71 nodes · cohesion 0.04

## Key Concepts

- **HolidayEntry** (26 connections) — `server/schemas/calendar/calendar.py`
- **ScheduleEntry** (23 connections) — `server/schemas/calendar/calendar.py`
- **test_calendar_schemas.py** (21 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **ScheduleCollection** (11 connections) — `server/schemas/calendar/calendar.py`
- **__init__.py** (10 connections) — `server/schemas/calendar/__init__.py`
- **calendar.py** (9 connections) — `server/schemas/calendar/calendar.py`
- **extract_observance_ids()** (8 connections) — `server/schemas/calendar/calendar.py`
- **load_schedule_directory()** (8 connections) — `server/schemas/calendar/calendar.py`
- **test_schedule_service.py** (7 connections) — `server/tests/unit/services/test_schedule_service.py`
- **slugify_observance()** (6 connections) — `server/schemas/calendar/calendar.py`
- **_DatabaseLoadResult** (5 connections) — `server/services/schedule_service.py`
- **.load_file()** (4 connections) — `server/schemas/calendar/calendar.py`
- **test_holiday_collection()** (4 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_holiday_collection_ensure_unique_ids()** (4 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_holiday_collection_id_map()** (4 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_schedule_collection()** (4 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **.id_map()** (3 connections) — `server/schemas/calendar/calendar.py`
- **.load_file()** (3 connections) — `server/schemas/calendar/calendar.py`
- **.validate_duration()** (3 connections) — `server/schemas/calendar/calendar.py`
- **test_extract_observance_ids()** (3 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_holiday_entry()** (3 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_holiday_entry_validation_bonus_tags()** (3 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_holiday_entry_validation_season()** (3 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_holiday_entry_validation_tradition()** (3 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_schedule_entry()** (3 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- *... and 46 more nodes in this community*

## Relationships

- [[Holiday Persistence Models]] (12 shared connections)
- [[Schedule Service Loader]] (10 shared connections)
- [[Admin NPC Schemas]] (8 shared connections)
- [[NPC Admin API]] (5 shared connections)
- [[Validate Calendar]] (4 shared connections)
- [[Game Status API]] (2 shared connections)
- [[NPC Death Lifecycle]] (1 shared connections)
- [[Dependency Risk Analyzer]] (1 shared connections)
- [[Async Persistence Layer]] (1 shared connections)
- [[Lucidity Rate Overrides]] (1 shared connections)
- [[Game Service Bundle]] (1 shared connections)

## Source Files

- `server/schemas/calendar/__init__.py`
- `server/schemas/calendar/calendar.py`
- `server/services/schedule_service.py`
- `server/tests/unit/schemas/test_calendar_schemas.py`
- `server/tests/unit/services/test_holiday_service.py`
- `server/tests/unit/services/test_schedule_service.py`

## Audit Trail

- EXTRACTED: 241 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
