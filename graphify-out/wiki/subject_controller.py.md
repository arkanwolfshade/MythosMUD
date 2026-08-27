# subject_controller.py

> 42 nodes

## Key Concepts

- **test_command_validator.py** (52 connections) — `server/tests/unit/validators/test_command_validator.py`
- **validate_command_format()** (9 connections) — `server/validators/command_validator.py`
- **normalize_command()** (8 connections) — `server/validators/command_validator.py`
- **validate_command_length()** (7 connections) — `server/validators/command_validator.py`
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
- **Test normalizing command without slash prefix.** (2 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Unit tests for command validator.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- *... and 17 more nodes in this community*

## Relationships

- [test_room_service.py](test_room_service.py.md) (13 shared connections)
- [WebSocketRequestContext](WebSocketRequestContext.md) (11 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (4 shared connections)
- [apply_migration](apply_migration.md) (4 shared connections)
- [generate_sql.mjs](generate_sql.mjs.md) (4 shared connections)
- [holidays](holidays.md) (3 shared connections)
- [schedules](schedules.md) (3 shared connections)

## Source Files

- `server/tests/unit/validators/test_command_validator.py`
- `server/validators/command_validator.py`

## Audit Trail

- EXTRACTED: 97 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*