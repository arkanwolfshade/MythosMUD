# PlayerService

> 196 nodes

## Key Concepts

- **PlayerService** (106 connections) — `server/game/player_service.py`
- **players.py** (77 connections) — `server/api/players.py`
- **test_players_api_coverage.py** (60 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **_user()** (31 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **asyncio** (29 connections)
- **get_player_quests()** (18 connections) — `server/api/players.py`
- **_start_login_grace_period_body()** (16 connections) — `server/api/players.py`
- **._init_player_quest_layer()** (16 connections) — `server/container/bundles/game.py`
- **FastAPIRequest** (16 connections)
- **delete_player()** (15 connections) — `server/api/players.py`
- **get_player()** (15 connections) — `server/api/players.py`
- **select_character()** (15 connections) — `server/api/players.py`
- **UUID** (14 connections)
- **create_player()** (13 connections) — `server/api/players.py`
- **get_player_skills()** (13 connections) — `server/api/players.py`
- **_validate_character_access()** (13 connections) — `server/api/players.py`
- **UUID** (13 connections)
- **delete_character()** (12 connections) — `server/api/players.py`
- **_disconnect_other_characters()** (11 connections) — `server/api/players.py`
- **get_player_by_name()** (11 connections) — `server/api/players.py`
- **list_players()** (11 connections) — `server/api/players.py`
- **_validate_player_for_grace_period()** (11 connections) — `server/api/players.py`
- **server/api/__init__.py** (11 connections) — `server/api/__init__.py`
- **Any** (11 connections)
- **get_available_classes()** (10 connections) — `server/api/players.py`
- *... and 171 more nodes in this community*

## Relationships

- [api/character_creation.py](api-character_creation.py.md) (41 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (38 shared connections)
- [pytest.md](pytest.md.md) (38 shared connections)
- [get_logger](get_logger.md) (18 shared connections)
- [api/player_effects.py](api-player_effects.py.md) (14 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (13 shared connections)
- [log_and_raise_enhanced](log_and_raise_enhanced.md) (8 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (7 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (7 shared connections)
- [QuestService](QuestService.md) (6 shared connections)
- [BaseCommand](BaseCommand.md) (5 shared connections)
- [DatabaseError](DatabaseError.md) (5 shared connections)

## Source Files

- `server/api/__init__.py`
- `server/api/player_router.py`
- `server/api/players.py`
- `server/app/game_tick_processing.py`
- `server/container/bundles/game.py`
- `server/game/player_service.py`
- `server/schemas/players/class_definition.py`
- `server/schemas/players/player.py`
- `server/schemas/players/skill.py`
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