# HolidayService

> 192 nodes

## Key Concepts

- **HolidayService** (44 connections) — `server/services/holiday_service.py`
- **HolidayCollection** (40 connections) — `server/schemas/calendar/calendar.py`
- **HolidayEntry** (31 connections) — `server/schemas/calendar/calendar.py`
- **ScheduleEntry** (29 connections) — `server/schemas/calendar/calendar.py`
- **TestHolidayService** (27 connections) — `server/tests/unit/services/test_holiday_service.py`
- **test_calendar_schemas.py** (21 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **validate_calendar.py** (17 connections) — `scripts/validate_calendar.py`
- **ScheduleCollection** (12 connections) — `server/schemas/calendar/calendar.py`
- **ChronicleLike** (12 connections) — `server/time/time_service.py`
- **calendar/__init__.py** (11 connections) — `server/schemas/calendar/__init__.py`
- **run_validation()** (9 connections) — `scripts/validate_calendar.py`
- **calendar/calendar.py** (9 connections) — `server/schemas/calendar/calendar.py`
- **test_holiday_service.py** (9 connections) — `server/tests/unit/services/test_holiday_service.py`
- **extract_observance_ids()** (8 connections) — `server/schemas/calendar/calendar.py`
- **load_schedule_directory()** (8 connections) — `server/schemas/calendar/calendar.py`
- **_holiday_entry_from_row()** (8 connections) — `server/services/holiday_service.py`
- **.get_upcoming_holidays()** (8 connections) — `server/services/holiday_service.py`
- **.__init__()** (8 connections) — `server/services/holiday_service.py`
- **_get_calendar_paths()** (7 connections) — `scripts/validate_calendar.py`
- **._async_load_from_database()** (7 connections) — `server/services/holiday_service.py`
- **.refresh_active()** (7 connections) — `server/services/holiday_service.py`
- **.__init__()** (7 connections) — `server/time/time_event_consumer.py`
- **_check_holiday_coverage()** (6 connections) — `scripts/validate_calendar.py`
- **_load_and_validate_holidays()** (6 connections) — `scripts/validate_calendar.py`
- **_validate_schedule_files()** (6 connections) — `scripts/validate_calendar.py`
- *... and 167 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (13 shared connections)
- [NPCDefinition](NPCDefinition.md) (12 shared connections)
- [world](world.md) (11 shared connections)
- [TestScheduleService](TestScheduleService.md) (9 shared connections)
- [PlayerService](PlayerService.md) (5 shared connections)
- [test_game.py](test_game.py.md) (3 shared connections)
- [MythosTimeEventConsumer](MythosTimeEventConsumer.md) (3 shared connections)
- [MythosChronicle](MythosChronicle.md) (3 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (2 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (2 shared connections)
- [event_types.py](event_types.py.md) (1 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)

## Source Files

- `scripts/validate_calendar.py`
- `server/npc/lifecycle_manager.py`
- `server/schemas/calendar/__init__.py`
- `server/schemas/calendar/calendar.py`
- `server/services/holiday_service.py`
- `server/services/schedule_service.py`
- `server/tests/unit/schemas/test_calendar_schemas.py`
- `server/tests/unit/services/test_holiday_service.py`
- `server/time/time_event_consumer.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 394 (98%)
- INFERRED: 6 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*