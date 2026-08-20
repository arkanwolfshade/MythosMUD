# register_user

> 47 nodes

## Key Concepts

- **register_user()** (32 connections) — `server/auth/endpoints.py`
- **UserCreate** (24 connections) — `server/auth/endpoints.py`
- **test_endpoints_register.py** (23 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **asyncio** (14 connections)
- **_handle_integrity_error()** (7 connections) — `server/auth/endpoints.py`
- **test_register_user_duplicate_username()** (7 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_register_user_email_constraint_violation()** (7 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_register_user_generic_constraint_violation()** (7 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_register_user_integrity_error()** (7 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_register_user_username_constraint_violation()** (7 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_register_user_invite_validation_failure()** (6 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_register_user_shutdown_pending()** (6 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_register_user_success()** (6 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **IntegrityError** (6 connections)
- **LoginResponse** (5 connections) — `server/auth/endpoints.py`
- **test_register_user_invite_marking_failure()** (5 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_register_user_invite_marking_success()** (5 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_register_user_no_email()** (5 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_register_user_unexpected_exception()** (5 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **_ensure_user_email()** (4 connections) — `server/auth/endpoints.py`
- **test_register_user_password_validation_empty()** (4 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_register_user_password_validation_whitespace()** (4 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **.validate_password()** (3 connections) — `server/auth/endpoints.py`
- **BaseModel** (3 connections)
- **field_validator** (1 connections)
- *... and 22 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (13 shared connections)
- [login_user](login_user.md) (11 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (9 shared connections)
- [User](User.md) (3 shared connections)
- [test_auth_dependencies.py](test_auth_dependencies.py.md) (2 shared connections)
- [Invite](Invite.md) (1 shared connections)
- [test_player_preferences_service.py](test_player_preferences_service.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/auth/endpoints.py`
- `server/tests/unit/auth/test_endpoints_register.py`

## Audit Trail

- EXTRACTED: 104 (78%)
- INFERRED: 29 (22%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*