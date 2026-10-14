# test_utility_threat.py

> 36 nodes

## Key Concepts

- **test_utility_threat.py** (44 connections) — `server/tests/unit/services/test_utility_threat.py`
- **_combat()** (18 connections) — `server/tests/unit/services/test_utility_threat.py`
- **_p()** (18 connections) — `server/tests/unit/services/test_utility_threat.py`
- **add_utility_threat()** (17 connections) — `server/services/aggro_threat.py`
- **add_utility_threat_for_spell()** (15 connections) — `server/game/magic/spell_effects_threat.py`
- **_hate()** (15 connections) — `server/tests/unit/services/test_utility_threat.py`
- **test_process_effect_adds_utility_threat_only_for_successful_buffs_and_debuffs()** (11 connections) — `server/tests/unit/services/test_utility_threat.py`
- **test_a_target_that_is_not_a_player_or_npc_adds_nothing()** (10 connections) — `server/tests/unit/services/test_utility_threat.py`
- **_service_for()** (9 connections) — `server/tests/unit/services/test_utility_threat.py`
- **_target()** (9 connections) — `server/tests/unit/services/test_utility_threat.py`
- **_spell_action()** (8 connections) — `server/tests/unit/services/test_utility_threat.py`
- **test_a_buff_on_an_ally_or_self_draws_every_npc_in_the_fight()** (8 connections) — `server/tests/unit/services/test_utility_threat.py`
- **test_a_debuff_on_one_npc_draws_only_that_npc()** (7 connections) — `server/tests/unit/services/test_utility_threat.py`
- **test_an_npc_target_outside_the_casters_fight_adds_nothing()** (7 connections) — `server/tests/unit/services/test_utility_threat.py`
- **test_nothing_is_added_outside_combat_or_without_a_service()** (7 connections) — `server/tests/unit/services/test_utility_threat.py`
- **test_passive_mobs_still_take_utility_threat_but_not_damage_threat()** (7 connections) — `server/tests/unit/services/test_utility_threat.py`
- **test_a_spell_queued_without_a_target_is_aimed_at_the_caster()** (6 connections) — `server/tests/unit/services/test_utility_threat.py`
- **test_non_positive_utility_threat_is_ignored()** (6 connections) — `server/tests/unit/services/test_utility_threat.py`
- **test_utility_threat_is_scaled_by_the_npcs_aggression_level()** (6 connections) — `server/tests/unit/services/test_utility_threat.py`
- **test_a_spell_aimed_at_an_ally_is_a_player_target()** (5 connections) — `server/tests/unit/services/test_utility_threat.py`
- **test_a_spell_aimed_at_an_npc_is_an_npc_target()** (5 connections) — `server/tests/unit/services/test_utility_threat.py`
- **test_a_spell_aimed_at_someone_no_longer_in_the_fight_keeps_the_old_npc_behaviour()** (5 connections) — `server/tests/unit/services/test_utility_threat.py`
- **test_default_utility_threat_comes_from_config()** (5 connections) — `server/tests/unit/services/test_utility_threat.py`
- **test_utility_threat_accumulates()** (5 connections) — `server/tests/unit/services/test_utility_threat.py`
- **parametrize** (5 connections)
- *... and 11 more nodes in this community*

## Relationships

- [CombatParticipant](CombatParticipant.md) (15 shared connections)
- [CombatService](CombatService.md) (11 shared connections)
- [aggro_threat.py](aggro_threat.py.md) (8 shared connections)
- [SpellEffects](SpellEffects.md) (7 shared connections)
- [TargetMatch](TargetMatch.md) (5 shared connections)
- [CombatInstance](CombatInstance.md) (5 shared connections)
- [TargetType](TargetType.md) (3 shared connections)
- [SpellEffectType](SpellEffectType.md) (3 shared connections)
- [NATSService](NATSService.md) (3 shared connections)

## Source Files

- `server/game/magic/spell_effects_threat.py`
- `server/services/aggro_threat.py`
- `server/tests/unit/services/test_utility_threat.py`

## Audit Trail

- EXTRACTED: 165 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*