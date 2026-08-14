# Invite

> 147 nodes

## Key Concepts

- **Invite** (38 connections) — `server/models/invite.py`
- **InviteManager** (37 connections) — `server/auth/invites.py`
- **test_auth_dependencies.py** (24 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_invite_manager.py** (21 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **auth/dependencies.py** (18 connections) — `server/auth/dependencies.py`
- **invites.py** (17 connections) — `server/auth/invites.py`
- **test_invite.py** (17 connections) — `server/tests/unit/models/test_invite.py`
- **asyncio** (14 connections)
- **generate_invites_db.py** (14 connections) — `tools/invite_tools/generate_invites_db.py`
- **get_current_superuser()** (12 connections) — `server/auth/dependencies.py`
- **models/invite.py** (12 connections) — `server/models/invite.py`
- **asyncio** (12 connections)
- **require_invite_code()** (11 connections) — `server/auth/dependencies.py`
- **get_invite_manager()** (11 connections) — `server/auth/invites.py`
- **get_current_verified_user()** (8 connections) — `server/auth/dependencies.py`
- **main()** (7 connections) — `tools/invite_tools/generate_invites_db.py`
- **server/auth/__init__.py** (7 connections) — `server/auth/__init__.py`
- **get_optional_current_user()** (6 connections) — `server/auth/dependencies.py`
- **.validate_invite()** (6 connections) — `server/auth/invites.py`
- **normalize_database_url()** (6 connections) — `server/database_config_helpers.py`
- **.create_invite()** (6 connections) — `server/models/invite.py`
- **._generate_invite_code()** (6 connections) — `server/models/invite.py`
- **create_invite_in_db()** (6 connections) — `tools/invite_tools/generate_invites_db.py`
- **.use_invite()** (5 connections) — `server/auth/invites.py`
- **test_get_current_superuser_failure()** (5 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- *... and 122 more nodes in this community*

## Relationships

- [User](User.md) (36 shared connections)
- [get_logger](get_logger.md) (26 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (9 shared connections)
- [Player](Player.md) (5 shared connections)
- [factory.py](factory.py.md) (2 shared connections)
- [test_users.py](test_users.py.md) (2 shared connections)
- [.__init__](__init__.md) (1 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (1 shared connections)

## Source Files

- `server/auth/__init__.py`
- `server/auth/dependencies.py`
- `server/auth/invites.py`
- `server/database_config_helpers.py`
- `server/models/invite.py`
- `server/tests/unit/auth/test_auth_dependencies.py`
- `server/tests/unit/auth/test_invite_manager.py`
- `server/tests/unit/models/test_invite.py`
- `tools/invite_tools/generate_invites_db.py`

## Audit Trail

- EXTRACTED: 325 (98%)
- INFERRED: 8 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*