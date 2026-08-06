# combat attack handler

> 32 nodes

## Key Concepts

- **processing.py** (26 connections) — `server/command_handler/processing.py`
- **test_command_processing.py** (15 connections) — `server/tests/unit/commands/test_command_processing.py`
- **process_command_with_validation()** (13 connections) — `server/command_handler/processing.py`
- **_dispatch_parsed_command()** (8 connections) — `server/command_handler/processing.py`
- **_run_command_service_for_validated()** (7 connections) — `server/command_handler/processing.py`
- **_log_security_sensitive_command()** (7 connections) — `server/command_handler/processing.py`
- **_handle_processing_error()** (7 connections) — `server/command_handler/processing.py`
- **_parse_command_line_or_client_error()** (6 connections) — `server/command_handler/processing.py`
- **_handle_validation_error()** (6 connections) — `server/command_handler/processing.py`
- **CommandExecutionRequest** (5 connections)
- **test_handle_validation_error_security_sensitive()** (3 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_process_command_with_validation_validation_error()** (3 connections) — `server/tests/unit/commands/test_command_processing.py`
- **ValidationError** (2 connections)
- **Exception** (2 connections)
- **test_parse_command_line_or_client_error_with_message()** (2 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_parse_command_line_or_client_error_no_validated()** (2 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_parse_command_line_or_client_error_success()** (2 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_dispatch_parsed_command_client_error()** (2 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_dispatch_parsed_command_success()** (2 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_run_command_service_security_sensitive_audit()** (2 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_log_security_sensitive_command_no_session()** (2 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_handle_processing_error()** (2 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_process_command_with_validation_generic_error()** (2 connections) — `server/tests/unit/commands/test_command_processing.py`
- **Command Processing Logic for MythosMUD.  This module contains the core command** (1 connections) — `server/command_handler/processing.py`
- **Validate the raw command string via CommandProcessor.      Returns:         (** (1 connections) — `server/command_handler/processing.py`
- *... and 7 more nodes in this community*

## Relationships

- [command validator validators](command_validator_validators.md) (6 shared connections)
- [command validation commands](command_validation_commands.md) (5 shared connections)
- [add used user](add_used_user.md) (4 shared connections)
- [player model models](player_model_models.md) (3 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (2 shared connections)
- [Error Conversion](Error_Conversion.md) (2 shared connections)
- [Security Validator Tests](Security_Validator_Tests.md) (2 shared connections)
- [player left room](player_left_room.md) (2 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (1 shared connections)
- [alias storage rationale](alias_storage_rationale.md) (1 shared connections)
- [realtime real time](realtime_real_time.md) (1 shared connections)
- [combat services initialization](combat_services_initialization.md) (1 shared connections)

## Source Files

- `server/command_handler/processing.py`
- `server/tests/unit/commands/test_command_processing.py`

## Audit Trail

- EXTRACTED: 133 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*