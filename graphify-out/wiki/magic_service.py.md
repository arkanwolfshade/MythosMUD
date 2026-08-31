# magic_service.py

> 112 nodes

## Key Concepts

- **magic_service.py** (48 connections) — `server/game/magic/magic_service.py`
- **SpellRegistry** (32 connections) — `server/game/magic/spell_registry.py`
- **send_game_event()** (28 connections) — `server/realtime/connection_manager_api.py`
- **CastingStateManager** (25 connections) — `server/game/magic/casting_state_manager.py`
- **SpellCostsService** (14 connections) — `server/game/magic/spell_costs.py`
- **resolve_lazy_attr()** (14 connections) — `server/realtime/connection_manager_lazy.py`
- **spell_costs.py** (13 connections) — `server/game/magic/spell_costs.py`
- **test_casting_state_manager.py** (12 connections) — `server/tests/unit/game/magic/test_casting_state_manager.py`
- **.__init__()** (11 connections) — `server/game/magic/magic_service.py`
- **casting_state_manager.py** (11 connections) — `server/game/magic/casting_state_manager.py`
- **test_connection_manager_api.py** (11 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **MagicServiceOptionalDeps** (10 connections) — `server/game/magic/magic_service.py`
- **connection_manager_lazy.py** (9 connections) — `server/realtime/connection_manager_lazy.py`
- **CastingState** (8 connections) — `server/game/magic/casting_state_manager.py`
- **StartCastingTarget** (8 connections) — `server/game/magic/casting_state_manager.py`
- **_spell()** (8 connections) — `server/tests/unit/game/magic/test_casting_state_manager.py`
- **UUID** (8 connections)
- **_ConnectionManagerAPI** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_player_status_update()** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_room_description()** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_system_notification()** (7 connections) — `server/realtime/connection_manager_api.py`
- **asyncio** (7 connections)
- **test_connection_manager_lazy.py** (7 connections) — `server/tests/unit/realtime/test_connection_manager_lazy.py`
- **.start_casting()** (6 connections) — `server/game/magic/casting_state_manager.py`
- **UUID** (6 connections)
- *... and 87 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (27 shared connections)
- [Spell](Spell.md) (23 shared connections)
- [_MagicServiceCore](_MagicServiceCore.md) (13 shared connections)
- [test_magic_service.py](test_magic_service.py.md) (6 shared connections)
- [magic_service_completion.py](magic_service_completion.py.md) (6 shared connections)
- [lifespan_magic.py](lifespan_magic.py.md) (6 shared connections)
- [resolve_connection_manager](resolve_connection_manager.md) (6 shared connections)
- [SpellLearningService](SpellLearningService.md) (5 shared connections)
- [CombatService](CombatService.md) (5 shared connections)
- [PlayerService](PlayerService.md) (5 shared connections)
- [AliasStorage](AliasStorage.md) (3 shared connections)
- [SpellMaterialsService](SpellMaterialsService.md) (3 shared connections)

## Source Files

- `server/game/magic/casting_state_manager.py`
- `server/game/magic/magic_service.py`
- `server/game/magic/spell_costs.py`
- `server/game/magic/spell_registry.py`
- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_api.py`
- `server/realtime/connection_manager_lazy.py`
- `server/tests/unit/game/magic/test_casting_state_manager.py`
- `server/tests/unit/realtime/test_connection_manager_api.py`
- `server/tests/unit/realtime/test_connection_manager_lazy.py`

## Audit Trail

- EXTRACTED: 285 (91%)
- INFERRED: 29 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*