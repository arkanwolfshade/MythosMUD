# authenticationbackend

> 123 nodes

## Key Concepts

- **test_users.py** (55 connections) — `server/tests/unit/auth/test_users.py`
- **UserManager** (41 connections) — `server/auth/users.py`
- **RestartInvalidatingJWTStrategy** (13 connections) — `server/auth/jwt_strategy.py`
- **get_user_manager()** (13 connections) — `server/auth/users.py`
- **get_auth_backend()** (12 connections) — `server/auth/users.py`
- **get_user_db()** (11 connections) — `server/auth/users.py`
- **asyncio** (11 connections)
- **get_username_auth_backend()** (9 connections) — `server/auth/users.py`
- **UsernameAuthenticationBackend** (8 connections) — `server/auth/users.py`
- **.read_token()** (7 connections) — `server/auth/jwt_strategy.py`
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
- *... and 98 more nodes in this community*

## Relationships

- [claude rules fastapi](claude_rules_fastapi.md) (30 shared connections)
- [characterinfo](characterinfo.md) (14 shared connections)
- [passwordhasher](passwordhasher.md) (2 shared connections)
- [server auth dependencies](server_auth_dependencies.md) (2 shared connections)
- [server realtime channel broadcasting strategies](server_realtime_channel_broadcasting_strategies.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (1 shared connections)
- [server auth email utils generate](server_auth_email_utils_generate.md) (1 shared connections)

## Source Files

- `server/auth/jwt_strategy.py`
- `server/auth/users.py`
- `server/tests/unit/auth/test_users.py`

## Audit Trail

- EXTRACTED: 193 (79%)
- INFERRED: 50 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*