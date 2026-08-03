# command handler processing

> 25 nodes

## Key Concepts

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
- **Validate the raw command string via CommandProcessor.      Returns:         (** (1 connections) — `server/command_handler/processing.py`
- **Extract structured command data, dispatch to CommandService, audit if needed.** (1 connections) — `server/command_handler/processing.py`
- **Parse the command line; on success run CommandService (see ``_parse_command_line** (1 connections) — `server/command_handler/processing.py`
- **Log a security-sensitive command for auditing.** (1 connections) — `server/command_handler/processing.py`
- **Handle a validation error during command processing.** (1 connections) — `server/command_handler/processing.py`
- **Handle a general exception during command processing.** (1 connections) — `server/command_handler/processing.py`
- **Test CommandValidator.is_security_sensitive detects admin commands.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.is_security_sensitive is case-insensitive.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.is_security_sensitive returns False for non-sensitive comm** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.is_security_sensitive returns False for empty command.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Check if command requires audit logging.          Identifies commands that shoul** (1 connections) — `server/validators/command_validator.py`

## Relationships

- [commands alias rationale](commands_alias_rationale.md) (7 shared connections)
- [command handler unified](command_handler_unified.md) (4 shared connections)
- [command validator validators](command_validator_validators.md) (4 shared connections)
- [command validation commands](command_validation_commands.md) (3 shared connections)
- [alias storage commands](alias_storage_commands.md) (2 shared connections)
- [realtime game state](realtime_game_state.md) (1 shared connections)

## Source Files

- `server/command_handler/processing.py`
- `server/tests/unit/validators/test_command_validator.py`
- `server/validators/command_validator.py`

## Audit Trail

- EXTRACTED: 69 (95%)
- INFERRED: 4 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*