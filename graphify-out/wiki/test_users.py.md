# test_users.py

> 139 nodes

## Key Concepts

- **test_users.py** (60 connections) — `server/tests/unit/auth/test_users.py`
- **UserManager** (46 connections) — `server/auth/users.py`
- **asyncio** (20 connections)
- **get_auth_backend()** (12 connections) — `server/auth/users.py`
- **get_current_user_with_logging()** (11 connections) — `server/auth/users.py`
- **UsernameAuthenticationBackend** (10 connections) — `server/auth/users.py`
- **get_username_auth_backend()** (9 connections) — `server/auth/users.py`
- **get_user_manager()** (8 connections) — `server/auth/users.py`
- **get_user_db()** (6 connections) — `server/auth/users.py`
- **.on_after_register()** (5 connections) — `server/auth/users.py`
- **test_get_current_user_with_logging_long_auth_header()** (5 connections) — `server/tests/unit/auth/test_users.py`
- **test_get_current_user_with_logging_no_auth_header()** (5 connections) — `server/tests/unit/auth/test_users.py`
- **test_get_current_user_with_logging_no_request()** (5 connections) — `server/tests/unit/auth/test_users.py`
- **test_get_current_user_with_logging_success()** (5 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_forgot_password()** (5 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_forgot_password_with_request()** (5 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_register_bogus_email()** (5 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_register_no_email()** (5 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_register_non_bogus_email()** (5 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_register_with_request()** (5 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_request_verify()** (5 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_request_verify_with_request()** (5 connections) — `server/tests/unit/auth/test_users.py`
- **test_username_authentication_backend_login()** (5 connections) — `server/tests/unit/auth/test_users.py`
- **.__init__()** (4 connections) — `server/auth/users.py`
- **.on_after_forgot_password()** (4 connections) — `server/auth/users.py`
- *... and 114 more nodes in this community*

## Relationships

- [User](User.md) (26 shared connections)
- [database.py](database.py.md) (11 shared connections)
- [lifespan.py](lifespan.py.md) (4 shared connections)
- [test_auth_utils.py](test_auth_utils.py.md) (2 shared connections)
- [UnknownChannelStrategy](UnknownChannelStrategy.md) (2 shared connections)

## Source Files

- `server/auth/users.py`
- `server/tests/unit/auth/test_users.py`

## Audit Trail

- EXTRACTED: 466 (98%)
- INFERRED: 9 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*