# TargetType

> 56 nodes

## Key Concepts

- **TargetType** (45 connections) — `server/schemas/shared/target_resolution.py`
- **run_flee_effect()** (25 connections) — `server/game/magic/spell_effect_flee.py`
- **spell_effects_status.py** (24 connections) — `server/game/magic/spell_effects_status.py`
- **StatusEffectType** (18 connections) — `server/models/game.py`
- **spell_effect_flee.py** (18 connections) — `server/game/magic/spell_effect_flee.py`
- **test_spell_effect_flee.py** (17 connections) — `server/tests/unit/game/magic/test_spell_effect_flee.py`
- **_apply_player_status_with_grace_check()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **run_status_effect()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **Any** (10 connections)
- **_apply_status_effect_to_player()** (9 connections) — `server/game/magic/spell_effects_status.py`
- **_handle_player_status_effect()** (9 connections) — `server/game/magic/spell_effects_status.py`
- **Any** (8 connections)
- **_flee_effect_validate_room_exits()** (7 connections) — `server/game/magic/spell_effect_flee.py`
- **_grace_period_blocks_negative_status_effect()** (7 connections) — `server/game/magic/spell_effects_status.py`
- **_maybe_run_force_flee_effect()** (7 connections) — `server/game/magic/spell_effects_status.py`
- **_remove_player_status_effect()** (7 connections) — `server/game/magic/spell_effects_status.py`
- **_player_target()** (7 connections) — `server/tests/unit/game/magic/test_spell_effect_flee.py`
- **_flee_effect_services_available()** (6 connections) — `server/game/magic/spell_effect_flee.py`
- **_parse_status_effect_metadata()** (6 connections) — `server/game/magic/spell_effects_status.py`
- **asyncio** (6 connections)
- **UUID** (5 connections)
- **_flee_effect_failure_response()** (4 connections) — `server/game/magic/spell_effect_flee.py`
- **_flee_effect_not_in_combat_response()** (4 connections) — `server/game/magic/spell_effect_flee.py`
- **_flee_effect_success_response()** (4 connections) — `server/game/magic/spell_effect_flee.py`
- **test_run_flee_effect_invalid_target_type()** (4 connections) — `server/tests/unit/game/magic/test_spell_effect_flee.py`
- *... and 31 more nodes in this community*

## Relationships

- [TargetMatch](TargetMatch.md) (35 shared connections)
- [StatusEffect](StatusEffect.md) (5 shared connections)
- [test_target_resolution_service.py](test_target_resolution_service.py.md) (5 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (4 shared connections)
- [CombatService](CombatService.md) (4 shared connections)
- [FollowService](FollowService.md) (3 shared connections)
- [combat_attack.py](combat_attack.py.md) (3 shared connections)
- [TargetResolutionResult](TargetResolutionResult.md) (3 shared connections)
- [SpellEffectType](SpellEffectType.md) (3 shared connections)
- [CombatInstance](CombatInstance.md) (3 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (3 shared connections)
- [CombatParticipant](CombatParticipant.md) (2 shared connections)

## Source Files

- `server/game/magic/spell_effect_flee.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_effects_status.py`
- `server/models/game.py`
- `server/schemas/shared/target_resolution.py`
- `server/tests/unit/game/magic/test_spell_effect_flee.py`

## Audit Trail

- EXTRACTED: 202 (94%)
- INFERRED: 12 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*