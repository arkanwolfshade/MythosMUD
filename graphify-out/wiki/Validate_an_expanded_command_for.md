# Validate an expanded command for

> 66 nodes

## Key Concepts

- **test_command_validator.py** (52 connections) — `server/tests/unit/validators/test_command_validator.py`
- **command_validator.py** (17 connections) — `server/validators/command_validator.py`
- **__init__.py** (9 connections) — `server/validators/__init__.py`
- **clean_command_input()** (9 connections) — `server/validators/command_validator.py`
- **validate_command_format()** (9 connections) — `server/validators/command_validator.py`
- **normalize_command()** (8 connections) — `server/validators/command_validator.py`
- **is_suspicious_input()** (8 connections) — `server/validators/command_validator.py`
- **validate_command_length()** (7 connections) — `server/validators/command_validator.py`
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
- *... and 41 more nodes in this community*

## Relationships

- [ContainerDataCore](ContainerDataCore.md) (21 shared connections)
- [.validate topic()](validate_topic%28%29.md) (6 shared connections)
- [test movement service](test_movement_service.md) (5 shared connections)
- [Player Position Service](Player_Position_Service.md) (2 shared connections)
- [world](world.md) (2 shared connections)
- [.get uuid mapping()](get_uuid_mapping%28%29.md) (1 shared connections)
- [check alias safety()](check_alias_safety%28%29.md) (1 shared connections)

## Source Files

- `server/tests/unit/validators/test_command_validator.py`
- `server/validators/__init__.py`
- `server/validators/command_validator.py`

## Audit Trail

- EXTRACTED: 230 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*