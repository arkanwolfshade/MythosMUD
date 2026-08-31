# test_players_quests.py

> 19 nodes

## Key Concepts

- **test_players_quests.py** (14 connections) — `server/tests/unit/api/test_players_quests.py`
- **test_get_player_quests_403_when_not_owner()** (5 connections) — `server/tests/unit/api/test_players_quests.py`
- **fixture** (5 connections)
- **test_get_player_quests_include_completed_false()** (4 connections) — `server/tests/unit/api/test_players_quests.py`
- **test_get_player_quests_returns_quest_log()** (4 connections) — `server/tests/unit/api/test_players_quests.py`
- **mock_player_service()** (3 connections) — `server/tests/unit/api/test_players_quests.py`
- **mock_quest_service()** (3 connections) — `server/tests/unit/api/test_players_quests.py`
- **mock_request()** (3 connections) — `server/tests/unit/api/test_players_quests.py`
- **mock_user()** (3 connections) — `server/tests/unit/api/test_players_quests.py`
- **player_id()** (3 connections) — `server/tests/unit/api/test_players_quests.py`
- **asyncio** (3 connections)
- **Unit tests for GET /api/players/{player_id}/quests (quest log). Tests…** (1 connections) — `server/tests/unit/api/test_players_quests.py`
- **GET quests with include_completed=False passes to get_quest_log.** (1 connections) — `server/tests/unit/api/test_players_quests.py`
- **GET quests raises 403 when validate_character_access returns not ok.** (1 connections) — `server/tests/unit/api/test_players_quests.py`
- **Minimal request for endpoint (not used for quest logic).** (1 connections) — `server/tests/unit/api/test_players_quests.py`
- **Character (player) UUID.** (1 connections) — `server/tests/unit/api/test_players_quests.py`
- **PlayerService that validates character access.** (1 connections) — `server/tests/unit/api/test_players_quests.py`
- **QuestService that returns quest log entries.** (1 connections) — `server/tests/unit/api/test_players_quests.py`
- **GET quests returns QuestLogResponse with entries when access allowed.** (1 connections) — `server/tests/unit/api/test_players_quests.py`

## Relationships

- [PlayerService](PlayerService.md) (5 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (4 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/tests/unit/api/test_players_quests.py`

## Audit Trail

- EXTRACTED: 32 (94%)
- INFERRED: 2 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*