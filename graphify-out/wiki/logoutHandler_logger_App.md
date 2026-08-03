# logoutHandler logger App

> 22 nodes

## Key Concepts

- **process_command_with_validation()** (11 connections) — `server/command_handler/processing.py`
- **.sanitize_for_logging()** (7 connections) — `server/validators/command_validator.py`
- **_run_command_service_for_validated()** (6 connections) — `server/command_handler/processing.py`
- **_dispatch_parsed_command()** (6 connections) — `server/command_handler/processing.py`
- **_log_security_sensitive_command()** (6 connections) — `server/command_handler/processing.py`
- **CommandExecutionRequest** (5 connections)
- **_handle_validation_error()** (5 connections) — `server/command_handler/processing.py`
- **_parse_command_line_or_client_error()** (3 connections) — `server/command_handler/processing.py`
- **test_command_validator_sanitize_for_logging()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_sanitize_for_logging_truncates()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_sanitize_for_logging_removes_sensitive()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **ValidationError** (2 connections)
- **Validate the raw command string via CommandProcessor.      Returns:         (** (1 connections) — `server/command_handler/processing.py`
- **Extract structured command data, dispatch to CommandService, audit if needed.** (1 connections) — `server/command_handler/processing.py`
- **Parse the command line; on success run CommandService (see ``_parse_command_line** (1 connections) — `server/command_handler/processing.py`
- **Validate ``command_line`` via Click/Pydantic, dispatch to handlers; result dict** (1 connections) — `server/command_handler/processing.py`
- **Log a security-sensitive command for auditing.** (1 connections) — `server/command_handler/processing.py`
- **Handle a validation error during command processing.** (1 connections) — `server/command_handler/processing.py`
- **Test CommandValidator.sanitize_for_logging sanitizes command for logging.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.sanitize_for_logging truncates long commands.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.sanitize_for_logging removes sensitive patterns.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Sanitize command for safe logging.          Truncates and removes sensitive data** (1 connections) — `server/validators/command_validator.py`

## Relationships

- [command inventory factories](command_inventory_factories.md) (11 shared connections)
- [command validation commands](command_validation_commands.md) (4 shared connections)
- [command commands handler](command_commands_handler.md) (3 shared connections)
- [command validator validators](command_validator_validators.md) (3 shared connections)
- [realtime game state](realtime_game_state.md) (1 shared connections)

## Source Files

- `server/command_handler/processing.py`
- `server/tests/unit/validators/test_command_validator.py`
- `server/validators/command_validator.py`

## Audit Trail

- EXTRACTED: 67 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*