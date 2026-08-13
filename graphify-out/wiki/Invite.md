# Invite

> 47 nodes

## Key Concepts

- **Invite** (34 connections) — `server/models/invite.py`
- **test_invite.py** (17 connections) — `server/tests/unit/models/test_invite.py`
- **.create_invite()** (6 connections) — `server/models/invite.py`
- **._generate_invite_code()** (6 connections) — `server/models/invite.py`
- **.get_unused_invites()** (3 connections) — `server/auth/invites.py`
- **.is_expired()** (3 connections) — `server/models/invite.py`
- **.is_valid()** (3 connections) — `server/models/invite.py`
- **test_invite_create_invite_defaults()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_create_invite_with_creator()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_create_invite_with_custom_expiry()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_generate_invite_code_format()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_generate_invite_code_uniqueness()** (3 connections) — `server/tests/unit/models/test_invite.py`
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
- *... and 22 more nodes in this community*

## Relationships

- [User](User.md) (9 shared connections)
- [log_and_raise](log_and_raise.md) (4 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (2 shared connections)
- [.get_instance](get_instance.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [.is_alive](is_alive.md) (1 shared connections)

## Source Files

- `server/auth/invites.py`
- `server/models/invite.py`
- `server/tests/unit/models/test_invite.py`

## Audit Trail

- EXTRACTED: 78 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*