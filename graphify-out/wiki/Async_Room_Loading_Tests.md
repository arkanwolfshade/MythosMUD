# Async Room Loading Tests

> 20 nodes

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
- **test_schedule_collection()** (4 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **Path** (3 connections)
- **Calendar domain schemas: holidays, schedules, and Mythos calendar.** (1 connections) — `server/schemas/calendar/__init__.py`
- **Calendar ingestion schemas for MythosMUD.  These models provide a typed wrapper** (1 connections) — `server/schemas/calendar/calendar.py`
- **Load holiday collection from JSON file.** (1 connections) — `server/schemas/calendar/calendar.py`
- **Wrapper around an array of schedule entries.** (1 connections) — `server/schemas/calendar/calendar.py`
- **Load schedule collection from a JSON file.          Args:             path: Path** (1 connections) — `server/schemas/calendar/calendar.py`
- **Utility for loading every schedule file within a directory.** (1 connections) — `server/schemas/calendar/calendar.py`
- **Normalize document observance names into snake_case ids.** (1 connections) — `server/schemas/calendar/calendar.py`
- **Parse table rows from MYTHOS_HOLIDAY_CANDIDATES.md into slug ids.** (1 connections) — `server/schemas/calendar/calendar.py`
- **Test ScheduleCollection can be instantiated.** (1 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`

## Relationships

- [Player Command Developer Guide](Player_Command_Developer_Guide.md) (8 shared connections)
- [ASCII Map API](ASCII_Map_API.md) (5 shared connections)
- [Spell Effects Tests](Spell_Effects_Tests.md) (4 shared connections)
- [WebSocket Code Review](WebSocket_Code_Review.md) (4 shared connections)
- [Player Respawn Service](Player_Respawn_Service.md) (3 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (3 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (2 shared connections)

## Source Files

- `server/schemas/calendar/__init__.py`
- `server/schemas/calendar/calendar.py`
- `server/tests/unit/schemas/test_calendar_schemas.py`

## Audit Trail

- EXTRACTED: 83 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*