# magic_service.py

> 160 nodes

## Key Concepts

- **magic_service.py** (48 connections) — `server/game/magic/magic_service.py`
- **_MagicServiceCore** (44 connections) — `server/game/magic/magic_service.py`
- **send_game_event()** (28 connections) — `server/realtime/connection_manager_api.py`
- **CastingStateManager** (25 connections) — `server/game/magic/casting_state_manager.py`
- **magic_service_completion.py** (25 connections) — `server/game/magic/magic_service_completion.py`
- **UUID** (21 connections)
- **SpellMaterialsService** (16 connections) — `server/game/magic/spell_materials.py`
- **get_current_tick()** (16 connections) — `server/app/game_tick_counter.py`
- **SpellCostsService** (14 connections) — `server/game/magic/spell_costs.py`
- **spell_costs.py** (13 connections) — `server/game/magic/spell_costs.py`
- **MagicServiceCompletionMixin** (12 connections) — `server/game/magic/magic_service_completion.py`
- **UUID** (12 connections)
- **JsonMap** (12 connections)
- **test_casting_state_manager.py** (12 connections) — `server/tests/unit/game/magic/test_casting_state_manager.py`
- **casting_state_manager.py** (11 connections) — `server/game/magic/casting_state_manager.py`
- **Any** (11 connections)
- **spell_materials.py** (11 connections) — `server/game/magic/spell_materials.py`
- **MagicServiceOptionalDeps** (10 connections) — `server/game/magic/magic_service.py`
- **.can_cast_spell()** (10 connections) — `server/game/magic/magic_service.py`
- **.cast_spell()** (10 connections) — `server/game/magic/magic_service.py`
- **._execute_instant_or_delayed_cast()** (10 connections) — `server/game/magic/magic_service.py`
- **._execute_casting_immediately()** (9 connections) — `server/game/magic/magic_service_completion.py`
- **._get_spell_and_validate_target()** (9 connections) — `server/game/magic/magic_service.py`
- **._start_delayed_cast()** (9 connections) — `server/game/magic/magic_service.py`
- **game_tick_counter.py** (9 connections) — `server/app/game_tick_counter.py`
- *... and 135 more nodes in this community*

## Relationships

- [TargetMatch](TargetMatch.md) (35 shared connections)
- [SpellEffects](SpellEffects.md) (17 shared connections)
- [SpellEffectType](SpellEffectType.md) (16 shared connections)
- [get_logger](get_logger.md) (14 shared connections)
- [test_magic_service.py](test_magic_service.py.md) (10 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (10 shared connections)
- [CombatService](CombatService.md) (8 shared connections)
- [resolve_lazy_attr](resolve_lazy_attr.md) (8 shared connections)
- [SpellLearningService](SpellLearningService.md) (6 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (6 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (5 shared connections)
- [NPCCombatDataProvider](NPCCombatDataProvider.md) (4 shared connections)

## Source Files

- `server/app/game_tick_counter.py`
- `server/game/magic/casting_state_manager.py`
- `server/game/magic/magic_service.py`
- `server/game/magic/magic_service_completion.py`
- `server/game/magic/spell_costs.py`
- `server/game/magic/spell_materials.py`
- `server/realtime/connection_manager_api.py`
- `server/tests/unit/game/magic/test_casting_state_manager.py`

## Audit Trail

- EXTRACTED: 442 (94%)
- INFERRED: 30 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*