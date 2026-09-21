# AggressiveMobNPC

> 41 nodes

## Key Concepts

- **AggressiveMobNPC** (31 connections) — `server/npc/aggressive_mob_npc.py`
- **test_aggressive_mob_npc.py** (23 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **_make_aggro()** (13 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **.flee()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **._handle_flee()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **.__init__()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **._setup_aggressive_mob_behavior_rules()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **test_attack_via_create_task_with_running_loop()** (3 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **test_enrich_behavior_context_handles_no_current_room()** (3 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **test_enrich_behavior_context_sets_false_when_no_players_in_room()** (3 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **test_enrich_behavior_context_sets_player_in_range_when_players_in_room()** (3 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **test_enrich_behavior_context_swallows_compute_errors()** (3 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **test_flee_error_returns_false()** (3 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **test_get_attack_damage_from_behavior_config()** (3 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **test_get_attack_damage_invalid_string_falls_back_to_one()** (3 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **test_hunt_target_avoids_duplicate_ids()** (3 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **.get_behavior_rules()** (2 connections) — `server/npc/aggressive_mob_npc.py`
- **test_attack_target_error_returns_false()** (2 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **test_attack_target_fallback_publishes_event()** (2 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **test_attack_via_combat_integration_none_when_missing()** (2 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **test_attack_via_dropped_without_loop_or_bus()** (2 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **test_attack_via_event_bus_without_running_loop()** (2 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **test_compute_player_context_without_service()** (2 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **test_flee_and_patrol_and_handlers()** (2 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **test_get_attack_damage_bool_and_float()** (2 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- *... and 16 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (5 shared connections)
- [._attack_target_impl](_attack_target_impl.md) (5 shared connections)
- [._compute_player_context](_compute_player_context.md) (3 shared connections)
- [._handle_hunt_target](_handle_hunt_target.md) (2 shared connections)
- [._handle_patrol_territory](_handle_patrol_territory.md) (2 shared connections)
- [test_auth_utils.py](test_auth_utils.py.md) (1 shared connections)

## Source Files

- `server/npc/aggressive_mob_npc.py`
- `server/tests/unit/npc/test_aggressive_mob_npc.py`

## Audit Trail

- EXTRACTED: 78 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*