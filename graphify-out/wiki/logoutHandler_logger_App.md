# logoutHandler logger App

> 40 nodes

## Key Concepts

- **test_command_processing.py** (15 connections) — `server/tests/unit/commands/test_command_processing.py`
- **process_command_with_validation()** (13 connections) — `server/command_handler/processing.py`
- **.is_security_sensitive()** (9 connections) — `server/validators/command_validator.py`
- **_dispatch_parsed_command()** (8 connections) — `server/command_handler/processing.py`
- **_run_command_service_for_validated()** (7 connections) — `server/command_handler/processing.py`
- **_log_security_sensitive_command()** (7 connections) — `server/command_handler/processing.py`
- **_handle_processing_error()** (7 connections) — `server/command_handler/processing.py`
- **_parse_command_line_or_client_error()** (6 connections) — `server/command_handler/processing.py`
- **_handle_validation_error()** (6 connections) — `server/command_handler/processing.py`
- **CommandExecutionRequest** (5 connections)
- **test_handle_validation_error_security_sensitive()** (3 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_process_command_with_validation_validation_error()** (3 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_command_validator_is_security_sensitive_admin()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_is_security_sensitive_case_insensitive()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_is_security_sensitive_non_sensitive()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_is_security_sensitive_empty()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **ValidationError** (2 connections)
- **Exception** (2 connections)
- **test_parse_command_line_or_client_error_with_message()** (2 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_parse_command_line_or_client_error_no_validated()** (2 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_parse_command_line_or_client_error_success()** (2 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_dispatch_parsed_command_client_error()** (2 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_dispatch_parsed_command_success()** (2 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_run_command_service_security_sensitive_audit()** (2 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_log_security_sensitive_command_no_session()** (2 connections) — `server/tests/unit/commands/test_command_processing.py`
- *... and 15 more nodes in this community*

## Relationships

- [Loot Generation](Loot_Generation.md) (10 shared connections)
- [command validator validators](command_validator_validators.md) (5 shared connections)
- [command validation commands](command_validation_commands.md) (3 shared connections)
- [alias graph rationale](alias_graph_rationale.md) (3 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (3 shared connections)
- [command commands handler](command_commands_handler.md) (2 shared connections)
- [nats services metrics](nats_services_metrics.md) (1 shared connections)
- [Security Validator Tests](Security_Validator_Tests.md) (1 shared connections)

## Source Files

- `server/command_handler/processing.py`
- `server/tests/unit/commands/test_command_processing.py`
- `server/tests/unit/validators/test_command_validator.py`
- `server/validators/command_validator.py`

## Audit Trail

- EXTRACTED: 132 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*