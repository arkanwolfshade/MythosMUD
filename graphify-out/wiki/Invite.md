# Invite

> 35 nodes

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
- **.__repr__()** (1 connections) — `server/models/invite.py`
- **Base** (1 connections)
- **Model for user registration invites.** (1 connections) — `server/models/invite.py`
- **Mark this invite as used by a specific user.** (1 connections) — `server/models/invite.py`
- **Create a new invite with the specified parameters.** (1 connections) — `server/models/invite.py`
- **Unit tests for the Invite model. Tests the Invite model methods including…** (1 connections) — `server/tests/unit/models/test_invite.py`
- **Test create_invite creates invite with creator user_id.** (1 connections) — `server/tests/unit/models/test_invite.py`
- **Test create_invite creates invite with custom expiry days.** (1 connections) — `server/tests/unit/models/test_invite.py`
- *... and 10 more nodes in this community*

## Relationships

- [InviteManager](InviteManager.md) (11 shared connections)
- [._generate_invite_code](_generate_invite_code.md) (7 shared connections)
- [sqlalchemy.md](sqlalchemy.md.md) (4 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (2 shared connections)
- [.use_invite](use_invite.md) (2 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)
- [.is_expired](is_expired.md) (2 shared connections)
- [.get_unused_invites](get_unused_invites.md) (1 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (1 shared connections)
- [ValidationError](ValidationError.md) (1 shared connections)
- [.validate_invite](validate_invite.md) (1 shared connections)
- [.__init__](__init__.md) (1 shared connections)

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