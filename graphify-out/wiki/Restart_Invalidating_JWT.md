# Restart Invalidating JWT

> 148 nodes · cohesion 0.02

## Key Concepts

- **test_users.py** (59 connections) — `server/tests/unit/auth/test_users.py`
- **UserManager** (53 connections) — `server/auth/users.py`
- **RestartInvalidatingJWTStrategy** (19 connections) — `server/auth/jwt_strategy.py`
- **get_auth_backend()** (12 connections) — `server/auth/users.py`
- **UsernameAuthenticationBackend** (10 connections) — `server/auth/users.py`
- **get_username_auth_backend()** (9 connections) — `server/auth/users.py`
- **get_user_manager()** (8 connections) — `server/auth/users.py`
- **.read_token()** (6 connections) — `server/auth/jwt_strategy.py`
- **get_user_db()** (6 connections) — `server/auth/users.py`
- **test_jwt_strategy.py** (5 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **get_current_user_with_logging()** (5 connections) — `server/auth/users.py`
- **.on_after_register()** (5 connections) — `server/auth/users.py`
- **Any** (5 connections) — `server/auth/users.py`
- **User** (5 connections) — `server/auth/users.py`
- **test_user_manager_on_after_forgot_password()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_forgot_password_with_request()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_register_bogus_email()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_register_no_email()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_register_non_bogus_email()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_register_with_request()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_request_verify()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_request_verify_with_request()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **.__init__()** (4 connections) — `server/auth/users.py`
- **.on_after_forgot_password()** (4 connections) — `server/auth/users.py`
- **.on_after_request_verify()** (4 connections) — `server/auth/users.py`
- *... and 123 more nodes in this community*

## Relationships

- [[Argon2 Password Hashing]] (16 shared connections)
- [[NPC Admin API]] (15 shared connections)
- [[API Test Fixtures]] (13 shared connections)

## Source Files

- `server/auth/jwt_strategy.py`
- `server/auth/users.py`
- `server/tests/unit/auth/test_jwt_strategy.py`
- `server/tests/unit/auth/test_users.py`

## Audit Trail

- EXTRACTED: 456 (94%)
- INFERRED: 30 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
