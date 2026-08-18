# server command handler processing

> 33 nodes

## Key Concepts

- **processing.py** (26 connections) — `server/command_handler/processing.py`
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
- **Command Processing Logic for MythosMUD. This module contains the core command…** (1 connections) — `server/command_handler/processing.py`
- *... and 8 more nodes in this community*

## Relationships

- [server tests unit validators test](server_tests_unit_validators_test.md) (6 shared connections)
- [server command handler alias expansion](server_command_handler_alias_expansion.md) (4 shared connections)
- [mythosvalidationerror](mythosvalidationerror.md) (4 shared connections)
- [server command handler command execution](server_command_handler_command_execution.md) (3 shared connections)
- [server models command alias aliascommand](server_models_command_alias_aliascommand.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (2 shared connections)
- [claude rules pydantic](claude_rules_pydantic.md) (2 shared connections)
- [server commands rescue commands](server_commands_rescue_commands.md) (1 shared connections)
- [commandhandler](commandhandler.md) (1 shared connections)
- [server tests unit utils test](server_tests_unit_utils_test.md) (1 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (1 shared connections)

## Source Files

- `server/command_handler/processing.py`
- `server/tests/unit/commands/test_command_processing.py`

## Audit Trail

- EXTRACTED: 87 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*