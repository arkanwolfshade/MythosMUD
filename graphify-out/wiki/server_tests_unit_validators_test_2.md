# server tests unit validators test

> 96 nodes

## Key Concepts

- **test_command_validator.py** (52 connections) — `server/tests/unit/validators/test_command_validator.py`
- **CommandValidator** (40 connections) — `server/validators/command_validator.py`
- **.validate_command_content()** (11 connections) — `server/validators/command_validator.py`
- **.is_security_sensitive()** (9 connections) — `server/validators/command_validator.py`
- **validate_command_format()** (9 connections) — `server/validators/command_validator.py`
- **.validate_expanded_command()** (8 connections) — `server/validators/command_validator.py`
- **normalize_command()** (8 connections) — `server/validators/command_validator.py`
- **.sanitize_for_logging()** (7 connections) — `server/validators/command_validator.py`
- **.validate_alias_definition()** (7 connections) — `server/validators/command_validator.py`
- **validate_command_length()** (7 connections) — `server/validators/command_validator.py`
- **.extract_command_name()** (5 connections) — `server/validators/command_validator.py`
- **test_command_validator_extract_command_name()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_extract_command_name_empty()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_extract_command_name_with_slash()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_is_security_sensitive_admin()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_is_security_sensitive_case_insensitive()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_is_security_sensitive_empty()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_is_security_sensitive_non_sensitive()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_is_valid_command_name()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_is_valid_command_name_invalid()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_sanitize_for_logging()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_sanitize_for_logging_removes_sensitive()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_sanitize_for_logging_truncates()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_validate_alias_definition_inherits_content_validation()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_validate_alias_definition_length_limit()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- *... and 71 more nodes in this community*

## Relationships

- [server tests unit validators test](server_tests_unit_validators_test.md) (16 shared connections)
- [server command handler processing](server_command_handler_processing.md) (5 shared connections)
- [server command handler alias expansion](server_command_handler_alias_expansion.md) (2 shared connections)
- [server command handler unified rationale](server_command_handler_unified_rationale.md) (2 shared connections)
- [server command handler command input](server_command_handler_command_input.md) (1 shared connections)
- [server command handler command execution](server_command_handler_command_execution.md) (1 shared connections)

## Source Files

- `server/tests/unit/validators/test_command_validator.py`
- `server/validators/command_validator.py`

## Audit Trail

- EXTRACTED: 164 (86%)
- INFERRED: 26 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*