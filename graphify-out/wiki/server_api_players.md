# server api players

> 213 nodes

## Key Concepts

- **LoggedHTTPException** (358 connections) — `server/exceptions.py`
- **PlayerService** (106 connections) — `server/game/player_service.py`
- **players.py** (73 connections) — `server/api/players.py`
- **test_players_api_coverage.py** (56 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **_user()** (27 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **asyncio** (25 connections)
- **skills.py** (19 connections) — `server/api/skills.py`
- **get_player_quests()** (18 connections) — `server/api/players.py`
- **_start_login_grace_period_body()** (16 connections) — `server/api/players.py`
- **FastAPIRequest** (16 connections)
- **test_skills.py** (16 connections) — `server/tests/unit/api/test_skills.py`
- **select_character()** (15 connections) — `server/api/players.py`
- **UUID** (14 connections)
- **test_players_quests.py** (14 connections) — `server/tests/unit/api/test_players_quests.py`
- **delete_player()** (13 connections) — `server/api/players.py`
- **get_player_skills()** (13 connections) — `server/api/players.py`
- **_validate_character_access()** (13 connections) — `server/api/players.py`
- **UUID** (13 connections)
- **delete_character()** (12 connections) — `server/api/players.py`
- **get_player()** (12 connections) — `server/api/players.py`
- **get_skills_catalog()** (12 connections) — `server/api/skills.py`
- **create_player()** (11 connections) — `server/api/players.py`
- **_disconnect_other_characters()** (11 connections) — `server/api/players.py`
- **list_players()** (11 connections) — `server/api/players.py`
- **_validate_player_for_grace_period()** (11 connections) — `server/api/players.py`
- *... and 188 more nodes in this community*

## Relationships

- [server api character creation](server_api_character_creation.md) (61 shared connections)
- [dependsparam](dependsparam.md) (42 shared connections)
- [docs examples logging fastapi integration](docs_examples_logging_fastapi_integration.md) (33 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (27 shared connections)
- [server api player respawn](server_api_player_respawn.md) (23 shared connections)
- [baseusermanager](baseusermanager.md) (23 shared connections)
- [server api player effects](server_api_player_effects.md) (22 shared connections)
- [server api monitoring](server_api_monitoring.md) (19 shared connections)
- [server api admin npc definitions](server_api_admin_npc_definitions.md) (18 shared connections)
- [server api admin npc instances](server_api_admin_npc_instances.md) (16 shared connections)
- [server api metrics](server_api_metrics.md) (15 shared connections)
- [server api container exception handlers](server_api_container_exception_handlers.md) (14 shared connections)

## Source Files

- `server/api/players.py`
- `server/api/skills.py`
- `server/exceptions.py`
- `server/game/player_service.py`
- `server/schemas/players/class_definition.py`
- `server/schemas/players/player.py`
- `server/schemas/players/skill.py`
- `server/schemas/quest/__init__.py`
- `server/schemas/quest/quest.py`
- `server/tests/unit/api/test_players_api_coverage.py`
- `server/tests/unit/api/test_players_quests.py`
- `server/tests/unit/api/test_skills.py`

## Audit Trail

- EXTRACTED: 848 (84%)
- INFERRED: 163 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*