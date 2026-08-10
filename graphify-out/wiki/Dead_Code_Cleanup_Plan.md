# Dead Code Cleanup Plan

> 346 nodes

## Key Concepts

- **PlayerService** (141 connections) — `server/game/player_service.py`
- **log_and_raise_enhanced()** (97 connections) — `server/utils/enhanced_error_logging.py`
- **__init__.py** (70 connections) — `server/schemas/__init__.py`
- **players.py** (69 connections) — `server/api/players.py`
- **PlayerRead** (48 connections) — `server/schemas/players/player.py`
- **player_service.py** (44 connections) — `server/game/player_service.py`
- **__init__.py** (38 connections) — `server/schemas/players/__init__.py`
- **test_players_api_coverage.py** (28 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **player_respawn.py** (25 connections) — `server/api/player_respawn.py`
- **test_player_schemas.py** (21 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **player.py** (20 connections) — `server/schemas/players/player.py`
- **player_schema_converter.py** (19 connections) — `server/game/player_schema_converter.py`
- **FastAPIRequest** (17 connections)
- **_start_login_grace_period_body()** (16 connections) — `server/api/players.py`
- **PlayerSchemaConverter** (16 connections) — `server/game/player_schema_converter.py`
- **UUID** (15 connections)
- **ClassDefinition** (15 connections) — `server/schemas/players/class_definition.py`
- **get_player_quests()** (14 connections) — `server/api/players.py`
- **player_creation_service.py** (14 connections) — `server/game/player_creation_service.py`
- **UUID** (14 connections)
- **_validate_character_access()** (13 connections) — `server/api/players.py`
- **_disconnect_other_characters()** (13 connections) — `server/api/players.py`
- **mp_regeneration_service.py** (13 connections) — `server/game/magic/mp_regeneration_service.py`
- **test_players_quests.py** (13 connections) — `server/tests/unit/api/test_players_quests.py`
- **select_character()** (12 connections) — `server/api/players.py`
- *... and 321 more nodes in this community*

## Relationships

- [Room Service Tests](Room_Service_Tests.md) (71 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (68 shared connections)
- [Game Mechanics Service](Game_Mechanics_Service.md) (50 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (36 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (32 shared connections)
- [test_profession_meets_stat_requirements_multiple_not_met](test_profession_meets_stat_requirements_multiple_not_met.md) (26 shared connections)
- [NPC Service Tests](NPC_Service_Tests.md) (21 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (17 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (13 shared connections)
- [Moderation Command Models](Moderation_Command_Models.md) (9 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (8 shared connections)
- [Cursor Plans Disconnect](Cursor_Plans_Disconnect.md) (8 shared connections)

## Source Files

- `server/api/player_respawn.py`
- `server/api/players.py`
- `server/api/skills.py`
- `server/game/magic/mp_regeneration_service.py`
- `server/game/player_creation_service.py`
- `server/game/player_schema_converter.py`
- `server/game/player_search_service.py`
- `server/game/player_service.py`
- `server/game/player_state_service.py`
- `server/schemas/__init__.py`
- `server/schemas/players/__init__.py`
- `server/schemas/players/class_definition.py`
- `server/schemas/players/player.py`
- `server/schemas/players/player_respawn.py`
- `server/schemas/players/profession.py`
- `server/schemas/players/skill.py`
- `server/schemas/quest/__init__.py`
- `server/schemas/quest/quest.py`
- `server/schemas/rooms/__init__.py`
- `server/schemas/rooms/room.py`

## Audit Trail

- EXTRACTED: 1735 (93%)
- INFERRED: 132 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*