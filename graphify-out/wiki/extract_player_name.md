# extract_player_name

> 36 nodes

## Key Concepts

- **spell_effects_status.py** (24 connections) — `server/game/magic/spell_effects_status.py`
- **StatusEffectType** (18 connections) — `server/models/game.py`
- **test_game_enums.py** (11 connections) — `server/tests/unit/models/test_game_enums.py`
- **_apply_player_status_with_grace_check()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **run_status_effect()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **_apply_status_effect_to_player()** (9 connections) — `server/game/magic/spell_effects_status.py`
- **_handle_player_status_effect()** (9 connections) — `server/game/magic/spell_effects_status.py`
- **Any** (8 connections)
- **_grace_period_blocks_negative_status_effect()** (7 connections) — `server/game/magic/spell_effects_status.py`
- **_maybe_run_force_flee_effect()** (7 connections) — `server/game/magic/spell_effects_status.py`
- **_remove_player_status_effect()** (7 connections) — `server/game/magic/spell_effects_status.py`
- **_parse_status_effect_metadata()** (6 connections) — `server/game/magic/spell_effects_status.py`
- **UUID** (5 connections)
- **.remove_status_effect()** (3 connections) — `server/models/game.py`
- **test_attribute_type_enum_all_types()** (2 connections) — `server/tests/unit/models/test_game_enums.py`
- **test_attribute_type_enum_values()** (2 connections) — `server/tests/unit/models/test_game_enums.py`
- **test_position_state_enum_all_states()** (2 connections) — `server/tests/unit/models/test_game_enums.py`
- **test_position_state_enum_values()** (2 connections) — `server/tests/unit/models/test_game_enums.py`
- **test_status_effect_type_enum_all_types()** (2 connections) — `server/tests/unit/models/test_game_enums.py`
- **test_status_effect_type_enum_values()** (2 connections) — `server/tests/unit/models/test_game_enums.py`
- **Test AttributeType enum contains expected values.** (2 connections) — `server/tests/unit/models/test_game_enums.py`
- **Test StatusEffectType enum contains expected values.** (2 connections) — `server/tests/unit/models/test_game_enums.py`
- **Status effect spell logic (apply/remove status, force-flee, grace-period…** (1 connections) — `server/game/magic/spell_effects_status.py`
- **Parse effect_data for status-effect type, duration, intensity, remove flag.…** (1 connections) — `server/game/magic/spell_effects_status.py`
- **Remove a matching status effect from a player.** (1 connections) — `server/game/magic/spell_effects_status.py`
- *... and 11 more nodes in this community*

## Relationships

- [connection_manager_methods.py](connection_manager_methods.py.md) (10 shared connections)
- [eventHandlers/types.ts](eventHandlers-types.ts.md) (8 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (7 shared connections)
- [ContainerComponent](ContainerComponent.md) (5 shared connections)
- [test_container_persistence_extended_crud.py](test_container_persistence_extended_crud.py.md) (3 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (3 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (2 shared connections)
- [SkillService](SkillService.md) (1 shared connections)
- [Any](Any.md) (1 shared connections)
- [bench_cache.py](bench_cache.py.md) (1 shared connections)
- [NATSError](NATSError.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_effects_status.py`
- `server/models/game.py`
- `server/tests/unit/models/test_game_enums.py`

## Audit Trail

- EXTRACTED: 97 (94%)
- INFERRED: 6 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*