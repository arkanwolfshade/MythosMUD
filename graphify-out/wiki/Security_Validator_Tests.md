# Security Validator Tests

> 193 nodes

## Key Concepts

- **test_security_validator.py** (97 connections) — `server/tests/unit/validators/test_security_validator.py`
- **security_validator.py** (36 connections) — `server/validators/security_validator.py`
- **validate_player_name()** (23 connections) — `server/validators/security_validator.py`
- **validate_message_content()** (21 connections) — `server/validators/security_validator.py`
- **comprehensive_sanitize_input()** (20 connections) — `server/validators/security_validator.py`
- **strip_ansi_codes()** (13 connections) — `server/validators/security_validator.py`
- **validate_action_content()** (11 connections) — `server/validators/security_validator.py`
- **validate_reason_content()** (10 connections) — `server/validators/security_validator.py`
- **__init__.py** (9 connections) — `server/validators/__init__.py`
- **clean_command_input()** (9 connections) — `server/validators/command_validator.py`
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
- **.validate_command()** (3 connections) — `server/models/command_alias.py`
- **.validate_action()** (3 connections) — `server/models/command_communication.py`
- **.validate_pose()** (3 connections) — `server/models/command_communication.py`
- **.validate_target()** (3 connections) — `server/models/command_communication.py`
- *... and 168 more nodes in this community*

## Relationships

- [command communication models](command_communication_models.md) (14 shared connections)
- [container persistence rationale](container_persistence_rationale.md) (11 shared connections)
- [feature services flag](feature_services_flag.md) (9 shared connections)
- [commands who helpers](commands_who_helpers.md) (8 shared connections)
- [command models moderation](command_models_moderation.md) (7 shared connections)
- [command validator validators](command_validator_validators.md) (7 shared connections)
- [models npc rationale](models_npc_rationale.md) (6 shared connections)
- [commands position system](commands_position_system.md) (4 shared connections)
- [calendar schemas validate](calendar_schemas_validate.md) (3 shared connections)
- [auth endpoints rationale](auth_endpoints_rationale.md) (2 shared connections)
- [emote models rationale](emote_models_rationale.md) (1 shared connections)
- [NPC Combat](NPC_Combat.md) (1 shared connections)

## Source Files

- `server/models/command_alias.py`
- `server/models/command_communication.py`
- `server/models/command_moderation.py`
- `server/models/command_utility.py`
- `server/tests/unit/validators/test_security_validator.py`
- `server/validators/__init__.py`
- `server/validators/command_validator.py`
- `server/validators/security_validator.py`

## Audit Trail

- EXTRACTED: 634 (98%)
- INFERRED: 16 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*