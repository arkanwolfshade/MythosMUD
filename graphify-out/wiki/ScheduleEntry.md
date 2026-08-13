# ScheduleEntry

> 64 nodes

## Key Concepts

- **ScheduleEntry** (28 connections) — `server/schemas/calendar/calendar.py`
- **TestScheduleService** (14 connections) — `server/tests/unit/services/test_schedule_service.py`
- **_schedule_entry_from_row()** (8 connections) — `server/services/schedule_service.py`
- **test_schedule_service.py** (8 connections) — `server/tests/unit/services/test_schedule_service.py`
- **._async_load_from_database()** (7 connections) — `server/services/schedule_service.py`
- **_fetch_schedule_entries()** (6 connections) — `server/services/schedule_service.py`
- **_DatabaseLoadResult** (5 connections) — `server/services/schedule_service.py`
- **normalize_weekday_names()** (5 connections) — `server/services/schedule_service.py`
- **.test_async_load_from_database_passes_search_path_for_mythos_e2e()** (5 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_init_loads_from_database()** (5 connections) — `server/tests/unit/services/test_schedule_service.py`
- **_lower_string_list_from_row()** (4 connections) — `server/services/schedule_service.py`
- **.get_active_entries()** (4 connections) — `server/services/schedule_service.py`
- **._load_from_database()** (4 connections) — `server/services/schedule_service.py`
- **_string_list_from_row()** (4 connections) — `server/services/schedule_service.py`
- **test_schedule_collection()** (4 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **.test_entries_property()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_entry_count_property()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_get_active_entries_boundary_conditions()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_get_active_entries_with_matches()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_get_active_entries_wrong_day()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_normalize_weekday_names_latin_to_standard()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.apply_schedule_state()** (3 connections) — `server/npc/lifecycle_manager.py`
- **_resolve_asyncpg_database_url()** (3 connections) — `server/services/schedule_service.py`
- **.entries()** (3 connections) — `server/services/schedule_service.py`
- **test_schedule_entry()** (3 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- *... and 39 more nodes in this community*

## Relationships

- [PlayerService](PlayerService.md) (15 shared connections)
- [get_logger](get_logger.md) (11 shared connections)
- [test_calendar_schemas.py](test_calendar_schemas.py.md) (9 shared connections)
- [field_validator](field_validator.md) (3 shared connections)
- [EventBus](EventBus.md) (2 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (1 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)
- [validate_calendar.py](validate_calendar.py.md) (1 shared connections)

## Source Files

- `server/npc/lifecycle_manager.py`
- `server/schemas/calendar/calendar.py`
- `server/services/schedule_service.py`
- `server/tests/unit/schemas/test_calendar_schemas.py`
- `server/tests/unit/services/test_schedule_service.py`

## Audit Trail

- EXTRACTED: 117 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*