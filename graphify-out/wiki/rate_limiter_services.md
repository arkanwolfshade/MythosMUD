# rate limiter services

> 139 nodes

## Key Concepts

- **MythosTickScheduler** (29 connections) — `server/time/tick_scheduler.py`
- **MythosChronicle** (29 connections) — `server/time/time_service.py`
- **MythosTimeEventConsumer** (24 connections) — `server/time/time_event_consumer.py`
- **test_time_bundle.py** (20 connections) — `server/tests/unit/container/test_time_bundle.py`
- **test_tick_scheduler.py** (17 connections) — `server/tests/unit/time/test_tick_scheduler.py`
- **MythosHourTickEvent** (16 connections) — `server/events/event_types.py`
- **tick_scheduler.py** (15 connections) — `server/time/tick_scheduler.py`
- **datetime** (15 connections)
- **TimeBundle** (14 connections) — `server/container/bundles/time.py`
- **_ensure_utc()** (13 connections) — `server/time/time_service.py`
- **.get_calendar_components()** (10 connections) — `server/time/time_service.py`
- **ChronicleState** (9 connections) — `server/time/time_service.py`
- **.get_current_mythos_datetime()** (9 connections) — `server/time/time_service.py`
- **test_time_event_consumer.py** (8 connections) — `server/tests/unit/time/test_time_event_consumer.py`
- **__init__.py** (8 connections) — `server/time/__init__.py`
- **.get_daypart()** (8 connections) — `server/time/time_service.py`
- **._load_state()** (8 connections) — `server/time/time_service.py`
- **._persist_state()** (8 connections) — `server/time/time_service.py`
- **.__init__()** (7 connections) — `server/time/tick_scheduler.py`
- **.to_mythos_datetime()** (7 connections) — `server/time/time_service.py`
- **.is_witching_hour()** (7 connections) — `server/time/time_service.py`
- **.is_daytime()** (7 connections) — `server/time/time_service.py`
- **._handle_tick()** (6 connections) — `server/time/time_event_consumer.py`
- **._migrate_old_state_file()** (6 connections) — `server/time/time_service.py`
- **.initialize()** (5 connections) — `server/container/bundles/time.py`
- *... and 114 more nodes in this community*

## Relationships

- [combat models rationale](combat_models_rationale.md) (28 shared connections)
- [nats services service](nats_services_service.md) (9 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (6 shared connections)
- [inventory mutation guard](inventory_mutation_guard.md) (5 shared connections)
- [Error Conversion](Error_Conversion.md) (5 shared connections)
- [follow service game](follow_service_game.md) (4 shared connections)
- [endpoints auth rationale](endpoints_auth_rationale.md) (3 shared connections)
- [aggro threat services](aggro_threat_services.md) (2 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (2 shared connections)
- [exceptions rationale error](exceptions_rationale_error.md) (2 shared connections)
- [command service commands](command_service_commands.md) (1 shared connections)
- [effect player repository](effect_player_repository.md) (1 shared connections)

## Source Files

- `server/container/bundles/time.py`
- `server/events/event_types.py`
- `server/tests/unit/container/test_container_bundles.py`
- `server/tests/unit/container/test_time_bundle.py`
- `server/tests/unit/time/test_tick_scheduler.py`
- `server/tests/unit/time/test_time_event_consumer.py`
- `server/time/__init__.py`
- `server/time/tick_scheduler.py`
- `server/time/time_event_consumer.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 502 (95%)
- INFERRED: 26 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*