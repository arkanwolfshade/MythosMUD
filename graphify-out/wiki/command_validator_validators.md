# command validator validators

> 98 nodes

## Key Concepts

- **test_command_validator.py** (52 connections) — `server/tests/unit/validators/test_command_validator.py`
- **.validate_command_content()** (11 connections) — `server/validators/command_validator.py`
- **validate_command_format()** (9 connections) — `server/validators/command_validator.py`
- **.validate_expanded_command()** (8 connections) — `server/validators/command_validator.py`
- **validate_command_length()** (7 connections) — `server/validators/command_validator.py`
- **.validate_alias_definition()** (7 connections) — `server/validators/command_validator.py`
- **.extract_command_name()** (5 connections) — `server/validators/command_validator.py`
- **.is_valid_command_name()** (4 connections) — `server/validators/command_validator.py`
- **test_normalize_command_no_slash()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_normalize_command_with_slash()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_normalize_command_empty()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_normalize_command_whitespace()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_is_suspicious_input_safe()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_is_suspicious_input_sql_injection()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_is_suspicious_input_xss()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_clean_command_input_basic()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_clean_command_input_whitespace()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_clean_command_input_empty()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_clean_command_input_unicode()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_validate_command_length_valid()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_validate_command_length_too_long()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_validate_command_length_custom_max()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_validate_command_format_valid()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_validate_command_format_empty()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_validate_command_format_suspicious()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- *... and 73 more nodes in this community*

## Relationships

- [command communication models](command_communication_models.md) (15 shared connections)
- [command inventory factories](command_inventory_factories.md) (13 shared connections)
- [logoutHandler logger App](logoutHandler_logger_App.md) (3 shared connections)
- [command commands handler](command_commands_handler.md) (2 shared connections)

## Source Files

- `server/tests/unit/validators/test_command_validator.py`
- `server/validators/command_validator.py`

## Audit Trail

- EXTRACTED: 275 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*