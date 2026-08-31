# InviteManager

> 26 nodes

## Key Concepts

- **InviteManager** (33 connections) — `server/auth/invites.py`
- **test_invite_manager.py** (24 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **asyncio** (14 connections)
- **get_invite_manager()** (11 connections) — `server/auth/invites.py`
- **test_use_invite()** (5 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **test_use_invite_capture_rejected()** (5 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **test_use_invite_reserve_rejected()** (5 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **test_validate_invite_expired()** (5 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **test_cleanup_expired_invites()** (4 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **test_create_invite_explicit_expiry()** (4 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **test_create_invite_with_default_expiry()** (4 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **test_get_invite_manager_dependency()** (4 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **test_get_unused_invites()** (4 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **test_get_user_invites()** (4 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **test_list_invites()** (4 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **test_validate_invite_missing_code()** (4 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **test_validate_invite_not_found()** (4 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **test_validate_invite_success()** (4 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **AsyncSession** (4 connections)
- **.__init__()** (2 connections) — `server/auth/invites.py`
- **Manages invite creation, validation, and tracking. Handles the invite-only…** (1 connections) — `server/auth/invites.py`
- **Get invite manager dependency.** (1 connections) — `server/auth/invites.py`
- **Unit tests for InviteManager (server.auth.invites).** (1 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **use_invite reserves, captures, commits, then re-fetches the row (3 execute()…** (1 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **A code that isn't reservable (unknown/already used) is rejected before any…** (1 connections) — `server/tests/unit/auth/test_invite_manager.py`
- *... and 1 more nodes in this community*

## Relationships

- [LoggedHTTPException](LoggedHTTPException.md) (23 shared connections)
- [Invite](Invite.md) (11 shared connections)
- [.use_invite](use_invite.md) (2 shared connections)
- [RestartInvalidatingJWTStrategy](RestartInvalidatingJWTStrategy.md) (1 shared connections)
- [.get_unused_invites](get_unused_invites.md) (1 shared connections)
- [.cleanup_expired_invites](cleanup_expired_invites.md) (1 shared connections)
- [._generate_invite_code](_generate_invite_code.md) (1 shared connections)
- [.validate_invite](validate_invite.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [mock_session](mock_session.md) (1 shared connections)

## Source Files

- `server/auth/invites.py`
- `server/tests/unit/auth/test_invite_manager.py`

## Audit Trail

- EXTRACTED: 67 (68%)
- INFERRED: 32 (32%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*