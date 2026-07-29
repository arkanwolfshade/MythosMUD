# Spell Targeting

> 284 nodes

## Key Concepts

- **TargetMatch** (115 connections) — `server/schemas/shared/target_resolution.py`
- **Spell** (80 connections) — `server/models/spell.py`
- **SpellEffects** (56 connections) — `server/game/magic/spell_effects.py`
- **spell_effects.py** (47 connections) — `server/game/magic/spell_effects.py`
- **spell_effects_heal.py** (40 connections) — `server/game/magic/spell_effects_heal.py`
- **test_spell_effects.py** (37 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **StatusEffect** (32 connections) — `server/models/game.py`
- **test_damage_grace_period.py** (26 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **spell_effects_status.py** (24 connections) — `server/game/magic/spell_effects_status.py`
- **spell_effects_support.py** (19 connections) — `server/game/magic/spell_effects_support.py`
- **run_flee_effect()** (18 connections) — `server/game/magic/spell_effect_flee.py`
- **StatusEffectType** (18 connections) — `server/models/game.py`
- **spell_effect_flee.py** (17 connections) — `server/game/magic/spell_effect_flee.py`
- **NpcSpellDamageTarget** (17 connections) — `server/game/magic/spell_effect_types.py`
- **._dispatch_effect()** (15 connections) — `server/game/magic/spell_effects.py`
- **run_heal_effect()** (15 connections) — `server/game/magic/spell_effects_heal.py`
- **SpellEffectPlayer** (14 connections) — `server/game/magic/spell_effect_types.py`
- **SpellEffectsEngineHealPort** (13 connections) — `server/game/magic/spell_effect_types.py`
- **UUID** (13 connections)
- **test_game_status_effect.py** (13 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **UUID** (12 connections)
- **spell_effect_types.py** (11 connections) — `server/game/magic/spell_effect_types.py`
- **_steal_life_resolve_target_dp()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **_steal_life_apply_target_damage()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **_run_steal_life()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- *... and 259 more nodes in this community*

## Relationships

- [. init ()](_init_%28%29.md) (52 shared connections)
- [Player Position Service](Player_Position_Service.md) (31 shared connections)
- [spell registry](spell_registry.md) (26 shared connections)
- [combat taunt](combat_taunt.md) (24 shared connections)
- [initialize nats and combat services()](initialize_nats_and_combat_services%28%29.md) (24 shared connections)
- [main()](main%28%29.md) (14 shared connections)
- [combat](combat.md) (11 shared connections)
- [Connection Manager](Connection_Manager.md) (9 shared connections)
- [login grace period](login_grace_period.md) (9 shared connections)
- [.end combat()](end_combat%28%29.md) (8 shared connections)
- [MagicServiceCore](MagicServiceCore.md) (8 shared connections)
- [Player](Player.md) (8 shared connections)

## Source Files

- `server/game/magic/spell_effect_flee.py`
- `server/game/magic/spell_effect_types.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_effects_heal.py`
- `server/game/magic/spell_effects_internal.py`
- `server/game/magic/spell_effects_stats.py`
- `server/game/magic/spell_effects_status.py`
- `server/game/magic/spell_effects_support.py`
- `server/models/game.py`
- `server/models/spell.py`
- `server/schemas/shared/target_resolution.py`
- `server/tests/unit/game/magic/test_spell_effects.py`
- `server/tests/unit/models/test_game_status_effect.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 1361 (96%)
- INFERRED: 59 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*