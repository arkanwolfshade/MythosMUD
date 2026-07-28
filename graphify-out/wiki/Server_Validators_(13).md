# Server Validators (13)

> 9 nodes

## Key Concepts

- **normalize_command()** (8 connections) — `server/validators/command_validator.py`
- **test_normalize_command_no_slash()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_normalize_command_with_slash()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_normalize_command_empty()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_normalize_command_whitespace()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test normalizing command without slash prefix.** (2 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test normalizing empty command.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test normalizing command with whitespace.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Normalize command input by removing optional slash prefix.      Supports both tr** (1 connections) — `server/validators/command_validator.py`

## Relationships

- [Server Validators (4)](Server_Validators_%284%29.md) (5 shared connections)
- [Server Commands (5)](Server_Commands_%285%29.md) (1 shared connections)
- [Server Commands](Server_Commands.md) (1 shared connections)

## Source Files

- `server/tests/unit/validators/test_command_validator.py`
- `server/validators/command_validator.py`

## Audit Trail

- EXTRACTED: 25 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*