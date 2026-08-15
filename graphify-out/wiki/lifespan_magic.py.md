# lifespan_magic.py

> 78 nodes

## Key Concepts

- **lifespan_magic.py** (36 connections) — `server/app/lifespan_magic.py`
- **PlayerSpellRepository** (35 connections) — `server/persistence/repositories/player_spell_repository.py`
- **SpellRegistry** (32 connections) — `server/game/magic/spell_registry.py`
- **spell_learning_service.py** (22 connections) — `server/game/magic/spell_learning_service.py`
- **test_spell_registry.py** (18 connections) — `server/tests/unit/game/magic/test_spell_registry.py`
- **spell_registry.py** (16 connections) — `server/game/magic/spell_registry.py`
- **SpellRepository** (15 connections) — `server/persistence/repositories/spell_repository.py`
- **initialize_magic_services()** (15 connections) — `server/app/lifespan_magic.py`
- **_initialize_magic_service()** (11 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_effects()** (10 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_targeting_service()** (9 connections) — `server/app/lifespan_magic.py`
- **_spell()** (9 connections) — `server/tests/unit/game/magic/test_spell_registry.py`
- **FastAPI** (9 connections)
- **_initialize_spell_learning_service()** (8 connections) — `server/app/lifespan_magic.py`
- **.__init__()** (8 connections) — `server/commands/magic_commands.py`
- **.combat_service()** (7 connections) — `server/game/magic/spell_effects.py`
- **_initialize_mp_regeneration_service()** (6 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_registry()** (6 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_repositories()** (6 connections) — `server/app/lifespan_magic.py`
- **_link_magic_to_combat()** (6 connections) — `server/app/lifespan_magic.py`
- **.__init__()** (5 connections) — `server/game/magic/spell_learning_service.py`
- **asyncio** (5 connections)
- **_validate_magic_prerequisites()** (4 connections) — `server/app/lifespan_magic.py`
- **.movement_service()** (4 connections) — `server/game/magic/spell_effects.py`
- **.list_spells()** (4 connections) — `server/game/magic/spell_registry.py`
- *... and 53 more nodes in this community*

## Relationships

- [Spell](Spell.md) (18 shared connections)
- [SpellEffectType](SpellEffectType.md) (16 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (15 shared connections)
- [magic_service.py](magic_service.py.md) (14 shared connections)
- [DatabaseError](DatabaseError.md) (14 shared connections)
- [TargetMatch](TargetMatch.md) (9 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [AliasStorage](AliasStorage.md) (8 shared connections)
- [test_spell_effects.py](test_spell_effects.py.md) (6 shared connections)
- [test_magic_service.py](test_magic_service.py.md) (4 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (3 shared connections)
- [test_spell_repository.py](test_spell_repository.py.md) (3 shared connections)

## Source Files

- `server/app/lifespan_magic.py`
- `server/commands/magic_commands.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_learning_service.py`
- `server/game/magic/spell_registry.py`
- `server/persistence/repositories/player_spell_repository.py`
- `server/persistence/repositories/spell_repository.py`
- `server/tests/unit/game/magic/test_spell_registry.py`

## Audit Trail

- EXTRACTED: 227 (85%)
- INFERRED: 39 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*