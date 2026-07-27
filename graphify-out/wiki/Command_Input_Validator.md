# Command Input Validator

> 92 nodes · cohesion 0.03

## Key Concepts

- **test_command_validator.py** (51 connections) — `server/tests/unit/validators/test_command_validator.py`
- **validate_command_format()** (9 connections) — `server/validators/command_validator.py`
- **is_suspicious_input()** (8 connections) — `server/validators/command_validator.py`
- **normalize_command()** (8 connections) — `server/validators/command_validator.py`
- **validate_command_length()** (7 connections) — `server/validators/command_validator.py`
- **Test CommandValidator.validate_command_content detects null bytes.** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_clean_command_input_basic()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_clean_command_input_empty()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_clean_command_input_unicode()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_clean_command_input_whitespace()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_is_suspicious_input_safe()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_is_suspicious_input_sql_injection()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_is_suspicious_input_xss()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_normalize_command_empty()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_normalize_command_no_slash()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_normalize_command_whitespace()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_normalize_command_with_slash()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_validate_command_format_empty()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_validate_command_format_suspicious()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_validate_command_format_too_long()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_validate_command_format_valid()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_validate_command_length_custom_max()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_validate_command_length_too_long()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_validate_command_length_valid()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test validate_command_format returns False for empty command.** (2 connections) — `server/tests/unit/validators/test_command_validator.py`
- *... and 67 more nodes in this community*

## Relationships

- [[Command Field Validators]] (7 shared connections)
- [[Alias Expansion Logic]] (4 shared connections)
- [[Command Input Utilities]] (1 shared connections)

## Source Files

- `server/tests/unit/validators/test_command_validator.py`
- `server/validators/command_validator.py`

## Audit Trail

- EXTRACTED: 238 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
