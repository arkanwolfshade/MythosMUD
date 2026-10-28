# Dream Messaging Subsystem Design

> 28 nodes · cohesion 0.10

## Key Concepts

- **CommandService** (20 connections) — `server/commands/command_service.py`
- **._extract_parsed_fields()** (7 connections) — `server/commands/command_service.py`
- **.process_command()** (7 connections) — `server/commands/command_service.py`
- **._execute_command_handler()** (6 connections) — `server/commands/command_service.py`
- **._parse_command_string()** (6 connections) — `server/commands/command_service.py`
- **._prepare_command_data()** (5 connections) — `server/commands/command_service.py`
- **Command** (5 connections)
- **._fallback_parsed_fields()** (4 connections) — `server/commands/command_service.py`
- **._log_parsed_command_inspection()** (4 connections) — `server/commands/command_service.py`
- **._log_model_dump_result()** (3 connections) — `server/commands/command_service.py`
- **.register_command_handler()** (3 connections) — `server/commands/command_service.py`
- **CommandHandler** (2 connections)
- **.get_available_commands()** (2 connections) — `server/commands/command_service.py`
- **.__init__()** (2 connections) — `server/commands/command_service.py`
- **.unregister_command_handler()** (2 connections) — `server/commands/command_service.py`
- **Main command processing service for MythosMUD. This service handles command…** (1 connections) — `server/commands/command_service.py`
- **Initialize the command service.** (1 connections) — `server/commands/command_service.py`
- **Parse and validate command string. Returns: tuple of (parsed_command, cmd,…** (1 connections) — `server/commands/command_service.py`
- **Prepare command_data dictionary by merging parsed command fields. Returns:…** (1 connections) — `server/commands/command_service.py`
- **Extract non-private, non-callable attributes from parsed_command, excluding…** (1 connections) — `server/commands/command_service.py`
- **Extract fields from parsed_command using model_dump or fallback method.…** (1 connections) — `server/commands/command_service.py`
- **Log parsed command object inspection details.** (1 connections) — `server/commands/command_service.py`
- **Log model_dump result details.** (1 connections) — `server/commands/command_service.py`
- **Execute command handler with error handling. Returns: dict: Command result** (1 connections) — `server/commands/command_service.py`
- **Process a command with full validation and routing. Args: command: The raw…** (1 connections) — `server/commands/command_service.py`
- *... and 3 more nodes in this community*

## Relationships

- [command_parser.py](command_parser.py.md) (8 shared connections)
- [test_combat_handler.py](test_combat_handler.py.md) (2 shared connections)
- [ChatChannelLoggerMixin](ChatChannelLoggerMixin.md) (1 shared connections)
- [QuestService](QuestService.md) (1 shared connections)
- [CommandFactory](CommandFactory.md) (1 shared connections)

## Source Files

- `server/commands/command_service.py`

## Audit Trail

- EXTRACTED: 51 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*