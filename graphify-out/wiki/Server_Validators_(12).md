# Server Validators (12)

> 9 nodes

## Key Concepts

- **validate_command_format()** (9 connections) — `server/validators/command_validator.py`
- **test_validate_command_format_valid()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_validate_command_format_empty()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_validate_command_format_suspicious()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_validate_command_format_too_long()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test validate_command_format returns False for empty command.** (2 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test validate_command_format returns True for valid command.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test validate_command_format returns False for suspicious command.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Validate command format and return validation result with error message.      Ar** (1 connections) — `server/validators/command_validator.py`

## Relationships

- [Server Validators (4)](Server_Validators_%284%29.md) (5 shared connections)
- [Server Commands](Server_Commands.md) (1 shared connections)
- [Server Commands (5)](Server_Commands_%285%29.md) (1 shared connections)
- [Server Validators (16)](Server_Validators_%2816%29.md) (1 shared connections)

## Source Files

- `server/tests/unit/validators/test_command_validator.py`
- `server/validators/command_validator.py`

## Audit Trail

- EXTRACTED: 26 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*