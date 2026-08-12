# ScheduleEntry

> 99 nodes

## Key Concepts

- **ScheduleEntry** (28 connections) — `server/schemas/calendar/calendar.py`
- **SchemaValidator** (24 connections) — `schemas/validator.py`
- **get_asyncpg_server_settings_for_database_url()** (19 connections) — `server/database_config_helpers.py`
- **emote_service.py** (19 connections) — `server/game/emote_service.py`
- **create_validator()** (10 connections) — `schemas/validator.py`
- **test_database_config_helpers_asyncpg_settings.py** (9 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
- **_get_alias_validator()** (8 connections) — `server/alias_storage.py`
- **_schedule_entry_from_row()** (8 connections) — `server/services/schedule_service.py`
- **test_schedule_service.py** (8 connections) — `server/tests/unit/services/test_schedule_service.py`
- **._async_load_from_database()** (7 connections) — `server/services/schedule_service.py`
- **schemas/validator.py** (7 connections) — `schemas/validator.py`
- **Any** (7 connections)
- **.validate_data()** (6 connections) — `schemas/validator.py`
- **.validate_room()** (6 connections) — `schemas/validator.py`
- **_holiday_entry_from_row()** (6 connections) — `server/services/holiday_service.py`
- **._async_load_from_database()** (6 connections) — `server/services/holiday_service.py`
- **_fetch_schedule_entries()** (6 connections) — `server/services/schedule_service.py`
- **EmoteDefinition** (5 connections) — `server/game/emote_service.py`
- **_HolidayLoadResult** (5 connections) — `server/services/holiday_service.py`
- **_DatabaseLoadResult** (5 connections) — `server/services/schedule_service.py`
- **normalize_weekday_names()** (5 connections) — `server/services/schedule_service.py`
- **_EmoteLoadResult** (4 connections) — `server/game/emote_service.py`
- **.__init__()** (4 connections) — `schemas/validator.py`
- **.validate_alias_bundle()** (4 connections) — `schemas/validator.py`
- **.validate_emote_file()** (4 connections) — `schemas/validator.py`
- *... and 74 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (26 shared connections)
- [GameBundle](GameBundle.md) (14 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (6 shared connections)
- [EmoteService](EmoteService.md) (5 shared connections)
- [ScheduleCollection](ScheduleCollection.md) (5 shared connections)
- [log_and_raise](log_and_raise.md) (4 shared connections)
- [test_calendar_schemas.py](test_calendar_schemas.py.md) (3 shared connections)
- [field_validator](field_validator.md) (3 shared connections)
- [PathValidator](PathValidator.md) (2 shared connections)
- [AliasStorage](AliasStorage.md) (2 shared connections)
- [test_alias_storage.py](test_alias_storage.py.md) (2 shared connections)
- [rate_overrides.py](rate_overrides.py.md) (2 shared connections)

## Source Files

- `schemas/validator.py`
- `server/alias_storage.py`
- `server/database_config_helpers.py`
- `server/game/emote_service.py`
- `server/npc/lifecycle_manager.py`
- `server/schemas/calendar/calendar.py`
- `server/services/holiday_service.py`
- `server/services/schedule_service.py`
- `server/tests/unit/services/test_schedule_service.py`
- `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`

## Audit Trail

- EXTRACTED: 347 (97%)
- INFERRED: 12 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*