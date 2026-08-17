# lifespan_magic.py

> 117 nodes

## Key Concepts

- **lifespan_magic.py** (36 connections) — `server/app/lifespan_magic.py`
- **PlayerSpellRepository** (35 connections) — `server/persistence/repositories/player_spell_repository.py`
- **SpellRegistry** (32 connections) — `server/game/magic/spell_registry.py`
- **MagicCommandHandler** (30 connections) — `server/commands/magic_commands.py`
- **magic_commands.py** (26 connections) — `server/commands/magic_commands.py`
- **spell_learning_service.py** (22 connections) — `server/game/magic/spell_learning_service.py`
- **Any** (19 connections)
- **spell_registry.py** (16 connections) — `server/game/magic/spell_registry.py`
- **SpellRepository** (15 connections) — `server/persistence/repositories/spell_repository.py`
- **initialize_magic_services()** (15 connections) — `server/app/lifespan_magic.py`
- **magic_service()** (14 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **_initialize_magic_service()** (11 connections) — `server/app/lifespan_magic.py`
- **.__init__()** (11 connections) — `server/game/magic/magic_service.py`
- **MagicServiceOptionalDeps** (10 connections) — `server/game/magic/magic_service.py`
- **_initialize_spell_effects()** (10 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_targeting_service()** (9 connections) — `server/app/lifespan_magic.py`
- **handle_cast_command()** (9 connections) — `server/commands/magic_commands.py`
- **handle_learn_command()** (9 connections) — `server/commands/magic_commands.py`
- **handle_spell_command()** (9 connections) — `server/commands/magic_commands.py`
- **handle_spells_command()** (9 connections) — `server/commands/magic_commands.py`
- **handle_stop_command()** (9 connections) — `server/commands/magic_commands.py`
- **FastAPI** (9 connections)
- **_initialize_spell_learning_service()** (8 connections) — `server/app/lifespan_magic.py`
- **.__init__()** (8 connections) — `server/commands/magic_commands.py`
- **.handle_cast_command()** (7 connections) — `server/commands/magic_commands.py`
- *... and 92 more nodes in this community*

## Relationships

- [TargetMatch](TargetMatch.md) (20 shared connections)
- [get_logger](get_logger.md) (19 shared connections)
- [test_magic_commands.py](test_magic_commands.py.md) (13 shared connections)
- [PlayerService](PlayerService.md) (13 shared connections)
- [SpellEffectType](SpellEffectType.md) (13 shared connections)
- [SpellLearningService](SpellLearningService.md) (12 shared connections)
- [AliasStorage](AliasStorage.md) (12 shared connections)
- [test_magic_service.py](test_magic_service.py.md) (10 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (8 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (7 shared connections)
- [test_spell_effects.py](test_spell_effects.py.md) (7 shared connections)
- [command_service.py](command_service.py.md) (6 shared connections)

## Source Files

- `server/app/lifespan_magic.py`
- `server/commands/magic_commands.py`
- `server/game/magic/magic_service.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_learning_service.py`
- `server/game/magic/spell_registry.py`
- `server/persistence/repositories/player_spell_repository.py`
- `server/persistence/repositories/spell_repository.py`
- `server/tests/unit/game/magic/test_magic_service.py`

## Audit Trail

- EXTRACTED: 328 (84%)
- INFERRED: 63 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*