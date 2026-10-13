# Community 247

> 64 nodes

## Key Concepts

- **ScheduleService** (28 connections) — `server/services/schedule_service.py`
- **time_event_consumer.py** (25 connections) — `server/time/time_event_consumer.py`
- **MythosTimeEventConsumer** (22 connections) — `server/time/time_event_consumer.py`
- **TestScheduleService** (21 connections) — `server/tests/unit/services/test_schedule_service.py`
- **MythosHourTickEvent** (15 connections) — `server/events/event_types.py`
- **test_time_event_consumer.py** (8 connections) — `server/tests/unit/time/test_time_event_consumer.py`
- **._build_broadcast_payload()** (7 connections) — `server/time/time_event_consumer.py`
- **._load_from_database()** (5 connections) — `server/services/schedule_service.py`
- **.test_init_loads_from_database()** (5 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_load_from_database_success()** (5 connections) — `server/tests/unit/services/test_schedule_service.py`
- **._handle_tick()** (5 connections) — `server/time/time_event_consumer.py`
- **.get_active_entries()** (4 connections) — `server/services/schedule_service.py`
- **.test_entries_property()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_entry_count_property()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_get_active_entries_boundary_conditions()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_get_active_entries_with_matches()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_get_active_entries_wrong_day()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_init_database_load_failure_raises()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **.test_normalize_weekday_names_latin_to_standard()** (4 connections) — `server/tests/unit/services/test_schedule_service.py`
- **test_handle_tick_updates_room_and_broadcasts()** (4 connections) — `server/tests/unit/time/test_time_event_consumer.py`
- **._serialize_holiday()** (4 connections) — `server/time/time_event_consumer.py`
- **._serialize_schedule()** (4 connections) — `server/time/time_event_consumer.py`
- **Any** (4 connections)
- **.entries()** (3 connections) — `server/services/schedule_service.py`
- **.test_get_active_entries_no_matches()** (3 connections) — `server/tests/unit/services/test_schedule_service.py`
- *... and 39 more nodes in this community*

## Relationships

- [Community 264](Community_264.md) (17 shared connections)
- [Community 114](Community_114.md) (11 shared connections)
- [Community 162](Community_162.md) (6 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (5 shared connections)
- [Community 92](Community_92.md) (4 shared connections)
- [Distributed Event Bus (NATS)](Distributed_Event_Bus_NATS.md) (4 shared connections)
- [Game Event Types](Game_Event_Types.md) (3 shared connections)
- [Community 588](Community_588.md) (3 shared connections)
- [Invite & NPC DB Scripts](Invite_&_NPC_DB_Scripts.md) (3 shared connections)
- [Community 364](Community_364.md) (2 shared connections)
- [NPC Room Lifecycle](NPC_Room_Lifecycle.md) (2 shared connections)
- [Community 893](Community_893.md) (2 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/services/schedule_service.py`
- `server/tests/unit/services/test_schedule_service.py`
- `server/tests/unit/time/test_time_event_consumer.py`
- `server/time/time_event_consumer.py`

## Audit Trail

- EXTRACTED: 146 (90%)
- INFERRED: 16 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*