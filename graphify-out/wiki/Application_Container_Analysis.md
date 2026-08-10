# Application Container Analysis

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

- [NATS Subject Patterns](NATS_Subject_Patterns.md) (5 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (4 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (4 shared connections)
- [Exploration Command Factories](Exploration_Command_Factories.md) (4 shared connections)
- [Chat Service Whispers](Chat_Service_Whispers.md) (1 shared connections)
- [Look Player Command](Look_Player_Command.md) (1 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (1 shared connections)
- [Game Client Container](Game_Client_Container.md) (1 shared connections)
- [Archive Planning E 2 E](Archive_Planning_E_2_E.md) (1 shared connections)
- [Command Alias Handling](Command_Alias_Handling.md) (1 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (1 shared connections)

## Source Files

- `server/services/wearable_container_service.py`
- `server/tests/unit/services/test_wearable_container_service.py`

## Audit Trail

- EXTRACTED: 38 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*