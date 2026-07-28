# Lucidity Database Models

> 67 nodes · cohesion 0.05

## Key Concepts

- **test_invite_schemas.py** (15 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **test_user_schemas.py** (13 connections) — `server/tests/unit/schemas/test_user_schemas.py`
- **__init__.py** (12 connections) — `server/schemas/auth/__init__.py`
- **InviteBase** (10 connections) — `server/schemas/auth/invite.py`
- **SecureBaseModel** (10 connections) — `server/schemas/shared/base.py`
- **InviteUpdate** (9 connections) — `server/schemas/auth/invite.py`
- **user.py** (9 connections) — `server/schemas/auth/user.py`
- **UserUpdate** (9 connections) — `server/schemas/auth/user.py`
- **invite.py** (8 connections) — `server/schemas/auth/invite.py`
- **InviteCreate** (8 connections) — `server/schemas/auth/invite.py`
- **UserBase** (8 connections) — `server/schemas/auth/user.py`
- **UserCreate** (8 connections) — `server/schemas/auth/user.py`
- **UserRead** (7 connections) — `server/schemas/auth/user.py`
- **base.py** (6 connections) — `server/schemas/shared/base.py`
- **ResponseBaseModel** (6 connections) — `server/schemas/shared/base.py`
- **test_invite_base_validation()** (4 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **test_invite_update_validation()** (4 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **test_user_create_password_validation()** (4 connections) — `server/tests/unit/schemas/test_user_schemas.py`
- **test_user_update_password_validation()** (4 connections) — `server/tests/unit/schemas/test_user_schemas.py`
- **test_invite_base()** (3 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **test_invite_base_defaults()** (3 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **test_invite_create()** (3 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **test_invite_create_no_expiry()** (3 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **test_invite_read()** (3 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **test_invite_read_with_used_by()** (3 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- *... and 42 more nodes in this community*

## Relationships

- [System Monitoring API](System_Monitoring_API.md) (6 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (6 shared connections)
- [Api Player Respawn](Api_Player_Respawn.md) (4 shared connections)
- [Commands Admin Shutdown](Commands_Admin_Shutdown.md) (3 shared connections)

## Source Files

- `server/schemas/auth/__init__.py`
- `server/schemas/auth/invite.py`
- `server/schemas/auth/user.py`
- `server/schemas/shared/base.py`
- `server/tests/unit/schemas/test_invite_schemas.py`
- `server/tests/unit/schemas/test_user_schemas.py`

## Audit Trail

- EXTRACTED: 227 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*