# lifespan_magic.py

> 91 nodes

## Key Concepts

- **lifespan_magic.py** (36 connections) — `server/app/lifespan_magic.py`
- **PlayerSpellRepository** (35 connections) — `server/persistence/repositories/player_spell_repository.py`
- **SpellRegistry** (32 connections) — `server/game/magic/spell_registry.py`
- **spell_learning_service.py** (25 connections) — `server/game/magic/spell_learning_service.py`
- **magic.py** (21 connections) — `server/container/bundles/magic.py`
- **MPRegenerationService** (18 connections) — `server/game/magic/mp_regeneration_service.py`
- **_create_registry_and_targeting()** (16 connections) — `server/container/bundles/magic.py`
- **spell_registry.py** (16 connections) — `server/game/magic/spell_registry.py`
- **SpellRepository** (15 connections) — `server/persistence/repositories/spell_repository.py`
- **initialize_magic_services()** (15 connections) — `server/app/lifespan_magic.py`
- **_initialize_magic_service()** (11 connections) — `server/app/lifespan_magic.py`
- **_create_learning_mp_regen_and_magic()** (11 connections) — `server/container/bundles/magic.py`
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
- **.initialize()** (6 connections) — `server/container/bundles/magic.py`
- **.process_tick_regeneration()** (6 connections) — `server/game/magic/mp_regeneration_service.py`
- **.__init__()** (5 connections) — `server/game/magic/spell_learning_service.py`
- *... and 66 more nodes in this community*

## Relationships

- [TargetMatch](TargetMatch.md) (19 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (13 shared connections)
- [SpellEffectType](SpellEffectType.md) (12 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (12 shared connections)
- [magic_service.py](magic_service.py.md) (11 shared connections)
- [SpellLearningService](SpellLearningService.md) (11 shared connections)
- [player_spell_repository.py](player_spell_repository.py.md) (11 shared connections)
- [get_logger](get_logger.md) (11 shared connections)
- [Spell](Spell.md) (9 shared connections)
- [test_magic_commands.py](test_magic_commands.py.md) (8 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (7 shared connections)
- [spell_repository.py](spell_repository.py.md) (7 shared connections)

## Source Files

- `server/app/lifespan_magic.py`
- `server/commands/magic_commands.py`
- `server/container/bundles/magic.py`
- `server/game/magic/mp_regeneration_service.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_learning_service.py`
- `server/game/magic/spell_registry.py`
- `server/persistence/repositories/player_spell_repository.py`
- `server/persistence/repositories/spell_repository.py`

## Audit Trail

- EXTRACTED: 280 (89%)
- INFERRED: 33 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*