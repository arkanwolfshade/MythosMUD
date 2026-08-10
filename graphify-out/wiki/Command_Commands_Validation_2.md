# Command Commands Validation

> 10 nodes

## Key Concepts

- **.validate_alias_definition()** (7 connections) — `server/validators/command_validator.py`
- **test_command_validator_validate_alias_definition_valid()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_validate_alias_definition_inherits_content_validation()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_validate_alias_definition_length_limit()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_validate_alias_definition_within_limit()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.validate_alias_definition returns True for valid alias.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.validate_alias_definition inherits content validation.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.validate_alias_definition enforces alias length limit.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.validate_alias_definition allows aliases within limit.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Validate alias definition command.          Applies validation to alias commands** (1 connections) — `server/validators/command_validator.py`

## Relationships

- [Persistence Container Extended](Persistence_Container_Extended.md) (4 shared connections)
- [Client Event Store](Client_Event_Store.md) (1 shared connections)
- [Look Command Helpers](Look_Command_Helpers.md) (1 shared connections)

## Source Files

- `server/tests/unit/validators/test_command_validator.py`
- `server/validators/command_validator.py`

## Audit Trail

- EXTRACTED: 24 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*