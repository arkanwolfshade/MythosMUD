# health monitor realtime

> 6 nodes

## Key Concepts

- **.create_shutdown_command()** (5 connections) — `server/utils/command_factories_utility.py`
- **test_create_shutdown_command()** (3 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_shutdown_command_with_args()** (3 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **Test create_shutdown_command() creates ShutdownCommand.** (1 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **Test create_shutdown_command() with args.** (1 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **Create ShutdownCommand from arguments.          Args can be:         - Empty: De** (1 connections) — `server/utils/command_factories_utility.py`

## Relationships

- [exceptions rationale error](exceptions_rationale_error.md) (2 shared connections)
- [command models admin](command_models_admin.md) (1 shared connections)
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