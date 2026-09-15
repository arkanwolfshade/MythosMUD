# PlayerService

> 177 nodes

## Key Concepts

- **PlayerService** (109 connections) — `server/game/player_service.py`
- **TargetResolutionService** (51 connections) — `server/services/target_resolution_service.py`
- **magic_service.py** (48 connections) — `server/game/magic/magic_service.py`
- **lifespan_magic.py** (36 connections) — `server/app/lifespan_magic.py`
- **PlayerSpellRepository** (35 connections) — `server/persistence/repositories/player_spell_repository.py`
- **SpellRegistry** (32 connections) — `server/game/magic/spell_registry.py`
- **target_resolution_service.py** (28 connections) — `server/services/target_resolution_service.py`
- **SpellTargetingService** (27 connections) — `server/game/magic/spell_targeting.py`
- **spell_learning_service.py** (25 connections) — `server/game/magic/spell_learning_service.py`
- **spell_targeting.py** (25 connections) — `server/game/magic/spell_targeting.py`
- **magic.py** (21 connections) — `server/container/bundles/magic.py`
- **SpellCostsService** (16 connections) — `server/game/magic/spell_costs.py`
- **_create_registry_and_targeting()** (16 connections) — `server/container/bundles/magic.py`
- **spell_costs.py** (16 connections) — `server/game/magic/spell_costs.py`
- **spell_registry.py** (16 connections) — `server/game/magic/spell_registry.py`
- **SpellRepository** (15 connections) — `server/persistence/repositories/spell_repository.py`
- **initialize_magic_services()** (15 connections) — `server/app/lifespan_magic.py`
- **UUID** (14 connections)
- **MagicBundle** (13 connections) — `server/container/bundles/magic.py`
- **_initialize_magic_service()** (11 connections) — `server/app/lifespan_magic.py`
- **_create_learning_mp_regen_and_magic()** (11 connections) — `server/container/bundles/magic.py`
- **.__init__()** (11 connections) — `server/game/magic/magic_service.py`
- **spell_materials.py** (11 connections) — `server/game/magic/spell_materials.py`
- **Any** (11 connections)
- **MagicServiceOptionalDeps** (10 connections) — `server/game/magic/magic_service.py`
- *... and 152 more nodes in this community*

## Relationships

- [TargetMatch](TargetMatch.md) (53 shared connections)
- [get_logger](get_logger.md) (41 shared connections)
- [SpellEffectType](SpellEffectType.md) (26 shared connections)
- [.resolve_target](resolve_target.md) (23 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (16 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (16 shared connections)
- [players.py](players.py.md) (16 shared connections)
- [test_target_resolution_service.py](test_target_resolution_service.py.md) (15 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (14 shared connections)
- [SpellLearningService](SpellLearningService.md) (14 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (14 shared connections)
- [test_magic_service.py](test_magic_service.py.md) (13 shared connections)

## Source Files

- `server/app/lifespan_magic.py`
- `server/commands/magic_commands.py`
- `server/container/bundles/magic.py`
- `server/game/magic/magic_service.py`
- `server/game/magic/spell_costs.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_learning_service.py`
- `server/game/magic/spell_materials.py`
- `server/game/magic/spell_registry.py`
- `server/game/magic/spell_targeting.py`
- `server/game/player_service.py`
- `server/persistence/repositories/player_spell_repository.py`
- `server/persistence/repositories/spell_repository.py`
- `server/services/target_resolution_service.py`
- `server/tests/unit/container/test_container_bundles.py`
- `server/tests/unit/game/magic/test_spell_targeting.py`
- `server/tests/unit/persistence/repositories/test_spell_repository.py`

## Audit Trail

- EXTRACTED: 630 (88%)
- INFERRED: 88 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*