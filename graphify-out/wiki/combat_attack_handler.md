# combat attack handler

> 54 nodes

## Key Concepts

- **processing.py** (26 connections) — `server/command_handler/processing.py`
- **alias_expansion.py** (17 connections) — `server/command_handler/alias_expansion.py`
- **test_command_processing.py** (15 connections) — `server/tests/unit/commands/test_command_processing.py`
- **__init__.py** (13 connections) — `server/command_handler/__init__.py`
- **process_command_with_validation()** (13 connections) — `server/command_handler/processing.py`
- **test_alias_expansion.py** (13 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **handle_expanded_command()** (11 connections) — `server/command_handler/alias_expansion.py`
- **check_alias_safety()** (10 connections) — `server/command_handler/alias_expansion.py`
- **validate_expanded_command()** (10 connections) — `server/command_handler/alias_expansion.py`
- **_dispatch_parsed_command()** (8 connections) — `server/command_handler/processing.py`
- **_run_command_service_for_validated()** (7 connections) — `server/command_handler/processing.py`
- **_log_security_sensitive_command()** (7 connections) — `server/command_handler/processing.py`
- **_handle_processing_error()** (7 connections) — `server/command_handler/processing.py`
- **_parse_command_line_or_client_error()** (6 connections) — `server/command_handler/processing.py`
- **_handle_validation_error()** (6 connections) — `server/command_handler/processing.py`
- **CommandExecutionRequest** (5 connections)
- **test_handle_validation_error_security_sensitive()** (3 connections) — `server/tests/unit/commands/test_command_processing.py`
- **test_process_command_with_validation_validation_error()** (3 connections) — `server/tests/unit/commands/test_command_processing.py`
- **Any** (2 connections)
- **CommandExecutionRequest** (2 connections)
- **ValidationError** (2 connections)
- **Exception** (2 connections)
- **test_check_alias_safety_cycle_detected()** (2 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **test_check_alias_safety_depth_too_deep()** (2 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **test_check_alias_safety_ok()** (2 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- *... and 29 more nodes in this community*

## Relationships

- [command commands handler](command_commands_handler.md) (14 shared connections)
- [command validator validators](command_validator_validators.md) (9 shared connections)
- [command validation commands](command_validation_commands.md) (7 shared connections)
- [commands npc admin](commands_npc_admin.md) (4 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (4 shared connections)
- [command inventory models](command_inventory_models.md) (4 shared connections)
- [time service rationale](time_service_rationale.md) (3 shared connections)
- [Security Validator Tests](Security_Validator_Tests.md) (3 shared connections)
- [player effects endpoints](player_effects_endpoints.md) (2 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (2 shared connections)
- [payload realtime optimizer](payload_realtime_optimizer.md) (2 shared connections)
- [character creation service](character_creation_service.md) (1 shared connections)

## Source Files

- `server/command_handler/__init__.py`
- `server/command_handler/alias_expansion.py`
- `server/command_handler/processing.py`
- `server/tests/unit/commands/test_alias_expansion.py`
- `server/tests/unit/commands/test_command_processing.py`

## Audit Trail

- EXTRACTED: 231 (97%)
- INFERRED: 6 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*