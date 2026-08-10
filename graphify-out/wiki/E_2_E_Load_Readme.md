# E 2 E Load Readme

> 10 nodes

## Key Concepts

- **__init__.py** (9 connections) — `server/validators/__init__.py`
- **is_suspicious_input()** (8 connections) — `server/validators/command_validator.py`
- **test_is_suspicious_input_safe()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_is_suspicious_input_sql_injection()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_is_suspicious_input_xss()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test that safe commands are not flagged as suspicious.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test that SQL injection patterns are detected.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test that XSS patterns are detected.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Input validation utilities for MythosMUD.  This package provides validation func** (1 connections) — `server/validators/__init__.py`
- **Check if command contains suspicious patterns that might indicate injection atte** (1 connections) — `server/validators/command_validator.py`

## Relationships

- [Persistence Container Extended](Persistence_Container_Extended.md) (5 shared connections)
- [Client Event Store](Client_Event_Store.md) (3 shared connections)
- [Chat Panel Components](Chat_Panel_Components.md) (3 shared connections)
- [Logging Structured Processors](Logging_Structured_Processors.md) (1 shared connections)
- [E 2 E Bugs Found](E_2_E_Bugs_Found.md) (1 shared connections)

## Source Files

- `server/tests/unit/validators/test_command_validator.py`
- `server/validators/__init__.py`
- `server/validators/command_validator.py`

## Audit Trail

- EXTRACTED: 31 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*