# commands party examples

> 18 nodes

## Key Concepts

- **ScheduleCollection** (12 connections) — `server/schemas/calendar/calendar.py`
- **__init__.py** (10 connections) — `server/schemas/calendar/__init__.py`
- **calendar.py** (9 connections) — `server/schemas/calendar/calendar.py`
- **load_schedule_directory()** (8 connections) — `server/schemas/calendar/calendar.py`
- **extract_observance_ids()** (8 connections) — `server/schemas/calendar/calendar.py`
- **slugify_observance()** (6 connections) — `server/schemas/calendar/calendar.py`
- **.load_file()** (5 connections) — `server/schemas/calendar/calendar.py`
- **.load_file()** (5 connections) — `server/schemas/calendar/calendar.py`
- **BaseModel** (4 connections)
- **Path** (3 connections)
- **Calendar domain schemas: holidays, schedules, and Mythos calendar.** (1 connections) — `server/schemas/calendar/__init__.py`
- **Calendar ingestion schemas for MythosMUD.  These models provide a typed wrapper** (1 connections) — `server/schemas/calendar/calendar.py`
- **Load holiday collection from JSON file.** (1 connections) — `server/schemas/calendar/calendar.py`
- **Wrapper around an array of schedule entries.** (1 connections) — `server/schemas/calendar/calendar.py`
- **Load schedule collection from a JSON file.          Args:             path: Path** (1 connections) — `server/schemas/calendar/calendar.py`
- **Utility for loading every schedule file within a directory.** (1 connections) — `server/schemas/calendar/calendar.py`
- **Normalize document observance names into snake_case ids.** (1 connections) — `server/schemas/calendar/calendar.py`
- **Parse table rows from MYTHOS_HOLIDAY_CANDIDATES.md into slug ids.** (1 connections) — `server/schemas/calendar/calendar.py`

## Relationships

- [schemas calendar rationale](schemas_calendar_rationale.md) (7 shared connections)
- [schedule services service](schedule_services_service.md) (5 shared connections)
- [calendar schemas validate](calendar_schemas_validate.md) (5 shared connections)
- [holiday service services](holiday_service_services.md) (4 shared connections)
- [project paths rationale](project_paths_rationale.md) (3 shared connections)
- [Player Stats](Player_Stats.md) (2 shared connections)
- [NATS Messaging](NATS_Messaging.md) (1 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (1 shared connections)

## Source Files

- `server/schemas/calendar/__init__.py`
- `server/schemas/calendar/calendar.py`

## Audit Trail

- EXTRACTED: 78 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*