# .create_invite

> 8 nodes

## Key Concepts

- **.create_invite()** (6 connections) — `server/models/invite.py`
- **test_invite_create_invite_defaults()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_create_invite_with_creator()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_create_invite_with_custom_expiry()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **Create a new invite with the specified parameters.** (1 connections) — `server/models/invite.py`
- **Test create_invite creates invite with creator user_id.** (1 connections) — `server/tests/unit/models/test_invite.py`
- **Test create_invite creates invite with custom expiry days.** (1 connections) — `server/tests/unit/models/test_invite.py`
- **Test create_invite creates invite with default parameters.** (1 connections) — `server/tests/unit/models/test_invite.py`

## Relationships

- [test_invite.py](test_invite.py.md) (3 shared connections)
- [._generate_invite_code](_generate_invite_code.md) (1 shared connections)
- [Invite](Invite.md) (1 shared connections)

## Source Files

- `server/models/invite.py`
- `server/tests/unit/models/test_invite.py`

## Audit Trail

- EXTRACTED: 19 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*