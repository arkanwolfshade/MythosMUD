# register_user

> 75 nodes

## Key Concepts

- **register_user()** (32 connections) — `server/auth/endpoints.py`
- **UserCreate** (24 connections) — `server/auth/endpoints.py`
- **test_endpoints_register.py** (23 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **asyncio** (14 connections)
- **RestartInvalidatingJWTStrategy** (13 connections) — `server/auth/jwt_strategy.py`
- **test_jwt_strategy.py** (10 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **get_username_auth_backend()** (9 connections) — `server/auth/users.py`
- **UsernameAuthenticationBackend** (8 connections) — `server/auth/users.py`
- **_generate_jwt_token()** (8 connections) — `server/auth/endpoints.py`
- **get_auth_epoch()** (8 connections) — `server/auth/token_epoch.py`
- **_handle_integrity_error()** (7 connections) — `server/auth/endpoints.py`
- **.read_token()** (7 connections) — `server/auth/jwt_strategy.py`
- **test_register_user_duplicate_username()** (7 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_register_user_email_constraint_violation()** (7 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_register_user_generic_constraint_violation()** (7 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_register_user_integrity_error()** (7 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_register_user_username_constraint_violation()** (7 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_register_user_invite_validation_failure()** (6 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_register_user_shutdown_pending()** (6 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_register_user_success()** (6 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_read_token_accepts_matching_epoch()** (6 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **IntegrityError** (6 connections)
- **LoginResponse** (5 connections) — `server/auth/endpoints.py`
- **test_register_user_invite_marking_failure()** (5 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_register_user_invite_marking_success()** (5 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- *... and 50 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (20 shared connections)
- [login_user](login_user.md) (10 shared connections)
- [test_users.py](test_users.py.md) (9 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (9 shared connections)
- [lifespan.py](lifespan.py.md) (6 shared connections)
- [User](User.md) (4 shared connections)
- [_validate_invite_code](_validate_invite_code.md) (2 shared connections)
- [get_auth_backend](get_auth_backend.md) (2 shared connections)
- [test_endpoints_invites.py](test_endpoints_invites.py.md) (2 shared connections)
- [InviteManager](InviteManager.md) (2 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)
- [factory.py](factory.py.md) (1 shared connections)

## Source Files

- `server/auth/endpoints.py`
- `server/auth/jwt_strategy.py`
- `server/auth/token_epoch.py`
- `server/auth/users.py`
- `server/tests/unit/auth/test_endpoints_register.py`
- `server/tests/unit/auth/test_jwt_strategy.py`
- `server/tests/unit/auth/test_users.py`

## Audit Trail

- EXTRACTED: 162 (81%)
- INFERRED: 39 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*