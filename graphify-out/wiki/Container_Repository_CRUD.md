# Container Repository CRUD

> 23 nodes

## Key Concepts

- **UsernameAuthenticationBackend** (11 connections) — `server/auth/users.py`
- **get_username_auth_backend()** (9 connections) — `server/auth/users.py`
- **.parse_id()** (4 connections) — `server/auth/users.py`
- **Any** (4 connections)
- **test_username_authentication_backend_login()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_get_username_auth_backend_returns_username_authentication_backend()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_username_authentication_backend_init()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **.__init__()** (3 connections) — `server/auth/users.py`
- **.login()** (3 connections) — `server/auth/users.py`
- **test_get_username_auth_backend()** (3 connections) — `server/tests/unit/auth/test_users.py`
- **test_get_username_auth_backend_jwt_strategy_uses_env_var()** (3 connections) — `server/tests/unit/auth/test_users.py`
- **test_get_username_auth_backend_jwt_strategy_default_secret()** (3 connections) — `server/tests/unit/auth/test_users.py`
- **AuthenticationBackend** (2 connections)
- **Parse a value into a UUID instance.** (1 connections) — `server/auth/users.py`
- **Custom authentication backend that uses username instead of email.** (1 connections) — `server/auth/users.py`
- **Custom login that uses username.** (1 connections) — `server/auth/users.py`
- **Get username-based authentication backend configuration.** (1 connections) — `server/auth/users.py`
- **Test getting username-based authentication backend.** (1 connections) — `server/tests/unit/auth/test_users.py`
- **Test UsernameAuthenticationBackend login method.** (1 connections) — `server/tests/unit/auth/test_users.py`
- **Test that get_username_auth_backend returns UsernameAuthenticationBackend.** (1 connections) — `server/tests/unit/auth/test_users.py`
- **Test that get_username_auth_backend uses environment variable for JWT secret.** (1 connections) — `server/tests/unit/auth/test_users.py`
- **Test that get_username_auth_backend uses default secret when env var not set.** (1 connections) — `server/tests/unit/auth/test_users.py`
- **Test UsernameAuthenticationBackend initialization.** (1 connections) — `server/tests/unit/auth/test_users.py`

## Relationships

- [Combat Command Handler](Combat_Command_Handler.md) (11 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (4 shared connections)
- [Docker PostgreSQL Typo Bug](Docker_PostgreSQL_Typo_Bug.md) (2 shared connections)
- [Error Monitor Service](Error_Monitor_Service.md) (2 shared connections)

## Source Files

- `server/auth/users.py`
- `server/tests/unit/auth/test_users.py`

## Audit Trail

- EXTRACTED: 62 (93%)
- INFERRED: 5 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*