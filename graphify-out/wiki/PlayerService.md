# PlayerService

> 461 nodes

## Key Concepts

- **PlayerService** (142 connections) — `server/game/player_service.py`
- **Spell** (119 connections) — `server/models/spell.py`
- **MagicService** (56 connections) — `server/game/magic/magic_service.py`
- **test_magic_service.py** (47 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **_MagicServiceCore** (43 connections) — `server/game/magic/magic_service.py`
- **magic_service.py** (41 connections) — `server/game/magic/magic_service.py`
- **test_spell.py** (30 connections) — `server/tests/unit/models/test_spell.py`
- **send_game_event()** (29 connections) — `server/realtime/connection_manager_api.py`
- **spell.py** (28 connections) — `server/models/spell.py`
- **CastingStateManager** (26 connections) — `server/game/magic/casting_state_manager.py`
- **UUID** (26 connections)
- **test_player_service.py** (26 connections) — `server/tests/unit/game/test_player_service.py`
- **SpellMaterial** (25 connections) — `server/models/spell.py`
- **magic_service_completion.py** (25 connections) — `server/game/magic/magic_service_completion.py`
- **test_spell_materials.py** (22 connections) — `server/tests/unit/game/magic/test_spell_materials.py`
- **MagicServiceCompletionMixin** (21 connections) — `server/game/magic/magic_service_completion.py`
- **UUID** (20 connections)
- **test_magic_healing_events.py** (20 connections) — `server/tests/unit/game/magic/test_magic_healing_events.py`
- **asyncio** (19 connections)
- **test_spell_costs.py** (19 connections) — `server/tests/unit/game/magic/test_spell_costs.py`
- **asyncio** (19 connections)
- **MagicServiceOptionalDeps** (18 connections) — `server/game/magic/magic_service.py`
- **Any** (18 connections)
- **test_spell_registry.py** (18 connections) — `server/tests/unit/game/magic/test_spell_registry.py`
- **MagicServiceHealingMixin** (17 connections) — `server/game/magic/magic_healing_events.py`
- *... and 436 more nodes in this community*

## Relationships

- [server/dependencies.py](server-dependencies.py.md) (98 shared connections)
- [TargetMatch](TargetMatch.md) (70 shared connections)
- [get_logger](get_logger.md) (42 shared connections)
- [SpellLearningService](SpellLearningService.md) (27 shared connections)
- [CombatService](CombatService.md) (17 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (17 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (16 shared connections)
- [api/player_effects.py](api-player_effects.py.md) (7 shared connections)
- [broadcast_game_event](broadcast_game_event.md) (7 shared connections)
- [server/models/game.py](server-models-game.py.md) (6 shared connections)
- [Player](Player.md) (6 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (5 shared connections)

## Source Files

- `server/game/magic/casting_state_manager.py`
- `server/game/magic/magic_healing_events.py`
- `server/game/magic/magic_service.py`
- `server/game/magic/magic_service_completion.py`
- `server/game/magic/spell_costs.py`
- `server/game/magic/spell_materials.py`
- `server/game/magic/spell_registry.py`
- `server/game/player_search_service.py`
- `server/game/player_service.py`
- `server/game/player_state_service.py`
- `server/models/spell.py`
- `server/realtime/connection_manager_api.py`
- `server/tests/unit/game/magic/test_casting_state_manager.py`
- `server/tests/unit/game/magic/test_magic_healing_events.py`
- `server/tests/unit/game/magic/test_magic_service.py`
- `server/tests/unit/game/magic/test_spell_costs.py`
- `server/tests/unit/game/magic/test_spell_materials.py`
- `server/tests/unit/game/magic/test_spell_registry.py`
- `server/tests/unit/game/test_player_service.py`
- `server/tests/unit/models/test_spell.py`

## Audit Trail

- EXTRACTED: 1181 (91%)
- INFERRED: 120 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*