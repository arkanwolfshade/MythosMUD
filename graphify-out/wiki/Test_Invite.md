# Test Invite

> 43 nodes

## Key Concepts

- **Invite** (32 connections) — `server/models/invite.py`
- **test_invite.py** (17 connections) — `server/tests/unit/models/test_invite.py`
- **.create_invite()** (6 connections) — `server/models/invite.py`
- **._generate_invite_code()** (5 connections) — `server/models/invite.py`
- **test_invite_create_invite_defaults()** (4 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_create_invite_with_creator()** (4 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_create_invite_with_custom_expiry()** (4 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_generate_invite_code_format()** (4 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_generate_invite_code_uniqueness()** (4 connections) — `server/tests/unit/models/test_invite.py`
- **.is_expired()** (3 connections) — `server/models/invite.py`
- **.is_valid()** (3 connections) — `server/models/invite.py`
- **test_invite_is_expired_with_aware_datetime()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_is_expired_with_future_expiry()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_is_expired_with_past_expiry()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_is_valid_with_active_and_not_expired()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_is_valid_with_expired()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_is_valid_with_inactive()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_is_valid_with_inactive_and_expired()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_repr()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_use_invite()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **.use_invite()** (2 connections) — `server/models/invite.py`
- **Test is_valid returns False for expired invite.** (2 connections) — `server/tests/unit/models/test_invite.py`
- **.__repr__()** (1 connections) — `server/models/invite.py`
- **Base** (1 connections)
- **Generate a unique invite code.** (1 connections) — `server/models/invite.py`
- *... and 18 more nodes in this community*

## Relationships

- [Player Model & Migrations](Player_Model_&_Migrations.md) (4 shared connections)
- [Database](Database.md) (3 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (2 shared connections)
- [Npc Base](Npc_Base.md) (1 shared connections)

## Source Files

- `server/models/invite.py`
- `server/tests/unit/models/test_invite.py`

## Audit Trail

- EXTRACTED: 67 (91%)
- INFERRED: 7 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*