# test_command_validator.py

> 135 nodes

## Key Concepts

- **test_command_validator.py** (52 connections) — `server/tests/unit/validators/test_command_validator.py`
- **processing.py** (25 connections) — `server/command_handler/processing.py`
- **CommandValidator** (14 connections) — `server/validators/command_validator.py`
- **process_command_with_validation()** (11 connections) — `server/command_handler/processing.py`
- **.validate_command_content()** (11 connections) — `server/validators/command_validator.py`
- **clean_command_input()** (9 connections) — `server/validators/command_validator.py`
- **.is_security_sensitive()** (9 connections) — `server/validators/command_validator.py`
- **validate_command_format()** (9 connections) — `server/validators/command_validator.py`
- **.validate_expanded_command()** (8 connections) — `server/validators/command_validator.py`
- **is_suspicious_input()** (8 connections) — `server/validators/command_validator.py`
- **normalize_command()** (8 connections) — `server/validators/command_validator.py`
- **.sanitize_for_logging()** (7 connections) — `server/validators/command_validator.py`
- **.validate_alias_definition()** (7 connections) — `server/validators/command_validator.py`
- **validate_command_length()** (7 connections) — `server/validators/command_validator.py`
- **_dispatch_parsed_command()** (6 connections) — `server/command_handler/processing.py`
- **_handle_processing_error()** (6 connections) — `server/command_handler/processing.py`
- **_log_security_sensitive_command()** (6 connections) — `server/command_handler/processing.py`
- **_run_command_service_for_validated()** (6 connections) — `server/command_handler/processing.py`
- **_handle_validation_error()** (5 connections) — `server/command_handler/processing.py`
- **.extract_command_name()** (5 connections) — `server/validators/command_validator.py`
- **.is_valid_command_name()** (4 connections) — `server/validators/command_validator.py`
- **CommandExecutionRequest** (4 connections)
- **_parse_command_line_or_client_error()** (3 connections) — `server/command_handler/processing.py`
- **test_clean_command_input_basic()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_clean_command_input_empty()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- *... and 110 more nodes in this community*

## Relationships

- [test_security_validator.py](test_security_validator.py.md) (15 shared connections)
- [command_handler_unified.py](command_handler_unified.py.md) (7 shared connections)
- [AliasStorage](AliasStorage.md) (6 shared connections)
- [catatonia_check.py](catatonia_check.py.md) (2 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [test_command_parser.py](test_command_parser.py.md) (2 shared connections)
- [command_input.py](command_input.py.md) (1 shared connections)
- [.state](state.md) (1 shared connections)
- [AuditLogger](AuditLogger.md) (1 shared connections)
- [WebSocketRequestContext](WebSocketRequestContext.md) (1 shared connections)

## Source Files

- `server/command_handler/processing.py`
- `server/tests/unit/validators/test_command_validator.py`
- `server/validators/command_validator.py`

## Audit Trail

- EXTRACTED: 234 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*