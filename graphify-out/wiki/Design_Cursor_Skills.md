# Design Cursor Skills

> 6 nodes

## Key Concepts

- **__init__.py** (12 connections) — `server/schemas/auth/__init__.py`
- **UserRead** (7 connections) — `server/schemas/auth/user.py`
- **test_user_read()** (3 connections) — `server/tests/unit/schemas/test_user_schemas.py`
- **Auth domain schemas: user and invite.** (1 connections) — `server/schemas/auth/__init__.py`
- **Schema for reading user data.** (1 connections) — `server/schemas/auth/user.py`
- **Test UserRead can be instantiated.** (1 connections) — `server/tests/unit/schemas/test_user_schemas.py`

## Relationships

- [Config Cors](Config_Cors.md) (4 shared connections)
- [Combat Flee Command](Combat_Flee_Command.md) (4 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (2 shared connections)
- [E 2 E Scenarios Scenario](E_2_E_Scenarios_Scenario.md) (2 shared connections)
- [Cursor Plans Github](Cursor_Plans_Github.md) (1 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (1 shared connections)
- [Cursor Plans App](Cursor_Plans_App.md) (1 shared connections)

## Source Files

- `server/schemas/auth/__init__.py`
- `server/schemas/auth/user.py`
- `server/tests/unit/schemas/test_user_schemas.py`

## Audit Trail

- EXTRACTED: 25 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*