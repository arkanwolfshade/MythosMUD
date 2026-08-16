# test_magic_service.py

> 75 nodes

## Key Concepts

- **test_magic_service.py** (48 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **MagicService** (41 connections) — `server/game/magic/magic_service.py`
- **UUID** (26 connections)
- **CastingStateManager** (25 connections) — `server/game/magic/casting_state_manager.py`
- **asyncio** (19 connections)
- **test_casting_state_manager.py** (12 connections) — `server/tests/unit/game/magic/test_casting_state_manager.py`
- **casting_state_manager.py** (11 connections) — `server/game/magic/casting_state_manager.py`
- **CastingState** (8 connections) — `server/game/magic/casting_state_manager.py`
- **StartCastingTarget** (8 connections) — `server/game/magic/casting_state_manager.py`
- **_spell()** (8 connections) — `server/tests/unit/game/magic/test_casting_state_manager.py`
- **UUID** (8 connections)
- **.start_casting()** (6 connections) — `server/game/magic/casting_state_manager.py`
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
- **.complete_casting()** (4 connections) — `server/game/magic/casting_state_manager.py`
- **.get_casting_state()** (4 connections) — `server/game/magic/casting_state_manager.py`
- *... and 50 more nodes in this community*

## Relationships

- [TargetMatch](TargetMatch.md) (34 shared connections)
- [test_magic_commands.py](test_magic_commands.py.md) (8 shared connections)
- [_MagicServiceCore](_MagicServiceCore.md) (4 shared connections)
- [SpellMaterial](SpellMaterial.md) (3 shared connections)
- [SpellLearningService](SpellLearningService.md) (2 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (1 shared connections)
- [CombatInstance](CombatInstance.md) (1 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (1 shared connections)

## Source Files

- `server/game/magic/casting_state_manager.py`
- `server/game/magic/magic_service.py`
- `server/tests/unit/game/magic/test_casting_state_manager.py`
- `server/tests/unit/game/magic/test_magic_service.py`

## Audit Trail

- EXTRACTED: 180 (77%)
- INFERRED: 55 (23%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*