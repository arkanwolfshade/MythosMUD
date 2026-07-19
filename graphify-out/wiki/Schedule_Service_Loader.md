# Schedule Service Loader

> 43 nodes · cohesion 0.05

## Key Concepts

- **TestScheduleService** (14 connections) — `server/tests/unit/services/test_schedule_service.py`
- **_schedule_entry_from_row()** (9 connections) — `server/services/schedule_service.py`
- **ScheduleEntry** (6 connections) — `server/services/schedule_service.py`
- **_fetch_schedule_entries()** (6 connections) — `server/services/schedule_service.py`
- **normalize_weekday_names()** (5 connections) — `server/services/schedule_service.py`
- **_lower_string_list_from_row()** (4 connections) — `server/services/schedule_service.py`
- **.get_active_entries()** (4 connections) — `server/services/schedule_service.py`
- **_string_list_from_row()** (4 connections) — `server/services/schedule_service.py`
- **.test_entries_property()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_entry_count_property()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_get_active_entries_boundary_conditions()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_get_active_entries_with_matches()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_get_active_entries_wrong_day()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_init_loads_from_database()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_normalize_weekday_names_latin_to_standard()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **datetime** (3 connections) — `server/services/schedule_service.py`
- **.entries()** (3 connections) — `server/services/schedule_service.py`
- **.test_async_load_from_database_passes_search_path_for_mythos_e2e()** (3 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_get_active_entries_no_matches()** (3 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_init_with_collections()** (3 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_init_without_persistence_raises()** (3 connections) — `server/tests/unit/services/test_schedule_service.py`
- **Connection** (2 connections) — `server/services/schedule_service.py`
- **Record** (2 connections) — `server/services/schedule_service.py`
- **MonkeyPatch** (2 connections) — `server/tests/unit/services/test_schedule_service.py`
- **Load and normalize schedule rows from PostgreSQL.** (1 connections) — `server/services/schedule_service.py`
- *... and 18 more nodes in this community*

## Relationships

- [[Game Service Bundle]] (14 shared connections)
- [[Calendar Holiday Schemas]] (10 shared connections)
- [[NPC Admin API]] (6 shared connections)
- [[Async Persistence Layer]] (4 shared connections)
- [[Lucidity Rate Overrides]] (1 shared connections)

## Source Files

- `server/services/schedule_service.py`
- `server/tests/unit/services/test_schedule_service.py`

## Audit Trail

- EXTRACTED: 117 (95%)
- INFERRED: 6 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
