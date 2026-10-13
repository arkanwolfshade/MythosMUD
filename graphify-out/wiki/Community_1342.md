# Community 1342

> 8 nodes

## Key Concepts

- **.sanitize_for_logging()** (5 connections) — `server/validators/command_validator.py`
- **test_command_validator_sanitize_for_logging()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_sanitize_for_logging_removes_sensitive()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_sanitize_for_logging_truncates()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.sanitize_for_logging sanitizes command for logging.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.sanitize_for_logging truncates long commands.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.sanitize_for_logging removes sensitive patterns.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Sanitize command for safe logging. Truncates and removes sensitive data before…** (1 connections) — `server/validators/command_validator.py`

## Relationships

- [Community 950](Community_950.md) (4 shared connections)
- [Community 851](Community_851.md) (3 shared connections)

## Source Files

- `server/tests/unit/validators/test_command_validator.py`
- `server/validators/command_validator.py`

## Audit Trail

- EXTRACTED: 11 (79%)
- INFERRED: 3 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*