# .use invite()

> 62 nodes

## Key Concepts

- **Invite** (35 connections) — `server/models/invite.py`
- **test_invite.py** (17 connections) — `server/tests/unit/models/test_invite.py`
- **.validate_invite()** (6 connections) — `server/auth/invites.py`
- **.create_invite()** (6 connections) — `server/models/invite.py`
- **._generate_invite_code()** (6 connections) — `server/models/invite.py`
- **.use_invite()** (5 connections) — `server/auth/invites.py`
- **.create_invite()** (4 connections) — `server/auth/invites.py`
- **.get_user_invites()** (4 connections) — `server/auth/invites.py`
- **.__init__()** (4 connections) — `server/models/invite.py`
- **UUID** (3 connections)
- **.get_unused_invites()** (3 connections) — `server/auth/invites.py`
- **.cleanup_expired_invites()** (3 connections) — `server/auth/invites.py`
- **.is_expired()** (3 connections) — `server/models/invite.py`
- **.is_valid()** (3 connections) — `server/models/invite.py`
- **test_invite_is_expired_with_future_expiry()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_is_expired_with_past_expiry()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_is_expired_with_aware_datetime()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_is_valid_with_active_and_not_expired()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_is_valid_with_inactive()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_is_valid_with_expired()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_is_valid_with_inactive_and_expired()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_use_invite()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_create_invite_defaults()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_create_invite_with_creator()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_create_invite_with_custom_expiry()** (3 connections) — `server/tests/unit/models/test_invite.py`
- *... and 37 more nodes in this community*

## Relationships

- [Connection Manager](Connection_Manager.md) (8 shared connections)
- [close db()](close_db%28%29.md) (4 shared connections)
- [main()](main%28%29.md) (4 shared connections)
- [.initialize()](initialize%28%29.md) (3 shared connections)
- [AbstractContextManager](AbstractContextManager.md) (1 shared connections)
- [Player](Player.md) (1 shared connections)

## Source Files

- `server/auth/invites.py`
- `server/models/invite.py`
- `server/tests/unit/models/test_invite.py`

## Audit Trail

- EXTRACTED: 176 (97%)
- INFERRED: 5 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*