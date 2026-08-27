# PlayerService

> 127 nodes

## Key Concepts

- **PlayerService** (106 connections) — `server/game/player_service.py`
- **magic_service.py** (48 connections) — `server/game/magic/magic_service.py`
- **send_game_event()** (29 connections) — `server/realtime/connection_manager_api.py`
- **CastingStateManager** (25 connections) — `server/game/magic/casting_state_manager.py`
- **magic_service_completion.py** (25 connections) — `server/game/magic/magic_service_completion.py`
- **SpellCostsService** (14 connections) — `server/game/magic/spell_costs.py`
- **UUID** (14 connections)
- **spell_costs.py** (13 connections) — `server/game/magic/spell_costs.py`
- **MagicServiceCompletionMixin** (12 connections) — `server/game/magic/magic_service_completion.py`
- **UUID** (12 connections)
- **test_casting_state_manager.py** (12 connections) — `server/tests/unit/game/magic/test_casting_state_manager.py`
- **.__init__()** (11 connections) — `server/game/magic/magic_service.py`
- **casting_state_manager.py** (11 connections) — `server/game/magic/casting_state_manager.py`
- **Any** (11 connections)
- **Any** (11 connections)
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
- *... and 102 more nodes in this community*

## Relationships

- [api/character_creation.py](api-character_creation.py.md) (14 shared connections)
- [players.py](players.py.md) (14 shared connections)
- [ValidationError](ValidationError.md) (14 shared connections)
- [_MagicServiceCore](_MagicServiceCore.md) (13 shared connections)
- [SpellEffects](SpellEffects.md) (12 shared connections)
- [TargetMatch](TargetMatch.md) (11 shared connections)
- [test_magic_service.py](test_magic_service.py.md) (9 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (9 shared connections)
- [resolve_lazy_attr](resolve_lazy_attr.md) (8 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [SpellLearningService](SpellLearningService.md) (7 shared connections)
- [SpellMaterialsService](SpellMaterialsService.md) (7 shared connections)

## Source Files

- `server/game/magic/casting_state_manager.py`
- `server/game/magic/magic_service.py`
- `server/game/magic/magic_service_completion.py`
- `server/game/magic/spell_costs.py`
- `server/game/player_service.py`
- `server/realtime/connection_manager_api.py`
- `server/tests/unit/game/magic/test_casting_state_manager.py`

## Audit Trail

- EXTRACTED: 395 (92%)
- INFERRED: 34 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*