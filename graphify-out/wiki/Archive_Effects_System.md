# Archive Effects System

> 8 nodes

## Key Concepts

- **.extract_command_name()** (5 connections) — `server/validators/command_validator.py`
- **test_command_validator_extract_command_name()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_extract_command_name_with_slash()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_extract_command_name_empty()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.extract_command_name extracts command name.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.extract_command_name handles slash prefix.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.extract_command_name returns None for empty command.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Extract the base command name from a command string.          Handles various fo** (1 connections) — `server/validators/command_validator.py`

## Relationships

- [Persistence Container Extended](Persistence_Container_Extended.md) (3 shared connections)
- [Client Event Store](Client_Event_Store.md) (1 shared connections)

## Source Files

- `server/tests/unit/validators/test_command_validator.py`
- `server/validators/command_validator.py`

## Audit Trail

- EXTRACTED: 18 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*