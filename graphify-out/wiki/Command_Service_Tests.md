# Command Service Tests

> 57 nodes · cohesion 0.04

## Key Concepts

- **test_spell_effects.py** (37 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **spell_effects()** (4 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_spell_effects_init_with_repository()** (4 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **mock_target_match()** (3 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_process_corruption_adjust_invalid_target()** (3 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_process_create_object_invalid_target()** (3 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_process_damage_invalid_target()** (3 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_process_effect_flee_not_in_combat()** (3 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_process_heal_heal_other_rejects_self_target()** (3 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_process_heal_invalid_target()** (3 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_process_heal_steal_life_capped_by_target_dp()** (3 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_process_heal_steal_life_damages_target_and_heals_caster()** (3 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_process_heal_steal_life_target_zero_dp()** (3 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_process_lucidity_adjust_invalid_target()** (3 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_process_stat_modify_invalid_target()** (3 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_process_status_effect_invalid_target()** (3 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_process_teleport_invalid_target()** (3 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **mock_player_service()** (2 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_process_effect_corruption_adjust()** (2 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_process_effect_create_object()** (2 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_process_effect_damage()** (2 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_process_effect_flee_services_not_configured()** (2 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_process_effect_heal()** (2 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_process_effect_lucidity_adjust()** (2 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_process_effect_stat_modify()** (2 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- *... and 32 more nodes in this community*

## Relationships

- [Game Magic Spell](Game_Magic_Spell.md) (20 shared connections)
- [Magic Lifespan Initialization](Magic_Lifespan_Initialization.md) (3 shared connections)
- [Realtime Connection Impl](Realtime_Connection_Impl.md) (2 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/magic/test_spell_effects.py`

## Audit Trail

- EXTRACTED: 137 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*