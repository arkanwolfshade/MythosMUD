# combat services initialization

> 30 nodes

## Key Concepts

- **CommandService** (20 connections) — `server/commands/command_service.py`
- **._extract_parsed_fields()** (7 connections) — `server/commands/command_service.py`
- **.process_command()** (6 connections) — `server/commands/command_service.py`
- **._parse_command_string()** (5 connections) — `server/commands/command_service.py`
- **Command** (5 connections)
- **._prepare_command_data()** (5 connections) — `server/commands/command_service.py`
- **._execute_command_handler()** (5 connections) — `server/commands/command_service.py`
- **.process_validated_command()** (4 connections) — `server/commands/command_service.py`
- **._fallback_parsed_fields()** (4 connections) — `server/commands/command_service.py`
- **._log_parsed_command_inspection()** (4 connections) — `server/commands/command_service.py`
- **._log_model_dump_result()** (3 connections) — `server/commands/command_service.py`
- **.register_command_handler()** (3 connections) — `server/commands/command_service.py`
- **.__init__()** (2 connections) — `server/commands/command_service.py`
- **CommandHandler** (2 connections)
- **.get_available_commands()** (2 connections) — `server/commands/command_service.py`
- **.unregister_command_handler()** (2 connections) — `server/commands/command_service.py`
- **Main command processing service for MythosMUD.      This service handles command** (1 connections) — `server/commands/command_service.py`
- **Initialize the command service.** (1 connections) — `server/commands/command_service.py`
- **Process a validated command with routing.          Args:             command_dat** (1 connections) — `server/commands/command_service.py`
- **Parse and validate command string.          Returns:             tuple of (parse** (1 connections) — `server/commands/command_service.py`
- **Prepare command_data dictionary by merging parsed command fields.          Retur** (1 connections) — `server/commands/command_service.py`
- **Extract non-private, non-callable attributes from parsed_command, excluding keys** (1 connections) — `server/commands/command_service.py`
- **Extract fields from parsed_command using model_dump or fallback method.** (1 connections) — `server/commands/command_service.py`
- **Log parsed command object inspection details.** (1 connections) — `server/commands/command_service.py`
- **Log model_dump result details.** (1 connections) — `server/commands/command_service.py`
- *... and 5 more nodes in this community*

## Relationships

- [commands party examples](commands_party_examples.md) (3 shared connections)
- [health service services](health_service_services.md) (2 shared connections)
- [Loot Generation](Loot_Generation.md) (1 shared connections)
- [command commands handler](command_commands_handler.md) (1 shared connections)
- [commands alias rationale](commands_alias_rationale.md) (1 shared connections)
- [commands admin mute](commands_admin_mute.md) (1 shared connections)
- [Security Validator Tests](Security_Validator_Tests.md) (1 shared connections)
- [command parser rationale](command_parser_rationale.md) (1 shared connections)

## Source Files

- `server/commands/command_service.py`

## Audit Trail

- EXTRACTED: 93 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*