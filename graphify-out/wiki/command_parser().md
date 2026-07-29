# command parser()

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

- [test command parser](test_command_parser.md) (4 shared connections)
- [main()](main%28%29.md) (4 shared connections)
- [test command parser helpers](test_command_parser_helpers.md) (2 shared connections)
- [BaseCommand](BaseCommand.md) (2 shared connections)
- [command processor()](command_processor%28%29.md) (2 shared connections)
- [Any](Any.md) (1 shared connections)

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