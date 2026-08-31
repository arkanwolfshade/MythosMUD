# PlayerService

> 127 nodes

## Key Concepts

- **PlayerService** (106 connections) — `server/game/player_service.py`
- **players.py** (77 connections) — `server/api/players.py`
- **PlayerRead** (47 connections) — `server/schemas/players/player.py`
- **get_player_quests()** (18 connections) — `server/api/players.py`
- **_start_login_grace_period_body()** (16 connections) — `server/api/players.py`
- **FastAPIRequest** (16 connections)
- **get_player()** (15 connections) — `server/api/players.py`
- **select_character()** (15 connections) — `server/api/players.py`
- **UUID** (14 connections)
- **get_player_skills()** (13 connections) — `server/api/players.py`
- **_validate_character_access()** (13 connections) — `server/api/players.py`
- **UUID** (13 connections)
- **delete_character()** (12 connections) — `server/api/players.py`
- **_disconnect_other_characters()** (11 connections) — `server/api/players.py`
- **get_player_by_name()** (11 connections) — `server/api/players.py`
- **list_players()** (11 connections) — `server/api/players.py`
- **_validate_player_for_grace_period()** (11 connections) — `server/api/players.py`
- **Any** (11 connections)
- **get_user_characters()** (10 connections) — `server/api/players.py`
- **start_login_grace_period_endpoint()** (10 connections) — `server/api/players.py`
- **_validate_character_id()** (10 connections) — `server/api/players.py`
- **schemas/quest/__init__.py** (10 connections) — `server/schemas/quest/__init__.py`
- **_get_connection_manager()** (9 connections) — `server/api/players.py`
- **quest/quest.py** (9 connections) — `server/schemas/quest/quest.py`
- **DeleteCharacterResponse** (8 connections) — `server/schemas/players/player.py`
- *... and 102 more nodes in this community*

## Relationships

- [test_players_api_coverage.py](test_players_api_coverage.py.md) (54 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (44 shared connections)
- [get_logger](get_logger.md) (22 shared connections)
- [players/__init__.py](players-__init__.py.md) (14 shared connections)
- [pytest.md](pytest.md.md) (13 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (12 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (8 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (7 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (6 shared connections)
- [magic_service.py](magic_service.py.md) (5 shared connections)
- [test_players_quests.py](test_players_quests.py.md) (5 shared connections)
- [QuestService](QuestService.md) (5 shared connections)

## Source Files

- `server/api/players.py`
- `server/game/player_search_service.py`
- `server/game/player_service.py`
- `server/schemas/players/player.py`
- `server/schemas/players/skill.py`
- `server/schemas/quest/__init__.py`
- `server/schemas/quest/quest.py`

## Audit Trail

- EXTRACTED: 477 (95%)
- INFERRED: 24 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*