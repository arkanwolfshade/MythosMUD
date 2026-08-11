# Chat Panel Components

> 235 nodes

## Key Concepts

- **test_security_validator.py** (96 connections) — `server/tests/unit/validators/test_security_validator.py`
- **security_validator.py** (33 connections) — `server/validators/security_validator.py`
- **validate_message_content()** (21 connections) — `server/validators/security_validator.py`
- **comprehensive_sanitize_input()** (20 connections) — `server/validators/security_validator.py`
- **validate_combat_target()** (14 connections) — `server/validators/security_validator.py`
- **strip_ansi_codes()** (13 connections) — `server/validators/security_validator.py`
- **validate_action_content()** (11 connections) — `server/validators/security_validator.py`
- **validate_alias_name()** (10 connections) — `server/validators/security_validator.py`
- **validate_reason_content()** (10 connections) — `server/validators/security_validator.py`
- **__init__.py** (9 connections) — `server/validators/__init__.py`
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
- *... and 210 more nodes in this community*

## Relationships

- [Zone Config Loader](Zone_Config_Loader.md) (15 shared connections)
- [Communication Command Models](Communication_Command_Models.md) (13 shared connections)
- [NPC Occupant Processor](NPC_Occupant_Processor.md) (9 shared connections)
- [Integer Coercion Utils](Integer_Coercion_Utils.md) (6 shared connections)
- [Environmental Container Scenario](Environmental_Container_Scenario.md) (4 shared connections)
- [Persistence Container Extended](Persistence_Container_Extended.md) (4 shared connections)
- [Admin Teleport Commands](Admin_Teleport_Commands.md) (3 shared connections)
- [Async Audit Cursor](Async_Audit_Cursor.md) (3 shared connections)
- [Chat NATS Publisher](Chat_NATS_Publisher.md) (2 shared connections)
- [Test Refactoring Deliverables](Test_Refactoring_Deliverables.md) (1 shared connections)

## Source Files

- `server/models/command_alias.py`
- `server/models/command_combat.py`
- `server/models/command_communication.py`
- `server/models/command_moderation.py`
- `server/models/command_utility.py`
- `server/tests/unit/validators/test_security_validator.py`
- `server/validators/__init__.py`
- `server/validators/security_validator.py`

## Audit Trail

- EXTRACTED: 705 (98%)
- INFERRED: 17 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*