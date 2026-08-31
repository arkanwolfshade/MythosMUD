# get_user_manager

> 17 nodes

## Key Concepts

- **get_user_manager()** (13 connections) — `server/auth/users.py`
- **get_user_db()** (11 connections) — `server/auth/users.py`
- **UUID** (7 connections)
- **.__init__()** (5 connections) — `server/auth/users.py`
- **test_get_user_manager()** (5 connections) — `server/tests/unit/auth/test_users.py`
- **test_get_user_db()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **.parse_id()** (3 connections) — `server/auth/users.py`
- **SQLAlchemyUserDatabase** (3 connections)
- **Depends** (2 connections)
- **AsyncSession** (1 connections)
- **get_async_session** (1 connections)
- **Get user database dependency.** (1 connections) — `server/auth/users.py`
- **Get user manager dependency.** (1 connections) — `server/auth/users.py`
- **Initialize UserManager with validated secrets.** (1 connections) — `server/auth/users.py`
- **Parse a value into a UUID instance.** (1 connections) — `server/auth/users.py`
- **Test getting user database dependency.** (1 connections) — `server/tests/unit/auth/test_users.py`
- **Test getting user manager dependency.** (1 connections) — `server/tests/unit/auth/test_users.py`

## Relationships

- [test_users.py](test_users.py.md) (10 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (8 shared connections)
- [RestartInvalidatingJWTStrategy](RestartInvalidatingJWTStrategy.md) (2 shared connections)
- [get_username_auth_backend](get_username_auth_backend.md) (1 shared connections)

## Source Files

- `server/auth/users.py`
- `server/tests/unit/auth/test_users.py`

## Audit Trail

- EXTRACTED: 40 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*