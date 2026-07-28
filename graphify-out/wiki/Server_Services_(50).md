# Server Services (50)

> 36 nodes

## Key Concepts

- **ScheduleService** (25 connections) — `server/services/schedule_service.py`
- **TestScheduleService** (14 connections) — `server/tests/unit/services/test_schedule_service.py`
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
- **datetime** (3 connections)
- **.entries()** (3 connections) — `server/services/schedule_service.py`
- **.test_init_with_collections()** (3 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_init_without_persistence_raises()** (3 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_get_active_entries_no_matches()** (3 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.entry_count()** (2 connections) — `server/services/schedule_service.py`
- **Provides schedule lookups for NPCs and environmental consumers.** (1 connections) — `server/services/schedule_service.py`
- **Load schedules from PostgreSQL database.** (1 connections) — `server/services/schedule_service.py`
- **Return schedule entries active at the provided Mythos date/time.** (1 connections) — `server/services/schedule_service.py`
- **Get all schedule entries.          Returns:             list[ScheduleEntry]: Lis** (1 connections) — `server/services/schedule_service.py`
- **Get the number of schedule entries.          Returns:             int: The count** (1 connections) — `server/services/schedule_service.py`
- **MonkeyPatch** (1 connections)
- **Test suite for ScheduleService class.** (1 connections) — `server/tests/unit/services/test_schedule_service.py`
- *... and 11 more nodes in this community*

## Relationships

- [Server Schemas (2)](Server_Schemas_%282%29.md) (12 shared connections)
- [Server Utils (14)](Server_Utils_%2814%29.md) (7 shared connections)
- [Server Npc (2)](Server_Npc_%282%29.md) (3 shared connections)
- [Server Infrastructure (4)](Server_Infrastructure_%284%29.md) (2 shared connections)
- [Server Api](Server_Api.md) (1 shared connections)

## Source Files

- `server/services/schedule_service.py`
- `server/tests/unit/services/test_schedule_service.py`

## Audit Trail

- EXTRACTED: 106 (92%)
- INFERRED: 9 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*