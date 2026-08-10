# Logging Structured Processors

> 10 nodes

## Key Concepts

- **normalize_command()** (8 connections) — `server/validators/command_validator.py`
- **test_normalize_command_no_slash()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_normalize_command_with_slash()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_normalize_command_empty()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_normalize_command_whitespace()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test normalizing command without slash prefix.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test normalizing command with slash prefix.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test normalizing empty command.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test normalizing command with whitespace.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Normalize command input by removing optional slash prefix.      Supports both tr** (1 connections) — `server/validators/command_validator.py`

## Relationships

- [Persistence Container Extended](Persistence_Container_Extended.md) (5 shared connections)
- [E 2 E Load Readme](E_2_E_Load_Readme.md) (1 shared connections)
- [Client Event Store](Client_Event_Store.md) (1 shared connections)

## Source Files

- `server/tests/unit/validators/test_command_validator.py`
- `server/validators/command_validator.py`

## Audit Trail

- EXTRACTED: 25 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*