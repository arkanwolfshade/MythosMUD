# event events serialization

> 16 nodes

## Key Concepts

- **.create_cast_command()** (12 connections) — `server/utils/command_factories_utility.py`
- **test_create_cast_command_no_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_cast_command()** (3 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_cast_command_heal_self()** (3 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_cast_command_heal_me()** (3 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_cast_command_multi_word()** (3 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_cast_command_with_target()** (3 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_cast_command_heal_other_with_target()** (3 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **Test create_cast_command() with 'heal' and no target invokes heal_self.** (1 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **Test /cast heal self -> heal_self, no target.** (1 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **Test /cast heal me -> heal_self, no target.** (1 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **Test create_cast_command() raises error with no args.** (1 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **Test create_cast_command() with two args: first=spell, rest=target.** (1 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **Test /cast heal <target> (target not self/me) -> heal_other with target.** (1 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **Test /cast heal other <target> -> heal_other with target.** (1 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **Create CastCommand from arguments.** (1 connections) — `server/utils/command_factories_utility.py`

## Relationships

- [exceptions rationale error](exceptions_rationale_error.md) (7 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [auth dependencies rationale](auth_dependencies_rationale.md) (2 shared connections)
- [Spell Validation](Spell_Validation.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_factories_utility.py`
- `server/utils/command_factories_utility.py`

## Audit Trail

- EXTRACTED: 41 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*