# Cursor Plans Room

> 6 nodes

## Key Concepts

- **.is_valid_command_name()** (4 connections) — `server/validators/command_validator.py`
- **test_command_validator_is_valid_command_name()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_is_valid_command_name_invalid()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.is_valid_command_name validates command names.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.is_valid_command_name rejects invalid names.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Check if a string is a valid command/alias name.          Valid names:         -** (1 connections) — `server/validators/command_validator.py`

## Relationships

- [Persistence Container Extended](Persistence_Container_Extended.md) (2 shared connections)
- [Client Event Store](Client_Event_Store.md) (1 shared connections)

## Source Files

- `server/tests/unit/validators/test_command_validator.py`
- `server/validators/command_validator.py`

## Audit Trail

- EXTRACTED: 13 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*