# websocket realtime handler

> 66 nodes

## Key Concepts

- **ScheduleService** (30 connections) — `server/services/schedule_service.py`
- **time_event_consumer.py** (25 connections) — `server/time/time_event_consumer.py`
- **MythosTimeEventConsumer** (24 connections) — `server/time/time_event_consumer.py`
- **TestScheduleService** (21 connections) — `server/tests/unit/services/test_schedule_service.py`
- **MythosHourTickEvent** (16 connections) — `server/events/event_types.py`
- **ChronicleLike** (13 connections) — `server/time/time_service.py`
- **test_time_event_consumer.py** (8 connections) — `server/tests/unit/time/test_time_event_consumer.py`
- **.__init__()** (8 connections) — `server/time/time_event_consumer.py`
- **._handle_tick()** (6 connections) — `server/time/time_event_consumer.py`
- **.test_async_load_from_database_passes_search_path_for_mythos_e2e()** (5 connections) — `server/tests/unit/services/test_schedule_service.py`
- **._build_broadcast_payload()** (5 connections) — `server/time/time_event_consumer.py`
- **.get_active_entries()** (4 connections) — `server/services/schedule_service.py`
- **.test_init_loads_from_database()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_get_active_entries_with_matches()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_get_active_entries_boundary_conditions()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_get_active_entries_wrong_day()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_entries_property()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_entry_count_property()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_resolve_asyncpg_database_url()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_resolve_asyncpg_database_url_missing()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **datetime** (3 connections)
- **.entries()** (3 connections) — `server/services/schedule_service.py`
- **.test_init_with_collections()** (3 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_init_without_persistence_raises()** (3 connections) — `server/tests/unit/services/test_schedule_service.py`
- **MonkeyPatch** (3 connections)
- *... and 41 more nodes in this community*

## Relationships

- [holiday service services](holiday_service_services.md) (35 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (12 shared connections)
- [time service rationale](time_service_rationale.md) (8 shared connections)
- [models npc rationale](models_npc_rationale.md) (5 shared connections)
- [Database Config](Database_Config.md) (4 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (3 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (3 shared connections)
- [maps handle ascii](maps_handle_ascii.md) (3 shared connections)
- [combat services messaging](combat_services_messaging.md) (3 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [command service commands](command_service_commands.md) (1 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/services/schedule_service.py`
- `server/tests/unit/services/test_schedule_service.py`
- `server/tests/unit/time/test_time_event_consumer.py`
- `server/time/time_event_consumer.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 241 (88%)
- INFERRED: 32 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*