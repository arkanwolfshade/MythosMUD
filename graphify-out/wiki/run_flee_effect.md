# run_flee_effect

> 31 nodes

## Key Concepts

- **run_flee_effect()** (25 connections) — `server/game/magic/spell_effect_flee.py`
- **spell_effect_flee.py** (18 connections) — `server/game/magic/spell_effect_flee.py`
- **test_spell_effect_flee.py** (18 connections) — `server/tests/unit/game/magic/test_spell_effect_flee.py`
- **Any** (10 connections)
- **_flee_effect_validate_room_exits()** (7 connections) — `server/game/magic/spell_effect_flee.py`
- **_player_target()** (7 connections) — `server/tests/unit/game/magic/test_spell_effect_flee.py`
- **_flee_effect_services_available()** (6 connections) — `server/game/magic/spell_effect_flee.py`
- **asyncio** (6 connections)
- **_flee_effect_failure_response()** (4 connections) — `server/game/magic/spell_effect_flee.py`
- **_flee_effect_not_in_combat_response()** (4 connections) — `server/game/magic/spell_effect_flee.py`
- **_flee_effect_success_response()** (4 connections) — `server/game/magic/spell_effect_flee.py`
- **test_run_flee_effect_invalid_target_type()** (4 connections) — `server/tests/unit/game/magic/test_spell_effect_flee.py`
- **test_run_flee_effect_invalid_uuid()** (4 connections) — `server/tests/unit/game/magic/test_spell_effect_flee.py`
- **test_run_flee_effect_not_in_combat()** (4 connections) — `server/tests/unit/game/magic/test_spell_effect_flee.py`
- **test_run_flee_effect_room_error()** (4 connections) — `server/tests/unit/game/magic/test_spell_effect_flee.py`
- **test_run_flee_effect_services_unavailable()** (4 connections) — `server/tests/unit/game/magic/test_spell_effect_flee.py`
- **test_run_flee_effect_success_and_failure()** (4 connections) — `server/tests/unit/game/magic/test_spell_effect_flee.py`
- **_flee_effect_invalid_target_response()** (3 connections) — `server/game/magic/spell_effect_flee.py`
- **_flee_effect_invalid_target_type_response()** (3 connections) — `server/game/magic/spell_effect_flee.py`
- **_flee_effect_room_error_response()** (3 connections) — `server/game/magic/spell_effect_flee.py`
- **_flee_effect_services_unavailable_response()** (3 connections) — `server/game/magic/spell_effect_flee.py`
- **.get_room_by_id()** (3 connections) — `server/game/magic/spell_effects.py`
- **test_flee_effect_services_available()** (2 connections) — `server/tests/unit/game/magic/test_spell_effect_flee.py`
- **test_flee_effect_validate_room_exits()** (2 connections) — `server/tests/unit/game/magic/test_spell_effect_flee.py`
- **UUID** (2 connections)
- *... and 6 more nodes in this community*

## Relationships

- [TargetMatch](TargetMatch.md) (13 shared connections)
- [CombatInstance](CombatInstance.md) (3 shared connections)
- [SpellEffects](SpellEffects.md) (3 shared connections)
- [get_username_from_user](get_username_from_user.md) (2 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_effect_flee.py`
- `server/game/magic/spell_effects.py`
- `server/tests/unit/game/magic/test_spell_effect_flee.py`

## Audit Trail

- EXTRACTED: 90 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*