# .create_cast_command

> 18 nodes

## Key Concepts

- **.create_cast_command()** (12 connections) — `server/utils/command_factories_utility.py`
- **test_create_cast_command_no_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_cast_command()** (4 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_cast_command_heal_me()** (4 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_cast_command_heal_other_with_target()** (4 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_cast_command_heal_self()** (4 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_cast_command_multi_word()** (4 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_cast_command_with_target()** (4 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **._resolve_heal_cast()** (4 connections) — `server/utils/command_factories_utility.py`
- **Test create_cast_command() with 'heal' and no target invokes heal_self.** (1 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **Test /cast heal self -> heal_self, no target.** (1 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **Test /cast heal me -> heal_self, no target.** (1 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **Test create_cast_command() raises error with no args.** (1 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **Test create_cast_command() with two args: first=spell, rest=target.** (1 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **Test /cast heal <target> (target not self/me) -> heal_other with target.** (1 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **Test /cast heal other <target> -> heal_other with target.** (1 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **Resolve 'heal' command variations to (spell_name, target). Returns None if not…** (1 connections) — `server/utils/command_factories_utility.py`
- **Create CastCommand from arguments.** (1 connections) — `server/utils/command_factories_utility.py`

## Relationships

- [UtilityCommandFactory](UtilityCommandFactory.md) (9 shared connections)
- [test_command_factories_utility.py](test_command_factories_utility.py.md) (7 shared connections)
- [ValidationError](ValidationError.md) (2 shared connections)
- [BaseCommand](BaseCommand.md) (2 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_factories_utility.py`
- `server/utils/command_factories_utility.py`

## Audit Trail

- EXTRACTED: 29 (78%)
- INFERRED: 8 (22%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*