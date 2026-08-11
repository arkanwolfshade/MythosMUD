# E 2 E Scenarios Scenario

> 49 nodes

## Key Concepts

- **Invite** (35 connections) — `server/models/invite.py`
- **test_invite.py** (17 connections) — `server/tests/unit/models/test_invite.py`
- **.create_invite()** (6 connections) — `server/models/invite.py`
- **._generate_invite_code()** (6 connections) — `server/models/invite.py`
- **.create_invite()** (4 connections) — `server/auth/invites.py`
- **.__init__()** (4 connections) — `server/models/invite.py`
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
- **datetime** (2 connections)
- **.use_invite()** (2 connections) — `server/models/invite.py`
- **Base** (1 connections)
- *... and 24 more nodes in this community*

## Relationships

- [Who Command Helpers](Who_Command_Helpers.md) (7 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (4 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (4 shared connections)
- [Realtime Conftest Mocks](Realtime_Conftest_Mocks.md) (2 shared connections)
- [Spell Registry Costs](Spell_Registry_Costs.md) (1 shared connections)
- [NPC Movement Integration](NPC_Movement_Integration.md) (1 shared connections)

## Source Files

- `server/auth/invites.py`
- `server/models/invite.py`
- `server/tests/unit/models/test_invite.py`

## Audit Trail

- EXTRACTED: 145 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*