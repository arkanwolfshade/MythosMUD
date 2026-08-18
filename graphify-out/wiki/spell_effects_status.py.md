# spell_effects_status.py

> 43 nodes

## Key Concepts

- **spell_effects_status.py** (24 connections) — `server/game/magic/spell_effects_status.py`
- **StatusEffectType** (18 connections) — `server/models/game.py`
- **test_game_enums.py** (11 connections) — `server/tests/unit/models/test_game_enums.py`
- **_apply_player_status_with_grace_check()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **run_status_effect()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **_apply_status_effect_to_player()** (9 connections) — `server/game/magic/spell_effects_status.py`
- **_handle_player_status_effect()** (9 connections) — `server/game/magic/spell_effects_status.py`
- **AttributeType** (8 connections) — `server/models/game.py`
- **Any** (8 connections)
- **_grace_period_blocks_negative_status_effect()** (7 connections) — `server/game/magic/spell_effects_status.py`
- **_maybe_run_force_flee_effect()** (7 connections) — `server/game/magic/spell_effects_status.py`
- **_remove_player_status_effect()** (7 connections) — `server/game/magic/spell_effects_status.py`
- **_parse_status_effect_metadata()** (6 connections) — `server/game/magic/spell_effects_status.py`
- **UUID** (5 connections)
- **.remove_status_effect()** (3 connections) — `server/models/game.py`
- **.get_attribute_modifier()** (3 connections) — `server/models/game.py`
- **StrEnum** (3 connections)
- **test_attribute_type_enum_all_types()** (2 connections) — `server/tests/unit/models/test_game_enums.py`
- **test_attribute_type_enum_values()** (2 connections) — `server/tests/unit/models/test_game_enums.py`
- **test_position_state_enum_all_states()** (2 connections) — `server/tests/unit/models/test_game_enums.py`
- **test_position_state_enum_values()** (2 connections) — `server/tests/unit/models/test_game_enums.py`
- **test_status_effect_type_enum_all_types()** (2 connections) — `server/tests/unit/models/test_game_enums.py`
- **test_status_effect_type_enum_values()** (2 connections) — `server/tests/unit/models/test_game_enums.py`
- **Status effect spell logic (apply/remove status, force-flee, grace-period…** (1 connections) — `server/game/magic/spell_effects_status.py`
- **Parse effect_data for status-effect type, duration, intensity, remove flag.…** (1 connections) — `server/game/magic/spell_effects_status.py`
- *... and 18 more nodes in this community*

## Relationships

- [server/models/game.py](server-models-game.py.md) (10 shared connections)
- [TargetMatch](TargetMatch.md) (10 shared connections)
- [Spell](Spell.md) (8 shared connections)
- [Stats](Stats.md) (3 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (3 shared connections)
- [run_flee_effect](run_flee_effect.md) (3 shared connections)
- [models/player.py](models-player.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [LucidityService](LucidityService.md) (2 shared connections)
- [CombatParticipant](CombatParticipant.md) (1 shared connections)
- [memory_profiler.py](memory_profiler.py.md) (1 shared connections)
- [TargetType](TargetType.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_effects_status.py`
- `server/models/game.py`
- `server/tests/unit/models/test_game_enums.py`

## Audit Trail

- EXTRACTED: 107 (95%)
- INFERRED: 6 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*