# test_users.py

> 158 nodes

## Key Concepts

- **test_users.py** (55 connections) — `server/tests/unit/auth/test_users.py`
- **users.py** (48 connections) — `server/auth/users.py`
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
- **server/auth/__init__.py** (7 connections) — `server/auth/__init__.py`
- **jwt_strategy.py** (7 connections) — `server/auth/jwt_strategy.py`
- **UUID** (7 connections)
- **.login()** (6 connections) — `server/auth/users.py`
- **validate_jwt_secret()** (6 connections) — `server/auth/users.py`
- **test_read_token_accepts_matching_epoch()** (6 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **test_username_authentication_backend_login()** (6 connections) — `server/tests/unit/auth/test_users.py`
- **.__init__()** (5 connections) — `server/auth/users.py`
- **.on_after_register()** (5 connections) — `server/auth/users.py`
- *... and 133 more nodes in this community*

## Relationships

- [User](User.md) (21 shared connections)
- [endpoints.py](endpoints.py.md) (13 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (12 shared connections)
- [test_auth_utils.py](test_auth_utils.py.md) (5 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (3 shared connections)
- [test_email_utils.py](test_email_utils.py.md) (3 shared connections)
- [pytest.md](pytest.md.md) (3 shared connections)
- [UnknownChannelStrategy](UnknownChannelStrategy.md) (2 shared connections)
- [factory.py](factory.py.md) (2 shared connections)
- [test_users_current_user_logging.py](test_users_current_user_logging.py.md) (2 shared connections)
- [get_async_session](get_async_session.md) (1 shared connections)

## Source Files

- `server/auth/__init__.py`
- `server/auth/jwt_strategy.py`
- `server/auth/token_epoch.py`
- `server/auth/users.py`
- `server/tests/unit/auth/conftest.py`
- `server/tests/unit/auth/test_jwt_strategy.py`
- `server/tests/unit/auth/test_users.py`

## Audit Trail

- EXTRACTED: 308 (91%)
- INFERRED: 30 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*