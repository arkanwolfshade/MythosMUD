# parse jsonb column()

> 42 nodes

## Key Concepts

- **ScheduleService** (28 connections) — `server/services/schedule_service.py`
- **TestScheduleService** (14 connections) — `server/tests/unit/services/test_schedule_service.py`
- **._async_load_from_database()** (7 connections) — `server/services/schedule_service.py`
- **_fetch_schedule_entries()** (6 connections) — `server/services/schedule_service.py`
- **.test_async_load_from_database_passes_search_path_for_mythos_e2e()** (5 connections) — `server/tests/unit/services/test_schedule_service.py`
- **._load_from_database()** (4 connections) — `server/services/schedule_service.py`
- **.get_active_entries()** (4 connections) — `server/services/schedule_service.py`
- **.test_init_loads_from_database()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_get_active_entries_with_matches()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_get_active_entries_boundary_conditions()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_get_active_entries_wrong_day()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_entries_property()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_normalize_weekday_names_latin_to_standard()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_entry_count_property()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **_resolve_asyncpg_database_url()** (3 connections) — `server/services/schedule_service.py`
- **.entries()** (3 connections) — `server/services/schedule_service.py`
- **.test_init_with_collections()** (3 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_init_without_persistence_raises()** (3 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_get_active_entries_no_matches()** (3 connections) — `server/tests/unit/services/test_schedule_service.py`
- **Connection** (2 connections)
- **.entry_count()** (2 connections) — `server/services/schedule_service.py`
- **Return asyncpg-compatible DATABASE_URL from the environment.** (1 connections) — `server/services/schedule_service.py`
- **Load and normalize schedule rows from PostgreSQL.** (1 connections) — `server/services/schedule_service.py`
- **Provides schedule lookups for NPCs and environmental consumers.** (1 connections) — `server/services/schedule_service.py`
- **Load schedules from PostgreSQL database.** (1 connections) — `server/services/schedule_service.py`
- *... and 17 more nodes in this community*

## Relationships

- [chat nats publisher](chat_nats_publisher.md) (11 shared connections)
- [hash password()](hash_password%28%29.md) (11 shared connections)
- [emit close container event()](emit_close_container_event%28%29.md) (3 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (3 shared connections)
- [Formatter](Formatter.md) (2 shared connections)
- [Lock](Lock.md) (1 shared connections)
- [rate overrides](rate_overrides.md) (1 shared connections)

## Source Files

- `server/services/schedule_service.py`
- `server/tests/unit/services/test_schedule_service.py`

## Audit Trail

- EXTRACTED: 126 (93%)
- INFERRED: 10 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*