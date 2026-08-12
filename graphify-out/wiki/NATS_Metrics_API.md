# NATS Metrics API

> 48 nodes

## Key Concepts

- **test_player_schemas.py** (21 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **player.py** (20 connections) — `server/schemas/players/player.py`
- **ClassDefinition** (15 connections) — `server/schemas/players/class_definition.py`
- **PlayerBase** (11 connections) — `server/schemas/players/player.py`
- **PlayerCreate** (10 connections) — `server/schemas/players/player.py`
- **CharacterInfo** (10 connections) — `server/schemas/players/player.py`
- **PlayerUpdate** (9 connections) — `server/schemas/players/player.py`
- **AvailableClassesResponse** (8 connections) — `server/schemas/players/player.py`
- **get_available_classes()** (7 connections) — `server/api/players.py`
- **BaseModel** (7 connections)
- **MessageResponse** (7 connections) — `server/schemas/players/player.py`
- **test_player_base_validation()** (4 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **test_player_create()** (4 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **test_player_create_custom_stats()** (4 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **test_player_read()** (4 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **test_player_read_defaults()** (4 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **test_player_base_rejects_extra_fields()** (4 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **test_player_create_rejects_extra_fields()** (4 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **class_definition.py** (3 connections) — `server/schemas/players/class_definition.py`
- **test_player_base()** (3 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **test_character_info()** (3 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **test_character_info_defaults()** (3 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **test_player_update()** (3 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **test_player_update_all_optional()** (3 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **Get information about all available character classes and their prerequisites.** (1 connections) — `server/api/players.py`
- *... and 23 more nodes in this community*

## Relationships

- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (17 shared connections)
- [Disconnect Grace Period](Disconnect_Grace_Period.md) (7 shared connections)
- [NPC Database Sessions](NPC_Database_Sessions.md) (6 shared connections)
- [Game Terminal Panels](Game_Terminal_Panels.md) (4 shared connections)
- [Combat NPC Lookup](Combat_NPC_Lookup.md) (3 shared connections)
- [React Node Upgrade Summary](React_Node_Upgrade_Summary.md) (3 shared connections)
- [Zone Config Loader](Zone_Config_Loader.md) (2 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (2 shared connections)
- [WebSocket Command Handler](WebSocket_Command_Handler.md) (1 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (1 shared connections)
- [Test Refactoring Complete](Test_Refactoring_Complete.md) (1 shared connections)
- [Game Mechanics Service](Game_Mechanics_Service.md) (1 shared connections)

## Source Files

- `server/api/players.py`
- `server/schemas/players/class_definition.py`
- `server/schemas/players/player.py`
- `server/tests/unit/schemas/test_player_schemas.py`

## Audit Trail

- EXTRACTED: 176 (90%)
- INFERRED: 19 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*