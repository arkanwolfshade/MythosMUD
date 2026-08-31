# Invite

> 27 nodes

## Key Concepts

- **Invite** (49 connections) — `server/models/invite.py`
- **test_invite.py** (17 connections) — `server/tests/unit/models/test_invite.py`
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
- **.__repr__()** (1 connections) — `server/models/invite.py`
- **Base** (1 connections)
- **Model for user registration invites.** (1 connections) — `server/models/invite.py`
- **Mark this invite as used by a specific user.** (1 connections) — `server/models/invite.py`
- **Unit tests for the Invite model. Tests the Invite model methods including…** (1 connections) — `server/tests/unit/models/test_invite.py`
- **Test is_expired returns False for future expiry date.** (1 connections) — `server/tests/unit/models/test_invite.py`
- **Test __repr__ returns expected string format.** (1 connections) — `server/tests/unit/models/test_invite.py`
- **Test is_expired returns True for past expiry date.** (1 connections) — `server/tests/unit/models/test_invite.py`
- **Test is_expired handles timezone-aware datetime.** (1 connections) — `server/tests/unit/models/test_invite.py`
- **Test is_valid returns True for active, non-expired invite.** (1 connections) — `server/tests/unit/models/test_invite.py`
- **Test is_valid returns False for inactive invite.** (1 connections) — `server/tests/unit/models/test_invite.py`
- **Test is_valid returns False for expired invite.** (1 connections) — `server/tests/unit/models/test_invite.py`
- *... and 2 more nodes in this community*

## Relationships

- [InviteManager](InviteManager.md) (11 shared connections)
- [.create_invite](create_invite.md) (7 shared connections)
- [._generate_invite_code](_generate_invite_code.md) (6 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (5 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (2 shared connections)
- [.use_invite](use_invite.md) (2 shared connections)
- [Player](Player.md) (2 shared connections)
- [.is_expired](is_expired.md) (2 shared connections)
- [.get_unused_invites](get_unused_invites.md) (1 shared connections)
- [DatabaseManager](DatabaseManager.md) (1 shared connections)
- [.validate_invite](validate_invite.md) (1 shared connections)
- [.__init__](__init__.md) (1 shared connections)

## Source Files

- `server/auth/invites.py`
- `server/models/invite.py`
- `server/tests/unit/models/test_invite.py`

## Audit Trail

- EXTRACTED: 60 (79%)
- INFERRED: 16 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*