# InviteManager

> 25 nodes

## Key Concepts

- **InviteManager** (32 connections) — `server/auth/invites.py`
- **test_invite_manager.py** (22 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **asyncio** (12 connections)
- **get_invite_manager()** (11 connections) — `server/auth/invites.py`
- **test_validate_invite_expired()** (5 connections) — `server/tests/unit/auth/test_invite_manager.py`
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
- **.cleanup_expired_invites()** (2 connections) — `server/auth/invites.py`
- **.__init__()** (2 connections) — `server/auth/invites.py`
- **mock_session()** (2 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **AsyncSession** (2 connections)
- **fixture** (1 connections)
- **Remove expired invites and return count of removed invites.** (1 connections) — `server/auth/invites.py`
- **Get invite manager dependency.** (1 connections) — `server/auth/invites.py`
- **Manages invite creation, validation, and tracking. Handles the invite-only…** (1 connections) — `server/auth/invites.py`
- **Unit tests for InviteManager (server.auth.invites).** (1 connections) — `server/tests/unit/auth/test_invite_manager.py`

## Relationships

- [Invite](Invite.md) (11 shared connections)
- [get_logger](get_logger.md) (10 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (5 shared connections)
- [test_endpoints_invites.py](test_endpoints_invites.py.md) (4 shared connections)
- [.validate_invite](validate_invite.md) (3 shared connections)
- [_validate_invite_code](_validate_invite_code.md) (2 shared connections)
- [register_user](register_user.md) (2 shared connections)
- [._generate_invite_code](_generate_invite_code.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/auth/invites.py`
- `server/tests/unit/auth/test_invite_manager.py`

## Audit Trail

- EXTRACTED: 60 (67%)
- INFERRED: 29 (33%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*