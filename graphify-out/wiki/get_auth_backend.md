# get_auth_backend

> 11 nodes

## Key Concepts

- **get_auth_backend()** (12 connections) — `server/auth/users.py`
- **test_get_auth_backend_jwt_strategy_uses_env_var()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_get_auth_backend()** (3 connections) — `server/tests/unit/auth/test_users.py`
- **test_get_auth_backend_jwt_strategy_default_secret()** (3 connections) — `server/tests/unit/auth/test_users.py`
- **test_get_auth_backend_returns_authentication_backend()** (3 connections) — `server/tests/unit/auth/test_users.py`
- **AuthenticationBackend** (1 connections)
- **Get authentication backend configuration.** (1 connections) — `server/auth/users.py`
- **Test getting authentication backend.** (1 connections) — `server/tests/unit/auth/test_users.py`
- **Test that get_auth_backend returns an AuthenticationBackend instance.** (1 connections) — `server/tests/unit/auth/test_users.py`
- **Test that get_auth_backend uses environment variable for JWT secret.** (1 connections) — `server/tests/unit/auth/test_users.py`
- **Test that get_auth_backend fails when JWT secret env var is missing.** (1 connections) — `server/tests/unit/auth/test_users.py`

## Relationships

- [test_users.py](test_users.py.md) (5 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [register_user](register_user.md) (2 shared connections)
- [get_user_manager](get_user_manager.md) (1 shared connections)
- [User](User.md) (1 shared connections)

## Source Files

- `server/auth/users.py`
- `server/tests/unit/auth/test_users.py`

## Audit Trail

- EXTRACTED: 19 (90%)
- INFERRED: 2 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*