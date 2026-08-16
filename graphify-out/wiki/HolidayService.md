# HolidayService

> 167 nodes

## Key Concepts

- **HolidayService** (44 connections) — `server/services/holiday_service.py`
- **HolidayCollection** (40 connections) — `server/schemas/calendar/calendar.py`
- **HolidayEntry** (31 connections) — `server/schemas/calendar/calendar.py`
- **TestHolidayService** (27 connections) — `server/tests/unit/services/test_holiday_service.py`
- **test_calendar_schemas.py** (23 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **ScheduleCollection** (12 connections) — `server/schemas/calendar/calendar.py`
- **ChronicleLike** (12 connections) — `server/time/time_service.py`
- **calendar/__init__.py** (11 connections) — `server/schemas/calendar/__init__.py`
- **calendar/calendar.py** (10 connections) — `server/schemas/calendar/calendar.py`
- **test_holiday_service.py** (10 connections) — `server/tests/unit/services/test_holiday_service.py`
- **extract_observance_ids()** (8 connections) — `server/schemas/calendar/calendar.py`
- **load_schedule_directory()** (8 connections) — `server/schemas/calendar/calendar.py`
- **_holiday_entry_from_row()** (8 connections) — `server/services/holiday_service.py`
- **.get_upcoming_holidays()** (8 connections) — `server/services/holiday_service.py`
- **.__init__()** (8 connections) — `server/services/holiday_service.py`
- **._async_load_from_database()** (7 connections) — `server/services/holiday_service.py`
- **.refresh_active()** (7 connections) — `server/services/holiday_service.py`
- **.__init__()** (7 connections) — `server/time/time_event_consumer.py`
- **slugify_observance()** (6 connections) — `server/schemas/calendar/calendar.py`
- **_ensure_utc()** (6 connections) — `server/services/holiday_service.py`
- **.test_init_loads_from_database()** (6 connections) — `server/tests/unit/services/test_holiday_service.py`
- **field_validator** (6 connections)
- **datetime** (6 connections)
- **.load_file()** (5 connections) — `server/schemas/calendar/calendar.py`
- **.load_file()** (5 connections) — `server/schemas/calendar/calendar.py`
- *... and 142 more nodes in this community*

## Relationships

- [get_npc_instance_service](get_npc_instance_service.md) (31 shared connections)
- [validate_calendar.py](validate_calendar.py.md) (12 shared connections)
- [PlayerService](PlayerService.md) (4 shared connections)
- [test_game.py](test_game.py.md) (3 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (2 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (2 shared connections)
- [MythosChronicle](MythosChronicle.md) (2 shared connections)
- [BaseCommand](BaseCommand.md) (2 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)
- [.initialize](initialize.md) (1 shared connections)
- [server/services/__init__.py](server-services-__init__.py.md) (1 shared connections)

## Source Files

- `server/schemas/calendar/__init__.py`
- `server/schemas/calendar/calendar.py`
- `server/services/holiday_service.py`
- `server/tests/unit/schemas/test_calendar_schemas.py`
- `server/tests/unit/services/test_holiday_service.py`
- `server/time/time_event_consumer.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 334 (98%)
- INFERRED: 6 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*