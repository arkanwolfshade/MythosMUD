# PassiveMobNPC

> 71 nodes

## Key Concepts

- **PassiveMobNPC** (57 connections) — `server/npc/passive_mob_npc.py`
- **test_npc_base.py** (25 connections) — `server/tests/unit/npc/test_npc_base.py`
- **test_passive_mob_npc.py** (20 connections) — `server/tests/unit/npc/test_passive_mob_npc.py`
- **.schedule_idle_movement()** (6 connections) — `server/npc/passive_mob_npc.py`
- **.wander()** (6 connections) — `server/npc/passive_mob_npc.py`
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
- **test_npc_base_handle_die_and_idle()** (2 connections) — `server/tests/unit/npc/test_npc_base.py`
- *... and 46 more nodes in this community*

## Relationships

- [time.py](time.py.md) (6 shared connections)
- [NPCBase](NPCBase.md) (3 shared connections)
- [IdleMovementHandler](IdleMovementHandler.md) (2 shared connections)
- [NPCActionMessage](NPCActionMessage.md) (2 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [NPCDefinition](NPCDefinition.md) (1 shared connections)

## Source Files

- `server/npc/passive_mob_npc.py`
- `server/tests/unit/npc/test_npc_base.py`
- `server/tests/unit/npc/test_passive_mob_npc.py`

## Audit Trail

- EXTRACTED: 110 (85%)
- INFERRED: 20 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*