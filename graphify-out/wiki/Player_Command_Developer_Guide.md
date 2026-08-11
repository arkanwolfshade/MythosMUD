# Player Command Developer Guide

> 28 nodes

## Key Concepts

- **test_calendar_schemas.py** (21 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_holiday_entry_validation_tradition()** (4 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_holiday_entry_validation_season()** (4 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_holiday_entry_validation_bonus_tags()** (4 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_holiday_collection()** (4 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_holiday_collection_id_map()** (4 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_holiday_collection_ensure_unique_ids()** (4 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_schedule_entry_validation_days()** (4 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_holiday_entry()** (3 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_holiday_collection_load_file()** (3 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_schedule_entry()** (3 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_schedule_collection_load_file()** (3 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_slugify_observance()** (3 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_extract_observance_ids()** (3 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **Unit tests for calendar schemas.  Tests the Pydantic models in calendar.py modul** (1 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **Test HolidayEntry can be instantiated.** (1 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **Test HolidayEntry validates tradition.** (1 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **Test HolidayEntry validates season.** (1 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **Test HolidayEntry validates bonus_tags format.** (1 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **Test HolidayCollection can be instantiated.** (1 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **Test HolidayCollection.id_map property.** (1 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **Test HolidayCollection.load_file() loads from JSON.** (1 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **Test HolidayCollection.ensure_unique_ids() detects duplicates.** (1 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **Test ScheduleEntry can be instantiated.** (1 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **Test ScheduleEntry validates days.** (1 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- *... and 3 more nodes in this community*

## Relationships

- [Player Respawn Service](Player_Respawn_Service.md) (8 shared connections)
- [Async Room Loading Tests](Async_Room_Loading_Tests.md) (8 shared connections)
- [Spell Effects Tests](Spell_Effects_Tests.md) (4 shared connections)
- [Command Parser Helpers](Command_Parser_Helpers.md) (4 shared connections)
- [WebSocket Code Review](WebSocket_Code_Review.md) (3 shared connections)

## Source Files

- `server/tests/unit/schemas/test_calendar_schemas.py`

## Audit Trail

- EXTRACTED: 77 (95%)
- INFERRED: 4 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*