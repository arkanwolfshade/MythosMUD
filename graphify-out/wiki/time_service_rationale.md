# time service rationale

> 125 nodes

## Key Concepts

- **MythosTickScheduler** (29 connections) — `server/time/tick_scheduler.py`
- **MythosChronicle** (29 connections) — `server/time/time_service.py`
- **get_mythos_chronicle()** (26 connections) — `server/time/time_service.py`
- **test_time_bundle.py** (20 connections) — `server/tests/unit/container/test_time_bundle.py`
- **test_tick_scheduler.py** (17 connections) — `server/tests/unit/time/test_tick_scheduler.py`
- **tick_scheduler.py** (15 connections) — `server/time/tick_scheduler.py`
- **datetime** (15 connections)
- **TimeBundle** (14 connections) — `server/container/bundles/time.py`
- **_ensure_utc()** (13 connections) — `server/time/time_service.py`
- **.get_calendar_components()** (10 connections) — `server/time/time_service.py`
- **ChronicleState** (9 connections) — `server/time/time_service.py`
- **.get_current_mythos_datetime()** (9 connections) — `server/time/time_service.py`
- **__init__.py** (8 connections) — `server/time/__init__.py`
- **.get_daypart()** (8 connections) — `server/time/time_service.py`
- **._load_state()** (8 connections) — `server/time/time_service.py`
- **._persist_state()** (8 connections) — `server/time/time_service.py`
- **.__init__()** (7 connections) — `server/time/tick_scheduler.py`
- **.to_mythos_datetime()** (7 connections) — `server/time/time_service.py`
- **.is_witching_hour()** (7 connections) — `server/time/time_service.py`
- **.is_daytime()** (7 connections) — `server/time/time_service.py`
- **._migrate_old_state_file()** (6 connections) — `server/time/time_service.py`
- **.initialize()** (5 connections) — `server/container/bundles/time.py`
- **._run()** (5 connections) — `server/time/tick_scheduler.py`
- **._emit_pending_ticks()** (5 connections) — `server/time/tick_scheduler.py`
- **._publish_tick()** (5 connections) — `server/time/tick_scheduler.py`
- *... and 100 more nodes in this community*

## Relationships

- [models npc rationale](models_npc_rationale.md) (19 shared connections)
- [Error Conversion](Error_Conversion.md) (9 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (8 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (5 shared connections)
- [follow service game](follow_service_game.md) (4 shared connections)
- [holiday service services](holiday_service_services.md) (4 shared connections)
- [map RoomMapViewer mapUtils](map_RoomMapViewer_mapUtils.md) (3 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (3 shared connections)
- [exceptions rationale error](exceptions_rationale_error.md) (2 shared connections)
- [command base models](command_base_models.md) (2 shared connections)
- [commands admin mute](commands_admin_mute.md) (2 shared connections)
- [container helpers endpoints](container_helpers_endpoints.md) (1 shared connections)

## Source Files

- `server/container/bundles/time.py`
- `server/tests/unit/container/test_container_bundles.py`
- `server/tests/unit/container/test_time_bundle.py`
- `server/tests/unit/time/test_tick_scheduler.py`
- `server/time/__init__.py`
- `server/time/tick_scheduler.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 465 (98%)
- INFERRED: 11 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*