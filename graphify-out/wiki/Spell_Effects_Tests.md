# Spell Effects Tests

> 152 nodes

## Key Concepts

- **HolidayService** (41 connections) — `server/services/holiday_service.py`
- **HolidayCollection** (37 connections) — `server/schemas/calendar/calendar.py`
- **HolidayEntry** (31 connections) — `server/schemas/calendar/calendar.py`
- **ScheduleEntry** (28 connections) — `server/schemas/calendar/calendar.py`
- **holiday_service.py** (24 connections) — `server/services/holiday_service.py`
- **test_calendar_schemas.py** (21 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **TestHolidayService** (20 connections) — `server/tests/unit/services/test_holiday_service.py`
- **ScheduleCollection** (12 connections) — `server/schemas/calendar/calendar.py`
- **__init__.py** (10 connections) — `server/schemas/calendar/__init__.py`
- **calendar.py** (9 connections) — `server/schemas/calendar/calendar.py`
- **load_schedule_directory()** (8 connections) — `server/schemas/calendar/calendar.py`
- **extract_observance_ids()** (8 connections) — `server/schemas/calendar/calendar.py`
- **.__init__()** (8 connections) — `server/services/holiday_service.py`
- **.get_upcoming_holidays()** (8 connections) — `server/services/holiday_service.py`
- **datetime** (7 connections)
- **.refresh_active()** (7 connections) — `server/services/holiday_service.py`
- **_load_and_validate_holidays()** (6 connections) — `scripts/validate_calendar.py`
- **_validate_schedule_files()** (6 connections) — `scripts/validate_calendar.py`
- **slugify_observance()** (6 connections) — `server/schemas/calendar/calendar.py`
- **_holiday_entry_from_row()** (6 connections) — `server/services/holiday_service.py`
- **._async_load_from_database()** (6 connections) — `server/services/holiday_service.py`
- **test_holiday_service.py** (6 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.load_file()** (5 connections) — `server/schemas/calendar/calendar.py`
- **.load_file()** (5 connections) — `server/schemas/calendar/calendar.py`
- **.get_active_holidays()** (5 connections) — `server/services/holiday_service.py`
- *... and 127 more nodes in this community*

## Relationships

- [WebSocket Code Review](WebSocket_Code_Review.md) (35 shared connections)
- [Combat Messaging Base](Combat_Messaging_Base.md) (9 shared connections)
- [Client Security Utilities](Client_Security_Utilities.md) (6 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (5 shared connections)
- [Spell Registry Costs](Spell_Registry_Costs.md) (5 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (3 shared connections)
- [Realtime Service Bundle](Realtime_Service_Bundle.md) (2 shared connections)
- [Player Respawn Service](Player_Respawn_Service.md) (2 shared connections)
- [Container Component Capacity](Container_Component_Capacity.md) (2 shared connections)
- [Command Factory Tests](Command_Factory_Tests.md) (2 shared connections)
- [Client Event Store](Client_Event_Store.md) (1 shared connections)
- [Realtime Npc Event](Realtime_Npc_Event.md) (1 shared connections)

## Source Files

- `scripts/validate_calendar.py`
- `server/npc/lifecycle_manager.py`
- `server/schemas/calendar/__init__.py`
- `server/schemas/calendar/calendar.py`
- `server/services/holiday_service.py`
- `server/tests/unit/schemas/test_calendar_schemas.py`
- `server/tests/unit/services/test_holiday_service.py`

## Audit Trail

- EXTRACTED: 570 (97%)
- INFERRED: 15 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*