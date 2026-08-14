# CommandParser

> 22 nodes

## Key Concepts

- **CommandParser** (19 connections) — `server/utils/command_parser.py`
- **._create_command_object()** (7 connections) — `server/utils/command_parser.py`
- **.parse_command()** (7 connections) — `server/utils/command_parser.py`
- **command_parser()** (4 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **._invoke_create_method()** (4 connections) — `server/utils/command_parser.py`
- **._parse_command_parts()** (4 connections) — `server/utils/command_parser.py`
- **Command** (4 connections)
- **test_create_command_object_pydantic_validation_error()** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- **._normalize_command()** (3 connections) — `server/utils/command_parser.py`
- **._resolve_command_alias()** (3 connections) — `server/utils/command_parser.py`
- **.get_command_help()** (2 connections) — `server/utils/command_parser.py`
- **fixture** (1 connections)
- **Create a CommandParser instance.** (1 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **Test _create_command_object handles Pydantic validation errors.** (1 connections) — `server/tests/unit/utils/test_command_parser.py`
- **Secure command parser using Click for parsing and Pydantic for validation.…** (1 connections) — `server/utils/command_parser.py`
- **Parse and validate a command string. Args: command_string: Raw command string…** (1 connections) — `server/utils/command_parser.py`
- **Normalize command string by removing slash prefix and cleaning whitespace.…** (1 connections) — `server/utils/command_parser.py`
- **Parse command string into command and arguments. Args: command_string:…** (1 connections) — `server/utils/command_parser.py`
- **Resolve single-letter aliases to full command names.** (1 connections) — `server/utils/command_parser.py`
- **Invoke the appropriate factory method for the command.** (1 connections) — `server/utils/command_parser.py`
- **Create and validate a Command; raise MythosValidationError on failure.** (1 connections) — `server/utils/command_parser.py`
- **Get help information for commands. Args: command_name: Specific command to get…** (1 connections) — `server/utils/command_parser.py`

## Relationships

- [get_logger](get_logger.md) (5 shared connections)
- [CommandProcessor](CommandProcessor.md) (2 shared connections)
- [test_command_parser.py](test_command_parser.py.md) (2 shared connections)
- [test_command_parser_helpers.py](test_command_parser_helpers.py.md) (2 shared connections)
- [BaseCommand](BaseCommand.md) (2 shared connections)
- [command_parser](command_parser.md) (1 shared connections)
- [parse_command](parse_command.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_parser.py`
- `server/tests/unit/utils/test_command_parser_helpers.py`
- `server/utils/command_parser.py`

## Audit Trail

- EXTRACTED: 41 (95%)
- INFERRED: 2 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*