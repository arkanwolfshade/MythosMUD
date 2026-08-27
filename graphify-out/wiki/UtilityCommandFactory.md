# UtilityCommandFactory

> 16 nodes

## Key Concepts

- **UtilityCommandFactory** (65 connections) — `server/utils/command_factories_utility.py`
- **.create_spell_command()** (7 connections) — `server/utils/command_factories_utility.py`
- **test_create_spell_command_no_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_teleport_command_invalid_direction()** (5 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_teleport_command_no_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_spell_command()** (4 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_spell_command_multi_word()** (4 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_teleport_command_with_direction()** (4 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **Test create_teleport_command() raises error with no args.** (1 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **Test create_teleport_command() with direction.** (1 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **Test create_teleport_command() raises error with invalid direction.** (1 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **Test create_spell_command() creates SpellCommand.** (1 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **Test create_spell_command() raises error with no args.** (1 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **Test create_spell_command() with multi-word spell name.** (1 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **Create SpellCommand from arguments.** (1 connections) — `server/utils/command_factories_utility.py`
- **Factory class for creating utility command objects.** (1 connections) — `server/utils/command_factories_utility.py`

## Relationships

- [test_command_factories_utility.py](test_command_factories_utility.py.md) (18 shared connections)
- [.create_cast_command](create_cast_command.md) (9 shared connections)
- [ValidationError](ValidationError.md) (6 shared connections)
- [BaseCommand](BaseCommand.md) (5 shared connections)
- [.create_learn_command](create_learn_command.md) (4 shared connections)
- [.create_alias_command](create_alias_command.md) (4 shared connections)
- [.create_unalias_command](create_unalias_command.md) (4 shared connections)
- [.create_goto_command](create_goto_command.md) (3 shared connections)
- [.create_shutdown_command](create_shutdown_command.md) (3 shared connections)
- [.create_spells_command](create_spells_command.md) (3 shared connections)
- [.create_aliases_command](create_aliases_command.md) (3 shared connections)
- [.create_help_command](create_help_command.md) (3 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_factories_utility.py`
- `server/utils/command_factories_utility.py`

## Audit Trail

- EXTRACTED: 40 (45%)
- INFERRED: 49 (55%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*