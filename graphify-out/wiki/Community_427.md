# Community 427

> 41 nodes

## Key Concepts

- **test_utility_threat.py** (41 connections) — `server/tests/unit/services/test_utility_threat.py`
- **_combat()** (18 connections) — `server/tests/unit/services/test_utility_threat.py`
- **_p()** (18 connections) — `server/tests/unit/services/test_utility_threat.py`
- **add_utility_threat()** (16 connections) — `server/services/aggro_threat.py`
- **add_utility_threat_for_spell()** (15 connections) — `server/game/magic/spell_effects_threat.py`
- **_hate()** (15 connections) — `server/tests/unit/services/test_utility_threat.py`
- **spell_effects_threat.py** (13 connections) — `server/game/magic/spell_effects_threat.py`
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
- *... and 16 more nodes in this community*

## Relationships

- [Combat Participants](Combat_Participants.md) (15 shared connections)
- [Community 52](Community_52.md) (9 shared connections)
- [Combat Attack Execution](Combat_Attack_Execution.md) (7 shared connections)
- [Spell Effects & Combat Wiring](Spell_Effects_&_Combat_Wiring.md) (5 shared connections)
- [Combat Instance Turns](Combat_Instance_Turns.md) (5 shared connections)
- [Community 55](Community_55.md) (4 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (3 shared connections)
- [Magic Service Lifespan](Magic_Service_Lifespan.md) (2 shared connections)
- [Community 226](Community_226.md) (2 shared connections)
- [Community 69](Community_69.md) (1 shared connections)
- [Community 50](Community_50.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_effects_threat.py`
- `server/services/aggro_threat.py`
- `server/tests/unit/services/test_utility_threat.py`

## Audit Trail

- EXTRACTED: 170 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*