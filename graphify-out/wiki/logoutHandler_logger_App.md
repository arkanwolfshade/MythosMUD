# logoutHandler logger App

> 30 nodes

## Key Concepts

- **test_command_processing.py** (15 connections) — `server/tests/unit/commands/test_command_processing.py`
- **process_command_with_validation()** (13 connections) — `server/command_handler/processing.py`
- **_dispatch_parsed_command()** (8 connections) — `server/command_handler/processing.py`
- **_run_command_service_for_validated()** (7 connections) — `server/command_handler/processing.py`
- **_log_security_sensitive_command()** (7 connections) — `server/command_handler/processing.py`
- **_handle_processing_error()** (7 connections) — `server/command_handler/processing.py`
- **_parse_command_line_or_client_error()** (6 connections) — `server/command_handler/processing.py`
- **_handle_validation_error()** (6 connections) — `server/command_handler/processing.py`
- **CommandExecutionRequest** (5 connections)
- **test_handle_validation_error_security_sensitive()** (3 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_process_command_with_validation_validation_error()** (3 connections) — `server/tests/unit/commands/test_command_processing.py`
- **ValidationError** (2 connections)
- **Exception** (2 connections)
- **test_parse_command_line_or_client_error_with_message()** (2 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_parse_command_line_or_client_error_no_validated()** (2 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_parse_command_line_or_client_error_success()** (2 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_dispatch_parsed_command_client_error()** (2 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_dispatch_parsed_command_success()** (2 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_run_command_service_security_sensitive_audit()** (2 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_log_security_sensitive_command_no_session()** (2 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_handle_processing_error()** (2 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_process_command_with_validation_generic_error()** (2 connections) — `server/tests/unit/commands/test_command_processing.py`
- **Validate the raw command string via CommandProcessor.      Returns:         (** (1 connections) — `server/command_handler/processing.py`
- **Extract structured command data, dispatch to CommandService, audit if needed.** (1 connections) — `server/command_handler/processing.py`
- **Parse the command line; on success run CommandService (see ``_parse_command_line** (1 connections) — `server/command_handler/processing.py`
- *... and 5 more nodes in this community*

## Relationships

- [Loot Generation](Loot_Generation.md) (12 shared connections)
- [command validator validators](command_validator_validators.md) (4 shared connections)
- [command validation commands](command_validation_commands.md) (3 shared connections)
- [fixtures mock helpers](fixtures_mock_helpers.md) (2 shared connections)
- [command commands handler](command_commands_handler.md) (2 shared connections)
- [commands recovery lucidity](commands_recovery_lucidity.md) (1 shared connections)
- [commands emote rationale](commands_emote_rationale.md) (1 shared connections)
- [Security Validator Tests](Security_Validator_Tests.md) (1 shared connections)

## Source Files

- `server/command_handler/processing.py`
- `server/tests/unit/commands/test_command_processing.py`

## Audit Trail

- EXTRACTED: 106 (96%)
- INFERRED: 4 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*