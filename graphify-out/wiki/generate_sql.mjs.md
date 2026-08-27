# generate_sql.mjs

> 10 nodes

## Key Concepts

- **.is_security_sensitive()** (9 connections) — `server/validators/command_validator.py`
- **test_command_validator_is_security_sensitive_admin()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_is_security_sensitive_case_insensitive()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_is_security_sensitive_empty()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_is_security_sensitive_non_sensitive()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.is_security_sensitive detects admin commands.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.is_security_sensitive is case-insensitive.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.is_security_sensitive returns False for non-sensitive…** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.is_security_sensitive returns False for empty command.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Check if command requires audit logging. Identifies commands that should be…** (1 connections) — `server/validators/command_validator.py`

## Relationships

- [test_room_service.py](test_room_service.py.md) (5 shared connections)
- [subject_controller.py](subject_controller.py.md) (4 shared connections)
- [PeriodicOrphanAuditor](PeriodicOrphanAuditor.md) (3 shared connections)

## Source Files

- `server/tests/unit/validators/test_command_validator.py`
- `server/validators/command_validator.py`

## Audit Trail

- EXTRACTED: 17 (81%)
- INFERRED: 4 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*