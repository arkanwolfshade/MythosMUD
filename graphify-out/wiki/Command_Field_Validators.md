# Command Field Validators

> 162 nodes · cohesion 0.02

## Key Concepts

- **test_security_validator.py** (95 connections) — `server/tests/unit/validators/test_security_validator.py`
- **security_validator.py** (32 connections) — `server/validators/security_validator.py`
- **comprehensive_sanitize_input()** (20 connections) — `server/validators/security_validator.py`
- **validate_message_content()** (20 connections) — `server/validators/security_validator.py`
- **command_communication.py** (18 connections) — `server/models/command_communication.py`
- **strip_ansi_codes()** (13 connections) — `server/validators/security_validator.py`
- **validate_action_content()** (11 connections) — `server/validators/security_validator.py`
- **validate_alias_name()** (10 connections) — `server/validators/security_validator.py`
- **validate_reason_content()** (10 connections) — `server/validators/security_validator.py`
- **__init__.py** (9 connections) — `server/validators/__init__.py`
- **clean_command_input()** (9 connections) — `server/validators/command_validator.py`
- **sanitize_unicode_input()** (9 connections) — `server/validators/security_validator.py`
- **validate_command_content()** (9 connections) — `server/validators/security_validator.py`
- **validate_pose_content()** (9 connections) — `server/validators/security_validator.py`
- **validate_filter_name()** (8 connections) — `server/validators/security_validator.py`
- **validate_help_topic()** (8 connections) — `server/validators/security_validator.py`
- **validate_target_player()** (8 connections) — `server/validators/security_validator.py`
- **validate_security_comprehensive()** (7 connections) — `server/validators/security_validator.py`
- **check_dangerous_characters()** (6 connections) — `server/validators/security_validator.py`
- **check_injection_patterns()** (6 connections) — `server/validators/security_validator.py`
- **Test that validate_message_content rejects angle brackets.** (6 connections) — `server/tests/unit/validators/test_security_validator.py`
- **get_dangerous_characters()** (5 connections) — `server/validators/security_validator.py`
- **get_injection_patterns()** (5 connections) — `server/validators/security_validator.py`
- **Centralized validation for message content fields.      This function provides c** (5 connections) — `server/validators/security_validator.py`
- **Centralized validation for player name fields.      This function provides consi** (5 connections) — `server/validators/security_validator.py`
- *... and 137 more nodes in this community*

## Relationships

- [[Base Command Models]] (19 shared connections)
- [[Communication Command Models]] (15 shared connections)
- [[Moderation Command Models]] (14 shared connections)
- [[Alias Expansion Logic]] (10 shared connections)
- [[Command Input Validator]] (7 shared connections)
- [[Combat Command Models]] (7 shared connections)
- [[Validators Security Validator]] (2 shared connections)
- [[Alias Command Models]] (1 shared connections)

## Source Files

- `server/models/command_alias.py`
- `server/models/command_communication.py`
- `server/models/command_utility.py`
- `server/tests/unit/validators/test_security_validator.py`
- `server/validators/__init__.py`
- `server/validators/command_validator.py`
- `server/validators/security_validator.py`

## Audit Trail

- EXTRACTED: 623 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
