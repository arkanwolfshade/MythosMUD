# services service hallucination

> 8 nodes

## Key Concepts

- **.create_learn_command()** (7 connections) — `server/utils/command_factories_utility.py`
- **test_create_learn_command_no_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_learn_command()** (3 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_learn_command_multi_word()** (3 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **Test create_learn_command() creates LearnCommand.** (1 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **Test create_learn_command() raises error with no args.** (1 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **Test create_learn_command() with multi-word spell name.** (1 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **Create LearnCommand from arguments.** (1 connections) — `server/utils/command_factories_utility.py`

## Relationships

- [exceptions rationale error](exceptions_rationale_error.md) (3 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [Spell Validation](Spell_Validation.md) (1 shared connections)
- [auth dependencies rationale](auth_dependencies_rationale.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_factories_utility.py`
- `server/utils/command_factories_utility.py`

## Audit Trail

- EXTRACTED: 20 (95%)
- INFERRED: 1 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*