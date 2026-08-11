# WebSocket Code Review

> 38 nodes

## Key Concepts

- **ScheduleEntry** (28 connections) — `server/schemas/calendar/calendar.py`
- **TestScheduleService** (14 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_async_load_from_database_passes_search_path_for_mythos_e2e()** (5 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_init_loads_from_database()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_get_active_entries_with_matches()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_get_active_entries_boundary_conditions()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_get_active_entries_wrong_day()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_entries_property()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_normalize_weekday_names_latin_to_standard()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_entry_count_property()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.apply_schedule_state()** (3 connections) — `server/npc/lifecycle_manager.py`
- **.validate_duration()** (3 connections) — `server/schemas/calendar/calendar.py`
- **.entries()** (3 connections) — `server/services/schedule_service.py`
- **.test_init_with_collections()** (3 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_init_without_persistence_raises()** (3 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_get_active_entries_no_matches()** (3 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.validate_days()** (2 connections) — `server/schemas/calendar/calendar.py`
- **.validate_slug_list()** (2 connections) — `server/schemas/calendar/calendar.py`
- **Record the schedule categories currently active for NPC routines.** (1 connections) — `server/npc/lifecycle_manager.py`
- **Any** (1 connections)
- **Single schedule block describing routine availability (`data/<env>/calendar/sche** (1 connections) — `server/schemas/calendar/calendar.py`
- **Validate schedule entry days are standard English weekday names (Sunday, Monday,** (1 connections) — `server/schemas/calendar/calendar.py`
- **Validate slug-formatted list entries.          Args:             value: Sequence** (1 connections) — `server/schemas/calendar/calendar.py`
- **Ensure the schedule window moves time forward like the Chronology Tablets prescr** (1 connections) — `server/schemas/calendar/calendar.py`
- **Get all schedule entries.          Returns:             list[ScheduleEntry]: Lis** (1 connections) — `server/services/schedule_service.py`
- *... and 13 more nodes in this community*

## Relationships

- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (21 shared connections)
- [Async Room Loading Tests](Async_Room_Loading_Tests.md) (4 shared connections)
- [Player Command Developer Guide](Player_Command_Developer_Guide.md) (3 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (2 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (1 shared connections)

## Source Files

- `server/npc/lifecycle_manager.py`
- `server/schemas/calendar/calendar.py`
- `server/services/schedule_service.py`
- `server/tests/unit/services/test_schedule_service.py`

## Audit Trail

- EXTRACTED: 114 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*