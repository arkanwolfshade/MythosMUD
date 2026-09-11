# magic_service.py

> 80 nodes

## Key Concepts

- **magic_service.py** (49 connections) — `server/game/magic/magic_service.py`
- **CastingStateManager** (25 connections) — `server/game/magic/casting_state_manager.py`
- **magic_service_completion.py** (25 connections) — `server/game/magic/magic_service_completion.py`
- **SpellCostsService** (16 connections) — `server/game/magic/spell_costs.py`
- **spell_costs.py** (16 connections) — `server/game/magic/spell_costs.py`
- **MagicServiceCompletionMixin** (12 connections) — `server/game/magic/magic_service_completion.py`
- **UUID** (12 connections)
- **.__init__()** (11 connections) — `server/game/magic/magic_service.py`
- **casting_state_manager.py** (11 connections) — `server/game/magic/casting_state_manager.py`
- **Any** (11 connections)
- **test_casting_state_manager.py** (11 connections) — `server/tests/unit/game/magic/test_casting_state_manager.py`
- **MagicServiceOptionalDeps** (10 connections) — `server/game/magic/magic_service.py`
- **._execute_casting_immediately()** (9 connections) — `server/game/magic/magic_service_completion.py`
- **StartCastingTarget** (8 connections) — `server/game/magic/casting_state_manager.py`
- **._complete_casting()** (8 connections) — `server/game/magic/magic_service_completion.py`
- **_spell()** (8 connections) — `server/tests/unit/game/magic/test_casting_state_manager.py`
- **UUID** (8 connections)
- **._recreate_target_from_state()** (7 connections) — `server/game/magic/magic_service_completion.py`
- **.start_casting()** (6 connections) — `server/game/magic/casting_state_manager.py`
- **._try_complete_casting_via_combat()** (6 connections) — `server/game/magic/magic_service_completion.py`
- **._try_queue_spell_for_combat()** (6 connections) — `server/game/magic/magic_service_completion.py`
- **.apply_costs()** (6 connections) — `server/game/magic/spell_costs.py`
- **._apply_spell_costs_and_effects()** (5 connections) — `server/game/magic/magic_service_completion.py`
- **._get_player_and_room()** (5 connections) — `server/game/magic/magic_service_completion.py`
- **._parse_casting_target_id()** (5 connections) — `server/game/magic/magic_service_completion.py`
- *... and 55 more nodes in this community*

## Relationships

- [Spell](Spell.md) (13 shared connections)
- [_MagicServiceCore](_MagicServiceCore.md) (12 shared connections)
- [TargetMatch](TargetMatch.md) (12 shared connections)
- [PlayerService](PlayerService.md) (10 shared connections)
- [get_logger](get_logger.md) (10 shared connections)
- [test_magic_service.py](test_magic_service.py.md) (9 shared connections)
- [SpellLearningService](SpellLearningService.md) (5 shared connections)
- [CorruptionService](CorruptionService.md) (5 shared connections)
- [Player](Player.md) (4 shared connections)
- [CombatService](CombatService.md) (3 shared connections)
- [SpellMaterialsService](SpellMaterialsService.md) (3 shared connections)
- [lifespan_magic.py](lifespan_magic.py.md) (3 shared connections)

## Source Files

- `server/game/magic/casting_state_manager.py`
- `server/game/magic/magic_service.py`
- `server/game/magic/magic_service_completion.py`
- `server/game/magic/spell_costs.py`
- `server/tests/unit/game/magic/test_casting_state_manager.py`

## Audit Trail

- EXTRACTED: 235 (94%)
- INFERRED: 15 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*