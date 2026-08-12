# fixture

> 10 nodes

## Key Concepts

- **fixture** (5 connections)
- **mock_player_service()** (3 connections) — `server/tests/unit/api/test_players_quests.py`
- **mock_quest_service()** (3 connections) — `server/tests/unit/api/test_players_quests.py`
- **mock_request()** (3 connections) — `server/tests/unit/api/test_players_quests.py`
- **mock_user()** (3 connections) — `server/tests/unit/api/test_players_quests.py`
- **player_id()** (3 connections) — `server/tests/unit/api/test_players_quests.py`
- **Minimal request for endpoint (not used for quest logic).** (1 connections) — `server/tests/unit/api/test_players_quests.py`
- **Character (player) UUID.** (1 connections) — `server/tests/unit/api/test_players_quests.py`
- **PlayerService that validates character access.** (1 connections) — `server/tests/unit/api/test_players_quests.py`
- **QuestService that returns quest log entries.** (1 connections) — `server/tests/unit/api/test_players_quests.py`

## Relationships

- [PlayerService](PlayerService.md) (5 shared connections)
- [User](User.md) (1 shared connections)

## Source Files

- `server/tests/unit/api/test_players_quests.py`

## Audit Trail

- EXTRACTED: 24 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*