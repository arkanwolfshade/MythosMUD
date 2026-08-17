# processing.py

> 45 nodes

## Key Concepts

- **processing.py** (26 connections) — `server/command_handler/processing.py`
- **test_command_processing.py** (16 connections) — `server/tests/unit/commands/test_command_processing.py`
- **process_command_with_validation()** (13 connections) — `server/command_handler/processing.py`
- **strip_ansi_codes()** (13 connections) — `server/validators/security_validator.py`
- **_dispatch_parsed_command()** (8 connections) — `server/command_handler/processing.py`
- **_handle_processing_error()** (7 connections) — `server/command_handler/processing.py`
- **_log_security_sensitive_command()** (7 connections) — `server/command_handler/processing.py`
- **_run_command_service_for_validated()** (7 connections) — `server/command_handler/processing.py`
- **_handle_validation_error()** (6 connections) — `server/command_handler/processing.py`
- **_parse_command_line_or_client_error()** (6 connections) — `server/command_handler/processing.py`
- **asyncio** (5 connections)
- **.process_validated_command()** (4 connections) — `server/commands/command_service.py`
- **test_process_command_with_validation_validation_error()** (4 connections) — `server/tests/unit/commands/test_command_processing.py`
- **CommandExecutionRequest** (4 connections)
- **test_dispatch_parsed_command_client_error()** (3 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_dispatch_parsed_command_success()** (3 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_handle_validation_error_security_sensitive()** (3 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_process_command_with_validation_generic_error()** (3 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_run_command_service_security_sensitive_audit()** (3 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_strip_ansi_codes_color_codes()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_strip_ansi_codes_cursor_movement()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_strip_ansi_codes_empty()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_strip_ansi_codes_no_ansi()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_handle_processing_error()** (2 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_log_security_sensitive_command_no_session()** (2 connections) — `server/tests/unit/commands/test_command_processing.py`
- *... and 20 more nodes in this community*

## Relationships

- [test_command_validator.py](test_command_validator.py.md) (7 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (6 shared connections)
- [AliasGraph](AliasGraph.md) (4 shared connections)
- [ValidationError](ValidationError.md) (4 shared connections)
- [command_handler_unified.py](command_handler_unified.py.md) (2 shared connections)
- [AliasStorage](AliasStorage.md) (2 shared connections)
- [CommandService](CommandService.md) (2 shared connections)
- [command_service.py](command_service.py.md) (2 shared connections)
- [BaseCommand](BaseCommand.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [DatabaseError](DatabaseError.md) (2 shared connections)
- [real_time.py](real_time.py.md) (1 shared connections)

## Source Files

- `server/command_handler/processing.py`
- `server/commands/command_service.py`
- `server/tests/unit/commands/test_command_processing.py`
- `server/tests/unit/validators/test_security_validator.py`
- `server/validators/security_validator.py`

## Audit Trail

- EXTRACTED: 108 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*