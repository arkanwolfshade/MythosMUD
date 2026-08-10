# Commands Command Handler

> 10 nodes

## Key Concepts

- **.validate_expanded_command()** (8 connections) — `server/validators/command_validator.py`
- **test_command_validator_validate_expanded_command_valid()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_validate_expanded_command_inherits_content_validation()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_validate_expanded_command_length_limit()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_validate_expanded_command_within_limit()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.validate_expanded_command returns True for valid expanded** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.validate_expanded_command inherits content validation.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.validate_expanded_command enforces expanded length limit.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.validate_expanded_command allows commands within expanded** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Validate command after alias expansion.          Uses stricter length limits sin** (1 connections) — `server/validators/command_validator.py`

## Relationships

- [Persistence Container Extended](Persistence_Container_Extended.md) (4 shared connections)
- [Client Event Store](Client_Event_Store.md) (2 shared connections)
- [Look Command Helpers](Look_Command_Helpers.md) (1 shared connections)

## Source Files

- `server/tests/unit/validators/test_command_validator.py`
- `server/validators/command_validator.py`

## Audit Trail

- EXTRACTED: 25 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*