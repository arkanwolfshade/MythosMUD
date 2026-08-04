# time service rationale

> 92 nodes

## Key Concepts

- **MythosTickScheduler** (29 connections) — `server/time/tick_scheduler.py`
- **MythosChronicle** (29 connections) — `server/time/time_service.py`
- **get_mythos_chronicle()** (26 connections) — `server/time/time_service.py`
- **test_tick_scheduler.py** (17 connections) — `server/tests/unit/time/test_tick_scheduler.py`
- **tick_scheduler.py** (15 connections) — `server/time/tick_scheduler.py`
- **datetime** (15 connections)
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
- **._run()** (5 connections) — `server/time/tick_scheduler.py`
- **._emit_pending_ticks()** (5 connections) — `server/time/tick_scheduler.py`
- **._publish_tick()** (5 connections) — `server/time/tick_scheduler.py`
- **._truncate_to_hour()** (5 connections) — `server/time/tick_scheduler.py`
- **.__init__()** (5 connections) — `server/time/time_service.py`
- **.to_real_datetime()** (5 connections) — `server/time/time_service.py`
- *... and 67 more nodes in this community*

## Relationships

- [NPC Combat](NPC_Combat.md) (12 shared connections)
- [cleanup combat handler](cleanup_combat_handler.md) (9 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (8 shared connections)
- [follow service game](follow_service_game.md) (4 shared connections)
- [Error Conversion](Error_Conversion.md) (4 shared connections)
- [command service commands](command_service_commands.md) (3 shared connections)
- [map RoomMapViewer mapUtils](map_RoomMapViewer_mapUtils.md) (3 shared connections)
- [Spell Validation](Spell_Validation.md) (2 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (2 shared connections)
- [command base models](command_base_models.md) (2 shared connections)
- [nats services service](nats_services_service.md) (2 shared connections)
- [commands admin mute](commands_admin_mute.md) (2 shared connections)

## Source Files

- `server/tests/unit/time/test_tick_scheduler.py`
- `server/time/__init__.py`
- `server/time/tick_scheduler.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 372 (98%)
- INFERRED: 9 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*