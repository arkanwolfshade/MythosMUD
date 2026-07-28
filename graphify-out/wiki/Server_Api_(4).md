# Server Api (4)

> 166 nodes

## Key Concepts

- **character_creation.py** (47 connections) — `server/api/character_creation.py`
- **StatsGenerator** (35 connections) — `server/game/stats_generator.py`
- **roll_character_stats()** (23 connections) — `server/api/character_creation.py`
- **test_character_creation.py** (22 connections) — `server/tests/unit/api/test_character_creation.py`
- **RollStatsRequest** (20 connections) — `server/schemas/players/player_requests.py`
- **create_character_with_stats()** (18 connections) — `server/api/character_creation.py`
- **ProfessionService** (17 connections) — `server/game/profession_service.py`
- **CreateCharacterRequest** (17 connections) — `server/schemas/players/player_requests.py`
- **_roll_stats_with_profession_preview()** (14 connections) — `server/api/character_creation.py`
- **is_shutdown_pending()** (14 connections) — `server/commands/admin_shutdown_command.py`
- **stats_generator.py** (14 connections) — `server/game/stats_generator.py`
- **_execute_create_character()** (13 connections) — `server/api/character_creation.py`
- **validate_character_stats()** (13 connections) — `server/api/character_creation.py`
- **get_shutdown_blocking_message()** (13 connections) — `server/commands/admin_shutdown_command.py`
- **character_creation_service.py** (13 connections) — `server/game/character_creation_service.py`
- **TestRollCharacterStats** (13 connections) — `server/tests/unit/api/test_character_creation.py`
- **CharacterCreationService** (12 connections) — `server/game/character_creation_service.py`
- **profession_service.py** (12 connections) — `server/game/profession_service.py`
- **Stats** (11 connections)
- **character_creation.py** (10 connections) — `server/schemas/players/character_creation.py`
- **CreateCharacterResponse** (10 connections) — `server/schemas/players/character_creation.py`
- **RolledStats** (10 connections) — `server/schemas/players/stat_values.py`
- **TestCreateCharacterWithStats** (10 connections) — `server/tests/unit/api/test_character_creation.py`
- **_convert_stat_summary_to_stat_summary_model()** (9 connections) — `server/api/character_creation.py`
- **RollStatsResponse** (9 connections) — `server/schemas/players/character_creation.py`
- *... and 141 more nodes in this community*

## Relationships

- [Server Admin](Server_Admin.md) (28 shared connections)
- [Server Api](Server_Api.md) (26 shared connections)
- [Server Schemas](Server_Schemas.md) (22 shared connections)
- [Server Api (3)](Server_Api_%283%29.md) (16 shared connections)
- [Server Infrastructure](Server_Infrastructure.md) (16 shared connections)
- [Server Utils](Server_Utils.md) (12 shared connections)
- [Server Models (12)](Server_Models_%2812%29.md) (10 shared connections)
- [Server Api (2)](Server_Api_%282%29.md) (9 shared connections)
- [Server Commands](Server_Commands.md) (9 shared connections)
- [Server Commands (21)](Server_Commands_%2821%29.md) (8 shared connections)
- [Server Game (9)](Server_Game_%289%29.md) (4 shared connections)
- [Server Realtime (21)](Server_Realtime_%2821%29.md) (4 shared connections)

## Source Files

- `server/api/character_creation.py`
- `server/commands/admin_shutdown_command.py`
- `server/game/character_creation_service.py`
- `server/game/profession_service.py`
- `server/game/stats_generator.py`
- `server/schemas/players/character_creation.py`
- `server/schemas/players/player_requests.py`
- `server/schemas/players/stat_values.py`
- `server/tests/unit/api/test_character_creation.py`
- `server/tests/unit/test_dependency_injection.py`

## Audit Trail

- EXTRACTED: 731 (94%)
- INFERRED: 50 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*