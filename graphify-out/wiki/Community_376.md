# Community 376

> 46 nodes

## Key Concepts

- **test_players_api_coverage.py** (39 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **_user()** (32 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **asyncio** (30 connections)
- **.get_player()** (10 connections) — `server/realtime/integration/game_state_provider.py`
- **.create_player()** (7 connections) — `server/game/player_service.py`
- **test_create_player_rejects_non_superuser()** (5 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **test_get_player_rejects_non_owner_non_admin()** (5 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **test_create_player_success()** (4 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **test_create_player_validation_error_to_400()** (4 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **test_delete_character_already_deleted_is_404_not_500()** (4 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **test_delete_player_rejects_non_superuser()** (4 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **test_get_player_allows_owner()** (4 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **test_get_player_by_name_success()** (4 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **test_get_player_not_found()** (4 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **test_get_player_success()** (4 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **test_get_user_characters_success()** (4 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **test_delete_character_invalid_id()** (3 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **test_delete_character_success()** (3 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **test_delete_player_not_found()** (3 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **test_delete_player_success()** (3 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **test_delete_player_validation_error()** (3 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **test_disconnect_other_characters_disconnects_peer()** (3 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **test_disconnect_other_characters_no_manager()** (3 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **test_get_available_classes()** (3 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **test_get_player_quests_forbidden()** (3 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- *... and 21 more nodes in this community*

## Relationships

- [DI Containers & API Bootstrap](DI_Containers_&_API_Bootstrap.md) (5 shared connections)
- [Community 467](Community_467.md) (3 shared connections)
- [Player Creation Service](Player_Creation_Service.md) (1 shared connections)
- [Community 246](Community_246.md) (1 shared connections)
- [Community 840](Community_840.md) (1 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (1 shared connections)
- [Player Effects (Corruption/Fear/Lucidity)](Player_Effects_Corruption-Fear-Lucidity.md) (1 shared connections)

## Source Files

- `server/game/player_service.py`
- `server/realtime/integration/game_state_provider.py`
- `server/tests/unit/api/test_players_api_coverage.py`

## Audit Trail

- EXTRACTED: 113 (92%)
- INFERRED: 10 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*