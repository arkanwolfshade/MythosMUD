# Combat Flee Command

> 16 nodes

## Key Concepts

- **test_user_schemas.py** (13 connections) — `server/tests/unit/schemas/test_user_schemas.py`
- **UserUpdate** (9 connections) — `server/schemas/auth/user.py`
- **UserCreate** (8 connections) — `server/schemas/auth/user.py`
- **test_user_create_password_validation()** (4 connections) — `server/tests/unit/schemas/test_user_schemas.py`
- **test_user_update_password_validation()** (4 connections) — `server/tests/unit/schemas/test_user_schemas.py`
- **test_user_create()** (3 connections) — `server/tests/unit/schemas/test_user_schemas.py`
- **test_user_update()** (3 connections) — `server/tests/unit/schemas/test_user_schemas.py`
- **test_user_update_all_optional()** (3 connections) — `server/tests/unit/schemas/test_user_schemas.py`
- **Schema for creating a new user.** (1 connections) — `server/schemas/auth/user.py`
- **Schema for updating user data.** (1 connections) — `server/schemas/auth/user.py`
- **Unit tests for user schemas.  Tests the Pydantic models in user.py module.** (1 connections) — `server/tests/unit/schemas/test_user_schemas.py`
- **Test UserCreate can be instantiated.** (1 connections) — `server/tests/unit/schemas/test_user_schemas.py`
- **Test UserCreate validates password length.** (1 connections) — `server/tests/unit/schemas/test_user_schemas.py`
- **Test UserUpdate can be instantiated with optional fields.** (1 connections) — `server/tests/unit/schemas/test_user_schemas.py`
- **Test UserUpdate can be instantiated with all fields optional.** (1 connections) — `server/tests/unit/schemas/test_user_schemas.py`
- **Test UserUpdate validates password length when provided.** (1 connections) — `server/tests/unit/schemas/test_user_schemas.py`

## Relationships

- [Design Cursor Skills](Design_Cursor_Skills.md) (4 shared connections)
- [E 2 E Scenarios Scenario](E_2_E_Scenarios_Scenario.md) (4 shared connections)
- [Config Cors](Config_Cors.md) (3 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (2 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (2 shared connections)

## Source Files

- `server/schemas/auth/user.py`
- `server/tests/unit/schemas/test_user_schemas.py`

## Audit Trail

- EXTRACTED: 53 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*