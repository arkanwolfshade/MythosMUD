# schemas invite user

> 28 nodes

## Key Concepts

- **test_invite_schemas.py** (15 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **InviteBase** (10 connections) — `server/schemas/auth/invite.py`
- **InviteUpdate** (9 connections) — `server/schemas/auth/invite.py`
- **InviteCreate** (8 connections) — `server/schemas/auth/invite.py`
- **test_invite_base_validation()** (4 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **test_invite_update_validation()** (4 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **test_invite_base()** (3 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **test_invite_base_defaults()** (3 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **test_invite_create()** (3 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **test_invite_create_no_expiry()** (3 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **test_invite_read()** (3 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **test_invite_read_with_used_by()** (3 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **test_invite_update()** (3 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **test_invite_update_all_optional()** (3 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **Base invite schema with common fields.** (1 connections) — `server/schemas/auth/invite.py`
- **Schema for creating a new invite.** (1 connections) — `server/schemas/auth/invite.py`
- **Schema for updating invite data.** (1 connections) — `server/schemas/auth/invite.py`
- **Unit tests for invite schemas.  Tests the Pydantic models in invite.py module.** (1 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **Test InviteBase can be instantiated.** (1 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **Test InviteBase has correct default values.** (1 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **Test InviteBase validates invite_code length.** (1 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **Test InviteCreate can be instantiated.** (1 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **Test InviteCreate can be instantiated without expiry.** (1 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **Test InviteRead can be instantiated.** (1 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **Test InviteRead with used_by_user_id.** (1 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- *... and 3 more nodes in this community*

## Relationships

- [command parser rationale](command_parser_rationale.md) (8 shared connections)
- [auth users rationale](auth_users_rationale.md) (4 shared connections)
- [Player Stats](Player_Stats.md) (2 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)

## Source Files

- `server/schemas/auth/invite.py`
- `server/tests/unit/schemas/test_invite_schemas.py`

## Audit Trail

- EXTRACTED: 86 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*