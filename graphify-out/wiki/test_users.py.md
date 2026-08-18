# test_users.py

> 151 nodes

## Key Concepts

- **test_users.py** (55 connections) — `server/tests/unit/auth/test_users.py`
- **UserManager** (41 connections) — `server/auth/users.py`
- **RestartInvalidatingJWTStrategy** (13 connections) — `server/auth/jwt_strategy.py`
- **get_user_manager()** (13 connections) — `server/auth/users.py`
- **get_auth_backend()** (12 connections) — `server/auth/users.py`
- **get_user_db()** (11 connections) — `server/auth/users.py`
- **asyncio** (11 connections)
- **set_auth_epoch()** (10 connections) — `server/auth/token_epoch.py`
- **test_jwt_strategy.py** (10 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **get_username_auth_backend()** (9 connections) — `server/auth/users.py`
- **UsernameAuthenticationBackend** (8 connections) — `server/auth/users.py`
- **get_auth_epoch()** (8 connections) — `server/auth/token_epoch.py`
- **token_epoch.py** (8 connections) — `server/auth/token_epoch.py`
- **auth/conftest.py** (8 connections) — `server/tests/unit/auth/conftest.py`
- **.read_token()** (7 connections) — `server/auth/jwt_strategy.py`
- **jwt_strategy.py** (7 connections) — `server/auth/jwt_strategy.py`
- **UUID** (7 connections)
- **.login()** (6 connections) — `server/auth/users.py`
- **validate_jwt_secret()** (6 connections) — `server/auth/users.py`
- **test_read_token_accepts_matching_epoch()** (6 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **test_username_authentication_backend_login()** (6 connections) — `server/tests/unit/auth/test_users.py`
- **.__init__()** (5 connections) — `server/auth/users.py`
- **test_read_token_rejects_missing_epoch()** (5 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **test_read_token_rejects_wrong_epoch()** (5 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **test_get_user_manager()** (5 connections) — `server/tests/unit/auth/test_users.py`
- *... and 126 more nodes in this community*

## Relationships

- [pytest.md](pytest.md.md) (32 shared connections)
- [DatabaseError](DatabaseError.md) (16 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [lifespan.py](lifespan.py.md) (3 shared connections)
- [UnknownChannelStrategy](UnknownChannelStrategy.md) (2 shared connections)

## Source Files

- `server/auth/jwt_strategy.py`
- `server/auth/token_epoch.py`
- `server/auth/users.py`
- `server/tests/unit/auth/conftest.py`
- `server/tests/unit/auth/test_jwt_strategy.py`
- `server/tests/unit/auth/test_users.py`

## Audit Trail

- EXTRACTED: 261 (90%)
- INFERRED: 30 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*