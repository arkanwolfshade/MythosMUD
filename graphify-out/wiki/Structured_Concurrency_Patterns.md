# Structured Concurrency Patterns

> 8 nodes

## Key Concepts

- **wearable_container_service.py** (20 connections) — `server/services/wearable_container_service.py`
- **_get_enum_value()** (8 connections) — `server/services/wearable_container_service.py`
- **test_get_enum_value_with_enum()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_get_enum_value_with_string()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **Wearable container service for unified container system.  As documented in the r** (1 connections) — `server/services/wearable_container_service.py`
- **Safely get enum value, handling both enum instances and string values.      When** (1 connections) — `server/services/wearable_container_service.py`
- **Test _get_enum_value returns value from enum instance.** (1 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **Test _get_enum_value returns string value unchanged.** (1 connections) — `server/tests/unit/services/test_wearable_container_service.py`

## Relationships

- [Schedule Service Loader](Schedule_Service_Loader.md) (5 shared connections)
- [Exploration Command Factories](Exploration_Command_Factories.md) (4 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (3 shared connections)
- [Combat Player Broadcasts](Combat_Player_Broadcasts.md) (3 shared connections)
- [Container Component Capacity](Container_Component_Capacity.md) (2 shared connections)
- [Client Event Store](Client_Event_Store.md) (2 shared connections)
- [Character Creation Service](Character_Creation_Service.md) (1 shared connections)
- [Look Player Command](Look_Player_Command.md) (1 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (1 shared connections)
- [E 2 E Testing Guide](E_2_E_Testing_Guide.md) (1 shared connections)
- [Pre-commit Hook Analysis](Pre-commit_Hook_Analysis.md) (1 shared connections)

## Source Files

- `server/services/wearable_container_service.py`
- `server/tests/unit/services/test_wearable_container_service.py`

## Audit Trail

- EXTRACTED: 38 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*