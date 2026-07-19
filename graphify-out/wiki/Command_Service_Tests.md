# Command Service Tests

> 63 nodes · cohesion 0.03

## Key Concepts

- **test_command_service.py** (35 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_parse_command_string_validation_error()** (4 connections) — `server/tests/unit/commands/test_command_service.py`
- **command_service()** (3 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_extract_parsed_fields_handles_missing_attributes()** (3 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_parse_command_string_unexpected_error()** (3 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_process_validated_command_logging_error()** (3 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_process_validated_command_validation_error()** (3 connections) — `server/tests/unit/commands/test_command_service.py`
- **mock_request()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **mock_user()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **Create a mock user object.** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **Test process_validated_command handles handler errors.** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_execute_command_handler_error()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_execute_command_handler_returns_non_dict()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_execute_command_handler_success()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_extract_parsed_fields_basic()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_extract_parsed_fields_with_pipe_target()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_get_available_commands()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_log_model_dump_result()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_log_parsed_command_inspection()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_parse_command_string_success()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_parse_command_string_with_subcommand()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_prepare_command_data_basic()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_prepare_command_data_with_pipe_target()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_process_command_no_handler()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_process_command_parse_error()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- *... and 38 more nodes in this community*

## Relationships

- [[NPC Admin API]] (3 shared connections)
- [[Alias Expansion Logic]] (2 shared connections)
- [[Database Manager Tests]] (2 shared connections)
- [[Pydantic Error Handlers]] (2 shared connections)
- [[Command Processor Commands]] (1 shared connections)
- [[Services Service Room]] (1 shared connections)
- [[Logout and Quit Commands]] (1 shared connections)
- [[Command Parser Tests]] (1 shared connections)

## Source Files

- `server/tests/unit/commands/test_command_service.py`
- `server/tests/unit/commands/test_logout_commands.py`
- `server/tests/unit/utils/test_command_parser.py`

## Audit Trail

- EXTRACTED: 134 (96%)
- INFERRED: 5 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
