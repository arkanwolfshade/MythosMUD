# Player Command Developer Guide

> 56 nodes

## Key Concepts

- **ScheduleEntry** (28 connections) — `server/schemas/calendar/calendar.py`
- **test_calendar_schemas.py** (21 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **ScheduleCollection** (12 connections) — `server/schemas/calendar/calendar.py`
- **__init__.py** (10 connections) — `server/schemas/calendar/__init__.py`
- **calendar.py** (9 connections) — `server/schemas/calendar/calendar.py`
- **extract_observance_ids()** (8 connections) — `server/schemas/calendar/calendar.py`
- **slugify_observance()** (6 connections) — `server/schemas/calendar/calendar.py`
- **BaseModel** (4 connections)
- **._load_from_database()** (4 connections) — `server/services/schedule_service.py`
- **test_holiday_entry_validation_tradition()** (4 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_holiday_entry_validation_season()** (4 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_holiday_entry_validation_bonus_tags()** (4 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_holiday_collection()** (4 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_holiday_collection_id_map()** (4 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_holiday_collection_ensure_unique_ids()** (4 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_schedule_entry_validation_days()** (4 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_schedule_collection()** (4 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **.apply_schedule_state()** (3 connections) — `server/npc/lifecycle_manager.py`
- **.validate_duration()** (3 connections) — `server/schemas/calendar/calendar.py`
- **.entries()** (3 connections) — `server/services/schedule_service.py`
- **test_holiday_entry()** (3 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_holiday_collection_load_file()** (3 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_schedule_entry()** (3 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_schedule_collection_load_file()** (3 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_slugify_observance()** (3 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- *... and 31 more nodes in this community*

## Relationships

- [WebSocket Code Review](WebSocket_Code_Review.md) (16 shared connections)
- [ASCII Map API](ASCII_Map_API.md) (15 shared connections)
- [Player Respawn Service](Player_Respawn_Service.md) (11 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (4 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (3 shared connections)
- [Level and XP Curve](Level_and_XP_Curve.md) (2 shared connections)
- [Real-Time Architecture Docs](Real-Time_Architecture_Docs.md) (2 shared connections)

## Source Files

- `server/npc/lifecycle_manager.py`
- `server/schemas/calendar/__init__.py`
- `server/schemas/calendar/calendar.py`
- `server/services/schedule_service.py`
- `server/tests/unit/schemas/test_calendar_schemas.py`

## Audit Trail

- EXTRACTED: 189 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*