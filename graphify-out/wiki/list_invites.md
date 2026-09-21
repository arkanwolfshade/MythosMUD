# list_invites

> 36 nodes

## Key Concepts

- **list_invites()** (14 connections) — `server/auth/endpoints.py`
- **test_endpoints_invites.py** (14 connections) — `server/tests/unit/auth/test_endpoints_invites.py`
- **InviteRead** (12 connections) — `server/schemas/auth/invite.py`
- **create_invite()** (12 connections) — `server/auth/endpoints.py`
- **get_current_user_info()** (9 connections) — `server/auth/endpoints.py`
- **asyncio** (7 connections)
- **test_create_invite()** (5 connections) — `server/tests/unit/auth/test_endpoints_invites.py`
- **test_create_invite_success()** (5 connections) — `server/tests/unit/auth/test_endpoints_invites.py`
- **test_get_current_user_info()** (5 connections) — `server/tests/unit/auth/test_endpoints_invites.py`
- **test_list_invites()** (5 connections) — `server/tests/unit/auth/test_endpoints_invites.py`
- **test_list_invites_empty_list()** (5 connections) — `server/tests/unit/auth/test_endpoints_invites.py`
- **test_list_invites_with_expired_invite()** (5 connections) — `server/tests/unit/auth/test_endpoints_invites.py`
- **test_list_invites_with_used_invite()** (5 connections) — `server/tests/unit/auth/test_endpoints_invites.py`
- **Depends** (5 connections)
- **CurrentUserInfo** (4 connections) — `server/auth/endpoints.py`
- **test_invite_read()** (3 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **test_invite_read_with_used_by()** (3 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **post** (3 connections)
- **get** (2 connections)
- **get_current_active_user** (1 connections)
- **TypedDict** (1 connections)
- **Payload for GET /auth/me.** (1 connections) — `server/auth/endpoints.py`
- **Get current user information. This endpoint returns information about the…** (1 connections) — `server/auth/endpoints.py`
- **List all invite codes. This endpoint returns all invite codes in the system.** (1 connections) — `server/auth/endpoints.py`
- **Create a new invite code. This endpoint creates a new invite code for user…** (1 connections) — `server/auth/endpoints.py`
- *... and 11 more nodes in this community*

## Relationships

- [User](User.md) (12 shared connections)
- [endpoints.py](endpoints.py.md) (7 shared connections)
- [SecureBaseModel](SecureBaseModel.md) (6 shared connections)
- [Invite](Invite.md) (6 shared connections)
- [register_user](register_user.md) (2 shared connections)
- [PlayerService](PlayerService.md) (1 shared connections)

## Source Files

- `server/auth/endpoints.py`
- `server/schemas/auth/invite.py`
- `server/tests/unit/auth/test_endpoints_invites.py`
- `server/tests/unit/schemas/test_invite_schemas.py`

## Audit Trail

- EXTRACTED: 78 (90%)
- INFERRED: 9 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*