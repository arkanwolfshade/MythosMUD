# Security Validator Tests

> 222 nodes

## Key Concepts

- **test_security_validator.py** (97 connections) — `server/tests/unit/validators/test_security_validator.py`
- **validate_player_name()** (23 connections) — `server/validators/security_validator.py`
- **validate_message_content()** (21 connections) — `server/validators/security_validator.py`
- **comprehensive_sanitize_input()** (20 connections) — `server/validators/security_validator.py`
- **validate_combat_target()** (15 connections) — `server/validators/security_validator.py`
- **strip_ansi_codes()** (13 connections) — `server/validators/security_validator.py`
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
- **.validate_target()** (3 connections) — `server/models/command_combat.py`
- **.validate_target()** (3 connections) — `server/models/command_combat.py`
- **.validate_action()** (3 connections) — `server/models/command_communication.py`
- *... and 197 more nodes in this community*

## Relationships

- [command factories create](command_factories_create.md) (42 shared connections)
- [command communication models](command_communication_models.md) (9 shared connections)
- [command validator validators](command_validator_validators.md) (5 shared connections)
- [commands who helpers](commands_who_helpers.md) (4 shared connections)
- [command commands talk](command_commands_talk.md) (3 shared connections)
- [commands whisper command](commands_whisper_command.md) (2 shared connections)
- [auth endpoints rationale](auth_endpoints_rationale.md) (2 shared connections)
- [admin auth service](admin_auth_service.md) (2 shared connections)
- [Loot Generation](Loot_Generation.md) (1 shared connections)
- [logoutHandler logger App](logoutHandler_logger_App.md) (1 shared connections)
- [combat services initialization](combat_services_initialization.md) (1 shared connections)
- [commands npc admin](commands_npc_admin.md) (1 shared connections)

## Source Files

- `server/models/command_alias.py`
- `server/models/command_combat.py`
- `server/models/command_communication.py`
- `server/models/command_moderation.py`
- `server/models/command_utility.py`
- `server/tests/unit/validators/test_security_validator.py`
- `server/validators/security_validator.py`

## Audit Trail

- EXTRACTED: 673 (99%)
- INFERRED: 10 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*