# server tests unit commands test

> 14 nodes

## Key Concepts

- **asyncio** (12 connections)
- **test_process_validated_command_validation_error()** (5 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_execute_command_handler_success()** (3 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_process_command_no_handler()** (3 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_process_validated_command_handler_error()** (3 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_process_validated_command_no_command_type()** (3 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_process_validated_command_success()** (3 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_process_validated_command_unknown_command()** (3 connections) — `server/tests/unit/commands/test_command_service.py`
- **Test process_validated_command handles handler errors.** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **Test _execute_command_handler successfully executes handler.** (1 connections) — `server/tests/unit/commands/test_command_service.py`
- **Test process_command handles missing handler.** (1 connections) — `server/tests/unit/commands/test_command_service.py`
- **Test process_validated_command successfully routes to handler.** (1 connections) — `server/tests/unit/commands/test_command_service.py`
- **Test process_validated_command handles missing command_type.** (1 connections) — `server/tests/unit/commands/test_command_service.py`
- **Test process_validated_command handles unknown command type.** (1 connections) — `server/tests/unit/commands/test_command_service.py`

## Relationships

- [server tests unit commands test](server_tests_unit_commands_test.md) (12 shared connections)
- [mythosvalidationerror](mythosvalidationerror.md) (2 shared connections)

## Source Files

- `server/tests/unit/commands/test_command_service.py`

## Audit Trail

- EXTRACTED: 26 (93%)
- INFERRED: 2 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*