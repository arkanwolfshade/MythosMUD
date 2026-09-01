# test_magic_service.py

> 39 nodes

## Key Concepts

- **test_magic_service.py** (48 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **MagicService** (41 connections) — `server/game/magic/magic_service.py`
- **UUID** (26 connections)
- **asyncio** (19 connections)
- **CastingState** (8 connections) — `server/game/magic/casting_state_manager.py`
- **test_can_cast_spell_unknown_and_materials()** (6 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **test_cast_spell_material_consume_failure()** (6 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **test_check_casting_progress_completes()** (6 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **test_start_delayed_cast_in_combat()** (6 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **test_start_delayed_cast_value_error()** (6 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **test_can_cast_spell_paths()** (5 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **test_cast_spell_delayed()** (5 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **test_complete_casting_via_combat_queue()** (5 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **test_interrupt_casting_luck_fail()** (5 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **test_interrupt_casting_luck_pass()** (5 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **fixture** (5 connections)
- **_build_magic_service()** (4 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **target_match()** (4 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **test_cast_spell_instant_success()** (4 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **test_cast_spell_not_found()** (4 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **test_cast_spell_roll_failure()** (4 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **test_check_mp_and_lucidity()** (4 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **test_get_player_and_normalized_stats()** (4 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **test_get_player_and_room_missing_player()** (4 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **test_interrupt_casting_not_casting()** (4 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- *... and 14 more nodes in this community*

## Relationships

- [TargetMatch](TargetMatch.md) (16 shared connections)
- [SpellEffectType](SpellEffectType.md) (11 shared connections)
- [magic_service.py](magic_service.py.md) (10 shared connections)
- [SpellEffects](SpellEffects.md) (5 shared connections)
- [command_service.py](command_service.py.md) (5 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (1 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (1 shared connections)
- [CombatService](CombatService.md) (1 shared connections)
- [MagicCommandHandler](MagicCommandHandler.md) (1 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/game/magic/casting_state_manager.py`
- `server/game/magic/magic_service.py`
- `server/tests/unit/game/magic/test_magic_service.py`

## Audit Trail

- EXTRACTED: 121 (74%)
- INFERRED: 42 (26%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*