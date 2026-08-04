# command validator validators

> 120 nodes

## Key Concepts

- **test_command_validator.py** (52 connections) — `server/tests/unit/validators/test_command_validator.py`
- **command_validator.py** (17 connections) — `server/validators/command_validator.py`
- **CommandValidator** (14 connections) — `server/validators/command_validator.py`
- **.validate_command_content()** (11 connections) — `server/validators/command_validator.py`
- **__init__.py** (9 connections) — `server/validators/__init__.py`
- **clean_command_input()** (9 connections) — `server/validators/command_validator.py`
- **validate_command_format()** (9 connections) — `server/validators/command_validator.py`
- **.is_security_sensitive()** (9 connections) — `server/validators/command_validator.py`
- **normalize_command()** (8 connections) — `server/validators/command_validator.py`
- **is_suspicious_input()** (8 connections) — `server/validators/command_validator.py`
- **.validate_expanded_command()** (8 connections) — `server/validators/command_validator.py`
- **validate_command_length()** (7 connections) — `server/validators/command_validator.py`
- **.validate_alias_definition()** (7 connections) — `server/validators/command_validator.py`
- **.sanitize_for_logging()** (7 connections) — `server/validators/command_validator.py`
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
- *... and 95 more nodes in this community*

## Relationships

- [Security Validator Tests](Security_Validator_Tests.md) (5 shared connections)
- [command commands handler](command_commands_handler.md) (4 shared connections)
- [logoutHandler logger App](logoutHandler_logger_App.md) (4 shared connections)
- [fixtures mock helpers](fixtures_mock_helpers.md) (3 shared connections)
- [command factories create](command_factories_create.md) (2 shared connections)
- [commands recovery lucidity](commands_recovery_lucidity.md) (2 shared connections)
- [Loot Generation](Loot_Generation.md) (2 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)

## Source Files

- `server/tests/unit/validators/test_command_validator.py`
- `server/validators/__init__.py`
- `server/validators/command_validator.py`

## Audit Trail

- EXTRACTED: 376 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*