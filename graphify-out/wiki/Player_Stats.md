# Player Stats

> 66 nodes

## Key Concepts

- **test_players_api_coverage.py** (28 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **FastAPIRequest** (16 connections)
- **start_login_grace_period_endpoint()** (16 connections) — `server/api/players.py`
- **get_player_quests()** (14 connections) — `server/api/players.py`
- **UUID** (13 connections)
- **_validate_character_access()** (13 connections) — `server/api/players.py`
- **test_players_quests.py** (13 connections) — `server/tests/unit/api/test_players_quests.py`
- **_disconnect_other_characters()** (12 connections) — `server/api/players.py`
- **select_character()** (12 connections) — `server/api/players.py`
- **_user()** (12 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **_validate_player_for_grace_period()** (11 connections) — `server/api/players.py`
- **create_player()** (10 connections) — `server/api/players.py`
- **list_players()** (10 connections) — `server/api/players.py`
- **_validate_character_id()** (10 connections) — `server/api/players.py`
- **get_player_skills()** (9 connections) — `server/api/players.py`
- **_get_connection_manager()** (9 connections) — `server/api/players.py`
- **delete_player()** (8 connections) — `server/api/players.py`
- **get_class_description()** (5 connections) — `server/api/players.py`
- **Any** (5 connections)
- **_end_combat_for_grace_period()** (5 connections) — `server/api/players.py`
- **test_create_player_validation_error_to_400()** (5 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **MessageResponse** (4 connections)
- **test_validate_character_id_rejects_bad_format()** (4 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **test_validate_character_access_not_found()** (4 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **test_validate_character_access_wrong_owner()** (4 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- *... and 41 more nodes in this community*

## Relationships

- [command inventory factories](command_inventory_factories.md) (29 shared connections)
- [Exception Containers](Exception_Containers.md) (19 shared connections)
- [ascii map renderer](ascii_map_renderer.md) (13 shared connections)
- [command inventory models](command_inventory_models.md) (11 shared connections)
- [command utility models](command_utility_models.md) (3 shared connections)
- [character creation service](character_creation_service.md) (2 shared connections)
- [room sync service](room_sync_service.md) (2 shared connections)
- [Database Config](Database_Config.md) (2 shared connections)
- [tick game processing](tick_game_processing.md) (2 shared connections)
- [endpoints auth rationale](endpoints_auth_rationale.md) (1 shared connections)
- [quest game service](quest_game_service.md) (1 shared connections)
- [game models stats](game_models_stats.md) (1 shared connections)

## Source Files

- `server/api/players.py`
- `server/tests/unit/api/test_players_api_coverage.py`
- `server/tests/unit/api/test_players_quests.py`

## Audit Trail

- EXTRACTED: 309 (95%)
- INFERRED: 16 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*