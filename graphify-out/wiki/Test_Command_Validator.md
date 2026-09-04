# Test Command Validator

> 124 nodes

## Key Concepts

- **test_command_validator.py** (52 connections) — `server/tests/unit/validators/test_command_validator.py`
- **CommandValidator** (39 connections) — `server/validators/command_validator.py`
- **comprehensive_sanitize_input()** (20 connections) — `server/validators/security_validator.py`
- **command_validator.py** (17 connections) — `server/validators/command_validator.py`
- **strip_ansi_codes()** (11 connections) — `server/validators/security_validator.py`
- **.validate_command_content()** (10 connections) — `server/validators/command_validator.py`
- **clean_command_input()** (9 connections) — `server/validators/command_validator.py`
- **.is_security_sensitive()** (9 connections) — `server/validators/command_validator.py`
- **validate_command_format()** (9 connections) — `server/validators/command_validator.py`
- **sanitize_unicode_input()** (9 connections) — `server/validators/security_validator.py`
- **server/validators/__init__.py** (9 connections) — `server/validators/__init__.py`
- **.validate_expanded_command()** (8 connections) — `server/validators/command_validator.py`
- **is_suspicious_input()** (8 connections) — `server/validators/command_validator.py`
- **normalize_command()** (8 connections) — `server/validators/command_validator.py`
- **.validate_alias_definition()** (7 connections) — `server/validators/command_validator.py`
- **validate_command_length()** (7 connections) — `server/validators/command_validator.py`
- **.sanitize_for_logging()** (6 connections) — `server/validators/command_validator.py`
- **.extract_command_name()** (5 connections) — `server/validators/command_validator.py`
- **test_command_validator_extract_command_name()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_extract_command_name_empty()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_extract_command_name_with_slash()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_is_security_sensitive_admin()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_is_security_sensitive_case_insensitive()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_is_security_sensitive_empty()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_command_validator_is_security_sensitive_non_sensitive()** (4 connections) — `server/tests/unit/validators/test_command_validator.py`
- *... and 99 more nodes in this community*

## Relationships

- [Security Validators](Security_Validators.md) (22 shared connections)
- [Processing](Processing.md) (8 shared connections)
- [Command Aliases](Command_Aliases.md) (6 shared connections)
- [Alias Graph](Alias_Graph.md) (3 shared connections)
- [Test Command Input](Test_Command_Input.md) (2 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (2 shared connections)
- [Test Command Aliases](Test_Command_Aliases.md) (1 shared connections)

## Source Files

- `server/tests/unit/validators/test_command_validator.py`
- `server/validators/__init__.py`
- `server/validators/command_validator.py`
- `server/validators/security_validator.py`

## Audit Trail

- EXTRACTED: 230 (90%)
- INFERRED: 26 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*