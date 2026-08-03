# player effects endpoints

> 15 nodes

## Key Concepts

- **CommandParser** (19 connections) — `server/utils/command_parser.py`
- **.parse_command()** (7 connections) — `server/utils/command_parser.py`
- **._create_command_object()** (7 connections) — `server/utils/command_parser.py`
- **Command** (4 connections)
- **._parse_command_parts()** (4 connections) — `server/utils/command_parser.py`
- **._invoke_create_method()** (4 connections) — `server/utils/command_parser.py`
- **._normalize_command()** (3 connections) — `server/utils/command_parser.py`
- **._resolve_command_alias()** (3 connections) — `server/utils/command_parser.py`
- **Secure command parser using Click for parsing and Pydantic for validation.** (1 connections) — `server/utils/command_parser.py`
- **Parse and validate a command string.          Args:             command_string:** (1 connections) — `server/utils/command_parser.py`
- **Normalize command string by removing slash prefix and cleaning whitespace.** (1 connections) — `server/utils/command_parser.py`
- **Parse command string into command and arguments.          Args:             comm** (1 connections) — `server/utils/command_parser.py`
- **Resolve single-letter aliases to full command names.** (1 connections) — `server/utils/command_parser.py`
- **Invoke the appropriate factory method for the command.** (1 connections) — `server/utils/command_parser.py`
- **Create and validate a Command; raise MythosValidationError on failure.** (1 connections) — `server/utils/command_parser.py`

## Relationships

- [command inventory factories](command_inventory_factories.md) (4 shared connections)
- [command factories create](command_factories_create.md) (3 shared connections)
- [command parser rationale](command_parser_rationale.md) (2 shared connections)
- [npc behavior engine](npc_behavior_engine.md) (2 shared connections)
- [skill game service](skill_game_service.md) (1 shared connections)
- [infrastructure persistence room](infrastructure_persistence_room.md) (1 shared connections)
- [command parser helpers](command_parser_helpers.md) (1 shared connections)
- [infrastructure persistence core](infrastructure_persistence_core.md) (1 shared connections)
- [command processor rationale](command_processor_rationale.md) (1 shared connections)

## Source Files

- `server/utils/command_parser.py`

## Audit Trail

- EXTRACTED: 56 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*