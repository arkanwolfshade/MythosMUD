# message realtime messaging

> 6 nodes

## Key Concepts

- **.create_goto_command()** (6 connections) — `server/utils/command_factories_utility.py`
- **test_create_goto_command_no_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_goto_command()** (3 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **Test create_goto_command() creates GotoCommand.** (1 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **Test create_goto_command() raises error with no args.** (1 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **Create GotoCommand from arguments.** (1 connections) — `server/utils/command_factories_utility.py`

## Relationships

- [exceptions rationale error](exceptions_rationale_error.md) (2 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [command models admin](command_models_admin.md) (1 shared connections)
- [auth dependencies rationale](auth_dependencies_rationale.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_factories_utility.py`
- `server/utils/command_factories_utility.py`

## Audit Trail

- EXTRACTED: 15 (94%)
- INFERRED: 1 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*