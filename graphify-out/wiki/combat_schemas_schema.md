# combat schemas schema

> 29 nodes

## Key Concepts

- **test_character_creation.py** (22 connections) — `server/tests/unit/api/test_character_creation.py`
- **CreateCharacterRequest** (17 connections) — `server/schemas/players/player_requests.py`
- **TestCreateCharacterWithStats** (10 connections) — `server/tests/unit/api/test_character_creation.py`
- **TestValidateCharacterStats** (9 connections) — `server/tests/unit/api/test_character_creation.py`
- **.test_create_character_rate_limit()** (6 connections) — `server/tests/unit/api/test_character_creation.py`
- **.test_create_character_shutdown_pending()** (5 connections) — `server/tests/unit/api/test_character_creation.py`
- **.test_create_character_not_authenticated()** (5 connections) — `server/tests/unit/api/test_character_creation.py`
- **.test_create_character_success()** (5 connections) — `server/tests/unit/api/test_character_creation.py`
- **.test_validate_stats_invalid_input()** (4 connections) — `server/tests/unit/api/test_character_creation.py`
- **test_create_character_request_validation()** (4 connections) — `server/tests/unit/schemas/test_player_requests.py`
- **.validate_name()** (2 connections) — `server/schemas/players/player_requests.py`
- **mock_request()** (2 connections) — `server/tests/unit/api/test_character_creation.py`
- **mock_user()** (2 connections) — `server/tests/unit/api/test_character_creation.py`
- **mock_stats_generator()** (2 connections) — `server/tests/unit/api/test_character_creation.py`
- **mock_profession_service()** (2 connections) — `server/tests/unit/api/test_character_creation.py`
- **Request model for character creation.** (1 connections) — `server/schemas/players/player_requests.py`
- **Validate character name format.** (1 connections) — `server/schemas/players/player_requests.py`
- **Unit tests for character creation API endpoints.  Tests roll stats, create chara** (1 connections) — `server/tests/unit/api/test_character_creation.py`
- **Create a mock request object.** (1 connections) — `server/tests/unit/api/test_character_creation.py`
- **Create a mock stats generator.** (1 connections) — `server/tests/unit/api/test_character_creation.py`
- **Create a mock profession service.** (1 connections) — `server/tests/unit/api/test_character_creation.py`
- **Test create_character_with_stats() endpoint.** (1 connections) — `server/tests/unit/api/test_character_creation.py`
- **Test create_character_with_stats() blocks when server is shutting down.** (1 connections) — `server/tests/unit/api/test_character_creation.py`
- **Test create_character_with_stats() requires authentication.** (1 connections) — `server/tests/unit/api/test_character_creation.py`
- **Test create_character_with_stats() enforces rate limiting.** (1 connections) — `server/tests/unit/api/test_character_creation.py`
- *... and 4 more nodes in this community*

## Relationships

- [auth users rationale](auth_users_rationale.md) (11 shared connections)
- [character creation validate](character_creation_validate.md) (9 shared connections)
- [Exception Containers](Exception_Containers.md) (7 shared connections)
- [player requests schemas](player_requests_schemas.md) (6 shared connections)
- [command inventory factories](command_inventory_factories.md) (5 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (4 shared connections)
- [Player Stats](Player_Stats.md) (3 shared connections)
- [game models stats](game_models_stats.md) (2 shared connections)

## Source Files

- `server/schemas/players/player_requests.py`
- `server/tests/unit/api/test_character_creation.py`
- `server/tests/unit/schemas/test_player_requests.py`

## Audit Trail

- EXTRACTED: 98 (88%)
- INFERRED: 13 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*