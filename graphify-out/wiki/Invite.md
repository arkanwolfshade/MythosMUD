# Invite

> 88 nodes

## Key Concepts

- **Invite** (52 connections) — `server/models/invite.py`
- **InviteManager** (32 connections) — `server/auth/invites.py`
- **test_invite_manager.py** (22 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **invites.py** (19 connections) — `server/auth/invites.py`
- **test_invite.py** (17 connections) — `server/tests/unit/models/test_invite.py`
- **models/invite.py** (13 connections) — `server/models/invite.py`
- **asyncio** (12 connections)
- **get_invite_manager()** (11 connections) — `server/auth/invites.py`
- **_validate_invite_code()** (7 connections) — `server/auth/endpoints.py`
- **.validate_invite()** (6 connections) — `server/auth/invites.py`
- **.create_invite()** (6 connections) — `server/models/invite.py`
- **._generate_invite_code()** (6 connections) — `server/models/invite.py`
- **.use_invite()** (5 connections) — `server/auth/invites.py`
- **test_validate_invite_expired()** (5 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **.create_invite()** (4 connections) — `server/auth/invites.py`
- **.get_user_invites()** (4 connections) — `server/auth/invites.py`
- **test_cleanup_expired_invites()** (4 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **test_create_invite_explicit_expiry()** (4 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **test_create_invite_with_default_expiry()** (4 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **test_get_invite_manager_dependency()** (4 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **test_get_unused_invites()** (4 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **test_get_user_invites()** (4 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **test_list_invites()** (4 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **test_use_invite()** (4 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **test_validate_invite_missing_code()** (4 connections) — `server/tests/unit/auth/test_invite_manager.py`
- *... and 63 more nodes in this community*

## Relationships

- [User](User.md) (19 shared connections)
- [get_session_maker](get_session_maker.md) (9 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (6 shared connections)
- [test_invite_schemas.py](test_invite_schemas.py.md) (4 shared connections)
- [register_user](register_user.md) (4 shared connections)
- [database_config_helpers.py](database_config_helpers.py.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [DatabaseError](DatabaseError.md) (2 shared connections)
- [DatabaseManager](DatabaseManager.md) (1 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/auth/endpoints.py`
- `server/auth/invites.py`
- `server/models/invite.py`
- `server/tests/unit/auth/test_invite_manager.py`
- `server/tests/unit/models/test_invite.py`

## Audit Trail

- EXTRACTED: 167 (78%)
- INFERRED: 46 (22%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*