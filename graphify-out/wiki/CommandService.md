# CommandService

> 30 nodes

## Key Concepts

- **CommandService** (20 connections) — `server/commands/command_service.py`
- **._extract_parsed_fields()** (7 connections) — `server/commands/command_service.py`
- **.process_command()** (6 connections) — `server/commands/command_service.py`
- **._execute_command_handler()** (5 connections) — `server/commands/command_service.py`
- **._parse_command_string()** (5 connections) — `server/commands/command_service.py`
- **._prepare_command_data()** (5 connections) — `server/commands/command_service.py`
- **Command** (5 connections)
- **._fallback_parsed_fields()** (4 connections) — `server/commands/command_service.py`
- **._log_parsed_command_inspection()** (4 connections) — `server/commands/command_service.py`
- **.process_validated_command()** (4 connections) — `server/commands/command_service.py`
- **._log_model_dump_result()** (3 connections) — `server/commands/command_service.py`
- **.register_command_handler()** (3 connections) — `server/commands/command_service.py`
- **.get_available_commands()** (2 connections) — `server/commands/command_service.py`
- **.__init__()** (2 connections) — `server/commands/command_service.py`
- **.unregister_command_handler()** (2 connections) — `server/commands/command_service.py`
- **CommandHandler** (2 connections)
- **Main command processing service for MythosMUD. This service handles command…** (1 connections) — `server/commands/command_service.py`
- **Initialize the command service.** (1 connections) — `server/commands/command_service.py`
- **Process a validated command with routing. Args: command_data: The validated…** (1 connections) — `server/commands/command_service.py`
- **Parse and validate command string. Returns: tuple of (parsed_command, cmd,…** (1 connections) — `server/commands/command_service.py`
- **Prepare command_data dictionary by merging parsed command fields. Returns:…** (1 connections) — `server/commands/command_service.py`
- **Extract non-private, non-callable attributes from parsed_command, excluding…** (1 connections) — `server/commands/command_service.py`
- **Extract fields from parsed_command using model_dump or fallback method.…** (1 connections) — `server/commands/command_service.py`
- **Log parsed command object inspection details.** (1 connections) — `server/commands/command_service.py`
- **Log model_dump result details.** (1 connections) — `server/commands/command_service.py`
- *... and 5 more nodes in this community*

## Relationships

- [AliasStorage](AliasStorage.md) (3 shared connections)
- [test_command_service.py](test_command_service.py.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [command_handler_unified.py](command_handler_unified.py.md) (1 shared connections)
- [server/commands/__init__.py](server-commands-__init__.py.md) (1 shared connections)
- [command_service.py](command_service.py.md) (1 shared connections)
- [ValidationError](ValidationError.md) (1 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (1 shared connections)

## Source Files

- `server/commands/command_service.py`

## Audit Trail

- EXTRACTED: 51 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*