# Async Audit Cursor

> 13 nodes

## Key Concepts

- **.is_security_sensitive()** (9 connections) — `server/validators/command_validator.py`
- **_handle_validation_error()** (5 connections) — `server/command_handler/processing.py`
- **test_command_validator_is_security_sensitive_admin()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_is_security_sensitive_case_insensitive()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_is_security_sensitive_non_sensitive()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_is_security_sensitive_empty()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **ValidationError** (2 connections)
- **Handle a validation error during command processing.** (1 connections) — `server/command_handler/processing.py`
- **Test CommandValidator.is_security_sensitive detects admin commands.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.is_security_sensitive is case-insensitive.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.is_security_sensitive returns False for non-sensitive comm** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.is_security_sensitive returns False for empty command.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Check if command requires audit logging.          Identifies commands that shoul** (1 connections) — `server/validators/command_validator.py`

## Relationships

- [Client Event Store](Client_Event_Store.md) (4 shared connections)
- [Persistence Container Extended](Persistence_Container_Extended.md) (4 shared connections)
- [Catatonia Check Logic](Catatonia_Check_Logic.md) (1 shared connections)
- [Manager Services Nats](Manager_Services_Nats.md) (1 shared connections)

## Source Files

- `server/command_handler/processing.py`
- `server/tests/unit/validators/test_command_validator.py`
- `server/validators/command_validator.py`

## Audit Trail

- EXTRACTED: 33 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*