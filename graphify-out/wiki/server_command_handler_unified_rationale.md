# server command handler unified rationale

> 19 nodes

## Key Concepts

- **_validate_command_basics()** (16 connections) — `server/command_handler_unified.py`
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
- **Validate basic command requirements. Returns result dict if invalid, None if…** (1 connections) — `server/command_handler_unified.py`
- **Test _validate_command_basics returns result for invalid content.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **Test _validate_command_basics returns None for valid command.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **Test _validate_command_basics function.** (1 connections) — `server/tests/unit/commands/test_command_validation.py`
- **Test _validate_command_basics returns result for empty command.** (1 connections) — `server/tests/unit/commands/test_command_validation.py`
- **Test _validate_command_basics returns result for command too long.** (1 connections) — `server/tests/unit/commands/test_command_validation.py`
- **Test _validate_command_basics returns result for invalid command content.** (1 connections) — `server/tests/unit/commands/test_command_validation.py`
- **Test _validate_command_basics returns None for valid command.** (1 connections) — `server/tests/unit/commands/test_command_validation.py`

## Relationships

- [server command handler command execution](server_command_handler_command_execution.md) (8 shared connections)
- [server command handler catatonia check](server_command_handler_catatonia_check.md) (2 shared connections)
- [server tests unit validators test](server_tests_unit_validators_test.md) (2 shared connections)

## Source Files

- `server/command_handler_unified.py`
- `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- `server/tests/unit/commands/test_command_validation.py`

## Audit Trail

- EXTRACTED: 34 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*