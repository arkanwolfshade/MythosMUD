# PlayerService

> 212 nodes

## Key Concepts

- **PlayerService** (106 connections) — `server/game/player_service.py`
- **players.py** (73 connections) — `server/api/players.py`
- **test_players_api_coverage.py** (56 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **PlayerRead** (46 connections) — `server/schemas/players/player.py`
- **_user()** (27 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **asyncio** (25 connections)
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
- **_validate_player_for_grace_period()** (11 connections) — `server/api/players.py`
- **Any** (11 connections)
- **PlayerSearchService** (10 connections) — `server/game/player_search_service.py`
- **SelectCharacterRequest** (10 connections) — `server/schemas/players/player_requests.py`
- *... and 187 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (40 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (34 shared connections)
- [User](User.md) (22 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (20 shared connections)
- [api/player_effects.py](api-player_effects.py.md) (13 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (12 shared connections)
- [AliasStorage](AliasStorage.md) (9 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (8 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (7 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (6 shared connections)
- [QuestService](QuestService.md) (6 shared connections)
- [PlayerSchemaConverter](PlayerSchemaConverter.md) (5 shared connections)

## Source Files

- `server/api/players.py`
- `server/app/game_tick_processing.py`
- `server/game/magic/spell_costs.py`
- `server/game/magic/spell_materials.py`
- `server/game/player_creation_service.py`
- `server/game/player_search_service.py`
- `server/game/player_service.py`
- `server/schemas/players/player.py`
- `server/schemas/players/player_requests.py`
- `server/schemas/quest/__init__.py`
- `server/schemas/quest/quest.py`
- `server/tests/unit/api/test_players_api_coverage.py`
- `server/tests/unit/api/test_players_quests.py`

## Audit Trail

- EXTRACTED: 650 (94%)
- INFERRED: 42 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*