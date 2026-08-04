# time service rationale

> 120 nodes

## Key Concepts

- **.initialize()** (35 connections) — `server/container/bundles/game.py`
- **MythosTickScheduler** (29 connections) — `server/time/tick_scheduler.py`
- **MythosChronicle** (29 connections) — `server/time/time_service.py`
- **time_service.py** (26 connections) — `server/time/time_service.py`
- **get_mythos_chronicle()** (26 connections) — `server/time/time_service.py`
- **test_time_bundle.py** (20 connections) — `server/tests/unit/container/test_time_bundle.py`
- **test_tick_scheduler.py** (17 connections) — `server/tests/unit/time/test_tick_scheduler.py`
- **tick_scheduler.py** (15 connections) — `server/time/tick_scheduler.py`
- **datetime** (15 connections)
- **_ensure_utc()** (13 connections) — `server/time/time_service.py`
- **.get_calendar_components()** (10 connections) — `server/time/time_service.py`
- **ChronicleState** (9 connections) — `server/time/time_service.py`
- **.get_current_mythos_datetime()** (9 connections) — `server/time/time_service.py`
- **.error()** (8 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
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
- *... and 95 more nodes in this community*

## Relationships

- [websocket realtime handler](websocket_realtime_handler.md) (10 shared connections)
- [nats services service](nats_services_service.md) (8 shared connections)
- [Loot Generation](Loot_Generation.md) (7 shared connections)
- [Database Config](Database_Config.md) (6 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (6 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (5 shared connections)
- [models npc rationale](models_npc_rationale.md) (4 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (4 shared connections)
- [follow service game](follow_service_game.md) (4 shared connections)
- [command base models](command_base_models.md) (3 shared connections)
- [player death service](player_death_service.md) (3 shared connections)
- [commands admin mute](commands_admin_mute.md) (3 shared connections)

## Source Files

- `server/container/bundles/game.py`
- `server/container/bundles/time.py`
- `server/tests/unit/container/test_time_bundle.py`
- `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- `server/tests/unit/time/test_tick_scheduler.py`
- `server/time/__init__.py`
- `server/time/tick_scheduler.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 498 (97%)
- INFERRED: 18 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*