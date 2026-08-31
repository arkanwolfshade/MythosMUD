# RestartInvalidatingJWTStrategy

> 20 nodes

## Key Concepts

- **RestartInvalidatingJWTStrategy** (13 connections) — `server/auth/jwt_strategy.py`
- **get_auth_backend()** (12 connections) — `server/auth/users.py`
- **.read_token()** (7 connections) — `server/auth/jwt_strategy.py`
- **server/auth/__init__.py** (7 connections) — `server/auth/__init__.py`
- **test_get_auth_backend_jwt_strategy_uses_env_var()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_get_auth_backend()** (3 connections) — `server/tests/unit/auth/test_users.py`
- **test_get_auth_backend_jwt_strategy_default_secret()** (3 connections) — `server/tests/unit/auth/test_users.py`
- **test_get_auth_backend_returns_authentication_backend()** (3 connections) — `server/tests/unit/auth/test_users.py`
- **AuthenticationBackend** (1 connections)
- **BaseUserManager** (1 connections)
- **ID** (1 connections)
- **UP** (1 connections)
- **Authentication module for MythosMUD. This package contains all authentication-…** (1 connections) — `server/auth/__init__.py`
- **JWT strategy that rejects tokens issued before the current server start.** (1 connections) — `server/auth/jwt_strategy.py`
- **Reads a JWT token, validating its signature, audience, and server epoch.** (1 connections) — `server/auth/jwt_strategy.py`
- **Get authentication backend configuration.** (1 connections) — `server/auth/users.py`
- **Test getting authentication backend.** (1 connections) — `server/tests/unit/auth/test_users.py`
- **Test that get_auth_backend returns an AuthenticationBackend instance.** (1 connections) — `server/tests/unit/auth/test_users.py`
- **Test that get_auth_backend uses environment variable for JWT secret.** (1 connections) — `server/tests/unit/auth/test_users.py`
- **Test that get_auth_backend fails when JWT secret env var is missing.** (1 connections) — `server/tests/unit/auth/test_users.py`

## Relationships

- [LoggedHTTPException](LoggedHTTPException.md) (12 shared connections)
- [test_users.py](test_users.py.md) (6 shared connections)
- [get_username_auth_backend](get_username_auth_backend.md) (2 shared connections)
- [get_user_manager](get_user_manager.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [InviteManager](InviteManager.md) (1 shared connections)

## Source Files

- `server/auth/__init__.py`
- `server/auth/jwt_strategy.py`
- `server/auth/users.py`
- `server/tests/unit/auth/test_users.py`

## Audit Trail

- EXTRACTED: 39 (89%)
- INFERRED: 5 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*