# Server Validators (9)

> 12 nodes

## Key Concepts

- **.validate_command_content()** (11 connections) — `server/validators/command_validator.py`
- **test_command_validator_validate_command_content_valid()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_validate_command_content_null_byte()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_validate_command_content_dangerous_pattern()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_validate_command_content_too_long()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_validate_command_content_non_printable()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_validate_command_content_allows_newline_tab_space()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.validate_command_content detects null bytes.** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.validate_command_content returns True for valid command.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.validate_command_content detects non-printable characters.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.validate_command_content allows newline, tab, and space.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Validate command for security threats.          Performs comprehensive security** (1 connections) — `server/validators/command_validator.py`

## Relationships

- [Server Validators (4)](Server_Validators_%284%29.md) (6 shared connections)
- [Server Commands (5)](Server_Commands_%285%29.md) (2 shared connections)
- [Server Commands (3)](Server_Commands_%283%29.md) (1 shared connections)
- [Server Validators (10)](Server_Validators_%2810%29.md) (1 shared connections)

## Source Files

- `server/tests/unit/validators/test_command_validator.py`
- `server/validators/command_validator.py`

## Audit Trail

- EXTRACTED: 36 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*