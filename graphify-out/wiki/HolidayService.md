# HolidayService

> 143 nodes

## Key Concepts

- **HolidayService** (44 connections) — `server/services/holiday_service.py`
- **server/services/__init__.py** (42 connections) — `server/services/__init__.py`
- **HolidayCollection** (40 connections) — `server/schemas/calendar/calendar.py`
- **HolidayEntry** (31 connections) — `server/schemas/calendar/calendar.py`
- **TestHolidayService** (27 connections) — `server/tests/unit/services/test_holiday_service.py`
- **holiday_service.py** (25 connections) — `server/services/holiday_service.py`
- **get_asyncpg_server_settings_for_database_url()** (17 connections) — `server/database_config_helpers.py`
- **ChronicleLike** (12 connections) — `server/time/time_service.py`
- **test_holiday_service.py** (10 connections) — `server/tests/unit/services/test_holiday_service.py`
- **test_database_config_helpers_asyncpg_settings.py** (10 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **_holiday_entry_from_row()** (8 connections) — `server/services/holiday_service.py`
- **.get_upcoming_holidays()** (8 connections) — `server/services/holiday_service.py`
- **.__init__()** (8 connections) — `server/services/holiday_service.py`
- **._async_load_from_database()** (7 connections) — `server/services/holiday_service.py`
- **.refresh_active()** (7 connections) — `server/services/holiday_service.py`
- **.__init__()** (7 connections) — `server/time/time_event_consumer.py`
- **_ensure_utc()** (6 connections) — `server/services/holiday_service.py`
- **.test_init_loads_from_database()** (6 connections) — `server/tests/unit/services/test_holiday_service.py`
- **datetime** (6 connections)
- **passive_lucidity_flux_service.py** (6 connections) — `server/services/passive_lucidity_flux_service.py`
- **.get_active_holidays()** (5 connections) — `server/services/holiday_service.py`
- **.get_serialized_active_holidays()** (5 connections) — `server/services/holiday_service.py`
- **_string_list_from_row()** (5 connections) — `server/services/holiday_service.py`
- **.test_async_load_from_database()** (5 connections) — `server/tests/unit/services/test_holiday_service.py`
- **.get_serialized_upcoming_holidays()** (4 connections) — `server/services/holiday_service.py`
- *... and 118 more nodes in this community*

## Relationships

- [time.py](time.py.md) (33 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (12 shared connections)
- [time_event_consumer.py](time_event_consumer.py.md) (6 shared connections)
- [MythosTickScheduler](MythosTickScheduler.md) (5 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [EventBus](EventBus.md) (5 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (4 shared connections)
- [test_game.py](test_game.py.md) (3 shared connections)
- [field_validator](field_validator.md) (3 shared connections)
- [test_wearable_container_service.py](test_wearable_container_service.py.md) (3 shared connections)
- [command_service.py](command_service.py.md) (3 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (2 shared connections)

## Source Files

- `server/database_config_helpers.py`
- `server/schemas/calendar/calendar.py`
- `server/services/__init__.py`
- `server/services/holiday_service.py`
- `server/services/passive_lucidity_flux_service.py`
- `server/tests/unit/schemas/test_calendar_schemas.py`
- `server/tests/unit/services/test_holiday_service.py`
- `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- `server/time/time_event_consumer.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 345 (98%)
- INFERRED: 6 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*