# Server Models (15)

> 51 nodes

## Key Concepts

- **Invite** (35 connections) — `server/models/invite.py`
- **test_invite.py** (17 connections) — `server/tests/unit/models/test_invite.py`
- **.create_invite()** (6 connections) — `server/models/invite.py`
- **._generate_invite_code()** (6 connections) — `server/models/invite.py`
- **.__init__()** (4 connections) — `server/models/invite.py`
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
- **test_invite_generate_invite_code_format()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_generate_invite_code_uniqueness()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_repr()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **.list_invites()** (2 connections) — `server/auth/invites.py`
- **.use_invite()** (2 connections) — `server/models/invite.py`
- *... and 26 more nodes in this community*

## Relationships

- [Server Admin](Server_Admin.md) (13 shared connections)
- [Server Tools](Server_Tools.md) (2 shared connections)
- [Server Services](Server_Services.md) (1 shared connections)
- [Server Models (14)](Server_Models_%2814%29.md) (1 shared connections)
- [Server Models (17)](Server_Models_%2817%29.md) (1 shared connections)
- [Server Models (6)](Server_Models_%286%29.md) (1 shared connections)

## Source Files

- `server/auth/invites.py`
- `server/models/invite.py`
- `server/tests/unit/models/test_invite.py`

## Audit Trail

- EXTRACTED: 148 (97%)
- INFERRED: 5 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*