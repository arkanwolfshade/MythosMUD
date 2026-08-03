# subject nats manager

> 32 nodes

## Key Concepts

- **validate_message_content()** (21 connections) — `server/validators/security_validator.py`
- **.validate_message()** (3 connections) — `server/models/command_communication.py`
- **.validate_message()** (3 connections) — `server/models/command_communication.py`
- **.validate_message()** (3 connections) — `server/models/command_communication.py`
- **.validate_message()** (3 connections) — `server/models/command_communication.py`
- **.validate_message()** (3 connections) — `server/models/command_communication.py`
- **test_validate_message_content_empty()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_message_content_normal()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_message_content_rejects_html_tags()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_message_content_rejects_angle_brackets()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_message_content_rejects_sql_injection()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_message_content_rejects_shell_metacharacters()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_message_content_rejects_xss_patterns()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_message_content_rejects_javascript_urls()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_message_content_rejects_path_traversal()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_message_content_allows_safe_special_chars()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Validate message content for security using centralized validation.** (1 connections) — `server/models/command_communication.py`
- **Validate message content for security using centralized validation.** (1 connections) — `server/models/command_communication.py`
- **Validate system message content for security using centralized validation.** (1 connections) — `server/models/command_communication.py`
- **Validate message content for security using centralized validation.** (1 connections) — `server/models/command_communication.py`
- **Validate message content for security using centralized validation.** (1 connections) — `server/models/command_communication.py`
- **Test validating empty message content.** (1 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Test validating normal message content.** (1 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Test that validate_message_content rejects HTML tags.** (1 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Test that validate_message_content rejects angle brackets.** (1 connections) — `server/tests/unit/validators/test_security_validator.py`
- *... and 7 more nodes in this community*

## Relationships

- [Security Validator Tests](Security_Validator_Tests.md) (11 shared connections)
- [command communication models](command_communication_models.md) (8 shared connections)
- [npc behavior engine](npc_behavior_engine.md) (1 shared connections)

## Source Files

- `server/models/command_communication.py`
- `server/tests/unit/validators/test_security_validator.py`
- `server/validators/security_validator.py`

## Audit Trail

- EXTRACTED: 80 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*