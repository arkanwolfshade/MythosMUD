# test_security_validator.py

> 187 nodes

## Key Concepts

- **test_security_validator.py** (101 connections) — `server/tests/unit/validators/test_security_validator.py`
- **validate_player_name()** (30 connections) — `server/validators/security_validator.py`
- **validate_message_content()** (22 connections) — `server/validators/security_validator.py`
- **validate_combat_target()** (15 connections) — `server/validators/security_validator.py`
- **validate_alias_name()** (10 connections) — `server/validators/security_validator.py`
- **validate_filter_name()** (8 connections) — `server/validators/security_validator.py`
- **validate_help_topic()** (8 connections) — `server/validators/security_validator.py`
- **validate_security_comprehensive()** (8 connections) — `server/validators/security_validator.py`
- **validate_target_player()** (8 connections) — `server/validators/security_validator.py`
- **check_dangerous_characters()** (6 connections) — `server/validators/security_validator.py`
- **check_injection_patterns()** (6 connections) — `server/validators/security_validator.py`
- **get_dangerous_characters()** (5 connections) — `server/validators/security_validator.py`
- **get_injection_patterns()** (5 connections) — `server/validators/security_validator.py`
- **.validate_target()** (4 connections) — `server/models/command_communication.py`
- **.validate_topic()** (4 connections) — `server/models/command_utility.py`
- **.validate_filter_name_field()** (4 connections) — `server/models/command_utility.py`
- **test_check_dangerous_characters_has_dangerous()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_check_dangerous_characters_no_dangerous()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_check_injection_patterns_has_patterns()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_check_injection_patterns_no_patterns()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_comprehensive_sanitize_input_empty()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_comprehensive_sanitize_input_normal()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_comprehensive_sanitize_input_normalizes_newlines()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_comprehensive_sanitize_input_preserves_tabs()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_comprehensive_sanitize_input_removes_control_chars()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- *... and 162 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (47 shared connections)
- [test_command_communication.py](test_command_communication.py.md) (10 shared connections)
- [test_command_moderation.py](test_command_moderation.py.md) (10 shared connections)
- [command.py](command.py.md) (6 shared connections)
- [test_command_combat.py](test_command_combat.py.md) (6 shared connections)
- [test_command_alias.py](test_command_alias.py.md) (3 shared connections)
- [test_command_admin.py](test_command_admin.py.md) (3 shared connections)
- [AliasStorage](AliasStorage.md) (1 shared connections)
- [PlayerService](PlayerService.md) (1 shared connections)
- [SecureBaseModel](SecureBaseModel.md) (1 shared connections)

## Source Files

- `server/models/command_communication.py`
- `server/models/command_utility.py`
- `server/tests/unit/validators/test_security_validator.py`
- `server/validators/security_validator.py`

## Audit Trail

- EXTRACTED: 321 (98%)
- INFERRED: 7 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*