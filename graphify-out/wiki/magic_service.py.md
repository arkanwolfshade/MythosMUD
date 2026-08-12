# magic_service.py

> 117 nodes

## Key Concepts

- **magic_service.py** (40 connections) — `server/game/magic/magic_service.py`
- **PlayerSpellRepository** (37 connections) — `server/persistence/repositories/player_spell_repository.py`
- **lifespan_magic.py** (35 connections) — `server/app/lifespan_magic.py`
- **SpellRegistry** (34 connections) — `server/game/magic/spell_registry.py`
- **MagicService** (29 connections) — `server/game/magic/magic_service.py`
- **SpellTargetingService** (27 connections) — `server/game/magic/spell_targeting.py`
- **SpellEffectsDeps** (25 connections) — `server/game/magic/spell_effects.py`
- **spell_learning_service.py** (21 connections) — `server/game/magic/spell_learning_service.py`
- **magic.py** (20 connections) — `server/container/bundles/magic.py`
- **spell_targeting.py** (20 connections) — `server/game/magic/spell_targeting.py`
- **MagicBundle** (19 connections) — `server/container/bundles/magic.py`
- **CastingStateManager** (18 connections) — `server/game/magic/casting_state_manager.py`
- **MagicServiceOptionalDeps** (18 connections) — `server/game/magic/magic_service.py`
- **initialize_magic_services()** (15 connections) — `server/app/lifespan_magic.py`
- **SpellRepository** (14 connections) — `server/persistence/repositories/spell_repository.py`
- **_create_registry_and_targeting()** (14 connections) — `server/container/bundles/magic.py`
- **SpellCommandError** (12 connections) — `server/commands/magic_commands.py`
- **_initialize_magic_service()** (11 connections) — `server/app/lifespan_magic.py`
- **.__init__()** (11 connections) — `server/game/magic/magic_service.py`
- **_initialize_spell_effects()** (10 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_targeting_service()** (9 connections) — `server/app/lifespan_magic.py`
- **_create_learning_mp_regen_and_magic()** (9 connections) — `server/container/bundles/magic.py`
- **FastAPI** (9 connections)
- **casting_state_manager.py** (9 connections) — `server/game/magic/casting_state_manager.py`
- **StartCastingTarget** (8 connections) — `server/game/magic/casting_state_manager.py`
- *... and 92 more nodes in this community*

## Relationships

- [Spell](Spell.md) (26 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (19 shared connections)
- [test_spell.py](test_spell.py.md) (19 shared connections)
- [SpellLearningService](SpellLearningService.md) (15 shared connections)
- [magic_service_completion.py](magic_service_completion.py.md) (15 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (15 shared connections)
- [get_logger](get_logger.md) (14 shared connections)
- [send_game_event](send_game_event.md) (11 shared connections)
- [_MagicServiceCore](_MagicServiceCore.md) (10 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (8 shared connections)
- [PlayerService](PlayerService.md) (8 shared connections)
- [spell_effects.py](spell_effects.py.md) (8 shared connections)

## Source Files

- `server/app/lifespan_magic.py`
- `server/commands/magic_commands.py`
- `server/container/bundles/magic.py`
- `server/game/magic/casting_state_manager.py`
- `server/game/magic/magic_service.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_learning_service.py`
- `server/game/magic/spell_registry.py`
- `server/game/magic/spell_targeting.py`
- `server/persistence/repositories/player_spell_repository.py`
- `server/persistence/repositories/spell_repository.py`
- `server/tests/unit/game/magic/test_spell_effects.py`
- `server/tests/unit/game/magic/test_spell_targeting.py`

## Audit Trail

- EXTRACTED: 562 (83%)
- INFERRED: 117 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*