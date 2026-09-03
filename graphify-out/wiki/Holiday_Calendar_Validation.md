# Holiday Calendar Validation

> 189 nodes

## Key Concepts

- **HolidayService** (44 connections) — `server/services/holiday_service.py`
- **HolidayCollection** (40 connections) — `server/schemas/calendar/calendar.py`
- **HolidayEntry** (31 connections) — `server/schemas/calendar/calendar.py`
- **ScheduleEntry** (27 connections) — `server/schemas/calendar/calendar.py`
- **TestHolidayService** (27 connections) — `server/tests/unit/services/test_holiday_service.py`
- **holiday_service.py** (25 connections) — `server/services/holiday_service.py`
- **test_calendar_schemas.py** (23 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **validate_calendar.py** (18 connections) — `scripts/validate_calendar.py`
- **ScheduleCollection** (12 connections) — `server/schemas/calendar/calendar.py`
- **ChronicleLike** (12 connections) — `server/time/time_service.py`
- **calendar/__init__.py** (11 connections) — `server/schemas/calendar/__init__.py`
- **calendar/calendar.py** (10 connections) — `server/schemas/calendar/calendar.py`
- **test_holiday_service.py** (10 connections) — `server/tests/unit/services/test_holiday_service.py`
- **run_validation()** (9 connections) — `scripts/validate_calendar.py`
- **extract_observance_ids()** (8 connections) — `server/schemas/calendar/calendar.py`
- **load_schedule_directory()** (8 connections) — `server/schemas/calendar/calendar.py`
- **_holiday_entry_from_row()** (8 connections) — `server/services/holiday_service.py`
- **.get_upcoming_holidays()** (8 connections) — `server/services/holiday_service.py`
- **.__init__()** (8 connections) — `server/services/holiday_service.py`
- **_get_calendar_paths()** (7 connections) — `scripts/validate_calendar.py`
- **._async_load_from_database()** (7 connections) — `server/services/holiday_service.py`
- **.refresh_active()** (7 connections) — `server/services/holiday_service.py`
- **_check_holiday_coverage()** (6 connections) — `scripts/validate_calendar.py`
- **_load_and_validate_holidays()** (6 connections) — `scripts/validate_calendar.py`
- **_validate_schedule_files()** (6 connections) — `scripts/validate_calendar.py`
- *... and 164 more nodes in this community*

## Relationships

- [Test Schedule Service](Test_Schedule_Service.md) (22 shared connections)
- [Application Container Bundles](Application_Container_Bundles.md) (15 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (7 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (7 shared connections)
- [Npc Admin](Npc_Admin.md) (5 shared connections)
- [Time Service](Time_Service.md) (5 shared connections)
- [Async Persistence](Async_Persistence.md) (3 shared connections)
- [Command Aliases](Command_Aliases.md) (3 shared connections)
- [Equipment & Inventory Helpers](Equipment_&_Inventory_Helpers.md) (2 shared connections)
- [Test Rate Overrides](Test_Rate_Overrides.md) (2 shared connections)
- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (1 shared connections)
- [Database](Database.md) (1 shared connections)

## Source Files

- `scripts/validate_calendar.py`
- `server/schemas/calendar/__init__.py`
- `server/schemas/calendar/calendar.py`
- `server/services/holiday_service.py`
- `server/tests/unit/schemas/test_calendar_schemas.py`
- `server/tests/unit/services/test_holiday_service.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 403 (99%)
- INFERRED: 6 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*