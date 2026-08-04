# combat models rationale

> 6 nodes

## Key Concepts

- **InviteCreate** (8 connections) — `server/schemas/auth/invite.py`
- **test_invite_create()** (3 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **test_invite_create_no_expiry()** (3 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **Schema for creating a new invite.** (1 connections) — `server/schemas/auth/invite.py`
- **Test InviteCreate can be instantiated.** (1 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **Test InviteCreate can be instantiated without expiry.** (1 connections) — `server/tests/unit/schemas/test_invite_schemas.py`

## Relationships

- [spawn npc services](spawn_npc_services.md) (3 shared connections)
- [inventory schemas schema](inventory_schemas_schema.md) (1 shared connections)
- [level curve game](level_curve_game.md) (1 shared connections)
- [message filtering helpers](message_filtering_helpers.md) (1 shared connections)
- [professions endpoints all](professions_endpoints_all.md) (1 shared connections)

## Source Files

- `server/schemas/auth/invite.py`
- `server/tests/unit/schemas/test_invite_schemas.py`

## Audit Trail

- EXTRACTED: 17 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*