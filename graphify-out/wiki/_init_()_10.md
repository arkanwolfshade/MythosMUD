# . init ()

> 242 nodes

## Key Concepts

- **Spell** (84 connections) — `server/models/spell.py`
- **SpellEffects** (56 connections) — `server/game/magic/spell_effects.py`
- **spell_effects.py** (47 connections) — `server/game/magic/spell_effects.py`
- **spell_effects_heal.py** (40 connections) — `server/game/magic/spell_effects_heal.py`
- **test_spell.py** (30 connections) — `server/tests/unit/models/test_spell.py`
- **spell_effects_status.py** (24 connections) — `server/game/magic/spell_effects_status.py`
- **spell.py** (22 connections) — `server/models/spell.py`
- **spell_effects_support.py** (19 connections) — `server/game/magic/spell_effects_support.py`
- **StatusEffectType** (18 connections) — `server/models/game.py`
- **NpcSpellDamageTarget** (17 connections) — `server/game/magic/spell_effect_types.py`
- **._dispatch_effect()** (15 connections) — `server/game/magic/spell_effects.py`
- **run_heal_effect()** (15 connections) — `server/game/magic/spell_effects_heal.py`
- **test_spell_targeting.py** (15 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **SpellEffectPlayer** (14 connections) — `server/game/magic/spell_effect_types.py`
- **SpellEffectsEngineHealPort** (13 connections) — `server/game/magic/spell_effect_types.py`
- **UUID** (13 connections)
- **SpellMaterial** (13 connections) — `server/models/spell.py`
- **UUID** (12 connections)
- **spell_effect_types.py** (11 connections) — `server/game/magic/spell_effect_types.py`
- **_steal_life_resolve_target_dp()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **_steal_life_apply_target_damage()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **_run_steal_life()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **PlayerPersistenceSpellPort** (10 connections) — `server/game/magic/spell_effect_types.py`
- **_run_standard_heal_after_validation()** (10 connections) — `server/game/magic/spell_effects_heal.py`
- **_apply_player_status_with_grace_check()** (10 connections) — `server/game/magic/spell_effects_status.py`
- *... and 217 more nodes in this community*

## Relationships

- [message handler factory](message_handler_factory.md) (58 shared connections)
- [CombatService](CombatService.md) (49 shared connections)
- [. initialize handlers()](_initialize_handlers%28%29.md) (28 shared connections)
- [Player](Player.md) (12 shared connections)
- [world](world.md) (10 shared connections)
- [.end combat()](end_combat%28%29.md) (8 shared connections)
- [command execution request](command_execution_request.md) (8 shared connections)
- [main()](main%28%29.md) (8 shared connections)
- [ASGIApp](ASGIApp.md) (7 shared connections)
- [test combat attack handler](test_combat_attack_handler.md) (6 shared connections)
- [. init ()](_init_%28%29.md) (5 shared connections)
- [login grace period](login_grace_period.md) (5 shared connections)

## Source Files

- `server/game/magic/spell_effect_types.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_effects_heal.py`
- `server/game/magic/spell_effects_internal.py`
- `server/game/magic/spell_effects_stats.py`
- `server/game/magic/spell_effects_status.py`
- `server/game/magic/spell_effects_support.py`
- `server/game/magic/spell_registry.py`
- `server/models/game.py`
- `server/models/spell.py`
- `server/tests/unit/game/magic/test_spell_targeting.py`
- `server/tests/unit/models/test_spell.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 1104 (96%)
- INFERRED: 49 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*