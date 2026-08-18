# HolidayService

> 196 nodes

## Key Concepts

- **HolidayService** (44 connections) — `server/services/holiday_service.py`
- **HolidayCollection** (40 connections) — `server/schemas/calendar/calendar.py`
- **HolidayEntry** (31 connections) — `server/schemas/calendar/calendar.py`
- **ScheduleEntry** (29 connections) — `server/schemas/calendar/calendar.py`
- **TestHolidayService** (27 connections) — `server/tests/unit/services/test_holiday_service.py`
- **test_calendar_schemas.py** (23 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **validate_calendar.py** (18 connections) — `scripts/validate_calendar.py`
- **test_schedule_service.py** (13 connections) — `server/tests/unit/services/test_schedule_service.py`
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
- **.__init__()** (7 connections) — `server/time/time_event_consumer.py`
- **_check_holiday_coverage()** (6 connections) — `scripts/validate_calendar.py`
- **_load_and_validate_holidays()** (6 connections) — `scripts/validate_calendar.py`
- *... and 171 more nodes in this community*

## Relationships

- [GameBundle](GameBundle.md) (26 shared connections)
- [get_logger](get_logger.md) (17 shared connections)
- [_schedule_entry_from_row](_schedule_entry_from_row.md) (9 shared connections)
- [PlayerService](PlayerService.md) (5 shared connections)
- [NPCDefinition](NPCDefinition.md) (5 shared connections)
- [MythosChronicle](MythosChronicle.md) (4 shared connections)
- [test_game.py](test_game.py.md) (3 shared connections)
- [MythosTimeEventConsumer](MythosTimeEventConsumer.md) (3 shared connections)
- [BaseCommand](BaseCommand.md) (3 shared connections)
- [pytest.md](pytest.md.md) (3 shared connections)
- [command_service.py](command_service.py.md) (1 shared connections)
- [database_config_helpers.py](database_config_helpers.py.md) (1 shared connections)

## Source Files

- `scripts/validate_calendar.py`
- `server/npc/lifecycle_manager.py`
- `server/schemas/calendar/__init__.py`
- `server/schemas/calendar/calendar.py`
- `server/services/holiday_service.py`
- `server/tests/unit/schemas/test_calendar_schemas.py`
- `server/tests/unit/services/test_holiday_service.py`
- `server/tests/unit/services/test_schedule_service.py`
- `server/time/time_event_consumer.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 412 (99%)
- INFERRED: 6 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*