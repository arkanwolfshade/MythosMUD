# ._generate_invite_code

> 8 nodes

## Key Concepts

- **._generate_invite_code()** (6 connections) — `server/models/invite.py`
- **.create_invite()** (4 connections) — `server/auth/invites.py`
- **test_invite_generate_invite_code_format()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_generate_invite_code_uniqueness()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **datetime** (2 connections)
- **Generate a unique invite code.** (1 connections) — `server/models/invite.py`
- **Test _generate_invite_code generates 12-character alphanumeric code.** (1 connections) — `server/tests/unit/models/test_invite.py`
- **Test _generate_invite_code generates different codes on multiple calls.** (1 connections) — `server/tests/unit/models/test_invite.py`

## Relationships

- [Invite](Invite.md) (2 shared connections)
- [User](User.md) (2 shared connections)
- [test_invite.py](test_invite.py.md) (2 shared connections)
- [.create_invite](create_invite.md) (1 shared connections)

## Source Files

- `server/auth/invites.py`
- `server/models/invite.py`
- `server/tests/unit/models/test_invite.py`

## Audit Trail

- EXTRACTED: 21 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*