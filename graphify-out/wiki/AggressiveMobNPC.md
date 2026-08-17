# AggressiveMobNPC

> 14 nodes

## Key Concepts

- **AggressiveMobNPC** (31 connections) — `server/npc/aggressive_mob_npc.py`
- **._handle_patrol_territory()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **.patrol_territory()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **test_enrich_behavior_context_swallows_compute_errors()** (3 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **test_get_attack_damage_invalid_string_falls_back_to_one()** (3 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **test_hunt_target_avoids_duplicate_ids()** (3 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **.get_behavior_rules()** (2 connections) — `server/npc/aggressive_mob_npc.py`
- **Patrol the NPC's territory.** (1 connections) — `server/npc/aggressive_mob_npc.py`
- **Aggressive mob NPC type with hunting and territorial behaviors.** (1 connections) — `server/npc/aggressive_mob_npc.py`
- **Handle patrolling territory action.** (1 connections) — `server/npc/aggressive_mob_npc.py`
- **Get aggressive mob-specific behavior rules.** (1 connections) — `server/npc/aggressive_mob_npc.py`
- **Non-digit attack_damage string in behavior_config falls back to 1.** (1 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **hunt_target appends each id once; repeated calls keep a single _targets entry.** (1 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **Warnings path: failure in _compute_player_context must not raise.** (1 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`

## Relationships

- [test_aggressive_mob_npc.py](test_aggressive_mob_npc.py.md) (5 shared connections)
- [._attack_target_impl](_attack_target_impl.md) (5 shared connections)
- [._compute_player_context](_compute_player_context.md) (3 shared connections)
- [npc_base.py](npc_base.py.md) (2 shared connections)
- [._handle_hunt_target](_handle_hunt_target.md) (2 shared connections)
- [.flee](flee.md) (2 shared connections)
- [.__init__](__init__.md) (2 shared connections)
- [test_enrich_behavior_context_handles_no_current_room](test_enrich_behavior_context_handles_no_current_room.md) (1 shared connections)
- [test_enrich_behavior_context_sets_false_when_no_players_in_room](test_enrich_behavior_context_sets_false_when_no_players_in_room.md) (1 shared connections)
- [test_enrich_behavior_context_sets_player_in_range_when_players_in_room](test_enrich_behavior_context_sets_player_in_range_when_players_in_room.md) (1 shared connections)
- [test_get_attack_damage_from_behavior_config](test_get_attack_damage_from_behavior_config.md) (1 shared connections)
- [NPCBase](NPCBase.md) (1 shared connections)

## Source Files

- `server/npc/aggressive_mob_npc.py`
- `server/tests/unit/npc/test_aggressive_mob_npc.py`

## Audit Trail

- EXTRACTED: 31 (76%)
- INFERRED: 10 (24%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*