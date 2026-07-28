# Server Utils (21)

> 23 nodes

## Key Concepts

- **CommandParser** (19 connections) — `server/utils/command_parser.py`
- **.parse_command()** (7 connections) — `server/utils/command_parser.py`
- **._create_command_object()** (7 connections) — `server/utils/command_parser.py`
- **Command** (4 connections)
- **._parse_command_parts()** (4 connections) — `server/utils/command_parser.py`
- **._invoke_create_method()** (4 connections) — `server/utils/command_parser.py`
- **command_parser()** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_create_command_object_pydantic_validation_error()** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- **command_parser()** (3 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **._normalize_command()** (3 connections) — `server/utils/command_parser.py`
- **._resolve_command_alias()** (3 connections) — `server/utils/command_parser.py`
- **.get_command_help()** (2 connections) — `server/utils/command_parser.py`
- **Create a CommandParser instance.** (1 connections) — `server/tests/unit/utils/test_command_parser.py`
- **Test _create_command_object handles Pydantic validation errors.** (1 connections) — `server/tests/unit/utils/test_command_parser.py`
- **Create a CommandParser instance.** (1 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **Secure command parser using Click for parsing and Pydantic for validation.** (1 connections) — `server/utils/command_parser.py`
- **Parse and validate a command string.          Args:             command_string:** (1 connections) — `server/utils/command_parser.py`
- **Normalize command string by removing slash prefix and cleaning whitespace.** (1 connections) — `server/utils/command_parser.py`
- **Parse command string into command and arguments.          Args:             comm** (1 connections) — `server/utils/command_parser.py`
- **Resolve single-letter aliases to full command names.** (1 connections) — `server/utils/command_parser.py`
- **Invoke the appropriate factory method for the command.** (1 connections) — `server/utils/command_parser.py`
- **Create and validate command object based on command type.          Args:** (1 connections) — `server/utils/command_parser.py`
- **Get help information for commands.          Args:             command_name: Spec** (1 connections) — `server/utils/command_parser.py`

## Relationships

- [Server Utils (7)](Server_Utils_%287%29.md) (3 shared connections)
- [Server Commands](Server_Commands.md) (3 shared connections)
- [Server Game](Server_Game.md) (3 shared connections)
- [Server Utils (16)](Server_Utils_%2816%29.md) (2 shared connections)
- [Server Utils (2)](Server_Utils_%282%29.md) (2 shared connections)
- [Server Utils (22)](Server_Utils_%2822%29.md) (2 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_parser.py`
- `server/tests/unit/utils/test_command_parser_helpers.py`
- `server/utils/command_parser.py`

## Audit Trail

- EXTRACTED: 71 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*