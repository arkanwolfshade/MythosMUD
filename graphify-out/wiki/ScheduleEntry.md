# ScheduleEntry

> 58 nodes

## Key Concepts

- **ScheduleEntry** (29 connections) — `server/schemas/calendar/calendar.py`
- **TestScheduleService** (21 connections) — `server/tests/unit/services/test_schedule_service.py`
- **._load_from_database()** (5 connections) — `server/services/schedule_service.py`
- **.test_async_load_from_database_passes_search_path_for_mythos_e2e()** (5 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_init_loads_from_database()** (5 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_load_from_database_success()** (5 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.get_active_entries()** (4 connections) — `server/services/schedule_service.py`
- **test_schedule_collection()** (4 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **.test_entries_property()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_entry_count_property()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_get_active_entries_boundary_conditions()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_get_active_entries_with_matches()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_get_active_entries_wrong_day()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_init_database_load_failure_raises()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_normalize_weekday_names_latin_to_standard()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_resolve_asyncpg_database_url()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_resolve_asyncpg_database_url_missing()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.apply_schedule_state()** (3 connections) — `server/npc/lifecycle_manager.py`
- **.entries()** (3 connections) — `server/services/schedule_service.py`
- **test_schedule_entry()** (3 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_schedule_entry_validation_days()** (3 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **.test_get_active_entries_no_matches()** (3 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_init_with_collections()** (3 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_init_without_persistence_raises()** (3 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_lower_string_list_from_row()** (3 connections) — `server/tests/unit/services/test_schedule_service.py`
- *... and 33 more nodes in this community*

## Relationships

- [bundles/game.py](bundles-game.py.md) (14 shared connections)
- [HolidayService](HolidayService.md) (14 shared connections)
- [HolidayCollection](HolidayCollection.md) (8 shared connections)
- [field_validator](field_validator.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (1 shared connections)

## Source Files

- `server/npc/lifecycle_manager.py`
- `server/schemas/calendar/calendar.py`
- `server/services/schedule_service.py`
- `server/tests/unit/schemas/test_calendar_schemas.py`
- `server/tests/unit/services/test_schedule_service.py`

## Audit Trail

- EXTRACTED: 110 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*