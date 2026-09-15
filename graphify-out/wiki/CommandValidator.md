# CommandValidator

> 58 nodes

## Key Concepts

- **CommandValidator** (40 connections) — `server/validators/command_validator.py`
- **.validate_command_content()** (11 connections) — `server/validators/command_validator.py`
- **.validate_expanded_command()** (8 connections) — `server/validators/command_validator.py`
- **.sanitize_for_logging()** (7 connections) — `server/validators/command_validator.py`
- **.validate_alias_definition()** (7 connections) — `server/validators/command_validator.py`
- **.extract_command_name()** (5 connections) — `server/validators/command_validator.py`
- **test_command_validator_extract_command_name()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_extract_command_name_empty()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_extract_command_name_with_slash()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_is_valid_command_name()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_is_valid_command_name_invalid()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_sanitize_for_logging()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_sanitize_for_logging_removes_sensitive()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_sanitize_for_logging_truncates()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_validate_alias_definition_inherits_content_validation()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_validate_alias_definition_length_limit()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_validate_alias_definition_valid()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_validate_alias_definition_within_limit()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_validate_command_content_allows_newline_tab_space()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_validate_command_content_dangerous_pattern()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_validate_command_content_non_printable()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_validate_command_content_null_byte()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_validate_command_content_too_long()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_validate_command_content_valid()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_validate_expanded_command_inherits_content_validation()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- *... and 33 more nodes in this community*

## Relationships

- [test_command_validator.py](test_command_validator.py.md) (23 shared connections)
- [test_command_processing.py](test_command_processing.py.md) (6 shared connections)
- [command_handler_unified.py](command_handler_unified.py.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [_validate_command_basics](_validate_command_basics.md) (2 shared connections)
- [_prepare_command_for_processing](_prepare_command_for_processing.md) (1 shared connections)

## Source Files

- `server/tests/unit/validators/test_command_validator.py`
- `server/validators/command_validator.py`

## Audit Trail

- EXTRACTED: 92 (78%)
- INFERRED: 26 (22%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*