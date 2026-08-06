# Player Stats

> 140 nodes

## Key Concepts

- **players.py** (66 connections) — `server/api/players.py`
- **test_players_api_coverage.py** (54 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **_user()** (27 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **skills.py** (18 connections) — `server/api/skills.py`
- **get_player_quests()** (17 connections) — `server/api/players.py`
- **FastAPIRequest** (16 connections)
- **start_login_grace_period_endpoint()** (16 connections) — `server/api/players.py`
- **select_character()** (14 connections) — `server/api/players.py`
- **test_skills.py** (14 connections) — `server/tests/unit/api/test_skills.py`
- **UUID** (13 connections)
- **_validate_character_access()** (13 connections) — `server/api/players.py`
- **test_players_quests.py** (13 connections) — `server/tests/unit/api/test_players_quests.py`
- **get_player_skills()** (12 connections) — `server/api/players.py`
- **delete_player()** (12 connections) — `server/api/players.py`
- **_disconnect_other_characters()** (12 connections) — `server/api/players.py`
- **get_player()** (11 connections) — `server/api/players.py`
- **delete_character()** (11 connections) — `server/api/players.py`
- **_validate_player_for_grace_period()** (11 connections) — `server/api/players.py`
- **get_skills_catalog()** (11 connections) — `server/api/skills.py`
- **create_player()** (10 connections) — `server/api/players.py`
- **list_players()** (10 connections) — `server/api/players.py`
- **get_user_characters()** (10 connections) — `server/api/players.py`
- **_validate_character_id()** (10 connections) — `server/api/players.py`
- **SelectCharacterRequest** (10 connections) — `server/schemas/players/player_requests.py`
- **get_available_classes()** (9 connections) — `server/api/players.py`
- *... and 115 more nodes in this community*

## Relationships

- [services inventory mutation](services_inventory_mutation.md) (35 shared connections)
- [player requests schemas](player_requests_schemas.md) (23 shared connections)
- [player service game](player_service_game.md) (17 shared connections)
- [persistence core infrastructure](persistence_core_infrastructure.md) (14 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (12 shared connections)
- [command utility models](command_utility_models.md) (7 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (6 shared connections)
- [profession game service](profession_game_service.md) (6 shared connections)
- [add used user](add_used_user.md) (5 shared connections)
- [quest game service](quest_game_service.md) (5 shared connections)
- [handler realtime nats](handler_realtime_nats.md) (4 shared connections)
- [Error Conversion](Error_Conversion.md) (4 shared connections)

## Source Files

- `server/api/players.py`
- `server/api/skills.py`
- `server/schemas/players/player_requests.py`
- `server/schemas/players/skill.py`
- `server/schemas/quest/__init__.py`
- `server/schemas/quest/quest.py`
- `server/tests/unit/api/test_players_api_coverage.py`
- `server/tests/unit/api/test_players_quests.py`
- `server/tests/unit/api/test_skills.py`

## Audit Trail

- EXTRACTED: 705 (97%)
- INFERRED: 25 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*