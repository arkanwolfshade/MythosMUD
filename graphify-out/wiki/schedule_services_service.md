# schedule services service

> 47 nodes

## Key Concepts

- **ScheduleEntry** (28 connections) — `server/schemas/calendar/calendar.py`
- **TestScheduleService** (14 connections) — `server/tests/unit/services/test_schedule_service.py`
- **test_schedule_service.py** (8 connections) — `server/tests/unit/services/test_schedule_service.py`
- **normalize_weekday_names()** (5 connections) — `server/services/schedule_service.py`
- **.get_active_entries()** (4 connections) — `server/services/schedule_service.py`
- **test_schedule_entry_validation_days()** (4 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
- **test_schedule_collection()** (4 connections) — `server/tests/unit/schemas/test_calendar_schemas.py`
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

- [time service rationale](time_service_rationale.md) (14 shared connections)
- [NATS Messaging](NATS_Messaging.md) (6 shared connections)
- [commands party examples](commands_party_examples.md) (5 shared connections)
- [schedule service services](schedule_service_services.md) (4 shared connections)
- [schemas calendar rationale](schemas_calendar_rationale.md) (4 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (1 shared connections)
- [Player Stats](Player_Stats.md) (1 shared connections)
- [command inventory factories](command_inventory_factories.md) (1 shared connections)

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