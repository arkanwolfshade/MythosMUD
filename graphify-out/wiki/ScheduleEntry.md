# ScheduleEntry

> 76 nodes

## Key Concepts

- **ScheduleEntry** (29 connections) — `server/schemas/calendar/calendar.py`
- **ScheduleService** (28 connections) — `server/services/schedule_service.py`
- **TestScheduleService** (21 connections) — `server/tests/unit/services/test_schedule_service.py`
- **test_schedule_service.py** (13 connections) — `server/tests/unit/services/test_schedule_service.py`
- **_schedule_entry_from_row()** (10 connections) — `server/services/schedule_service.py`
- **._async_load_from_database()** (7 connections) — `server/services/schedule_service.py`
- **_fetch_schedule_entries()** (6 connections) — `server/services/schedule_service.py`
- **_lower_string_list_from_row()** (6 connections) — `server/services/schedule_service.py`
- **_resolve_asyncpg_database_url()** (6 connections) — `server/services/schedule_service.py`
- **_string_list_from_row()** (6 connections) — `server/services/schedule_service.py`
- **normalize_weekday_names()** (5 connections) — `server/services/schedule_service.py`
- **._load_from_database()** (5 connections) — `server/services/schedule_service.py`
- **.test_async_load_from_database_passes_search_path_for_mythos_e2e()** (5 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_init_loads_from_database()** (5 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_load_from_database_success()** (5 connections) — `server/tests/unit/services/test_schedule_service.py`
- **_DatabaseLoadResult** (4 connections) — `server/services/schedule_service.py`
- **.get_active_entries()** (4 connections) — `server/services/schedule_service.py`
- **.test_entries_property()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_entry_count_property()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_get_active_entries_boundary_conditions()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_get_active_entries_with_matches()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_get_active_entries_wrong_day()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_init_database_load_failure_raises()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_normalize_weekday_names_latin_to_standard()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_resolve_asyncpg_database_url()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- *... and 51 more nodes in this community*

## Relationships

- [schedule_service.py](schedule_service.py.md) (14 shared connections)
- [HolidayEntry](HolidayEntry.md) (8 shared connections)
- [field_validator](field_validator.md) (3 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (2 shared connections)
- [time_event_consumer.py](time_event_consumer.py.md) (2 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (1 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)
- [server/services/__init__.py](server-services-__init__.py.md) (1 shared connections)
- [HolidayService](HolidayService.md) (1 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (1 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)
- [get_asyncpg_server_settings_for_database_url](get_asyncpg_server_settings_for_database_url.md) (1 shared connections)

## Source Files

- `server/npc/lifecycle_manager.py`
- `server/schemas/calendar/calendar.py`
- `server/services/schedule_service.py`
- `server/tests/unit/services/test_schedule_service.py`

## Audit Trail

- EXTRACTED: 151 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*