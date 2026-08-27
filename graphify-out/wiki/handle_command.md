# handle_command

> 45 nodes

## Key Concepts

- **AggressiveMobNPC** (31 connections) — `server/npc/aggressive_mob_npc.py`
- **test_aggressive_mob_npc.py** (24 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **_make_aggro()** (13 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **.flee()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **._handle_flee()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **._handle_hunt_target()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **._handle_patrol_territory()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **.hunt_target()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **.patrol_territory()** (3 connections) — `server/npc/aggressive_mob_npc.py`
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
- *... and 20 more nodes in this community*

## Relationships

- [worktree-plan-template.md](worktree-plan-template.md.md) (5 shared connections)
- [NPCDefinition](NPCDefinition.md) (3 shared connections)
- [NPC Occupants Verification Summary](NPC_Occupants_Verification_Summary.md) (3 shared connections)
- [📈 Performance Impact](📈_Performance_Impact.md) (2 shared connections)
- [test_combat_monitoring_service.py](test_combat_monitoring_service.py.md) (1 shared connections)
- [Invite](Invite.md) (1 shared connections)
- [build_event](build_event.md) (1 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)

## Source Files

- `server/npc/aggressive_mob_npc.py`
- `server/tests/unit/npc/test_aggressive_mob_npc.py`

## Audit Trail

- EXTRACTED: 82 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*