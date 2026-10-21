# test_admin_setlucidity_command.py

> 91 nodes · cohesion 0.04

## Key Concepts

- **Invite** (49 connections) — `server/models/invite.py`
- **InviteManager** (33 connections) — `server/auth/invites.py`
- **test_invite_manager.py** (23 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **invites.py** (21 connections) — `server/auth/invites.py`
- **test_invite.py** (17 connections) — `server/tests/unit/models/test_invite.py`
- **asyncio** (14 connections)
- **get_invite_manager()** (11 connections) — `server/auth/invites.py`
- **models/invite.py** (11 connections) — `server/models/invite.py`
- **server/auth/__init__.py** (7 connections) — `server/auth/__init__.py`
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
- **AsyncSession** (4 connections)
- **test_cleanup_expired_invites()** (4 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **test_create_invite_explicit_expiry()** (4 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **test_create_invite_with_default_expiry()** (4 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **test_get_invite_manager_dependency()** (4 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **test_get_unused_invites()** (4 connections) — `server/tests/unit/auth/test_invite_manager.py`
- *... and 66 more nodes in this community*

## Relationships

- [useGameConnectionRefactored.ts](useGameConnectionRefactored.ts.md) (16 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (9 shared connections)
- [schema.sql](schema.sql.md) (5 shared connections)
- [useMythosAppActions.ts](useMythosAppActions.ts.md) (4 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (4 shared connections)
- [test_channel_commands.py](test_channel_commands.py.md) (3 shared connections)
- [._create_grid_map](_create_grid_map.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)
- [AttributeError](AttributeError.md) (2 shared connections)
- [test_active_lucidity_service.py](test_active_lucidity_service.py.md) (2 shared connections)
- [ItemFactory](ItemFactory.md) (1 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (1 shared connections)

## Source Files

- `server/auth/__init__.py`
- `server/auth/invites.py`
- `server/models/invite.py`
- `server/tests/unit/auth/test_invite_manager.py`
- `server/tests/unit/models/test_invite.py`

## Audit Trail

- EXTRACTED: 182 (82%)
- INFERRED: 39 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*