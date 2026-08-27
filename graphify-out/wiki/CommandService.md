# CommandService

> 41 nodes

## Key Concepts

- **TestScheduleService** (21 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_async_load_from_database_passes_search_path_for_mythos_e2e()** (5 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_init_loads_from_database()** (5 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_load_from_database_success()** (5 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_entries_property()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_entry_count_property()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_get_active_entries_boundary_conditions()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_get_active_entries_with_matches()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_get_active_entries_wrong_day()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_init_database_load_failure_raises()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_normalize_weekday_names_latin_to_standard()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_resolve_asyncpg_database_url()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_resolve_asyncpg_database_url_missing()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_get_active_entries_no_matches()** (3 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_init_with_collections()** (3 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_init_without_persistence_raises()** (3 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_lower_string_list_from_row()** (3 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_schedule_entry_from_row()** (3 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_string_list_from_row()** (3 connections) — `server/tests/unit/services/test_schedule_service.py`
- **MonkeyPatch** (3 connections)
- **patch** (3 connections)
- **asyncio** (1 connections)
- **Test get_active_entries returns empty list when no matches.** (1 connections) — `server/tests/unit/services/test_schedule_service.py`
- **Test get_active_entries returns matching entries.** (1 connections) — `server/tests/unit/services/test_schedule_service.py`
- **Test get_active_entries handles boundary conditions correctly.** (1 connections) — `server/tests/unit/services/test_schedule_service.py`
- *... and 16 more nodes in this community*

## Relationships

- [NPCDefinition](NPCDefinition.md) (20 shared connections)
- [AliasStorage](AliasStorage.md) (8 shared connections)

## Source Files

- `server/tests/unit/services/test_schedule_service.py`

## Audit Trail

- EXTRACTED: 71 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*