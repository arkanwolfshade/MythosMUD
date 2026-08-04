# professions endpoints all

> 8 nodes

## Key Concepts

- **InviteBase** (10 connections) — `server/schemas/auth/invite.py`
- **test_invite_base_validation()** (4 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **test_invite_base()** (3 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **test_invite_base_defaults()** (3 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **Base invite schema with common fields.** (1 connections) — `server/schemas/auth/invite.py`
- **Test InviteBase can be instantiated.** (1 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **Test InviteBase has correct default values.** (1 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **Test InviteBase validates invite_code length.** (1 connections) — `server/tests/unit/schemas/test_invite_schemas.py`

## Relationships

- [spawn npc services](spawn_npc_services.md) (4 shared connections)
- [message filtering helpers](message_filtering_helpers.md) (2 shared connections)
- [level curve game](level_curve_game.md) (1 shared connections)
- [combat models rationale](combat_models_rationale.md) (1 shared connections)
- [player requests schemas](player_requests_schemas.md) (1 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (1 shared connections)

## Source Files

- `server/schemas/auth/invite.py`
- `server/tests/unit/schemas/test_invite_schemas.py`

## Audit Trail

- EXTRACTED: 23 (96%)
- INFERRED: 1 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*