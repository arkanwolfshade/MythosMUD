# RestartInvalidatingJWTStrategy

> 35 nodes

## Key Concepts

- **RestartInvalidatingJWTStrategy** (13 connections) — `server/auth/jwt_strategy.py`
- **set_auth_epoch()** (10 connections) — `server/auth/token_epoch.py`
- **get_username_auth_backend()** (9 connections) — `server/auth/users.py`
- **test_jwt_strategy.py** (9 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **UsernameAuthenticationBackend** (8 connections) — `server/auth/users.py`
- **get_auth_epoch()** (8 connections) — `server/auth/token_epoch.py`
- **token_epoch.py** (8 connections) — `server/auth/token_epoch.py`
- **.read_token()** (7 connections) — `server/auth/jwt_strategy.py`
- **test_read_token_accepts_matching_epoch()** (6 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **auth/conftest.py** (6 connections) — `server/tests/unit/auth/conftest.py`
- **test_read_token_rejects_missing_epoch()** (5 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **test_read_token_rejects_wrong_epoch()** (5 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **set_auth_epoch_for_tests()** (4 connections) — `server/tests/unit/auth/conftest.py`
- **mock_request()** (3 connections) — `server/tests/unit/auth/conftest.py`
- **mock_session()** (3 connections) — `server/tests/unit/auth/conftest.py`
- **fixture** (3 connections)
- **asyncio** (3 connections)
- **BaseUserManager** (1 connections)
- **ID** (1 connections)
- **UP** (1 connections)
- **JWT strategy that rejects tokens issued before the current server start.** (1 connections) — `server/auth/jwt_strategy.py`
- **Reads a JWT token, validating its signature, audience, and server epoch.** (1 connections) — `server/auth/jwt_strategy.py`
- **Auth token epoch for server-restart invalidation. All JWTs issued before the…** (1 connections) — `server/auth/token_epoch.py`
- **Set the current auth epoch (call once at server startup).** (1 connections) — `server/auth/token_epoch.py`
- **Return the current auth epoch. Must be set before any token validation.** (1 connections) — `server/auth/token_epoch.py`
- *... and 10 more nodes in this community*

## Relationships

- [test_users.py](test_users.py.md) (11 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [User](User.md) (3 shared connections)
- [lifespan.py](lifespan.py.md) (2 shared connections)
- [UnknownChannelStrategy](UnknownChannelStrategy.md) (1 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (1 shared connections)

## Source Files

- `server/auth/jwt_strategy.py`
- `server/auth/token_epoch.py`
- `server/auth/users.py`
- `server/tests/unit/auth/conftest.py`
- `server/tests/unit/auth/test_jwt_strategy.py`

## Audit Trail

- EXTRACTED: 75 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*