# Player Stats

> 217 nodes

## Key Concepts

- **__init__.py** (70 connections) — `server/schemas/__init__.py`
- **players.py** (66 connections) — `server/api/players.py`
- **PlayerRead** (48 connections) — `server/schemas/players/player.py`
- **__init__.py** (38 connections) — `server/schemas/players/__init__.py`
- **test_players_api_coverage.py** (28 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **test_player_schemas.py** (21 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **player.py** (20 connections) — `server/schemas/players/player.py`
- **professions.py** (19 connections) — `server/api/professions.py`
- **skills.py** (18 connections) — `server/api/skills.py`
- **FastAPIRequest** (16 connections)
- **start_login_grace_period_endpoint()** (16 connections) — `server/api/players.py`
- **ClassDefinition** (15 connections) — `server/schemas/players/class_definition.py`
- **get_player_quests()** (14 connections) — `server/api/players.py`
- **test_skills.py** (14 connections) — `server/tests/unit/api/test_skills.py`
- **UUID** (13 connections)
- **_validate_character_access()** (13 connections) — `server/api/players.py`
- **test_players_quests.py** (13 connections) — `server/tests/unit/api/test_players_quests.py`
- **test_professions_endpoints.py** (13 connections) — `server/tests/unit/api/test_professions_endpoints.py`
- **_disconnect_other_characters()** (12 connections) — `server/api/players.py`
- **select_character()** (12 connections) — `server/api/players.py`
- **_user()** (12 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **_validate_player_for_grace_period()** (11 connections) — `server/api/players.py`
- **get_skills_catalog()** (11 connections) — `server/api/skills.py`
- **PlayerBase** (11 connections) — `server/schemas/players/player.py`
- **create_player()** (10 connections) — `server/api/players.py`
- *... and 192 more nodes in this community*

## Relationships

- [Exception Containers](Exception_Containers.md) (39 shared connections)
- [auth users rationale](auth_users_rationale.md) (38 shared connections)
- [magic healing game](magic_healing_game.md) (27 shared connections)
- [command inventory factories](command_inventory_factories.md) (21 shared connections)
- [character creation validate](character_creation_validate.md) (19 shared connections)
- [admin auth service](admin_auth_service.md) (11 shared connections)
- [NATS Messaging](NATS_Messaging.md) (10 shared connections)
- [respawn player handlers](respawn_player_handlers.md) (9 shared connections)
- [grace period login](grace_period_login.md) (7 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (6 shared connections)
- [metrics schemas rationale](metrics_schemas_rationale.md) (6 shared connections)
- [game models stats](game_models_stats.md) (6 shared connections)

## Source Files

- `server/api/players.py`
- `server/api/professions.py`
- `server/api/skills.py`
- `server/game/player_service.py`
- `server/schemas/__init__.py`
- `server/schemas/players/__init__.py`
- `server/schemas/players/class_definition.py`
- `server/schemas/players/player.py`
- `server/schemas/players/profession.py`
- `server/schemas/players/skill.py`
- `server/schemas/quest/__init__.py`
- `server/schemas/quest/quest.py`
- `server/tests/unit/api/test_players_api_coverage.py`
- `server/tests/unit/api/test_players_quests.py`
- `server/tests/unit/api/test_professions_endpoints.py`
- `server/tests/unit/api/test_skills.py`
- `server/tests/unit/schemas/test_player_schemas.py`

## Audit Trail

- EXTRACTED: 1071 (96%)
- INFERRED: 48 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*