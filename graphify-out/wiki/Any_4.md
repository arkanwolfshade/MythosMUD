# Any

> 20 nodes

## Key Concepts

- **Any** (10 connections)
- **._extract_parsed_fields()** (7 connections) — `server/commands/command_service.py`
- **.process_command()** (7 connections) — `server/commands/command_service.py`
- **._execute_command_handler()** (6 connections) — `server/commands/command_service.py`
- **._parse_command_string()** (5 connections) — `server/commands/command_service.py`
- **._prepare_command_data()** (5 connections) — `server/commands/command_service.py`
- **._fallback_parsed_fields()** (4 connections) — `server/commands/command_service.py`
- **._log_model_dump_result()** (4 connections) — `server/commands/command_service.py`
- **._log_parsed_command_inspection()** (4 connections) — `server/commands/command_service.py`
- **.register_command_handler()** (3 connections) — `server/commands/command_service.py`
- **CommandHandler** (1 connections)
- **Parse and validate command string. Returns: tuple of (parsed_command, cmd,…** (1 connections) — `server/commands/command_service.py`
- **Prepare command_data dictionary by merging parsed command fields. Returns:…** (1 connections) — `server/commands/command_service.py`
- **Extract non-private, non-callable attributes from parsed_command, excluding…** (1 connections) — `server/commands/command_service.py`
- **Extract fields from parsed_command using model_dump or fallback method.…** (1 connections) — `server/commands/command_service.py`
- **Log parsed command object inspection details.** (1 connections) — `server/commands/command_service.py`
- **Log model_dump result details.** (1 connections) — `server/commands/command_service.py`
- **Execute command handler with error handling. Returns: dict: Command result** (1 connections) — `server/commands/command_service.py`
- **Process a command with full validation and routing. Args: command: The raw…** (1 connections) — `server/commands/command_service.py`
- **Register a new command handler. Args: command: Command name handler: Handler…** (1 connections) — `server/commands/command_service.py`

## Relationships

- [AliasStorage](AliasStorage.md) (12 shared connections)
- [test_command_parser.py](test_command_parser.py.md) (1 shared connections)

## Source Files

- `server/commands/command_service.py`

## Audit Trail

- EXTRACTED: 39 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*