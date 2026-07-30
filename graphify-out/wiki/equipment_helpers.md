# equipment helpers

> 138 nodes

## Key Concepts

- **test_users.py** (60 connections) — `server/tests/unit/auth/test_users.py`
- **UserManager** (47 connections) — `server/auth/users.py`
- **RestartInvalidatingJWTStrategy** (12 connections) — `server/auth/jwt_strategy.py`
- **UsernameAuthenticationBackend** (11 connections) — `server/auth/users.py`
- **get_current_user_with_logging()** (11 connections) — `server/auth/users.py`
- **get_username_auth_backend()** (9 connections) — `server/auth/users.py`
- **get_user_manager()** (8 connections) — `server/auth/users.py`
- **jwt_strategy.py** (7 connections) — `server/auth/jwt_strategy.py`
- **.read_token()** (7 connections) — `server/auth/jwt_strategy.py`
- **get_user_db()** (7 connections) — `server/auth/users.py`
- **.__init__()** (4 connections) — `server/auth/users.py`
- **.on_after_forgot_password()** (4 connections) — `server/auth/users.py`
- **.on_after_request_verify()** (4 connections) — `server/auth/users.py`
- **.parse_id()** (4 connections) — `server/auth/users.py`
- **Any** (4 connections)
- **test_user_manager_on_after_register_bogus_email()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_register_non_bogus_email()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_register_no_email()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_register_with_request()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_forgot_password()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_request_verify()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_get_user_manager()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_username_authentication_backend_login()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_forgot_password_with_request()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_request_verify_with_request()** (4 connections) — `server/tests/unit/auth/test_users.py`
- *... and 113 more nodes in this community*

## Relationships

- [metrics](metrics.md) (37 shared connections)
- [Connection Manager](Connection_Manager.md) (7 shared connections)
- [.shutdown()](shutdown%28%29.md) (6 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (2 shared connections)
- [test security headers](test_security_headers.md) (2 shared connections)
- [create access token()](create_access_token%28%29.md) (2 shared connections)
- [add fastapi users columns](add_fastapi_users_columns.md) (2 shared connections)

## Source Files

- `server/auth/jwt_strategy.py`
- `server/auth/users.py`
- `server/tests/unit/auth/test_users.py`

## Audit Trail

- EXTRACTED: 426 (96%)
- INFERRED: 16 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*