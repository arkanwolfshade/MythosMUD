# Combat Messaging Base

> 45 nodes

## Key Concepts

- **HolidayService** (41 connections) — `server/services/holiday_service.py`
- **HolidayEntry** (31 connections) — `server/schemas/calendar/calendar.py`
- **holiday_service.py** (24 connections) — `server/services/holiday_service.py`
- **.get_upcoming_holidays()** (8 connections) — `server/services/holiday_service.py`
- **datetime** (7 connections)
- **.refresh_active()** (7 connections) — `server/services/holiday_service.py`
- **_holiday_entry_from_row()** (6 connections) — `server/services/holiday_service.py`
- **._async_load_from_database()** (6 connections) — `server/services/holiday_service.py`
- **test_holiday_service.py** (6 connections) — `server/tests/unit/services/test_holiday_service.py`
- **_HolidayLoadResult** (5 connections) — `server/services/holiday_service.py`
- **.get_active_holidays()** (5 connections) — `server/services/holiday_service.py`
- **.get_serialized_active_holidays()** (5 connections) — `server/services/holiday_service.py`
- **.test_init_loads_from_database()** (5 connections) — `server/tests/unit/services/test_holiday_service.py`
- **_ensure_utc()** (4 connections) — `server/services/holiday_service.py`
- **.get_serialized_upcoming_holidays()** (4 connections) — `server/services/holiday_service.py`
- **_string_list_from_row()** (3 connections) — `server/services/holiday_service.py`
- **.get_active_holiday_names()** (3 connections) — `server/services/holiday_service.py`
- **.get_upcoming_summary()** (3 connections) — `server/services/holiday_service.py`
- **._day_ordinal()** (3 connections) — `server/services/holiday_service.py`
- **.last_refresh()** (3 connections) — `server/services/holiday_service.py`
- **.validate_tradition()** (2 connections) — `server/schemas/calendar/calendar.py`
- **.validate_season()** (2 connections) — `server/schemas/calendar/calendar.py`
- **.validate_bonus_tags()** (2 connections) — `server/schemas/calendar/calendar.py`
- **Record** (2 connections)
- **Single holiday definition loaded from data/<env>/calendar/holidays.json.** (1 connections) — `server/schemas/calendar/calendar.py`
- *... and 20 more nodes in this community*

## Relationships

- [Spell Effects Tests](Spell_Effects_Tests.md) (25 shared connections)
- [Client Event Store](Client_Event_Store.md) (12 shared connections)
- [Minimap Fallback Helpers](Minimap_Fallback_Helpers.md) (9 shared connections)
- [Client Security Utilities](Client_Security_Utilities.md) (5 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (4 shared connections)
- [Container Repository CRUD](Container_Repository_CRUD.md) (4 shared connections)
- [Chat Channel Logger](Chat_Channel_Logger.md) (3 shared connections)
- [Error Handling Guide](Error_Handling_Guide.md) (2 shared connections)
- [Player Respawn Service](Player_Respawn_Service.md) (2 shared connections)
- [Container Component Capacity](Container_Component_Capacity.md) (2 shared connections)
- [Game Terminal Panels](Game_Terminal_Panels.md) (1 shared connections)
- [Realtime Conftest Mocks](Realtime_Conftest_Mocks.md) (1 shared connections)

## Source Files

- `server/schemas/calendar/calendar.py`
- `server/services/holiday_service.py`
- `server/tests/unit/services/test_holiday_service.py`

## Audit Trail

- EXTRACTED: 197 (95%)
- INFERRED: 11 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*