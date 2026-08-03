# countdown rest task

> 6 nodes

## Key Concepts

- **.create_npc_command()** (5 connections) — `server/utils/command_factories_utility.py`
- **test_create_npc_command_no_args()** (3 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_npc_command_with_subcommand()** (3 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **Test create_npc_command() with no args.** (1 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **Test create_npc_command() with subcommand.** (1 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **Create NPCCommand from arguments.** (1 connections) — `server/utils/command_factories_utility.py`

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