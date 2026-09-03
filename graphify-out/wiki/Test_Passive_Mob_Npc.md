# Test Passive Mob Npc

> 21 nodes

## Key Concepts

- **test_passive_mob_npc.py** (20 connections) — `server/tests/unit/npc/test_passive_mob_npc.py`
- **passive_mob_npc.py** (11 connections) — `server/npc/passive_mob_npc.py`
- **passive_npc()** (3 connections) — `server/tests/unit/npc/test_passive_mob_npc.py`
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
- **test_should_schedule_movement_first_time()** (2 connections) — `server/tests/unit/npc/test_passive_mob_npc.py`
- **test_should_schedule_movement_interval_elapsed()** (2 connections) — `server/tests/unit/npc/test_passive_mob_npc.py`
- **test_should_schedule_movement_interval_not_elapsed()** (2 connections) — `server/tests/unit/npc/test_passive_mob_npc.py`
- **test_wander_no_persistence()** (2 connections) — `server/tests/unit/npc/test_passive_mob_npc.py`
- **test_wander_success()** (2 connections) — `server/tests/unit/npc/test_passive_mob_npc.py`
- **fixture** (1 connections)
- **Passive mob NPC type for MythosMUD. This module provides the PassiveMobNPC…** (1 connections) — `server/npc/passive_mob_npc.py`
- **Unit tests for PassiveMobNPC.** (1 connections) — `server/tests/unit/npc/test_passive_mob_npc.py`

## Relationships

- [Test Npc Base](Test_Npc_Base.md) (19 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (3 shared connections)
- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (3 shared connections)
- [NPC Behavior & Spawning](NPC_Behavior_&_Spawning.md) (1 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/npc/passive_mob_npc.py`
- `server/tests/unit/npc/test_passive_mob_npc.py`

## Audit Trail

- EXTRACTED: 32 (68%)
- INFERRED: 15 (32%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*