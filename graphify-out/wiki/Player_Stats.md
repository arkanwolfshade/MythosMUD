# Player Stats

> 198 nodes

## Key Concepts

- **__init__.py** (70 connections) — `server/schemas/__init__.py`
- **players.py** (66 connections) — `server/api/players.py`
- **test_players_api_coverage.py** (54 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **PlayerRead** (48 connections) — `server/schemas/players/player.py`
- **__init__.py** (38 connections) — `server/schemas/players/__init__.py`
- **_user()** (27 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **test_player_schemas.py** (21 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **player.py** (20 connections) — `server/schemas/players/player.py`
- **get_player_quests()** (17 connections) — `server/api/players.py`
- **FastAPIRequest** (16 connections)
- **start_login_grace_period_endpoint()** (16 connections) — `server/api/players.py`
- **ClassDefinition** (15 connections) — `server/schemas/players/class_definition.py`
- **player_requests.py** (15 connections) — `server/schemas/players/player_requests.py`
- **select_character()** (14 connections) — `server/api/players.py`
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
- **PlayerBase** (11 connections) — `server/schemas/players/player.py`
- *... and 173 more nodes in this community*

## Relationships

- [profession game service](profession_game_service.md) (43 shared connections)
- [Exception Containers](Exception_Containers.md) (32 shared connections)
- [NPC Combat](NPC_Combat.md) (30 shared connections)
- [player requests schemas](player_requests_schemas.md) (25 shared connections)
- [Loot Generation](Loot_Generation.md) (12 shared connections)
- [logging setup structured](logging_setup_structured.md) (11 shared connections)
- [endpoints auth rationale](endpoints_auth_rationale.md) (8 shared connections)
- [game models stats](game_models_stats.md) (8 shared connections)
- [command factories communication](command_factories_communication.md) (8 shared connections)
- [security sessionManager SessionManager](security_sessionManager_SessionManager.md) (8 shared connections)
- [command utility models](command_utility_models.md) (7 shared connections)
- [player service game](player_service_game.md) (7 shared connections)

## Source Files

- `server/api/players.py`
- `server/api/skills.py`
- `server/game/player_search_service.py`
- `server/game/player_service.py`
- `server/schemas/__init__.py`
- `server/schemas/players/__init__.py`
- `server/schemas/players/class_definition.py`
- `server/schemas/players/player.py`
- `server/schemas/players/player_requests.py`
- `server/schemas/players/skill.py`
- `server/schemas/quest/__init__.py`
- `server/schemas/quest/quest.py`
- `server/services/target_resolution_service.py`
- `server/tests/unit/api/test_players_api_coverage.py`
- `server/tests/unit/api/test_players_quests.py`
- `server/tests/unit/api/test_skills.py`
- `server/tests/unit/schemas/test_player_schemas.py`

## Audit Trail

- EXTRACTED: 1035 (95%)
- INFERRED: 51 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*