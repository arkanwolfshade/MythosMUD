# Security Validator Tests

> 223 nodes

## Key Concepts

- **test_security_validator.py** (96 connections) — `server/tests/unit/validators/test_security_validator.py`
- **security_validator.py** (34 connections) — `server/validators/security_validator.py`
- **validate_player_name()** (23 connections) — `server/validators/security_validator.py`
- **validate_message_content()** (21 connections) — `server/validators/security_validator.py`
- **comprehensive_sanitize_input()** (20 connections) — `server/validators/security_validator.py`
- **validate_combat_target()** (14 connections) — `server/validators/security_validator.py`
- **validate_action_content()** (11 connections) — `server/validators/security_validator.py`
- **validate_alias_name()** (10 connections) — `server/validators/security_validator.py`
- **validate_reason_content()** (10 connections) — `server/validators/security_validator.py`
- **sanitize_unicode_input()** (9 connections) — `server/validators/security_validator.py`
- **validate_command_content()** (9 connections) — `server/validators/security_validator.py`
- **validate_pose_content()** (9 connections) — `server/validators/security_validator.py`
- **validate_filter_name()** (8 connections) — `server/validators/security_validator.py`
- **validate_target_player()** (8 connections) — `server/validators/security_validator.py`
- **validate_help_topic()** (8 connections) — `server/validators/security_validator.py`
- **validate_security_comprehensive()** (8 connections) — `server/validators/security_validator.py`
- **check_dangerous_characters()** (6 connections) — `server/validators/security_validator.py`
- **check_injection_patterns()** (6 connections) — `server/validators/security_validator.py`
- **get_dangerous_characters()** (5 connections) — `server/validators/security_validator.py`
- **get_injection_patterns()** (5 connections) — `server/validators/security_validator.py`
- **.validate_alias_name_field()** (3 connections) — `server/models/command_alias.py`
- **.validate_command()** (3 connections) — `server/models/command_alias.py`
- **.validate_alias_name_field()** (3 connections) — `server/models/command_alias.py`
- **.validate_target()** (3 connections) — `server/models/command_combat.py`
- **.validate_target()** (3 connections) — `server/models/command_combat.py`
- *... and 198 more nodes in this community*

## Relationships

- [command utility models](command_utility_models.md) (20 shared connections)
- [command communication models](command_communication_models.md) (14 shared connections)
- [commands alias rationale](commands_alias_rationale.md) (12 shared connections)
- [command models moderation](command_models_moderation.md) (7 shared connections)
- [command validator validators](command_validator_validators.md) (6 shared connections)
- [command combat models](command_combat_models.md) (4 shared connections)
- [command models admin](command_models_admin.md) (4 shared connections)

## Source Files

- `server/models/command_alias.py`
- `server/models/command_combat.py`
- `server/models/command_communication.py`
- `server/models/command_moderation.py`
- `server/models/command_utility.py`
- `server/tests/unit/validators/test_security_validator.py`
- `server/validators/security_validator.py`

## Audit Trail

- EXTRACTED: 685 (97%)
- INFERRED: 18 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*