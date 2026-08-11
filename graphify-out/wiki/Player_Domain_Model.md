# Player Domain Model

> 207 nodes

## Key Concepts

- **dependencies.py** (103 connections) — `server/dependencies.py`
- **test_dependencies.py** (60 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **get_container()** (41 connections) — `server/dependencies.py`
- **RuntimeError** (37 connections)
- **Request** (29 connections)
- **test_dependency_injection.py** (18 connections) — `server/tests/unit/test_dependency_injection.py`
- **stats_generator.py** (14 connections) — `server/game/stats_generator.py`
- **get_player_service()** (12 connections) — `server/dependencies.py`
- **get_room_service()** (12 connections) — `server/dependencies.py`
- **get_player_death_service()** (10 connections) — `server/dependencies.py`
- **get_combat_service()** (10 connections) — `server/dependencies.py`
- **get_magic_service()** (10 connections) — `server/dependencies.py`
- **get_spell_learning_service()** (10 connections) — `server/dependencies.py`
- **get_chat_service()** (10 connections) — `server/dependencies.py`
- **get_connection_manager()** (9 connections) — `server/dependencies.py`
- **get_async_persistence()** (9 connections) — `server/dependencies.py`
- **get_player_respawn_service()** (9 connections) — `server/dependencies.py`
- **get_player_combat_service()** (9 connections) — `server/dependencies.py`
- **get_spell_registry()** (9 connections) — `server/dependencies.py`
- **get_spell_targeting_service()** (9 connections) — `server/dependencies.py`
- **get_spell_effects()** (9 connections) — `server/dependencies.py`
- **get_mp_regeneration_service()** (9 connections) — `server/dependencies.py`
- **get_npc_lifecycle_manager()** (9 connections) — `server/dependencies.py`
- **get_npc_spawning_service()** (9 connections) — `server/dependencies.py`
- **get_npc_population_controller()** (9 connections) — `server/dependencies.py`
- *... and 182 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (49 shared connections)
- [WebSocket Command Handler](WebSocket_Command_Handler.md) (14 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (12 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (10 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (10 shared connections)
- [Game Mechanics Service](Game_Mechanics_Service.md) (6 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (5 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (5 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (4 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (4 shared connections)
- [Inventory Service Helpers](Inventory_Service_Helpers.md) (4 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (4 shared connections)

## Source Files

- `server/dependencies.py`
- `server/game/stats_generator.py`
- `server/tests/unit/infrastructure/test_dependencies.py`
- `server/tests/unit/test_dependency_injection.py`

## Audit Trail

- EXTRACTED: 804 (88%)
- INFERRED: 106 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*