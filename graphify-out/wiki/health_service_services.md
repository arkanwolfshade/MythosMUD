# health service services

> 65 nodes

## Key Concepts

- **test_command_service.py** (36 connections) — `server/tests/unit/commands/test_command_service.py`
- **MythosValidationError** (9 connections)
- **test_parse_command_string_validation_error()** (4 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_create_command_object_re_raises_mythos_validation_error()** (4 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_process_command_string_mythos_validation_error()** (4 connections) — `server/tests/unit/utils/test_command_processor.py`
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
- *... and 40 more nodes in this community*

## Relationships

- [command inventory models](command_inventory_models.md) (4 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (2 shared connections)
- [combat services initialization](combat_services_initialization.md) (2 shared connections)
- [Exception Containers](Exception_Containers.md) (1 shared connections)
- [inventory commands command](inventory_commands_command.md) (1 shared connections)
- [room conftest toolkit](room_conftest_toolkit.md) (1 shared connections)
- [commands position system](commands_position_system.md) (1 shared connections)
- [command inventory factories](command_inventory_factories.md) (1 shared connections)
- [look helpers commands](look_helpers_commands.md) (1 shared connections)
- [command parser rationale](command_parser_rationale.md) (1 shared connections)
- [command processor rationale](command_processor_rationale.md) (1 shared connections)

## Source Files

- `server/tests/unit/commands/test_command_service.py`
- `server/tests/unit/utils/test_command_parser.py`
- `server/tests/unit/utils/test_command_processor.py`

## Audit Trail

- EXTRACTED: 135 (92%)
- INFERRED: 11 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*