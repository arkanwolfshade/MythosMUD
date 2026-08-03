# room validator toolkit

> 55 nodes

## Key Concepts

- **test_aggro_threat.py** (29 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **_make_combat()** (23 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **get_or_create_hate_list()** (19 connections) — `server/services/aggro_threat.py`
- **_make_participant()** (13 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **combat_service_end.py** (11 connections) — `server/services/combat_service_end.py`
- **clear_aggro_for_combat()** (6 connections) — `server/services/aggro_threat.py`
- **test_update_aggro_one_entity_sets_target()** (6 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **test_update_aggro_stability_no_switch_when_below_threshold()** (6 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **test_update_aggro_stability_switch_when_at_or_above_threshold()** (6 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **test_update_aggro_excludes_dead_from_candidate()** (6 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **test_on_player_entered_stealth_wipes_from_all_npcs()** (6 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **end_combat()** (5 connections) — `server/services/combat_service_end.py`
- **test_apply_taunt_same_room_sets_threat_above_top()** (5 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **test_apply_taunt_different_room_no_op()** (5 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **test_apply_stealth_wipe_removes_entity()** (5 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **test_update_aggro_no_hate_list_clears_target()** (5 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **test_add_damage_threat_passive_mob_skipped()** (5 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **test_add_damage_threat_aggressive_mob_adds()** (5 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **test_aggression_level_scales_damage_threat()** (5 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **test_aggression_level_scales_heal_threat()** (5 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **test_get_or_create_hate_list_creates_empty()** (4 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **test_add_damage_threat_accumulates()** (4 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **test_add_damage_threat_ignores_zero()** (4 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **test_add_heal_threat_accumulates_with_factor()** (4 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **test_apply_stealth_wipe_no_list_no_op()** (4 connections) — `server/tests/unit/services/test_aggro_threat.py`
- *... and 30 more nodes in this community*

## Relationships

- [Item Instances](Item_Instances.md) (41 shared connections)
- [NPC Combat](NPC_Combat.md) (3 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)

## Source Files

- `server/services/aggro_threat.py`
- `server/services/combat_service_end.py`
- `server/tests/unit/services/test_aggro_threat.py`

## Audit Trail

- EXTRACTED: 236 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*