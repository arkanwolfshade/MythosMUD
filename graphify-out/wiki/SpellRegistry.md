# SpellRegistry

> 84 nodes

## Key Concepts

- **SpellRegistry** (32 connections) — `server/game/magic/spell_registry.py`
- **MagicCommandHandler** (30 connections) — `server/commands/magic_commands.py`
- **magic_commands.py** (26 connections) — `server/commands/magic_commands.py`
- **Any** (19 connections)
- **test_spell_registry.py** (18 connections) — `server/tests/unit/game/magic/test_spell_registry.py`
- **spell_registry.py** (16 connections) — `server/game/magic/spell_registry.py`
- **SpellRepository** (15 connections) — `server/persistence/repositories/spell_repository.py`
- **magic_service()** (13 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **handle_cast_command()** (9 connections) — `server/commands/magic_commands.py`
- **handle_learn_command()** (9 connections) — `server/commands/magic_commands.py`
- **handle_spell_command()** (9 connections) — `server/commands/magic_commands.py`
- **handle_spells_command()** (9 connections) — `server/commands/magic_commands.py`
- **handle_stop_command()** (9 connections) — `server/commands/magic_commands.py`
- **_spell()** (9 connections) — `server/tests/unit/game/magic/test_spell_registry.py`
- **.__init__()** (8 connections) — `server/commands/magic_commands.py`
- **.handle_cast_command()** (7 connections) — `server/commands/magic_commands.py`
- **SpellCommandError** (6 connections) — `server/commands/magic_commands.py`
- **._build_cast_response()** (6 connections) — `server/commands/magic_commands.py`
- **.handle_learn_command()** (6 connections) — `server/commands/magic_commands.py`
- **.handle_spell_command()** (6 connections) — `server/commands/magic_commands.py`
- **._interrupt_rest_for_cast()** (6 connections) — `server/commands/magic_commands.py`
- **._resolve_learn_context()** (5 connections) — `server/commands/magic_commands.py`
- **._resolve_spell_context()** (5 connections) — `server/commands/magic_commands.py`
- **asyncio** (5 connections)
- **._announce_spell_cast()** (4 connections) — `server/commands/magic_commands.py`
- *... and 59 more nodes in this community*

## Relationships

- [SpellEffectType](SpellEffectType.md) (17 shared connections)
- [test_magic_commands.py](test_magic_commands.py.md) (13 shared connections)
- [AliasStorage](AliasStorage.md) (12 shared connections)
- [magic_service.py](magic_service.py.md) (11 shared connections)
- [TargetMatch](TargetMatch.md) (10 shared connections)
- [DatabaseError](DatabaseError.md) (8 shared connections)
- [SpellLearningService](SpellLearningService.md) (8 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (7 shared connections)
- [command_service.py](command_service.py.md) (6 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (5 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (4 shared connections)

## Source Files

- `server/commands/magic_commands.py`
- `server/game/magic/spell_registry.py`
- `server/persistence/repositories/spell_repository.py`
- `server/tests/unit/game/magic/test_magic_service.py`
- `server/tests/unit/game/magic/test_spell_registry.py`

## Audit Trail

- EXTRACTED: 216 (84%)
- INFERRED: 40 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*