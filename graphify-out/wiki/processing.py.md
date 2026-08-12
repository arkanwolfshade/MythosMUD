# processing.py

> 47 nodes

## Key Concepts

- **processing.py** (25 connections) — `server/command_handler/processing.py`
- **command_validator.py** (17 connections) — `server/validators/command_validator.py`
- **alias_expansion.py** (16 connections) — `server/command_handler/alias_expansion.py`
- **CommandValidator** (14 connections) — `server/validators/command_validator.py`
- **process_command_with_validation()** (11 connections) — `server/command_handler/processing.py`
- **.is_security_sensitive()** (9 connections) — `server/validators/command_validator.py`
- **handle_expanded_command()** (8 connections) — `server/command_handler/alias_expansion.py`
- **.sanitize_for_logging()** (7 connections) — `server/validators/command_validator.py`
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
- **test_command_validator_sanitize_for_logging()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_sanitize_for_logging_removes_sensitive()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_sanitize_for_logging_truncates()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Any** (1 connections)
- **CommandExecutionRequest** (1 connections)
- **Exception** (1 connections)
- *... and 22 more nodes in this community*

## Relationships

- [test_command_validator.py](test_command_validator.py.md) (20 shared connections)
- [command_handler_unified.py](command_handler_unified.py.md) (9 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [catatonia_check.py](catatonia_check.py.md) (4 shared connections)
- [CommandService](CommandService.md) (3 shared connections)
- [AliasStorage](AliasStorage.md) (3 shared connections)
- [command_input.py](command_input.py.md) (2 shared connections)
- [AuditLogger](AuditLogger.md) (2 shared connections)
- [WebSocketRequestContext](WebSocketRequestContext.md) (2 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (2 shared connections)
- [command.py](command.py.md) (2 shared connections)
- [.state](state.md) (1 shared connections)

## Source Files

- `server/command_handler/alias_expansion.py`
- `server/command_handler/processing.py`
- `server/tests/unit/validators/test_command_validator.py`
- `server/validators/command_validator.py`

## Audit Trail

- EXTRACTED: 188 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*