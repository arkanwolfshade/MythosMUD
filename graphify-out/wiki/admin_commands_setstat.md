# admin commands setstat

> 30 nodes

## Key Concepts

- **run_flee_effect()** (25 connections) — `server/game/magic/spell_effect_flee.py`
- **spell_effect_flee.py** (18 connections) — `server/game/magic/spell_effect_flee.py`
- **test_spell_effect_flee.py** (17 connections) — `server/tests/unit/game/magic/test_spell_effect_flee.py`
- **Any** (10 connections)
- **_flee_effect_validate_room_exits()** (7 connections) — `server/game/magic/spell_effect_flee.py`
- **_player_target()** (7 connections) — `server/tests/unit/game/magic/test_spell_effect_flee.py`
- **_flee_effect_services_available()** (6 connections) — `server/game/magic/spell_effect_flee.py`
- **_flee_effect_not_in_combat_response()** (4 connections) — `server/game/magic/spell_effect_flee.py`
- **_flee_effect_success_response()** (4 connections) — `server/game/magic/spell_effect_flee.py`
- **_flee_effect_failure_response()** (4 connections) — `server/game/magic/spell_effect_flee.py`
- **_flee_effect_invalid_target_type_response()** (3 connections) — `server/game/magic/spell_effect_flee.py`
- **_flee_effect_services_unavailable_response()** (3 connections) — `server/game/magic/spell_effect_flee.py`
- **_flee_effect_invalid_target_response()** (3 connections) — `server/game/magic/spell_effect_flee.py`
- **_flee_effect_room_error_response()** (3 connections) — `server/game/magic/spell_effect_flee.py`
- **.get_room_by_id()** (3 connections) — `server/game/magic/spell_effects.py`
- **test_run_flee_effect_invalid_target_type()** (3 connections) — `server/tests/unit/game/magic/test_spell_effect_flee.py`
- **test_run_flee_effect_services_unavailable()** (3 connections) — `server/tests/unit/game/magic/test_spell_effect_flee.py`
- **test_run_flee_effect_invalid_uuid()** (3 connections) — `server/tests/unit/game/magic/test_spell_effect_flee.py`
- **test_run_flee_effect_not_in_combat()** (3 connections) — `server/tests/unit/game/magic/test_spell_effect_flee.py`
- **test_run_flee_effect_room_error()** (3 connections) — `server/tests/unit/game/magic/test_spell_effect_flee.py`
- **test_run_flee_effect_success_and_failure()** (3 connections) — `server/tests/unit/game/magic/test_spell_effect_flee.py`
- **UUID** (2 connections)
- **test_flee_effect_services_available()** (2 connections) — `server/tests/unit/game/magic/test_spell_effect_flee.py`
- **test_flee_effect_validate_room_exits()** (2 connections) — `server/tests/unit/game/magic/test_spell_effect_flee.py`
- **Flee spell effect: voluntary flee mechanics (success roll, lose-attack-on-fail,** (1 connections) — `server/game/magic/spell_effect_flee.py`
- *... and 5 more nodes in this community*

## Relationships

- [spell game magic](spell_game_magic.md) (10 shared connections)
- [coercion int inventory](coercion_int_inventory.md) (5 shared connections)
- [command factories exploration](command_factories_exploration.md) (3 shared connections)
- [command factories communication](command_factories_communication.md) (3 shared connections)

## Source Files

- `server/game/magic/spell_effect_flee.py`
- `server/game/magic/spell_effects.py`
- `server/tests/unit/game/magic/test_spell_effect_flee.py`

## Audit Trail

- EXTRACTED: 145 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*