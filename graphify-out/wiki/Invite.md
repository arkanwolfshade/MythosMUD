# Invite

> 138 nodes

## Key Concepts

- **Invite** (49 connections) — `server/models/invite.py`
- **InviteManager** (33 connections) — `server/auth/invites.py`
- **test_auth_dependencies.py** (24 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_invite_manager.py** (23 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **invites.py** (21 connections) — `server/auth/invites.py`
- **auth/dependencies.py** (18 connections) — `server/auth/dependencies.py`
- **test_invite.py** (17 connections) — `server/tests/unit/models/test_invite.py`
- **asyncio** (14 connections)
- **asyncio** (14 connections)
- **get_current_superuser()** (12 connections) — `server/auth/dependencies.py`
- **require_invite_code()** (11 connections) — `server/auth/dependencies.py`
- **get_invite_manager()** (11 connections) — `server/auth/invites.py`
- **models/invite.py** (11 connections) — `server/models/invite.py`
- **get_current_verified_user()** (8 connections) — `server/auth/dependencies.py`
- **capture_invite()** (7 connections) — `server/auth/invites.py`
- **server/auth/__init__.py** (7 connections) — `server/auth/__init__.py`
- **get_optional_current_user()** (6 connections) — `server/auth/dependencies.py`
- **reserve_invite()** (6 connections) — `server/auth/invites.py`
- **.create_invite()** (6 connections) — `server/models/invite.py`
- **._generate_invite_code()** (6 connections) — `server/models/invite.py`
- **test_get_current_superuser_failure()** (6 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_get_current_superuser_with_none_user()** (6 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_get_current_verified_user_failure()** (6 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_get_current_verified_user_with_none_user()** (6 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **.use_invite()** (5 connections) — `server/auth/invites.py`
- *... and 113 more nodes in this community*

## Relationships

- [LoggedHTTPException](LoggedHTTPException.md) (24 shared connections)
- [User](User.md) (21 shared connections)
- [endpoints.py](endpoints.py.md) (11 shared connections)
- [list_invites](list_invites.md) (6 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [models/player.py](models-player.py.md) (5 shared connections)
- [register_user](register_user.md) (4 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (3 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (2 shared connections)
- [DatabaseManager](DatabaseManager.md) (1 shared connections)
- [.__init__](__init__.md) (1 shared connections)
- [subject_controller.py](subject_controller.py.md) (1 shared connections)

## Source Files

- `server/auth/__init__.py`
- `server/auth/dependencies.py`
- `server/auth/invites.py`
- `server/models/invite.py`
- `server/tests/unit/auth/test_auth_dependencies.py`
- `server/tests/unit/auth/test_invite_manager.py`
- `server/tests/unit/models/test_invite.py`

## Audit Trail

- EXTRACTED: 284 (84%)
- INFERRED: 54 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*