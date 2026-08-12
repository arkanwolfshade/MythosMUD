# CommandService

> 38 nodes

## Key Concepts

- **CommandService** (20 connections) — `server/commands/command_service.py`
- **strip_ansi_codes()** (13 connections) — `server/validators/security_validator.py`
- **Any** (10 connections)
- **._extract_parsed_fields()** (7 connections) — `server/commands/command_service.py`
- **.process_command()** (7 connections) — `server/commands/command_service.py`
- **._execute_command_handler()** (6 connections) — `server/commands/command_service.py`
- **._parse_command_string()** (5 connections) — `server/commands/command_service.py`
- **._prepare_command_data()** (5 connections) — `server/commands/command_service.py`
- **.process_validated_command()** (5 connections) — `server/commands/command_service.py`
- **._fallback_parsed_fields()** (4 connections) — `server/commands/command_service.py`
- **._log_model_dump_result()** (4 connections) — `server/commands/command_service.py`
- **._log_parsed_command_inspection()** (4 connections) — `server/commands/command_service.py`
- **.register_command_handler()** (3 connections) — `server/commands/command_service.py`
- **test_strip_ansi_codes_color_codes()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_strip_ansi_codes_cursor_movement()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_strip_ansi_codes_empty()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_strip_ansi_codes_no_ansi()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **.get_available_commands()** (2 connections) — `server/commands/command_service.py`
- **.unregister_command_handler()** (2 connections) — `server/commands/command_service.py`
- **CommandHandler** (1 connections)
- **Main command processing service for MythosMUD. This service handles command…** (1 connections) — `server/commands/command_service.py`
- **Process a validated command with routing. Args: command_data: The validated…** (1 connections) — `server/commands/command_service.py`
- **Parse and validate command string. Returns: tuple of (parsed_command, cmd,…** (1 connections) — `server/commands/command_service.py`
- **Prepare command_data dictionary by merging parsed command fields. Returns:…** (1 connections) — `server/commands/command_service.py`
- **Extract non-private, non-callable attributes from parsed_command, excluding…** (1 connections) — `server/commands/command_service.py`
- *... and 13 more nodes in this community*

## Relationships

- [AliasStorage](AliasStorage.md) (6 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (6 shared connections)
- [processing.py](processing.py.md) (3 shared connections)
- [test_command_service.py](test_command_service.py.md) (2 shared connections)
- [command_handler_unified.py](command_handler_unified.py.md) (1 shared connections)
- [test_alias_commands.py](test_alias_commands.py.md) (1 shared connections)
- [BaseCommand](BaseCommand.md) (1 shared connections)
- [test_command_validator.py](test_command_validator.py.md) (1 shared connections)
- [command.py](command.py.md) (1 shared connections)

## Source Files

- `server/commands/command_service.py`
- `server/tests/unit/validators/test_security_validator.py`
- `server/validators/security_validator.py`

## Audit Trail

- EXTRACTED: 128 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*