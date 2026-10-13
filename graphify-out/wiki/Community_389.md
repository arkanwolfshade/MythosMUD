# Community 389

> 45 nodes

## Key Concepts

- **PassiveMobNPC** (36 connections) — `server/npc/passive_mob_npc.py`
- **test_passive_mob_npc.py** (19 connections) — `server/tests/unit/npc/test_passive_mob_npc.py`
- **.wander()** (7 connections) — `server/npc/passive_mob_npc.py`
- **.schedule_idle_movement()** (6 connections) — `server/npc/passive_mob_npc.py`
- **.__init__()** (5 connections) — `server/npc/passive_mob_npc.py`
- **._queue_wander_action()** (5 connections) — `server/npc/passive_mob_npc.py`
- **._create_wander_action()** (4 connections) — `server/npc/passive_mob_npc.py`
- **._handle_respond_to_greeting()** (3 connections) — `server/npc/passive_mob_npc.py`
- **._handle_wander()** (3 connections) — `server/npc/passive_mob_npc.py`
- **.respond_to_player()** (3 connections) — `server/npc/passive_mob_npc.py`
- **._setup_passive_mob_behavior_rules()** (3 connections) — `server/npc/passive_mob_npc.py`
- **._should_schedule_movement()** (3 connections) — `server/npc/passive_mob_npc.py`
- **passive_npc()** (3 connections) — `server/tests/unit/npc/test_passive_mob_npc.py`
- **.get_behavior_rules()** (2 connections) — `server/npc/passive_mob_npc.py`
- **._handle_flee()** (2 connections) — `server/npc/passive_mob_npc.py`
- **test_create_wander_action()** (2 connections) — `server/tests/unit/npc/test_passive_mob_npc.py`
- **test_get_behavior_rules_returns_list()** (2 connections) — `server/tests/unit/npc/test_passive_mob_npc.py`
- **test_handle_flee()** (2 connections) — `server/tests/unit/npc/test_passive_mob_npc.py`
- **test_handle_respond_to_greeting()** (2 connections) — `server/tests/unit/npc/test_passive_mob_npc.py`
- **test_queue_wander_action_no_service()** (2 connections) — `server/tests/unit/npc/test_passive_mob_npc.py`
- **test_respond_to_player_high_chance()** (2 connections) — `server/tests/unit/npc/test_passive_mob_npc.py`
- **test_respond_to_player_low_chance()** (2 connections) — `server/tests/unit/npc/test_passive_mob_npc.py`
- **test_schedule_idle_movement_fallback_wander()** (2 connections) — `server/tests/unit/npc/test_passive_mob_npc.py`
- **test_schedule_idle_movement_queues_action()** (2 connections) — `server/tests/unit/npc/test_passive_mob_npc.py`
- **test_should_schedule_movement_disabled()** (2 connections) — `server/tests/unit/npc/test_passive_mob_npc.py`
- *... and 20 more nodes in this community*

## Relationships

- [NPC Behavior Engine](NPC_Behavior_Engine.md) (7 shared connections)
- [Community 160](Community_160.md) (2 shared connections)
- [Community 817](Community_817.md) (2 shared connections)
- [Distributed Event Bus (NATS)](Distributed_Event_Bus_NATS.md) (1 shared connections)
- [Community 523](Community_523.md) (1 shared connections)
- [Community 118](Community_118.md) (1 shared connections)
- [Community 187](Community_187.md) (1 shared connections)

## Source Files

- `server/npc/passive_mob_npc.py`
- `server/tests/unit/npc/test_passive_mob_npc.py`

## Audit Trail

- EXTRACTED: 63 (77%)
- INFERRED: 19 (23%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*