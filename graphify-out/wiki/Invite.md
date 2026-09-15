# Invite

> 128 nodes

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
- **require_invite_code()** (11 connections) — `server/auth/dependencies.py`
- **get_invite_manager()** (11 connections) — `server/auth/invites.py`
- **models/invite.py** (11 connections) — `server/models/invite.py`
- **get_current_verified_user()** (8 connections) — `server/auth/dependencies.py`
- **server/auth/__init__.py** (7 connections) — `server/auth/__init__.py`
- **get_optional_current_user()** (6 connections) — `server/auth/dependencies.py`
- **.create_invite()** (6 connections) — `server/models/invite.py`
- **._generate_invite_code()** (6 connections) — `server/models/invite.py`
- **test_get_current_verified_user_failure()** (6 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_get_current_verified_user_with_none_user()** (6 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **.use_invite()** (5 connections) — `server/auth/invites.py`
- **.validate_invite()** (5 connections) — `server/auth/invites.py`
- **test_get_current_superuser_success()** (5 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_get_current_verified_user_success()** (5 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_get_optional_current_user_with_user()** (5 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_require_invite_code_generic_exception()** (5 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- *... and 103 more nodes in this community*

## Relationships

- [LoggedHTTPException](LoggedHTTPException.md) (40 shared connections)
- [User](User.md) (17 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [Player](Player.md) (5 shared connections)
- [get_session_maker](get_session_maker.md) (3 shared connections)
- [DatabaseManager](DatabaseManager.md) (2 shared connections)
- [test_users.py](test_users.py.md) (2 shared connections)
- [.__init__](__init__.md) (1 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (1 shared connections)
- [api/game.py](api-game.py.md) (1 shared connections)

## Source Files

- `server/auth/__init__.py`
- `server/auth/dependencies.py`
- `server/auth/invites.py`
- `server/models/invite.py`
- `server/tests/unit/auth/test_auth_dependencies.py`
- `server/tests/unit/auth/test_invite_manager.py`
- `server/tests/unit/models/test_invite.py`

## Audit Trail

- EXTRACTED: 264 (84%)
- INFERRED: 50 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*