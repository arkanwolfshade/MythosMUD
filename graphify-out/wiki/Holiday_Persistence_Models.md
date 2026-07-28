# Holiday Persistence Models

> 146 nodes · cohesion 0.02

## Key Concepts

- **HolidayService** (41 connections) — `server/services/holiday_service.py`
- **HolidayCollection** (37 connections) — `server/schemas/calendar/calendar.py`
- **HolidayEntry** (31 connections) — `server/schemas/calendar/calendar.py`
- **holiday_service.py** (24 connections) — `server/services/holiday_service.py`
- **test_calendar_schemas.py** (21 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **TestHolidayService** (20 connections) — `server/tests/unit/services/test_holiday_service.py`
- **ChronicleLike** (13 connections) — `server/time/time_service.py`
- **ScheduleCollection** (12 connections) — `server/schemas/calendar/calendar.py`
- **__init__.py** (10 connections) — `server/schemas/calendar/__init__.py`
- **calendar.py** (9 connections) — `server/schemas/calendar/calendar.py`
- **extract_observance_ids()** (8 connections) — `server/schemas/calendar/calendar.py`
- **load_schedule_directory()** (8 connections) — `server/schemas/calendar/calendar.py`
- **.get_upcoming_holidays()** (8 connections) — `server/services/holiday_service.py`
- **.__init__()** (8 connections) — `server/services/holiday_service.py`
- **.refresh_active()** (7 connections) — `server/services/holiday_service.py`
- **datetime** (7 connections)
- **_load_and_validate_holidays()** (6 connections) — `scripts/validate_calendar.py`
- **_validate_schedule_files()** (6 connections) — `scripts/validate_calendar.py`
- **slugify_observance()** (6 connections) — `server/schemas/calendar/calendar.py`
- **_holiday_entry_from_row()** (6 connections) — `server/services/holiday_service.py`
- **._async_load_from_database()** (6 connections) — `server/services/holiday_service.py`
- **test_holiday_service.py** (6 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.load_file()** (5 connections) — `server/schemas/calendar/calendar.py`
- **.load_file()** (5 connections) — `server/schemas/calendar/calendar.py`
- **_HolidayLoadResult** (5 connections) — `server/services/holiday_service.py`
- *... and 121 more nodes in this community*

## Relationships

- [Calendar Holiday Schemas](Calendar_Holiday_Schemas.md) (27 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (10 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (7 shared connections)
- [System Monitoring API](System_Monitoring_API.md) (4 shared connections)
- [Weapon Resolution Helpers](Weapon_Resolution_Helpers.md) (4 shared connections)
- [Dependency Injection Tests](Dependency_Injection_Tests.md) (4 shared connections)
- [Api Player Respawn](Api_Player_Respawn.md) (4 shared connections)
- [Chat Panel Filtering](Chat_Panel_Filtering.md) (3 shared connections)
- [Lucidity Rate Overrides](Lucidity_Rate_Overrides.md) (2 shared connections)
- [Commands Inventory Item](Commands_Inventory_Item.md) (2 shared connections)
- [Quest Flow Integration](Quest_Flow_Integration.md) (2 shared connections)
- [NPC Admin API](NPC_Admin_API.md) (1 shared connections)

## Source Files

- `scripts/validate_calendar.py`
- `server/schemas/calendar/__init__.py`
- `server/schemas/calendar/calendar.py`
- `server/services/holiday_service.py`
- `server/tests/unit/schemas/test_calendar_schemas.py`
- `server/tests/unit/services/test_holiday_service.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 542 (96%)
- INFERRED: 20 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*