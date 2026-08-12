# spell_effects_status.py

> 40 nodes

## Key Concepts

- **spell_effects_status.py** (24 connections) — `server/game/magic/spell_effects_status.py`
- **StatusEffectType** (18 connections) — `server/models/game.py`
- **run_flee_effect()** (18 connections) — `server/game/magic/spell_effect_flee.py`
- **spell_effect_flee.py** (17 connections) — `server/game/magic/spell_effect_flee.py`
- **_apply_player_status_with_grace_check()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **run_status_effect()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **Any** (10 connections)
- **_apply_status_effect_to_player()** (9 connections) — `server/game/magic/spell_effects_status.py`
- **_handle_player_status_effect()** (9 connections) — `server/game/magic/spell_effects_status.py`
- **Any** (8 connections)
- **_grace_period_blocks_negative_status_effect()** (7 connections) — `server/game/magic/spell_effects_status.py`
- **_maybe_run_force_flee_effect()** (7 connections) — `server/game/magic/spell_effects_status.py`
- **_remove_player_status_effect()** (7 connections) — `server/game/magic/spell_effects_status.py`
- **_parse_status_effect_metadata()** (6 connections) — `server/game/magic/spell_effects_status.py`
- **_flee_effect_validate_room_exits()** (5 connections) — `server/game/magic/spell_effect_flee.py`
- **UUID** (5 connections)
- **_flee_effect_failure_response()** (4 connections) — `server/game/magic/spell_effect_flee.py`
- **_flee_effect_not_in_combat_response()** (4 connections) — `server/game/magic/spell_effect_flee.py`
- **_flee_effect_services_available()** (4 connections) — `server/game/magic/spell_effect_flee.py`
- **_flee_effect_success_response()** (4 connections) — `server/game/magic/spell_effect_flee.py`
- **_flee_effect_invalid_target_response()** (3 connections) — `server/game/magic/spell_effect_flee.py`
- **_flee_effect_invalid_target_type_response()** (3 connections) — `server/game/magic/spell_effect_flee.py`
- **_flee_effect_room_error_response()** (3 connections) — `server/game/magic/spell_effect_flee.py`
- **_flee_effect_services_unavailable_response()** (3 connections) — `server/game/magic/spell_effect_flee.py`
- **.get_room_by_id()** (3 connections) — `server/game/magic/spell_effects.py`
- *... and 15 more nodes in this community*

## Relationships

- [TargetMatch](TargetMatch.md) (14 shared connections)
- [Spell](Spell.md) (11 shared connections)
- [server/models/game.py](server-models-game.py.md) (9 shared connections)
- [spell_effects.py](spell_effects.py.md) (4 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [test_combat_flee_handler.py](test_combat_flee_handler.py.md) (2 shared connections)
- [Player](Player.md) (1 shared connections)
- [test_damage_grace_period.py](test_damage_grace_period.py.md) (1 shared connections)
- [MemoryProfiler](MemoryProfiler.md) (1 shared connections)
- [test_spell.py](test_spell.py.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_effect_flee.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_effects_status.py`
- `server/models/game.py`

## Audit Trail

- EXTRACTED: 214 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*