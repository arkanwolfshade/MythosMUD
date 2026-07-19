# Command Parser

> 19 nodes · cohesion 0.15

## Key Concepts

- **CommandParser** (20 connections) — `server/utils/command_parser.py`
- **._create_command_object()** (7 connections) — `server/utils/command_parser.py`
- **.parse_command()** (7 connections) — `server/utils/command_parser.py`
- **Command** (5 connections) — `server/utils/command_parser.py`
- **._invoke_create_method()** (4 connections) — `server/utils/command_parser.py`
- **._parse_command_parts()** (4 connections) — `server/utils/command_parser.py`
- **._normalize_command()** (3 connections) — `server/utils/command_parser.py`
- **._resolve_command_alias()** (3 connections) — `server/utils/command_parser.py`
- **command_parser()** (3 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`
- **.get_command_help()** (2 connections) — `server/utils/command_parser.py`
- **Secure command parser using Click for parsing and Pydantic for validation.** (1 connections) — `server/utils/command_parser.py`
- **Parse and validate a command string.          Args:             command_string:** (1 connections) — `server/utils/command_parser.py`
- **Normalize command string by removing slash prefix and cleaning whitespace.** (1 connections) — `server/utils/command_parser.py`
- **Parse command string into command and arguments.          Args:             comm** (1 connections) — `server/utils/command_parser.py`
- **Resolve single-letter aliases to full command names.** (1 connections) — `server/utils/command_parser.py`
- **Invoke the appropriate factory method for the command.** (1 connections) — `server/utils/command_parser.py`
- **Create and validate command object based on command type.          Args:** (1 connections) — `server/utils/command_parser.py`
- **Get help information for commands.          Args:             command_name: Spec** (1 connections) — `server/utils/command_parser.py`
- **Create a CommandParser instance.** (1 connections) — `server/tests/unit/utils/test_command_parser_helpers.py`

## Relationships

- [[Command Processor]] (4 shared connections)
- [[Alias Expansion Logic]] (3 shared connections)
- [[NPC Admin API]] (3 shared connections)
- [[Command Factory Creators]] (2 shared connections)
- [[Command Parser]] (2 shared connections)
- [[Command Parser Helpers]] (2 shared connections)
- [[Command Parser Tests]] (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_parser_helpers.py`
- `server/utils/command_parser.py`

## Audit Trail

- EXTRACTED: 61 (91%)
- INFERRED: 6 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
