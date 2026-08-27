# _utc_now

> 14 nodes

## Key Concepts

- **validate_alias_name()** (10 connections) — `server/validators/security_validator.py`
- **.validate_alias_name_field()** (4 connections) — `server/models/command_alias.py`
- **.validate_alias_name_field()** (4 connections) — `server/models/command_alias.py`
- **test_validate_alias_name_empty()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_alias_name_rejects_hyphens()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_alias_name_rejects_invalid_format()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_alias_name_valid()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **field_validator** (3 connections)
- **Validate alias name format using centralized validation.** (2 connections) — `server/models/command_alias.py`
- **Test validating empty alias name.** (1 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Test validating valid alias name.** (1 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Test that validate_alias_name rejects invalid format.** (1 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Test that validate_alias_name rejects hyphens.** (1 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Centralized validation for alias name fields. This function provides consistent…** (1 connections) — `server/validators/security_validator.py`

## Relationships

- [test_rate_limiter_utils.py](test_rate_limiter_utils.py.md) (5 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (3 shared connections)
- [WebSocketRequestContext](WebSocketRequestContext.md) (2 shared connections)

## Source Files

- `server/models/command_alias.py`
- `server/tests/unit/validators/test_security_validator.py`
- `server/validators/security_validator.py`

## Audit Trail

- EXTRACTED: 24 (96%)
- INFERRED: 1 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*