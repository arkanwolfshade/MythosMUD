# HolidayService

> 159 nodes

## Key Concepts

- **HolidayService** (41 connections) — `server/services/holiday_service.py`
- **HolidayCollection** (37 connections) — `server/schemas/calendar/calendar.py`
- **HolidayEntry** (31 connections) — `server/schemas/calendar/calendar.py`
- **ScheduleEntry** (28 connections) — `server/schemas/calendar/calendar.py`
- **holiday_service.py** (24 connections) — `server/services/holiday_service.py`
- **test_calendar_schemas.py** (21 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **TestHolidayService** (20 connections) — `server/tests/unit/services/test_holiday_service.py`
- **get_asyncpg_server_settings_for_database_url()** (19 connections) — `server/database_config_helpers.py`
- **ScheduleCollection** (12 connections) — `server/schemas/calendar/calendar.py`
- **calendar/__init__.py** (10 connections) — `server/schemas/calendar/__init__.py`
- **calendar/calendar.py** (9 connections) — `server/schemas/calendar/calendar.py`
- **extract_observance_ids()** (8 connections) — `server/schemas/calendar/calendar.py`
- **load_schedule_directory()** (8 connections) — `server/schemas/calendar/calendar.py`
- **.get_upcoming_holidays()** (8 connections) — `server/services/holiday_service.py`
- **.__init__()** (8 connections) — `server/services/holiday_service.py`
- **.refresh_active()** (7 connections) — `server/services/holiday_service.py`
- **_load_and_validate_holidays()** (6 connections) — `scripts/validate_calendar.py`
- **_validate_schedule_files()** (6 connections) — `scripts/validate_calendar.py`
- **slugify_observance()** (6 connections) — `server/schemas/calendar/calendar.py`
- **_holiday_entry_from_row()** (6 connections) — `server/services/holiday_service.py`
- **._async_load_from_database()** (6 connections) — `server/services/holiday_service.py`
- **.test_init_loads_from_database()** (6 connections) — `server/tests/unit/services/test_holiday_service.py`
- **field_validator** (6 connections)
- **datetime** (6 connections)
- **test_holiday_service.py** (6 connections) — `server/tests/unit/services/test_holiday_service.py`
- *... and 134 more nodes in this community*

## Relationships

- [bundles/game.py](bundles-game.py.md) (28 shared connections)
- [ScheduleService](ScheduleService.md) (18 shared connections)
- [test_database_config_helpers_asyncpg_settings.py](test_database_config_helpers_asyncpg_settings.py.md) (6 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (5 shared connections)
- [ValidationError](ValidationError.md) (5 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (4 shared connections)
- [test_game.py](test_game.py.md) (3 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (2 shared connections)
- [GameBundle](GameBundle.md) (2 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (2 shared connections)
- [rate_overrides.py](rate_overrides.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)

## Source Files

- `scripts/validate_calendar.py`
- `server/database_config_helpers.py`
- `server/npc/lifecycle_manager.py`
- `server/schemas/calendar/__init__.py`
- `server/schemas/calendar/calendar.py`
- `server/services/holiday_service.py`
- `server/tests/unit/schemas/test_calendar_schemas.py`
- `server/tests/unit/services/test_holiday_service.py`

## Audit Trail

- EXTRACTED: 614 (99%)
- INFERRED: 8 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*