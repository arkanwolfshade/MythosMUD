# Request

> 5 nodes

## Key Concepts

- **.on_after_forgot_password()** (4 connections) — `server/auth/users.py`
- **.on_after_request_verify()** (4 connections) — `server/auth/users.py`
- **Request** (3 connections)
- **Handle forgot password logic.** (1 connections) — `server/auth/users.py`
- **Handle username verification logic.** (1 connections) — `server/auth/users.py`

## Relationships

- [Custom user manager for MythosMUD.](Custom_user_manager_for_MythosMUD.md) (2 shared connections)
- [APIRouter](APIRouter.md) (2 shared connections)
- [BaseUserManager](BaseUserManager.md) (1 shared connections)

## Source Files

- `server/auth/users.py`

## Audit Trail

- EXTRACTED: 13 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*