# Player Domain Model

> 62 nodes

## Key Concepts

- **dependencies.py** (103 connections) — `server/dependencies.py`
- **test_dependencies.py** (60 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **get_container()** (41 connections) — `server/dependencies.py`
- **RuntimeError** (37 connections)
- **Request** (29 connections)
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
- **get_catatonia_registry()** (9 connections) — `server/dependencies.py`
- **get_mythos_time_consumer()** (9 connections) — `server/dependencies.py`
- *... and 37 more nodes in this community*

## Relationships

- [Game Service Bundle](Game_Service_Bundle.md) (18 shared connections)
- [Game Mechanics Service](Game_Mechanics_Service.md) (17 shared connections)
- [NPC Service Tests](NPC_Service_Tests.md) (14 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (11 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (8 shared connections)
- [Cursor Skills Frontend](Cursor_Skills_Frontend.md) (7 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (5 shared connections)
- [Level and XP Curve](Level_and_XP_Curve.md) (4 shared connections)
- [LRU Cache Manager](LRU_Cache_Manager.md) (4 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (3 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (3 shared connections)
- [Inventory Service Helpers](Inventory_Service_Helpers.md) (3 shared connections)

## Source Files

- `server/dependencies.py`
- `server/tests/unit/infrastructure/test_dependencies.py`

## Audit Trail

- EXTRACTED: 458 (85%)
- INFERRED: 80 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*