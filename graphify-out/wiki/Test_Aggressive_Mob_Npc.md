# Test Aggressive Mob Npc

> 13 nodes

## Key Concepts

- **AggressiveMobNPC** (31 connections) — `server/npc/aggressive_mob_npc.py`
- **test_enrich_behavior_context_handles_no_current_room()** (3 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **test_enrich_behavior_context_sets_false_when_no_players_in_room()** (3 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **test_enrich_behavior_context_swallows_compute_errors()** (3 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **test_hunt_target_avoids_duplicate_ids()** (3 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **.get_behavior_rules()** (2 connections) — `server/npc/aggressive_mob_npc.py`
- **NPCBase** (1 connections)
- **Aggressive mob NPC type with hunting and territorial behaviors.** (1 connections) — `server/npc/aggressive_mob_npc.py`
- **Get aggressive mob-specific behavior rules.** (1 connections) — `server/npc/aggressive_mob_npc.py`
- **_enrich_behavior_context sets False when current_room is None.** (1 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **hunt_target appends each id once; repeated calls keep a single _targets entry.** (1 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **Warnings path: failure in _compute_player_context must not raise.** (1 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **_enrich_behavior_context sets player_in_range and enemy_nearby False when room…** (1 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`

## Relationships

- [Aggressive Mob Npc](Aggressive_Mob_Npc.md) (16 shared connections)
- [Test Aggressive Mob Npc](Test_Aggressive_Mob_Npc.md) (9 shared connections)
- [NPC Behavior & Spawning](NPC_Behavior_&_Spawning.md) (1 shared connections)
- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (1 shared connections)
- [Npc Base](Npc_Base.md) (1 shared connections)

## Source Files

- `server/npc/aggressive_mob_npc.py`
- `server/tests/unit/npc/test_aggressive_mob_npc.py`

## Audit Trail

- EXTRACTED: 39 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*