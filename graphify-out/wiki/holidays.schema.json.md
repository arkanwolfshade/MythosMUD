# holidays.schema.json

> 11 nodes

## Key Concepts

- **validate_reason_content()** (10 connections) — `server/validators/security_validator.py`
- **.validate_reason()** (4 connections) — `server/models/command_moderation.py`
- **.validate_reason()** (4 connections) — `server/models/command_moderation.py`
- **test_validate_reason_content_empty()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_reason_content_rejects_html()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_reason_content_valid()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Validate mute reason for security using centralized validation.** (2 connections) — `server/models/command_moderation.py`
- **Test validating empty reason content.** (1 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Test validating valid reason content.** (1 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Test that validate_reason_content rejects HTML tags.** (1 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Centralized validation for reason content fields. This function provides…** (1 connections) — `server/validators/security_validator.py`

## Relationships

- [test_rate_limiter_utils.py](test_rate_limiter_utils.py.md) (4 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (3 shared connections)
- [ChatChannelLoggerMixin](ChatChannelLoggerMixin.md) (2 shared connections)
- [StandardizedErrorResponse](StandardizedErrorResponse.md) (1 shared connections)
- [WebSocketRequestContext](WebSocketRequestContext.md) (1 shared connections)

## Source Files

- `server/models/command_moderation.py`
- `server/tests/unit/validators/test_security_validator.py`
- `server/validators/security_validator.py`

## Audit Trail

- EXTRACTED: 22 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*