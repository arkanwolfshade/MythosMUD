# processing.py

> 19 nodes · cohesion 0.16

## Key Concepts

- **processing.py** (25 connections) — `server/command_handler/processing.py`
- **process_command_with_validation()** (11 connections) — `server/command_handler/processing.py`
- **_dispatch_parsed_command()** (6 connections) — `server/command_handler/processing.py`
- **_handle_processing_error()** (6 connections) — `server/command_handler/processing.py`
- **_log_security_sensitive_command()** (6 connections) — `server/command_handler/processing.py`
- **_run_command_service_for_validated()** (6 connections) — `server/command_handler/processing.py`
- **_handle_validation_error()** (5 connections) — `server/command_handler/processing.py`
- **CommandExecutionRequest** (5 connections)
- **_parse_command_line_or_client_error()** (3 connections) — `server/command_handler/processing.py`
- **Exception** (2 connections)
- **ValidationError** (2 connections)
- **Command Processing Logic for MythosMUD.  This module contains the core command** (1 connections) — `server/command_handler/processing.py`
- **Validate ``command_line`` via Click/Pydantic, dispatch to handlers; result dict** (1 connections) — `server/command_handler/processing.py`
- **Log a security-sensitive command for auditing.** (1 connections) — `server/command_handler/processing.py`
- **Handle a validation error during command processing.** (1 connections) — `server/command_handler/processing.py`
- **Handle a general exception during command processing.** (1 connections) — `server/command_handler/processing.py`
- **Validate the raw command string via CommandProcessor.      Returns:         (** (1 connections) — `server/command_handler/processing.py`
- **Extract structured command data, dispatch to CommandService, audit if needed.** (1 connections) — `server/command_handler/processing.py`
- **Parse the command line; on success run CommandService (see ``_parse_command_line** (1 connections) — `server/command_handler/processing.py`

## Relationships

- [test_command_validator.py](test_command_validator.py.md) (7 shared connections)
- [catatonia_check.py](catatonia_check.py.md) (6 shared connections)
- [AliasStorage](AliasStorage.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (3 shared connections)
- [command_handler_unified.py](command_handler_unified.py.md) (2 shared connections)
- [WebSocketRequestContext](WebSocketRequestContext.md) (1 shared connections)
- [test_command_service.py](test_command_service.py.md) (1 shared connections)
- [exceptions.py](exceptions.py.md) (1 shared connections)
- [ValidationError](ValidationError.md) (1 shared connections)
- [BaseCommand](BaseCommand.md) (1 shared connections)
- [test_command_processor.py](test_command_processor.py.md) (1 shared connections)

## Source Files

- `server/command_handler/processing.py`

## Audit Trail

- EXTRACTED: 81 (95%)
- INFERRED: 4 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*