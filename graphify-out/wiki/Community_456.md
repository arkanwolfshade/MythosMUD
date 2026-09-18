# Community 456

> 39 nodes

## Key Concepts

- **CommandParser** (19 connections) — `server/utils/command_parser.py`
- **CommandProcessor** (15 connections) — `server/utils/command_processor.py`
- **._create_command_object()** (6 connections) — `server/utils/command_parser.py`
- **.parse_command()** (6 connections) — `server/utils/command_parser.py`
- **.extract_command_data()** (5 connections) — `server/utils/command_processor.py`
- **command_parser()** (4 connections) — `server/tests/unit/utils/test_command_parser.py`
- **._invoke_create_method()** (4 connections) — `server/utils/command_parser.py`
- **._extract_attributes()** (4 connections) — `server/utils/command_processor.py`
- **._is_combat_command()** (4 connections) — `server/utils/command_processor.py`
- **.process_command_string()** (4 connections) — `server/utils/command_processor.py`
- **Command** (4 connections)
- **test_process_command_string_pydantic_validation_error()** (3 connections) — `server/tests/unit/utils/test_command_processor.py`
- **._normalize_command()** (3 connections) — `server/utils/command_parser.py`
- **._parse_command_parts()** (3 connections) — `server/utils/command_parser.py`
- **._resolve_command_alias()** (3 connections) — `server/utils/command_parser.py`
- **.__init__()** (3 connections) — `server/utils/command_processor.py`
- **Any** (3 connections)
- **.get_command_help()** (2 connections) — `server/utils/command_parser.py`
- **.get_command_help()** (2 connections) — `server/utils/command_processor.py`
- **.validate_command_safety()** (2 connections) — `server/utils/command_processor.py`
- **fixture** (1 connections)
- **Create a CommandParser instance.** (1 connections) — `server/tests/unit/utils/test_command_parser.py`
- **Test process_command_string handles Pydantic validation errors.** (1 connections) — `server/tests/unit/utils/test_command_processor.py`
- **Secure command parser using Click for parsing and Pydantic for validation.…** (1 connections) — `server/utils/command_parser.py`
- **Parse and validate a command string. Args: command_string: Raw command string…** (1 connections) — `server/utils/command_parser.py`
- *... and 14 more nodes in this community*

## Relationships

- [Community 115](Community_115.md) (5 shared connections)
- [Community 251](Community_251.md) (5 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (3 shared connections)
- [Community 457](Community_457.md) (2 shared connections)
- [Community 39](Community_39.md) (2 shared connections)
- [Community 316](Community_316.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_parser.py`
- `server/tests/unit/utils/test_command_processor.py`
- `server/utils/command_parser.py`
- `server/utils/command_processor.py`

## Audit Trail

- EXTRACTED: 62 (91%)
- INFERRED: 6 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*