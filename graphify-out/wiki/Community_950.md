# Community 950

> 16 nodes

## Key Concepts

- **CommandValidator** (36 connections) — `server/validators/command_validator.py`
- **.validate_command_content()** (10 connections) — `server/validators/command_validator.py`
- **test_command_validator_validate_command_content_allows_newline_tab_space()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_validate_command_content_dangerous_pattern()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_validate_command_content_non_printable()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_validate_command_content_null_byte()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_validate_command_content_too_long()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_validate_command_content_valid()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.validate_command_content returns True for valid command.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.validate_command_content detects null bytes.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.validate_command_content detects dangerous patterns.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.validate_command_content detects excessive length.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.validate_command_content detects non-printable characters.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.validate_command_content allows newline, tab, and space.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Enhanced command security validation to prevent injection attacks. Implements…** (1 connections) — `server/validators/command_validator.py`
- **Validate command for security threats. Performs comprehensive security checks…** (1 connections) — `server/validators/command_validator.py`

## Relationships

- [Community 851](Community_851.md) (7 shared connections)
- [Community 1234](Community_1234.md) (6 shared connections)
- [Community 1235](Community_1235.md) (6 shared connections)
- [Community 1236](Community_1236.md) (5 shared connections)
- [Community 1342](Community_1342.md) (4 shared connections)
- [Community 1343](Community_1343.md) (4 shared connections)
- [Community 1449](Community_1449.md) (3 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (1 shared connections)

## Source Files

- `server/tests/unit/validators/test_command_validator.py`
- `server/validators/command_validator.py`

## Audit Trail

- EXTRACTED: 31 (54%)
- INFERRED: 26 (46%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*