# server npc passive mob npc

> 73 nodes

## Key Concepts

- **PassiveMobNPC** (59 connections) — `server/npc/passive_mob_npc.py`
- **test_npc_base.py** (25 connections) — `server/tests/unit/npc/test_npc_base.py`
- **test_passive_mob_npc.py** (20 connections) — `server/tests/unit/npc/test_passive_mob_npc.py`
- **.schedule_idle_movement()** (6 connections) — `server/npc/passive_mob_npc.py`
- **.wander()** (6 connections) — `server/npc/passive_mob_npc.py`
- **.__init__()** (5 connections) — `server/npc/passive_mob_npc.py`
- **._queue_wander_action()** (5 connections) — `server/npc/passive_mob_npc.py`
- **._create_wander_action()** (4 connections) — `server/npc/passive_mob_npc.py`
- **._handle_respond_to_greeting()** (3 connections) — `server/npc/passive_mob_npc.py`
- **._handle_wander()** (3 connections) — `server/npc/passive_mob_npc.py`
- **.respond_to_player()** (3 connections) — `server/npc/passive_mob_npc.py`
- **._setup_passive_mob_behavior_rules()** (3 connections) — `server/npc/passive_mob_npc.py`
- **._should_schedule_movement()** (3 connections) — `server/npc/passive_mob_npc.py`
- **test_npc_base_execute_behavior()** (3 connections) — `server/tests/unit/npc/test_npc_base.py`
- **test_npc_base_get_combat_stats()** (3 connections) — `server/tests/unit/npc/test_npc_base.py`
- **test_npc_base_get_combat_stats_defaults()** (3 connections) — `server/tests/unit/npc/test_npc_base.py`
- **test_npc_base_get_combat_stats_legacy_dp()** (3 connections) — `server/tests/unit/npc/test_npc_base.py`
- **test_npc_base_is_alive_property()** (3 connections) — `server/tests/unit/npc/test_npc_base.py`
- **test_npc_base_move_to_room_blocked_when_in_combat()** (3 connections) — `server/tests/unit/npc/test_npc_base.py`
- **passive_npc()** (3 connections) — `server/tests/unit/npc/test_passive_mob_npc.py`
- **.get_behavior_rules()** (2 connections) — `server/npc/passive_mob_npc.py`
- **._handle_flee()** (2 connections) — `server/npc/passive_mob_npc.py`
- **test_npc_base_ai_placeholders()** (2 connections) — `server/tests/unit/npc/test_npc_base.py`
- **test_npc_base_from_dict()** (2 connections) — `server/tests/unit/npc/test_npc_base.py`
- **test_npc_base_get_behavior_and_ai_config()** (2 connections) — `server/tests/unit/npc/test_npc_base.py`
- *... and 48 more nodes in this community*

## Relationships

- [server npc init](server_npc_init.md) (7 shared connections)
- [server events event bus eventbus](server_events_event_bus_eventbus.md) (4 shared connections)
- [server events event types playerenteredroom](server_events_event_types_playerenteredroom.md) (2 shared connections)
- [server npc idle movement](server_npc_idle_movement.md) (2 shared connections)
- [characterinfo](characterinfo.md) (2 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (1 shared connections)
- [server container main applicationcontainer get](server_container_main_applicationcontainer_get.md) (1 shared connections)
- [draft7validator](draft7validator.md) (1 shared connections)

## Source Files

- `server/npc/passive_mob_npc.py`
- `server/tests/unit/npc/test_npc_base.py`
- `server/tests/unit/npc/test_passive_mob_npc.py`

## Audit Trail

- EXTRACTED: 93 (69%)
- INFERRED: 42 (31%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*