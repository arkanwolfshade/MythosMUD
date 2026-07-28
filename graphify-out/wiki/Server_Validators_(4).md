# Server Validators (4)

> 28 nodes

## Key Concepts

- **test_command_validator.py** (52 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_is_suspicious_input_sql_injection()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_is_suspicious_input_xss()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_clean_command_input_basic()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_clean_command_input_whitespace()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_clean_command_input_empty()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_clean_command_input_unicode()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_validate_expanded_command_valid()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_validate_expanded_command_inherits_content_validation()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_validate_expanded_command_length_limit()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_validate_expanded_command_within_limit()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_sanitize_for_logging()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_sanitize_for_logging_truncates()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_sanitize_for_logging_removes_sensitive()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Unit tests for command validator.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test that SQL injection patterns are detected.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test that XSS patterns are detected.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test cleaning basic command input.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test cleaning command with extra whitespace.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test cleaning empty command.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test cleaning command with unicode characters.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.validate_expanded_command returns True for valid expanded** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.validate_expanded_command inherits content validation.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.validate_expanded_command enforces expanded length limit.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test CommandValidator.validate_expanded_command allows commands within expanded** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- *... and 3 more nodes in this community*

## Relationships

- [Server Commands (5)](Server_Commands_%285%29.md) (16 shared connections)
- [Server Validators (9)](Server_Validators_%289%29.md) (6 shared connections)
- [Server Validators (13)](Server_Validators_%2813%29.md) (5 shared connections)
- [Server Validators (12)](Server_Validators_%2812%29.md) (5 shared connections)
- [Server Validators (17)](Server_Validators_%2817%29.md) (4 shared connections)
- [Server Validators (10)](Server_Validators_%2810%29.md) (4 shared connections)
- [Server Validators (16)](Server_Validators_%2816%29.md) (4 shared connections)
- [Server Validators (18)](Server_Validators_%2818%29.md) (3 shared connections)
- [Server Validators (21)](Server_Validators_%2821%29.md) (2 shared connections)
- [Server Validators (24)](Server_Validators_%2824%29.md) (1 shared connections)
- [Server Commands](Server_Commands.md) (1 shared connections)

## Source Files

- `server/tests/unit/validators/test_command_validator.py`

## Audit Trail

- EXTRACTED: 105 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*