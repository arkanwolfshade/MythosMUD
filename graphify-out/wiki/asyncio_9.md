# asyncio

> 15 nodes

## Key Concepts

- **asyncio** (12 connections)
- **test_execute_command_handler_error()** (3 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_execute_command_handler_returns_non_dict()** (3 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_process_command_parse_error()** (3 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_process_validated_command_logging_error()** (3 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_process_validated_command_no_command_type()** (3 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_process_validated_command_success()** (3 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_process_validated_command_unknown_command()** (3 connections) — `server/tests/unit/commands/test_command_service.py`
- **Test _execute_command_handler handles handler errors.** (1 connections) — `server/tests/unit/commands/test_command_service.py`
- **Test process_command handles parse errors.** (1 connections) — `server/tests/unit/commands/test_command_service.py`
- **Test _execute_command_handler handles handler returning non-dict.** (1 connections) — `server/tests/unit/commands/test_command_service.py`
- **Test process_validated_command successfully routes to handler.** (1 connections) — `server/tests/unit/commands/test_command_service.py`
- **Test process_validated_command handles missing command_type.** (1 connections) — `server/tests/unit/commands/test_command_service.py`
- **Test process_validated_command handles unknown command type.** (1 connections) — `server/tests/unit/commands/test_command_service.py`
- **Test process_validated_command handles logging errors gracefully.** (1 connections) — `server/tests/unit/commands/test_command_service.py`

## Relationships

- [test_command_service.py](test_command_service.py.md) (7 shared connections)
- [test_execute_command_handler_success](test_execute_command_handler_success.md) (1 shared connections)
- [test_process_command_no_handler](test_process_command_no_handler.md) (1 shared connections)
- [test_process_command_success](test_process_command_success.md) (1 shared connections)
- [test_process_validated_command_handler_error](test_process_validated_command_handler_error.md) (1 shared connections)
- [test_process_validated_command_validation_error](test_process_validated_command_validation_error.md) (1 shared connections)

## Source Files

- `server/tests/unit/commands/test_command_service.py`

## Audit Trail

- EXTRACTED: 26 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*