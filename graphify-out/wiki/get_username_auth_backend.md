# get_username_auth_backend

> 20 nodes

## Key Concepts

- **get_username_auth_backend()** (9 connections) — `server/auth/users.py`
- **UsernameAuthenticationBackend** (8 connections) — `server/auth/users.py`
- **.login()** (6 connections) — `server/auth/users.py`
- **test_username_authentication_backend_login()** (6 connections) — `server/tests/unit/auth/test_users.py`
- **test_username_authentication_backend_init()** (5 connections) — `server/tests/unit/auth/test_users.py`
- **test_get_username_auth_backend_jwt_strategy_uses_env_var()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_get_username_auth_backend_returns_username_authentication_backend()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_get_username_auth_backend()** (3 connections) — `server/tests/unit/auth/test_users.py`
- **test_get_username_auth_backend_jwt_strategy_default_secret()** (3 connections) — `server/tests/unit/auth/test_users.py`
- **Response** (1 connections)
- **Strategy** (1 connections)
- **Custom authentication backend that uses username instead of email.** (1 connections) — `server/auth/users.py`
- **Custom login that uses username.** (1 connections) — `server/auth/users.py`
- **Get username-based authentication backend configuration.** (1 connections) — `server/auth/users.py`
- **Test getting username-based authentication backend.** (1 connections) — `server/tests/unit/auth/test_users.py`
- **Test UsernameAuthenticationBackend login method.** (1 connections) — `server/tests/unit/auth/test_users.py`
- **Test that get_username_auth_backend returns UsernameAuthenticationBackend.** (1 connections) — `server/tests/unit/auth/test_users.py`
- **Test that get_username_auth_backend uses environment variable for JWT secret.** (1 connections) — `server/tests/unit/auth/test_users.py`
- **Test that get_username_auth_backend fails when JWT secret env var is missing.** (1 connections) — `server/tests/unit/auth/test_users.py`
- **Test UsernameAuthenticationBackend initialization.** (1 connections) — `server/tests/unit/auth/test_users.py`

## Relationships

- [test_users.py](test_users.py.md) (9 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (5 shared connections)
- [RestartInvalidatingJWTStrategy](RestartInvalidatingJWTStrategy.md) (2 shared connections)
- [test_channel_broadcasting_strategies.py](test_channel_broadcasting_strategies.py.md) (2 shared connections)
- [get_user_manager](get_user_manager.md) (1 shared connections)

## Source Files

- `server/auth/users.py`
- `server/tests/unit/auth/test_users.py`

## Audit Trail

- EXTRACTED: 32 (82%)
- INFERRED: 7 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*