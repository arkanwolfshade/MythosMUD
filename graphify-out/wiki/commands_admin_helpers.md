# commands admin helpers

> 138 nodes

## Key Concepts

- **character_creation.py** (47 connections) — `server/api/character_creation.py`
- **roll_character_stats()** (23 connections) — `server/api/character_creation.py`
- **test_character_creation.py** (22 connections) — `server/tests/unit/api/test_character_creation.py`
- **RollStatsRequest** (20 connections) — `server/schemas/players/player_requests.py`
- **professions.py** (19 connections) — `server/api/professions.py`
- **ProfessionService** (19 connections) — `server/game/profession_service.py`
- **create_character_with_stats()** (18 connections) — `server/api/character_creation.py`
- **CreateCharacterRequest** (17 connections) — `server/schemas/players/player_requests.py`
- **test_profession_service.py** (15 connections) — `server/tests/unit/game/test_profession_service.py`
- **_roll_stats_with_profession_preview()** (14 connections) — `server/api/character_creation.py`
- **_execute_create_character()** (13 connections) — `server/api/character_creation.py`
- **validate_character_stats()** (13 connections) — `server/api/character_creation.py`
- **get_shutdown_blocking_message()** (13 connections) — `server/commands/admin_shutdown_command.py`
- **profession_service.py** (13 connections) — `server/game/profession_service.py`
- **TestRollCharacterStats** (13 connections) — `server/tests/unit/api/test_character_creation.py`
- **test_professions_endpoints.py** (13 connections) — `server/tests/unit/api/test_professions_endpoints.py`
- **get_all_professions()** (10 connections) — `server/api/professions.py`
- **get_profession_by_id()** (10 connections) — `server/api/professions.py`
- **TestCreateCharacterWithStats** (10 connections) — `server/tests/unit/api/test_character_creation.py`
- **_convert_stat_summary_to_stat_summary_model()** (9 connections) — `server/api/character_creation.py`
- **TestValidateCharacterStats** (9 connections) — `server/tests/unit/api/test_character_creation.py`
- **_check_shutdown_status()** (8 connections) — `server/api/character_creation.py`
- **_roll_stats_raw()** (8 connections) — `server/api/character_creation.py`
- **_roll_stats_with_class()** (8 connections) — `server/api/character_creation.py`
- **_stats_to_rolled_stats()** (7 connections) — `server/api/character_creation.py`
- *... and 113 more nodes in this community*

## Relationships

- [services inventory mutation](services_inventory_mutation.md) (28 shared connections)
- [player service game](player_service_game.md) (22 shared connections)
- [player requests schemas](player_requests_schemas.md) (21 shared connections)
- [add used user](add_used_user.md) (12 shared connections)
- [System Metrics](System_Metrics.md) (12 shared connections)
- [profession game service](profession_game_service.md) (11 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (8 shared connections)
- [shutdown admin command](shutdown_admin_command.md) (7 shared connections)
- [Exception Containers](Exception_Containers.md) (7 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (6 shared connections)
- [Error Conversion](Error_Conversion.md) (6 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (5 shared connections)

## Source Files

- `server/api/character_creation.py`
- `server/api/professions.py`
- `server/commands/admin_shutdown_command.py`
- `server/game/profession_service.py`
- `server/schemas/players/player_requests.py`
- `server/schemas/players/profession.py`
- `server/tests/unit/api/test_character_creation.py`
- `server/tests/unit/api/test_professions_endpoints.py`
- `server/tests/unit/game/test_profession_service.py`
- `server/tests/unit/schemas/test_player_requests.py`

## Audit Trail

- EXTRACTED: 611 (96%)
- INFERRED: 26 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*