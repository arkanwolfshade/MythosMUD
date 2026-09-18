# Community 625

> 27 nodes

## Key Concepts

- **_validate_command_basics()** (15 connections) — `server/command_handler_unified.py`
- **.sanitize_for_logging()** (7 connections) — `server/validators/command_validator.py`
- **TestValidateCommandBasics** (6 connections) — `server/tests/unit/commands/test_command_validation.py`
- **test_command_validator_sanitize_for_logging()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_sanitize_for_logging_removes_sensitive()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_sanitize_for_logging_truncates()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
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
- **Test CommandValidator.sanitize_for_logging sanitizes command for logging.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.sanitize_for_logging truncates long commands.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- *... and 2 more nodes in this community*

## Relationships

- [Community 120](Community_120.md) (4 shared connections)
- [Community 360](Community_360.md) (4 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (4 shared connections)
- [Catatonia Status Checks](Catatonia_Status_Checks.md) (2 shared connections)
- [Community 726](Community_726.md) (1 shared connections)
- [Community 256](Community_256.md) (1 shared connections)
- [Character Creation & Auth Dependencies](Character_Creation_&_Auth_Dependencies.md) (1 shared connections)
- [Community 432](Community_432.md) (1 shared connections)

## Source Files

- `server/command_handler_unified.py`
- `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- `server/tests/unit/commands/test_command_validation.py`
- `server/tests/unit/validators/test_command_validator.py`
- `server/validators/command_validator.py`

## Audit Trail

- EXTRACTED: 45 (94%)
- INFERRED: 3 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*