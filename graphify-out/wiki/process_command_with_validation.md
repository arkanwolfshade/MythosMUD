# process_command_with_validation

> 31 nodes

## Key Concepts

- **process_command_with_validation()** (11 connections) — `server/command_handler/processing.py`
- **.is_security_sensitive()** (9 connections) — `server/validators/command_validator.py`
- **handle_expanded_command()** (8 connections) — `server/command_handler/alias_expansion.py`
- **_dispatch_parsed_command()** (6 connections) — `server/command_handler/processing.py`
- **_handle_processing_error()** (6 connections) — `server/command_handler/processing.py`
- **_log_security_sensitive_command()** (6 connections) — `server/command_handler/processing.py`
- **_run_command_service_for_validated()** (6 connections) — `server/command_handler/processing.py`
- **_handle_validation_error()** (5 connections) — `server/command_handler/processing.py`
- **CommandExecutionRequest** (4 connections)
- **_parse_command_line_or_client_error()** (3 connections) — `server/command_handler/processing.py`
- **test_command_validator_is_security_sensitive_admin()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_is_security_sensitive_case_insensitive()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_is_security_sensitive_empty()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_is_security_sensitive_non_sensitive()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Any** (1 connections)
- **CommandExecutionRequest** (1 connections)
- **Exception** (1 connections)
- **ValidationError** (1 connections)
- **Handle command processing with alias expansion and loop detection. This…** (1 connections) — `server/command_handler/alias_expansion.py`
- **Validate ``command_line`` via Click/Pydantic, dispatch to handlers; result dict…** (1 connections) — `server/command_handler/processing.py`
- **Log a security-sensitive command for auditing.** (1 connections) — `server/command_handler/processing.py`
- **Handle a validation error during command processing.** (1 connections) — `server/command_handler/processing.py`
- **Handle a general exception during command processing.** (1 connections) — `server/command_handler/processing.py`
- **Validate the raw command string via CommandProcessor. Returns:…** (1 connections) — `server/command_handler/processing.py`
- **Extract structured command data, dispatch to CommandService, audit if needed.** (1 connections) — `server/command_handler/processing.py`
- *... and 6 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (10 shared connections)
- [test_command_validator.py](test_command_validator.py.md) (5 shared connections)
- [command_handler_unified.py](command_handler_unified.py.md) (4 shared connections)
- [catatonia_check.py](catatonia_check.py.md) (2 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (1 shared connections)
- [.state](state.md) (1 shared connections)

## Source Files

- `server/command_handler/alias_expansion.py`
- `server/command_handler/processing.py`
- `server/tests/unit/validators/test_command_validator.py`
- `server/validators/command_validator.py`

## Audit Trail

- EXTRACTED: 57 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*