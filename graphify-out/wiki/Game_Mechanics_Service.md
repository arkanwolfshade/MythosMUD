# Game Mechanics Service

> 144 nodes

## Key Concepts

- **character_creation.py** (54 connections) — `server/api/character_creation.py`
- **SkillService** (37 connections) — `server/game/skill_service.py`
- **RollStatsRequest** (22 connections) — `server/schemas/players/player_requests.py`
- **test_character_creation.py** (22 connections) — `server/tests/unit/api/test_character_creation.py`
- **roll_character_stats()** (21 connections) — `server/api/character_creation.py`
- **CreateCharacterRequest** (21 connections) — `server/schemas/players/player_requests.py`
- **ProfessionService** (19 connections) — `server/game/profession_service.py`
- **create_character_with_stats()** (17 connections) — `server/api/character_creation.py`
- **_execute_create_character()** (15 connections) — `server/api/character_creation.py`
- **_roll_stats_with_profession_preview()** (14 connections) — `server/api/character_creation.py`
- **validate_character_stats()** (13 connections) — `server/api/character_creation.py`
- **TestRollCharacterStats** (13 connections) — `server/tests/unit/api/test_character_creation.py`
- **Any** (10 connections)
- **_dispatch_roll_stats()** (10 connections) — `server/api/character_creation.py`
- **Any** (10 connections)
- **character_creation.py** (10 connections) — `server/schemas/players/character_creation.py`
- **RollStatsResponse** (10 connections) — `server/schemas/players/character_creation.py`
- **CreateCharacterResponse** (10 connections) — `server/schemas/players/character_creation.py`
- **RolledStats** (10 connections) — `server/schemas/players/stat_values.py`
- **TestCreateCharacterWithStats** (10 connections) — `server/tests/unit/api/test_character_creation.py`
- **_convert_stat_summary_to_stat_summary_model()** (9 connections) — `server/api/character_creation.py`
- **.set_player_skills()** (9 connections) — `server/game/skill_service.py`
- **ValidateStatsResponse** (9 connections) — `server/schemas/players/character_creation.py`
- **_check_shutdown_status()** (8 connections) — `server/api/character_creation.py`
- **_roll_stats_raw()** (8 connections) — `server/api/character_creation.py`
- *... and 119 more nodes in this community*

## Relationships

- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (22 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (21 shared connections)
- [Disconnect Grace Period](Disconnect_Grace_Period.md) (18 shared connections)
- [Client Event Store](Client_Event_Store.md) (11 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (10 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (9 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (7 shared connections)
- [Command Parser Helpers](Command_Parser_Helpers.md) (7 shared connections)
- [WebSocket Command Handler](WebSocket_Command_Handler.md) (7 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (6 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (6 shared connections)
- [NPC Database Sessions](NPC_Database_Sessions.md) (5 shared connections)

## Source Files

- `server/api/character_creation.py`
- `server/game/profession_service.py`
- `server/game/skill_service.py`
- `server/schemas/players/character_creation.py`
- `server/schemas/players/player_requests.py`
- `server/schemas/players/stat_values.py`
- `server/tests/unit/api/test_character_creation.py`

## Audit Trail

- EXTRACTED: 671 (95%)
- INFERRED: 37 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*