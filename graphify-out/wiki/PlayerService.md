# PlayerService

> 230 nodes

## Key Concepts

- **PlayerService** (137 connections) — `server/game/player_service.py`
- **players.py** (69 connections) — `server/api/players.py`
- **PlayerRead** (48 connections) — `server/schemas/players/player.py`
- **test_players_api_coverage.py** (28 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **test_player_schemas.py** (21 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **players/player.py** (20 connections) — `server/schemas/players/player.py`
- **_start_login_grace_period_body()** (16 connections) — `server/api/players.py`
- **FastAPIRequest** (16 connections)
- **ClassDefinition** (15 connections) — `server/schemas/players/class_definition.py`
- **get_player_quests()** (15 connections) — `server/api/players.py`
- **UUID** (14 connections)
- **select_character()** (13 connections) — `server/api/players.py`
- **_validate_character_access()** (13 connections) — `server/api/players.py`
- **UUID** (13 connections)
- **test_players_quests.py** (13 connections) — `server/tests/unit/api/test_players_quests.py`
- **_user()** (12 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **PlayerBase** (11 connections) — `server/schemas/players/player.py`
- **create_player()** (11 connections) — `server/api/players.py`
- **_disconnect_other_characters()** (11 connections) — `server/api/players.py`
- **list_players()** (11 connections) — `server/api/players.py`
- **_validate_player_for_grace_period()** (11 connections) — `server/api/players.py`
- **Any** (11 connections)
- **CharacterInfo** (10 connections) — `server/schemas/players/player.py`
- **PlayerCreate** (10 connections) — `server/schemas/players/player.py`
- **get_player_skills()** (10 connections) — `server/api/players.py`
- *... and 205 more nodes in this community*

## Relationships

- [server/dependencies.py](server-dependencies.py.md) (36 shared connections)
- [User](User.md) (24 shared connections)
- [players/__init__.py](players-__init__.py.md) (20 shared connections)
- [Player](Player.md) (20 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (20 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (15 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (14 shared connections)
- [magic_service.py](magic_service.py.md) (8 shared connections)
- [server/models/game.py](server-models-game.py.md) (7 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (7 shared connections)
- [StatsGenerator](StatsGenerator.md) (6 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (5 shared connections)

## Source Files

- `server/api/players.py`
- `server/game/magic/mp_regeneration_service.py`
- `server/game/magic/spell_costs.py`
- `server/game/magic/spell_materials.py`
- `server/game/player_search_service.py`
- `server/game/player_service.py`
- `server/schemas/players/class_definition.py`
- `server/schemas/players/player.py`
- `server/schemas/players/skill.py`
- `server/schemas/quest/__init__.py`
- `server/schemas/quest/quest.py`
- `server/services/target_resolution_service.py`
- `server/tests/unit/api/test_players_api_coverage.py`
- `server/tests/unit/api/test_players_quests.py`
- `server/tests/unit/schemas/test_player_schemas.py`

## Audit Trail

- EXTRACTED: 634 (90%)
- INFERRED: 67 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*