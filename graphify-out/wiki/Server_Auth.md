# Server Auth

> 118 nodes

## Key Concepts

- **test_users.py** (60 connections) — `server/tests/unit/auth/test_users.py`
- **UserManager** (47 connections) — `server/auth/users.py`
- **UsernameAuthenticationBackend** (11 connections) — `server/auth/users.py`
- **get_current_user_with_logging()** (11 connections) — `server/auth/users.py`
- **get_username_auth_backend()** (9 connections) — `server/auth/users.py`
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
- **test_user_manager_on_after_forgot_password_with_request()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_request_verify_with_request()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_get_username_auth_backend_returns_username_authentication_backend()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_get_current_user_with_logging_success()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_get_current_user_with_logging_no_request()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_get_current_user_with_logging_long_auth_header()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_get_current_user_with_logging_no_auth_header()** (4 connections) — `server/tests/unit/auth/test_users.py`
- *... and 93 more nodes in this community*

## Relationships

- [Server Admin](Server_Admin.md) (40 shared connections)
- [Server Auth (5)](Server_Auth_%285%29.md) (4 shared connections)
- [Server Auth (2)](Server_Auth_%282%29.md) (3 shared connections)
- [Server Middleware](Server_Middleware.md) (2 shared connections)
- [Server Auth (4)](Server_Auth_%284%29.md) (2 shared connections)

## Source Files

- `server/auth/users.py`
- `server/tests/unit/auth/test_users.py`

## Audit Trail

- EXTRACTED: 379 (97%)
- INFERRED: 12 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*