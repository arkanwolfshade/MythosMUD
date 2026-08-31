# test_command_processing.py

> 31 nodes

## Key Concepts

- **test_command_processing.py** (16 connections) — `server/tests/unit/commands/test_command_processing.py`
- **process_command_with_validation()** (13 connections) — `server/command_handler/processing.py`
- **_dispatch_parsed_command()** (8 connections) — `server/command_handler/processing.py`
- **_handle_processing_error()** (7 connections) — `server/command_handler/processing.py`
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
- **test_handle_processing_error()** (2 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_log_security_sensitive_command_no_session()** (2 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_parse_command_line_or_client_error_no_validated()** (2 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_parse_command_line_or_client_error_success()** (2 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_parse_command_line_or_client_error_with_message()** (2 connections) — `server/tests/unit/commands/test_command_processing.py`
- **Exception** (1 connections)
- **ValidationError** (1 connections)
- **Validate ``command_line`` via Click/Pydantic, dispatch to handlers; result dict…** (1 connections) — `server/command_handler/processing.py`
- **Log a security-sensitive command for auditing.** (1 connections) — `server/command_handler/processing.py`
- *... and 6 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (12 shared connections)
- [test_command_validator.py](test_command_validator.py.md) (4 shared connections)
- [alias_expansion.py](alias_expansion.py.md) (2 shared connections)
- [command_handler_unified.py](command_handler_unified.py.md) (2 shared connections)
- [BaseCommand](BaseCommand.md) (1 shared connections)
- [.state](state.md) (1 shared connections)
- [command_input.py](command_input.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/command_handler/processing.py`
- `server/tests/unit/commands/test_command_processing.py`

## Audit Trail

- EXTRACTED: 69 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*