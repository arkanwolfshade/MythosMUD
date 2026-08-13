# TargetMatch

> 272 nodes

## Key Concepts

- **TargetMatch** (121 connections) — `server/schemas/shared/target_resolution.py`
- **spell_effects.py** (48 connections) — `server/game/magic/spell_effects.py`
- **spell_effects_heal.py** (40 connections) — `server/game/magic/spell_effects_heal.py`
- **test_spell_effects.py** (38 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **TargetType** (31 connections) — `server/schemas/shared/target_resolution.py`
- **test_damage_grace_period.py** (27 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **SpellEffectsDeps** (25 connections) — `server/game/magic/spell_effects.py`
- **spell_effects_status.py** (24 connections) — `server/game/magic/spell_effects_status.py`
- **asyncio** (23 connections)
- **spell_effects_support.py** (19 connections) — `server/game/magic/spell_effects_support.py`
- **NpcSpellDamageTarget** (18 connections) — `server/game/magic/spell_effect_types.py`
- **StatusEffectType** (18 connections) — `server/models/game.py`
- **run_flee_effect()** (18 connections) — `server/game/magic/spell_effect_flee.py`
- **spell_effect_flee.py** (17 connections) — `server/game/magic/spell_effect_flee.py`
- **test_target_resolution.py** (16 connections) — `server/tests/unit/schemas/test_target_resolution.py`
- **run_heal_effect()** (15 connections) — `server/game/magic/spell_effects_heal.py`
- **SpellEffectsEngineHealPort** (13 connections) — `server/game/magic/spell_effect_types.py`
- **PlayerPersistenceSpellPort** (11 connections) — `server/game/magic/spell_effect_types.py`
- **SpellEffectPlayer** (11 connections) — `server/game/magic/spell_effect_types.py`
- **_run_steal_life()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **_steal_life_apply_target_damage()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **spell_effect_types.py** (11 connections) — `server/game/magic/spell_effect_types.py`
- **_run_standard_heal_after_validation()** (10 connections) — `server/game/magic/spell_effects_heal.py`
- **_apply_player_status_with_grace_check()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **run_status_effect()** (10 connections) — `server/game/magic/spell_effects_status.py`
- *... and 247 more nodes in this community*

## Relationships

- [PlayerService](PlayerService.md) (101 shared connections)
- [CombatService](CombatService.md) (44 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (38 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (14 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (10 shared connections)
- [get_logger](get_logger.md) (10 shared connections)
- [StatusEffect](StatusEffect.md) (7 shared connections)
- [get_username_from_user](get_username_from_user.md) (6 shared connections)
- [server/models/game.py](server-models-game.py.md) (4 shared connections)
- [EventBus](EventBus.md) (4 shared connections)
- [log_and_raise](log_and_raise.md) (3 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (3 shared connections)

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
- `server/schemas/shared/target_resolution.py`
- `server/services/combat_service_state.py`
- `server/tests/unit/game/magic/test_spell_effects.py`
- `server/tests/unit/schemas/test_target_resolution.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 749 (97%)
- INFERRED: 26 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*