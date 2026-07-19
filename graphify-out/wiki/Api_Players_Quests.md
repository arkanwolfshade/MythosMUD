# Api Players Quests

> 17 nodes · cohesion 0.12

## Key Concepts

- **test_players_quests.py** (12 connections) — `server/tests/unit/api/test_players_quests.py`
- **test_get_player_quests_403_when_not_owner()** (3 connections) — `server/tests/unit/api/test_players_quests.py`
- **test_get_player_quests_include_completed_false()** (3 connections) — `server/tests/unit/api/test_players_quests.py`
- **test_get_player_quests_returns_quest_log()** (3 connections) — `server/tests/unit/api/test_players_quests.py`
- **mock_player_service()** (2 connections) — `server/tests/unit/api/test_players_quests.py`
- **mock_quest_service()** (2 connections) — `server/tests/unit/api/test_players_quests.py`
- **mock_request()** (2 connections) — `server/tests/unit/api/test_players_quests.py`
- **mock_user()** (2 connections) — `server/tests/unit/api/test_players_quests.py`
- **player_id()** (2 connections) — `server/tests/unit/api/test_players_quests.py`
- **Unit tests for GET /api/players/{player_id}/quests (quest log).  Tests get_playe** (1 connections) — `server/tests/unit/api/test_players_quests.py`
- **GET quests with include_completed=False passes to get_quest_log.** (1 connections) — `server/tests/unit/api/test_players_quests.py`
- **GET quests raises 403 when validate_character_access returns not ok.** (1 connections) — `server/tests/unit/api/test_players_quests.py`
- **Minimal request for endpoint (not used for quest logic).** (1 connections) — `server/tests/unit/api/test_players_quests.py`
- **Character (player) UUID.** (1 connections) — `server/tests/unit/api/test_players_quests.py`
- **PlayerService that validates character access.** (1 connections) — `server/tests/unit/api/test_players_quests.py`
- **QuestService that returns quest log entries.** (1 connections) — `server/tests/unit/api/test_players_quests.py`
- **GET quests returns QuestLogResponse with entries when access allowed.** (1 connections) — `server/tests/unit/api/test_players_quests.py`

## Relationships

- [[Players API Endpoints]] (4 shared connections)
- [[API Test Fixtures]] (2 shared connections)
- [[Container Exception Handlers]] (1 shared connections)

## Source Files

- `server/tests/unit/api/test_players_quests.py`

## Audit Trail

- EXTRACTED: 39 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
