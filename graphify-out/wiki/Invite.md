# Invite

> 91 nodes

## Key Concepts

- **Invite** (49 connections) — `server/models/invite.py`
- **InviteManager** (33 connections) — `server/auth/invites.py`
- **test_invite_manager.py** (23 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **invites.py** (21 connections) — `server/auth/invites.py`
- **test_invite.py** (17 connections) — `server/tests/unit/models/test_invite.py`
- **asyncio** (14 connections)
- **get_invite_manager()** (11 connections) — `server/auth/invites.py`
- **reserve_invite()** (6 connections) — `server/auth/invites.py`
- **.create_invite()** (6 connections) — `server/models/invite.py`
- **._generate_invite_code()** (6 connections) — `server/models/invite.py`
- **.use_invite()** (5 connections) — `server/auth/invites.py`
- **.validate_invite()** (5 connections) — `server/auth/invites.py`
- **test_use_invite()** (5 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **test_use_invite_capture_rejected()** (5 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **test_use_invite_reserve_rejected()** (5 connections) — `server/tests/unit/auth/test_invite_manager.py`
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
- *... and 66 more nodes in this community*

## Relationships

- [User](User.md) (18 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (10 shared connections)
- [server/models/__init__.py](server-models-__init__.py.md) (6 shared connections)
- [register_user](register_user.md) (3 shared connections)
- [get_session_maker](get_session_maker.md) (2 shared connections)
- [Player](Player.md) (2 shared connections)
- [DatabaseManager](DatabaseManager.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (2 shared connections)
- [test_database_helpers.py](test_database_helpers.py.md) (1 shared connections)
- [.__init__](__init__.md) (1 shared connections)

## Source Files

- `server/auth/invites.py`
- `server/models/invite.py`
- `server/tests/unit/auth/test_invite_manager.py`
- `server/tests/unit/models/test_invite.py`

## Audit Trail

- EXTRACTED: 174 (82%)
- INFERRED: 39 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*