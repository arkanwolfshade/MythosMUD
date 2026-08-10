# E 2 E Scenarios Scenario

> 6 nodes

## Key Concepts

- **UserBase** (8 connections) — `server/schemas/auth/user.py`
- **test_user_base()** (3 connections) — `server/tests/unit/schemas/test_user_schemas.py`
- **test_user_base_defaults()** (3 connections) — `server/tests/unit/schemas/test_user_schemas.py`
- **Base user schema with common fields.** (1 connections) — `server/schemas/auth/user.py`
- **Test UserBase can be instantiated.** (1 connections) — `server/tests/unit/schemas/test_user_schemas.py`
- **Test UserBase has correct default values.** (1 connections) — `server/tests/unit/schemas/test_user_schemas.py`

## Relationships

- [Combat Flee Command](Combat_Flee_Command.md) (4 shared connections)
- [Config Cors](Config_Cors.md) (2 shared connections)
- [Design Cursor Skills](Design_Cursor_Skills.md) (1 shared connections)

## Source Files

- `server/schemas/auth/user.py`
- `server/tests/unit/schemas/test_user_schemas.py`

## Audit Trail

- EXTRACTED: 17 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*