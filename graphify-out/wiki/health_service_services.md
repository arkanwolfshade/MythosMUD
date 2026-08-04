# health service services

> 60 nodes

## Key Concepts

- **test_command_service.py** (36 connections) — `server/tests/unit/commands/test_command_service.py`
- **command_service()** (3 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_process_validated_command_validation_error()** (3 connections) — `server/tests/unit/commands/test_command_service.py`
- **mock_request()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **mock_user()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_process_validated_command_success()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_process_validated_command_no_command_type()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_process_validated_command_unknown_command()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_process_validated_command_handler_error()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_process_validated_command_logging_error()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_parse_command_string_success()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_parse_command_string_with_subcommand()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_parse_command_string_unexpected_error()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_prepare_command_data_basic()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_prepare_command_data_with_pipe_target()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_extract_parsed_fields_basic()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_extract_parsed_fields_with_pipe_target()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_execute_command_handler_success()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_execute_command_handler_error()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_process_command_success()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_process_command_parse_error()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_process_command_no_handler()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_get_available_commands()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_register_command_handler()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_register_command_handler_overwrites_existing()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- *... and 35 more nodes in this community*

## Relationships

- [Database Access Layer](Database_Access_Layer.md) (3 shared connections)
- [combat services initialization](combat_services_initialization.md) (2 shared connections)
- [commands admin mute](commands_admin_mute.md) (1 shared connections)
- [Loot Generation](Loot_Generation.md) (1 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (1 shared connections)

## Source Files

- `server/tests/unit/commands/test_command_service.py`

## Audit Trail

- EXTRACTED: 125 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*