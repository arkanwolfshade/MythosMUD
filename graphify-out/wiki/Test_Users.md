# Test Users

> 122 nodes

## Key Concepts

- **test_users.py** (55 connections) — `server/tests/unit/auth/test_users.py`
- **UserManager** (38 connections) — `server/auth/users.py`
- **RestartInvalidatingJWTStrategy** (13 connections) — `server/auth/jwt_strategy.py`
- **get_auth_backend()** (12 connections) — `server/auth/users.py`
- **get_user_db()** (11 connections) — `server/auth/users.py`
- **get_user_manager()** (11 connections) — `server/auth/users.py`
- **asyncio** (11 connections)
- **get_username_auth_backend()** (9 connections) — `server/auth/users.py`
- **UsernameAuthenticationBackend** (8 connections) — `server/auth/users.py`
- **server/auth/__init__.py** (7 connections) — `server/auth/__init__.py`
- **UUID** (7 connections)
- **.login()** (6 connections) — `server/auth/users.py`
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
- **test_username_authentication_backend_init()** (5 connections) — `server/tests/unit/auth/test_users.py`
- *... and 97 more nodes in this community*

## Relationships

- [Container Exception Handling](Container_Exception_Handling.md) (22 shared connections)
- [Character Creation API](Character_Creation_API.md) (11 shared connections)
- [Test Lifespan Startup](Test_Lifespan_Startup.md) (6 shared connections)
- [Test Argon2 Utils](Test_Argon2_Utils.md) (2 shared connections)
- [Channel Broadcasting Strategies](Channel_Broadcasting_Strategies.md) (2 shared connections)
- [Invites](Invites.md) (2 shared connections)
- [Test Email Utils](Test_Email_Utils.md) (1 shared connections)
- [Test Auth Dependencies](Test_Auth_Dependencies.md) (1 shared connections)

## Source Files

- `server/auth/__init__.py`
- `server/auth/jwt_strategy.py`
- `server/auth/users.py`
- `server/tests/unit/auth/test_users.py`

## Audit Trail

- EXTRACTED: 211 (88%)
- INFERRED: 28 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*