# Async Audit Cursor

> 29 nodes

## Key Concepts

- **processing.py** (25 connections) — `server/command_handler/processing.py`
- **process_command_with_validation()** (11 connections) — `server/command_handler/processing.py`
- **.is_security_sensitive()** (9 connections) — `server/validators/command_validator.py`
- **_run_command_service_for_validated()** (6 connections) — `server/command_handler/processing.py`
- **_dispatch_parsed_command()** (6 connections) — `server/command_handler/processing.py`
- **_log_security_sensitive_command()** (6 connections) — `server/command_handler/processing.py`
- **_handle_processing_error()** (6 connections) — `server/command_handler/processing.py`
- **CommandExecutionRequest** (5 connections)
- **_handle_validation_error()** (5 connections) — `server/command_handler/processing.py`
- **_parse_command_line_or_client_error()** (3 connections) — `server/command_handler/processing.py`
- **test_command_validator_is_security_sensitive_admin()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_is_security_sensitive_case_insensitive()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_is_security_sensitive_non_sensitive()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_is_security_sensitive_empty()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **ValidationError** (2 connections)
- **Exception** (2 connections)
- **Command Processing Logic for MythosMUD.  This module contains the core command** (1 connections) — `server/command_handler/processing.py`
- **Validate the raw command string via CommandProcessor.      Returns:         (** (1 connections) — `server/command_handler/processing.py`
- **Extract structured command data, dispatch to CommandService, audit if needed.** (1 connections) — `server/command_handler/processing.py`
- **Parse the command line; on success run CommandService (see ``_parse_command_line** (1 connections) — `server/command_handler/processing.py`
- **Validate ``command_line`` via Click/Pydantic, dispatch to handlers; result dict** (1 connections) — `server/command_handler/processing.py`
- **Log a security-sensitive command for auditing.** (1 connections) — `server/command_handler/processing.py`
- **Handle a validation error during command processing.** (1 connections) — `server/command_handler/processing.py`
- **Handle a general exception during command processing.** (1 connections) — `server/command_handler/processing.py`
- **Test CommandValidator.is_security_sensitive detects admin commands.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- *... and 4 more nodes in this community*

## Relationships

- [Admin Teleport Commands](Admin_Teleport_Commands.md) (11 shared connections)
- [Persistence Container Extended](Persistence_Container_Extended.md) (4 shared connections)
- [Client Event Store](Client_Event_Store.md) (3 shared connections)
- [Chat Panel Components](Chat_Panel_Components.md) (3 shared connections)
- [Catatonia Check Logic](Catatonia_Check_Logic.md) (3 shared connections)
- [Cursor Agents Analyzer](Cursor_Agents_Analyzer.md) (2 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (1 shared connections)
- [Chat NATS Publisher](Chat_NATS_Publisher.md) (1 shared connections)
- [Test Refactoring Deliverables](Test_Refactoring_Deliverables.md) (1 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (1 shared connections)
- [Command Parser Helpers](Command_Parser_Helpers.md) (1 shared connections)
- [Audit Logger Service](Audit_Logger_Service.md) (1 shared connections)

## Source Files

- `server/command_handler/processing.py`
- `server/tests/unit/validators/test_command_validator.py`
- `server/validators/command_validator.py`

## Audit Trail

- EXTRACTED: 107 (96%)
- INFERRED: 4 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*