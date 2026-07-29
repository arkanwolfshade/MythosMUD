# Validate an expanded command for

> 110 nodes

## Key Concepts

- **test_command_validator.py** (52 connections) — `server/tests/unit/validators/test_command_validator.py`
- **command_validator.py** (17 connections) — `server/validators/command_validator.py`
- **command_input.py** (14 connections) — `server/command_handler/command_input.py`
- **CommandValidator** (14 connections) — `server/validators/command_validator.py`
- **.validate_command_content()** (11 connections) — `server/validators/command_validator.py`
- **__init__.py** (9 connections) — `server/validators/__init__.py`
- **clean_command_input()** (9 connections) — `server/validators/command_validator.py`
- **validate_command_format()** (9 connections) — `server/validators/command_validator.py`
- **normalize_command()** (8 connections) — `server/validators/command_validator.py`
- **is_suspicious_input()** (8 connections) — `server/validators/command_validator.py`
- **.validate_expanded_command()** (8 connections) — `server/validators/command_validator.py`
- **validate_command_length()** (7 connections) — `server/validators/command_validator.py`
- **.validate_alias_definition()** (7 connections) — `server/validators/command_validator.py`
- **.sanitize_for_logging()** (7 connections) — `server/validators/command_validator.py`
- **validate_expanded_command()** (6 connections) — `server/command_handler/alias_expansion.py`
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
- *... and 85 more nodes in this community*

## Relationships

- [processing](processing.md) (8 shared connections)
- [.validate topic()](validate_topic%28%29.md) (7 shared connections)
- [clean command input()](clean_command_input%28%29.md) (5 shared connections)
- [main()](main%28%29.md) (5 shared connections)
- [Any](Any.md) (4 shared connections)
- [check alias safety()](check_alias_safety%28%29.md) (4 shared connections)
- [CommandExecutionRequest](CommandExecutionRequest.md) (2 shared connections)
- [Test validate command basics returns](Test_validate_command_basics_returns.md) (2 shared connections)
- [initialize nats and combat services()](initialize_nats_and_combat_services%28%29.md) (1 shared connections)

## Source Files

- `server/command_handler/alias_expansion.py`
- `server/command_handler/command_input.py`
- `server/tests/unit/validators/test_command_validator.py`
- `server/validators/__init__.py`
- `server/validators/command_validator.py`

## Audit Trail

- EXTRACTED: 372 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*