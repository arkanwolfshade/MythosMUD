# E 2 E Scenarios Scenario

> 8 nodes

## Key Concepts

- **.sanitize_for_logging()** (7 connections) — `server/validators/command_validator.py`
- **test_command_validator_sanitize_for_logging()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_sanitize_for_logging_truncates()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_sanitize_for_logging_removes_sensitive()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.sanitize_for_logging sanitizes command for logging.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.sanitize_for_logging truncates long commands.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.sanitize_for_logging removes sensitive patterns.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Sanitize command for safe logging.          Truncates and removes sensitive data** (1 connections) — `server/validators/command_validator.py`

## Relationships

- [Persistence Container Extended](Persistence_Container_Extended.md) (3 shared connections)
- [Manager Services Nats](Manager_Services_Nats.md) (1 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (1 shared connections)
- [Client Event Store](Client_Event_Store.md) (1 shared connections)

## Source Files

- `server/tests/unit/validators/test_command_validator.py`
- `server/validators/command_validator.py`

## Audit Trail

- EXTRACTED: 20 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*