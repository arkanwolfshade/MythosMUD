# WebSocket Code Review

> 47 nodes

## Key Concepts

- **ScheduleEntry** (28 connections) — `server/schemas/calendar/calendar.py`
- **TestScheduleService** (14 connections) — `server/tests/unit/services/test_schedule_service.py`
- **test_schedule_service.py** (8 connections) — `server/tests/unit/services/test_schedule_service.py`
- **normalize_weekday_names()** (5 connections) — `server/services/schedule_service.py`
- **._load_from_database()** (4 connections) — `server/services/schedule_service.py`
- **.get_active_entries()** (4 connections) — `server/services/schedule_service.py`
- **test_schedule_entry_validation_days()** (4 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
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
- **test_schedule_entry()** (3 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **.test_init_with_collections()** (3 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_init_without_persistence_raises()** (3 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_get_active_entries_no_matches()** (3 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.validate_days()** (2 connections) — `server/schemas/calendar/calendar.py`
- **.validate_slug_list()** (2 connections) — `server/schemas/calendar/calendar.py`
- **Record the schedule categories currently active for NPC routines.** (1 connections) — `server/npc/lifecycle_manager.py`
- **Any** (1 connections)
- *... and 22 more nodes in this community*

## Relationships

- [Chat Channel Logger](Chat_Channel_Logger.md) (14 shared connections)
- [Minimap Fallback Helpers](Minimap_Fallback_Helpers.md) (6 shared connections)
- [Client Event Store](Client_Event_Store.md) (5 shared connections)
- [Chat Archive Advanced](Chat_Archive_Advanced.md) (4 shared connections)
- [Error Handling Guide](Error_Handling_Guide.md) (2 shared connections)
- [Client Security Utilities](Client_Security_Utilities.md) (2 shared connections)
- [Game Terminal Panels](Game_Terminal_Panels.md) (1 shared connections)
- [Container Repository CRUD](Container_Repository_CRUD.md) (1 shared connections)
- [React Node Upgrade Summary](React_Node_Upgrade_Summary.md) (1 shared connections)

## Source Files

- `server/npc/lifecycle_manager.py`
- `server/schemas/calendar/calendar.py`
- `server/services/schedule_service.py`
- `server/tests/unit/schemas/test_calendar_schemas.py`
- `server/tests/unit/services/test_schedule_service.py`

## Audit Trail

- EXTRACTED: 141 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*