# test_aggro_threat.py

> 34 nodes · cohesion 0.10

## Key Concepts

- **test_aggro_threat.py** (29 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **_make_combat()** (23 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **_make_participant()** (13 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **test_on_player_entered_stealth_wipes_from_all_npcs()** (6 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **test_update_aggro_excludes_dead_from_candidate()** (6 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **test_update_aggro_one_entity_sets_target()** (6 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **test_update_aggro_stability_no_switch_when_below_threshold()** (6 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **test_update_aggro_stability_switch_when_at_or_above_threshold()** (6 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **test_add_damage_threat_aggressive_mob_adds()** (5 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **test_add_damage_threat_passive_mob_skipped()** (5 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **test_aggression_level_scales_damage_threat()** (5 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **test_aggression_level_scales_heal_threat()** (5 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **test_update_aggro_no_hate_list_clears_target()** (5 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **test_add_heal_threat_accumulates_with_factor()** (4 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **test_apply_stealth_wipe_no_list_no_op()** (4 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **test_clear_aggro_for_combat_clears_both()** (4 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **test_get_npc_current_target_returns_none_when_unset()** (4 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **test_get_npc_current_target_returns_set_target()** (4 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **Unit tests for aggro/threat module (ADR-016).** (1 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **apply_stealth_wipe when NPC has no hate list does not raise.** (1 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **clear_aggro_for_combat clears npc_hate_lists and npc_current_target.** (1 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **update_aggro with empty hate list clears current target and returns (None, True)** (1 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **update_aggro with one alive entity in hate list sets them as target and returns** (1 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **update_aggro does not switch when candidate is below 110% of current target.** (1 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **update_aggro switches when candidate >= 110% of current target.** (1 connections) — `server/tests/unit/services/test_aggro_threat.py`
- *... and 9 more nodes in this community*

## Relationships

- [get_or_create_hate_list](get_or_create_hate_list.md) (13 shared connections)
- [aggro_threat.py](aggro_threat.py.md) (7 shared connections)
- [add_damage_threat](add_damage_threat.md) (7 shared connections)
- [CombatInstance](CombatInstance.md) (5 shared connections)
- [update_aggro](update_aggro.md) (5 shared connections)
- [CombatService](CombatService.md) (3 shared connections)

## Source Files

- `server/tests/unit/services/test_aggro_threat.py`

## Audit Trail

- EXTRACTED: 156 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*