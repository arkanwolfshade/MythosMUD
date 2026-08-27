# enum

> 35 nodes

## Key Concepts

- **InviteManager** (27 connections) — `server/auth/invites.py`
- **test_invite_manager.py** (22 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **asyncio** (12 connections)
- **get_invite_manager()** (7 connections) — `server/auth/invites.py`
- **.validate_invite()** (6 connections) — `server/auth/invites.py`
- **.use_invite()** (5 connections) — `server/auth/invites.py`
- **test_validate_invite_expired()** (5 connections) — `server/tests/unit/auth/test_invite_manager.py`
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
- **test_validate_invite_not_found()** (4 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **test_validate_invite_success()** (4 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **.get_unused_invites()** (3 connections) — `server/auth/invites.py`
- **UUID** (3 connections)
- **.cleanup_expired_invites()** (2 connections) — `server/auth/invites.py`
- **.__init__()** (2 connections) — `server/auth/invites.py`
- **mock_session()** (2 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **AsyncSession** (2 connections)
- *... and 10 more nodes in this community*

## Relationships

- [Test Suite Refactoring Plan](Test_Suite_Refactoring_Plan.md) (16 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (5 shared connections)
- [NPCSpawningService](NPCSpawningService.md) (5 shared connections)
- [test_player_position_service.py](test_player_position_service.py.md) (3 shared connections)
- [models/container.py](models-container.py.md) (1 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (1 shared connections)

## Source Files

- `server/auth/invites.py`
- `server/tests/unit/auth/test_invite_manager.py`

## Audit Trail

- EXTRACTED: 69 (73%)
- INFERRED: 25 (27%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*