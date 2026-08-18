# server schemas auth init

> 67 nodes

## Key Concepts

- **test_invite_schemas.py** (17 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **test_user_schemas.py** (15 connections) — `server/tests/unit/schemas/test_user_schemas.py`
- **schemas/auth/__init__.py** (13 connections) — `server/schemas/auth/__init__.py`
- **InviteRead** (12 connections) — `server/schemas/auth/invite.py`
- **InviteBase** (10 connections) — `server/schemas/auth/invite.py`
- **SecureBaseModel** (10 connections) — `server/schemas/shared/base.py`
- **auth/user.py** (10 connections) — `server/schemas/auth/user.py`
- **InviteUpdate** (9 connections) — `server/schemas/auth/invite.py`
- **UserUpdate** (9 connections) — `server/schemas/auth/user.py`
- **auth/invite.py** (9 connections) — `server/schemas/auth/invite.py`
- **InviteCreate** (8 connections) — `server/schemas/auth/invite.py`
- **UserBase** (8 connections) — `server/schemas/auth/user.py`
- **UserCreate** (8 connections) — `server/schemas/auth/user.py`
- **UserRead** (7 connections) — `server/schemas/auth/user.py`
- **shared/base.py** (7 connections) — `server/schemas/shared/base.py`
- **ResponseBaseModel** (6 connections) — `server/schemas/shared/base.py`
- **test_invite_base()** (3 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **test_invite_base_defaults()** (3 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **test_invite_base_validation()** (3 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **test_invite_create()** (3 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **test_invite_create_no_expiry()** (3 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **test_invite_read()** (3 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **test_invite_read_with_used_by()** (3 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **test_invite_update()** (3 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **test_invite_update_all_optional()** (3 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- *... and 42 more nodes in this community*

## Relationships

- [server api admin npc instances](server_api_admin_npc_instances.md) (7 shared connections)
- [baseusermanager](baseusermanager.md) (5 shared connections)
- [claude rules pydantic](claude_rules_pydantic.md) (5 shared connections)
- [server schemas shared init](server_schemas_shared_init.md) (3 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (2 shared connections)

## Source Files

- `server/schemas/auth/__init__.py`
- `server/schemas/auth/invite.py`
- `server/schemas/auth/user.py`
- `server/schemas/shared/base.py`
- `server/tests/unit/schemas/test_invite_schemas.py`
- `server/tests/unit/schemas/test_user_schemas.py`

## Audit Trail

- EXTRACTED: 135 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*