# test_users.py

> 127 nodes

## Key Concepts

- **test_users.py** (55 connections) — `server/tests/unit/auth/test_users.py`
- **users.py** (48 connections) — `server/auth/users.py`
- **UserManager** (41 connections) — `server/auth/users.py`
- **RestartInvalidatingJWTStrategy** (13 connections) — `server/auth/jwt_strategy.py`
- **get_user_manager()** (13 connections) — `server/auth/users.py`
- **get_auth_backend()** (12 connections) — `server/auth/users.py`
- **get_user_db()** (11 connections) — `server/auth/users.py`
- **asyncio** (11 connections)
- **get_username_auth_backend()** (9 connections) — `server/auth/users.py`
- **UsernameAuthenticationBackend** (8 connections) — `server/auth/users.py`
- **server/auth/__init__.py** (7 connections) — `server/auth/__init__.py`
- **UUID** (7 connections)
- **.login()** (6 connections) — `server/auth/users.py`
- **validate_jwt_secret()** (6 connections) — `server/auth/users.py`
- **test_username_authentication_backend_login()** (6 connections) — `server/tests/unit/auth/test_users.py`
- **.__init__()** (5 connections) — `server/auth/users.py`
- **.on_after_register()** (5 connections) — `server/auth/users.py`
- **test_get_user_manager()** (5 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_forgot_password()** (5 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_forgot_password_with_request()** (5 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_register_bogus_email()** (5 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_register_no_email()** (5 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_register_non_bogus_email()** (5 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_register_with_request()** (5 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_request_verify()** (5 connections) — `server/tests/unit/auth/test_users.py`
- *... and 102 more nodes in this community*

## Relationships

- [pytest.md](pytest.md.md) (31 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (10 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (6 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (6 shared connections)
- [test_auth_utils.py](test_auth_utils.py.md) (5 shared connections)
- [test_email_utils.py](test_email_utils.py.md) (3 shared connections)
- [UnknownChannelStrategy](UnknownChannelStrategy.md) (2 shared connections)
- [ValidationError](ValidationError.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (2 shared connections)
- [.read_token](read_token.md) (1 shared connections)
- [InviteManager](InviteManager.md) (1 shared connections)

## Source Files

- `server/auth/__init__.py`
- `server/auth/jwt_strategy.py`
- `server/auth/users.py`
- `server/tests/unit/auth/test_users.py`

## Audit Trail

- EXTRACTED: 253 (89%)
- INFERRED: 30 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*