# Player Domain Model

> 235 nodes

## Key Concepts

- **dependencies.py** (103 connections) — `server/dependencies.py`
- **test_dependencies.py** (60 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **get_container()** (41 connections) — `server/dependencies.py`
- **RuntimeError** (37 connections)
- **Request** (29 connections)
- **test_dependency_injection.py** (18 connections) — `server/tests/unit/test_dependency_injection.py`
- **get_player_service()** (12 connections) — `server/dependencies.py`
- **get_room_service()** (12 connections) — `server/dependencies.py`
- **get_player_death_service()** (10 connections) — `server/dependencies.py`
- **get_combat_service()** (10 connections) — `server/dependencies.py`
- **get_magic_service()** (10 connections) — `server/dependencies.py`
- **get_spell_learning_service()** (10 connections) — `server/dependencies.py`
- **get_chat_service()** (10 connections) — `server/dependencies.py`
- **get_player_service_for_testing()** (9 connections) — `server/dependencies.py`
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
- *... and 210 more nodes in this community*

## Relationships

- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (34 shared connections)
- [Client Event Store](Client_Event_Store.md) (21 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (21 shared connections)
- [WebSocket Command Handler](WebSocket_Command_Handler.md) (16 shared connections)
- [Container Persistence Ops](Container_Persistence_Ops.md) (9 shared connections)
- [Chat Channel Logger](Chat_Channel_Logger.md) (8 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (4 shared connections)
- [Rest Command Flow](Rest_Command_Flow.md) (4 shared connections)
- [Game Mechanics Service](Game_Mechanics_Service.md) (3 shared connections)
- [Client Security Utilities](Client_Security_Utilities.md) (3 shared connections)
- [Catatonia Registry Service](Catatonia_Registry_Service.md) (3 shared connections)
- [Enhanced Logging Exceptions](Enhanced_Logging_Exceptions.md) (3 shared connections)

## Source Files

- `server/dependencies.py`
- `server/tests/unit/infrastructure/test_dependencies.py`
- `server/tests/unit/test_dependency_injection.py`

## Audit Trail

- EXTRACTED: 860 (89%)
- INFERRED: 111 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*