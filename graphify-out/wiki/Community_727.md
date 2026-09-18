# Community 727

> 23 nodes

## Key Concepts

- **CommandService** (20 connections) — `server/commands/command_service.py`
- **._extract_parsed_fields()** (7 connections) — `server/commands/command_service.py`
- **.process_command()** (6 connections) — `server/commands/command_service.py`
- **._parse_command_string()** (5 connections) — `server/commands/command_service.py`
- **._prepare_command_data()** (5 connections) — `server/commands/command_service.py`
- **Command** (5 connections)
- **._fallback_parsed_fields()** (4 connections) — `server/commands/command_service.py`
- **._log_parsed_command_inspection()** (4 connections) — `server/commands/command_service.py`
- **._log_model_dump_result()** (3 connections) — `server/commands/command_service.py`
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
- **Process a command with full validation and routing. Args: command: The raw…** (1 connections) — `server/commands/command_service.py`
- **Get list of available commands.** (1 connections) — `server/commands/command_service.py`
- **Unregister a command handler. Args: command: Command name to unregister** (1 connections) — `server/commands/command_service.py`

## Relationships

- [Community 1267](Community_1267.md) (5 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (2 shared connections)
- [Character Creation & Auth Dependencies](Character_Creation_&_Auth_Dependencies.md) (1 shared connections)
- [Community 496](Community_496.md) (1 shared connections)
- [Community 521](Community_521.md) (1 shared connections)
- [Community 1359](Community_1359.md) (1 shared connections)
- [Community 115](Community_115.md) (1 shared connections)

## Source Files

- `server/commands/command_service.py`

## Audit Trail

- EXTRACTED: 43 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*