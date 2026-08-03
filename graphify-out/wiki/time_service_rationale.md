# time service rationale

> 101 nodes

## Key Concepts

- **ScheduleService** (28 connections) — `server/services/schedule_service.py`
- **MythosChronicle** (27 connections) — `server/time/time_service.py`
- **get_mythos_chronicle()** (24 connections) — `server/time/time_service.py`
- **MythosTimeEventConsumer** (21 connections) — `server/time/time_event_consumer.py`
- **lifespan_shutdown.py** (15 connections) — `server/app/lifespan_shutdown.py`
- **datetime** (15 connections)
- **ChronicleLike** (13 connections) — `server/time/time_service.py`
- **shutdown_services()** (12 connections) — `server/app/lifespan_shutdown.py`
- **MythosHourTickEvent** (12 connections) — `server/events/event_types.py`
- **_ensure_utc()** (11 connections) — `server/time/time_service.py`
- **.get_calendar_components()** (10 connections) — `server/time/time_service.py`
- **ChronicleState** (9 connections) — `server/time/time_service.py`
- **.get_current_mythos_datetime()** (9 connections) — `server/time/time_service.py`
- **.error()** (8 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **__init__.py** (8 connections) — `server/time/__init__.py`
- **.__init__()** (8 connections) — `server/time/time_event_consumer.py`
- **.get_daypart()** (8 connections) — `server/time/time_service.py`
- **._load_state()** (8 connections) — `server/time/time_service.py`
- **._persist_state()** (8 connections) — `server/time/time_service.py`
- **.to_mythos_datetime()** (7 connections) — `server/time/time_service.py`
- **.is_witching_hour()** (7 connections) — `server/time/time_service.py`
- **.is_daytime()** (7 connections) — `server/time/time_service.py`
- **._handle_tick()** (6 connections) — `server/time/time_event_consumer.py`
- **._migrate_old_state_file()** (6 connections) — `server/time/time_service.py`
- **FastAPI** (5 connections)
- *... and 76 more nodes in this community*

## Relationships

- [NATS Messaging](NATS_Messaging.md) (29 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (14 shared connections)
- [schedule services service](schedule_services_service.md) (14 shared connections)
- [System Metrics](System_Metrics.md) (7 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (7 shared connections)
- [config models rationale](config_models_rationale.md) (5 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (4 shared connections)
- [project paths rationale](project_paths_rationale.md) (4 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (3 shared connections)
- [npc populate databases](npc_populate_databases.md) (3 shared connections)
- [auth endpoints rationale](auth_endpoints_rationale.md) (3 shared connections)
- [schedule service services](schedule_service_services.md) (2 shared connections)

## Source Files

- `server/app/lifespan_shutdown.py`
- `server/config/models/app.py`
- `server/container/bundles/time.py`
- `server/events/event_types.py`
- `server/services/schedule_service.py`
- `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- `server/time/__init__.py`
- `server/time/time_event_consumer.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 406 (92%)
- INFERRED: 36 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*