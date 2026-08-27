# test_command_factories_inventory_helpers.py

> 26 nodes

## Key Concepts

- **validate_message_content()** (21 connections) — `server/validators/security_validator.py`
- **field_validator** (9 connections)
- **.validate_message()** (4 connections) — `server/models/command_communication.py`
- **.validate_message()** (4 connections) — `server/models/command_communication.py`
- **.validate_message()** (4 connections) — `server/models/command_communication.py`
- **.validate_message()** (4 connections) — `server/models/command_communication.py`
- **.validate_message()** (4 connections) — `server/models/command_communication.py`
- **Validate message content for security using centralized validation.** (4 connections) — `server/models/command_communication.py`
- **test_validate_message_content_allows_safe_special_chars()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_message_content_empty()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_message_content_normal()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_message_content_rejects_angle_brackets()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_message_content_rejects_html_tags()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_message_content_rejects_javascript_urls()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_message_content_rejects_path_traversal()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_message_content_rejects_shell_metacharacters()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Validate system message content for security using centralized validation.** (1 connections) — `server/models/command_communication.py`
- **Test validating empty message content.** (1 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Test validating normal message content.** (1 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Test that validate_message_content rejects HTML tags.** (1 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Test that validate_message_content rejects angle brackets.** (1 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Test that validate_message_content rejects shell metacharacters.** (1 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Test that validate_message_content rejects javascript: URLs.** (1 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Test that validate_message_content rejects path traversal patterns.** (1 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Test that validate_message_content allows safe special characters.** (1 connections) — `server/tests/unit/validators/test_security_validator.py`
- *... and 1 more nodes in this community*

## Relationships

- [test_rate_limiter_utils.py](test_rate_limiter_utils.py.md) (11 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (8 shared connections)
- [WebSocketRequestContext](WebSocketRequestContext.md) (4 shared connections)
- [test_lucidity_service.py](test_lucidity_service.py.md) (1 shared connections)

## Source Files

- `server/models/command_communication.py`
- `server/tests/unit/validators/test_security_validator.py`
- `server/validators/security_validator.py`

## Audit Trail

- EXTRACTED: 54 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*