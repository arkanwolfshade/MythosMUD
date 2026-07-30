# ContainerDataCore

> 44 nodes

## Key Concepts

- **CommandValidator** (14 connections) — `server/validators/command_validator.py`
- **.validate_command_content()** (11 connections) — `server/validators/command_validator.py`
- **.validate_expanded_command()** (8 connections) — `server/validators/command_validator.py`
- **.validate_alias_definition()** (7 connections) — `server/validators/command_validator.py`
- **validate_expanded_command()** (6 connections) — `server/command_handler/alias_expansion.py`
- **.is_valid_command_name()** (4 connections) — `server/validators/command_validator.py`
- **test_command_validator_validate_command_content_valid()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_validate_command_content_null_byte()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_validate_command_content_dangerous_pattern()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_validate_command_content_too_long()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_validate_command_content_non_printable()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_validate_command_content_allows_newline_tab_space()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_validate_expanded_command_valid()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_validate_expanded_command_inherits_content_validation()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_validate_expanded_command_length_limit()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_validate_expanded_command_within_limit()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_validate_alias_definition_valid()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_validate_alias_definition_inherits_content_validation()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_validate_alias_definition_length_limit()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_validate_alias_definition_within_limit()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_is_valid_command_name()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_is_valid_command_name_invalid()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Validate an expanded command for length and content.      Args:         expanded** (1 connections) — `server/command_handler/alias_expansion.py`
- **Test CommandValidator.validate_command_content returns True for valid command.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.validate_command_content detects null bytes.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- *... and 19 more nodes in this community*

## Relationships

- [Validate an expanded command for](Validate_an_expanded_command_for.md) (19 shared connections)
- [check alias safety()](check_alias_safety%28%29.md) (4 shared connections)
- [test alias graph](test_alias_graph.md) (2 shared connections)
- [test movement service](test_movement_service.md) (2 shared connections)
- [CommandExecutionRequest](CommandExecutionRequest.md) (1 shared connections)
- [.get uuid mapping()](get_uuid_mapping%28%29.md) (1 shared connections)
- [.validate topic()](validate_topic%28%29.md) (1 shared connections)

## Source Files

- `server/command_handler/alias_expansion.py`
- `server/tests/unit/validators/test_command_validator.py`
- `server/validators/command_validator.py`

## Audit Trail

- EXTRACTED: 120 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*