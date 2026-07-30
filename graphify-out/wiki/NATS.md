# NATS

> 67 nodes

## Key Concepts

- **test_command_service.py** (36 connections) — `server/tests/unit/commands/test_command_service.py`
- **MythosValidationError** (8 connections)
- **test_parse_command_string_validation_error()** (4 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_create_command_object_re_raises_mythos_validation_error()** (4 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_process_command_string_mythos_validation_error()** (4 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_process_validated_command_validation_error()** (3 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_extract_parsed_fields_handles_missing_attributes()** (3 connections) — `server/tests/unit/commands/test_command_service.py`
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
- *... and 42 more nodes in this community*

## Relationships

- [.initialize()](initialize%28%29.md) (4 shared connections)
- [Player Position Service](Player_Position_Service.md) (3 shared connections)
- [convert pydantic error()](convert_pydantic_error%28%29.md) (2 shared connections)
- [AbstractContextManager](AbstractContextManager.md) (1 shared connections)
- [Any](Any.md) (1 shared connections)
- [real time](real_time.md) (1 shared connections)
- [create access token()](create_access_token%28%29.md) (1 shared connections)
- [.apply dp change()](apply_dp_change%28%29.md) (1 shared connections)
- [test command processor](test_command_processor.md) (1 shared connections)

## Source Files

- `server/tests/unit/commands/test_command_service.py`
- `server/tests/unit/utils/test_command_parser.py`
- `server/tests/unit/utils/test_command_processor.py`

## Audit Trail

- EXTRACTED: 138 (93%)
- INFERRED: 11 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*