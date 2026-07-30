# append unique valid occupant()

> 127 nodes

## Key Concepts

- **players.py** (66 connections) — `server/api/players.py`
- **test_players_api_coverage.py** (28 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **FastAPIRequest** (16 connections)
- **start_login_grace_period_endpoint()** (16 connections) — `server/api/players.py`
- **get_player_quests()** (14 connections) — `server/api/players.py`
- **test_skills.py** (14 connections) — `server/tests/unit/api/test_skills.py`
- **UUID** (13 connections)
- **_validate_character_access()** (13 connections) — `server/api/players.py`
- **test_players_quests.py** (13 connections) — `server/tests/unit/api/test_players_quests.py`
- **_disconnect_other_characters()** (12 connections) — `server/api/players.py`
- **select_character()** (12 connections) — `server/api/players.py`
- **_user()** (12 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **_validate_player_for_grace_period()** (11 connections) — `server/api/players.py`
- **create_player()** (10 connections) — `server/api/players.py`
- **list_players()** (10 connections) — `server/api/players.py`
- **_validate_character_id()** (10 connections) — `server/api/players.py`
- **get_player_skills()** (9 connections) — `server/api/players.py`
- **_get_connection_manager()** (9 connections) — `server/api/players.py`
- **__init__.py** (9 connections) — `server/schemas/quest/__init__.py`
- **get_user_characters()** (8 connections) — `server/api/players.py`
- **get_player()** (8 connections) — `server/api/players.py`
- **delete_player()** (8 connections) — `server/api/players.py`
- **delete_character()** (8 connections) — `server/api/players.py`
- **get_tick_interval()** (8 connections) — `server/app/game_tick_processing.py`
- **AvailableClassesResponse** (8 connections) — `server/schemas/players/player.py`
- *... and 102 more nodes in this community*

## Relationships

- [AbstractContextManager](AbstractContextManager.md) (26 shared connections)
- [Connection Manager](Connection_Manager.md) (22 shared connections)
- [Player](Player.md) (21 shared connections)
- [real time](real_time.md) (15 shared connections)
- [message handler factory](message_handler_factory.md) (14 shared connections)
- [close db()](close_db%28%29.md) (9 shared connections)
- [login grace period](login_grace_period.md) (7 shared connections)
- [admin shutdown command](admin_shutdown_command.md) (5 shared connections)
- [QuestCompleted](QuestCompleted.md) (5 shared connections)
- [Room](Room.md) (3 shared connections)
- [Protocol](Protocol.md) (3 shared connections)
- [. init ()](_init_%28%29.md) (3 shared connections)

## Source Files

- `server/api/players.py`
- `server/app/game_tick_processing.py`
- `server/schemas/players/player.py`
- `server/schemas/players/skill.py`
- `server/schemas/quest/__init__.py`
- `server/schemas/quest/quest.py`
- `server/tests/unit/api/test_players_api_coverage.py`
- `server/tests/unit/api/test_players_quests.py`
- `server/tests/unit/api/test_skills.py`

## Audit Trail

- EXTRACTED: 590 (96%)
- INFERRED: 24 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*