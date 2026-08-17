# test_command_validator.py

> 114 nodes

## Key Concepts

- **test_command_validator.py** (52 connections) — `server/tests/unit/validators/test_command_validator.py`
- **CommandValidator** (40 connections) — `server/validators/command_validator.py`
- **.validate_command_content()** (11 connections) — `server/validators/command_validator.py`
- **.is_security_sensitive()** (9 connections) — `server/validators/command_validator.py`
- **validate_command_format()** (9 connections) — `server/validators/command_validator.py`
- **.validate_expanded_command()** (8 connections) — `server/validators/command_validator.py`
- **is_suspicious_input()** (8 connections) — `server/validators/command_validator.py`
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
- *... and 89 more nodes in this community*

## Relationships

- [AliasStorage](AliasStorage.md) (10 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (7 shared connections)
- [test_command_processing.py](test_command_processing.py.md) (4 shared connections)
- [TestHelperFunctions](TestHelperFunctions.md) (2 shared connections)
- [test_alias_expansion.py](test_alias_expansion.py.md) (1 shared connections)

## Source Files

- `server/tests/unit/validators/test_command_validator.py`
- `server/validators/command_validator.py`

## Audit Trail

- EXTRACTED: 181 (87%)
- INFERRED: 26 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*