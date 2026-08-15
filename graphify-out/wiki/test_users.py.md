# test_users.py

> 127 nodes

## Key Concepts

- **test_users.py** (53 connections) — `server/tests/unit/auth/test_users.py`
- **users.py** (48 connections) — `server/auth/users.py`
- **UserManager** (41 connections) — `server/auth/users.py`
- **RestartInvalidatingJWTStrategy** (13 connections) — `server/auth/jwt_strategy.py`
- **get_user_manager()** (13 connections) — `server/auth/users.py`
- **get_auth_backend()** (12 connections) — `server/auth/users.py`
- **get_user_db()** (11 connections) — `server/auth/users.py`
- **asyncio** (11 connections)
- **get_username_auth_backend()** (9 connections) — `server/auth/users.py`
- **UsernameAuthenticationBackend** (8 connections) — `server/auth/users.py`
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
- **test_user_manager_on_after_request_verify_with_request()** (5 connections) — `server/tests/unit/auth/test_users.py`
- *... and 102 more nodes in this community*

## Relationships

- [User](User.md) (28 shared connections)
- [lifespan.py](lifespan.py.md) (7 shared connections)
- [models/user.py](models-user.py.md) (6 shared connections)
- [DatabaseError](DatabaseError.md) (5 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [test_email_utils.py](test_email_utils.py.md) (3 shared connections)
- [test_argon2_utils.py](test_argon2_utils.py.md) (2 shared connections)
- [UnknownChannelStrategy](UnknownChannelStrategy.md) (2 shared connections)
- [get_admin_auth_service](get_admin_auth_service.md) (2 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (2 shared connections)
- [test_users_current_user_logging.py](test_users_current_user_logging.py.md) (2 shared connections)
- [get_async_session](get_async_session.md) (1 shared connections)

## Source Files

- `server/auth/jwt_strategy.py`
- `server/auth/users.py`
- `server/tests/unit/auth/test_users.py`

## Audit Trail

- EXTRACTED: 229 (82%)
- INFERRED: 50 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*