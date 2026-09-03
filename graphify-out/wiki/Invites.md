# Invites

> 49 nodes

## Key Concepts

- **InviteManager** (33 connections) — `server/auth/invites.py`
- **test_invite_manager.py** (22 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **invites.py** (19 connections) — `server/auth/invites.py`
- **asyncio** (14 connections)
- **get_invite_manager()** (11 connections) — `server/auth/invites.py`
- **capture_invite()** (7 connections) — `server/auth/invites.py`
- **Invite** (6 connections)
- **.use_invite()** (5 connections) — `server/auth/invites.py`
- **.validate_invite()** (5 connections) — `server/auth/invites.py`
- **.get_user_invites()** (4 connections) — `server/auth/invites.py`
- **test_get_invite_manager_dependency()** (4 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **test_use_invite()** (4 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **test_use_invite_capture_rejected()** (4 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **test_use_invite_reserve_rejected()** (4 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **AsyncSession** (4 connections)
- **.create_invite()** (3 connections) — `server/auth/invites.py`
- **.get_unused_invites()** (3 connections) — `server/auth/invites.py`
- **test_cleanup_expired_invites()** (3 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **test_create_invite_explicit_expiry()** (3 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **test_create_invite_with_default_expiry()** (3 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **test_get_unused_invites()** (3 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **test_get_user_invites()** (3 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **test_list_invites()** (3 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **test_validate_invite_expired()** (3 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **test_validate_invite_missing_code()** (3 connections) — `server/tests/unit/auth/test_invite_manager.py`
- *... and 24 more nodes in this community*

## Relationships

- [Test Endpoints Register](Test_Endpoints_Register.md) (9 shared connections)
- [Test Auth Dependencies](Test_Auth_Dependencies.md) (4 shared connections)
- [Test Endpoints Invites](Test_Endpoints_Invites.md) (4 shared connections)
- [Players](Players.md) (3 shared connections)
- [Player Model & Migrations](Player_Model_&_Migrations.md) (3 shared connections)
- [Test Users](Test_Users.md) (2 shared connections)
- [Error Handling & Exceptions](Error_Handling_&_Exceptions.md) (2 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (2 shared connections)
- [Async Persistence Direct Queries](Async_Persistence_Direct_Queries.md) (1 shared connections)
- [Correlation Middleware](Correlation_Middleware.md) (1 shared connections)
- [Database](Database.md) (1 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (1 shared connections)

## Source Files

- `server/auth/invites.py`
- `server/tests/unit/auth/test_invite_manager.py`

## Audit Trail

- EXTRACTED: 101 (83%)
- INFERRED: 21 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*