# E 2 E Bugs Found

> 10 nodes

## Key Concepts

- **validate_command_format()** (9 connections) — `server/validators/command_validator.py`
- **test_validate_command_format_valid()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_validate_command_format_empty()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_validate_command_format_suspicious()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_validate_command_format_too_long()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test validate_command_format returns True for valid command.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test validate_command_format returns False for empty command.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test validate_command_format returns False for suspicious command.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test validate_command_format returns False for too long command.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Validate command format and return validation result with error message.      Ar** (1 connections) — `server/validators/command_validator.py`

## Relationships

- [Persistence Container Extended](Persistence_Container_Extended.md) (5 shared connections)
- [Client Event Store](Client_Event_Store.md) (1 shared connections)
- [E 2 E Load Readme](E_2_E_Load_Readme.md) (1 shared connections)
- [E 2 E Scenarios Scenario](E_2_E_Scenarios_Scenario.md) (1 shared connections)

## Source Files

- `server/tests/unit/validators/test_command_validator.py`
- `server/validators/command_validator.py`

## Audit Trail

- EXTRACTED: 26 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*