# get user db()

> 8 nodes

## Key Concepts

- **get_user_db()** (7 connections) — `server/auth/users.py`
- **.__init__()** (4 connections) — `server/auth/users.py`
- **SQLAlchemyUserDatabase** (3 connections)
- **test_get_user_db()** (3 connections) — `server/tests/unit/auth/test_users.py`
- **AsyncSession** (1 connections)
- **Initialize UserManager with validated secrets.** (1 connections) — `server/auth/users.py`
- **Get user database dependency.** (1 connections) — `server/auth/users.py`
- **Test getting user database dependency.** (1 connections) — `server/tests/unit/auth/test_users.py`

## Relationships

- [Custom user manager for MythosMUD.](Custom_user_manager_for_MythosMUD.md) (3 shared connections)
- [BaseUserManager](BaseUserManager.md) (2 shared connections)
- [AuthenticationBackend](AuthenticationBackend.md) (1 shared connections)
- [APIRouter](APIRouter.md) (1 shared connections)

## Source Files

- `server/auth/users.py`
- `server/tests/unit/auth/test_users.py`

## Audit Trail

- EXTRACTED: 20 (95%)
- INFERRED: 1 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*