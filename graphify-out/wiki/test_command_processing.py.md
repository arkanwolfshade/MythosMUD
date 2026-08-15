# test_command_processing.py

> 25 nodes

## Key Concepts

- **test_command_processing.py** (15 connections) — `server/tests/unit/commands/test_command_processing.py`
- **_dispatch_parsed_command()** (8 connections) — `server/command_handler/processing.py`
- **_log_security_sensitive_command()** (7 connections) — `server/command_handler/processing.py`
- **_run_command_service_for_validated()** (7 connections) — `server/command_handler/processing.py`
- **_handle_validation_error()** (6 connections) — `server/command_handler/processing.py`
- **_parse_command_line_or_client_error()** (6 connections) — `server/command_handler/processing.py`
- **asyncio** (5 connections)
- **test_process_command_with_validation_validation_error()** (4 connections) — `server/tests/unit/commands/test_command_processing.py`
- **CommandExecutionRequest** (4 connections)
- **test_dispatch_parsed_command_client_error()** (3 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_dispatch_parsed_command_success()** (3 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_handle_validation_error_security_sensitive()** (3 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_process_command_with_validation_generic_error()** (3 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_run_command_service_security_sensitive_audit()** (3 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_log_security_sensitive_command_no_session()** (2 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_parse_command_line_or_client_error_no_validated()** (2 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_parse_command_line_or_client_error_success()** (2 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_parse_command_line_or_client_error_with_message()** (2 connections) — `server/tests/unit/commands/test_command_processing.py`
- **ValidationError** (1 connections)
- **Log a security-sensitive command for auditing.** (1 connections) — `server/command_handler/processing.py`
- **Handle a validation error during command processing.** (1 connections) — `server/command_handler/processing.py`
- **Validate the raw command string via CommandProcessor. Returns:…** (1 connections) — `server/command_handler/processing.py`
- **Extract structured command data, dispatch to CommandService, audit if needed.** (1 connections) — `server/command_handler/processing.py`
- **Parse the command line; on success run CommandService (see…** (1 connections) — `server/command_handler/processing.py`
- **Unit tests for command_handler.processing module.** (1 connections) — `server/tests/unit/commands/test_command_processing.py`

## Relationships

- [get_logger](get_logger.md) (6 shared connections)
- [command_handler_unified.py](command_handler_unified.py.md) (5 shared connections)
- [test_command_validator.py](test_command_validator.py.md) (3 shared connections)
- [ValidationError](ValidationError.md) (3 shared connections)
- [.state](state.md) (1 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (1 shared connections)

## Source Files

- `server/command_handler/processing.py`
- `server/tests/unit/commands/test_command_processing.py`

## Audit Trail

- EXTRACTED: 53 (95%)
- INFERRED: 3 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*