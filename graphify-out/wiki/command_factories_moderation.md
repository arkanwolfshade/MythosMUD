# command factories moderation

> 88 nodes

## Key Concepts

- **InviteRead** (15 connections) — `server/schemas/auth/invite.py`
- **test_invite_schemas.py** (15 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **test_endpoints_invites.py** (14 connections) — `server/tests/unit/auth/test_endpoints_invites.py`
- **test_user_schemas.py** (13 connections) — `server/tests/unit/schemas/test_user_schemas.py`
- **__init__.py** (12 connections) — `server/schemas/auth/__init__.py`
- **InviteBase** (10 connections) — `server/schemas/auth/invite.py`
- **SecureBaseModel** (10 connections) — `server/schemas/shared/base.py`
- **InviteUpdate** (9 connections) — `server/schemas/auth/invite.py`
- **user.py** (9 connections) — `server/schemas/auth/user.py`
- **UserUpdate** (9 connections) — `server/schemas/auth/user.py`
- **get_current_user_info()** (8 connections) — `server/auth/endpoints.py`
- **invite.py** (8 connections) — `server/schemas/auth/invite.py`
- **InviteCreate** (8 connections) — `server/schemas/auth/invite.py`
- **UserBase** (8 connections) — `server/schemas/auth/user.py`
- **UserCreate** (8 connections) — `server/schemas/auth/user.py`
- **UserRead** (7 connections) — `server/schemas/auth/user.py`
- **base.py** (6 connections) — `server/schemas/shared/base.py`
- **ResponseBaseModel** (6 connections) — `server/schemas/shared/base.py`
- **test_list_invites()** (5 connections) — `server/tests/unit/auth/test_endpoints_invites.py`
- **test_create_invite()** (5 connections) — `server/tests/unit/auth/test_endpoints_invites.py`
- **test_create_invite_success()** (5 connections) — `server/tests/unit/auth/test_endpoints_invites.py`
- **test_get_current_user_info()** (4 connections) — `server/tests/unit/auth/test_endpoints_invites.py`
- **test_list_invites_empty_list()** (4 connections) — `server/tests/unit/auth/test_endpoints_invites.py`
- **test_list_invites_with_used_invite()** (4 connections) — `server/tests/unit/auth/test_endpoints_invites.py`
- **test_list_invites_with_expired_invite()** (4 connections) — `server/tests/unit/auth/test_endpoints_invites.py`
- *... and 63 more nodes in this community*

## Relationships

- [auth users rationale](auth_users_rationale.md) (14 shared connections)
- [ascii map renderer](ascii_map_renderer.md) (9 shared connections)
- [admin auth service](admin_auth_service.md) (7 shared connections)
- [command inventory models](command_inventory_models.md) (4 shared connections)
- [npc population stats](npc_population_stats.md) (3 shared connections)
- [logging file setup](logging_file_setup.md) (1 shared connections)

## Source Files

- `server/auth/endpoints.py`
- `server/schemas/auth/__init__.py`
- `server/schemas/auth/invite.py`
- `server/schemas/auth/user.py`
- `server/schemas/shared/base.py`
- `server/tests/unit/auth/test_endpoints_invites.py`
- `server/tests/unit/schemas/test_invite_schemas.py`
- `server/tests/unit/schemas/test_user_schemas.py`

## Audit Trail

- EXTRACTED: 300 (97%)
- INFERRED: 10 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*