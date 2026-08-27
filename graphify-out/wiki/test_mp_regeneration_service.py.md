# test_mp_regeneration_service.py

> 18 nodes

## Key Concepts

- **_validate_command_basics()** (14 connections) — `server/command_handler_unified.py`
- **TestValidateCommandBasics** (6 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_validate_command_basics_empty()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_validate_command_basics_invalid_content()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_validate_command_basics_too_long()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_validate_command_basics_valid()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_validate_command_basics_empty()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_validate_command_basics_invalid_content()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_validate_command_basics_too_long()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_validate_command_basics_valid()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **Test _validate_command_basics returns result for empty command.** (2 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **Test _validate_command_basics returns result for empty command.** (2 connections) — `server/tests/unit/commands/test_command_validation.py`
- **Validate basic command requirements. Returns result dict if invalid, None if…** (1 connections) — `server/command_handler_unified.py`
- **Test _validate_command_basics returns result for invalid content.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **Test _validate_command_basics returns None for valid command.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **Test _validate_command_basics function.** (1 connections) — `server/tests/unit/commands/test_command_validation.py`
- **Test _validate_command_basics returns result for invalid command content.** (1 connections) — `server/tests/unit/commands/test_command_validation.py`
- **Test _validate_command_basics returns None for valid command.** (1 connections) — `server/tests/unit/commands/test_command_validation.py`

## Relationships

- [test_connection_statistics.py](test_connection_statistics.py.md) (4 shared connections)
- [test_error_handling_middleware.py](test_error_handling_middleware.py.md) (4 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (2 shared connections)

## Source Files

- `server/command_handler_unified.py`
- `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- `server/tests/unit/commands/test_command_validation.py`

## Audit Trail

- EXTRACTED: 32 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*