# time service rationale

> 6 nodes

## Key Concepts

- **.create_help_command()** (5 connections) — `server/utils/command_factories_utility.py`
- **test_create_help_command()** (3 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_help_command_no_args()** (3 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **Test create_help_command() creates HelpCommand.** (1 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **Test create_help_command() creates HelpCommand with no topic.** (1 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **Create HelpCommand from arguments.** (1 connections) — `server/utils/command_factories_utility.py`

## Relationships

- [exceptions rationale error](exceptions_rationale_error.md) (2 shared connections)
- [command utility models](command_utility_models.md) (1 shared connections)
- [auth dependencies rationale](auth_dependencies_rationale.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_factories_utility.py`
- `server/utils/command_factories_utility.py`

## Audit Trail

- EXTRACTED: 14 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*