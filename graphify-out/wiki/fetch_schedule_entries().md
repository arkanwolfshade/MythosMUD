# fetch schedule entries()

> 41 nodes

## Key Concepts

- **TestScheduleService** (14 connections) — `server/tests/unit/services/test_schedule_service.py`
- **_schedule_entry_from_row()** (8 connections) — `server/services/schedule_service.py`
- **._async_load_from_database()** (7 connections) — `server/services/schedule_service.py`
- **_fetch_schedule_entries()** (6 connections) — `server/services/schedule_service.py`
- **normalize_weekday_names()** (5 connections) — `server/services/schedule_service.py`
- **.test_async_load_from_database_passes_search_path_for_mythos_e2e()** (5 connections) — `server/tests/unit/services/test_schedule_service.py`
- **_string_list_from_row()** (4 connections) — `server/services/schedule_service.py`
- **_lower_string_list_from_row()** (4 connections) — `server/services/schedule_service.py`
- **.test_init_loads_from_database()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_get_active_entries_with_matches()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_get_active_entries_boundary_conditions()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_get_active_entries_wrong_day()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_entries_property()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_normalize_weekday_names_latin_to_standard()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_entry_count_property()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **_resolve_asyncpg_database_url()** (3 connections) — `server/services/schedule_service.py`
- **.test_init_with_collections()** (3 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_init_without_persistence_raises()** (3 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_get_active_entries_no_matches()** (3 connections) — `server/tests/unit/services/test_schedule_service.py`
- **Record** (2 connections)
- **Connection** (2 connections)
- **Map Latin weekday names to standard English (Sunday, Monday, ...); pass-through** (1 connections) — `server/services/schedule_service.py`
- **Normalize nullable PostgreSQL array columns to string values.** (1 connections) — `server/services/schedule_service.py`
- **Normalize nullable PostgreSQL array columns to lowercase slug strings.** (1 connections) — `server/services/schedule_service.py`
- **Return asyncpg-compatible DATABASE_URL from the environment.** (1 connections) — `server/services/schedule_service.py`
- *... and 16 more nodes in this community*

## Relationships

- [Any](Any.md) (12 shared connections)
- [Path](Path.md) (11 shared connections)
- [main()](main%28%29.md) (6 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (3 shared connections)
- [get asyncpg server settings for](get_asyncpg_server_settings_for.md) (1 shared connections)

## Source Files

- `server/services/schedule_service.py`
- `server/tests/unit/services/test_schedule_service.py`

## Audit Trail

- EXTRACTED: 112 (96%)
- INFERRED: 5 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*