# Command Commands Validation

> 18 nodes · cohesion 0.14

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
- **Test _validate_command_basics returns result for invalid command content.** (2 connections) — `server/tests/unit/commands/test_command_validation.py`
- **Test _validate_command_basics returns None for valid command.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **Test _validate_command_basics function.** (1 connections) — `server/tests/unit/commands/test_command_validation.py`
- **Test _validate_command_basics returns result for empty command.** (1 connections) — `server/tests/unit/commands/test_command_validation.py`
- **Test _validate_command_basics returns result for command too long.** (1 connections) — `server/tests/unit/commands/test_command_validation.py`
- **Test _validate_command_basics returns None for valid command.** (1 connections) — `server/tests/unit/commands/test_command_validation.py`
- **Validate basic command requirements. Returns result dict if invalid, None if val** (1 connections) — `server/command_handler_unified.py`

## Relationships

- [[Command Alias Handling]] (5 shared connections)
- [[Catatonia Check Logic]] (2 shared connections)
- [[Unified Command Handler]] (2 shared connections)
- [[Alias Expansion Logic]] (1 shared connections)

## Source Files

- `server/command_handler_unified.py`
- `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- `server/tests/unit/commands/test_command_validation.py`

## Audit Trail

- EXTRACTED: 54 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
