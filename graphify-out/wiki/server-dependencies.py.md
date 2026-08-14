# server/dependencies.py

> 488 nodes

## Key Concepts

- **server/dependencies.py** (104 connections) — `server/dependencies.py`
- **test_dependencies.py** (60 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **TargetResolutionService** (53 connections) — `server/services/target_resolution_service.py`
- **get_container()** (40 connections) — `server/dependencies.py`
- **PlayerSpellRepository** (39 connections) — `server/persistence/repositories/player_spell_repository.py`
- **SpellRegistry** (36 connections) — `server/game/magic/spell_registry.py`
- **lifespan_magic.py** (35 connections) — `server/app/lifespan_magic.py`
- **SpellTargetingService** (30 connections) — `server/game/magic/spell_targeting.py`
- **Request** (28 connections)
- **target_resolution_service.py** (27 connections) — `server/services/target_resolution_service.py`
- **spell_targeting.py** (25 connections) — `server/game/magic/spell_targeting.py`
- **MagicBundle** (23 connections) — `server/container/bundles/magic.py`
- **spell_learning_service.py** (22 connections) — `server/game/magic/spell_learning_service.py`
- **magic.py** (21 connections) — `server/container/bundles/magic.py`
- **MPRegenerationService** (19 connections) — `server/game/magic/mp_regeneration_service.py`
- **test_dependency_injection.py** (18 connections) — `server/tests/unit/test_dependency_injection.py`
- **SpellRepository** (16 connections) — `server/persistence/repositories/spell_repository.py`
- **_create_registry_and_targeting()** (16 connections) — `server/container/bundles/magic.py`
- **spell_registry.py** (16 connections) — `server/game/magic/spell_registry.py`
- **test_level_service.py** (16 connections) — `server/tests/unit/game/test_level_service.py`
- **initialize_magic_services()** (15 connections) — `server/app/lifespan_magic.py`
- **total_xp_for_level()** (15 connections) — `server/game/level_curve.py`
- **test_level_curve.py** (15 connections) — `server/tests/unit/game/test_level_curve.py`
- **LevelService** (13 connections) — `server/game/level_service.py`
- **get_player_service()** (13 connections) — `server/dependencies.py`
- *... and 463 more nodes in this community*

## Relationships

- [PlayerService](PlayerService.md) (98 shared connections)
- [get_logger](get_logger.md) (59 shared connections)
- [TargetMatch](TargetMatch.md) (50 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (34 shared connections)
- [CombatService](CombatService.md) (25 shared connections)
- [SpellLearningService](SpellLearningService.md) (22 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (22 shared connections)
- [test_target_resolution_service.py](test_target_resolution_service.py.md) (13 shared connections)
- [Stats](Stats.md) (9 shared connections)
- [RoomService](RoomService.md) (8 shared connections)
- [Player](Player.md) (6 shared connections)
- [test_mp_regeneration_service.py](test_mp_regeneration_service.py.md) (5 shared connections)

## Source Files

- `server/app/lifespan_magic.py`
- `server/commands/teach_command.py`
- `server/container/bundles/magic.py`
- `server/dependencies.py`
- `server/game/level_curve.py`
- `server/game/level_service.py`
- `server/game/magic/mp_regeneration_service.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_learning_service.py`
- `server/game/magic/spell_registry.py`
- `server/game/magic/spell_targeting.py`
- `server/persistence/repositories/player_spell_repository.py`
- `server/persistence/repositories/spell_repository.py`
- `server/services/target_resolution_service.py`
- `server/tests/unit/container/test_container_bundles.py`
- `server/tests/unit/game/magic/test_spell_targeting.py`
- `server/tests/unit/game/test_level_curve.py`
- `server/tests/unit/game/test_level_service.py`
- `server/tests/unit/infrastructure/test_dependencies.py`
- `server/tests/unit/test_dependency_injection.py`

## Audit Trail

- EXTRACTED: 1107 (91%)
- INFERRED: 108 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*