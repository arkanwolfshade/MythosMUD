# Server Validators

> 184 nodes

## Key Concepts

- **test_security_validator.py** (96 connections) — `server/tests/unit/validators/test_security_validator.py`
- **security_validator.py** (33 connections) — `server/validators/security_validator.py`
- **validate_message_content()** (21 connections) — `server/validators/security_validator.py`
- **validate_player_name()** (21 connections) — `server/validators/security_validator.py`
- **comprehensive_sanitize_input()** (20 connections) — `server/validators/security_validator.py`
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
- **Test that validate_message_content rejects angle brackets.** (6 connections) — `server/tests/unit/validators/test_security_validator.py`
- **check_dangerous_characters()** (6 connections) — `server/validators/security_validator.py`
- **check_injection_patterns()** (6 connections) — `server/validators/security_validator.py`
- **get_dangerous_characters()** (5 connections) — `server/validators/security_validator.py`
- **get_injection_patterns()** (5 connections) — `server/validators/security_validator.py`
- **Centralized validation for message content fields.      This function provides c** (5 connections) — `server/validators/security_validator.py`
- **Centralized validation for player name fields.      This function provides consi** (5 connections) — `server/validators/security_validator.py`
- **Validate message content for security using centralized validation.** (4 connections) — `server/models/command_communication.py`
- **Test that validate_message_content rejects HTML tags.** (4 connections) — `server/tests/unit/validators/test_security_validator.py`
- **.validate_alias_name_field()** (3 connections) — `server/models/command_alias.py`
- *... and 159 more nodes in this community*

## Relationships

- [Server Models](Server_Models.md) (29 shared connections)
- [Server Commands (5)](Server_Commands_%285%29.md) (12 shared connections)
- [Server Models (4)](Server_Models_%284%29.md) (10 shared connections)
- [Server Models (7)](Server_Models_%287%29.md) (7 shared connections)
- [Server Models (8)](Server_Models_%288%29.md) (4 shared connections)
- [Server Commands](Server_Commands.md) (3 shared connections)

## Source Files

- `server/models/command_alias.py`
- `server/models/command_communication.py`
- `server/models/command_moderation.py`
- `server/models/command_utility.py`
- `server/tests/unit/validators/test_security_validator.py`
- `server/validators/security_validator.py`

## Audit Trail

- EXTRACTED: 644 (97%)
- INFERRED: 17 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*