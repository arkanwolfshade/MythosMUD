# System Monitoring API

> 53 nodes

## Key Concepts

- **test_player_schemas.py** (21 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **player.py** (20 connections) — `server/schemas/players/player.py`
- **ClassDefinition** (15 connections) — `server/schemas/players/class_definition.py`
- **PlayerBase** (11 connections) — `server/schemas/players/player.py`
- **PlayerCreate** (10 connections) — `server/schemas/players/player.py`
- **CharacterInfo** (10 connections) — `server/schemas/players/player.py`
- **PlayerUpdate** (9 connections) — `server/schemas/players/player.py`
- **DeleteCharacterResponse** (9 connections) — `server/schemas/players/player.py`
- **delete_character()** (8 connections) — `server/api/players.py`
- **AvailableClassesResponse** (8 connections) — `server/schemas/players/player.py`
- **get_available_classes()** (7 connections) — `server/api/players.py`
- **_soft_delete_character()** (7 connections) — `server/api/players.py`
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
- *... and 28 more nodes in this community*

## Relationships

- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (19 shared connections)
- [Disconnect Grace Period](Disconnect_Grace_Period.md) (8 shared connections)
- [NPC Database Sessions](NPC_Database_Sessions.md) (6 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (5 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (5 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (4 shared connections)
- [Client Event Store](Client_Event_Store.md) (3 shared connections)
- [Command Parser Helpers](Command_Parser_Helpers.md) (3 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (2 shared connections)
- [Combat NPC Lookup](Combat_NPC_Lookup.md) (2 shared connections)
- [WebSocket Command Handler](WebSocket_Command_Handler.md) (1 shared connections)
- [Game Mechanics Service](Game_Mechanics_Service.md) (1 shared connections)

## Source Files

- `server/api/players.py`
- `server/schemas/players/class_definition.py`
- `server/schemas/players/player.py`
- `server/tests/unit/schemas/test_player_schemas.py`

## Audit Trail

- EXTRACTED: 201 (91%)
- INFERRED: 20 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*