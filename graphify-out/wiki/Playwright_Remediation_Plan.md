# Playwright Remediation Plan

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

- [Character Creation API](Character_Creation_API.md) (4 shared connections)
- [NPC Definition Admin API](NPC_Definition_Admin_API.md) (3 shared connections)
- [Player Respawn Handlers](Player_Respawn_Handlers.md) (2 shared connections)
- [NPC Death Lifecycle](NPC_Death_Lifecycle.md) (2 shared connections)
- [Environmental Container Scenario](Environmental_Container_Scenario.md) (2 shared connections)
- [Container Open Events](Container_Open_Events.md) (1 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (1 shared connections)

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