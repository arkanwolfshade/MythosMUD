# test_command_service.py

> 88 nodes

## Key Concepts

- **test_command_service.py** (37 connections) — `server/tests/unit/commands/test_command_service.py`
- **CommandService** (20 connections) — `server/commands/command_service.py`
- **asyncio** (12 connections)
- **._extract_parsed_fields()** (7 connections) — `server/commands/command_service.py`
- **.process_command()** (6 connections) — `server/commands/command_service.py`
- **._execute_command_handler()** (5 connections) — `server/commands/command_service.py`
- **._parse_command_string()** (5 connections) — `server/commands/command_service.py`
- **._prepare_command_data()** (5 connections) — `server/commands/command_service.py`
- **Command** (5 connections)
- **._fallback_parsed_fields()** (4 connections) — `server/commands/command_service.py`
- **._log_parsed_command_inspection()** (4 connections) — `server/commands/command_service.py`
- **command_service()** (4 connections) — `server/tests/unit/commands/test_command_service.py`
- **._log_model_dump_result()** (3 connections) — `server/commands/command_service.py`
- **.register_command_handler()** (3 connections) — `server/commands/command_service.py`
- **mock_request()** (3 connections) — `server/tests/unit/commands/test_command_service.py`
- **mock_user()** (3 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_execute_command_handler_error()** (3 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_execute_command_handler_returns_non_dict()** (3 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_execute_command_handler_success()** (3 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_process_command_no_handler()** (3 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_process_command_parse_error()** (3 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_process_command_success()** (3 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_process_validated_command_handler_error()** (3 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_process_validated_command_logging_error()** (3 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_process_validated_command_no_command_type()** (3 connections) — `server/tests/unit/commands/test_command_service.py`
- *... and 63 more nodes in this community*

## Relationships

- [AliasStorage](AliasStorage.md) (5 shared connections)
- [ValidationError](ValidationError.md) (4 shared connections)
- [processing.py](processing.py.md) (1 shared connections)
- [command_handler_unified.py](command_handler_unified.py.md) (1 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (1 shared connections)
- [get_username_from_user](get_username_from_user.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)
- [AttributeError](AttributeError.md) (1 shared connections)

## Source Files

- `server/commands/command_service.py`
- `server/tests/unit/commands/test_command_service.py`

## Audit Trail

- EXTRACTED: 127 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*