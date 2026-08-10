# Cursor Plans App

> 14 nodes

## Key Concepts

- **test_invite_schemas.py** (15 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **InviteUpdate** (9 connections) — `server/schemas/auth/invite.py`
- **test_invite_update_validation()** (4 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **test_invite_read()** (3 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **test_invite_read_with_used_by()** (3 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **test_invite_update()** (3 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **test_invite_update_all_optional()** (3 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **Schema for updating invite data.** (1 connections) — `server/schemas/auth/invite.py`
- **Unit tests for invite schemas.  Tests the Pydantic models in invite.py module.** (1 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **Test InviteRead can be instantiated.** (1 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **Test InviteRead with used_by_user_id.** (1 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **Test InviteUpdate can be instantiated with optional fields.** (1 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **Test InviteUpdate can be instantiated with all fields optional.** (1 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **Test InviteUpdate validates invite_code length when provided.** (1 connections) — `server/tests/unit/schemas/test_invite_schemas.py`

## Relationships

- [Cursor Plans Github](Cursor_Plans_Github.md) (4 shared connections)
- [E 2 E Scenarios Scenario](E_2_E_Scenarios_Scenario.md) (3 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (3 shared connections)
- [Config Cors](Config_Cors.md) (2 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (1 shared connections)
- [Design Cursor Skills](Design_Cursor_Skills.md) (1 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (1 shared connections)

## Source Files

- `server/schemas/auth/invite.py`
- `server/tests/unit/schemas/test_invite_schemas.py`

## Audit Trail

- EXTRACTED: 46 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*