# get_player_quests

> 36 nodes

## Key Concepts

- **get_player_quests()** (18 connections) — `server/api/players.py`
- **test_players_quests.py** (14 connections) — `server/tests/unit/api/test_players_quests.py`
- **schemas/quest/__init__.py** (10 connections) — `server/schemas/quest/__init__.py`
- **quest/quest.py** (9 connections) — `server/schemas/quest/quest.py`
- **QuestLogEntryResponse** (7 connections) — `server/schemas/quest/quest.py`
- **QuestLogResponse** (7 connections) — `server/schemas/quest/quest.py`
- **BaseModel** (6 connections)
- **test_get_player_quests_403_when_not_owner()** (5 connections) — `server/tests/unit/api/test_players_quests.py`
- **fixture** (5 connections)
- **QuestGoalSchema** (4 connections) — `server/schemas/quest/quest.py`
- **QuestRewardSchema** (4 connections) — `server/schemas/quest/quest.py`
- **QuestTriggerSchema** (4 connections) — `server/schemas/quest/quest.py`
- **test_get_player_quests_include_completed_false()** (4 connections) — `server/tests/unit/api/test_players_quests.py`
- **test_get_player_quests_returns_quest_log()** (4 connections) — `server/tests/unit/api/test_players_quests.py`
- **mock_player_service()** (3 connections) — `server/tests/unit/api/test_players_quests.py`
- **mock_quest_service()** (3 connections) — `server/tests/unit/api/test_players_quests.py`
- **mock_request()** (3 connections) — `server/tests/unit/api/test_players_quests.py`
- **mock_user()** (3 connections) — `server/tests/unit/api/test_players_quests.py`
- **player_id()** (3 connections) — `server/tests/unit/api/test_players_quests.py`
- **asyncio** (3 connections)
- **Get quest log for a character. Requires ownership (403 if not owner).** (1 connections) — `server/api/players.py`
- **Quest subsystem schemas: definition, progress, API responses.** (1 connections) — `server/schemas/quest/__init__.py`
- **Quest subsystem Pydantic schemas for MythosMUD server. Defines schemas for…** (1 connections) — `server/schemas/quest/quest.py`
- **Single goal in a quest definition (complete_activity, kill_n, collect_n, etc.).** (1 connections) — `server/schemas/quest/quest.py`
- **Single reward in a quest definition (xp, item, spell).** (1 connections) — `server/schemas/quest/quest.py`
- *... and 11 more nodes in this community*

## Relationships

- [players.py](players.py.md) (11 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (6 shared connections)
- [QuestService](QuestService.md) (4 shared connections)
- [User](User.md) (3 shared connections)
- [PlayerService](PlayerService.md) (1 shared connections)
- [BaseCommand](BaseCommand.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/api/players.py`
- `server/schemas/quest/__init__.py`
- `server/schemas/quest/quest.py`
- `server/tests/unit/api/test_players_quests.py`

## Audit Trail

- EXTRACTED: 79 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*