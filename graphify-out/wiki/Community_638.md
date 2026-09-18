# Community 638

> 26 nodes

## Key Concepts

- **get_user_manager()** (13 connections) — `server/auth/users.py`
- **get_user_db()** (11 connections) — `server/auth/users.py`
- **User** (8 connections)
- **UUID** (7 connections)
- **.login()** (6 connections) — `server/auth/users.py`
- **.__init__()** (5 connections) — `server/auth/users.py`
- **.on_after_forgot_password()** (4 connections) — `server/auth/users.py`
- **.on_after_register()** (4 connections) — `server/auth/users.py`
- **.on_after_request_verify()** (4 connections) — `server/auth/users.py`
- **test_get_user_db()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **.parse_id()** (3 connections) — `server/auth/users.py`
- **Request** (3 connections)
- **SQLAlchemyUserDatabase** (3 connections)
- **Depends** (2 connections)
- **Response** (1 connections)
- **AsyncSession** (1 connections)
- **Strategy** (1 connections)
- **Get user database dependency.** (1 connections) — `server/auth/users.py`
- **Get user manager dependency.** (1 connections) — `server/auth/users.py`
- **Custom login that uses username.** (1 connections) — `server/auth/users.py`
- **Initialize UserManager with validated secrets.** (1 connections) — `server/auth/users.py`
- **Handle post-registration logic.** (1 connections) — `server/auth/users.py`
- **Handle forgot password logic.** (1 connections) — `server/auth/users.py`
- **Handle username verification logic.** (1 connections) — `server/auth/users.py`
- **Parse a value into a UUID instance.** (1 connections) — `server/auth/users.py`
- *... and 1 more nodes in this community*

## Relationships

- [Community 145](Community_145.md) (12 shared connections)
- [Character Creation & Auth Dependencies](Character_Creation_&_Auth_Dependencies.md) (4 shared connections)
- [User Manager & Character Info](User_Manager_&_Character_Info.md) (2 shared connections)
- [Community 1099](Community_1099.md) (2 shared connections)
- [Community 161](Community_161.md) (1 shared connections)

## Source Files

- `server/auth/users.py`
- `server/tests/unit/auth/test_users.py`

## Audit Trail

- EXTRACTED: 55 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*