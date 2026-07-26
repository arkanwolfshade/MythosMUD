# PassiveMobNPC

> 48 nodes · cohesion 0.06

## Key Concepts

- **PassiveMobNPC** (29 connections) — `server/npc/passive_mob_npc.py`
- **NPCActionMessage** (12 connections) — `server/npc/threading.py`
- **test_npc_base.py** (8 connections) — `server/tests/unit/npc/test_npc_base.py`
- **.schedule_idle_movement()** (6 connections) — `server/npc/passive_mob_npc.py`
- **.wander()** (6 connections) — `server/npc/passive_mob_npc.py`
- **.__init__()** (5 connections) — `server/npc/passive_mob_npc.py`
- **._queue_wander_action()** (5 connections) — `server/npc/passive_mob_npc.py`
- **.from_dict()** (5 connections) — `server/npc/threading.py`
- **._create_wander_action()** (4 connections) — `server/npc/passive_mob_npc.py`
- **.to_dict()** (4 connections) — `server/npc/threading.py`
- **._handle_respond_to_greeting()** (3 connections) — `server/npc/passive_mob_npc.py`
- **._handle_wander()** (3 connections) — `server/npc/passive_mob_npc.py`
- **.respond_to_player()** (3 connections) — `server/npc/passive_mob_npc.py`
- **._setup_passive_mob_behavior_rules()** (3 connections) — `server/npc/passive_mob_npc.py`
- **._should_schedule_movement()** (3 connections) — `server/npc/passive_mob_npc.py`
- **.from_json()** (3 connections) — `server/npc/threading.py`
- **.to_json()** (3 connections) — `server/npc/threading.py`
- **test_npc_base_get_combat_stats()** (3 connections) — `server/tests/unit/npc/test_npc_base.py`
- **test_npc_base_get_combat_stats_defaults()** (3 connections) — `server/tests/unit/npc/test_npc_base.py`
- **test_npc_base_get_combat_stats_legacy_dp()** (3 connections) — `server/tests/unit/npc/test_npc_base.py`
- **test_npc_base_is_alive_property()** (3 connections) — `server/tests/unit/npc/test_npc_base.py`
- **test_npc_base_move_to_room_blocked_when_in_combat()** (3 connections) — `server/tests/unit/npc/test_npc_base.py`
- **.get_behavior_rules()** (2 connections) — `server/npc/passive_mob_npc.py`
- **._handle_flee()** (2 connections) — `server/npc/passive_mob_npc.py`
- **Check if idle movement should be scheduled based on configuration and timing.** (1 connections) — `server/npc/passive_mob_npc.py`
- *... and 23 more nodes in this community*

## Relationships

- [npc_base.py](npc_base.py.md) (9 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [IdleMovementHandler](IdleMovementHandler.md) (3 shared connections)
- [CombatService](CombatService.md) (2 shared connections)
- [NPCThreadManager](NPCThreadManager.md) (2 shared connections)
- [NPCBase](NPCBase.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)

## Source Files

- `server/npc/passive_mob_npc.py`
- `server/npc/threading.py`
- `server/tests/unit/npc/test_npc_base.py`

## Audit Trail

- EXTRACTED: 140 (95%)
- INFERRED: 8 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*