# PlayerService

> 275 nodes

## Key Concepts

- **PlayerService** (106 connections) — `server/game/player_service.py`
- **players.py** (73 connections) — `server/api/players.py`
- **server/schemas/__init__.py** (70 connections) — `server/schemas/__init__.py`
- **test_players_api_coverage.py** (56 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **players/__init__.py** (48 connections) — `server/schemas/players/__init__.py`
- **PlayerRead** (46 connections) — `server/schemas/players/player.py`
- **_user()** (27 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **asyncio** (25 connections)
- **test_player_schemas.py** (23 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **players/player.py** (21 connections) — `server/schemas/players/player.py`
- **get_player_quests()** (18 connections) — `server/api/players.py`
- **_start_login_grace_period_body()** (16 connections) — `server/api/players.py`
- **FastAPIRequest** (16 connections)
- **select_character()** (15 connections) — `server/api/players.py`
- **UUID** (14 connections)
- **test_players_quests.py** (14 connections) — `server/tests/unit/api/test_players_quests.py`
- **delete_player()** (13 connections) — `server/api/players.py`
- **get_player_skills()** (13 connections) — `server/api/players.py`
- **_validate_character_access()** (13 connections) — `server/api/players.py`
- **UUID** (13 connections)
- **delete_character()** (12 connections) — `server/api/players.py`
- **get_player()** (12 connections) — `server/api/players.py`
- **create_player()** (11 connections) — `server/api/players.py`
- **_disconnect_other_characters()** (11 connections) — `server/api/players.py`
- **list_players()** (11 connections) — `server/api/players.py`
- *... and 250 more nodes in this community*

## Relationships

- [LoggedHTTPException](LoggedHTTPException.md) (81 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (25 shared connections)
- [api/player_effects.py](api-player_effects.py.md) (24 shared connections)
- [ValidationError](ValidationError.md) (16 shared connections)
- [api/player_respawn.py](api-player_respawn.py.md) (13 shared connections)
- [pytest.md](pytest.md.md) (13 shared connections)
- [server/models/game.py](server-models-game.py.md) (12 shared connections)
- [TargetMatch](TargetMatch.md) (11 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (10 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (9 shared connections)
- [Stats](Stats.md) (8 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (7 shared connections)

## Source Files

- `server/api/players.py`
- `server/game/magic/spell_costs.py`
- `server/game/magic/spell_materials.py`
- `server/game/player_search_service.py`
- `server/game/player_service.py`
- `server/schemas/__init__.py`
- `server/schemas/players/__init__.py`
- `server/schemas/players/character_creation.py`
- `server/schemas/players/class_definition.py`
- `server/schemas/players/player.py`
- `server/schemas/players/player_requests.py`
- `server/schemas/players/profession.py`
- `server/schemas/players/skill.py`
- `server/schemas/quest/__init__.py`
- `server/schemas/quest/quest.py`
- `server/tests/unit/api/test_players_api_coverage.py`
- `server/tests/unit/api/test_players_quests.py`
- `server/tests/unit/schemas/test_player_schemas.py`

## Audit Trail

- EXTRACTED: 863 (95%)
- INFERRED: 43 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*