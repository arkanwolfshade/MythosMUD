# holidays

> 8 nodes

## Key Concepts

- **.sanitize_for_logging()** (6 connections) — `server/validators/command_validator.py`
- **test_command_validator_sanitize_for_logging()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_sanitize_for_logging_removes_sensitive()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_sanitize_for_logging_truncates()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.sanitize_for_logging sanitizes command for logging.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.sanitize_for_logging truncates long commands.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.sanitize_for_logging removes sensitive patterns.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Sanitize command for safe logging. Truncates and removes sensitive data before…** (1 connections) — `server/validators/command_validator.py`

## Relationships

- [test_room_service.py](test_room_service.py.md) (4 shared connections)
- [subject_controller.py](subject_controller.py.md) (3 shared connections)
- [PeriodicOrphanAuditor](PeriodicOrphanAuditor.md) (1 shared connections)

## Source Files

- `server/tests/unit/validators/test_command_validator.py`
- `server/validators/command_validator.py`

## Audit Trail

- EXTRACTED: 12 (80%)
- INFERRED: 3 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*