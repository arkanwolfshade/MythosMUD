# test_endpoints_invites.py

> 30 nodes

## Key Concepts

- **test_endpoints_invites.py** (15 connections) — `server/tests/unit/auth/test_endpoints_invites.py`
- **list_invites()** (14 connections) — `server/auth/endpoints.py`
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
- **post** (3 connections)
- **get** (2 connections)
- **get_current_active_user** (1 connections)
- **TypedDict** (1 connections)
- **Payload for GET /auth/me.** (1 connections) — `server/auth/endpoints.py`
- **Get current user information. This endpoint returns information about the…** (1 connections) — `server/auth/endpoints.py`
- **List all invite codes. This endpoint returns all invite codes in the system.** (1 connections) — `server/auth/endpoints.py`
- **Create a new invite code. This endpoint creates a new invite code for user…** (1 connections) — `server/auth/endpoints.py`
- **Unit tests for auth invite endpoints and current-user info.** (1 connections) — `server/tests/unit/auth/test_endpoints_invites.py`
- **Test listing invites when list is empty.** (1 connections) — `server/tests/unit/auth/test_endpoints_invites.py`
- **Test listing invites with a used invite.** (1 connections) — `server/tests/unit/auth/test_endpoints_invites.py`
- *... and 5 more nodes in this community*

## Relationships

- [User](User.md) (11 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [InviteManager](InviteManager.md) (4 shared connections)
- [test_invite_schemas.py](test_invite_schemas.py.md) (3 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (2 shared connections)
- [login_user](login_user.md) (2 shared connections)
- [register_user](register_user.md) (2 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/auth/endpoints.py`
- `server/tests/unit/auth/test_endpoints_invites.py`

## Audit Trail

- EXTRACTED: 66 (88%)
- INFERRED: 9 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*