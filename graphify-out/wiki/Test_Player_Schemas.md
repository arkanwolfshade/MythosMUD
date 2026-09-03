# Test Player Schemas

> 67 nodes

## Key Concepts

- **PlayerRead** (39 connections) — `server/schemas/players/player.py`
- **test_player_schemas.py** (23 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **players/player.py** (21 connections) — `server/schemas/players/player.py`
- **PlayerBase** (10 connections) — `server/schemas/players/player.py`
- **PlayerCreate** (9 connections) — `server/schemas/players/player.py`
- **PlayerUpdate** (8 connections) — `server/schemas/players/player.py`
- **CharacterInfo** (7 connections) — `server/schemas/players/player.py`
- **BaseModel** (7 connections)
- **AvailableClassesResponse** (6 connections) — `server/schemas/players/player.py`
- **ClassDefinition** (5 connections) — `server/schemas/players/class_definition.py`
- **DeleteCharacterResponse** (5 connections) — `server/schemas/players/player.py`
- **LoginGracePeriodResponse** (5 connections) — `server/schemas/players/player.py`
- **MessageResponse** (5 connections) — `server/schemas/players/player.py`
- **test_player_create_custom_stats()** (4 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **test_player_read()** (4 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **test_player_read_defaults()** (4 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **class_definition.py** (4 connections) — `server/schemas/players/class_definition.py`
- **.get_online_players()** (3 connections) — `server/game/player_search_service.py`
- **.search_players_by_name()** (3 connections) — `server/game/player_search_service.py`
- **.get_online_players()** (3 connections) — `server/game/player_service.py`
- **.get_player_by_name()** (3 connections) — `server/game/player_service.py`
- **.list_players()** (3 connections) — `server/game/player_service.py`
- **.resolve_player_name()** (3 connections) — `server/game/player_service.py`
- **.search_players_by_name()** (3 connections) — `server/game/player_service.py`
- **.resolve_player_name()** (3 connections) — `server/services/target_resolution_service.py`
- *... and 42 more nodes in this community*

## Relationships

- [Character Creation API](Character_Creation_API.md) (17 shared connections)
- [Dependency Injection (FastAPI)](Dependency_Injection_FastAPI.md) (15 shared connections)
- [Npc Admin](Npc_Admin.md) (7 shared connections)
- [Stats Generator](Stats_Generator.md) (5 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (4 shared connections)
- [Player Creation Service](Player_Creation_Service.md) (3 shared connections)
- [Test Target Resolution Service](Test_Target_Resolution_Service.md) (3 shared connections)
- [Command Aliases](Command_Aliases.md) (3 shared connections)
- [Player Model & Migrations](Player_Model_&_Migrations.md) (2 shared connections)
- [Game](Game.md) (2 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (1 shared connections)
- [Test Game Player](Test_Game_Player.md) (1 shared connections)

## Source Files

- `server/game/player_search_service.py`
- `server/game/player_service.py`
- `server/schemas/players/class_definition.py`
- `server/schemas/players/player.py`
- `server/services/target_resolution_service.py`
- `server/tests/unit/schemas/test_player_schemas.py`

## Audit Trail

- EXTRACTED: 156 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*