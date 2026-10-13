# Community 1344

> 8 nodes

## Key Concepts

- **is_suspicious_input()** (8 connections) — `server/validators/command_validator.py`
- **test_is_suspicious_input_safe()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_is_suspicious_input_sql_injection()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_is_suspicious_input_xss()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test that safe commands are not flagged as suspicious.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test that SQL injection patterns are detected.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test that XSS patterns are detected.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Check if command contains suspicious patterns that might indicate injection…** (1 connections) — `server/validators/command_validator.py`

## Relationships

- [Community 851](Community_851.md) (4 shared connections)
- [Community 1284](Community_1284.md) (1 shared connections)
- [Command Alias Models](Command_Alias_Models.md) (1 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (1 shared connections)

## Source Files

- `server/tests/unit/validators/test_command_validator.py`
- `server/validators/command_validator.py`

## Audit Trail

- EXTRACTED: 14 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*