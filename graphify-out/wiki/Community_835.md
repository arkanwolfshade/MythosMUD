# Community 835

> 19 nodes

## Key Concepts

- **get_user_db()** (11 connections) — `server/auth/users.py`
- **get_user_manager()** (11 connections) — `server/auth/users.py`
- **UUID** (7 connections)
- **.login()** (6 connections) — `server/auth/users.py`
- **.__init__()** (5 connections) — `server/auth/users.py`
- **test_get_user_db()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **.parse_id()** (3 connections) — `server/auth/users.py`
- **SQLAlchemyUserDatabase** (3 connections)
- **Depends** (2 connections)
- **AsyncSession** (1 connections)
- **get_async_session** (1 connections)
- **Response** (1 connections)
- **Strategy** (1 connections)
- **Get user database dependency.** (1 connections) — `server/auth/users.py`
- **Get user manager dependency.** (1 connections) — `server/auth/users.py`
- **Custom login that uses username.** (1 connections) — `server/auth/users.py`
- **Initialize UserManager with validated secrets.** (1 connections) — `server/auth/users.py`
- **Parse a value into a UUID instance.** (1 connections) — `server/auth/users.py`
- **Test getting user database dependency.** (1 connections) — `server/tests/unit/auth/test_users.py`

## Relationships

- [Auth Dependencies & Users](Auth_Dependencies_&_Users.md) (8 shared connections)
- [Community 236](Community_236.md) (8 shared connections)
- [Community 682](Community_682.md) (1 shared connections)
- [Community 1128](Community_1128.md) (1 shared connections)

## Source Files

- `server/auth/users.py`
- `server/tests/unit/auth/test_users.py`

## Audit Trail

- EXTRACTED: 40 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*