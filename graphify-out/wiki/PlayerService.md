# PlayerService

> 182 nodes

## Key Concepts

- **PlayerService** (106 connections) — `server/game/player_service.py`
- **player_service.py** (49 connections) — `server/game/player_service.py`
- **magic_service.py** (48 connections) — `server/game/magic/magic_service.py`
- **lifespan_magic.py** (36 connections) — `server/app/lifespan_magic.py`
- **PlayerSpellRepository** (35 connections) — `server/persistence/repositories/player_spell_repository.py`
- **SpellRegistry** (32 connections) — `server/game/magic/spell_registry.py`
- **send_game_event()** (29 connections) — `server/realtime/connection_manager_api.py`
- **magic_service_completion.py** (25 connections) — `server/game/magic/magic_service_completion.py`
- **spell_learning_service.py** (22 connections) — `server/game/magic/spell_learning_service.py`
- **player_spell_repository.py** (22 connections) — `server/persistence/repositories/player_spell_repository.py`
- **MPRegenerationService** (18 connections) — `server/game/magic/mp_regeneration_service.py`
- **initialize_magic_services()** (15 connections) — `server/app/lifespan_magic.py`
- **magic_healing_events.py** (15 connections) — `server/game/magic/magic_healing_events.py`
- **SpellCostsService** (14 connections) — `server/game/magic/spell_costs.py`
- **UUID** (14 connections)
- **mp_regeneration_service.py** (13 connections) — `server/game/magic/mp_regeneration_service.py`
- **spell_costs.py** (13 connections) — `server/game/magic/spell_costs.py`
- **PlayerStateService** (12 connections) — `server/game/player_state_service.py`
- **_initialize_magic_service()** (11 connections) — `server/app/lifespan_magic.py`
- **.__init__()** (11 connections) — `server/game/magic/magic_service.py`
- **Any** (11 connections)
- **MagicServiceOptionalDeps** (10 connections) — `server/game/magic/magic_service.py`
- **PlayerSearchService** (10 connections) — `server/game/player_search_service.py`
- **_initialize_spell_effects()** (10 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_targeting_service()** (9 connections) — `server/app/lifespan_magic.py`
- *... and 157 more nodes in this community*

## Relationships

- [Spell](Spell.md) (32 shared connections)
- [get_logger](get_logger.md) (32 shared connections)
- [TargetMatch](TargetMatch.md) (20 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (19 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (17 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (17 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (15 shared connections)
- [SpellLearningService](SpellLearningService.md) (13 shared connections)
- [test_magic_service.py](test_magic_service.py.md) (13 shared connections)
- [_MagicServiceCore](_MagicServiceCore.md) (12 shared connections)
- [test_player_spell_repository.py](test_player_spell_repository.py.md) (12 shared connections)
- [AliasStorage](AliasStorage.md) (11 shared connections)

## Source Files

- `server/app/lifespan_magic.py`
- `server/commands/magic_commands.py`
- `server/game/magic/magic_healing_events.py`
- `server/game/magic/magic_service.py`
- `server/game/magic/magic_service_completion.py`
- `server/game/magic/mp_regeneration_service.py`
- `server/game/magic/spell_costs.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_learning_service.py`
- `server/game/magic/spell_registry.py`
- `server/game/player_search_service.py`
- `server/game/player_service.py`
- `server/game/player_state_service.py`
- `server/persistence/repositories/player_spell_repository.py`
- `server/realtime/connection_manager_api.py`
- `server/tests/unit/game/magic/test_spell_targeting.py`

## Audit Trail

- EXTRACTED: 605 (90%)
- INFERRED: 65 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*