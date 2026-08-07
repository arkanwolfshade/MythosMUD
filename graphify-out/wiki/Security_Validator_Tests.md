# Security Validator Tests

> 193 nodes

## Key Concepts

- **test_security_validator.py** (97 connections) — `server/tests/unit/validators/test_security_validator.py`
- **security_validator.py** (36 connections) — `server/validators/security_validator.py`
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
- **.validate_pose()** (3 connections) — `server/models/command_communication.py`
- *... and 168 more nodes in this community*

## Relationships

- [command communication models](command_communication_models.md) (14 shared connections)
- [health models rationale](health_models_rationale.md) (13 shared connections)
- [dialogue definition persistence](dialogue_definition_persistence.md) (9 shared connections)
- [command validator validators](command_validator_validators.md) (7 shared connections)
- [command processor rationale](command_processor_rationale.md) (6 shared connections)
- [commands who helpers](commands_who_helpers.md) (4 shared connections)
- [combat attack handler](combat_attack_handler.md) (3 shared connections)
- [character creation service](character_creation_service.md) (2 shared connections)
- [commands npc admin](commands_npc_admin.md) (1 shared connections)
- [world models rationale](world_models_rationale.md) (1 shared connections)
- [emote models rationale](emote_models_rationale.md) (1 shared connections)
- [NPC Services Bootstrap](NPC_Services_Bootstrap.md) (1 shared connections)

## Source Files

- `server/models/command_alias.py`
- `server/models/command_combat.py`
- `server/models/command_communication.py`
- `server/models/command_utility.py`
- `server/tests/unit/validators/test_security_validator.py`
- `server/validators/security_validator.py`

## Audit Trail

- EXTRACTED: 620 (97%)
- INFERRED: 17 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*