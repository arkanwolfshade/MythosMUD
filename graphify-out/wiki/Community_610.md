# Community 610

> 28 nodes

## Key Concepts

- **InviteManager** (29 connections) — `server/auth/invites.py`
- **test_invite_manager.py** (23 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **asyncio** (14 connections)
- **get_invite_manager()** (7 connections) — `server/auth/invites.py`
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
- **mock_session()** (2 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **fixture** (1 connections)
- **Manages invite creation, validation, and tracking. Handles the invite-only…** (1 connections) — `server/auth/invites.py`
- **Get invite manager dependency.** (1 connections) — `server/auth/invites.py`
- **Unit tests for InviteManager (server.auth.invites).** (1 connections) — `server/tests/unit/auth/test_invite_manager.py`
- *... and 3 more nodes in this community*

## Relationships

- [Community 510](Community_510.md) (11 shared connections)
- [Auth Dependencies & Users](Auth_Dependencies_&_Users.md) (10 shared connections)
- [Container API Models](Container_API_Models.md) (6 shared connections)
- [Community 1493](Community_1493.md) (2 shared connections)
- [Community 1781](Community_1781.md) (1 shared connections)
- [Community 1780](Community_1780.md) (1 shared connections)
- [Community 1321](Community_1321.md) (1 shared connections)
- [Community 1680](Community_1680.md) (1 shared connections)
- [Invite & NPC DB Scripts](Invite_&_NPC_DB_Scripts.md) (1 shared connections)

## Source Files

- `server/auth/invites.py`
- `server/tests/unit/auth/test_invite_manager.py`

## Audit Trail

- EXTRACTED: 62 (68%)
- INFERRED: 29 (32%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*