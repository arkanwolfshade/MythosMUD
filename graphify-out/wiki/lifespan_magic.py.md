# lifespan_magic.py

> 58 nodes

## Key Concepts

- **lifespan_magic.py** (36 connections) — `server/app/lifespan_magic.py`
- **SpellRegistry** (32 connections) — `server/game/magic/spell_registry.py`
- **spell_registry.py** (16 connections) — `server/game/magic/spell_registry.py`
- **SpellRepository** (15 connections) — `server/persistence/repositories/spell_repository.py`
- **initialize_magic_services()** (15 connections) — `server/app/lifespan_magic.py`
- **_initialize_magic_service()** (11 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_effects()** (10 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_targeting_service()** (9 connections) — `server/app/lifespan_magic.py`
- **FastAPI** (9 connections)
- **_initialize_spell_learning_service()** (8 connections) — `server/app/lifespan_magic.py`
- **.__init__()** (8 connections) — `server/commands/magic_commands.py`
- **.combat_service()** (7 connections) — `server/game/magic/spell_effects.py`
- **_initialize_mp_regeneration_service()** (6 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_registry()** (6 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_repositories()** (6 connections) — `server/app/lifespan_magic.py`
- **_link_magic_to_combat()** (6 connections) — `server/app/lifespan_magic.py`
- **.__init__()** (5 connections) — `server/game/magic/spell_learning_service.py`
- **_validate_magic_prerequisites()** (4 connections) — `server/app/lifespan_magic.py`
- **.movement_service()** (4 connections) — `server/game/magic/spell_effects.py`
- **.list_spells()** (4 connections) — `server/game/magic/spell_registry.py`
- **.connection_manager()** (3 connections) — `server/game/magic/spell_effects.py`
- **.get_spell()** (3 connections) — `server/game/magic/spell_registry.py`
- **.get_spell_by_name()** (3 connections) — `server/game/magic/spell_registry.py`
- **.__init__()** (3 connections) — `server/game/magic/spell_registry.py`
- **.search_spells()** (3 connections) — `server/game/magic/spell_registry.py`
- *... and 33 more nodes in this community*

## Relationships

- [SpellEffects](SpellEffects.md) (15 shared connections)
- [SpellEffectType](SpellEffectType.md) (11 shared connections)
- [TargetMatch](TargetMatch.md) (9 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (9 shared connections)
- [SpellLearningService](SpellLearningService.md) (8 shared connections)
- [DatabaseError](DatabaseError.md) (6 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (5 shared connections)
- [test_magic_commands.py](test_magic_commands.py.md) (5 shared connections)
- [PlayerService](PlayerService.md) (5 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [test_magic_service.py](test_magic_service.py.md) (4 shared connections)
- [test_spell_repository.py](test_spell_repository.py.md) (3 shared connections)

## Source Files

- `server/app/lifespan_magic.py`
- `server/commands/magic_commands.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_learning_service.py`
- `server/game/magic/spell_registry.py`
- `server/persistence/repositories/spell_repository.py`
- `server/tests/unit/persistence/repositories/test_spell_repository.py`

## Audit Trail

- EXTRACTED: 167 (89%)
- INFERRED: 20 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*