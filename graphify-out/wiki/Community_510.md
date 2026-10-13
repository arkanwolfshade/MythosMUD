# Community 510

> 34 nodes

## Key Concepts

- **Invite** (49 connections) — `server/models/invite.py`
- **test_invite.py** (17 connections) — `server/tests/unit/models/test_invite.py`
- **.create_invite()** (6 connections) — `server/models/invite.py`
- **test_invite_create_invite_defaults()** (4 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_create_invite_with_creator()** (4 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_create_invite_with_custom_expiry()** (4 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_is_expired_with_aware_datetime()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_is_expired_with_future_expiry()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_is_expired_with_past_expiry()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_is_valid_with_active_and_not_expired()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_is_valid_with_expired()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_is_valid_with_inactive()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_is_valid_with_inactive_and_expired()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_repr()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_use_invite()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **.list_invites()** (2 connections) — `server/auth/invites.py`
- **.use_invite()** (2 connections) — `server/models/invite.py`
- **Test is_valid returns False for expired invite.** (2 connections) — `server/tests/unit/models/test_invite.py`
- **.__repr__()** (1 connections) — `server/models/invite.py`
- **Base** (1 connections)
- **Model for user registration invites.** (1 connections) — `server/models/invite.py`
- **Mark this invite as used by a specific user.** (1 connections) — `server/models/invite.py`
- **Create a new invite with the specified parameters.** (1 connections) — `server/models/invite.py`
- **Unit tests for the Invite model. Tests the Invite model methods including…** (1 connections) — `server/tests/unit/models/test_invite.py`
- **Test create_invite creates invite with creator user_id.** (1 connections) — `server/tests/unit/models/test_invite.py`
- *... and 9 more nodes in this community*

## Relationships

- [Community 610](Community_610.md) (11 shared connections)
- [Community 1321](Community_1321.md) (7 shared connections)
- [Auth Dependencies & Users](Auth_Dependencies_&_Users.md) (5 shared connections)
- [Community 870](Community_870.md) (2 shared connections)
- [Community 1493](Community_1493.md) (2 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (2 shared connections)
- [Community 1586](Community_1586.md) (2 shared connections)
- [Community 1781](Community_1781.md) (1 shared connections)
- [Core Bundle & DB Init](Core_Bundle_&_DB_Init.md) (1 shared connections)
- [Community 1680](Community_1680.md) (1 shared connections)
- [Community 1496](Community_1496.md) (1 shared connections)

## Source Files

- `server/auth/invites.py`
- `server/models/invite.py`
- `server/tests/unit/models/test_invite.py`

## Audit Trail

- EXTRACTED: 68 (81%)
- INFERRED: 16 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*