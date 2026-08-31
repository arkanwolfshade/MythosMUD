# test_command_validator.py

> 147 nodes

## Key Concepts

- **test_command_validator.py** (52 connections) — `server/tests/unit/validators/test_command_validator.py`
- **CommandValidator** (40 connections) — `server/validators/command_validator.py`
- **processing.py** (26 connections) — `server/command_handler/processing.py`
- **test_command_processing.py** (16 connections) — `server/tests/unit/commands/test_command_processing.py`
- **process_command_with_validation()** (13 connections) — `server/command_handler/processing.py`
- **.validate_command_content()** (11 connections) — `server/validators/command_validator.py`
- **.is_security_sensitive()** (9 connections) — `server/validators/command_validator.py`
- **validate_command_format()** (9 connections) — `server/validators/command_validator.py`
- **_dispatch_parsed_command()** (8 connections) — `server/command_handler/processing.py`
- **.validate_expanded_command()** (8 connections) — `server/validators/command_validator.py`
- **is_suspicious_input()** (8 connections) — `server/validators/command_validator.py`
- **normalize_command()** (8 connections) — `server/validators/command_validator.py`
- **_handle_processing_error()** (7 connections) — `server/command_handler/processing.py`
- **_log_security_sensitive_command()** (7 connections) — `server/command_handler/processing.py`
- **_run_command_service_for_validated()** (7 connections) — `server/command_handler/processing.py`
- **.sanitize_for_logging()** (7 connections) — `server/validators/command_validator.py`
- **.validate_alias_definition()** (7 connections) — `server/validators/command_validator.py`
- **validate_command_length()** (7 connections) — `server/validators/command_validator.py`
- **_handle_validation_error()** (6 connections) — `server/command_handler/processing.py`
- **_parse_command_line_or_client_error()** (6 connections) — `server/command_handler/processing.py`
- **.extract_command_name()** (5 connections) — `server/validators/command_validator.py`
- **asyncio** (5 connections)
- **test_process_command_with_validation_validation_error()** (4 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_command_validator_extract_command_name()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_extract_command_name_empty()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- *... and 122 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (13 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (9 shared connections)
- [command_handler_unified.py](command_handler_unified.py.md) (7 shared connections)
- [ValidationError](ValidationError.md) (4 shared connections)
- [AliasStorage](AliasStorage.md) (3 shared connections)
- [test_alias_expansion.py](test_alias_expansion.py.md) (2 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (2 shared connections)
- [BaseCommand](BaseCommand.md) (2 shared connections)
- [.state](state.md) (1 shared connections)
- [CommandService](CommandService.md) (1 shared connections)
- [test_command_processor.py](test_command_processor.py.md) (1 shared connections)
- [WebSocketRequestContext](WebSocketRequestContext.md) (1 shared connections)

## Source Files

- `server/command_handler/processing.py`
- `server/tests/unit/commands/test_command_processing.py`
- `server/tests/unit/validators/test_command_validator.py`
- `server/validators/command_validator.py`

## Audit Trail

- EXTRACTED: 263 (90%)
- INFERRED: 28 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*