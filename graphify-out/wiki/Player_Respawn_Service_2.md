# Player Respawn Service

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

- [Spell Effects Tests](Spell_Effects_Tests.md) (24 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (12 shared connections)
- [Player Command Developer Guide](Player_Command_Developer_Guide.md) (8 shared connections)
- [Client Event Store](Client_Event_Store.md) (8 shared connections)
- [Async Room Loading Tests](Async_Room_Loading_Tests.md) (3 shared connections)
- [Chat Panel Filtering](Chat_Panel_Filtering.md) (3 shared connections)
- [Test Migration Report](Test_Migration_Report.md) (2 shared connections)
- [Container Component Capacity](Container_Component_Capacity.md) (2 shared connections)
- [Exploration Command Factory](Exploration_Command_Factory.md) (2 shared connections)
- [Cursor Skills Critique](Cursor_Skills_Critique.md) (2 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (1 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (1 shared connections)

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