# AggressiveMobNPC

> 16 nodes

## Key Concepts

- **AggressiveMobNPC** (31 connections) — `server/npc/aggressive_mob_npc.py`
- **.flee()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **._handle_flee()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **.__init__()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **._setup_aggressive_mob_behavior_rules()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **test_enrich_behavior_context_handles_no_current_room()** (3 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **test_enrich_behavior_context_sets_false_when_no_players_in_room()** (3 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **.get_behavior_rules()** (2 connections) — `server/npc/aggressive_mob_npc.py`
- **Flee from current situation.** (1 connections) — `server/npc/aggressive_mob_npc.py`
- **Aggressive mob NPC type with hunting and territorial behaviors.** (1 connections) — `server/npc/aggressive_mob_npc.py`
- **Handle fleeing action.** (1 connections) — `server/npc/aggressive_mob_npc.py`
- **Initialize aggressive mob NPC.** (1 connections) — `server/npc/aggressive_mob_npc.py`
- **Setup aggressive mob-specific behavior rules.** (1 connections) — `server/npc/aggressive_mob_npc.py`
- **Get aggressive mob-specific behavior rules.** (1 connections) — `server/npc/aggressive_mob_npc.py`
- **_enrich_behavior_context sets False when current_room is None.** (1 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **_enrich_behavior_context sets player_in_range and enemy_nearby False when room…** (1 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`

## Relationships

- [._attack_target_impl](_attack_target_impl.md) (5 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [test_aggressive_mob_npc.py](test_aggressive_mob_npc.py.md) (4 shared connections)
- [._compute_player_context](_compute_player_context.md) (3 shared connections)
- [._handle_hunt_target](_handle_hunt_target.md) (2 shared connections)
- [._handle_patrol_territory](_handle_patrol_territory.md) (2 shared connections)
- [test_enrich_behavior_context_sets_player_in_range_when_players_in_room](test_enrich_behavior_context_sets_player_in_range_when_players_in_room.md) (1 shared connections)
- [test_enrich_behavior_context_swallows_compute_errors](test_enrich_behavior_context_swallows_compute_errors.md) (1 shared connections)
- [test_get_attack_damage_from_behavior_config](test_get_attack_damage_from_behavior_config.md) (1 shared connections)
- [test_get_attack_damage_invalid_string_falls_back_to_one](test_get_attack_damage_invalid_string_falls_back_to_one.md) (1 shared connections)
- [test_hunt_target_avoids_duplicate_ids](test_hunt_target_avoids_duplicate_ids.md) (1 shared connections)

## Source Files

- `server/npc/aggressive_mob_npc.py`
- `server/tests/unit/npc/test_aggressive_mob_npc.py`

## Audit Trail

- EXTRACTED: 32 (76%)
- INFERRED: 10 (24%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*