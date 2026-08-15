# PlayerService

> 162 nodes

## Key Concepts

- **PlayerService** (106 connections) — `server/game/player_service.py`
- **players.py** (73 connections) — `server/api/players.py`
- **test_players_api_coverage.py** (54 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **_user()** (27 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **asyncio** (25 connections)
- **get_player_quests()** (18 connections) — `server/api/players.py`
- **_start_login_grace_period_body()** (16 connections) — `server/api/players.py`
- **get_current_tick()** (16 connections) — `server/app/game_tick_processing.py`
- **FastAPIRequest** (16 connections)
- **select_character()** (15 connections) — `server/api/players.py`
- **UUID** (14 connections)
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
- **get_available_classes()** (10 connections) — `server/api/players.py`
- **get_player_by_name()** (10 connections) — `server/api/players.py`
- **get_user_characters()** (10 connections) — `server/api/players.py`
- *... and 137 more nodes in this community*

## Relationships

- [server/schemas/__init__.py](server-schemas-__init__.py.md) (39 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (30 shared connections)
- [User](User.md) (20 shared connections)
- [api/player_effects.py](api-player_effects.py.md) (14 shared connections)
- [magic_service.py](magic_service.py.md) (10 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (9 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (8 shared connections)
- [Stats](Stats.md) (7 shared connections)
- [ValidationError](ValidationError.md) (7 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [QuestService](QuestService.md) (6 shared connections)
- [PlayerStateService](PlayerStateService.md) (5 shared connections)

## Source Files

- `server/api/players.py`
- `server/app/game_tick_processing.py`
- `server/game/player_service.py`
- `server/schemas/players/skill.py`
- `server/schemas/quest/__init__.py`
- `server/schemas/quest/quest.py`
- `server/tests/unit/api/test_players_api_coverage.py`

## Audit Trail

- EXTRACTED: 554 (93%)
- INFERRED: 40 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*