# Test Schedule Service

> 97 nodes

## Key Concepts

- **ScheduleService** (28 connections) — `server/services/schedule_service.py`
- **MythosTimeEventConsumer** (25 connections) — `server/time/time_event_consumer.py`
- **time_event_consumer.py** (25 connections) — `server/time/time_event_consumer.py`
- **TestScheduleService** (21 connections) — `server/tests/unit/services/test_schedule_service.py`
- **MythosHourTickEvent** (15 connections) — `server/events/event_types.py`
- **test_schedule_service.py** (13 connections) — `server/tests/unit/services/test_schedule_service.py`
- **_schedule_entry_from_row()** (10 connections) — `server/services/schedule_service.py`
- **test_time_event_consumer.py** (9 connections) — `server/tests/unit/time/test_time_event_consumer.py`
- **._async_load_from_database()** (7 connections) — `server/services/schedule_service.py`
- **._build_broadcast_payload()** (7 connections) — `server/time/time_event_consumer.py`
- **.__init__()** (7 connections) — `server/time/time_event_consumer.py`
- **_fetch_schedule_entries()** (6 connections) — `server/services/schedule_service.py`
- **_lower_string_list_from_row()** (6 connections) — `server/services/schedule_service.py`
- **_resolve_asyncpg_database_url()** (6 connections) — `server/services/schedule_service.py`
- **_string_list_from_row()** (6 connections) — `server/services/schedule_service.py`
- **normalize_weekday_names()** (5 connections) — `server/services/schedule_service.py`
- **._load_from_database()** (5 connections) — `server/services/schedule_service.py`
- **.test_async_load_from_database_passes_search_path_for_mythos_e2e()** (5 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_init_loads_from_database()** (5 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_load_from_database_success()** (5 connections) — `server/tests/unit/services/test_schedule_service.py`
- **._handle_tick()** (5 connections) — `server/time/time_event_consumer.py`
- **_DatabaseLoadResult** (4 connections) — `server/services/schedule_service.py`
- **.get_active_entries()** (4 connections) — `server/services/schedule_service.py`
- **.test_entries_property()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_entry_count_property()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- *... and 72 more nodes in this community*

## Relationships

- [Holiday Calendar Validation](Holiday_Calendar_Validation.md) (22 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (15 shared connections)
- [Application Container Bundles](Application_Container_Bundles.md) (6 shared connections)
- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (5 shared connections)
- [Time Service](Time_Service.md) (4 shared connections)
- [Test Event Bus](Test_Event_Bus.md) (4 shared connections)
- [Test Lifespan Startup](Test_Lifespan_Startup.md) (3 shared connections)
- [Room Service](Room_Service.md) (3 shared connections)
- [NPC Behavior & Spawning](NPC_Behavior_&_Spawning.md) (3 shared connections)
- [Error Handling & Exceptions](Error_Handling_&_Exceptions.md) (3 shared connections)
- [Connection Manager Api](Connection_Manager_Api.md) (3 shared connections)
- [Dependency Injection (FastAPI)](Dependency_Injection_FastAPI.md) (2 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/services/schedule_service.py`
- `server/tests/unit/services/test_schedule_service.py`
- `server/tests/unit/time/test_time_event_consumer.py`
- `server/time/time_event_consumer.py`

## Audit Trail

- EXTRACTED: 208 (93%)
- INFERRED: 16 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*