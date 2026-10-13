# Community 682

> 24 nodes

## Key Concepts

- **RestartInvalidatingJWTStrategy** (13 connections) — `server/auth/jwt_strategy.py`
- **get_username_auth_backend()** (9 connections) — `server/auth/users.py`
- **UsernameAuthenticationBackend** (8 connections) — `server/auth/users.py`
- **.read_token()** (7 connections) — `server/auth/jwt_strategy.py`
- **.get_strategy()** (6 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **test_username_authentication_backend_login()** (6 connections) — `server/tests/unit/auth/test_users.py`
- **test_username_authentication_backend_init()** (5 connections) — `server/tests/unit/auth/test_users.py`
- **test_get_username_auth_backend_jwt_strategy_uses_env_var()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_get_username_auth_backend_returns_username_authentication_backend()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_get_username_auth_backend()** (3 connections) — `server/tests/unit/auth/test_users.py`
- **test_get_username_auth_backend_jwt_strategy_default_secret()** (3 connections) — `server/tests/unit/auth/test_users.py`
- **Test UsernameAuthenticationBackend login method.** (2 connections) — `server/tests/unit/auth/test_users.py`
- **BaseUserManager** (1 connections)
- **ID** (1 connections)
- **UP** (1 connections)
- **JWT strategy that rejects tokens issued before the current server start.** (1 connections) — `server/auth/jwt_strategy.py`
- **Reads a JWT token, validating its signature, audience, and server epoch.** (1 connections) — `server/auth/jwt_strategy.py`
- **Custom authentication backend that uses username instead of email.** (1 connections) — `server/auth/users.py`
- **Get username-based authentication backend configuration.** (1 connections) — `server/auth/users.py`
- **Get strategy for channel type. Args: channel_type: Type of channel to get…** (1 connections) — `server/realtime/channel_broadcasting_strategies.py`
- **Test getting username-based authentication backend.** (1 connections) — `server/tests/unit/auth/test_users.py`
- **Test that get_username_auth_backend returns UsernameAuthenticationBackend.** (1 connections) — `server/tests/unit/auth/test_users.py`
- **Test that get_username_auth_backend uses environment variable for JWT secret.** (1 connections) — `server/tests/unit/auth/test_users.py`
- **Test that get_username_auth_backend fails when JWT secret env var is missing.** (1 connections) — `server/tests/unit/auth/test_users.py`

## Relationships

- [Community 236](Community_236.md) (10 shared connections)
- [Community 644](Community_644.md) (6 shared connections)
- [Auth Dependencies & Users](Auth_Dependencies_&_Users.md) (5 shared connections)
- [Community 240](Community_240.md) (3 shared connections)
- [Community 1128](Community_1128.md) (2 shared connections)
- [Community 835](Community_835.md) (1 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (1 shared connections)

## Source Files

- `server/auth/jwt_strategy.py`
- `server/auth/users.py`
- `server/realtime/channel_broadcasting_strategies.py`
- `server/tests/unit/auth/test_users.py`

## Audit Trail

- EXTRACTED: 44 (80%)
- INFERRED: 11 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*