# E 2 E Scenarios Scenario

> 6 nodes

## Key Concepts

- **InviteCreate** (8 connections) — `server/schemas/auth/invite.py`
- **test_invite_create()** (3 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **test_invite_create_no_expiry()** (3 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **Schema for creating a new invite.** (1 connections) — `server/schemas/auth/invite.py`
- **Test InviteCreate can be instantiated.** (1 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **Test InviteCreate can be instantiated without expiry.** (1 connections) — `server/tests/unit/schemas/test_invite_schemas.py`

## Relationships

- [Cursor Plans App](Cursor_Plans_App.md) (3 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (1 shared connections)
- [Design Cursor Skills](Design_Cursor_Skills.md) (1 shared connections)
- [Config Cors](Config_Cors.md) (1 shared connections)
- [Cursor Plans Github](Cursor_Plans_Github.md) (1 shared connections)

## Source Files

- `server/schemas/auth/invite.py`
- `server/tests/unit/schemas/test_invite_schemas.py`

## Audit Trail

- EXTRACTED: 17 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*